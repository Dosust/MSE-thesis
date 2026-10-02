# Physics-Based Mathematical Engineering — 200 → 26 Literature Screen

This folder archives the reproducible literature-screening package for the MSE thesis:

**Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**

## Guiding research question

> How do time-varying physical states and interdependencies between Power and Transportation systems determine service degradation and recovery under extreme heat, and how can targeted operational interventions reduce the resulting coupled service deficits?

## Review philosophy

The review does **not** search for a gap first. It reconstructs the existing science and then evaluates where a justified methodological adaptation may be needed:

`FRAMEWORK → METHOD → FINDINGS → LIMITATIONS → SYNTHESIS → CONTRIBUTION`

A strict distinction is maintained between:

- author-stated limitations;
- limitations inferred by this thesis;
- candidate thesis contributions.

## Screening result

- **200 records screened**
- **26 priority papers retained for full-text deep extraction**
- Evidence roles: **5 Foundations + 9 Coupled P–T + 9 Heat/Physical State + 3 Intervention/Recovery**

The final 26 are a **priority evidence set**, not proof of novelty or a definitive research gap. Any gap/contribution claim must follow full-text extraction and synthesis.

## Files

- `Physics_Based_Mathematical_Engineering_200_to_26.xlsx` — evidence workbook and deep-extraction template.
- `thesis_screen_200.csv` — full 200-record screening table.
- `thesis_shortlist_26.csv` — 26-paper priority evidence set.
- `thesis_shortlist_26.json` — machine-readable 26-paper set.
- `screen_200.py` — Python screening and workbook-generation pipeline.
- `verify_screen_200.js` — independent JavaScript audit of the 200 → 26 result.
- `MANIFEST.sha256` — file integrity hashes.

## Scientific status

The screening is a reproducible triage and evidence-architecture step. The next mandatory stage is full-text extraction of, for each priority paper:

1. framework;
2. mathematical/physical method;
3. data and parameters;
4. experiment;
5. findings;
6. assumptions;
7. author-stated limitations;
8. validation;
9. thesis relevance (adopt / adapt / compare / avoid);
10. candidate improvement, only after synthesis.
