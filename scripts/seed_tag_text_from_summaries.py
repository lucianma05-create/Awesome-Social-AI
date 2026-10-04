#!/usr/bin/env python3
"""Use existing repository one-sentence summaries as a disclosed tag-text fallback."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def summary_text(path: Path) -> str | None:
    content = path.read_text(encoding="utf-8")
    match = re.search(r"^## 一句话总结[^\n]*\n(.*?)(?=^## |\Z)", content, re.MULTILINE | re.DOTALL)
    if not match:
        return None
    text = re.sub(r"!\[[^]]*\]\([^)]*\)", "", match.group(1))
    text = re.sub(r"[`>*#]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) >= 20 else None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metadata", default="metadata/papers.json")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    metadata = Path(args.metadata)
    payload = json.loads(metadata.read_text(encoding="utf-8"))
    added = 0
    for record in payload["papers"].values():
        if record.get("abstract") or record.get("tag_text") or not record.get("summary_path"):
            continue
        source_path = Path(record["summary_path"])
        if not source_path.is_file():
            continue
        text = summary_text(source_path)
        if text:
            record["tag_text"] = text
            record["tag_text_source"] = "repository_summary"
            added += 1
    print(f"Would add {added} repository-summary tag texts." if args.dry_run else
          f"Added {added} repository-summary tag texts.")
    if not args.dry_run:
        metadata.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
