# Session Snapshot Archive

This directory preserves the thesis artifacts available in the active 2026-08-20 session without pretending that hidden system/developer instructions or private chain-of-thought are user-facing conversation records.

## Textual/scientific snapshot

`textual/partNNN.b64` are ordered Base64 chunks of:

`MSE-thesis-textual-snapshot.tar.gz`

- Original archive bytes: `376269`
- SHA-256: `8e2ab6aee07a23471554af361e35bd755f4758b1d95b0006ff23014976fadefe`
- Base64 characters: `501692`
- Parts: `18`
- Part size: 28,000 Base64 characters except the final part

The tarball contains the repository-ready thesis snapshot excluding only three binary convenience artifacts (`*.xlsx` workbooks and the duplicate Monte Carlo ZIP). Their scientific/source content is preserved in CSV/result form inside the textual snapshot; the authoritative final 325-paper workbook is separately preserved under `archive/binary_payloads/final325_xlsx/`.

## Final 325-paper workbook

`../binary_payloads/final325_xlsx/partNNN.b64` reconstructs:

`Thesis_Final_Unique_Papers_325_2026-08-20.xlsx`

- Bytes: `111129`
- SHA-256: `2a1b7155f6d71d320fef7237ffba97375f673ee6cb4d8d3ac471bdd4a27285f0`
- Parts: `6`

## Reconstruction

Use `provenance/reconstruct_archives.py` from the repository root. It concatenates the ordered parts, Base64-decodes them, verifies SHA-256, and writes the recovered files.

This split representation is used because the connected GitHub write interface accepts UTF-8 repository content but does not expose direct local binary-file upload.
