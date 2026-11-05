# Candidate foundational formulation: stochastic EV-cluster demand coupled to transformer thermal ageing and charging service

**Date:** 2026-11-05. **Status:** candidate mathematical foundation, NOT an experimentally identified coupling, finalized model, novel finding or approved amendment to frozen SO1–SO3.
**Official thesis title V3:** Engineering of Power–Electrified Transportation Interdependencies for Resilience.
**Scope:** Thermal Power ↔ Electrified Transportation interdependencies under extreme heat, with physical state/time and downstream electricity/mobility-service consequences. Does not change frozen objectives or commit to an optimization-heavy thesis.

## 1. What the source actually establishes

Qian, Zhou and Yuan (2015), *Impacts of high penetration level of fully electric vehicles charging loads on the thermal ageing of power transformers*, International Journal of Electrical Power & Energy Systems 65, 102–112, https://doi.org/10.1016/j.ijepes.2014.09.040, report stochastic EV charging load and transformer thermal ageing depending on ambient temperature, start of charging, initial SOC and charging mode. Their aggregate EV demand derives from an analytical solution for clustered chargers. The publication reports a UK generic LV distribution network with real non-EV load demand, and models charging strategies including smart charging.

**Source boundary:** The publisher abstract and public manuscript description support this general methodological architecture; the exact analytical cluster-load equation, mathematical assumptions, calibration, boundary conditions, numerical coefficients and eligibility of any original code still require a full-text equation-by-equation reproduction audit. The equations BELOW are a **new proposed generalization**, not verbatim equations or independently reproduced results from Qian et al.

**Prior-art boundary:** Aggregate FEV demand → transformer hot-spot/ageing is established in 2015, not novelty. A credible potential contribution would have to establish what is new in **validated temperature-state dynamics ↔ thermally restricted charging capability ↔ electricity/mobility-service state/time consequences**, against 2015–2026 coupled EV/transformer thermal rating research.

## 2. Stochastic EV cluster: physical load interface

Let scenario omega describe a **joint** (possibly correlated) collection of EV charging-start/arrival A_i, initial SOC s_i,0, charging mode m_i, energy capacity E_i, required departure D_i and any uncertain non-EV/ambient profiles, for i=1,...,N. Do not assume independent or identically distributed sessions without empirical support.

- s_i(t,omega) in [0,1] is EV battery state-of-charge; E_i in kWh is usable battery energy.
- c_i(t,omega) in {0,1} indicates physically connected/eligible charging during its session; u_i(t,omega) in [0,1] is allocated fraction of available charger power; m_i identifies charger mode/rating.
- Measured **AC-side** EV charging demand p_i(t,omega) in kW must respect actual charger and battery constraints: 0 <= p_i <= c_i u_i min(P_i,rated(m_i), P_i,battery-acceptable(s_i,thermal EV state), P_i,EVSE-thermal-allowable). Do not assume these functions are measured from source KIT PHIL.
- In a consistent one-way charging model, ds_i/dt = eta_i p_i/E_i with time measured in hours and dimensionless eta_i in [0,1]; distinguish AC input from battery DC charging and allow time/departure terminal constraints. Bidirectional V2G is optional, and requires a separate signed-power/efficiency convention if admitted.
- Aggregate parent-feeder EV real power: P_EV(t,omega) = sum over those EVs **verified supplied by the selected transformer** of p_i(t,omega). Add non-EV real and reactive demand explicitly: P_tot=P_base+P_EV; Q_tot=Q_base+Q_EV.
- Transformer load factor is based on **transformer current** (potentially three-phase/unbalanced): K(t,omega)=I_tr(t,omega)/I_rated, with I_tr derived from a justified network electric model using voltage, phases, P/Q/power factor, base load and topology. Never equate P_EV alone to I_tr or assume a unique feeder path from synchronized signals.

These equations represent a candidate **stochastic hybrid charging process**: random sessions, discrete connection/mode states and deterministic continuous SOC updates between events. It is NOT necessarily an Ito stochastic differential equation; no diffusion term is justified without relevant observed noise.

## 3. Transformer state/time mechanics

For a qualifying oil-immersed transformer, let x_P=[T_o, DeltaT_h/o] with T_H=T_o+DeltaT_h/o in degC. Illustrative reduced thermal equations are

- tau_o dT_o/dt = T_ambient + DeltaT_o,ultimate(K, cooling,theta) − T_o.
- tau_w d(DeltaT_h/o)/dt = DeltaT_h/o,ultimate(K,cooling,theta) − DeltaT_h/o.

Here tau_o and tau_w are time constants (same unit as time), and theta includes calibrated equipment rating, no-load/load losses, temperature exponents, oil flow/cooling mode and operating parameters. These are **schematic first-order lumped ODEs, not verbatim IEC/IEEE equations**. Real transformer measurement, cooling mode and temperature-dependent validity constrain the final form.

For appropriate **thermally upgraded insulation** as an example, reference-ageing acceleration relative to 110 degC can be modeled as F_AA(T_H)=exp(15000/383 − 15000/(T_H+273)). Then dL_eq/dt=F_AA(T_H) when t is measured in hours, yielding L_eq in reference-equivalent hours. For non-thermally upgraded insulation a distinct model such as 2^((T_H−98)/6) may be appropriate after verifying paper grade and standard edition.

