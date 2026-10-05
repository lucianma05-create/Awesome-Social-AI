#!/usr/bin/env python3
"""Render Awesome-RLHF-style README paper entries from metadata/papers.json."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import quote


SECTION_ORDER = [
    ("pd", "influence-negotiation"), ("ed", "support-care"),
    ("recommend", "conversational-recommendation"), ("coop", "cooperation-coordination"),
    ("tom", "mental-state-modeling"), ("emotion", "affect-social-perception"),
    ("norms", "social-context-norms-morality"), ("memory", "social-memory-adaptation"),
    ("rlhf", "learning-planning-alignment"), ("us", "user-simulation-environments"),
    ("data", "datasets-benchmarks-evaluation"),
]


def link(label: str, url: str | None) -> str:
    return f"[{label}]({url})" if url else "-"


def keywords(record: dict) -> str:
    parts = [record["type"], record["goal"]]
    parts.extend(record["capabilities"])
    parts.extend(record["contexts"])
    parts.extend(record["approaches"])
    if record["horizon"] != "Unspecified":
        parts.append(record["horizon"])
    return " · ".join(f"`{part}`" for part in parts)


def has_local_note(record: dict) -> bool:
    path = record.get("summary_path")
    return bool(path and Path(path).exists())


def entry(record: dict) -> str:
    title = record["title"].replace("]", "\\]")
    paper = link(title, record.get("paper_url")) if record.get("paper_url") else title
    fields = []
    if record.get("venue") and record["venue"] != "-":
        fields.append(f"  - Publisher: `{record['venue']} {record['year']}`")
    if record.get("type") and record.get("goal"):
        fields.append(f"  - Keywords: {keywords(record)}")
    if record.get("code_url"):
        fields.append(f"  - Code: {link('GitHub / Project', record['code_url'])}")
    if has_local_note(record):
        fields.append(f"  - Summary: {link('Summary', quote(record['summary_path'], safe='/:'))}")
    return f"- {paper}\n" + "\n".join(fields) + "\n"


def replace_section(text: str, anchor: str, records: list[dict]) -> str:
    start = text.index(f'<a id="{anchor}"></a>')
    end = text.index("</details>", start)
    block = text[start:end]
    header_match = re.search(r"<summary>(.*?) · \d+ (篇|papers)</summary>", block)
    if not header_match:
        raise ValueError(f"missing count summary for {anchor}")
    unit = header_match.group(2)
    block = block[:header_match.start()] + f"<summary>{header_match.group(1)} · {len(records)} {unit}</summary>" + block[header_match.end():]
    marker_start = "<!-- CATALOGUE:START -->"
    marker_end = "<!-- CATALOGUE:END -->"
    rendered = marker_start + "\n" + "".join(entry(record) for record in records) + marker_end + "\n"
    if marker_start in block:
        content_start = block.index(marker_start)
        content_end = block.index(marker_end, content_start) + len(marker_end)
        block = block[:content_start] + rendered + block[content_end:]
    else:
        table_start = block.find("| Year |")
        if table_start < 0:
            table_start = block.index("| 年份 |")
        block = block[:table_start] + rendered
    return text[:start] + block + text[end:]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", default=None,
                        help="render only this file (default: README.md and README_CN.md when present)")
    parser.add_argument("--metadata", default="metadata/papers.json")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    targets = [Path(args.readme)] if args.readme else [p for p in (Path("README.md"), Path("README_CN.md")) if p.exists()]
    records = json.loads(Path(args.metadata).read_text(encoding="utf-8"))["papers"].values()
    linked = sum(1 for record in records if has_local_note(record))
    for readme_path in targets:
        text = readme_path.read_text(encoding="utf-8")
        for anchor, section in reversed(SECTION_ORDER):
            section_records = sorted((record for record in records if record.get("primary_section") == section),
                                     key=lambda record: (record["year"], record["title"].lower()))
            text = replace_section(text, anchor, section_records)
        text = re.sub(r"Papers-\d+-", f"Papers-{len(records)}-", text, count=1)
        text = re.sub(r"Summaries-\d+-", f"Summaries-{linked}-", text, count=1)
        if args.dry_run:
            print(f"Would render 11 README sections from {len(records):d} catalogue records into {readme_path}.")
        else:
            readme_path.write_text(text, encoding="utf-8")
            print(f"Rendered 11 README sections from {len(records):d} catalogue records into {readme_path}.")


if __name__ == "__main__":
    main()
