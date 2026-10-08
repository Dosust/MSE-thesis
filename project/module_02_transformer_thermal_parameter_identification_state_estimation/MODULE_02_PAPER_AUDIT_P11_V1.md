# Module 02 — Paper Audit P11 V1: Ambient-Dependent Effective Parameters

**Status:** PRIMARY-PUBLISHER FULL-HTML EVIDENCE AUDITED — MODEL ADMISSION OPEN  
**Date:** 2026-10-08  
**Evidence authority:** `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`

## P11 — Souza, Picher, Fofana & Zinflou (2026)

**Title:** Ambient Temperature-Dependent Parameterization of the IEC 60076-7 Top-Oil Thermal Model  
**Journal:** *Energies* 19(17), 4224  
**DOI:** https://doi.org/10.3390/en19174224  
**Primary source:** https://www.mdpi.com/1996-1073/19/17/4224  
**Class:** [A3] utility field observations + [A4] calibrated adaptive model.  
**Scope:** top-oil temperature (TOT) **only**; no demonstrated winding-HST reconstruction. **No standard equation or threshold adopted.**

## Experimental/data authority

The single transformer is at La Suète substation, Québec: 225/26.4 kV, 40/53/66 MVA (at 30°C) across ONAN/ONAF stages. Measurements: 8 December 2021–15 December 2025; 1-min source data resampled to 5-min observations, **423,072** retained samples. Inputs include top-oil, ambient temperature, normalized load, tap position, cooling stage. Chronological **70% development / 30% test** partition.

## Focal method

IEC 60076-7-inspired top-oil differential model is calibrated (not replaced by an independently established constitutive law). Authors optimize model exponent `x`, rated top-oil rise `Delta_theta_to,r`, load-loss ratio `R` and stage-dependent oil time constants using tree-structured Parzen estimator (150 trials). The development data are also divided into 6-h segments for local calibration of `x` and `Delta_theta_to,r`, then fitted to ambient-dependent relationships by cooling stage.

Conceptual dependence, **[T1] thesis-level shorthand, not an exact author or standard equation**:

~~~math
p_eff(t) = g(T_a(t),\,c(t);\,\beta)
~~~

Here `T_a` is ambient forcing; `c` cooling stage; `p_eff` effective fitted coefficients. Dependence on forcing does **not** automatically create an additional dynamic thermal state.

## Test-subset evidence (author Table 7)

| Model | MAE °C | RMSE °C | R² | Bias °C |
|---|---:|---:|---:|---:|
| Globally optimized fixed | 3.11 | 4.00 | 0.65 | 0.35 |
| Adaptive cooling stages comparison | 2.89 | 3.48 | 0.73 | 1.66 |
| Ambient-dependent proposed | **2.03** | **2.56** | **0.86** | **0.13** |

Segment mean ambient temperatures reported for development span **−26.90 to 36.30°C**. The reported ambient-linear fit has substantially weaker explanatory power in ONAN (**R² approximately 0.25–0.26**) than ONAF modes (higher R², up to ~0.90), hence the same covariate is not comparably informative in all cooling states.

## Critical limitations: source vs review inference

**Authors' explicit cautions:** effective fitted coefficients are **not uniquely identifiable intrinsic physical properties**; parameter compensation can yield similar outputs. Correlation with ambient does **not** establish a physical causal mechanism. A single transformer does not validate transfer to different equipment/climates. Top-oil calibration does not establish hot-spot or thermal capability.

**Independent [T1] review checks (not author results):**
- Table 4 cooling-stage counts total **3458** (2196+938+324), while Section 3.2 reports **3463** segments. Preserve both; difference of **5** is unresolved, not silently repaired.
- Globally optimized ONAN oil time constant **5.95 h** is close to optimization upper bound **6 h** (Tables 2–3). Boundary-proximity flags parameter-identification sensitivity; not proof of bias.
- The publisher HTML rendering of Eq. (1) needs independent equation-symbol verification against the final PDF and applicable IEC clause before equation adoption; no exact ODE transcribed/frozen here.
- Chronological within-transformer test reduces temporal leakage compared with random splitting, but is **not external transformer validation**; parameter identifiability and extreme-heat extrapolation remain unresolved. Test-range extremes must not be inferred from development-range bounds.

## Thesis consequence / admission

**ADMIT CONCEPT [A3/A4]:** top-oil model calibration can benefit from conditioning **effective parameters** on measured ambient temperature and cooling stage.

**DO NOT ADMIT:** the paper's fitted parameter values as transferable physical constants; any HST estimator; any unique `tau_o` law; normative temperature/loading limits; a state-to-capability map; proof that `X_P,th=[theta_TO,theta_HS]^T` is dynamically sufficient.

Keep `T_a(t)` as **external forcing**, `theta_TO` as candidate thermal state, and `p_eff=g(T_a,c)` as **optional [T1] parametrization candidate** pending case-specific validation.

**Next (P12 candidate):** directly observed/predicted HST estimation with explicit observability, time-varying state, noise and external validation; publisher source candidate Chen & Su (2013), https://doi.org/10.1002/tee.21862, requires independent equation-level audit.

**Overall P11:** **PARAMETER-IDENTIFICATION MECHANISM / CASE-SPECIFIC PREDICTION EVIDENCE ONLY.**  
**Module-02 final state model:** **NOT FROZEN**.
