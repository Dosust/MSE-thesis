# NUS 30-paper Excel research release — 2026-10-23
Curator: **Dossiya Dakou**

**Private repository release.** The original approved 24 paper records remain preserved, subject only to the documented NUS-52 reliability notation corrections. Original journal PDFs are not redistributed.

## Fast access

- **Complete Excel workbook in Google Drive:** https://drive.google.com/file/d/1Bna09kYpeGE6rRJycIMhp03DuAuoBFiT/view
- **Algorithm and audit ZIP in Google Drive:** https://drive.google.com/file/d/1jNDgCw8ytgBkl4OzDYkLqHFhwuL7zcp_/view
- SHA-256 of final workbook: `cba6747c1c18e83f4a86677d1971bdbc010b9e7f7c61d0060b75f358ddea550a`

## Exact workbook in GitHub

The 14 MB workbook is held as **10 ordered binary Git objects** in `workbook_parts/`; this avoids the connector's single large-upload limitation. These parts reconstruct the **exact same XLSM file**, not a conversion or recomputation.

```bash
python reassemble_workbook.py
```

The script verifies SHA-256 before accepting the reconstructed workbook.

## Contents

- `nus_lp_constraint_corrector.py`: source-preserving MILP/HiGHS notation corrector, strict invariants.
- `NUS_LP_Audit_Report.md` and `NUS_Independent_Baseline_and_LP_Assurance.md`: independent QA.
- `Previous_15_Issue_Disposition_Source.csv` and `Fifteen_Issue_Resolution.csv`: issue register.
- `Corrected_24_Sentence_Provenance.csv`: six-new-paper evidence classification.
- `Six_Paper_Engineering_to_Sustainability_Crosswalk.csv`, `Sustainability_and_SDG_Classification.csv`: implemented-method boundaries.
- `Comment_Placement_Register.csv`, `figure_provenance.csv`: placement documentation.

## Preservation

30 research records, 75 embedded figures, 75 author-labeled notes with distinct review timestamps. **No new rows, columns or worksheets.** The latest LP selected three notation-only updates: NUS-52 at `visual and general!C95`, `Verified!C15`, and `Verified!E15`. A prior alignment already corrected `Verified!I15`.

## Qualifications and release boundaries

**NUS-153 remains on source-integrity/provenance hold.** Published results were not all independently reproduced. Other papers retain source-level scope and metric-comparability qualifications. Validation certifies documented workbook integrity and limited notation edits, not scientific infallibility. The 7 pending papers are outside scope.

This repository is private; permission to publicly redistribute extracted journal figures is not asserted.
