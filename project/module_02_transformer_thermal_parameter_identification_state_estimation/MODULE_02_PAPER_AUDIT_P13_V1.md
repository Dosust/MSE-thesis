# Module 02 — Paper Audit P13 V1: Spatial HST Reconstruction, Measured Error and Observability Boundary

**Status:** VERIFIED OPEN-ACCESS PRIMARY PAPER; PUBLISHER-INDEXED METHOD/RESULT SECTIONS AUDITED — FINAL PDF/EQUATION-BY-EQUATION VERIFICATION OPEN  
**Date:** 2026-10-08  
**Governing authority:** `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`  
**Admissible role:** [A4] reduced-order surrogate / spatial prediction; [A3] prototype winding-temperature measurements; **case-specific evidence only**.

## P13 — Liu et al. (2024)

**Authors:** Yunpeng Liu, Qingxian Zhao, Gang Liu, Ying Zou, Shuo Zhang, Kun Wang, Xingyuan Zhao.  
**Title:** A real-time solution method for three-dimensional steady temperature field of transformer windings based on mechanism-embedded cascade network  
**Journal:** *Case Studies in Thermal Engineering*, 58, 104444 (June 2024).  
**DOI:** https://doi.org/10.1016/j.csite.2024.104444  
**Primary source:** https://www.sciencedirect.com/science/article/pii/S2214157X24004751  
**Publisher access:** Open access under a Creative Commons license. Detailed publisher-indexed full-article sections (method, Tables 1/4, Sections 4.1–4.3, conclusion) were available to search; direct browser page fetch returned 403, so full PDF and exact equation-symbol transcription were **not** independently completed. No exact author numerical coefficient adopted.

## Why this source was selected over other candidates

The paper explicitly reports both a **hottest-spot-specific prediction error** and independent spatial winding **fiber-optic experimental comparisons**. Newer Li et al. (2026), DOI 10.1016/j.epsr.2026.113033, is valuable for *transient sparse-sensor reconstruction*, but its publicly surfaced 1.95/2.14 °C MAEs were not verified as errors specifically of the physical global winding hottest spot. P13 must not silently substitute general reconstruction MAE for HST validation.

## Scientific and experimental structure

**Target:** 3-D **steady-state** oil-immersed transformer winding temperature field; **not** transient thermal-state dynamics. Reported FOM geometry: **200 kVA, 35 kV/0.4 kV, ONAN**, with explicit winding/core geometry (Table 1).

**Method:**
1. Numerically solve heat-flow/temperature fields for multiple working conditions using a full-order CFD model (Fluent), assemble snapshots;
2. Proper orthogonal decomposition (POD) extracts spatial temperature modes;
3. A mechanism-embedded RBF-neural-network / multilayer-perceptron cascade maps working conditions to modal coefficients;
4. Reconstruct steady spatial field, then locate the modeled hottest point.

**Measurement:** a rated-load temperature-rise test on a **35 kV oil-immersed transformer** uses distributed Raman-scattering optical fibers laid closely along winding wires and secured with insulation paper. The recorded winding profiles are compared to reconstructed profiles (example: B phase). Top-oil temperature is measured by thermocouple; thermal stabilization condition reported as top-oil rise rate below **1 K/h for 2 h**. The paper divides each phase winding height into **100 virtual comparison positions**. These are **not equivalent to 100 independently documented physical temperature sensors**.

Sensor calibration/accuracy, positional uncertainty, independent sampling strategy and comprehensive test-range extreme-heat applicability were not independently confirmed at the necessary detail from the accessible sections.

## Quantitative claim audit — do not mix denominators

### A4: surrogate versus Fluent CFD, 40 held-out working conditions