**Do not equate equivalent ageing to directly measured paper degradation, a failure probability or remaining years.** HST measurement uncertainty, insulation chemistry, moisture and oxygen can materially affect inference.

## 4. Close the P ↔ Transportation loop

From thermal state x_P and an explicitly chosen future time horizon H, define feasible EV charging power/currents based on equipment limits, future ambient, predicted other loads and thermal inertia:

- P_EV,allow^thermal(t,omega;H) = the maximum admitted EV charging demand such that predicted T_H(tau) <= T_H,lim(tau), I_tr(tau)<=I_lim(tau) for all tau in [t,t+H], optionally respecting a justified insulation-ageing budget.
- Under uncertainty, declare a chosen risk tolerance epsilon and use Pr(max over tau in [t,t+H] T_H(tau) > T_H,lim) <= epsilon only if scenario probabilities have calibration and support.
- Actual charging allocation p_i(t,omega) must respect the aggregate charging cap and session constraints. This creates the **P→T** feedback: thermal physics changes feasible charging, which changes delivered charging energy and, in turn, transformer loading.
- E_shortfall,i = max[0, E_required,i at departure − E_delivered,i by departure] in kWh, if real requests/departures are available; otherwise a labeled modeled service scenario. Net mobility-service consequences require a specific mobility-demand definition and should not be equated automatically to kWh.

Thus a mathematically consistent coupled model has a random/hybrid demand-state sector, electricity interface algebraic constraints, continuous thermal state dynamics and slow derived ageing accumulation, with thermal operating limits feeding back into EV charging controls.

## 5. Candidate measurable thesis metrics and comparisons

| Metric | Quantity and unit | Evidence requirement |
|---|---|---|
| H1 thermal estimation accuracy | held-out measured HV/LV hot-spot temperature RMSE/MAE, degC | direct/qualified measured HST and temporal holdout (e.g. SINTEF) |
| H3 marginal EV thermal increment | DeltaT_H^EV at fixed initial state, non-EV load and ambient, degC | same-transformer EV connection or explicitly model-based paired counterfactual |
| H7c marginal EV equivalent ageing | E[L_eq(with EV) − L_eq(no EV)], reference-equivalent hours; plus distribution/quantiles | common-condition paired scenarios, physical insulation model; not independently observed ageing |
| H2/H4 time-to-limit | thermal headroom and time to first legitimate limit crossing, degC, s/min/h | real equipment limits, state validation and hazard/uncertainty description |
| H5 thermal charging restriction and demand service | feasible EV power, kW; requested minus delivered energy, kWh | parent transformer/EVSE and real requests or explicitly labeled model scenario |
| Benchmark fairness | ODE/DAE physics baseline, conditional FVM/PINN, same HST dataset, horizon, splits, residual/accuracy/runtime, calibrated uncertainty | a PINN is optional and neither a guaranteed winner nor a unique thesis contribution |

Report scenario distributions, e.g. expected ageing E[L_eq], 95th percentile, conditioned high-heat results, and uncertainty in hot-spot estimation/charging arrivals. Prefer coupled marginal measures over an unqualified aggregate interdependency score.

## 6. Evidence-gated execution

1. **Verify and reproduce Qian et al. methods:** their original EV-cluster analytical assumptions, joint distributions, charging modes and transformer load/ageing equations. Do not assert an exact copied mathematical expression without consulting the relevant original pages.
2. **Validate stand-alone physical thermal model first:** verify SINTEF publisher sensor file, direct HV/LV HST, timestamps, observed transformer current, ambient and train/test splits. Fit physical ODE baseline before attempting PINN comparison.
3. **Validate or qualify stochastic EV sessions:** actual charged energy, arrival/start, initial SOC, charging mode, battery/EVSE limits and (if available) charger command traces; no arbitrary probability distribution imposed as measured truth.
4. **Qualify physical electrical coupling:** topology to same transformer, non-EV loads, voltages, phase currents and reactive power. If unavailable, declare the EV→HST effect **scenario-based**, not field-validated.
5. **Simulate identical ambient/base-load/initial conditions with and without EVs**, and with no intervention versus a thermal-constrained policy. Derive HST, relative ageing, life-consumption difference, first constraint time, allowable charging and unmet declared service. Include extreme-heat scenario uncertainty.
6. **Benchmark without predetermined winner:** physically constrained ODE/DAE reference, optional FVM and PINN component-level methods on identical measured HST holdouts, followed by model-specific coupled-service evaluation under qualified scenarios.

## Frozen-contract alignment

- SO1 identifies and qualifies thermal pathways and measurable state/interface requirements.
- SO2 formulates the hybrid stochastic–deterministic state/time dynamics and propagation.
- SO3 evaluates critical transition timing and electricity/mobility service consequences. Slow insulation-ageing H7 is supporting degradation, not a new independent objective.
- No change to title V3, SO1–SO3 or the decision to treat PINN as a comparative method candidate.

**Decision:** STOCHASTIC_EV_CLUSTER_PLUS_THERMAL_ODE_CANDIDATE | QIAN_2015_PRIOR_ART | CLOSED_LOOP_CHARGING_CAPABILITY_HYPOTHESIS | HST_DATA_AND_COUPLING_VALIDATION_PENDING | MODEL_NOT_FINALIZED
