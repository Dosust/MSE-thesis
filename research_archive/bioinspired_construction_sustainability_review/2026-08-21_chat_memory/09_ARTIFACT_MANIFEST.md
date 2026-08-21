# Artifact Manifest and Provenance

## A. Controlled bio-inspired corpus

### Source workbook

Filename used in the active runtime:

`scopus_export_bio-inspiration%20AND%20%28%20framework%20OR%20evaluation%20%29%20AND%20construction%208%281%29.xlsx`

Equivalent human-readable name:

`scopus_export_bio-inspiration AND ( framework OR evaluation ) AND construction 8(1).xlsx`

Runtime SHA-256:

`c32a1bf178402593bbf04bf47ef8ad5ead0e3f785c131d41084a4349e7247d96`

Role: authoritative controlled corpus and legacy coding/synthesis workbook. Legacy interpretation cells are not primary evidence.

## B. Version 1.0 extraction workbook

Filename:

`BioInspired_Construction_Evidence_Extraction_v1.0.xlsx`

Runtime SHA-256:

`7d671564f061befe686648a18ac3a3d77d1e5a23dcd3930dca8c94504771ab07`

Role: initial frozen 10-sheet schema populated conservatively for BIO58.

Important: later File Library audits/workbooks strengthen/correct some BIO58 content while preserving the schema. Therefore this binary is a historical Version 1.0 snapshot, not the latest evidence-rigor content state.

## C. Initial BIO58 audit

Filename:

`BIO58_v1.0_Audit.json`

Runtime SHA-256:

`1c6721d9423de34d5dab1e47a7a01a9142231458636b07029d6beac63d3e5bdb`

Initial audit state:
- schema frozen;
- identity confirmed;
- focal PDF not located in uploaded sources;
- page verification pending;
- no spreadsheet formula errors.

## D. Later high-rigor BIO58 artifacts in ChatGPT File Library

These are later than the initial Version 1.0 snapshot and should be consulted before future BIO58 interpretation:

### `BioInspired_Construction_Evidence_Extraction_v1.0_BIO58_High_Rigor.xlsx`

High-rigor workbook retaining the frozen 10-sheet schema.

### `BIO58_High_Rigor_Audit.json`

Reported state includes:
- result: PASS_WITH_PDF_ACCESS_LIMITATION;
- schema: FROZEN_UNCHANGED;
- BiSA focal assessment;
- environmental LCA embedded;
- GaBi-based LCI + economic/country process information;
- intended building-physical function as confirmed linkage to BiSA social function;
- exact numeric sustainability output/page locators still unresolved.

Reported output workbook SHA in one audit snapshot:

`62c4d3bd8d88b6c258aed39cb883e712c16cf345b807731453014e448a8e2414`

### `BioInspired_Construction_Evidence_Extraction_v1.0_BIO58_Evidence_Rigor.xlsx`

Later evidence-rigor workbook with strengthened focal metrics and more audit entries.

### `BIO58_Evidence_Rigor_Audit.json`

This is the strongest later audit state preserved in this memory folder.

Reported key state:
- assessment tools: 3;
- tool inputs: 8;
- engineering performance: 3;
- sustainability outcomes: 8;
- linkages: 2;
- validation: 2;
- audit log: 12;
- residual indentation: 0.14 mm;
- permanent thickness change: 0.02 mm;
- S-LCA discussed only, not implemented;
- direct numeric sustainability output not anchored;
- M gate = U / PROVISIONAL HOLD;
- workbook SHA-256 reported by the audit:
  `443c434c8be67b62d743be0a75f43139738d7618b40b51c8a5ab5981e6abe59f`.

### `BIO58_v1.0_PrimarySource_Audit.json`

Multiple snapshots exist in File Library. They consistently preserve:
- schema frozen unchanged;
- primary-source content audited;
- no fabricated PDF page numbers;
- focal PDF binary not available in accessible evidence;
- page-level verification pending.

One reported audited-workbook SHA-256:

`9a2c24cfe169dadb30965f4f65052d041fd9fc3f04a03064e489123880aa1127`

## E. 26-paper high-rigor re-audit

Filename:

`BIO_26_High_Rigor_Reaudit_Stage3.xlsx`

Latest Stage 3 summary preserved in chat/File Library:
- total legacy synthesis papers re-audited: 26;
- confirmed KLM PASS: 1;
- definitive FAIL: 23;
- provisional HOLD: 2;
- confirmed survivor: BIO55;
- priority hold: BIO58;
- full-text hold: BIO65;
- scaling rule: only KLM PASS papers proceed to detailed evidence/PFSD/scoring.

This later re-audit supersedes older assumptions that many of the 26 studies directly implemented sustainability assessment.

## F. Earlier 10-paper evidence-first package

The same chat referenced a separate 10-paper engineering-sustainability workflow and these artifacts:

- `Top10_Evidence_First_Extraction_Corpus.xlsx`
- `Top10_Evidence_First_Extraction_Package.zip`
- `Top10_Evidence_First_Extraction_Audit.json`

They belong to a separate corpus/workstream and must not be silently merged into the bio-inspired review.

## G. Presentation artifacts

Source template:

`0-Cognition X lab ppt template-updated.pptx`

White-background variant:

`Cognition_X_Lab_Template_White_Background.pptx`

Presentation artifacts are downstream communication assets, not scientific evidence.

## H. Zotero artifact

`07_ZOTERO_TOP10_SUBCOLLECTION.js`

Purpose: identify the earlier 10-paper reference set by DOI/title and add uniquely matched parent items to a subcollection without deleting or moving items.

## I. Binary-storage note

This GitHub archive prioritizes reproducible text/state and hashes. Some binary artifacts are stored in ChatGPT File Library/runtime rather than duplicated into this branch. The hashes and filenames above are therefore essential identity anchors.

If binaries are later copied into GitHub/LFS, their SHA-256 must be checked against this manifest and any mismatch must be logged rather than silently accepted.