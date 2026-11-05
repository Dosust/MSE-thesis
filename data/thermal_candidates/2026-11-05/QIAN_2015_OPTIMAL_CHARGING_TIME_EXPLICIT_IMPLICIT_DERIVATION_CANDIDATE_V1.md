# Qian et al. (2015) charging-time method: explicit use, implicit mathematical derivations, and evidence gates

**Date:** 2026-11-05. **Status:** derivation candidate, not published-source equation transcription, not demonstrated thesis novelty or implemented result.
**Scope and authority:** official title V3 and frozen SO1–SO3 unchanged; thermal-only dynamic Power ↔ Electrified Transportation, extreme heat primary forcing, insulation ageing supporting slow degradation state/metric. Whole-network optimization is not required.

## 1. Source audit — what is and is not established

Qian, Zhou and Yuan (2015), *Impacts of high penetration level of fully electric vehicles charging loads on the thermal ageing of power transformers*, DOI https://doi.org/10.1016/j.ijepes.2014.09.040. Author accepted manuscript https://researchonline.gcu.ac.uk/ws/files/6078356/FEV_transformer_paper_IJEPS2014oct.pdf .

Original manuscript (II–V) specifies stochastic charger start, SOC and mode, a piecewise charger load curve, aggregate EV loading and IEEE C57.91-1995-derived HST/accelerated-life consumption. It evaluates uncontrolled domestic, off-peak domestic, smart domestic, and public charging on a generic UK network, using half-hourly time intervals, actual non-EV demand/weather forcing and modeled transformer thermal parameters.

The paper **states** that its method can be applied to find an optimal EV charging time as a function of existing load and ambient temperature; its smart domestic charging scenario refers to an **optimal start-time distribution** and to previous literature: Zhang et al. (2012), *A Methodology for Optimization of Power Systems Demand Due to Electric Vehicle Charging Load*, IEEE Trans. Power Syst. 27(3):1628–1636. The 2015 scenario also uses real-time pricing and load-valley filling. **Do not assert that Qian et al. explicitly solved a new general constrained minimum-HST-ageing optimization problem solely from the abstract/smart scenario.** Verify the 2012 cited optimization objective and detailed source before exact reproduction.

Observed in manuscript: moving many chargers into 9pm–midnight off-peak time creates a new load peak; even coordinated nighttime charging can inhibit transformer cooling at high penetration; smart charging generally reduces computed life consumption in tested cases; static peak shaving alone is insufficient.

## 2. Explicit role in the thesis

- Benchmark generation of stochastic EV session/charging demands from start-time, SOC, charging mode and penetration distributions.
- Baseline predicted feeder/transformer load, winding hot-spot T_H(t), relative ageing F_AA and equivalent loss L_eq.
- Literature-backed comparison of uncontrolled, uniformly off-peak, and smart-start-time strategies.
- Source-derived physical lesson: charging decisions depend on *both* baseline demand and ambient/thermal memory, and can shift load/ageing between transformers.
- **Conditional:** 2015 reported numerical outcomes are model-simulation results, not measured EV–HST coupling at our site; the original numerical paper's data/assumptions and original optimization objective are not yet reproduced here.

## 3. Minimal proposed mechanistic model (OUR derivation, not Qian's exact formula)

For scenario omega, let p_i(t; tau_i, s_i0, m_i, omega) be physical AC-side charging power with start time tau_i; total P_EV(t,omega) = sum_i p_i, delivered only to a verified parent transformer. The actual transformer current I_tr=G(P_base+P_EV,Q_total,V,topology), respecting phases and other loads.

Let x(t)=(top-oil T_o, winding-over-oil deltaT) be a measured-parameter-qualified transformer thermal state, with dx/dt=f(x,I_tr,T_a;theta) and hot-spot T_H=g(x). **Illustrative** transformer oil/winding lumped ODE; IEC/IEEE equipment-specific equations must be properly checked.

Let **conditional insulation model** ageing acceleration be F_AA(T_H)=exp(15000/383 - 15000/(T_H+273)) for a qualifying thermally-upgraded cellulose case (time measured in hours). Equivalent ageing L_eq(t0,t1)=integral_{t0}^{t1} F_AA[T_H(t)] dt, reference-equivalent hours; it is not direct actual remaining-life measurement.

## 4. A decision problem that becomes explicit only after derivation

Let u be an admissible vector of start-time shifts, charging powers or a predeclared charging policy; model the device/network as above, and define

**Ageing-aware objective:** min_{u in U} E_omega[L_eq(u,omega)] (possibly risk-augmented, e.g. +beta CVaR_alpha(L_eq), if distributions/risk tolerance are scientifically justified).

**Energy/service feasibility:** for each vehicle i, integral over [arrival_i, departure_i] eta_i p_i(t,u,omega) dt >= E_i,required (kWh with time in hours), or a defined quantified service shortfall if demand is unfeasible; charging powers between 0 and charger/EV/battery/EVSE allowable limits.

