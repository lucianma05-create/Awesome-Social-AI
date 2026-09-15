#!/usr/bin/env python3
"""
update_readme.py - Automatically update README.md based on new paper .md files.

Scans the paper/ directory for .md files not yet referenced in README.md,
parses filenames and paper content, then inserts new rows into the correct
section's table sorted by year.

Usage:
    python update_readme.py [--dry-run] [--readme PATH] [--paper-dir PATH]
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import Optional
from urllib.parse import unquote


# Direction prefix → README section heading (the ### heading line text)
DIRECTION_MAP = {
    "Data":      "Data：Benchmark & Evaluation",
    "ED":        "ED：Empathetic Dialogue Systems",
    "Memory":    "Memory：Agent Memory",
    "PD":        "PD：Persuasion & Negotiation",
    "Recommend": "Recommend：Recommender Systems",
    "Recommned": "Recommend：Recommender Systems",
    "Recommeend":"Recommend：Recommender Systems",
    "RLHF":      "RLHF：RL & Alignment",
    "ToM":       "ToM：Theory of Mind",
    "US":        "US：User Simulator",
}

# Canonical direction label to use in table entries (for dedup)
CANONICAL_DIRECTION = {
    "Data":       "Data",
    "ED":         "ED",
    "Memory":     "Memory",
    "PD":         "PD",
    "Recommend":  "Recommend",
    "Recommned":  "Recommend",
    "Recommeend": "Recommend",
    "RLHF":       "RLHF",
    "ToM":        "ToM",
    "US":         "US",
}


def parse_filename(filename: str) -> Optional[dict]:
    """
    Parse a paper filename into components.

    Format: [方向]-[会议/期刊名]-[年份]-[论文名].md
    Combined prefixes: ToM+Data, PD+RLHF, etc.
    → "Data" wins for combined prefixes (benchmark papers such as
      ToM+Data belong to the Benchmark & Evaluation section per the
      README convention); otherwise use the first known prefix.

    Returns dict with keys: direction, canonical_dir, venue, year, title, filepath
    """
    name = filename.replace(".md", "").strip()
    parts = name.split("-", 3)  # Split into at most 4 parts
    if len(parts) < 4:
        return None

    raw_direction, venue, year_str, title = parts
    year_str = year_str.strip()

    # Validate year
    if not year_str.isdigit():
        return None
    year = int(year_str)

    # Handle combined prefixes like "ToM+Data" or "ToM+Recommend+Data"
    direction_parts = raw_direction.split("+")
    parts_list = [p.strip() for p in direction_parts]

    direction_key = None
    # "Data" wins: benchmark/dataset papers are listed under
    # Data：Benchmark & Evaluation regardless of the leading prefix
    if any(p.lower() == "data" for p in parts_list):
        direction_key = "Data"
    else:
        for part in parts_list:
            if part in CANONICAL_DIRECTION:
                direction_key = part
                break
            # Case-insensitive fallback
            for known in CANONICAL_DIRECTION:
                if known.lower() == part.lower():
                    direction_key = known
                    break
            if direction_key:
                break

    if direction_key is None:
        return None

    return {
        "direction": raw_direction,
        "canonical_dir": CANONICAL_DIRECTION[direction_key],
        "venue": venue.strip(),
        "year": year,
        "title": title.strip().replace("_", " "),
        "filepath": f"paper/{filename}",
    }


def extract_urls(filepath: str) -> tuple:
    """
    Extract paper link and code link from a paper .md file.

    Tries three strategies in order:
    1. Standard markdown link format: *字段：[text](url)*
    2. Bare URL format: *字段：https://...* (no markdown link wrapper)
    3. Full-text fallback: search entire file for known URL patterns

    Returns (link_url, code_url). Each is a string URL or "-" if absent.
    """
    link_url = "-"
    code_url = "-"

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (FileNotFoundError, UnicodeDecodeError):
        return link_url, code_url

    # ── Strategy 1: Markdown link format ──────────────────────────
    # *论文下载地址（可选）：[text](url)*  or  *论文下载地址：[text](url)*
    paper_md = re.search(
        r"\*论文下载地址(?:[（(]可选[）)])?[：:]\s*\[.*?\]\((https?://[^\s\)]+)\)",
        content
    )
    if paper_md:
        link_url = paper_md.group(1)

    # *代码是否开源：是 [text](url)*  or  *代码是否开源：否 [text](url)*
    code_md = re.search(
        r"\*代码是否开源[：:].*?\[.*?\]\((https?://[^\s\)]+)\)",
        content
    )
    if code_md:
        code_url = code_md.group(1)

    # ── Strategy 2: Bare URL format (no markdown link wrapper) ────
    # *论文下载地址：https://arxiv.org/...*  or  *论文下载地址（可选）：https://...*
    if link_url == "-":
        paper_bare = re.search(
            r"\*论文下载地址(?:[（(]可选[）)])?[：:]\s*(https?://[^\s\*]+?)(?:\*)?$",
            content, re.MULTILINE
        )
        if paper_bare:
            candidate = paper_bare.group(1).rstrip("*").strip()
            if candidate and candidate != "未提及":
                link_url = candidate

    # *代码是否开源：是 https://github.com/...*
    if code_url == "-":
        code_bare = re.search(
            r"\*代码是否开源[：:]\s*(?:是|否)?\s*(https?://[^\s\*]+?)(?:\*)?$",
            content, re.MULTILINE
        )
        if code_bare:
            candidate = code_bare.group(1).rstrip("*").strip()
            if candidate and candidate != "未提及":
                code_url = candidate

    # ── Strategy 3: Full-text fallback search ─────────────────────
    # When both strategies above failed, scan the entire file for
    # URLs from known academic / code-hosting domains.
    if link_url == "-":
        link_url = _fallback_search(content, [
            "arxiv.org", "aclanthology.org", "doi.org",
            "nature.com", "science.org", "dl.acm.org",
            "ieeexplore.ieee.org", "ojs.aaai.org",
            "proceedings.neurips.cc", "openreview.net",
            "semanticscholar.org", "researchgate.net",
        ])

    if code_url == "-":
        code_url = _fallback_search(content, [
            "github.com", "gitlab.com", "huggingface.co",
            "bitbucket.org",
        ])

    return link_url, code_url


def _fallback_search(content: str, domains: list) -> str:
    """
    Search the full text for URLs matching any of the given domains.
    Returns the first match, or "-" if none found.
    """
    # Build a regex that matches any URL containing one of the domains
    pattern = r"https?://[^\s\)\]\*]+"
    all_urls = re.findall(pattern, content)
    for url in all_urls:
        url = url.rstrip(".*,;:")  # clean trailing punctuation
        for domain in domains:
            if domain in url:
                return url
    return "-"


def extract_paper_title(filepath: str) -> str:
    """
    Extract the paper title from the first heading in the .md file.
    Falls back to the filename-derived title.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    # Remove the leading "# " and any direction-venue-year prefix
                    title = line[2:].strip()
                    # Try to strip the prefix like "ED-未提及-2025-"
                    title = re.sub(r"^[A-Za-z+]+-[^-]+-\d{4}-", "", title)
                    return title
    except (FileNotFoundError, UnicodeDecodeError):
        pass
    return ""


