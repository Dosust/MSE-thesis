# Transformer winding hot-spot temperature as a coupled thermal-interdependency metric

**Date:** 2026-11-05. **Status:** CANDIDATE METRIC PROTOCOL, NOT a model result or amendment to frozen objectives.
**Canonical thesis title V3:** Engineering of Power–Electrified Transportation Interdependencies for Resilience.
**Scope:** Frozen SO1–SO3, extreme heat, thermal-only physical interdependencies, state-time and electricity/mobility service consequences. This proposal does not alter the canonical title or objectives.

## Scientific decision

Transformer winding hot-spot temperature (HST), T_H(t), is a primary power-system *thermal state*. The HST estimation error is an estimator validation metric, NOT by itself a measured Power–Electrified Transportation interdependency.

The directional mechanism must be separately tested: (T→P) EV load flows through a *verified parent transformer*, increasing relevant transformer current/losses and affecting its thermal state; (P→T) that state can constrain admissible EV charging capacity, and possibly electricity and mobility services. Extreme ambient heat is a forcing; thermal capability is derived, not itself a state; service and resilience are downstream outcomes.

## Physical baseline (illustrative, not verbatim standard equations)

- T_H(t) = T_o(t) + DeltaT_H-over-oil(t).
- tau_o * dT_o/dt = T_ambient(t) + DeltaT_o,ultimate(K, cooling, parameters) - T_o(t).
- tau_w * d(DeltaT_H-over-oil)/dt = DeltaT_H-over-oil,ultimate(K, cooling, parameters) - DeltaT_H-over-oil(t).
- K(t) = I_transformer(t) / I_rated. EV charging power by itself is NOT a measured transformer load factor without circuit topology, power factor, parent feeder measurement and other loads.
- Cooling parameters, loss laws, thermal time constants, winding factors and allowable thermal limits must match the tested transformer and mode. More detailed models are admitted only if justified by error/physics/evidence.

## Metric registry

| Metric | Definition | Units | Admission criterion |
|---|---|---|---|
| H1: HST accuracy | Held-out MAE/RMSE and near-critical error of estimated vs independently **measured winding hot-spot** (HV/LV evaluated separately) | degC | Recorded sensor position, quality, noise, train/test time split, uncertainty |
| H2: thermal headroom | h_H(t) = T_H,max - T_H(t) | degC | Equipment-appropriate validated limit, correct thermal state and uncertainty |
| H3: EV marginal thermal impact (T→P) | DeltaT_H^EV(t,h) = T_H(t+h with qualified EV load) - T_H(t+h without that load), with same ambient/initial/other loads | degC | Proven parent transformer and controlled measurements or calibrated clearly labeled model counterfactual; no measured causal claim from separate-installation datasets |
| H4: thermal criticality risk | p_exceed(t,h) = Pr[T_H(t+h)>T_H,max given observations]; first critical threshold crossing t_crit | probability, time | Calibrated forecast intervals, high-temperature false-negative rate and trustworthy threshold |
| H5: constrained charging and service (P→T) | P_EV,max^thermal(t,h) constrained by predicted HST and capacity; E_shortfall = integral max(0, P_requested-P_delivered) dt | kW, kWh | Measured/validated transformer constraint, charging request and actual delivered service; otherwise scenario only |
| H6: real-time physical validity | Prediction latency, physical residual, parameter admissibility, coverage under unseen ambient/loading and computational time vs baseline | ms, error/coverage | Hardware, window and time horizon disclosed; calibrated reduced-order baseline included |

**Core interdependency outputs:** H3 characterizes transport-to-power loading/heating, and H5 characterizes power-to-transport thermal capacity/service constraints. H1 validates the thermal state underpinning both; it is not enough alone.

## Dataset gate — SINTEF measured HST

**Bærug, Madshaven, Espedal, 2025; Zenodo DOI 10.5281/zenodo.17223516:** https://zenodo.org/records/17223516