**Electrical/thermal capability:** I_tr(t) <= I_allow(t), and T_H(t) <= T_H,lim(t) for all times in declared horizon if justified by asset and safety standard. If uncertain, a chance constraint Pr(max_{h in [0,H]} T_H(t+h)>T_H,lim)<=epsilon is only admissible with calibrated uncertainty. Do not invent numerical thermal limits or risk tolerances.

**Critical distinction:** This is *a proposed testable mathematical program*, not evidence that the 2015 method already solved it. Optimization can be used as a limited comparison/decision experiment and is NOT necessary as a new frozen fourth thesis objective.

## 5. A mathematically useful implicit derivation: charging-time sensitivity

At fixed equipment, ambient, base load, other EV demands and smooth controls, let q_i(t)=partial x(t)/partial tau_i. Differentiate the physically qualified thermal ODE:

dq_i/dt = f_x q_i + f_I (partial I_tr/partial tau_i), with q_i(t0)=0 when initial x independent of tau_i.

Then, if g(x) has no explicit tau_i dependence, **chain-rule time shift sensitivity** becomes

dL_eq/dtau_i = integral_{t0}^{t1} F_AA'(T_H(t)) [g_x(x(t)) q_i(t)] dt.

For the illustrative upgraded-cellulose law, **F_AA'(T)=F_AA(T) × 15000/(T+273)^2 > 0** (units inverse degC). The derivative shows *why a marginal charging-time shift's ageing effect depends on the entire evolving hot-spot path*, not solely the initial EV power or immediate base-load peak. q_i integrates transformer thermal inertia, power factor/network and load overlap.

For a differentiable time-shifted charging profile p_i(t;tau_i)=phi_i(t-tau_i), dp_i/dtau_i = -phi_i'(t-tau_i); when profiles switch abruptly or constraints change active sets, use one-sided perturbations, finite differences or hybrid-event sensitivities rather than asserting differentiability.

This derivative can support a **thermal marginal charging-time cost** ranking for a small number of admissible session shifts, alongside uncertainty and risk, but requires verified model physics/parameters. It is a proposed derivation and not a novel mathematics theorem.

## 6. Implicit thesis extensions and evidence

| Prospective consequence | Derived quantity | Strong condition |
|---|---|---|
| Thermal headroom | h_H(t)=T_H,lim - T_H(t), degC | Equipment-appropriate limit and uncertainty |
| Time to thermal criticality | t_crit = inf{t: T_H(t)>=T_H,lim}, min/h | Qualified limits and continuous time-state model |
| EV charging capability | P_EV,max^thermal(t;H) under predicted HST/other-load conditions, kW | Verified parentage, ambient and current model, limits, future horizon |
| T→P incremental ageing | Delta L_EV = L_eq(with EV) - L_eq(without EV) | Paired same-context model scenarios or controlled connected-system measurements |
| P→T curtailed service | sum of requested minus delivered charging by departure, kWh; related mobility metrics separately | Actual request/departure/service measures or explicit scenario-only labels |
| Robustness to heatwaves | change in tau*_i, hot-spot, life consumption and energy shortfall under high ambient | Extreme-heat measurements or explicit non-validated stress scenarios |

Counterexample to simplistic claims: lowest instantaneous base load need not minimize equivalent ageing because ambient temperature and accumulated oil/winding heat can differ; cheapest tariff slot can create correlated charging peaks; optimizing one transformer can displace stress to another. Compare same requested energy and departure constraints.

## 7. Thesis relevance and research gate

- **SO1:** qualify start time/ambient/current/HST/ageing mechanism and transformer–EV interface.
- **SO2:** represent stochastic charging sessions, oil/winding state, feedback charging cap and associated thermal time scales.
- **SO3:** quantify time to limit, feasible charging, lost requested energy and service continuity, with or without a small comparative schedule intervention.
- **Validation:** calibrate transformer-only physical model against SINTEF directly measured HV/LV HST (not EV-linked); qualify local EV demand and network interface, otherwise clearly label EV-coupled scenarios as synthetic; do not claim measured extreme-heat causal effects. PINN/FVM are conditional methodological benchmarks, not default winners.
- **Prior-art audit:** Qian 2015 establishes charging optimization *applicability* and tests smart load-scheduling outcomes; Zhang et al. 2012 addresses EV-demand optimization. Newness can only be claimed after systematic novelty checks around dynamic thermal rating, aging-aware charging, EVSE control, and critical-service resilience.

**Candidate decision:** EVALUATOR_AND_START_TIME_DECISION_SUPPORT | DERIVATIVE_BASED_AGEING_SENSITIVITY_CANDIDATE | THERMAL_FEEDBACK_AND_SERVICE_EXTENSION_PENDING | ORIGINAL_OBJECTIVE_REPRODUCTION_PENDING | SO1_SO3_FROZEN
