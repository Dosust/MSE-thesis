# Evidence-qualified assumptions: ambient temperature, FEV penetration and charging start time

**Date:** 2026-11-05. **Status:** USER-PROPOSED PRIORITY FACTORS / TESTABLE ASSUMPTIONS, NOT observed results for the thesis systems, not a universal factor ranking, and not a frozen objective amendment.
**Current thesis title (canonical V3):** Engineering of Power–Electrified Transportation Interdependencies for Resilience.
**Frozen scope:** thermal-only power ↔ electrified-transportation interdependencies under extreme heat; SO1 identify/qualify, SO2 model state/time, SO3 quantify critical timing and electricity/mobility service consequences.

## 1. Primary literature: what is established, and where

**Qian, K., Zhou, C. and Yuan, Y. (2015)**, *Impacts of high penetration level of fully electric vehicles charging loads on the thermal ageing of power transformers*, International Journal of Electrical Power & Energy Systems **65**, 102–112. DOI: https://doi.org/10.1016/j.ijepes.2014.09.040 ; author accepted manuscript: https://researchonline.gcu.ac.uk/ws/files/6078356/FEV_transformer_paper_IJEPS2014oct.pdf .

The publisher abstract and original manuscript report that **ambient temperature, FEV penetration and charging start time were the principal factors affecting modeled transformer life expectancy in the authors' tested scenarios**. Their framework also includes **initial battery SOC and charging modes**. The authors simulate a **generic UK LV distribution network** with real non-EV load input and ambient temperature input (central Scotland 2010); FEV penetration varied **0%–50%**. Thermal/ageing calculations are performed on a **half-hourly** basis. Four simulated charging scenarios are uncontrolled domestic, off-peak domestic, smart domestic, and uncontrolled public charging.

These are modeled/analytical findings under the specific UK network, equipment, behavior, meteorological and scenario assumptions—not a universal empirical ranking or proof of our transformer condition, dynamic extreme-heat exposure or coupled service outcome.

Original study's important cautions: smart charging generally reduced modeled loss of life; shifting many sessions into overnight off-peak periods may inhibit transformer cooling at high penetration; shifting charging to commercial/industrial feeders may relieve a residential transformer while worsening other feeders. The original discussion notes neglect of transformer extra heating due to current harmonics/eddy-current effects. Do not assume every intervention reduces total-system ageing.

## 2. Priority testable assumptions and variable definitions

| ID | Variable, units | Research assumption / hypothesis | Conditional status and confounders |
|---|---|---|---|
| A1 ambient heat | T_a(t), degrees C; heatwave duration/intensity with measured profile | For the **same transformer, initial thermal state, load and cooling**, a higher ambient profile generally raises winding HST and modeled relative ageing. | **Source-supported physical candidate**, not independently measured EV coupling. Control top-oil/winding initial conditions, cooling transitions, equipment parameters and time of day. |
| A2 FEV penetration | lambda = N_FEV / N_all_vehicles served by selected geographical/network region, dimensionless or %; separately define N_EV_connected_to_this_transformer | As penetration rises, aggregate charging demand **can** rise and can increase thermal stress/ageing if additional EV charging is **on the transformer in question**. | **Source-supported scenario factor**, but monotonic effect requires fixed charging energy, behavior, management, local allocation and capacity assumptions; national/area penetration alone does not determine transformer load. |
| A3 charging start time | A_i or t_i_start, timestamp/hours; joint distribution and concurrency | Start-time coincidence with base demand and prior thermal state affects hot-spot peak, cooling interval and equivalent ageing. Controlled staggering **may** reduce ageing versus uncoordinated coincidence; not all night shifts are beneficial. | **Source-supported conditional scheduling factor**; depends on departures, session duration, SOC, tariff, occupancy, other loads and cooling inertia. |

**Do not preassign absolute factor-ranking or interaction coefficients**: fit/derive and quantify the actual effects after validating data, equipment and distributions. Paper's 'main factors' means most important in *those tested scenarios*, not the only causal determinants.

## 3. Supporting variables that MUST stay explicit

| Role | Variables | Why needed |
|---|---|---|
| Stochastic EV session inputs | Initial SOC s_i0 [0,1], energy request [kWh], charging mode/power [kW], battery capacity, session start/end and stochastic correlations | Determine how much electrical energy is requested and when; Qian includes SOC and charging mode in input modeling even though they are not the paper's three headline factors. |
| Physical electrical interface | Verified parent-transformer allocation, phase connection, voltage, real/reactive power and transformer total current | Determines whether EV load is physically supplied by the modeled transformer; penetration alone is insufficient. |
| Competing electrical demand | Non-EV baseline load, distributed generation and other transformer feeders | Controls transformer current/thermal consequences independent of charging. |
| Transformer thermal physics | Cooling mode, oil/winding time constants, loss coefficients, rated current, sensor placement, initial HST/top-oil, insulation type | Needed to estimate temperature dynamics and select the correct ageing relation. |
| Other external/operational conditions | Season, extreme-heat profile, charging coordination, outdoor siting, harmonics if material | Determine extrapolation, uncertainty and validity of simple load-loss assumptions. |

