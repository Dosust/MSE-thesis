# Literature-Based Qualification of Four Power + Four Electrified Transportation Components — V2

**Date:** 2026-10-10  
**Status:** WORKING LITERATURE DECISION / NOT AN EQUIPMENT-VALIDATED 8-COMPONENT MODEL / NOT A SYSTEMATIC REVIEW / NO NUMERICAL ABLATIONS EXECUTED.  
**Scientific authority:** Current canonical GO/SO1–SO3, Conceptual V5, Mathematical V3, frozen Electrified Transportation System boundary and two-pathway sustainability authority unchanged. Proposed V6 remains provisional.

## 1. Research decision

**The objective is NOT to make eight equations.** The objective is to test whether four independently identifiable Power and four independently identifiable Electrified Transportation *physical components* are the minimum sufficient portfolio to study thermal states, qualified interdependencies, service impacts, and resilience under extreme heat.

**Literature validation means only source-backed physical/mathematical feasibility at the studied technology**, not that our installation has been identified, its thermal limit is admitted, it implements a specified operating action, or its physical predictions are independently validated.

**40-source caveat:** The 40-row screening CSV is a reconstructed 19 P + 21 T_e candidate set. It comprises 29 thermal-limit inventory entries and 11 labeled candidate additions; some rows are nested assemblies, functions, controls or mutually exclusive device options, not the original 40 independently identified hardware units. Historical identity reconciliation (G0) remains OPEN. See:
- [Selection protocol](../DOSSIYA_REALITY_FIRST_40_TO_8_COMPONENT_SELECTION_PROTOCOL_V1.md)
- [40-row source and G0–G5 screening CSV](40_TO_8_COMPONENT_SELECTION_MATRIX_PROVISIONAL_V1.csv)
- [Initial portfolio and planned ablations](40_TO_8_PHYSICAL_COMPONENT_SELECTION_MATRIX_PROVISIONAL_V1.md)
- [First literature review](40_TO_8_LITERATURE_QUALIFICATION_AND_SDG_TRACEABILITY_V1.md)

## 2. Four Power component candidates — verified primary source and what it actually proves

