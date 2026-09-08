# Database search screenshot evidence — 2026-09-08

This directory preserves the visual audit trail for the database-search work completed in the thesis workflow.

## Coverage

- **78 original screenshots** captured in the thesis chat/session.
- **Compendex / Engineering Village:** screenshots 001–068.
- **IEEE Xplore:** screenshots 069–072.
- **Scopus:** screenshots 073–078.

The exact original PNG files are preserved in the local research evidence package and fingerprinted individually in `screenshot_manifest.csv`. GitHub stores the complete machine-readable manifest plus visual contact-sheet previews of all 78 screenshots.

## Files

- `screenshot_manifest.csv` — one row per original screenshot with database, UUID filename, byte size, dimensions, date, and SHA-256.
- `archive_manifest.csv` — SHA-256 fingerprints for the exact-original archive chunks held in the local/private evidence package.
- `previews/contact_sheet_01.jpg` … `contact_sheet_04.jpg` — visual overview containing all 78 screenshots in sequence.

## Relationship to search provenance

The Compendex Q0 scientific query/count ledger is maintained at:

`project_memory/2026-09-08_native_systematic_review/02_COMPENDEX_Q0_SEARCH_LEDGER.csv`

The screenshot package is the **visual native-execution audit trail**. The search ledger, raw-export hashes, pilot screening decisions, and run manifests remain the machine-readable scientific provenance.

## Database mapping

- `001–068`: Compendex / Engineering Village search construction, parser errors, atomic queries, Search History unions, final Q0 result, and export UI.
- `069–072`: IEEE Xplore search/result/export evidence from the same review workflow.
- `073–078`: Scopus search/result/export evidence from the same review workflow.

## Integrity rule

Do not edit or overwrite the original evidence. If a screenshot must be annotated, create a derivative under a separate `annotations/` directory and preserve the original SHA-256 record unchanged.

## Exact-original private package

Local research package created for this audit:

`database_search_screenshot_evidence_2026-09-08.zip`

Package SHA-256:

`5d62b201a9699221b2fc4428b12dd3e7d6a1672bec060d859fcd6e88b613a788`

This package contains all 78 original PNG screenshots byte-for-byte, grouped into six smaller archive chunks. The archive-level hashes are recorded in `archive_manifest.csv`.
