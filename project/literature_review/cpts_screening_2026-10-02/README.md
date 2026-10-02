# CPTS Literature Screening Package — 2026-10-02

**Thesis:** Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience

**Guiding research question:** How do time-varying physical states and interdependencies between power and transportation systems determine service degradation and recovery under extreme heat, and how can targeted operational interventions reduce the resulting coupled service deficits?

## Scientific review logic

FRAMEWORK → METHOD → FINDINGS → LIMITATIONS → SYNTHESIS → CONTRIBUTION

Review philosophy:

ADOPT → ADAPT → TEST → COMPARE → IMPROVE

## Status

This package contains a **26-paper high-priority evidence seed and screening workflow**. It is **not yet an exact auditable 200→26 PRISMA flow**. In the originating run, scholarly bulk API access did not yield a verified 200-record corpus. The scripts therefore preserve the distinction between:

- an executed 26-paper priority evidence map;
- a reproducible screening engine;
- a future exact 200-record discovery/deduplication/title-abstract/full-text workflow.

Do not report “200 papers screened to 26” until `01_deduplicated_pool.csv` contains 200 unique records from a documented scholarly export or retrieval run and the screening decisions are preserved.

## Files

- `CPTS_26_High_Rigor_Literature_Map.xlsx` — generated evidence workbook (SHA-256 recorded in the manifest; binary workbook remains a generated artifact and is not committed by this connector run).
- `CPTS_literature_screening_protocol.md` — screening protocol and rubric.
- `cpts_26_screened.csv` — 26-paper priority evidence table.
- `cpts_26_seed.json` — structured seed dataset.
- `screen_cpts_literature.py` — Python retrieval/screening/ranking pipeline.
- `screen_cpts_literature.js` — JavaScript deterministic scoring mirror.
- `js_seed_ranked.json` — JavaScript execution output on the seed set.
- `CPTS_screening_manifest.json` — SHA-256 manifest.

## Evidence discipline

Keep these separate:

`author-stated limitation != reviewer-inferred limitation != thesis contribution`

A limitation becomes a candidate contribution only after a controlled comparison shows that the proposed adaptation materially improves explanation, prediction, service-resilience assessment, or intervention choice.