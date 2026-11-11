# Advanced experimental execution: transformer thermal dynamics, stochastic charging and scientific boundaries

**Date:** 2026-11-11. **Title:** Engineering of Power–Electrified Transportation Interdependencies for Resilience.  
**Status:** Assistant-executed exploratory numerical research; **NOT** a validated coupled transformer-EVSE field experiment; **NOT** independently reproduced student work or supervisor-approved final thesis content.

## Headline original-data numerical findings

1. **Transformer dynamics, SINTEF:** 8,592 original hourly records; 6,012 contiguous one-hour training pairs and 2,576 test pairs. The physics-motivated first-order temperature model obtained **0.2165 °C RMSE** versus **0.2517 °C** persistence, but MAE was **0.1499 °C** versus **0.1450 °C**, so the RMSE gain is not unqualified improvement.
2. **New timing-sensitivity test:** Across **106** 24-hour SINTEF holdout windows, changing only the temporal ordering of *measured* current while preserving its 24-hour sum of squared current changed the first-order model's final temperature by **0.355 °C** median absolute difference (front-loaded versus back-loaded). This is a within-transformer, model-based counterfactual, **not EV charging causal evidence**.
3. **Thermal parameter nonstationarity:** Effective one-hour-model tau across Jan–Apr / May–Aug / Sep–Dec was **15.98, 8.29, 13.57 hours**. Calendar variation does not independently establish structural non-identifiability; the local standardized one-step sensitivity matrix had condition number **2.42**, so a simplistic claim of universally singular parameters would be false.
4. **Sensor semantics:** The SINTEF channel labeled HV winding 'hot-spot' is lower than measured top oil in **84.1%** of paired observations; LV 'hot-spot' is lower in **70.9%**. An insulation aging-life claim based on these labels remains **BLOCKED** pending sensor-definition and transformer insulation/aging-law qualification.
5. **EPFL stochastic demand:** **1,878** original sessions on two connectors. Of these, 1,865 are entirely within one observed calendar day, spread over **221** observed days. Mean daily maximum simultaneous sessions: **1.706**, with a conditional day-block bootstrap interval **[1.643, 1.765]**. This quantifies observed sample variability, not EV penetration effects.
6. **EPFL LP reproduced:** A separate code replay reprocessed the original measurement XLSX, matched all **1,878** session IDs, and verified the 16-high-use-day median **44.01%** hypothetical peak reduction relative to a separately modeled *front-load* comparator. It is **not** a measured before/after benefit.
7. **Electrical/battery evidence:** KU Leuven archive contains **40,873** charging observations, with 12 observed backward timestamp steps across files. STREAM has **419,184** matched time-station P/Q numeric pairs with source units/ratings still unqualified.
8. **Chronological residual coverage:** Under a *new* first-60% training, next-20% calibration, last-20% evaluation scheme, a nominal 90% absolute-residual band covered **95.3%** of later observations. Temporal dependence, model discrepancy and changing conditions prohibit treating this as a guaranteed prediction interval.

## Central inference

The data establish *component-level observation* and support exploratory reduced-order thermal dynamics, scheduling optimization, and variability analysis. The strongest newly executed physics-centered test isolates within-transformer **load-order sensitivity** under fixed squared-current integral, exposing why a time-state model can matter beyond an aggregate peak or aggregate load measure. However, no original Drive measurement maps this transformer to the EPFL charger or independently proves a thermal power-to-transportation feedback or observed service shortfall. **Aging-life claims, temperature-constrained EV charging, 30°C-plus extreme-heat validation, and harmonic aging remain evidence-blocked.**

## Eight reports and reproducibility

- `01_ORIGINAL_DATA_AUDIT.md`: source hashes, eligibility, instrumentation and blockers.
- `02_EQUATIONS_AND_HYPOTHESES.md`: model formulation, parameter semantics, numerical and falsification tests.
- `03_SINTEF_THERMAL_HOTSPOT_AND_AGING.md`: within-transformer experiments and qualified sensor interpretation.
- `04_EPFL_STOCHASTIC_CHARGING.md`: session-level joint dependence and day-block bootstrap.
- `05_MATCHED_OPTIMIZATION_GATE.md`: offline LP replay and thermal-objective blocker.
- `06_STREAM_KU_HARMONIC_EVIDENCE.md`: source-measurement characteristics and power/thermal boundaries.
- `07_VVUQ_IDENTIFIABILITY.md`: Jacobian profile, chronological coverage, ODE numerical test.
- `08_FINDINGS_SO_TRACEABILITY_AND_NEXT_GATES.md`: SO1/SO2/SO3, paper transferability, roadmap.

Runnable source `../thermal_extension_20261111_v2.py`, independent original XLSX replay `epfl_reproduce.py`, `RESULTS.json`, `ORIGINAL_INPUT_MANIFEST.json`, and figures/csv summaries are included in the ZIP. **Raw original empirical datasets excluded**; original paths and SHA-256 are included in the source manifest.

## Source and authority references

- SINTEF original monitored transformer sensor file, checksum in `ORIGINAL_INPUT_MANIFEST.json`; data description: [Bærug transformer measurements](https://doi.org/10.5281/zenodo.17223516). User-owned original Drive record, not redistribution.
- EPFL original `Measurement_data.xlsx` and `Session_data.xlsx` user-owned Drive copies. See previously audited source register in GitHub. 
- KU Leuven C5PT0R measured EV charging efficiency original archive, authenticated Drive copy. 
- STREAM Slovenia 2025 active/reactive transformer-station monitoring CSV copies, authenticated Drive archive.
- [Qian, Zhou & Yuan (2015), DOI 10.1016/j.ijepes.2014.09.040](https://doi.org/10.1016/j.ijepes.2014.09.040) (abstract and user-supplied summary; full methodological reproduction not claimed).
- [Visakh & Selvan (2022), DOI 10.55730/1300-0632.3819](https://doi.org/10.55730/1300-0632.3819) (published charging scheduling/aging method; no exact reproduction).
- [Pavlićević & Mujović (2022), DOI 10.3390/en15197085](https://doi.org/10.3390/en15197085) (power flow and transformer aging methodology; no exact reproduction).
- Gómez & Morcos (2003), *Impact of EV battery chargers on the power quality of distribution systems*, IEEE Transactions on Power Delivery 18(3), 975–981. Original harmonic spectra required for transfer to Drive data.
- Nishanth (2026), *Physics-Informed Neural Networks for Transient Thermal Analysis and Insulation Life Assessment in Power Transformers*, DOI 10.1109/NE-IECCE69680.2026.11665934. Only available abstract-level method information; AI/PINN is excluded under this thesis's physics-first authority.
- GitHub current authority: [thesis title V3](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THESIS_TITLE_V3.md); [objectives SO1–SO3](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md); [evidence non-invention standard](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md); [physics first scope](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/PHYSICS_MATHEMATICS_FIRST_HYPOTHESIS_TESTING_SCOPE_DIRECTIVE_V1.md).
