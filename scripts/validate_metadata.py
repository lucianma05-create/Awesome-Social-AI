#!/usr/bin/env python3
"""Validate the structured paper metadata used by the Social AI catalogue.

The script intentionally uses only Python's standard library.  It validates
controlled-vocabulary fields, checks that records point to real summaries,
and reports migration coverage.  It does not infer tags from titles: tag
assignment requires evidence recorded by a curator.

Usage:
    python scripts/validate_metadata.py
    python scripts/validate_metadata.py --strict --paper-dir paper
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SINGLE_FIELDS = {
    "primary_section": {
        "influence-negotiation", "support-care", "conversational-recommendation",
        "cooperation-coordination", "mental-state-modeling", "affect-social-perception",
        "social-context-norms-morality", "social-memory-adaptation",
        "learning-planning-alignment", "user-simulation-environments",
        "datasets-benchmarks-evaluation",
    },
    "type": {"System", "Method", "Dataset", "Benchmark", "Evaluation", "Survey"},
    "goal": {"Influence", "Support", "Recommendation", "Coordination", "General Interaction"},
    "horizon": {"Single-turn", "Multi-turn", "Longitudinal", "Unspecified"},
}
MULTI_FIELDS = {
    "capabilities": {
        "Social Perception", "Affect", "Mental-State Modeling", "Social Context",
        "Interaction Management", "Social Memory & Adaptation",
    },
    "contexts": {
        "Personalization", "Relationship & Role", "Norms & Morality", "Culture",
        "Multi-party", "Embodied",
    },
    "approaches": {
        "Supervised Learning", "Retrieval", "Planning", "RL", "Preference Optimization",
        "Reward Modeling", "Self-play", "User Simulation",
    },
}
REVIEW_STATUSES = {"unclassified", "auto_extracted", "draft", "reviewed", "needs_review"}
REQUIRED_CATALOG_FIELDS = {"title": str, "year": int, "venue": str}


def error(messages: list[str], record_id: str, message: str) -> None:
    messages.append(f"{record_id}: {message}")


def validate_record(record_id: str, record: object, paper_dir: Path) -> list[str]:
    """Return validation errors for one metadata record."""
    messages: list[str] = []
    if not isinstance(record, dict):
        return [f"{record_id}: record must be an object"]

    for field, expected_type in REQUIRED_CATALOG_FIELDS.items():
        value = record.get(field)
        if not isinstance(value, expected_type) or not value:
            error(messages, record_id, f"{field!r} must be a non-empty {expected_type.__name__}")
    for field in ("paper_url", "code_url"):
        value = record.get(field)
        if value is not None and (not isinstance(value, str) or not value):
            error(messages, record_id, f"{field!r} must be a non-empty string or null")
    summary_path = record.get("summary_path")
    if summary_path is not None:
        if not isinstance(summary_path, str) or not summary_path.startswith("paper/"):
            error(messages, record_id, "summary_path must be null or a path starting with 'paper/'")
        elif not Path(summary_path).is_file():
            error(messages, record_id, "summary_path does not refer to an existing file")

    status = record.get("review_status")
    if status not in REVIEW_STATUSES:
        error(messages, record_id, f"review_status must be one of {sorted(REVIEW_STATUSES)}")
    if status == "unclassified":
        return messages

    for field, allowed in SINGLE_FIELDS.items():
        value = record.get(field)
        if value not in allowed:
            error(messages, record_id, f"{field!r} must be one of {sorted(allowed)}, got {value!r}")

    field_evidence = record.get("field_evidence")
    if not isinstance(field_evidence, list):
        error(messages, record_id, "field_evidence must be a list")
    else:
        evidenced_fields = set()
        for item in field_evidence:
            if not isinstance(item, dict):
                error(messages, record_id, "each field_evidence item must be an object")
                continue
            field, rationale, source = item.get("field"), item.get("rationale"), item.get("source")
            if field not in SINGLE_FIELDS:
                error(messages, record_id, f"field_evidence refers to unknown field {field!r}")
            if not isinstance(rationale, str) or not rationale.strip():
                error(messages, record_id, f"field_evidence for {field!r} lacks a rationale")
            if not isinstance(source, str) or not source.strip():
                error(messages, record_id, f"field_evidence for {field!r} lacks a source section/page")
            evidenced_fields.add(field)
        missing_field_evidence = set(SINGLE_FIELDS) - evidenced_fields
        if missing_field_evidence:
            error(messages, record_id, f"missing field_evidence for {sorted(missing_field_evidence)}")

    selected_tags: set[str] = set()
    for field, allowed in MULTI_FIELDS.items():
        values = record.get(field)
        if not isinstance(values, list):
            error(messages, record_id, f"{field!r} must be a list")
            continue
        if len(values) != len(set(values)):
            error(messages, record_id, f"{field!r} contains duplicate tags")
        for value in values:
            if value not in allowed:
                error(messages, record_id, f"unknown {field} tag {value!r}")
            else:
                selected_tags.add(value)

    annotated_by = record.get("annotated_by")
    if not isinstance(annotated_by, str) or not annotated_by.strip():
        error(messages, record_id, "annotated_by must be a non-empty string")
    if status == "reviewed":
        reviewed_by = record.get("reviewed_by")
        if not isinstance(reviewed_by, str) or not reviewed_by.strip():
            error(messages, record_id, "reviewed records require a non-empty reviewed_by")
        elif reviewed_by == annotated_by:
            error(messages, record_id, "reviewed_by must differ from annotated_by")

    evidence = record.get("evidence")
    if not isinstance(evidence, list):
        error(messages, record_id, "evidence must be a list")
        return messages

    evidenced_tags = set()
    for item in evidence:
        if not isinstance(item, dict):
            error(messages, record_id, "each evidence item must be an object")
            continue
        tag, rationale, source = item.get("tag"), item.get("rationale"), item.get("source")
        if tag not in selected_tags:
            error(messages, record_id, f"evidence refers to unselected tag {tag!r}")
        if not isinstance(rationale, str) or not rationale.strip():
            error(messages, record_id, f"evidence for {tag!r} lacks a rationale")
        if not isinstance(source, str) or not source.strip():
            error(messages, record_id, f"evidence for {tag!r} lacks a source section/page")
        evidenced_tags.add(tag)

    missing_evidence = selected_tags - evidenced_tags
    if missing_evidence:
        error(messages, record_id, f"missing evidence for {sorted(missing_evidence)}")
    return messages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metadata", default="metadata/papers.json")
    parser.add_argument("--paper-dir", default="paper")
    parser.add_argument("--strict", action="store_true", help="fail if any paper lacks a metadata record")
    args = parser.parse_args()

    metadata_path, paper_dir = Path(args.metadata), Path(args.paper_dir)
    try:
        payload = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Metadata error: {exc}", file=sys.stderr)
        return 2

    if payload.get("schema_version") != "1.0.0" or not isinstance(payload.get("papers"), dict):
        print("Metadata error: expected schema_version '1.0.0' and a papers object", file=sys.stderr)
        return 2

    records: dict[str, object] = payload["papers"]
    invalid_ids = [record_id for record_id in records if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", record_id)]
    if invalid_ids:
        print(f"Metadata error: invalid paper IDs: {', '.join(invalid_ids)}", file=sys.stderr)
        return 2
    errors = [message for record_id, record in records.items()
              for message in validate_record(record_id, record, paper_dir)]
    summary_files = {str(path) for path in paper_dir.glob("*.md")}
    linked_summaries = {record.get("summary_path") for record in records.values()
                        if isinstance(record, dict) and record.get("summary_path")}
    orphan_summaries = summary_files - linked_summaries
    if args.strict and orphan_summaries:
        errors.append(f"coverage: {len(orphan_summaries)} summary files lack metadata records")

    print(f"Catalogue records: {len(records)}; linked summaries: {len(linked_summaries)}/{len(summary_files)}")
    if errors:
        print("Validation failed:", file=sys.stderr)
        print("\n".join(f"- {message}" for message in errors), file=sys.stderr)
        return 1
    if orphan_summaries:
        print(f"Pending migration: {len(orphan_summaries)} paper summaries have no metadata record")
    print("Metadata validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
