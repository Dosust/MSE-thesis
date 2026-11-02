# Thesis research skill package V1 — ready for GitHub

This package implements the request for **eight complementary, research-operational skills** and a central `SKILL.md` orchestrator. It is an *additive working skill*, not a canonical thesis amendment or a field validation result.

## Layout

- `SKILLS.md`: short research skill catalog.
- `.github/skills/power-ev-thermal-research/SKILL.md`: master orchestrator.
- `.github/skills/thesis-*/SKILL.md`: eight specialized execution skills.
- `references/`: authority snapshot, scientific evidence gates and data dictionary.
- `templates/`: header-only CSV registers, no fabricated records.
- `tools/check_evidence.py` and `tests/`: schema gate and regression tests.

## Install and run

Copy `.github/skills/*` to your thesis repo's `.github/skills/` and retain the shared `references/`, `templates/`, `tools/`, and `tests/` in the package root; or keep this whole package as one versioned research-skill directory and adjust relative reference paths accordingly. **The preferred installation is to keep the reference/template/tool directories alongside the master skill under `.github/skills/power-ev-thermal-research/`; this package includes a copy there** so it is self-contained after installation.

```bash
python -m unittest discover -s tests -v
python tools/check_evidence.py --root templates
```

The second command checks only CSV schema and claim-tier rules. It does not validate raw data, physical modeling or a connected thermal field study. Current scope/title/claim controls must be loaded from the repository, not from an old memory/snapshot.

## V2 learning overlay — November 2026

Includes an explicitly source-grounded integration of the published University of Houston ECE6378 (Fall 2026) machine learning for power systems outline, and three public RPG Lab Python resource descriptions. Lectures 19–27 are marked tentative. A seventh scientific workstream is **not** created: this is a supporting method layer integrated into the eight original modules. The added ML experiment checker is an independent structural gate only; no code or educational resource magically validates physical transformer–EVSE coupling. All original V1 materials and frozen canonical authorities are preserved.
