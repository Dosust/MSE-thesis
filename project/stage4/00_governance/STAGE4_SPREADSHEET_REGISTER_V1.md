# Stage 4 Spreadsheet Register v1

**Status:** CANONICAL structured-register index  
**Date:** 2026-09-19

## 1. Master scientific register

`project/stage4/02_constitution/STAGE4_MASTER_SCIENTIFIC_REGISTER_V1.xlsx`

This is the primary structured Stage-4 workbook. It contains the canonical and case-facing registers needed to govern Stage 4, including:

1. `00_Dashboard`
2. `01_Authority`
3. `02_Canonical_Objects`
4. `03_State_Ontology`
5. `04_Case_Binding`
6. `05_Measurements`
7. `06_Estimation_UQ`
8. `07_Information`
9. `08_Organization`
10. `09_Feasible_Control`
11. `10_H2_Scenarios`
12. `11_H2_QOIs`
13. `12_Gates`
14. `13_Claim_Ceiling`
15. `14_Stage5_Handoff`
16. `15_Literature_Evidence`
17. `16_Provenance`

The master workbook is subordinate to the Markdown authority files in `00_governance/`; it is not allowed to silently redefine the Stage-4 scientific constitution.

## 2. Case observability workbook

`project/stage4/03_cases/greensboro_greenevt_smartds/01_observability/STAGE4_CASE_STATE_OBSERVABILITY_REGISTRY_V2.xlsx`

This workbook is a **case-realization register**. It must not be interpreted as the canonical definition of required Stage-4 objects.

## 3. Separation rule

`canonical requirement != case realization != gate result != validation status`

The master workbook therefore tracks, where relevant, separate epistemic, data-realization, gate, and validation statuses.

## 4. Current closure status

- `G4-CON = PASS`
- `G4-CASE = BLOCKED`
- `G4-V = BLOCKED`
- `G4-H2 = BLOCKED / NOT TESTED`
- `G4->5 = BLOCKED`

Thus the Stage-4 **architecture and files are finalized v1**, while the empirical Stage-4 science is not closed.