def get_existing_papers(readme_path: str) -> set:
    """
    Extract the set of paper .md filenames already referenced in README.md.

    Handles both relative paths (paper/xxx.md) and full GitHub blob URLs.
    URL-decodes the captured filenames before returning.
    """
    existing = set()
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return existing

    # Match relative reference: [摘要](paper/xxx.md) → captures filename
    for m in re.findall(r"paper/([^\s\)]+\.md)", content):
        existing.add(unquote(m))

    # Match GitHub blob URLs: github.com/.../blob/.../paper/xxx.md
    for m in re.findall(r"github\.com/[^\s\)]+/paper/([^\s\)]+\.md)", content):
        existing.add(unquote(m))

    return existing


def find_new_papers(paper_dir: str, readme_path: str) -> list:
    """
    Find paper .md files in paper_dir not yet referenced in README.md.

    Returns list of dicts with paper info, sorted by (canonical_dir, year).
    """
    existing = get_existing_papers(readme_path)
    new_papers = []

    paper_path = Path(paper_dir)
    if not paper_path.is_dir():
        print(f"Error: paper directory not found: {paper_dir}", file=sys.stderr)
        return []

    for f in sorted(paper_path.iterdir()):
        if not f.name.endswith(".md"):
            continue

        paper_ref = f.name
        if paper_ref in existing:
            continue

        info = parse_filename(f.name)
        if info is None:
            print(f"Warning: could not parse filename: {f.name}", file=sys.stderr)
            continue

        # Extract URLs from the paper file
        link_url, code_url = extract_urls(str(f))
        info["link_url"] = link_url
        info["code_url"] = code_url

        new_papers.append(info)

    # Sort by canonical direction, then year
    new_papers.sort(key=lambda x: (x["canonical_dir"], x["year"], x["title"]))
    return new_papers


