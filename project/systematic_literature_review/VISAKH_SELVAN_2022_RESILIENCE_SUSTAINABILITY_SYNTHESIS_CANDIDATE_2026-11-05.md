# Visakh & Selvan (2022) — Research synthesis: smart charging, resilience, and sustainability

**Date:** 2026-11-05  
**Status:** Original **publisher abstract examined**, full published PDF retrieval unsuccessful (publisher download blocked). Source-specific equation numbers, solver details, test setup and numerical improvement values **UNVERIFIED**. **Not a completed systematic full-text extraction, not human-screened inclusion, not field-validated coupled thermal result.**
**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience. Official thermal SO1–SO3 remain unchanged.
**Paper:** Arjun Visakh and M. P. Selvan (2022), *Smart charging of electric vehicles to minimize the cost of charging and the rate of transformer aging in a residential distribution network*, Turkish Journal of Electrical Engineering and Computer Sciences, 30(3), 927–942, DOI https://doi.org/10.55730/1300-0632.3819. Publisher https://journals.tubitak.gov.tr/elektrik/vol30/iss3/28/; prior journal-site PDF link https://aj.tubitak.gov.tr/elektrik/issues/elk-22-30-3/elk-30-3-28-2106-80.pdf inaccessible in audit.

## 1. Explicit evidence (publisher abstract only)
The paper proposes optimizing EV **charging powers** in response to **real-time pricing tariffs** to lower owners' charging expenditure. It argues a tariff tied to system demand can shift charging away from high demand, relieve congestion and mitigate aging of residential distribution transformers. The published abstract asserts simulation improvements in both owner charging costs and modeled transformer aging rate. **No numerical percent, field-measured HST, source equations, implementation/solver, EV deadline reliability, actual price signal locality, GHG reductions, heat-wave resilience, or social equity may be attributed to this abstract alone.**

## 2. Research inference and necessary caveats
- **Power → transportation information/control:** electricity prices influence charging decisions; this is a price-mediated **information/economic dependency**, not independent physical demonstration of a thermally enforced P→T charger power restriction.
- **Transportation → power physical:** changing actual EV AC charging current/load changes transformer thermal forcing, HST and modeled insulation aging under qualified grid and transformer models.
- **Potential physical P→T feedback for thesis (not validated by this paper):** HST limits, dynamic thermal ratings, protection/utility policy reduce allowable EV charging power, affecting delivered energy and departure requirements.
- **Price ≠ congestion universally:** a regional price may not reflect a particular transformer, cheap periods can attract synchronized charging peaks, existing weather-dependent loads and thermal inertia may dominate. The same authors' 2023 follow-up *Assessing the need for network-based technical constraints in economic optimization of electric vehicle charging* (https://doi.org/10.1007/s00202-023-01764-z) examines whether economic cost minimization sufficiently enforces local operating requirements.
- **Reliability vs resilience:** less modeled insulation aging supports long-term component reliability; resilience needs **hazard-conditioned service preservation, crossing/propagation and recovery** under extreme heat.
- **Sustainability:** lower user price = affordability; lower model-derived aging = reduced asset-consumption proxy. Environmental GHG, energy losses, renewable share and embodied impact require dedicated measurements/data and system boundaries. Peak reduction does not imply lower marginal emissions.

## 3. Four distinct research pathways

| Pathway | Literature-supported or proposed mechanism | Quantifiable candidate | Verification condition |
|---|---|---|---|
| Engineering reliability | EV load → transformer HST → aging | HST [°C], FAA dimensionless, equivalent aging time [h] | Valid transformer equations and observed thermal measurements |
| Physical resilience | Heat + charging load → capacity restriction → lost/delayed EV charging; restoration | first thermal-limit crossing [min], downstream delay [min], unmet required kWh, recovery-to-service [min] | Explicit equipment limits, controls and service requirements; field causality only if real connected records |
| Economic sustainability | Real-time price + charge-power control → owner bill and DSO operating decisions | user bill [currency], tariff marginal cost, operating cost | Pricing rules and correct consumer burden, nonanticipative decisions |
| Environmental/social sustainability | Charging time affects energy losses, marginal GHG and service equity | kWh losses, kgCO2e via **verified** time-dependent emissions factors, deadline satisfaction [%], fairness across vehicles | Marginal emissions data, network model, user requirements and optional lifecycle scope |

