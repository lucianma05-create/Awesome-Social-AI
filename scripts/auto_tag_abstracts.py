#!/usr/bin/env python3
"""Assign transparent, controlled-vocabulary draft tags from cached abstracts.

This is a deterministic bootstrapper, not a claim of human validation.  Each
assigned tag stores the matched abstract cue as evidence and is marked
``auto_extracted`` for display and later correction.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


RULES = {
    "goal": {
        "Influence": r"persua|negotiat|bargain|debate|opponent|convinc|说服|劝服|谈判|辩论",
        "Support": r"empath|emotional support|mental health|counsel|comfort|共情|情感支持|心理健康|心理辅导",
        "Recommendation": r"recommend|recommender|preference elicitation|推荐",
        "Coordination": r"cooperat|collaborat|coordina|teamwork|consensus|协作|合作|协调|共识",
    },
    "capabilities": {
        "Social Perception": r"social cue|body language|gaze|gesture|social signal",
        "Affect": r"emotion|empath|affect|sentiment|情绪|共情|情感",
        "Mental-State Modeling": r"theory of mind|mental state|belief|intention|opponent.{0,30}(state|thought|stance)|user model|心智理论|心理状态|信念|意图|对手建模",
        "Social Context": r"social context|social norm|cultur|relationship|role-play|social goal|persona|社会情境|社会规范|文化|关系|角色|人格",
        "Interaction Management": r"dialogue strateg|conversation strateg|turn.taking|rapport|strategic communication|interaction.{0,30}(goal|strateg)|对话策略|轮次|关系维护|交互",
        "Social Memory & Adaptation": r"long.?term memory|social memory|previous (interaction|conversation|history)|personaliz|adapt.{0,25}(user|interaction)|长期记忆|互动历史|个性化|适应",
    },
    "contexts": {
        "Personalization": r"personaliz|individual preference|user profile",
        "Relationship & Role": r"relationship|role-play|social role|buyer|seller|persona",
        "Norms & Morality": r"social norm|moral|ethical|secret|privacy",
        "Culture": r"cultur|cross-cultural",
        "Multi-party": r"multi.?agent|multiple agents|three agents|multi.?party",
        "Embodied": r"embodied|robot|physical action|gesture|gaze",
    },
    "approaches": {
        "Supervised Learning": r"supervised|fine.?tun",
        "Retrieval": r"retriev|retrieval-augmented",
        "Planning": r"planning|planner|plan over",
        "RL": r"reinforcement learning|\bppo\b|policy optimization",
        "Preference Optimization": r"direct preference optimization|\bdpo\b|preference optimization",
        "Reward Modeling": r"reward model|reward modeling|reward signal",
        "Self-play": r"self-play|self play",
        "User Simulation": r"user simulat|simulate.{0,30}user",
    },
}


def match(text: str, pattern: str) -> str | None:
    found = re.search(pattern, text, flags=re.IGNORECASE)
    return found.group(0) if found else None


def choose_type(text: str) -> tuple[str, str]:
    for label, pattern in [
        ("Survey", r"\bsurvey\b|comprehensive review"),
        ("Benchmark", r"\bbenchmark\b|evaluation framework|evaluate .* abilities"),
        ("Dataset", r"\bdataset\b|corpus|we collected"),
        ("Evaluation", r"evaluate|assessment|measuring"),
        ("System", r"environment|simulator|platform"),
    ]:
        cue = match(text, pattern)
        if cue:
            return label, cue
    return "Method", "method proposed in abstract"


def choose_horizon(text: str) -> tuple[str, str]:
    cue = match(text, r"long.?term|across sessions|longitudinal|长期|跨会话")
    if cue:
        return "Longitudinal", cue
    cue = match(text, r"multi.?turn|multiple rounds|iterative interaction|dialogue|多轮|对话")
    if cue:
        return "Multi-turn", cue
    return "Unspecified", "no interaction-horizon cue in source text"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metadata", default="metadata/papers.json")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--refresh-summary", action="store_true",
                        help="recompute tags generated from repository summaries")
    parser.add_argument("--refresh-title-fallback", action="store_true",
                        help="replace title-fallback tags when an original abstract was obtained")
    args = parser.parse_args()
    path = Path(args.metadata)
    payload = json.loads(path.read_text(encoding="utf-8"))
    candidates = [(paper_id, record) for paper_id, record in payload["papers"].items()
                  if (record.get("abstract") or record.get("tag_text")) and
                  (record.get("review_status") == "unclassified" or
                   (args.refresh_summary and record.get("tag_text_source") == "repository_summary") or
                   (args.refresh_title_fallback and record.get("tag_text_source") == "title_fallback" and record.get("abstract")))][:args.limit]
    for paper_id, record in candidates:
        text = record.get("abstract") or record["tag_text"]
        text_source = "abstract" if record.get("abstract") else record.get("tag_text_source", "repository_summary")
        goal_matches = {label: match(text, pattern) for label, pattern in RULES["goal"].items()}
        legacy_goal = {"influence-negotiation": "Influence", "support-care": "Support",
                       "conversational-recommendation": "Recommendation",
                       "cooperation-coordination": "Coordination"}.get(record.get("primary_section"))
        goal, goal_cue = next(((label, cue) for label, cue in goal_matches.items() if cue),
                              (legacy_goal or "General Interaction", "legacy primary section" if legacy_goal else "no specific social-goal cue in source text"))
        paper_type, type_cue = choose_type(text)
        horizon, horizon_cue = choose_horizon(text)
        selected = {facet: [(label, cue) for label, pattern in rules.items()
                             if (cue := match(text, pattern))]
                    for facet, rules in RULES.items() if facet != "goal"}
        evidence = [
            {"tag": label, "rationale": f"Source cue: '{cue}'.", "source": text_source}
            for facet in ("capabilities", "contexts", "approaches") for label, cue in selected[facet]
        ]
        record.update({
            "type": paper_type, "goal": goal,
            "capabilities": [label for label, _ in selected["capabilities"]],
            "contexts": [label for label, _ in selected["contexts"]],
            "approaches": [label for label, _ in selected["approaches"]],
            "horizon": horizon,
            "field_evidence": [
                {"field": "primary_section", "rationale": "Preserved legacy browse section during automatic migration.", "source": "legacy README"},
                {"field": "type", "rationale": f"Source cue: '{type_cue}'.", "source": text_source},
                {"field": "goal", "rationale": f"Source cue: '{goal_cue}'.", "source": text_source},
                {"field": "horizon", "rationale": f"Source cue: '{horizon_cue}'.", "source": text_source},
            ],
            "evidence": evidence,
            "annotated_by": "auto-abstract-extractor-v1",
            "review_status": "auto_extracted",
            "auto_tag_version": "1.0.0",
        })
        if text_source == "abstract":
            record.pop("auto_confidence", None)
            record.pop("tag_text", None)
            record.pop("tag_text_source", None)
    print(f"Would automatically tag {len(candidates)} source-backed records." if args.dry_run
          else f"Automatically tagged {len(candidates)} source-backed records.")
    if not args.dry_run:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