def find_section_boundaries(lines: list, section_heading: str) -> Optional[tuple]:
    """
    Find the start and end line indices for a section's table in README.md.

    A section starts with "### <heading>" and its table continues until
    the next "### " heading or the "---" separator.

    Returns (table_header_line, last_data_line) or None.
    """
    section_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("### " + section_heading):
            section_start = i
            break

    if section_start is None:
        return None

    # The table header is 2 lines after the section heading
    # (one blank line, then the header row)
    header_line = section_start + 2
    if header_line >= len(lines):
        return None

    # Find the end of this section's table
    # Table ends at the next "### " heading, or "---" separator,
    # or a blank line followed by non-table content
    table_end = header_line + 1  # Skip header separator line
    for i in range(table_end, len(lines)):
        line = lines[i]
        # Next section heading
        if line.startswith("### "):
            table_end = i - 1
            break
        # Separator line in README
        if line.strip().startswith("---"):
            table_end = i - 1
            break
        # End of table (blank line followed by non-table)
        if line.strip() == "" and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if next_line and not next_line.startswith("|"):
                table_end = i - 1
                break
        table_end = i

    # Find the last actual data row (non-empty, starts with |)
    last_data = table_end
    while last_data > header_line + 1:
        if lines[last_data].strip().startswith("|") and lines[last_data].strip() != "":
            break
        last_data -= 1

    return (header_line + 1, last_data)  # +1 to skip the header separator


def format_row(info: dict) -> str:
    """Format a paper info dict as a README table row."""
    link_text = f"[查看]({info['link_url']})" if info['link_url'] != "-" else "[查看](-)"
    # URL-encode spaces in the filepath so GitHub links don't break.
    # Other special chars (+, !, :, etc.) are left as-is, matching existing
    # convention in this README.
    encoded_path = info['filepath'].replace(' ', '%20')
    summary_text = f"[摘要]({encoded_path})"
    code_text = f"[代码]({info['code_url']})" if info['code_url'] != "-" else "-"

    return f"| {info['year']} | {info['venue']} | {info['title']} | {link_text} | {summary_text} | {code_text} |\n"


def update_readme(readme_path: str, paper_dir: str, dry_run: bool = False) -> list:
    """
    Main function: update README.md with new papers.

    Returns list of added paper info dicts.
    """
    new_papers = find_new_papers(paper_dir, readme_path)
    if not new_papers:
        print("No new papers found to add.")
        return []

    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Group new papers by canonical direction → section heading
    papers_by_section = {}
    for paper in new_papers:
        heading = DIRECTION_MAP.get(paper["canonical_dir"])
        if heading is None:
            print(f"Warning: unknown direction '{paper['canonical_dir']}' "
                  f"for {paper['filepath']}, skipping", file=sys.stderr)
            continue
        papers_by_section.setdefault(heading, []).append(paper)

    # We need to insert papers from the bottom up to preserve line numbers
    # Collect all insertion operations first
    insertions = []  # List of (line_number, rows_to_insert)
    sections_not_found = []

    for heading, papers in papers_by_section.items():
        boundaries = find_section_boundaries(lines, heading)
        if boundaries is None:
            sections_not_found.append((heading, papers))
            continue

        _, last_data_line = boundaries
        # Insert after the last existing data row
        insert_after = last_data_line
        new_rows = [format_row(p) for p in papers]
        insertions.append((insert_after, new_rows))

    # Sort insertions by line number (descending) so we can insert from bottom up
    insertions.sort(key=lambda x: x[0], reverse=True)

    # Apply insertions
    for insert_after, new_rows in insertions:
        for row in reversed(new_rows):
            lines.insert(insert_after + 1, row)

    # Handle sections not found — print warning
    for heading, papers in sections_not_found:
        papers_list = [p["filepath"] for p in papers]
        print(f"Warning: section '{heading}' not found in README.md. "
              f"Cannot add: {', '.join(papers_list)}", file=sys.stderr)

    if not dry_run:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"Updated {readme_path} with {len(new_papers)} new paper(s).")
    else:
        print(f"[DRY RUN] Would update {readme_path} with {len(new_papers)} new paper(s):")
        for p in new_papers:
            print(f"  [{p['canonical_dir']}] {p['year']} | {p['venue']} | {p['title']}")

    return new_papers


def main():
    parser = argparse.ArgumentParser(
        description="Update README.md with new papers from paper/ directory"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be changed without actually modifying README.md"
    )
    parser.add_argument(
        "--readme", default="README.md",
        help="Path to README.md (default: README.md in current directory)"
    )
    parser.add_argument(
        "--paper-dir", default="paper",
        help="Path to paper directory (default: paper)"
    )
    args = parser.parse_args()

    if not os.path.isfile(args.readme):
        print(f"Error: README not found: {args.readme}", file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(args.paper_dir):
        print(f"Error: paper directory not found: {args.paper_dir}", file=sys.stderr)
        sys.exit(1)

    added = update_readme(args.readme, args.paper_dir, dry_run=args.dry_run)

    if added:
        print(f"\nSummary: {len(added)} paper(s) added.")
        for p in added:
            print(f"  ✓ [{p['canonical_dir']}] {p['year']} {p['title']}")
    else:
        print("\nNo changes needed — README is up to date.")


if __name__ == "__main__":
    main()
