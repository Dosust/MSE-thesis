# Native database-search screenshot archive — 2026-09-08

This folder is the provenance index for screenshots captured during the native database-search workflow used for the MSE thesis systematic review.

## Scope

- Database interface evidence: Engineering Village / Compendex searches, Search History, parser/system errors, date/database settings, result counts, and export dialogs.
- Total screenshot files identified from the 2026-09-08 search session: **78**.
- Every original screenshot is fingerprinted in `SCREENSHOT_MANIFEST.csv` using SHA-256 and byte size.
- Two non-database mind-map images mounted in the same runtime were intentionally excluded from the database-search screenshot set.

## Compendex Q0 search evidence

The exact atomic query/count ledger is preserved at:

`project_memory/2026-09-08_native_systematic_review/02_COMPENDEX_Q0_SEARCH_LEDGER.csv`

The frozen result is:

- Power union P = 504,675
- Transportation union T = 375,268
- Interdependency union Z = 275,522
- Resilience union R = 1,056,435
- Final Q0 = P AND T AND Z AND R = **245**

The early invalid transportation unions returning 372,049 are preserved as diagnostics; they duplicated `transport system*` and omitted `charging station*` and therefore are not part of the frozen scientific run.

## Search-history evidence

Exact native Search-History exports are stored under:

`evidence/native_search_history/compendex/2026-09-08/`

The first archived history captures queries #1-#23, including the valid Power block and the diagnostic/invalid Transportation unions.

## Screenshot integrity

`SCREENSHOT_MANIFEST.csv` is authoritative for screenshot identity. It records:

`sequence, original_filename, bytes, sha256, classification`

This permits byte-level verification if screenshots are copied, renamed, moved, or later stored using Git LFS.

## Binary-image storage note

The connected GitHub write interface available in this chat supports repository text writes directly but does not expose a local-file upload parameter for binary PNG attachments. Therefore the repository now contains the complete search/query provenance and an exact cryptographic manifest for all 78 screenshots. The original PNG files remain available in the thesis chat/runtime and should be copied into this folder (or Git LFS) without transformation; their SHA-256 values must match the manifest.

Recommended destination for original screenshots:

`evidence/native_search_screenshots/2026-09-08/original_png/`

Do not resize, recompress, crop, or rename the archival originals before hashing/verification.