## 4. Candidate thesis mathematical framework (authors' ideas inspired it; equations below are **OUR PROPOSAL**, not quoted from 2022)
Time k=0...K-1, interval Δt, scenario ω. Nonanticipative charging control π determines delivered EV charging `p_{i,k}(ω)`.

**Economic objective (price-only comparator):**
\[
C_\pi=\Delta t\sum_{k=0}^{K-1}\sum_i \pi_k(\omega) p_{i,k}(\omega).
\]
Prices can be exogenous observed forecasts or endogenous `π_k(P_net,k)` if justified; distinguish latter's optimization feedback, market vs local demand.

**Power and physical state:**
\[
P_{net,k}=P_{base,k}+\sum_i p_{i,k},\quad
I_{tr,k}=\mathcal G(P_{net,k},Q_{net,k},V_k,\mathcal N),
\quad
x_{k+1}=f_\theta(x_k,I_{tr,k},T_{a,k},u_{cool,k}),\quad T_{H,k}=h(x_k).
\]
\(x\) should include justified oil/winding thermal states and thermal memory; a fitted lumped model is not full transformer proof. Network topology and true sensor-hotspot mapping must be established.

**Insulation-aging assessment:** for suitable insulation and independently checked standard edition,
\[
L=\Delta t\sum_k F_{AA}(T_{H,k}),\qquad F_{AA}(T)=\exp(15000/383-15000/(T+273)).
\]
This estimates equivalent thermal-aging **time**, not observed transformer years remaining or failure probability.

**Service objective:** EV i has arrival a_i, departure d_i, usable energy E_i and minimum departure SOC s_i*. Subject to
\[
s_{i,k+1}=s_{i,k}+\eta_i p_{i,k}\Delta t/E_i,\quad
0\le p_{i,k}\le \bar p_{i,k}\mathbf 1(a_i\le k<d_i);
\quad
U_i=E_i[s_i^*-s_{i,d_i}]_+ .
\]
Additional SOC saturation, charger temperature-dependent power limits, taper and feeder voltage constraints apply only if equipment specific.

**Thermal risk and service resilience:**
\[
H_{tr,k}=T_{H,lim}-T_{H,k},\quad
R_{over}=\Pr(\max_k T_{H,k}>T_{H,lim}),\quad
E_{short}=\mathbb E\sum_iU_i.
\]
Thermal limit must come from specific equipment/rating policy; a duration above threshold and crossing time are also useful. Resilience is not a numerical property of an aging equation alone; record time to crossing, downstream control delay and time to restore requested service.

**Sustainability candidates beyond bills:**
\[
E_{loss}=\Delta t\sum_k P_{loss,k},\quad
G_{charge}=\Delta t\sum_k g_{marginal,k} P_{grid,charge,k}
\]
with location-specific time-dependent **marginal** emissions factors, accounting for associated baseline changes where a defensible causal comparison is possible; full life-cycle claims need expanded system boundaries. Avoid implying cheap is low-carbon.

**Proposed transparent multiobjective comparison:** evaluate Pareto tradeoffs between `C_π` (currency), `L` (equivalent aging h), `ΣU_i` (kWh), optional `G_charge` (kgCO2e); if scalarize, normalize/convert units and prespecify weights. Physical thermal safety constraints and essential mobility needs can instead be hard constraints. For uncertain heat/arrivals, use scenario-based/nonanticipative or robust/chance constraints with stated distribution confidence.

