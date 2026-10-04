#!/usr/bin/env python3
"""Classify catalogue records with an Anthropic-compatible LLM endpoint (v2).

The caller must opt into network calls and writes with ``--write``.  Results
are accepted only when every model-supplied evidence quote is located in the
cached source text: preferably via the model's own character offsets
(``source[start:end] == evidence``), falling back to a normalized substring
check.  ``horizon: Unspecified`` is the only label allowed without evidence.

Facet rules in the prompt implement the narrowed `Social Context` definition
from metadata/KEYWORDS.md: tag it only when the model explicitly represents,
infers, or uses social context to change reasoning/decisions; roles, culture
and norms as mere study conditions belong in `contexts` only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import http.client
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


V2_MARKER = "llm-abstract-extractor-v2"

VALUES = {
    "type": {"System", "Method", "Dataset", "Benchmark", "Evaluation", "Survey"},
    "goal": {"Influence", "Support", "Recommendation", "Coordination", "General Interaction"},
    "horizon": {"Single-turn", "Multi-turn", "Longitudinal", "Unspecified"},
    "capabilities": {"Social Perception", "Affect", "Mental-State Modeling", "Social Context", "Interaction Management", "Social Memory & Adaptation"},
    "contexts": {"Personalization", "Relationship & Role", "Norms & Morality", "Culture", "Multi-party", "Embodied"},
    "approaches": {"Supervised Learning", "Retrieval", "Planning", "RL", "Preference Optimization", "Reward Modeling", "Self-play", "User Simulation"},
}
MULTI = ("capabilities", "contexts", "approaches")

FACET_RULES = """FACET RULES:
- type is the paper's PRIMARY contribution. A new model, algorithm, training framework, or planning architecture is Method even if the paper evaluates it. Select Evaluation only when the main contribution is a measurement protocol, evaluation framework, comparative analysis, or study. Dataset/Benchmark only when the contribution is a reusable data or test resource.
- goal is the primary social interaction objective. General Interaction is NOT a fallback: use it only when no specific social goal (Influence, Support, Recommendation, Coordination) dominates.
- horizon: tag Single-turn/Multi-turn/Longitudinal only when SOURCE explicitly establishes the interaction duration (e.g. "multi-turn", "multiple rounds", "across sessions", "long-term"). Otherwise use Unspecified. Do not infer Multi-turn merely from the paper being about dialogue.
- capabilities describe what the model can do or reason about; contexts describe the setting where the problem lives.
- capabilities.Social Context is narrow: tag it only when the model explicitly represents, infers, or uses social context (roles, relationships, group structure, common ground, culture, norms) to change its reasoning or decisions. When roles/culture/norms are merely the study setting, dataset design, or application condition (e.g. personas in a benchmark, a corpus collected in one culture), tag the matching contexts (Relationship & Role, Culture, Norms & Morality) and NOT Social Context.
- approaches: tag only core training/inference mechanisms. Do not tag Supervised Learning merely because a classifier or fine-tuning is used somewhere; reserve it for work centered on supervised training.
- Never select a label without supporting source text."""


TRANS = str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'", "–": "-", "—": "-"})


def normal(text: str) -> str:
    text = text.casefold().translate(TRANS)
    return re.sub(r"\s+", " ", text).strip()


def locate(source_text: str, quote: str) -> list[int] | None:
    """Locate quote in source (case-insensitive, Unicode-normalized).

    Transliteration is 1:1 in length, so indices in the translated text equal
    indices in the original. Returns None when the quote spans a
    whitespace-normalization boundary.
    """
    if not source_text or not quote:
        return None
    match = re.search(re.escape(quote.translate(TRANS)), source_text.translate(TRANS), re.IGNORECASE)
    if match:
        return [match.start(), match.end()]
    return None


CITATION_LIKE = re.compile(r"Proceedings of|Technical Papers|\(pp\.|Vol\. \d|—\s*\d{4}|"
                           r"Findings of the Association|Annual Meeting of the Association|"
                           r"Long Papers|Short Papers|\d{4}\.\s*\d{4}\.?$", re.IGNORECASE)


def is_citation_only(text: str) -> bool:
    if re.search(r"[一-鿿]", text):
        return False  # CJK prose has no spaces; the word-count heuristic does not apply
    return len(text) < 500 and (bool(CITATION_LIKE.search(text)) or len(text.split()) < 20)


def source_for(record: dict) -> tuple[str, str, str | None]:
    abstract = record.get("abstract") or ""
    tag_text = record.get("tag_text") or ""
    # Citation lines are bibliographic, not prose: prefer real notes over them.
    if abstract and not is_citation_only(abstract):
        return abstract, "abstract", record.get("abstract_source")
    if tag_text:
        return tag_text, record.get("tag_text_source", "recorded_text"), record.get("tag_text_url")
    return abstract, "abstract", record.get("abstract_source")


def prompt(record: dict, text: str, source_type: str, source_url: str | None) -> str:
    taxonomy = "\n".join(f"- {key}: {', '.join(sorted(values))}" for key, values in VALUES.items())
    return f'''You are annotating a Social AI research catalogue. Read only the supplied source text.
Choose labels only from the closed vocabulary below. Do not use title or outside knowledge.

{FACET_RULES}

VOCABULARY:
{taxonomy}

TITLE (context only; do not use for decisions): {record['title']}
SOURCE TYPE: {source_type}
SOURCE URL: {source_url or 'not recorded'}
SOURCE:
{text}

For every selected label, provide `evidence` as a SHORT (3-12 word) EXACT contiguous substring of SOURCE, copied character-for-character with no paraphrase, merging, splicing, or ellipsis, plus its 0-based character offsets `start` and `end` such that SOURCE[start:end] equals evidence exactly. For horizon Unspecified, set value "Unspecified", evidence "" and start/end null.

Return JSON only:
{{
  "type": {{"value": "...", "evidence": "exact quote", "start": 0, "end": 10}},
  "goal": {{"value": "...", "evidence": "exact quote", "start": 0, "end": 10}},
  "horizon": {{"value": "Unspecified", "evidence": "", "start": null, "end": null}},
  "capabilities": [{{"value": "...", "evidence": "exact quote", "start": 0, "end": 10}}],
  "contexts": [{{"value": "...", "evidence": "exact quote", "start": 0, "end": 10}}],
  "approaches": [{{"value": "...", "evidence": "exact quote", "start": 0, "end": 10}}]
}}'''


def extract_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.I)
    return json.loads(text)


def check_evidence(item: dict, source_text: str, label: str) -> None:
    evidence = item.get("evidence")
    if not isinstance(evidence, str) or not normal(evidence):
        raise ValueError(f"empty {label} evidence")
    start, end = item.get("start"), item.get("end")
    if isinstance(start, int) and isinstance(end, int) and 0 <= start <= end <= len(source_text):
        if normal(source_text[start:end]) == normal(evidence):
            return
    if normal(evidence) in normal(source_text):
        return
    raise ValueError(f"unverifiable {label} evidence {evidence[:80]!r} does not appear in SOURCE")


def validate(result: dict, source_text: str) -> None:
    for field in ("type", "goal", "horizon"):
        item = result.get(field)
        if not isinstance(item, dict) or item.get("value") not in VALUES[field]:
            raise ValueError(f"invalid {field}")
        if field == "horizon" and item["value"] == "Unspecified":
            continue
        check_evidence(item, source_text, field)
    for field in MULTI:
        items = result.get(field)
        if not isinstance(items, list):
            raise ValueError(f"invalid {field}")
        seen = set()
        for item in items:
            if not isinstance(item, dict) or item.get("value") not in VALUES[field] or item["value"] in seen:
                raise ValueError(f"invalid {field} label")
            check_evidence(item, source_text, field)
            seen.add(item["value"])


def call(base_url: str, token: str, model: str, user_prompt: str, max_tokens: int, reasoning_effort: str,
         followup: tuple[str, str] | None = None) -> str:
    """Return the assistant's raw text block (not parsed)."""
    url = base_url.rstrip("/") + "/v1/messages"
    messages = [{"role": "user", "content": user_prompt}]
    if followup is not None:
        messages += [{"role": "assistant", "content": followup[0]},
                     {"role": "user", "content": followup[1]}]
    request_body = {
        "model": model, "max_tokens": max_tokens, "temperature": 0,
        "reasoning": {"effort": reasoning_effort},
        "system": "Return only valid JSON. Never invent evidence.",
        "messages": messages,
    }
    if reasoning_effort == "none":
        request_body["thinking"] = {"type": "disabled"}
    body = json.dumps(request_body).encode()
    request = urllib.request.Request(url, data=body, headers={
        "content-type": "application/json", "x-api-key": token,
        "anthropic-version": "2023-06-01",
    })
    with urllib.request.urlopen(request, timeout=90) as response:
        payload = json.load(response)
    content = payload.get("content", [])
    text_block = next((item for item in content if item.get("type") == "text"), None) if isinstance(content, list) else None
    if not text_block:
        block_types = [item.get("type", "unknown") for item in content] if isinstance(content, list) else []
        raise ValueError(f"response contains no Anthropic text block; keys={sorted(payload)} content_types={block_types}")
    return text_block["text"]


