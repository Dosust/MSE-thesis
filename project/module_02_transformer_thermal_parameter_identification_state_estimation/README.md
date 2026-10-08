# Module 02 — Transformer Thermal Parameter Identification and State Estimation

**Status:** ACTIVE — P11 evidence audited at publisher-full-HTML level; P12–P20 pending.  
**Parent:** `project/THERMAL_200_PAPER_SCHOOL_V3_1_EVIDENCE_CONTROLLED.md`  
**Rule:** Better temperature prediction does not establish unique parameters, full-state observability, capability limits, or cross-equipment validation.

## Objective

Determine which reduced transformer thermal states/parameters can be identified or estimated from the accessible measurements under variable load, ambient temperature, and cooling, with uncertainty and independent validation.

## Current first-paper checkpoint

**P11:** Souza et al. (2026), `10.3390/en19174224` — field measurements and ambient-dependent IEC top-oil parameterization. Test MAE **2.03°C**, RMSE **2.56°C**, versus globally optimized fixed-parameter errors **3.11°C** and **4.00°C**.

**Hard limitation:** Fitted coefficients are *effective* and possibly nonidentifiable, not intrinsic transformer physics; ONAN ambient dependence is weak; one transformer, TOT only.

**Source:** `MODULE_02_PAPER_AUDIT_P11_V1.md`

## Decision-control ledger

| Object | Status |
|---|---|
| Ambient temperature as input forcing | ADMITTED CONCEPT; never internal thermal state by default |
| Top-oil temperature as reduced thermal state | CANDIDATE |
| Ambient/cooling-dependent effective parameters | CANDIDATE CONSTITUTIVE/PARAMETERIZATION, not a new state |
| Unique physical thermal parameters | OPEN |
| Hottest-spot state estimation/observability | OPEN — P11 does not establish |
| Cross-transformer/extrapolation accuracy | OPEN |
| Dynamic model-state sufficiency | OPEN |
| Thermal-state-to-capability map | OPEN, standards/equipment authority required |

## Evidence-density / non-invention

More information ≠ better information. Source-specific numbers, applicability, quantitative error, limitations, and admission consequence matter. No numerical law, standard clause or limit is frozen from an unverified equation or a single case.
