# Contributing to Awesome Social AI

**[English](CONTRIBUTING.md)** | **[简体中文](CONTRIBUTING_CN.md)**

Anyone interested in socially intelligent conversational agents is welcome to contribute to this repository. You can:

- add new papers to the catalogue (`metadata/papers.json`)
- add Chinese summaries to `paper/` (optional)
- improve keywords, vocabulary definitions, and the pipeline scripts
- fix typos, links, or metadata issues

In general, we follow the "fork-and-pull" Git workflow:

1. Fork this repository to your own GitHub account.
2. Clone it locally and create a branch for your changes.
3. Make your changes and commit them.
4. Push the branch to your fork.
5. Open a pull request to the `main` branch of this repository.

## Adding a paper

1. Add a structured record in `metadata/papers.json`: `type`, `goal`, `horizon` are single-choice; capabilities, contexts, and approaches are multi-choice. All label values must come from the [keyword vocabulary](metadata/KEYWORDS.md); add paper evidence for every multi-choice label.
2. Validate and rebuild the catalogue before committing:

```bash
python scripts/validate_metadata.py --paper-dir paper
python scripts/render_readme_catalog.py
```

## Adding a Chinese summary (optional)

A Chinese summary is not required for a paper to enter the catalogue — summary links only appear in the Chinese README. If you want to add one:

- Name files under `paper/` strictly as `[Section]-[Venue]-[Year]-[Full paper title].md`, e.g. `Memory-NeurIPS-2023-Retrieval-Augmented-Generation.md`. The filename prefix is the paper's **primary section** — pick the closest of the 11 existing prefixes; it does not replace the keywords. Discuss in the group before adding a new prefix. Current prefixes: `PD`, `ED`, `Recommend`, `Coop`, `ToM`, `Emotion`, `Norms`, `Memory`, `RLHF`, `US`, `Data`.
- Write the note following the [Example.md](Example.md) template and set the record's `summary_path` to the new file.
- Re-run the validation and render commands above.

You can also use [Auto-Summary](https://github.com/lucianma05-create/Auto-Summary) to draft summaries, then proofread them manually.

## Images

Name files under `image/` as `[Year]-[Month]-[Day]-[Number]-[Initials].png`, e.g. `2024010101mmh.png`.