def offset_of(item: dict, source_text: str) -> list[int] | None:
    # Never trust model offsets blindly: locate the quote ourselves so the
    # recorded offset always slices the source to the evidence.
    return locate(source_text, item.get("evidence", ""))


def apply(record: dict, result: dict, source_text: str, source_type: str, source_url: str | None, model: str) -> None:
    field_evidence = [
        {"field": "primary_section", "rationale": "Preserved legacy browse section during LLM reclassification.", "source": "legacy README"},
    ]
    for field in ("type", "goal", "horizon"):
        item = result[field]
        if field == "horizon" and item["value"] == "Unspecified":
            field_evidence.append({"field": field, "source": source_type,
                                   "rationale": "No explicit interaction-duration evidence in source; conservative default."})
        else:
            entry = {"field": field, "source": source_type,
                     "rationale": f"Source quote: '{item.get('evidence', '')}'."}
            if (offsets := offset_of(item, source_text)) is not None:
                entry["quote_offset"] = offsets
            field_evidence.append(entry)
    multi_evidence = []
    for field in MULTI:
        for item in result[field]:
            entry = {"tag": item["value"], "source": source_type,
                     "rationale": f"Source quote: '{item['evidence']}'."}
            if (offsets := offset_of(item, source_text)) is not None:
                entry["quote_offset"] = offsets
            multi_evidence.append(entry)
    record.update({
        "type": result["type"]["value"], "goal": result["goal"]["value"],
        "horizon": result["horizon"]["value"],
        **{field: [item["value"] for item in result[field]] for field in MULTI},
        "review_status": "auto_extracted", "annotated_by": V2_MARKER,
        "llm_tagging": {"model": model, "source_type": source_type, "source_url": source_url,
                        "tagged_at": dt.date.today().isoformat()},
        "field_evidence": field_evidence,
        "evidence": multi_evidence,
    })


