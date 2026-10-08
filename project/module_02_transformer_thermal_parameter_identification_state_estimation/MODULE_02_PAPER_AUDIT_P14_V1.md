# Module 02 — P14 Audit V1: Transient Winding Temperature-Field Reconstruction from Sparse Sensors

**As of:** 2026-10-08
**Status:** PRIMARY-PUBLISHER INDEXED ABSTRACT + SELECT METHOD/EXPERIMENT SECTIONS AUDITED; FINAL FULL-TEXT EQUATION/UNCERTAINTY AUDIT OPEN
**Evidence authority:** `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`
**Admissible claim classes:** [A4] reduced-order reconstruction methodology; [A3] prototype measurements at verification points. **Not** a numerical transfer authority.

## Bibliographic identity
Li, Jiahao; Wang, Qingyu; Liu, Chuang; Gao, Zhijie; Liu, Peng; Wu, Zehua; Cheng, Jianwei; Zeng, Qiang (2026).
**A real-time calculation method for transformer winding global temperature field.**
*Electric Power Systems Research*, **257**, 113033.
**DOI:** https://doi.org/10.1016/j.epsr.2026.113033
**Publisher:** https://www.sciencedirect.com/science/article/pii/S0378779626003263
Publisher index exposes the abstract, methods overview and experimental setup; direct browser fetch returned a 403. Therefore **not** full independent equation-by-equation audit.

## Actual study and measurements
- **Goal:** online **transient spatial winding-temperature-field reconstruction** from a limited number of discrete winding sensors.
- **Architecture:** high-fidelity transient CFD snapshots -> proper orthogonal decomposition (POD) spatial modes -> greedy sensor-location selection optimizing conditioning/noise robustness -> sparse observations -> Gappy-POD least-squares modal coefficients -> reconstructed field.
- **Physical prototype:** manufacturer study reports a **630 kVA/10 kV oil-immersed transformer** temperature-monitoring platform. Physical verification points are referenced. Exact independent sensor count, coordinates, calibration, uncertainties, temperature range, and holdout independence are **not independently resolved** from accessible text.
- **Comparison 1 (A4):** publisher highlights report simulation reconstruction maximum absolute errors **<= 0.4 °C**. The comparator is modeled field data, **not** a directly observed global spatial maximum.
- **Comparison 2 (A3):** publisher highlights report experimental **MAE 1.95 °C and 2.14 °C** against sensor measurements. The two error groups' exact measurement-location definitions and sample sizes remain OPEN in accessible indexed sections; never label either number as **global HST MAE** without locating the corresponding figure/table.
- **Computational result:** **~0.015 s reconstruction time per step**, **not** physical thermal response time, measurement period or hazard-transition time.
- **Noise claim:** greedy placement explicitly targets reduced reconstruction sensitivity to measurement noise. Exact noise distributions/magnitudes, covariance, perturbation protocol, independent repeated tests and quantified confidence bounds require full-equation/result verification.

## Scientific distinctions / [T1] thesis interpretation (NOT author equations)

Let `T(x,t)` be the true transformer winding temperature field, `y_j(t)` the measured sensor temperatures, and `hat T(x,t)` the reconstructed field. A **thesis-defined** candidate hottest-spot estimator is

~~~math
\widehat{\theta}_{HS}(t)=\max_{x\in\Omega_w}\widehat T(x,t).
~~~

The physically intended maximum is

~~~math
\theta_{HS}(t)=\max_{x\in\Omega_w}T(x,t).
~~~

Thus:

~~~text
small modeled-field reconstruction error ≠ small physical global-HST error
validation at sensor verification points ≠ global field observability
fast online calculation ≠ validated transient switching/threshold time
POD modal coefficients ≠ independent physical dynamic state variables
conditional noise robustness ≠ measured sensor-placement universality
temperature reconstruction ≠ transformer allowable capability
~~~

The paper provides *field reconstruction*, not proof of formal dynamic observability, uniqueness of the inverse map, a closed-form stochastic error bound or a validated capability map for the eventual case.

## Admission
- **ADMITTED CONCEPT [A4+A3]:** transient spatial winding-field reconstruction using sparse physical measurements, subject to source- and architecture-specific validation.
- **CANDIDATE:** Gappy-POD for a future higher-fidelity spatial estimator if simple HST prediction fails the thesis's decision-relevant fidelity tests.
- **OPEN:** independently quantified actual **global** HST error; formal observability; transient extreme-heat transition timing; selected ONAN/ONAF architecture parameter transfer; load/harmonic scenarios; estimator uncertainty and measurement noise bounds.
- **NOT ADMITTED:** numerical 0.4/1.95/2.14 °C error values as universal thermal accuracy; 15 ms as state-evolution timescale; extra dynamic states automatically; state-to-electrical capability mapping.

**No Power-side thermal model freeze.** `X_{P,th}=[theta_TO,theta_HS]^T` remains **CANDIDATE — NOT FROZEN**.

## Next source-qualification gates
1. Acquire publisher or lawful author full text and verify exact observation matrices, sensor positions, operating profiles, noise injections and error definitions.
2. Require **independent sensors reserved from the reconstruction fit** and an explicit global-max error estimate or spatial uncertainty bound.
3. Compare reduced top-oil/HST model and spatial reconstruction on *the same transient extreme-heat/load profiles* before introducing additional physical dynamic states.
4. Establish state-to-capability laws separately from applicable current standard and exact equipment authority.

**Key result:** spatial/transient reconstruction is feasible for the tested setup; **true-global-hottest-spot observability and capability consequences are not established by the reported mean sensor errors**.
