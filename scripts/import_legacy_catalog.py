#!/usr/bin/env python3
"""Import legacy README paper rows as unclassified catalogue records.

This importer deliberately transfers bibliographic fields only.  It never
guesses social-AI keywords from titles, and it preserves already curated
records in metadata/papers.json.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote


SECTION_BY_ANCHOR = {
    "pd": "influence-negotiation",
    "ed": "support-care",
    "recommend": "conversational-recommendation",
    "coop": "cooperation-coordination",
    "tom": "mental-state-modeling",
    "emotion": "affect-social-perception",
    "norms": "social-context-norms-morality",
    "memory": "social-memory-adaptation",
    "rlhf": "learning-planning-alignment",
    "us": "user-simulation-environments",
    "data": "datasets-benchmarks-evaluation",
}
LINK_RE = re.compile(r"\[[^]]+\]\(([^)]+)\)")
ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')


def link_or_none(cell: str) -> str | None:
    match = LINK_RE.search(cell)
    if not match or match.group(1) == "-":
        return None
    url = unquote(match.group(1))
    # Older rows sometimes link to the repository's GitHub blob rather than
    # the same local summary.  Keep metadata portable by canonicalizing it.
    if "/paper/" in url and "github.com/" in url:
        return "paper/" + url.split("/paper/", 1)[1]
    return url


def make_id(title: str, year: int, existing: set[str]) -> str:
    normalized = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    stem = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")[:70].strip("-")
    candidate = f"{stem}-{year}" if stem else f"paper-{year}"
    number = 2
    unique = candidate
    while unique in existing:
        unique = f"{candidate}-{number}"
        number += 1
    return unique


def fingerprint(title: str, year: int, venue: str) -> tuple[str, int, str]:
    """Compare records despite legacy hyphen/colon punctuation variants."""
    normalized_title = re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()
    return normalized_title, year, venue.strip().lower()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", default="README.md")
    parser.add_argument("--metadata", default="metadata/papers.json")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--normalize-ids", action="store_true",
                        help="normalize existing legacy IDs before importing")
    args = parser.parse_args()

    payload = json.loads(Path(args.metadata).read_text(encoding="utf-8"))
    records = payload["papers"]
    if args.normalize_ids:
        normalized_records = {}
        for record_id, record in records.items():
            normalized_id = re.sub(r"-+", "-", record_id).strip("-")
            if normalized_id in normalized_records:
                raise ValueError(f"ID collision while normalizing {record_id!r}")
            normalized_records[normalized_id] = record
        payload["papers"] = normalized_records
        records = normalized_records
    known = {fingerprint(r.get("title", ""), r.get("year"), r.get("venue", ""))
             for r in records.values() if isinstance(r, dict)}
    anchor = None
    added = 0
    for line in Path(args.readme).read_text(encoding="utf-8").splitlines():
        anchor_match = ANCHOR_RE.fullmatch(line.strip())
        if anchor_match:
            anchor = anchor_match.group(1)
            continue
        if anchor not in SECTION_BY_ANCHOR or not re.match(r"^\| \d{4} \|", line):
            continue
        cells = line.split("|")[1:-1]
        if len(cells) != 6:
            continue
        year_text, venue, title, paper, summary, code = (cell.strip() for cell in cells)
        paper_fingerprint = fingerprint(title, int(year_text), venue)
        if paper_fingerprint in known:
            continue
        record_id = make_id(title, int(year_text), set(records))
        records[record_id] = {
            "title": title,
            "year": int(year_text),
            "venue": venue,
            "paper_url": link_or_none(paper),
            "code_url": link_or_none(code),
            "summary_path": link_or_none(summary),
            "primary_section": SECTION_BY_ANCHOR[anchor],
            "review_status": "unclassified"
        }
        known.add(paper_fingerprint)
        added += 1

    print(f"Would add {added} unclassified catalogue records." if args.dry_run else
          f"Added {added} unclassified catalogue records.")
    if not args.dry_run:
        Path(args.metadata).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