## 4. Proposed equations (thesis candidate, NOT transcribed Qian formulas)

Sample a joint EV scenario omega=(lambda, {A_i,s_i0,m_i,E_i,D_i}_i, other uncertainty), with empirically justified dependence between arrival and SOC.

**EV aggregate:** P_EV(t,omega) = sum over verified EV connections i of p_i(t,omega;A_i,s_i0,m_i,control).

**Physical electrical loading:** I_tr(t,omega) = G(P_baseline(t)+P_EV(t,omega), Q(t,omega), V(t,omega), topology). For unbalanced networks G may require phase-specific currents, not a scalar conversion from P_EV.

**Thermal state:** dot(x_th)=f_th(x_th,I_tr,T_a,theta,cooling); T_H=g_th(x_th), based on transformer-specific qualified winding/oil physics.

**Ageing proxy:** dot(L_eq)=F_AA(T_H,insulation parameters), with time in hours and reference-equivalent insulation-ageing hours as the output.

**Key paired estimand:** Delta L_EV(lambda,T_a,schedule;H) = L_eq(with assigned EV sessions, identical background/initial state) - L_eq(without those EV sessions, same conditions). **Model-based counterfactual only unless direct same-system causal evidence exists.**

**Feedback and service (distinct thesis addition to validate):** P_EV,delivered <= P_EV,thermal_admissible(x_th,T_a,I_baseline,H,limits), and E_unserved = sum_i max(0,E_i,requested-by-departure - E_i,delivered-by-departure), with actual requests or explicitly labeled assumptions.

## 5. Predeclared factor and interaction tests

| Test | Vary | Hold constant / pair | Primary metrics |
|---|---|---|---|
| E1 ambient heat | measured baseline vs independently defined heatwave profiles | EV draws, baseline loads, initial thermal condition, cooling/parameters (unless specifically varying cooling) | Peak HST [degC], HST headroom [degC], L_eq [hours], t_critical if valid limit |
| E2 local FEV allocation/penetration | 0 EV baseline plus predeclared feasible levels (paper uses 0–50%, **not automatically portable**) | identical weather, baseline, same stochastic seeds/behavior per comparison, verified connection or explicit scenario | marginal HST rise [degC], Delta L_EV [hours], distribution of loading/current |
| E3 charge-start schedule | uncontrolled vs shifted/staggered/smart (subject to actual session constraints) | same individual EV energy requests/SOC, parent network, initial states, heat exposure | peak HST, equivalent ageing, time-to-limit, charging deadline violations |
| E4 interactions | ambient x penetration; penetration x start time; all three | same calibrated thermal model and common random draws | interaction effect on Delta L_EV and service shortfall; uncertainty bands |

Do not interpret three-factor tests as calibrated importance ranking unless scenario support, parameter uncertainty and sampling conditions justify it. A coupled result must report **both** transformer thermal/ageing outcomes and charging capacity/service consequences. Monte Carlo estimates need sample-count/convergence tests; if inputs are assumed rather than measured, results are **simulated scenarios**, not observed field effects.

## 6. Evidence classification, dependencies and next gates

**Established prior literature:** Qian 2015 identifies A1–A3 as main modeled factors in UK LV/seasonal simulations; also acknowledges initial SOC and charging mode, and smart charging/site relocation effects.

**Hypotheses for this thesis:** transfer of factor ordering to different transformer types, extreme heat, local charging behavior, validated direction/magnitude of ageing changes, interactions and upstream thermal-feedback impacts on charging delivery.

**Measured-component validation candidate:** SINTEF 40 MVA ONAN measured HV/LV winding HST plus ambient and transformer current (https://doi.org/10.5281/zenodo.17223516), subject to exact file/sensor and rating QA. It does **not** measure EV penetration, sessions or a linked EV interface.

**Other distinct electrical sources:** KIT OLTC field and KIT PHIL laboratory evidence cannot be merged with SINTEF to fabricate a synchronized measured EV→HST time series. TU Dortmund controller metadata may qualify device control profiles on another installation only.

**Protocol gates:** (1) validate SINTEF actual measured HST, (2) calibrate ODE/physics reference, (3) qualify stochastic charging inputs and connected topology or label model-only scenarios, (4) run E1–E4 factorial/paired studies with uncertainty, (5) compute P↔T thermal headroom and service only when constraints and requests are valid, (6) compare PINN/FVM only on fair measured HST benchmark data, not pre-assumed superiority.

**Research decision:** A1_AMBIENT, A2_LOCAL_FEV_PENETRATION and A3_CHARGING_START_TIME are **priority, literature-backed candidate explanatory factors**; initial SOC/modes and physical/equipment variables remain controls; ranking/effect sizes and service coupling require testing. **Do not amend frozen SO1–SO3 or canonical title V3.**