Publisher describes direct online 2024 measurements from a **40 MVA ONAN transformer in southern Norway**, with Voltage [kV], Current [A], Ambient [degC], Top oil [degC], Bottom oil [degC], Mid-spot HV/LV [degC], **Hot-spot HV/LV [degC]** and clamping data in the **measured sensor CSV**, plus a separate calculated-model CSV and README.

- Measured input candidate: Barug2025_sensordata.csv, approximately 873 kB, publisher MD5 5d81840a2f901f04fded98c3e1097b6e.
- Calculated-model CSV: Barug2025_calculated.csv, approximately 481 kB. Never use calculated HST proxies as independently observed HST ground truth.
- Sensor location may not capture the absolute hottest winding point. Publisher warns of gaps. Inspect actual schema, units, timestamps, cooling configuration and sensor placement before quantitative validation.
- **Suitable candidate for H1**, and potentially H2/H4 after legitimate limit/rating identification. **NOT direct evidence for EV-specific H3 or H5:** no documented EV charging connection/charging demand; also Norway measurements alone cannot validate extreme-heat extrapolation.
- KIT 50-day OLTC field electrical M2/M3, independent KIT PHIL lab voltage/current, and SINTEF transformer HST records are DIFFERENT installations. Do not splice these datasets into a claimed simultaneously measured interface.

## Literature, baselines and novelty boundary

- IEC 60076-7:2018 (https://webstore.iec.ch/en/publication/34351) and IEEE C57.91-2025 (https://standards.ieee.org/ieee/C57.91/7163/) address mineral-oil transformer thermal loading, temperatures and thermal aging.
- Nishanth 2026, Physics-Informed Neural Networks for Transient Thermal Analysis and Insulation Life Assessment in Power Transformers, DOI https://doi.org/10.1109/NE-IECCE69680.2026.11665934, already discusses physics-informed HST estimation and EV-charging load context.
- Cao 2026 online transformer HST physics/data hybrid, DOI https://doi.org/10.1007/s44163-026-02632-y, already describes physical recursion plus uncertainty and overtemperature probability; therefore neither PINN-HST alone nor physics-data HST uncertainty alone is novel.
- Full three-dimensional CFD/FEA can be computationally costly for real-time monitoring. Standard lumped thermal ODEs and difference equations are often computationally inexpensive. The blanket claim that all traditional numerical methods are prohibitively expensive is scientifically inaccurate.
- Specific prospective contribution to test against global prior work: **measured-HST-validated estimator + quantified EV loading-to-HST dependency + temperature-bound charging capability + time-resolved service consequence under extreme heat**. This is a research hypothesis, NOT a currently verified originality claim.

## Execution and validation order

1. Acquire publisher SINTEF sensor, calculated, and README files; verify checksums, distinguish observed HV/LV HST from calculated values, audit sensor/time gaps and legal use.
2. Develop transformer-specific calibrated IEC/IEEE-type physics ODE baseline; train on chronological training only, hold out validation and testing; quantify H1 against both observed HST channels, including hot/loading extreme subsets.
3. Add grey-box/residual correction or PINN/PDE surrogate only if physically justified, and compare accuracy, coverage, extrapolation and speed against the simple baseline.
4. Obtain same-transformer EV charging/topology/other load and thermal-limit evidence, or **explicitly declare model-only EV charging scenarios**. Compute H3 transport-to-power heat increment and H2/H4 criticality under consistent scenarios.
5. Estimate H5 feasible charging/energy service with correctly qualified EV requests, limits, horizons and uncertainty. Model-generated curtailment is not observed mobility loss.
6. Report SO1 physical mechanism, SO2 state-time evolution and SO3 transition times/service trajectories separately. No measured extreme-heat or EV thermal causal claim from SINTEF-only data.

**Status:** HST_PRIMARY_STATE_CANDIDATE | SINTEF_MEASURED_HV_LV_HST_DATA_IDENTIFIED | NO_HST_MODEL_VALIDATION_EXECUTED | COUPLED_EV_THERMAL_EVIDENCE_OPEN | FROZEN_SCOPE_UNCHANGED
