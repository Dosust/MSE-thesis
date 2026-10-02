# Physics-Based Mathematical Engineering — 200 → 26 Literature Screen

This folder archives the high-rigor literature-screening package for the MSE thesis:

**Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**

## Guiding research question

> How do time-varying physical states and interdependencies between Power and Transportation systems determine service degradation and recovery under extreme heat, and how can targeted operational interventions reduce the resulting coupled service deficits?

## Review philosophy

The review does **not** search for a gap first. It reconstructs the existing science and then evaluates where a justified methodological adaptation may be needed:

`FRAMEWORK → METHOD → FINDINGS → LIMITATIONS → SYNTHESIS → CONTRIBUTION`

A strict distinction is maintained between:

- **author-stated limitations**;
- **limitations inferred by this thesis**;
- **candidate thesis contributions**.

## Screening result

`200 screened → 26 priority papers for full-text extraction`

Evidence architecture:

- **5 Foundations**
- **9 Coupled Power–Transportation**
- **9 Heat / physical-state**
- **3 Intervention / recovery**

The final 26 are a **priority evidence set**, not proof of novelty and not a definitive research gap. Any gap or contribution claim must follow full-text extraction and synthesis.

## Repository files

- `thesis_screen_200.csv` — canonical archived 200-record screening table.
- `thesis_shortlist_26.csv` — human-readable 26-paper priority evidence set.
- `thesis_shortlist_26.json` — machine-readable 26-paper priority evidence set.
- `screen_200.py` — self-contained reproduction and integrity check of the 200 → 26 selection.
- `verify_screen_200.js` — independent JavaScript audit of counts, DOI uniqueness, and evidence-role coverage.
- `build_evidence_workbook.py` — rebuilds the formatted XLSX evidence workbook from the archived CSV files.
- `WORKBOOK_SHA256.txt` — checksum of the workbook generated during the original screening run.
- `MANIFEST.sha256` — provenance/checksum note for generated artifacts.

## Generated workbook

The XLSX is treated as a **generated artifact**, not the canonical evidence source. This avoids committing a redundant binary file when the exact evidence tables are already stored as text.

Build it from this directory:

```bash
python screen_200.py
python verify_screen_200.js
python build_evidence_workbook.py
```

Original generated workbook:

`Physics_Based_Mathematical_Engineering_200_to_26.xlsx`

SHA-256:

`a168d45494fccb41f30ef606d1899db206ec0877e259bac5512f9a52d9fa3a80`

## Mandatory next stage

For every priority paper, extract and verify from full text:

1. conceptual framework and system boundary;
2. mathematical method;
3. physics represented;
4. data / parameters;
5. experiment or case study;
6. findings and conditions of validity;
7. assumptions;
8. **author-stated** limitations;
9. validation evidence;
10. thesis relevance: adopt / adapt / compare / avoid.

Only after this synthesis should a methodological improvement be promoted to a thesis contribution.

## Scientific status

This package supports the thesis literature-review rule:

> **Do not search for a gap first. Understand the existing science first.**