def classify(task: tuple[str, dict], base_url: str, token: str, model: str, max_tokens: int,
             reasoning_effort: str) -> tuple[str, dict, str, str, str | None, dict | None, Exception | None]:
    paper_id, record = task
    try:
        text, source_type, source_url = source_for(record)
        if is_citation_only(text) or len(normal(text)) < 60:
            raise ValueError("insufficient source text for evidence extraction")
        user_prompt = prompt(record, text, source_type, source_url)
        raw = call(base_url, token, model, user_prompt, max_tokens, reasoning_effort)
        try:
            result = extract_json(raw)
            validate(result, text)
        except (ValueError, json.JSONDecodeError) as error:
            correction = (
                f"Your previous response was rejected: {error}. Return ONLY the corrected JSON. "
                "Evidence MUST come from the SOURCE text shown above; never use title words or outside knowledge. "
                "Copy every evidence as a SHORT (3-12 word) contiguous span of SOURCE, character-for-character. "
                "Never merge, splice, paraphrase, or use ellipsis. Label values must match VOCABULARY exactly. "
                "Horizon Unspecified uses evidence \"\". Use [] when no label fits."
            )
            raw = call(base_url, token, model, user_prompt, max_tokens, reasoning_effort, followup=(raw, correction))
            result = extract_json(raw)
            validate(result, text)
        return paper_id, record, text, source_type, source_url, result, None
    except (ValueError, KeyError, json.JSONDecodeError, OSError, http.client.HTTPException) as error:
        return paper_id, record, "", "", None, None, error


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metadata", default="metadata/papers.json")
    parser.add_argument("--base-url", default=os.getenv("ANTHROPIC_BASE_URL", ""))
    parser.add_argument("--model", default=os.getenv("ANTHROPIC_MODEL", ""))
    parser.add_argument("--limit", type=int, default=214)
    parser.add_argument("--write", action="store_true", help="permit external API calls and metadata writes")
    parser.add_argument("--resume", action="store_true", help="skip records already annotated by this extractor version")
    parser.add_argument("--skip-annotated-by", default="", help="comma-separated annotated_by values to exclude")
    parser.add_argument("--only-with-capability", default="", help="only re-tag records whose capabilities contain this tag")
    parser.add_argument("--pause", type=float, default=0.2, help="seconds between requests (single worker only)")
    parser.add_argument("--workers", type=int, default=1, help="concurrent API requests (default: 1)")
    parser.add_argument("--max-tokens", type=int, default=3000)
    parser.add_argument("--reasoning-effort", choices=("none", "low", "high", "max"), default="none")
    args = parser.parse_args()
    payload = json.loads(Path(args.metadata).read_text(encoding="utf-8"))
    skip = {value for value in args.skip_annotated_by.split(",") if value}
    if args.resume:
        skip.add(V2_MARKER)
    candidates = [
        (paper_id, record) for paper_id, record in payload["papers"].items()
        if (record.get("abstract") or record.get("tag_text"))
        and record.get("annotated_by") not in skip
        and (not args.only_with_capability or args.only_with_capability in record.get("capabilities", []))
    ][:args.limit]
    print(f"Candidates: {len(candidates)}; model: {args.model or 'NOT CONFIGURED'}; endpoint: {args.base_url or 'NOT CONFIGURED'}"
          + (f"; capability filter: {args.only_with_capability}" if args.only_with_capability else ""))
    if not args.write:
        print("Dry run only. Pass --write to make API calls and update metadata.")
        return
    token = os.getenv("ANTHROPIC_AUTH_TOKEN")
    if not token or not args.base_url or not args.model:
        raise SystemExit("ANTHROPIC_AUTH_TOKEN, ANTHROPIC_BASE_URL, and ANTHROPIC_MODEL must be configured.")
    if args.workers < 1:
        raise SystemExit("--workers must be positive")
    accepted = rejected = completed = 0
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(classify, task, args.base_url, token, args.model, args.max_tokens,
                                   args.reasoning_effort) for task in candidates]
        for future in as_completed(futures):
            paper_id, record, source_text, source_type, source_url, result, error = future.result()
            completed += 1
            if error is None:
                apply(record, result, source_text, source_type, source_url, args.model)
                record.pop("llm_tagging_error", None)
                accepted += 1
                print(f"[{completed}/{len(candidates)}] accepted {paper_id}")
            else:
                rejected += 1
                record["llm_tagging_error"] = {
                    "model": args.model, "rejected_at": dt.date.today().isoformat(), "reason": str(error),
                }
                print(f"[{completed}/{len(candidates)}] rejected {paper_id}: {error}", file=sys.stderr)
            # Writes are deliberately serialized: workers never mutate the catalogue.
            Path(args.metadata).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            if args.workers == 1:
                time.sleep(args.pause)
    print(f"Accepted: {accepted}; rejected: {rejected}")


if __name__ == "__main__":
    main()
