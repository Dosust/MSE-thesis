# Archived Artifacts

This directory stores machine-readable audit snapshots and, where practical, binary artifacts encoded as Base64 text so they can be version-controlled through the GitHub connector.

## Restore Version 1.0 workbook

File:

`BioInspired_Construction_Evidence_Extraction_v1.0.xlsx.base64.txt`

Restore on macOS/Linux:

```bash
base64 --decode BioInspired_Construction_Evidence_Extraction_v1.0.xlsx.base64.txt > BioInspired_Construction_Evidence_Extraction_v1.0.xlsx
```

On some macOS versions use:

```bash
base64 -D BioInspired_Construction_Evidence_Extraction_v1.0.xlsx.base64.txt > BioInspired_Construction_Evidence_Extraction_v1.0.xlsx
```

Expected SHA-256:

`7d671564f061befe686648a18ac3a3d77d1e5a23dcd3930dca8c94504771ab07`

Verify:

```bash
shasum -a 256 BioInspired_Construction_Evidence_Extraction_v1.0.xlsx
```

## Audit snapshots

- `BIO58_v1.0_Audit.initial.json` — initial frozen Version 1.0 audit.
- `BIO58_Evidence_Rigor_Audit.latest.json` — later strengthened evidence-rigor state preserved from File Library/chat.

The later audit supersedes the initial audit for substantive BIO58 state while preserving the same frozen schema.

## Controlled source workbook

The controlled Scopus workbook is identified in `../09_ARTIFACT_MANIFEST.md` by filename and SHA-256. It is intentionally not treated as a source of focal full-text evidence; legacy coded cells are comparison data only.