#!/usr/bin/env python3
"""Fetch and cache paper abstracts for the catalogue.

Uses the original paper URL first (arXiv/ACL and other pages exposing
``citation_abstract`` metadata), then falls back to Semantic Scholar title
search.  It only enriches records with a source and timestamp; it does not
assign research keywords.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import time
from datetime import UTC, datetime
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import quote, unquote
from urllib.request import Request, urlopen
import subprocess
import tempfile


USER_AGENT = "Awesome-Social-AI metadata maintainer (research catalogue)"


def get(url: str) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/json"})
    with urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8", errors="replace")


def get_bytes(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/pdf"})
    with urlopen(request, timeout=30) as response:
        return response.read()


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", value))).strip()


CITATION_LIKE = re.compile(r"Proceedings of|Technical Papers|\(pp\.|Vol\. \d|—\s*\d{4}|"
                           r"Findings of the Association|Annual Meeting of the Association|"
                           r"Long Papers|Short Papers|\d{4}\.\s*\d{4}\.?$", re.IGNORECASE)


def is_citation_only(text: str) -> bool:
    if re.search(r"[一-鿿]", text):
        return False  # CJK prose has no spaces; the word-count heuristic does not apply
    return len(text) < 500 and (bool(CITATION_LIKE.search(text)) or len(text.split()) < 20)


def meta_abstract(page: str) -> str | None:
    """Extract common publisher metadata without assuming attribute order."""
    for tag in re.findall(r"<meta\b[^>]*>", page, flags=re.IGNORECASE):
        name = re.search(r"(?:name|property)=[\"']([^\"']+)[\"']", tag, flags=re.IGNORECASE)
        content = re.search(r"content=[\"'](.*?)[\"']", tag, flags=re.IGNORECASE | re.DOTALL)
        if not name or not content:
            continue
        key = name.group(1).lower()
        if key not in {"citation_abstract", "dc.description", "description", "og:description"}:
            continue
        candidate = clean(content.group(1))
        # Generic page descriptions can be navigation text or bare citation
        # lines; retain only sentence-like prose of meaningful length.
        if len(candidate) >= 160 and candidate.count(" ") >= 20 and not is_citation_only(candidate):
            return candidate
    for block in re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
                            page, flags=re.IGNORECASE | re.DOTALL):
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        candidates = data if isinstance(data, list) else [data]
        for item in candidates:
            description = item.get("description") if isinstance(item, dict) else None
            if isinstance(description, str):
                candidate = clean(description)
                if len(candidate) >= 160 and not is_citation_only(candidate):
                    return candidate
    return None


def direct_abstract(url: str) -> str | None:
    if not url:
        return None
    # A PDF does not expose citation metadata.  arXiv's abstract endpoint is
    # stable and carries the same canonical abstract.
    arxiv_pdf = re.search(r"https?://(?:www\.)?arxiv\.org/pdf/([^?#]+)", url)
    if arxiv_pdf:
        identifier = arxiv_pdf.group(1).removesuffix(".pdf")
        url = f"https://arxiv.org/abs/{identifier}"
    # ACL Anthology PDFs are binary; the landing page carries the abstract.
    if re.search(r"aclanthology\.org/.+\.pdf$", url):
        url = re.sub(r"\.pdf$", "/", url)
    page = get(url)
    candidate = meta_abstract(page)
    if candidate:
        return candidate
    patterns = [
        r'<blockquote[^>]+class=["\']abstract[^"\']*["\'][^>]*>(.*?)</blockquote>',
        # ACL Anthology: <div class="card-body acl-abstract"><h5>Abstract</h5><span>...</span></div>
        r'<div[^>]+class=["\'][^"\']*acl-abstract[^"\']*["\'][^>]*>(.*?)</div>',
    ]
    for pattern in patterns:
        match = re.search(pattern, page, flags=re.IGNORECASE | re.DOTALL)
        if match:
            candidate = clean(match.group(1))
            candidate = re.sub(r"^Abstract\s+", "", candidate)
            if len(candidate) >= 80:
                return candidate
    return None


def crossref_abstract(url: str) -> str | None:
    """Retrieve deposited abstracts for DOI landing pages when available."""
    match = re.search(r"(?:doi\.org/|doi:)(10\.\d{4,9}/[^?#\s]+)", url, flags=re.IGNORECASE)
    if not match:
        return None
    doi = unquote(match.group(1)).rstrip(".,;:)")
    payload = json.loads(get("https://api.crossref.org/works/" + quote(doi, safe="")))
    abstract = payload.get("message", {}).get("abstract")
    candidate = clean(abstract) if isinstance(abstract, str) else ""
    return candidate if len(candidate) >= 80 else None


def semantic_scholar_abstract(title: str, year: int) -> str | None:
    # Semantic Scholar relevance search treats hyphenated query terms poorly.
    query = re.sub(r"[-–—]", " ", title)
    url = ("https://api.semanticscholar.org/graph/v1/paper/search?limit=3&fields="
           "title,abstract,year&year=" + str(year) + "&query=" + quote(query))
    payload = json.loads(get(url))
    for paper in payload.get("data", []):
        candidate_title, abstract = paper.get("title") or "", paper.get("abstract")
        similarity = SequenceMatcher(None, query.lower(), re.sub(r"[-–—]", " ", candidate_title.lower())).ratio()
        if abstract and similarity >= 0.72:
            return clean(abstract)
    return None


def crossref_title_abstract(title: str, year: int) -> str | None:
    """Find a DOI record with a deposited abstract when no DOI was stored."""
    url = "https://api.crossref.org/works?rows=3&select=title,abstract,published&query.title=" + quote(title)
    payload = json.loads(get(url))
    query = re.sub(r"[-–—]", " ", title.lower())
    for work in payload.get("message", {}).get("items", []):
        candidate_title = " ".join(work.get("title") or [])
        similarity = SequenceMatcher(None, query, re.sub(r"[-–—]", " ", candidate_title.lower())).ratio()
        abstract = work.get("abstract")
        if similarity >= 0.80 and isinstance(abstract, str):
            candidate = clean(abstract)
            if len(candidate) >= 80:
                return candidate
    return None


def openalex_abstract(title: str) -> str | None:
    """Query OpenAlex and reconstruct its positional abstract index."""
    url = "https://api.openalex.org/works?per-page=3&search=" + quote(title)
    payload = json.loads(get(url))
    for work in payload.get("results", []):
        candidate_title = work.get("title") or ""
        similarity = SequenceMatcher(None, title.lower(), candidate_title.lower()).ratio()
        index = work.get("abstract_inverted_index") or {}
        if similarity < 0.72 or not index:
            continue
        positions = {position: word for word, values in index.items() for position in values}
        abstract = " ".join(positions[position] for position in sorted(positions))
        if len(abstract) >= 80:
            return clean(abstract)
    return None


def openalex_oa_pdf_abstract(title: str) -> str | None:
    """Extract an abstract from the first page of a verified OA PDF, if any."""
    url = "https://api.openalex.org/works?per-page=3&search=" + quote(title)
    payload = json.loads(get(url))
    query = re.sub(r"[-–—]", " ", title.lower())
    for work in payload.get("results", []):
        candidate_title = work.get("title") or ""
        similarity = SequenceMatcher(None, query, re.sub(r"[-–—]", " ", candidate_title.lower())).ratio()
        location = work.get("best_oa_location") or {}
        pdf_url = location.get("pdf_url") if work.get("open_access", {}).get("is_oa") else None
        if similarity < 0.80 or not pdf_url:
            continue
        with tempfile.NamedTemporaryFile(suffix=".pdf") as handle:
            handle.write(get_bytes(pdf_url))
            handle.flush()
            extracted = subprocess.run(["pdftotext", "-f", "1", "-l", "1", handle.name, "-"],
                                       text=True, capture_output=True, timeout=30, check=False).stdout
        match = re.search(r"\babstract\b\s*[:.]?\s*(.{100,3500}?)(?=\b(?:keywords?|introduction|1\s*[. ]+introduction)\b|\Z)",
                          extracted, flags=re.IGNORECASE | re.DOTALL)
        if match:
            candidate = clean(match.group(1))
            if len(candidate) >= 100:
                return candidate
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metadata", default="metadata/papers.json")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--retry-failed", action="store_true",
                        help="retry records previously unavailable from configured sources")
    parser.add_argument("--only-title-fallback", action="store_true",
                        help="only retrieve records currently tagged from title fallback")
    parser.add_argument("--refetch-citation-only", action="store_true",
                        help="refetch records whose cached abstract is a short citation line rather than prose")
    args = parser.parse_args()

    path = Path(args.metadata)
    payload = json.loads(path.read_text(encoding="utf-8"))
    pending = [(paper_id, record) for paper_id, record in payload["papers"].items()
               if (not record.get("abstract") or
                   (args.refetch_citation_only and is_citation_only(record.get("abstract") or ""))) and
               (args.retry_failed or not record.get("abstract_fetch_attempted_at")) and
               (not args.only_title_fallback or record.get("tag_text_source") == "title_fallback")][:args.limit]
    fetched = failed = 0
    for paper_id, record in pending:
        abstract = source = None
        try:
            abstract = direct_abstract(record.get("paper_url") or "")
            source = record.get("paper_url") if abstract else None
        except Exception:
            abstract = None
        if not abstract:
            try:
                abstract = crossref_abstract(record.get("paper_url") or "")
                source = "https://api.crossref.org/works" if abstract else None
            except Exception:
                abstract = None
        if not abstract:
            try:
                abstract = semantic_scholar_abstract(record["title"], record["year"])
                source = "https://api.semanticscholar.org/graph/v1/paper/search" if abstract else None
            except Exception:
                abstract = None
        if not abstract:
            try:
                abstract = crossref_title_abstract(record["title"], record["year"])
                source = "https://api.crossref.org/works?query.title" if abstract else None
            except Exception:
                abstract = None
        if not abstract:
            try:
                abstract = openalex_abstract(record["title"])
                source = "https://api.openalex.org/works" if abstract else None
            except Exception:
                abstract = None
        if not abstract:
            try:
                abstract = openalex_oa_pdf_abstract(record["title"])
                source = "https://api.openalex.org/works (OA PDF)" if abstract else None
            except Exception:
                abstract = None
        record["abstract_fetch_attempted_at"] = datetime.now(UTC).date().isoformat()
        if abstract:
            record["abstract"] = abstract
            record["abstract_source"] = source
            record["abstract_retrieved_at"] = datetime.now(UTC).date().isoformat()
            fetched += 1
        else:
            record["abstract_fetch_error"] = "unavailable_from_configured_sources"
            failed += 1
        time.sleep(0.35)
    print(f"Fetched {fetched}/{len(pending)} abstracts; {failed} unavailable.")
    if not args.dry_run:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