| Quantity | Reported difference | Correct interpretation |
|---|---:|---|
| Full-field winding temperature rise | maximum mean absolute temperature difference **2.63 K** over evaluated cases | model-to-model, not physical measurement |
| Hottest-spot temperature | maximum absolute **3.31 K**; relative **3.16%** | surrogate versus CFD-derived maximum, **not direct true-global-HST error** |
| Hottest-spot location | maximum normalized distance **1.28%**, mean **0.71%** | normalized by geometry; location relative to CFD peak, not physical sensor-confirmed peak |
| Runtime per single steady solution | **0.0087 s** | computational speed, **not transient sampling rate**, thermal time constant, or event-time accuracy |

**Interpretation warning:** publisher says the whole-field `2.63 K` maximum for Eq. (20)'s spatial mean of nodewise absolute differences; do **not** rebrand as maximum pointwise error.

### A3: surrogate versus distributed optical-fiber winding measurements

| Measured winding domain | Maximum reported calculation difference |
|---|---:|
| Low-voltage winding | **3.95 °C** |
| High-voltage inner winding | **3.36 °C** |
| High-voltage outer winding | **3.97 °C** |

**Interpretation:** spatial profile comparison at accessible instrumented winding positions, not a verified global-winding-maximum error. The paper cites ambient variation during testing and possible fiber-induced perturbation of winding heat dissipation as contributors to discrepancies.

**Model comparison:** publisher Table 4 reports 3.97°C and 0.0087 s for proposed approach, versus U-Net 4.56°C and 0.07s, POD-RSM 4.80°C and 0.73s. This comparison is case/platform-specific, not independent generalization.

## State-estimation / observability inference [T1], not author-proven

Let `T(x,t)` be the physical field, `y_j(t)` measurements at instrumented locations, and `hat T_ROM(x;u)` the computed **steady** field. These quantities and claims must remain distinct:

~~~text
max_x hat T_ROM(x;u)
    != guaranteed max_x T(x,t)
max_j y_j(t)
    != guaranteed max_x T(x,t)
surrogate-CFD agreement
    != direct experimental error of the global hottest-spot
field reconstruction from operating conditions
    != demonstrated dynamic Kalman observer
fast solving time
    != transient response validation
~~~

P13's POD dimension and fitting are **spatial-compression/model-surrogate degrees of freedom**; they are not automatically independently evolving thermodynamic states for `X_P,th`. The work does not demonstrate formal observability rank, unique inverse recovery from sparse sensors, quantitative global-HST uncertainty, cross-transformer transfer, or extreme-heat transient threshold timing.

## Transfer/admission decision

**ADMIT [A3/A4, case-qualified]:** dense optical sensing is a credible experimental basis for comparing predicted winding temperature **profiles**; spatial reduced-order reconstructions can approximate a high-fidelity spatial model, with documented numerical and experimental discrepancies.

**DO NOT ADMIT:** `3.31 K` as sensor-validated HST error; virtual 100 comparison points as 100 independently located sensors; `0.0087 s` as physical temperature-response timescale; surrogate POD coefficients as compulsory new dynamic states; any model parameter/thermal threshold/allowable capability for the thesis case.

**Model state status remains:**

~~~text
theta_TO, theta_HS:                 CANDIDATE REDUCED THERMAL STATES
Spatial temperature T(x,t):       REFERENCE MODEL / MEASUREMENT FIELD, NOT ACTIVE
POD reduced spatial field:        CANDIDATE HIGHER-FIDELITY ESTIMATOR
True global-HST observability:    OPEN
Transient model sufficiency:      OPEN
Extreme heat / EV transferability OPEN
Thermal-state-to-capability map:  OPEN — normative/equipment authority required
X_P,th = [theta_TO,theta_HS]^T:    CANDIDATE — NOT FROZEN
~~~

**P14 priority:** a source with genuine **transient** sparse-sensor field reconstruction, explicit independent physical verification points, measurement noise sensitivity, and errors kept separate for reconstructed field and actual hottest-spot temperature. Candidate Li et al. (2026), DOI 10.1016/j.epsr.2026.113033; verify access and HST-specific error before model admission.

**Governing sentence:** **A numerically well reconstructed hottest spot is not yet an independently observed physical maximum; a spatial steady surrogate is not a validated transient thermal-state estimator.**