| Candidate | Primary source: paper-specific method/finding | Candidate mathematics (not case-admitted exact law) | Available / required observations | Literature-only verdict |
|---|---|---|---|---|
| **P13 Distribution transformer**, specifically oil-immersed only if installed | **Hilshey et al. (2013)** [full author PDF](https://phines.w3.uvm.edu/publications/2013/hilshey_2013.pdf), [DOI](https://doi.org/10.1109/TSG.2012.2217385): IEEE-based thermal ODEs driven by simulated 25-kVA residential+EV loads, 2009 NHTS, historical weather, Monte Carlo charging/aging. **Pan et al. (2025)** [open paper](https://doi.org/10.1049/hve2.70024): dynamic thermal rating of transformers AND cables with EV response; cost/power improvements are *their* scenario findings, not our result. | Thermal energy: \(\tau_o\dot T_{TO}=-T_{TO}+T_a+\Delta T_{TO,U}(I)\) (Pan Eq. 6); winding/hotspot evolution, insulated aging output. Avoid assuming aging = outage. | Historical weather/NHTS + electrical test feeders available for simulation. Missing selected nameplate, loss and cooling parameters, thermal measurements, actual operator thermal capability rule. | **STRONG PHYSICAL MODEL FAMILY; CASE/P→T_e THERMAL RESTRICTION OPEN.** |
| **P14 Distribution feeder**, exact overhead versus buried type must be specified | **Marshall et al. (2013)** [DOI](https://doi.org/10.1016/j.epsr.2012.12.006), accessible **publisher abstract only**: modeling transient heating around underground cables with PEV demand. **Pan et al. (2025)** [open paper](https://doi.org/10.1049/hve2.70024): cable conductor transient temperature and dynamic thermal rating integrated with network/planning. | Algebraic Kirchhoff/AC network calculations required; add \(\rho c\partial T/\partial t = \nabla\cdot(k\nabla T)+q_{\mathrm{Joule}}\) **only if** real cable thermal states change the QOI. Pan's conductor Eq. 5 is discrete transient rating; no unconditional universal conductor limit. | Public IEEE feeder circuits and NOAA. Missing actual line/cable installation, cross-section/material, thermal environment (wind/solar or soil), current, voltage and limits. | **STRONG ELECTRICAL/THERMAL BASIS; INDEPENDENT THERMAL ODE CONDITIONAL.** |
| **P15 Physical breaker** | **ABB RET615 ANSI application manual**, [manufacturer PDF](https://library.e.abb.com/public/e5e9f20ae5454e14a5572a13ec67e88a/RET615ANSI_appl_201230_ENb.pdf): thermal-overload ANSI 49T exists; **default configuration does not trip the breaker** in cited implementation. Manufacturer functionality is NOT experimental evidence for our site; no strong primary paper found establishing selected-site breaker thermal causality. | **Hybrid control** \(b^+ = \mathcal R(T_{\rm sensed},I,\mathrm{relay\ settings},b)\) is a *proposed schematic*, not an observed ABB formula. Switch open/closed is a discrete status, not a continuously evolving thermal state. | Missing breaker model, relay topology, settings, events, voltage/current and actual switch actions. | **DEVICE ROLE PLAUSIBLE; TEMPERATURE→BREAKER OPERATION NOT QUALIFIED. CHALLENGE IN 4+4.** |
| **P06 Transformer cooling apparatus**, only if distinct physical assembly in case | **Li et al. (2024)** [open primary study](https://doi.org/10.1049/hve2.12345): **110-kV** oil natural/air forced transformer geometry and thermofluid simulation compared with temperature-rise tests; average model error ~2 °C; cooling geometry affects temperature. These 110-kV parameters are NOT portable to a small EVSE-serving transformer. | \(C_{th}\dot T=P_{\rm heat}-Q_{\rm cooling}\) is an **author-independent generic first-law template**. A separate fan/pump/coolant state requires equipment and measurement evidence; otherwise cooling can be a constitutive loss term within P13. | Published experimental paper, but no selected-cooler temperature/flow/fan status or auxiliary power. | **STRONG HEAT-REJECTION PHYSICS; SEPARATE HARDWARE BLOCK NECESSITY OPEN.** |

## 3. Four Electrified Transportation component candidates — verified primary source and what it actually proves

| Candidate | Primary source: paper-specific method/finding | Candidate mathematics (not case-admitted exact law) | Available / required observations | Literature-only verdict |
|---|---|---|---|---|
| **T18 DC EV charger / EVSE assembly** | **Krama et al. (2026)** [open field study](https://doi.org/10.1016/j.ecmx.2026.101960): measured a commercial air-cooled ~50 kW charger in Qatar, ambient range ~15–55 °C, rectifier temperature, AC electrical data, offered/delivered DC power, efficiency, distortion, sessions. Strong observed **charger self-derating**; no paired transformer physical field validation. Raw data available on request. | Consistent grid-side \(P_{\rm AC,in}=P_{\rm DC,out}+P_{\rm converter+auxiliary\ losses}\), with correctly matched boundary; \(P_{\rm DC}\le C_E(T_{\rm rect},T_a,\mathrm{control})\) only for an identified admissible device law. AC reactive load separate. | Paper field evidence. Missing selected device, matched AC port P/Q, derating command logs and transferability checks. | **STRONGEST T_e THERMAL CAPABILITY CASE; T_e→P ACTUAL AC RESPONSE OPEN.** |
| **T05 EVSE cooling device**, only if separately measurable/controlled | **Rahman et al. (2024)** [IEEE Access review](https://doi.org/10.1109/ACCESS.2024.3385429): credible thermal-management **survey** of power-electronic converters; **not a device-specific primary cooling experiment**. **Krama et al. (2026)** observes field charger thermal effects but does NOT prove our charger has a separately necessary cooling-device dynamical block. | Heat rejection \(Q_{\rm cool}(T,T_a,u_{\rm fan/pump})\); auxiliary \(P_{\rm aux}\) must be included in grid-side AC power. No invented airflow/heat-transfer coefficients. | Need fan/pump speed or duty, air/coolant temperature, rectifier temperature, and auxiliary energy at same site. | **SUPPORTING GENERAL PHYSICS ONLY; SEPARATE-BLOCK INCLUSION OPEN.** |
| **T08 DC charging cable** (versus T09 connector alternative) | **Zhang et al. (2023; online)** [publisher abstract](https://doi.org/10.1080/10407782.2023.2285374): equivalent thermal-circuit method calibrated/tested against observed charging-cable temperature rise; exact full constitutive equations unavailable in accessible abstract. **Liang et al. (2025)** [publisher abstract](https://doi.org/10.1016/j.ijthermalsci.2025.110139): connector current/contact resistance/ambient temperature and model comparison, but connector not cable. | Candidate \(C_{\rm cable}\dot T=I_{\rm DC}^2R(T)-Q_{\rm out}\), **first-law reconstruction**, not verbatim Zhang Eq.; only activate if measured cable temperature → actual current limit. | Manufacturer cable/connector data, contact temp/current, derating and disconnection logs absent. No manufacturer universal limit assumed. | **EXPERIMENTAL CABLE TEMPERATURE-MODEL PRECEDENT; SERVICE-LIMIT CONDITIONAL.** |
| **T12 Vehicle traction battery pack / RESS** | **Bernardi et al. (1985)** [original](https://doi.org/10.1149/1.2113792): general cell heat/energy balance, chemical and ohmic contributions. **Thakur et al. (2023)** [review](https://doi.org/10.1016/j.applthermaleng.2023.120303): battery thermal management under fast charging (supporting, not selected battery validation). | Battery-terminal **energy** state \(\dot E_B=P_{\rm battery,accepted}\) after consistent boundary definition; thermal state \(\rho c\partial_t T=\nabla\cdot(k\nabla T)+q\) and acceptance \(P_B\le C_B(T_B,SOC)\) ONLY if case-relevant. SOC is not temperature; charger power ≠ battery terminal power without vehicle-side losses. | ACN-Data useful for charging sessions only: no direct BMS SOC/temp. Actual battery chemistry, manufacturer limits and SOC/accepted-power logging OPEN. | **STRONG ENERGY/THERMAL FOUNDATIONS; SEPARATE BATTERY TEMPERATURE DYNAMICS CONDITIONAL.** |

**Publication levels:** Hilshey/Pan/Krama/Li primary papers directly examined in publisher/author-accessible materials. Zhang/Marshall/Liang accessible publisher abstracts support general methods but NOT exact full equations. Rahman/Thakur are reviews and cannot be cited as if they experimentally validated a selected device. ABB is manufacturer protection documentation, not peer-reviewed field proof.

## 4. The six selection checks and actual admission result

G0: physically distinct correct inventory object. G1: actual compatible equipment and correct port. G2: supported thermal mechanism. G3: indispensable for actual directional interdependency OR declared required electricity/mobility service. G4: equations + admissible parameters/data/validation plan. G5: independent added value of detailed component representation confirmed by paired exclusion/ablation.

| Component | Physics / math from literature (G2) | Actual case/ports (G1/G3/G4) | Independent necessity (G5) | Decision |
|---|---|---|---|---|
| P13 transformer | Strong | OPEN | NOT_RUN | **Core proposed** |
| P14 feeder | Strong | OPEN | NOT_RUN | **Core electrical path; optional detailed thermal state** |
| P15 breaker | Protection functionality documented; thermal action CASE OPEN | OPEN | NOT_RUN | **Conditional / replace if no actual thermal response** |
| P06 transformer cooling | Strong equipment-type physics; small-case transfer OPEN | OPEN | NOT_RUN | **Conditional / aggregate if redundant** |
| T18 EVSE | Strong device-family empirical heat derating | OPEN | NOT_RUN | **Core proposed** |
| T05 EVSE cooling | General supporting thermal management | OPEN | NOT_RUN | **Conditional / aggregate if redundant** |
| T08 charging cable | Experimental thermal model precedent | OPEN | NOT_RUN | **Conditional / replace with connector T09 if controlling** |
| T12 battery pack | Strong general physics/energy basis | OPEN | NOT_RUN | **Core energy/service; thermal state conditional** |

**Result:** Literature *supports studying all eight*, but it does **NOT validate that all eight are uniquely necessary separate components or distinct dynamical models**. The four strongest functional equipment roles are **P13 transformer, P14 feeder, T18 charger, T12 battery**. The remaining **P15/P06/T05/T08** are unresolved pending compatible topology, primary equipment parameters, measured controls and ablation. If there is no valid independent fourth component in one subsystem, report fewer qualified components rather than force 4+4.

## 5. The physical-science-to-service mathematical chain (proposed)

1. **Heat environment** \(H(t)\) is common external forcing for P and T_e, not P↔T_e causation.
2. **Power thermal state** \(x_P\): loss, inertia, heat rejection; potential \(T_{TO},T_{HS}\) pending oil-type admission.
3. **EVSE thermal state/capability** \(x_E,C_E\): measured rectifier state where available; ambient-derived limit if that is what manufacturer actually specifies.
4. **Electrical AC port**: \(P_{AC},Q_{AC},V,I\); \(P_{AC}=P_{DC}+P_{loss}\) only under consistent EVSE control volume and auxiliary accounting.
5. **P→T_e additional conditional chain**: \(x_P^{th}\to C_P\) *documented actually implemented loading/control action* \(\to\) EVSE AC supply \(\to\) delivered battery energy/service. Unobserved trip ≠ documented capability.
6. **T_e→P conditional chain**: \(x_E^{th}\to C_E\to\) **actual** EVSE AC power/reactive demand \(\to\) transformer load/loss/temperature. A DC power decline alone does not specify AC response.
7. **Services**: electrical delivery \(\int P_{\rm served}dt\) versus requirement; vehicle battery departure readiness \(E_B(t_{\rm dep})\ge E_{\rm req}\) is a **proxy**, not observed passenger trips.
8. **Time**: first thermal capability restriction, actual operating action, first service shortfall, recovery (where actually modeled), attributable cross-sector propagation delay only when identifiable via matched perturbation/measurement.

**Test using current frozen meanings:** M0 controlled severed tested influence; M1 static/algebraic qualified electrical coupling; M2 added dynamic thermal mechanism only after evidence qualification. Run same environmental forcing, non-EV demand, initial conditions, charging requests and control assumptions. Numerical solver consistency/energy conservation and independent physical validation are different gates.

## 6. Resilience, two sustainability pathways and SDGs — no direct equipment→SDG jump

**Resilience:** Maintain/recover *declared* required electricity and mobility services, with critical timing. Improvement/adaptation/restoration is an optional response: modify physical model inputs/controls and **rerun**, comparing with the same extreme-heat case without response.

**Sustainability pathway 1 (direct):** differences from reference to extreme-heat case in observed/model-valid electricity loss (kWh), EV energy shortfall (kWh and number/fraction meeting departure requirement), service time (minutes), emissions \( \Delta E\times \mathrm{EF}\) only with justified emission factor and energy boundary, cost with justified price/maintenance data, access/continuity with measured service population when available.

**Pathway 2 (engineering response):** comparison of extreme heat WITH versus WITHOUT a documented Improve/Adapt/Restore action: record improved service AND added cooling auxiliary energy, power losses, material/maintenance burden and costs. Positive resilience ≠ automatically positive sustainability.

| Local **thesis** output (units) | Sustainability meaning | SDG target thematic relevance | **Is it the official SDG indicator?** |
|---|---|---|---|
| Electricity-service shortfall (kWh, minutes) | Reliability, continuity | [7.1](https://sdgs.un.org/goals/goal7), [9.1](https://sdgs.un.org/goals/goal9) | **NO**: official 7.1.1 is *population electricity access*, not minutes/kWh; official 9.1.2 is *transport volumes*, not transformer uptime |
| Vehicle ready-on-time fraction (%, count) | Mobility readiness proxy | [11.2](https://sdgs.un.org/goals/goal11) | **NO**: 11.2.1 concerns *population access to public transport*, not charge completion |
| Device/network losses (kWh), estimated GHG (kgCO₂e, where EF is justified) | Environmental effect, heat/response burdens | 7.3, potentially climate-relevant targets with independent mapping | **NO**: official 7.3.1 is *primary energy / GDP*; local efficiency/loss is NOT 7.3.1 |
| Energy, maintenance and cooling cost ($/defined horizon) | Economic service burden | 9.1 contextual relevance | **NO** official target-indicator equivalence without matched definitions |

SDG alignment is an evidence-bounded discussion **after** indicator measurement. Do not claim SDG achievement or numerical official-indicator impact from local charging simulations.

## 7. Decisive next evidence and removal tests

| Test | Perturbation/reduced model | Keep separate block only if... |
|---|---|---|
| P06 cooler | P13 with aggregated manufacturer cooling envelope vs distinct fan/pump dynamics | Real cooler independent state/control changes held-out hotspot/capability/recovery QOIs |
| P15 breaker | Fixed permissible AC input / actual policy vs realized breaker switching | Real thermal rule causes observable switching/service change rather than alarm only |
| T05 cooler | T18 with temperature-dependent integrated cooling vs separate cooling dynamics | Fan/pump duty + auxiliary AC draw changes predicted rectifier/charging/AC QOIs |
| T08 cable | Fixed certified current rating/connector check vs dynamic cable heat | Cable becomes actual limiting component and event/service difference exceeds preregistered observational uncertainty |
| P14 detailed feeder | Algebraic feeder vs extra conductor temperature state | Additional temperature predicts real thermal rating or service constraint better |
| T12 thermal battery | Energy-only acceptance envelope vs pack thermal model | Battery temperature changes accepted charging power/readiness and is identified |
| P13 transformer | Static thermal envelope versus measured time-dependent model | Dynamic model improves state/event prediction under matched inputs and independent data |
| T18 charger | Manufacturer ambient-only derating versus admissible internal-temperature model | Measured inner temperature/time changes actual DC AND AC charging response beyond simpler model |

**All tests NOT_RUN.** Select failure thresholds and QOI error tolerances before execution, tied to actual sensor accuracy and service requirement; never invent universal numerical pass scores.

## 8. Sources checked and limitations

Primary source:
- Hilshey et al. 2013: https://doi.org/10.1109/TSG.2012.2217385 (author full text).
- Marshall et al. 2013: https://doi.org/10.1016/j.epsr.2012.12.006 (publisher abstract, not full equations).
- Pan et al. 2025: https://doi.org/10.1049/hve2.70024 (publisher open text includes Eq. 5–8 cable/transformer).
- Li et al. 2024: https://doi.org/10.1049/hve2.12345 (publisher abstract and modeling text, 110-kV ONAF; temperature-rise validation).
- Krama et al. 2026: https://doi.org/10.1016/j.ecmx.2026.101960 (open field paper; raw data request).
- Zhang et al. 2023 online: https://doi.org/10.1080/10407782.2023.2285374 (publisher abstract).
- Liang et al. 2025: https://doi.org/10.1016/j.ijthermalsci.2025.110139 (publisher abstract).
- Bernardi et al. 1985: https://doi.org/10.1149/1.2113792 (original energy-balance abstract).
- ABB RET615 ANSI 2010 manual: https://library.e.abb.com/public/e5e9f20ae5454e14a5572a13ec67e88a/RET615ANSI_appl_201230_ENb.pdf .

Supporting reviews (NOT direct device validation):
- Rahman et al. 2024: https://doi.org/10.1109/ACCESS.2024.3385429 .
- Thakur et al. 2023: https://doi.org/10.1016/j.applthermaleng.2023.120303 .

Official target/indicator authority:
- UN SDG 7: https://sdgs.un.org/goals/goal7 .
- UN SDG 9: https://sdgs.un.org/goals/goal9 .
- UN SDG 11: https://sdgs.un.org/goals/goal11 .

### Explicit unsolved scientific gates
- Historical exact 40 component identity reconciliation: OPEN.
- Compatible oil/dry transformer–feeder–DCFC–vehicle configuration and ratings: OPEN.
- Actual transformer thermal state → *implemented* EVSE power restriction: OPEN.
- Actual EVSE temperature → grid-side AC P/Q response → transformer measured thermal effect: OPEN.
- Independent physical validation, parameter confidence, actual M0/M1/M2 trials, component removal: NOT_RUN.
- Claims of measured sustainable or SDG outcomes: NOT_ESTABLISHED.

**Final literature decision:** The eight are reasonable **candidates to investigate**. The literature does not independently select or validate all eight. Begin with transformer–feeder–DCFC–battery as the strongest physical/service backbone and screen breaker/cooler/cable necessity with evidence and ablation before final 4+4 admission.
