# Module 02 — Paper Audit P12 V1: Hottest-Spot State Estimation and Observability Boundary

**Status:** VERIFIED PUBLISHER METADATA + ABSTRACT; **FULL-TEXT EQUATION/NUMERICAL AUDIT OPEN**  
**Date:** 2026-10-08  
**Governing authority:** `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`

## P12 — Chen & Su (2013)

**Title:** Application of Kalman filter to hot-spot temperature monitoring in oil-immersed power transformer  
**Authors:** Weigen Chen; Xiaoping Su  
**Journal:** *IEEJ Transactions on Electrical and Electronic Engineering*, 8(4), 322–327  
**Publication:** first published 2 May 2013; July 2013 issue  
**DOI:** https://doi.org/10.1002/tee.21862  
**Primary publisher:** https://onlinelibrary.wiley.com/doi/abs/10.1002/tee.21862  
**Access-depth limit:** publisher bibliographic record, published abstract and references; independent full article/equations/tables were **not accessed**. Wiley Scholar Gateway full-text connector returned an internal error; it is not evidence of full-text content.

**Evidence classification:** [A4] proposed HST differential/discrete state estimator; [A3] publisher-abstract-reported laboratory heat-run and field application. **Abstract-qualified mechanism/validation claim only; no numerical model admission.**

## What is source-supported

1. The focal authors **present** a winding HST differential prediction equation accounting for top-oil variation and load thermal dynamics.
2. They construct a **discrete Kalman-filter real-time HST estimator** from that model.
3. They report a laboratory transformer heat-run test and application to a large operating power transformer.
4. The published abstract reports estimated HST values closer to measured values than the classical **IEEE Annex G** comparator in the cases presented.

**Neither the exact equation nor the magnitude of improvement is available in the accessed primary evidence.** The comparator is historical; this paper does not authorize use of the cited older standard as the thesis's current normative loading authority.

## Crucial scientific distinctions

- A **state estimate** is model-and-observation dependent; it is not an independent direct temperature reading.
- Measurements at installed sensor positions are **local observations**, not automatically the true spatial winding maximum. P08/P09 demonstrate why location matters. Therefore neither the use of Kalman filtering nor reported estimation agreement establishes global hottest-spot observability.
- **Numerical convergence, filtering improvement, observability, parameter identification and external validation are distinct claims.**
- Laboratory/field examples do not automatically validate the same measurement function, cooling architecture, load harmonics, extreme ambient range, or equipment-specific state-to-capability conversion needed in the thesis.

## Required evidence still OPEN — no guessing

| Gate | Status |
|---|---|
| Exact differential and discrete state/observation equations | OPEN: publisher full text needed |
| Which signals were direct observations, controls, inputs, or estimated states | OPEN |
| Sensor type, count, coordinates and measurement uncertainty | OPEN |
| State/measurement dimensions, sampling period, system matrices | OPEN |
| Process/measurement-noise covariance, initialization, filtering assumptions | OPEN |
| Formal observability or identifiability test | NOT ESTABLISHED in accessed abstract |
| Quantitative KF-versus-IEEE-Annex G error metrics, holdout protocol | OPEN |
| Independent external-transformer and extreme-heat validation | NOT ESTABLISHED |
| Estimator accuracy for true **spatial global** hottest spot | NOT ESTABLISHED |
| Current-standard thermal limits and state-to-capability map | OPEN |

No numbers, matrices, covariance choices, confidence intervals, observability ranks or model equations are inferred.

## Thesis transfer and decision

**Supported concept [A4, abstract-qualified]:** A time-updated mathematical HST state estimate may be constructed by coupling a reduced thermal dynamics model with observations. This makes a future estimator for `theta_HS` a **candidate research design**, not a proven observer for the final transformer.

**Explicit [T1] interpretation, NOT an author equation:** an estimate `hat(theta_HS)(t)` and actual (spatial) winding maximum `max_{x in Omega_w}T(x,t)` must be kept distinct until sensor coverage, observation mapping, model validation and uncertainty justify their relationship.

### Admission ledger

~~~text
Kalman-filter HST estimation:  ADMITTED CONCEPT / MECHANISM EVIDENCE ONLY
Exact P12 state/observation equations: OPEN
Formal observability of theta_HS:      OPEN
Parameter transfer:                    NOT AUTHORIZED
Extreme-heat estimation quality:       OPEN
Capability C_P or a derating law:       OPEN
X_P,th = [theta_TO,theta_HS]^T:         CANDIDATE — NOT FROZEN
~~~

**Next priority:** full primary-text audit or a separate verified full-access HST observer experiment with exact equations, sensor geometry, observation/noise model, quantitative holdout errors and an explicit observability/validation analysis. Do **not** substitute a cited related paper's measurements for Chen & Su's focal results.

**Governing conclusion:** **An HST estimator is not evidence that the global hottest spot is observable or that the resulting temperature estimate may be converted into allowable electrical capability.**