## 5. Strongest candidate experimental comparison
For identical qualified network, charger, transformer and weather, test:
1. **B0** Uncontrolled charging, realistic arrivals/SOC.
2. **B1** Published-method **concept**: real-time electricity price-only cost-minimizing charging. No false claim of exact source algorithm reproduction without full PDF and method.
3. **B2** Thermal-aware charging with measured/qualified transformer state estimates and explicit rating/HST constraints.
4. **B3** Proposed coupled thermal+service strategy: thermal safety + required departure energy + price, with optional carbon sensitivity analysis. If infeasible, quantify service deficits rather than ignoring them.
Factorial scenario axes: regular vs documented extreme-hot conditions (beyond SINTEF actual weather-range = extrapolation/simulation only); EV penetration and arrival coincidence; price/transformer local correlation; transformer initial oil/HST state; network base load and power factor; charger derating, service deadline and SOC. Use same input information in all approaches and multiple stochastic replicates.

**Scorecard:** HST held-out MAE/RMSE [°C] if observations, peak HST and hot-time [°C,h], equivalent aging time [h], thermal-limit crossing and risk, transformer dynamic loading margin [kVA], EV kWh unmet/departure lateness, price paid, electricity losses and source-qualified GHG (where factors exist), solver wall-clock and violations, and uncertainty intervals. Observe separate P→T and T→P directions; don't confuse tariff-mediated control with thermal forcing.

## 6. Prior-art/novelty constraints
- Visakh & Selvan 2022 already demonstrate price-coordinated charging and reported modeled aging reduction.
- Visakh & Selvan 2023 explicitly interrogate need for network technical constraints under price optimization.
- Crozier et al. 2020 *Controlled workplace charging ... transformer aging*, https://doi.org/10.1016/j.apenergy.2020.115352 compares electricity bills, transformer health and charging capacity.
- IEEE Access 2020 *Reducing the Impacts of Electric Vehicle Charging on Power Distribution Transformers*, https://doi.org/10.1109/ACCESS.2020.3040056, considers transformer thermal demand-response tariff.
- Nie et al. 2026 https://doi.org/10.1016/j.epsr.2025.112522 compares transformer aging and EV profit; not novel to combine economics with aging in an optimization objective.
**Potential defensible question**, subject to more novelty falsification: *Under extreme heat, to what extent does explicit transformer thermal state/time memory and verified capacity restriction alter the feasibility, critical transition times, and delivered mobility service compared with economically motivated price-only scheduling?*

## 7. Data and evidence readiness
- SINTEF transformer field original: hourly weather, current, oil and *sensor-labelled* HV/LV HST (8,589 good rows per HST variable) allows qualified **component** thermal-state validation, but ambient only up to +25.97 °C; no verified extreme heat.
- Existing Slovenia P/Q station measurements: verify units/rating/topology; **not connected to same transformer and EVSE** with thermal control.
- KU Leuven EV charging records: sessions/electrical/battery channels; independent setup and unverified synchronicity with transformer.
- No same-site measured transformer-HST-to-EVSE-delivery restriction loop currently validated in project. Explicitly distinguish modeled coupled counterfactuals from observed system resilience.

## 8. Source verification and screening next
Retrieve publisher PDF or authentic author manuscript; verify original optimization variables, exact tariff price formation, constraints, thermal aging equations, solver, baseline comparison, simulated network/EV numbers, actual % improvements, weather season, service adequacy and price locality; extract page/equation/figure citations. JBI protocol v0.3 researcher-approved, **no reviewer inclusion yet**; keep candidate role **CORE+CONTEXT/CONTROL provisional**. Do not assert the 2022 original contains the proposed full resilience, sustainability, robust-control, carbon or extreme-heat formulation.

**Current status:** STRONG BENCHMARK / PRIOR-ART CANDIDATE FOR PRICE-ONLY SMART CHARGING, not established heat-resilience or LCA validation.
