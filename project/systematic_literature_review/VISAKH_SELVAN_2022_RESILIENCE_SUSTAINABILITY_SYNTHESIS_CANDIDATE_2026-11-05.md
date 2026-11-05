# Visakh & Selvan (2022) — Research synthesis: smart charging, resilience, and sustainability

**Date:** 2026-11-05  
**Status update 2026-11-05:** Publisher abstract verified; **author-uploaded full-text transcription inspected** at https://www.researchgate.net/publication/360722059_Smart_charging_of_electric_vehicles_to_minimize_the_cost_of_charging_and_the_rate_of_transformer_aging_in_a_residential_distribution_network . Source-specific equations, test setup, solver and numerical results now extracted in the addendum below. **Publisher-hosted PDF still blocked; OCR/transcription versus publisher source has not been independently cross-verified, numerical simulation not reproduced, no reviewer-screened inclusion, no measured coupled thermal resilience validation.**
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
Original author-uploaded full-text transcription now inspected and numerical/model/solver details extracted in the addendum; seek publisher PDF for transcription cross-check and exact figure/tables; then reproduce original simulations with documented parameter equivalence and fair data splits if computationally justified. Audit exact pricing interpretation, device models, short-time thermal limits, departure/charging fulfillment, heatwave and recovery scope. JBI reviewer-screening remains pending. JBI protocol v0.3 researcher-approved, **no reviewer inclusion yet**; keep candidate role **CORE+CONTEXT/CONTROL provisional**. Do not assert the 2022 original contains the proposed full resilience, sustainability, robust-control, carbon or extreme-heat formulation.

**Current status:** STRONG BENCHMARK / PRIOR-ART CANDIDATE FOR PRICE-ONLY SMART CHARGING, not established heat-resilience or LCA validation.


## 9. Full-text equations and numerical evidence upgrade — 2026-11-05

**Primary provenance:** Original publisher abstract https://journals.tubitak.gov.tr/elektrik/vol30/iss3/28/ ; author-uploaded full-text transcribed on ResearchGate https://www.researchgate.net/publication/360722059_Smart_charging_of_electric_vehicles_to_minimize_the_cost_of_charging_and_the_rate_of_transformer_aging_in_a_residential_distribution_network . Public publisher PDF link (https://aj.tubitak.gov.tr/elektrik/issues/elk-22-30-3/elk-30-3-28-2106-80.pdf) failed with HTTP 502. The text source displays actual equations, sections, tables and page labels; no publisher-file binary checksum or full experiment reproduction is asserted. **Earlier 'source equations unverified' applies only to the initial abstract-only review and has now been superseded by this original-text extraction.**

### Paper study configuration (pp. 929–938)

