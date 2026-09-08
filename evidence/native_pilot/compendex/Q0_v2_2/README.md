# Compendex Q0 v2.2 evidence package

Status: **FROZEN**

This Git package intentionally stores reproducibility metadata and derived decisions, not the raw Compendex detailed-record export.

## Frozen result
- Native result: 245
- Export rows: 245
- SHA-256 of raw export: `2c15662b02f27a085dc39f50245d33c4f2166c63839050feb8fc2eb22f7816a8`
- Canonical unique N: 245
- Exact DOI duplicates: 0
- Exact title+same-year duplicates: 0
- Years: 2001–2026; outside protocol window: 0
- Missing abstracts: 0
- Missing DOI: 29
- Superseded-version candidates: 12
- Development: 20/30 = 66.7%; Wilson 48.8–80.8%
- Validation: 16/30 = 53.3%; Wilson 36.1–69.8%
- Dev–validation difference: 13.3 pp
- Prospective anchors: 3/3 = 100%
- Exact-key overlap with Scopus Q0: 212; Jaccard 0.7413
- Exact-key overlap with IEEE Q0: 65; Jaccard 0.1762
- Exact-key unique vs Scopus∪IEEE: 32
- Decision: FREEZE

## Execution deviation
`RD-CPX-Q0-SET-01`: Engineering Village rejected the full frozen Expert Search in one long expression. The same semantics were executed as atomic `KY` searches, OR-unioned into P/T/Z/R Search-History blocks, then intersected. This is an execution-only deviation, not a scientific query change.

Final block counts:
- P = 504,675
- T = 375,268
- Z = 275,522
- R = 1,056,435
- Q0 = 245

## Raw export
Expected filename:
`2026-09-08_COMPENDEX_Q0_v2_2_RAW_N0245.csv`

The raw detailed-record file includes database-provided abstracts/metadata. Keep it in private research storage and verify it against the SHA-256 above. Do not publish it unless licensing permits.

## Git-safe derivatives
- exact search ledger: `project_memory/2026-09-08_native_systematic_review/02_COMPENDEX_Q0_SEARCH_LEDGER.csv`
- artifact hashes: `project_memory/2026-09-08_native_systematic_review/04_ARTIFACT_MANIFEST.csv`
- screening codebook: `project_memory/2026-09-08_native_systematic_review/05_SCREENING_CODEBOOK.md`
- processing pipeline: `project_memory/2026-09-08_native_systematic_review/03_PROCESSING_PIPELINE.md`
- reproducibility utility: `methods/native_systematic_review/native_pilot_reproduce.py`
- continuation prompt: `project_memory/2026-09-08_native_systematic_review/01_FULL_HANDOFF_PROMPT.md`

## Next native run
`CPX-Q3 v1.1` — Direct P–T timescales/delays.
