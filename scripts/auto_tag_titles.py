#!/usr/bin/env python3
"""Complete catalogue coverage using explicitly low-confidence title fallback.

Only records without an abstract or repository summary are eligible.  The
result is visibly sourced as ``title_fallback`` and uses ``Unspecified`` for
facts a title cannot support, such as interaction horizon.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


GOAL_BY_SECTION = {
    "influence-negotiation": "Influence", "support-care": "Support",
    "conversational-recommendation": "Recommendation",
    "cooperation-coordination": "Coordination",
}
TYPE_BY_TITLE = [("Survey", r"survey|review"), ("Benchmark", r"benchmark"),
                 ("Dataset", r"dataset|corpus"), ("Evaluation", r"evaluat|measur")]
CAPS = {"Mental-State Modeling": r"theory of mind|\btom\b|mental state|intention|belief",
        "Affect": r"emotion|empath|affective", "Social Memory & Adaptation": r"memory|personaliz",
        "Social Context": r"norm|moral|cultur|persona|social", "Interaction Management": r"dialogue|conversation|interaction"}
CONTEXTS = {"Multi-party": r"multi.?agent|multi.?party", "Embodied": r"embodied|video|robot",
            "Culture": r"cultur", "Norms & Morality": r"norm|moral", "Personalization": r"persona|personaliz"}
APPROACHES = {"RL": r"reinforcement learning|\brl\b|policy optimization", "Planning": r"planning|planner",
              "Self-play": r"self-play", "User Simulation": r"user simulat", "Retrieval": r"retrieval"}


def labels(text: str, rules: dict[str, str]) -> list[str]:
    return [label for label, pattern in rules.items() if re.search(pattern, text, re.I)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metadata", default="metadata/papers.json")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    path = Path(args.metadata)
    payload = json.loads(path.read_text(encoding="utf-8"))
    updated = 0
    for record in payload["papers"].values():
        if record.get("review_status") != "unclassified":
            continue
        text = record["title"].lower()
        paper_type = next((kind for kind, pattern in TYPE_BY_TITLE if re.search(pattern, text, re.I)), "Method")
        goal = GOAL_BY_SECTION.get(record.get("primary_section"), "General Interaction")
        capabilities, contexts, approaches = labels(text, CAPS), labels(text, CONTEXTS), labels(text, APPROACHES)
        evidence = [{"tag": tag, "rationale": f"Title cue: '{tag}'.", "source": "title_fallback"}
                    for tag in capabilities + contexts + approaches]
        record.update({
            "type": paper_type, "goal": goal, "capabilities": capabilities, "contexts": contexts,
            "approaches": approaches, "horizon": "Unspecified",
            "field_evidence": [
                {"field": "primary_section", "rationale": "Preserved legacy browse section.", "source": "legacy README"},
                {"field": "type", "rationale": "Inferred from title wording; otherwise defaulted to Method.", "source": "title_fallback"},
                {"field": "goal", "rationale": "Inferred only from legacy primary section.", "source": "legacy README"},
                {"field": "horizon", "rationale": "No abstract or summary text is available.", "source": "title_fallback"},
            ],
            "evidence": evidence, "annotated_by": "auto-title-fallback-v1",
            "review_status": "auto_extracted", "auto_tag_version": "1.0.0-title-fallback",
            "auto_confidence": "low", "tag_text_source": "title_fallback",
        })
        updated += 1
    print(f"Would title-tag {updated} remaining records." if args.dry_run else
          f"Title-tagged {updated} remaining records.")
    if not args.dry_run:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
