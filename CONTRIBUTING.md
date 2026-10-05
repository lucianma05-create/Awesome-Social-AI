# Contributing to Awesome Social AI

**[English](CONTRIBUTING.md)** | **[简体中文](CONTRIBUTING_CN.md)**

Anyone interested in socially intelligent conversational agents is welcome to contribute to this repository. You can:

- add new papers to the catalogue (`metadata/papers.json`) and Chinese summaries to `paper/`
- improve keywords, vocabulary definitions, and the pipeline scripts
- fix typos, links, or metadata issues

In general, we follow the "fork-and-pull" Git workflow:

1. Fork this repository to your own GitHub account.
2. Clone it locally and create a branch for your changes.
3. Make your changes and commit them.
4. Push the branch to your fork.
5. Open a pull request to the `main` branch of this repository.

## Naming conventions

- Name files under `paper/` strictly as `[Section]-[Venue]-[Year]-[Full paper title].md`, e.g. `Memory-NeurIPS-2023-Retrieval-Augmented-Generation.md`.
- The filename prefix is the paper's **primary section** — pick the closest of the 11 existing prefixes; it does not replace the keywords. Discuss in the group before adding a new prefix. Current prefixes: `PD`, `ED`, `Recommend`, `Coop`, `ToM`, `Emotion`, `Norms`, `Memory`, `RLHF`, `US`, `Data`.
- Name files under `image/` as `[Year]-[Month]-[Day]-[Number]-[Initials].png`, e.g. `2024010101mmh.png`.

## Adding a paper

1. Write the Chinese summary following the [Example.md](Example.md) template.
2. Add a structured record in `metadata/papers.json`: `type`, `goal`, `horizon` are single-choice; capabilities, contexts, and approaches are multi-choice. All label values must come from the [keyword vocabulary](metadata/KEYWORDS.md); add paper evidence for every multi-choice label.
3. Validate and rebuild the catalogue before committing:

```bash
python scripts/validate_metadata.py --paper-dir paper
python scripts/render_readme_catalog.py
```

You can also use [Auto-Summary](https://github.com/lucianma05-create/Auto-Summary) to draft summaries, then proofread them manually.
