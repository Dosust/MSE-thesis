# Module 02 — Transformer Thermal Parameter Identification and State Estimation

**Status:** ACTIVE — P11 primary-HTML, P12 abstract-qualified, P13 primary open-access indexed-method/results audit; P14–P20 pending.  
**Parent:** `project/THERMAL_200_PAPER_SCHOOL_V3_1_EVIDENCE_CONTROLLED.md`  
**Rule:** Better temperature prediction does not establish unique parameters, full-state observability, capability limits, or cross-equipment validation.

## Objective

Determine which reduced transformer thermal states/parameters can be identified or estimated from the accessible measurements under variable load, ambient temperature, and cooling, with uncertainty and independent validation.

## Current first-paper checkpoint

**P11:** Souza et al. (2026), `10.3390/en19174224` — field measurements and ambient-dependent IEC top-oil parameterization. Test MAE **2.03°C**, RMSE **2.56°C**, versus globally optimized fixed-parameter errors **3.11°C** and **4.00°C**.

**Hard limitation:** Fitted coefficients are *effective* and possibly nonidentifiable, not intrinsic transformer physics; ONAN ambient dependence is weak; one transformer, TOT only.

**Source:** `MODULE_02_PAPER_AUDIT_P11_V1.md`

## P12 checkpoint — Chen & Su (2013)

**P12:** `10.1002/tee.21862` — proposes a differential/discrete Kalman-filter hottest-spot estimator, reporting laboratory heat-run and large-transformer comparison with measurements and historical IEEE Annex G. **Only publisher metadata + abstract directly verified**; exact equations, observation/noise model, numerical errors, formal observability and external applicability remain OPEN.

**Source:** `MODULE_02_PAPER_AUDIT_P12_V1.md`

## P13 checkpoint — Liu et al. (2024)

**P13:** `10.1016/j.csite.2024.104444` — POD/cascade-network steady 3D winding temperature reconstruction. **Maximum HST-model-versus-CFD error: 3.31 K** across 40 tested conditions; separate DOFS-measured winding-profile comparison errors: **3.36–3.97 °C** by winding. The 3.31 K value is *not* a measured global HST prediction error. Spatial measurement support exists, but steady-state surrogate does **not** prove dynamic observer validity, global maxima observability or thermal-state sufficiency.

**Source:** `MODULE_02_PAPER_AUDIT_P13_V1.md`

## Decision-control ledger

| Object | Status |
|---|---|
| Ambient temperature as input forcing | ADMITTED CONCEPT; never internal thermal state by default |
| Top-oil temperature as reduced thermal state | CANDIDATE |
| Ambient/cooling-dependent effective parameters | CANDIDATE CONSTITUTIVE/PARAMETERIZATION, not a new state |
| Unique physical thermal parameters | OPEN |
| Hottest-spot estimator mechanism | CONCEPT SUPPORT [A4], P12 abstract-qualified; exact observer OPEN |
| Spatial HST surrogate versus CFD | CONCEPT AND CASE-SPECIFIC ERROR SUPPORT [A4], P13; not independently global-HST validated |
| Distributed winding-profile comparison | CASE-SPECIFIC MEASUREMENT EVIDENCE [A3], P13; 3.36–3.97°C reported error |
| Global HST observability/measurement uncertainty | OPEN — P13 does not establish true global-maximum observability |
| Cross-transformer/extrapolation accuracy | OPEN |
| Dynamic model-state sufficiency | OPEN |
| Thermal-state-to-capability map | OPEN, standards/equipment authority required |

## Evidence-density / non-invention

More information ≠ better information. Source-specific numbers, applicability, quantitative error, limitations, and admission consequence matter. No numerical law, standard clause or limit is frozen from an unverified equation or a single case.