- IEEE European LV feeder, **55 households** at 240 V single-phase / 416 V line-line, **160 kVA 11 kV/416 V three-phase distribution transformer**, 0.9 lagging non-EV base power factor (p. 929).
- **100% EV penetration**: one EV for each of 55 consumers; four historical EV battery models and efficiencies; up to **3 kW AC-side per EV**, no V2G (p. 930).
- Gaussian-model arrival **18:00 ± 2 h** and departure **07:00 ± 2 h** (paper's means/standard deviations), initial battery energy fraction normal with mean **50%**, sd **30%** of usable capacity; all target full by departure (p. 930). Joint stochastic behavior, physical clipping/truncation of Normal SOC and transferability to actual datasets remain to be checked.
- Daily scheduling discretized into **96 fifteen-minute intervals**; MATLAB **CVX** convex charging-power optimization, **OpenDSS** electrical simulation, MATLAB IEEE-style thermal model; **two illustrative Madrid days**, one in July/summer and one in December/winter (pp. 929, 937).
- The original work compares **uncontrolled/dumb** and **smart price-based** charging; a base-load-only scenario is also reported. No adaptive extreme-heat recovery experiment or measured charger–transformer connected site.

### Exact method nuance: price-to-loading construction (pp. 931–933)

The paper models real-time tariff as **r_k(l)=k0+k1*l** (Eq. 5), where 'l' is the relevant load variable. Its cost attributed to EV charging in time slot k (Eqs. 7–12) is the *integral of that marginal price rule from base load to total load*:

C_EV = Delta_t * sum_k integral_{L_B,k}^{L_B,k+P_EV,k} r_k(l) dl
     = Delta_t * sum_k [k0 P_EV,k + k1 L_B,k P_EV,k + (k1/2) P_EV,k^2].

The constant Delta_t is omitted from the published minimization as it does not change the minimizer. This objective is **convex quadratic** when k1>0 and feasible charger/energy constraints are affine; the authors say it is solvable by an interior-point method (p. 933). **This is not the same expression as an exogenous retailer price \\sum pi_k P_EV,k Delta_t** when prices depend on local EV charging. 'Price minimization equals decongestion' depends on the authors' constructed local price-load link, not a universal retail-price theorem. For exact reproduction verify their use of kW versus kVA and power factor when moving between OpenDSS apparent load and energy-price load.

Constraints Eqs. 13–17: total load = base plus availability/energy-eligible EV power; each EV meets desired departure energy and does not exceed battery capacity, charging power in [0, 3 kW], and final energy = initial + sum_i eta_n p_{n,k} Delta_t. Their model minimizes **charging cost**, while HST and equivalent ageing are **computed after optimization**, not included directly as an objective or explicit validated temperature-limit constraint.

### Original transformer thermal calculation (pp. 935–936)

Eq. 19: HST = ambient + top-oil rise + winding HST rise over oil. Eqs. 20–21 use discrete first-order thermal memory with exp(-Delta_t/tau); Eqs. 22–23 use load factor and IEC/IEEE-type power-law steady-state thermal rises. Paper reports tau_o=3 h, tau_w=5 min, rated top-oil rise 55 degC, rated winding-over-oil rise 25 degC, R=5, n=m=0.8 **for its assumed 160 kVA transformer**. Eq. 24 has F_AA=exp[15000/(110+273)-15000/(T_H+273)], referencing 110 degC; insulation qualification required before transplantation. Eq. 25 reports **F_EQ = sum F_AA,k Delta_t / sum Delta_t**, dimensionless average ageing acceleration. The equivalently aged duration is F_EQ*duration, not F_EQ 'years' or measured remaining lifetime.

### Numerical baseline reproduction targets (pp. 934–939, Table 3)

| Output | Base only | Uncontrolled EV | Price-smart EV |
|---|---:|---:|---:|
| Peak transformer apparent loading [kVA] | 143.08 | 255.97 | 143.08 |
| All-EV charging cost [EUR] | 0 | 421.39 | 266.61 |
| Summer peak HST [degC] | 91.06 | 167.26 | 94.32 |
| Summer mean HST [degC] | 64.52 | 88.39 | 79.82 |
| Summer equivalent ageing factor [dimensionless] | 0.02 | 12.48 | 0.05 rounded (body text 0.046) |
| Winter peak HST [degC] | 60.95 | 141.34 | 64.22 |
| Winter mean HST [degC] | 38.89 | 62.77 | 54.20 |
| Winter equivalent ageing factor [dimensionless] | 0.0004 | 1.22 | 0.004 |

Reported charging cost change **36.73% reduction** and peak transformer loading **44% reduction**, in the particular 55-EV/160 kVA simulated system; drastic ageing reduction follows removal of severe modeled overload, not field-tested percent lifetime extension. Paper notes summer HST peak >160 degC in uncontrolled case, an adverse modeled threshold, not a reliable default operating condition.

### Important limitations / new falsification route

- **Tariff assumption:** local price modeled explicitly as increasing with loading; exogenous time-of-use or wholesale RTP can synchronize EV loads and create local overload. Avoid universal inference price-minimization => transformer safety.
- **Physics:** transformer thermal law applied via parameterized model, not validation against directly observed HST; original text does not establish measurement-based transformer life consumption or field-calibrated extreme-heat response.
- **Mobility:** the optimization explicitly imposes full departure-energy satisfaction in its constructed cases; it does **not** quantify mobility service loss/recovery or charging restrictions under infeasible heatwave operation.
- **Resilience ≠ ageing:** thermal load, fast TOT/HST constraints and charging service disruptions are separate observables from long-term F_EQ; recovery must be a new assessed trajectory, not inferred from a lower cost.
- **Sustainability:** economic EV cost and modeled asset ageing are supported; network kWh losses, marginal carbon intensity, resource use and equitable charging require additional explicit measurements/models. Lower charging price alone does not imply lower emissions.
- **Important later prior art by same authors:** Visakh & Selvan (2023), *Analysis and mitigation of the impact of electric vehicle charging on service disruption of distribution transformers*, *Sustainable Energy, Grids and Networks* 35:101096, DOI https://doi.org/10.1016/j.segan.2023.101096. This **already directly studies** short-time apparent loading, top-oil and hot-spot limits, charger harmonics, controlled charging, and simulation-based avoidance of service disruption. Therefore, do **not** claim it is novel to add thermal-limit/service-interruption constraints to EV scheduling. The remaining potential thesis distinction must be narrowed through a systematic audit (e.g., explicit coupled thermal state→available mobility service over time, extreme heat, stochastic viability/recovery, and independent HST/electrical-interface validation), not asserted a priori.
- **Additional independent caution:** Unterluggauer et al. (2023), *Impact of cost-based smart electric vehicle charging on urban low voltage power distribution networks*, DOI https://doi.org/10.1016/j.segan.2023.101085, shows in multi-feeder simulations that price-driven charging synchronization can aggravate local congestion.

### Proposed fair experiment

Hold EV session requests, network, external base load and ambient scenario fixed across B0 uncontrolled, B1 reconstructed paper-specific local load-coupled pricing, B1b exogenous retail tariff (if available), B2 calibrated HST-constrained, and B3 state/time + thermal-restriction + departure-energy service policy; report peak HST, equivalent aged hours, top-oil/short-time loading/limit criticality, charging kWh shortfall, energy costs, and explicit calibrated carbon/loss measures **only where data support them**. Check feasibility, thermal inertia, price assumptions, uncertainty and real-time information availability. Require source full-text replication of B1 before claiming quantitative superiority.

**Updated evidence status:** ORIGINAL_EQUATIONS_INSPECTED_FROM_AUTHOR_TRANSCRIPTION | SOURCE_NUMBERS_EXTRACTED | PUBLISHER_PDF_BINARY_NOT_VERIFIED | SIMULATION_NOT_REPRODUCED | NO_MEASURED_COUPLED_RESILIENCE_OR_CARBON_RESULT | JBI_REVIEW_PENDING | SO1_SO3_UNCHANGED
