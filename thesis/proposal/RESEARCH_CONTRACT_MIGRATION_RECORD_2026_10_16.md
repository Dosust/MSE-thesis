# Evidence provenance and contract-migration record — 2026-10-16

**Status:** review-support record; does not itself confirm scientific novelty or final proposal approval.

## Historical contract archive
`thesis/proposal/README.md` and `thesis/proposal/PROPOSAL_RELEASE_CHECKLIST.md` previously referenced `CANONICAL_RQ_SO_HYPOTHESES_V3.md`, the seven-stage framework, old RQ1–RQ7, SO1–SO7 and H1–H5. The exact prior-main copies are preserved under `thesis/proposal/archive/` in this branch. The present draft replaces them with the current thermal-only GO/SO1–SO3 and working W-RQ1–3. No old hypotheses or earlier scientific claims have been silently carried forward into the active proposal.

## Methodological distinctions
- Scope files are **governing thesis definitions**, not empirical validation.
- Publisher original PDFs are stronger sources for paper-specific equations than snippets; a paper with field data inputs may still compare predictions against **simulated internal temperature fields**.
- Krama experimental results are publisher-abstract verified; its full authenticated PDF and raw logs remain inaccessible. Avoid copying third-party transcription regression coefficients into proposal methods.
- EV-EcoSim is established simulation prior art and the inspected preprint is not automatically the audited IEEE journal version.
- Four research databases have **not actually been searched using authenticated interfaces**; neither a novelty conclusion nor PRISMA completeness follows from the pilot.
- No synchronized transformer–EVSE time-series dataset has been opened. “Not located in pilot” is **NOT** “does not exist.”
- All numerical operating parameters, threshold temperatures and capability laws must be sourced from exact equipment/standard or fitted under transferable experimental conditions.

## Source-level provenance checkpoints

| Reference | DOI and audited access level | Valid prior-art conclusion | Excluded extrapolation |
| --- | --- | --- | --- |
| Godina et al. (2016) | [P008: DOI](https://doi.org/10.1016/j.enconman.2016.04.087), Original publisher-version PDF text inspected in pilot follow-up | Real baseline load/transformer parameters + modeled EV charging → simulated transformer thermal aging and hot-spot dynamics | Not direct measured EVSE–transformer same-site thermal causal validation, not observed winding HST and trips |
| Blomgren et al. (2023) | [P002: DOI](https://doi.org/10.1016/j.segan.2023.101048), Original publisher-version PDF text inspected | Measured feeder/transformer temperatures and aggregate current; grey-box thermal identification/prediction including uncertainty; main measured target is lid temperature | Does not validate a measured winding global hot spot, identify EV charger contribution, or supply matched mobility data |
| Bragone et al. (2022) | [P003: DOI](https://doi.org/10.1016/j.epsr.2022.108447), Original publisher-version PDF text inspected | 1D transformer heat equation PINN with measured operating/boundary inputs; evaluated against numerical finite-volume solution | Numerical interior thermal field reference is not directly measured field validation; PINN not shown superior to FVM here |
| Balogun et al. (2024) — EV-EcoSim | [P007: DOI](https://doi.org/10.1109/TSG.2023.3339374), Original arXiv author manuscript text inspected, journal article DOI verified, manuscript/publisher equivalence unverified | Existing joint EV charging–grid/transformer thermal and network co-simulation | Simulated grid-to-charging behavior is not a matched field thermal experiment; battery internal temperature states omitted in inspected author manuscript |
| Villarroel et al. (2017) | [P010: DOI](https://doi.org/10.1049/oap-cired.2017.1102), Publisher-indexed original article text; PDF file/figure pixel audit not completed | 200 kVA transformer experiment with internal optical HST sensors; calibrated temperature model independently checked on same transformer overload test | Not EVSE-to-distribution-transformer coupling data, not field extreme heat; raw measured data not downloaded |
| Krama et al. (2026) | [P001: DOI](https://doi.org/10.1016/j.ecmx.2026.101960), Original publisher abstract and HBKU record verified; original PDF/raw measurements unavailable | 50 kW DC fast charger tested under Qatar heat; rectifier temperature derating and extended charging time observed; data on request | No original PDF equation/figure audit or synchronized external distribution-transformer and mobility trip measurements established |

## Research decision gates
1. The frozen general and three objectives remain exact string authorities.
2. Working W-RQ1–W-RQ3, any hypothesis, state vector and method comparison design are **PROPOSED**, not a new freeze.
3. No raw measurement/calibration/simulation may be presented as the other's evidence tier.
4. Proposal may be reviewed now, **but release-ready status requires the separately documented supervisor/ASU/technical evidence gates**.
5. Stacked PR depends on completion of V3 title sync PR #85. Neither PR must be merged automatically.
