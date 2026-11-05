# HST as a strong candidate metric — decision record v1
**Date:** 2026-11-05
**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience
**Status:** RESEARCHER-SELECTED STRONG CANDIDATE, NOT FINAL METRIC SELECTION; NO SUPERVISOR APPROVAL CLAIM
**Authority:** Active thermal SO1–SO3, original physical interface scope. This note does not revise the thesis objectives or previously approved scoping review.

## Researcher decision
Retain **precise, time-resolved transformer winding hot-spot temperature (HST) estimation** as a strong candidate physical-state/validation metric. Its primacy relative to other metrics will be decided only after comparing evidence, observable physical interdependencies and SO1–SO3 traceability. Do not announce HST accuracy as the final primary research metric or as proof of coupled-system resilience.

## Candidate metrics for comparative selection
| Candidate | Observable quantity/units | Relevant objective | Principal limitation / gate |
|---|---|---|---|
| HST estimation accuracy | HV/LV winding HST RMSE/MAE [°C], peak error, 95th percentile error; timing | SO2, supporting SO1 | Directly validates component temperature estimate, **not** observed P↔T thermal coupling |
| Thermal-limit crossing timing | error in predicted vs observed threshold entry/exit [min]; false/true events | SO2, SO3 | Must establish asset-specific thermal/rating thresholds and independent transition observations |
| Dynamic thermal capacity / derating | eligible transformer apparent power [kVA] or EVSE allowable charging power [kW] under T_a, loading and HST | SO1–SO3 | Physical equipment ratings/control actions and topology must be established, not merely inferred |
| Charging restriction and mobility-service deficit | requested-delivered energy [kWh], curtailed charging [kW], lateness [min], departures unmet [count/%] | SO3 | Requires qualified demand and power/charger control records; simulated outcomes clearly labeled |
| Coupling/propagation sensitivity | direction-specific change in downstream state/service under matched forcing; delay [min]; quantitative elasticity or impulse-response with uncertainty | SO1–SO3 | Causal attribution requires verified connectivity, shared clock, interventions/matched design; otherwise model-only or association |

## Model testing gates
1. **Observed HST qualification:** The recorded SINTEF dataset contains measured HV/LV 'hot-spot' named channels (8,589 valid rows each in the current report). Verify sensor location, actual observable versus true maximum, calibration, clock and operating range. Prior top-oil prediction is not an HST result.
2. **Physics-first baseline:** Compare appropriate transformer thermal-standard equations, reduced ODE/DAE (and full PDE/FVM only where justified) against simple persistence and reasonable gray-box baselines. Do not assert all conventional numerical methods are computationally prohibitive.
3. **Evaluation protocol:** Chronological holdout; no training or normalization leakage; compare RMSE, MAE, bias, severe-temperature errors, computational latency, parametric sensitivity and prediction under admissible future forcing; report uncertainties and model validity domain.
4. **Extreme-heat transfer:** Norwegian SINTEF observed ambient range (-19.58 to 25.97 °C in current report) does not independently validate hot extreme-heat behavior; include separate high-temperature experiment or transparently qualified scenario inference.
5. **Coupling test:** Do not infer transformer→EVSE derating or electrified mobility loss merely from HST estimation. Require instrumented electrical/thermal interface and real control/service observations for field-causal claims, or explicitly label a physics-based scenario simulation.
6. **Selection stage:** Rank candidate metrics by **physical relevance to direction-specific P→T/T→P mechanisms**, **actual measured observability**, **time resolution/identifiability**, **independent validation**, **sensitivity to extreme heat and EV charging**, **SO1–SO3 traceability**, **uncertainty** and **feasible execution**. Choose a small complementary suite, not one universal metric by convenience.

## Current conclusion
**HST = STRONG CANDIDATE for transformer thermal-state accuracy.**
**Final primary interdependency metric(s) = UNDECIDED** until systematic literature evidence extraction and benchmark tests are completed.
No objective amendments, claims of independent screening, or final methodological comparisons are implied.

## Evidence pointers
- `project/data_qualification/2026-11-03/REPORT_01_MEASURED_DATA_RQ1_RQ7_2026-11-03.md`: recorded SINTEF sensor channels and qualified preliminary top-oil results.
- `project/systematic_literature_review/PHYSICS_VS_PINN_MODEL_DECISION_V01.md`: PINN eligibility remains conditional.
- `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`: governing SO1–SO3.

## Added strong candidate — EV charging induced transformer thermal aging (2026-11-05)
**Researcher decision:** Retain transformer thermal insulation aging / loss-of-life under increasing EV penetration as a second **strong candidate consequence metric**, derived from Qian, Zhou & Yuan (2015), DOI 10.1016/j.ijepes.2014.09.040. This is complementary to, not interchangeable with, HST-estimation accuracy.

**Controlled variables:** EV penetration [fraction/% of fleet], coincident EV charging demand [kW or per-unit load], charging-time strategy, ambient temperature and baseline electrical load. **Potential response metrics:** HST [°C], instantaneous aging acceleration factor FAA [dimensionless], time-weighted equivalent aging factor F_EQA [dimensionless], estimated insulation loss-of-life [hours/% under explicitly stated nominal-life/standard assumptions], and change relative to baseline or charging policy. In this paper, FAA and F_EQA are calculated from **modeled HST**, not independently observed aging of the field transformer.

**Source model:** `F_AA(t) = exp(15000/383 - 15000/(T_H(t)+273))` (paper's adopted IEEE-style form, equipment/standard edition must be checked); `F_EQA = Σ F_AA,n Δt_n / ΣΔt_n`. Prefer primary-source clause/eq verification before manuscript reuse. This is an **T→P EV-load-to-transformer thermal aging** metric; not proof of feedback P→T or actual mobility-service consequences.

**Benchmark test:** At identical baseline load/weather and controlled EV charging penetration/policy, compare conventional transformer thermal ODE/guide, conditional PINN, and proposed model predictions of HST, FAA, F_EQA and estimated loss-of-life; separate independently measured HST-model validation from model-derived aging. Report parameter and scenario uncertainty and avoid comparing absolute lifespan estimates without verified insulation reference assumptions. Do not infer real-time aging measurement from estimated HST.

**Metric status:** STRONG CANDIDATE; not selected final. Check sensitivity to EV charging only after confounding, source applicability, and thermal parameters are qualified. Compare ultimately with dynamic power limits, charger curtailment, service deficit and propagation delay for SO1–SO3.

**Original paper extraction:** `project/systematic_literature_review/PRIMARY_EXTRACTION_QIAN_ZHOU_YUAN_2015_2026-11-05.md`.
