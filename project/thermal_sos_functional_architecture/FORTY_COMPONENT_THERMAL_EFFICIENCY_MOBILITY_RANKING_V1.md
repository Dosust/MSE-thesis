# Ranking all 40 candidates: Thermal Processes, Cross-System Influence, Efficient Electricity Use and Mobility Service — V1

**Date:** 2026-10-10. **Status:** EVIDENCE-INFORMED QUALITATIVE PRIORITIZATION, **NOT** PHYSICALLY VALIDATED RANKS OR ADMITTED 4+4 MODEL.  
**Machine-readable ranking:** [40 rows, 20 Power and 20 Electrified Transportation](FORTY_COMPONENT_THERMAL_EFFICIENCY_MOBILITY_RANKING_V1.csv).  
**Roster:** The *explicit 20 Power + 20 Transportation* equipment/function screening population in [FORTY_TO_EIGHT_COMPONENT_SELECTION_REGISTER_V1.md](FORTY_TO_EIGHT_COMPONENT_SELECTION_REGISTER_V1.md) (names and IDs preserved unchanged). **Do not mix** its P02, T01 etc. with the incompatible 19 Power + 21 Transportation candidate/thermal-check list in [40_TO_8_COMPONENT_SELECTION_MATRIX_PROVISIONAL_V1.csv](40_TO_8_COMPONENT_SELECTION_MATRIX_PROVISIONAL_V1.csv). Neither is a reconciled, canonical inventory of forty independent physical components; duplicate/nested/boundary/observer entries persist.

**Fixed scientific purpose:** GO/SO1–SO3 remain thermal interdependency under extreme heat, physical state/time and electricity/mobility services. The user's **energy-efficient use and mobility-service emphasis** controls *ranking of service consequences* and downstream environmental indicators; it is **NOT an amendment to the frozen GO/SOs or evidence of an optimization objective**.

## 1. What is ranked and how

The US NRC's *Phenomena Identification and Ranking Table (PIRT)* method ranks the importance and knowledge of phenomena for specific decisions (Ball & Fisher, 2008, [NUREG/CR-6944](https://www.nrc.gov/regulations-legislation/nureg-series-publications/publications-prepared-by-nrc-contractors/next-generation-nuclear-plant-phenomena-identification-and-ranking-tables-pirts-nuregcr-6944/v1)). We adapt the principle as a **thesis-proposed qualitative ranking**, **NOT a formal NRC PIRT**, expert-panel consensus or calculated scientific score.

The columns are:
- **Th = thermal-process importance**: does temperature evolve through self-heating, heat storage, transport, cooling, electrochemistry, temperature-conditioned capability? For actuators and meters, high thermal importance is not presumed.
- **X = potential directional P↔T_e mechanism importance**: does the component carry or condition actual grid-side AC demand/power or implement a *qualifiable* thermal operating response? **H means high *potential*, NOT established causal propagation.** Shared ambient heat is NOT cross-system interaction.
- **E = importance for electricity/energy-use efficiency**: electrical and conversion losses, auxiliary load, delivered/accepted kWh at declared boundaries; an energy-loss indicator is NOT a new thermal law.
- **M = required mobility-service importance**: charging completion, battery readiness, heat-conditioned propulsion/auxiliary energy, mobility when actually observed. Readiness proxy ≠ completed trip.
- **Literature = strength of directly applicable *class-level* evidence**, with H/M/L only qualitative; some rows have **no qualified equipment-class primary study**.
- **Distinctness = apparent ability to justify an independent reduced-model physical block**, subject to G0, chosen case, sensor observability and G5 leave-one-out.

H = high; M = medium; L = low; the values are explicitly **reviewer judgments**, *not measured rates, statistical probabilities, weights or known case properties*. Hierarchical positioning weighs qualified directional influence and required service above heat magnitude; avoid equating high temperature with high importance. In ties prefer nonredundant equipment and better directly applicable literature. This makes the total order a **provisional priority list**, not a quantitative physical ranking. No numerical 1–5/100 scores are invented. **All actual G1/G4/G5 admissions remain OPEN/NOT_RUN.**

## 2. Power: ranked 1–20

| Rank | ID and original candidate | Th | X | E/M | Role | Literature or evidence limitation |
|---:|---|:---:|:---:|:---:|---|---|
| 1 | P02 — Oil-immersed distribution transformer | H | H | H/H | THERMAL CORE | [Hilshey et al. (2013)](https://doi.org/10.1109/TSG.2012.2217385) |
| 2 | P10 — Distribution feeder conductor/cable | H | H | H/H | ELECTRICAL CORE | [Pan et al. (2025)](https://doi.org/10.1049/hve2.70024) |
| 3 | P08 — Transformer protection/loading controller | L | H | H/H | OPERATING GATE OPEN | [ABB RET615 application manual](https://library.e.abb.com/public/e5e9f20ae5454e14a5572a13ec67e88a/RET615ANSI_appl_201230_ENb.pdf) |
| 4 | P05 — Transformer cooling assembly | H | M | M/M | COOLING CONDITIONAL | [Li et al. (2024)](https://doi.org/10.1049/hve2.12345) |
| 5 | P09 — Feeder head breaker | L | M | H/H | BACKUP | [ABB RET615 application manual](https://library.e.abb.com/public/e5e9f20ae5454e14a5572a13ec67e88a/RET615ANSI_appl_201230_ENb.pdf) |
| 6 | P04 — Tank/passive radiator | H | L | M/M | AGGREGATE | [Li et al. (2024)](https://doi.org/10.1049/hve2.12345) |
| 7 | P06 — Bushings/terminals | M | M | M/M | CASE OPEN | *no specific primary source* |
| 8 | P03 — Dry-type transformer | H | H | H/H | ALTERNATIVE | *no specific primary source* |
| 9 | P11 — Cable termination | M | M | M/M | CASE OPEN | *no specific primary source* |
| 10 | P12 — Cable splice/line joint | M | M | M/M | CASE OPEN | *no specific primary source* |
| 11 | P13 — Distribution busbar/switchgear | M | M | M/M | CASE OPEN | *no specific primary source* |
| 12 | P19 — DER inverter | H | M | H/M | ALTERNATIVE | *no specific primary source* |
| 13 | P20 — Grid battery inverter | H | M | H/M | ALTERNATIVE | *no specific primary source* |
| 14 | P15 — Voltage regulator | M | M | M/M | CASE OPEN | *no specific primary source* |
| 15 | P14 — Pole-mounted recloser | L | M | M/M | CASE OPEN | *no specific primary source* |
| 16 | P16 — Capacitor bank | L | L | M/M | BOUNDARY | *no specific primary source* |
| 17 | P07 — Transformer thermal sensor | L | L | L/M | SUPPORT NOT BLOCK | *no specific primary source* |
| 18 | P17 — AC power meter | L | M | H/M | SUPPORT NOT BLOCK | *no specific primary source* |
| 19 | P18 — SCADA/RTU hardware | L | M | M/M | SUPPORT NOT BLOCK | *no specific primary source* |
| 20 | P01 — Upstream supply terminal | L | M | H/H | BOUNDARY NOT COMPONENT | *no specific primary source* |

### Interpretation of Power top four

1. **P02 — oil distribution transformer:** load- and ambient-conditioned winding/oil thermal inertia; Hilshey et al. (2013) provides EV/transformer simulations, Pan et al. (2025) temperature-conditioned rating, and Li et al. (2024) physical thermofluid tests at 110 kV. These are not calibrated for our site.
2. **P10 — feeder conductor/cable:** electrically necessary path; one actual overhead or buried technology must be selected before conductor/soil/wind heat equations. Pan et al. (2025) studies thermal ratings with EV demand. A feeder may be algebraic even if physically counted.
3. **P08 — protection/loading controller:** ranks high for **conditional P→T_e effect**, not for heat generation. ABB's RET615 manual states its 49T is *not configured to trip the breaker by default* in its example. An actual implemented **temperature→setpoint/curtailment/switch action** is a blocking requirement.
4. **P05 — transformer cooling:** physically affects transient heat rejection, but separate component modeling may duplicate P02's cooling function. Retain only if installed/identifiable/necessary versus a valid integrated cooling law.

**Alternative:** P09 breaker, P04 passive radiator, P03 dry-type transformer (technology replacement, not an additional simultaneous transformer). Real transformer/feeder topology overrides this order.

## 3. Electrified Transportation: ranked 1–20

| Rank | ID and original candidate | Th | X | E/M | Role | Literature or evidence limitation |
|---:|---|:---:|:---:|:---:|---|---|
| 1 | T01 — Off-board DC EVSE converter | H | H | H/H | THERMAL CORE | [Krama et al. (2026)](https://doi.org/10.1016/j.ecmx.2026.101960) |
| 2 | T11 — Vehicle battery pack | H | M | H/H | SERVICE CORE | [Gao et al. (2021)](https://doi.org/10.1016/j.energy.2020.119688) |
| 3 | T04 — EVSE cooling system | H | M | H/H | COOLING CONDITIONAL | [Krama et al. (2026)](https://doi.org/10.1016/j.ecmx.2026.101960) |
| 4 | T17 — Vehicle HVAC compressor | H | M | H/H | MOBILITY CORE CONDITIONAL | [Parker et al. (2025)](https://doi.org/10.1016/j.apenergy.2024.125051) |
| 5 | T09 — Charging connector/contact | M | M | M/H | CONTACT CONDITIONAL | [Li et al. (2025)](https://doi.org/10.1016/j.applthermaleng.2025.127680) |
| 6 | T08 — DC charging cable | M | M | M/H | CABLE CONDITIONAL | [Zhang et al. (2023)](https://doi.org/10.1080/10407782.2023.2285374) |
| 7 | T12 — Battery management ECU | M | M | H/H | SUPPORT OR CONTROL | [Gao et al. (2021)](https://doi.org/10.1016/j.energy.2020.119688) |
| 8 | T13 — Battery cooling circuit | H | L | M/H | AGGREGATE | [Bernardi et al. (1985)](https://doi.org/10.1149/1.2113792) |
| 9 | T05 — EVSE cabinet/ventilation | M | L | M/M | AGGREGATE | [Krama et al. (2026)](https://doi.org/10.1016/j.ecmx.2026.101960) |
| 10 | T03 — EVSE DC output module | H | M | H/H | AGGREGATE | [Krama et al. (2026)](https://doi.org/10.1016/j.ecmx.2026.101960) |
| 11 | T10 — Vehicle charging inlet | M | M | M/M | CASE OPEN | *no specific primary source* |
| 12 | T15 — Traction inverter | H | L | M/H | DOWNSTREAM CASE | [Parker et al. (2025)](https://doi.org/10.1016/j.apenergy.2024.125051) |
| 13 | T16 — Traction motor | H | L | M/H | DOWNSTREAM CASE | [Parker et al. (2025)](https://doi.org/10.1016/j.apenergy.2024.125051) |
| 14 | T19 — Vehicle DC-DC converter | M | L | M/M | AGGREGATE | [Parker et al. (2025)](https://doi.org/10.1016/j.apenergy.2024.125051) |
| 15 | T02 — EVSE input contactor/filter | M | M | M/M | AGGREGATE | [Krama et al. (2026)](https://doi.org/10.1016/j.ecmx.2026.101960) |
| 16 | T14 — Onboard AC charger | H | M | M/H | ALTERNATIVE | *no specific primary source* |
| 17 | T20 — Charging communications controller | L | H | H/H | CONTROL SUPPORT | *no specific primary source* |
| 18 | T06 — EVSE rectifier T sensor | L | L | L/M | SUPPORT NOT BLOCK | [Krama et al. (2026)](https://doi.org/10.1016/j.ecmx.2026.101960) |
| 19 | T07 — EVSE AC meter | L | H | H/M | SUPPORT NOT BLOCK | [Krama et al. (2026)](https://doi.org/10.1016/j.ecmx.2026.101960) |
| 20 | T18 — Cabin HVAC blower | L | L | M/H | DOWNSTREAM AGGREGATE | [Parker et al. (2025)](https://doi.org/10.1016/j.apenergy.2024.125051) |

### Interpretation of Transportation top four

1. **T01 — off-board DC EVSE converter:** strongest direct extreme-heat charging evidence. Krama et al. (2026) collected measured charger rectifier temperature, offered/delivered power, grid power indicators, efficiency and session duration in Qatar. Its published charger derating is **not** the selected future EVSE law, and **DC output changes do not directly establish changes to grid-side AC demand**.
2. **T11 — vehicle battery pack:** stored energy and potential battery-temperature/SOC-conditioned acceptance. Gao et al. (2021) reports control-oriented electrothermal battery modeling, temperature-dependent calibration and on-road BMS validation. Start energy balance; battery thermal states only if needed.
3. **T04 — EVSE cooling system:** heat-rejection and auxiliary-load importance, but must demonstrate a *separately identifiable* cooler. A nested fan/control is usually a physical subassembly rather than an independently necessary state.
4. **T17 — vehicle HVAC compressor:** **new priority under the user's explicit energy-efficiency and mobility-service emphasis**. Parker et al. (2025) analyzed 345,622 trips from 300 BEVs across ambient temperatures including extreme heat; at 46–50°C, total energy/km increased 25–28% relative to 26–30°C. The paper **does not isolate the HVAC compressor as the sole cause**, and an EV's higher trip energy demand is only an **indirect and conditional** T_e→P charging-demand pathway. T17 can use measured aux-energy demand as an exogenous model input **without** an independent compressor thermal ODE.

**Alternative high-priority thermal interface:** T09 charging connector/contact (Li et al., 2025) or T08 DC charging cable (Zhang et al., 2023). If verified connector/cable thermal derating imposes an actual current restriction and charger service impact, it may outrank T17 for the narrow **charging-interface thermal-propagation case**. If the model's primary service is only *departure-energy readiness*, not heat-conditioned actual trips, T17 should revert to a supporting energy-demand input rather than a fourth separate component. T12 BMS ECU normally encodes accepted current as control/constraint within T11, not an additional thermal state.

## 4. Provisional 4+4 portfolio for energy-efficient electricity and mobility

| Role | Power | Electrified Transportation |
|---|---|---|
| 1 Main thermal/electrical conversion | **P02 oil transformer** | **T01 off-board DC EVSE converter** |
| 2 Electricity/energy transfer to service | **P10 feeder conductor/cable** | **T11 traction battery pack** |
| 3 Thermal-dependent functional response | **P08 protection/loading controller (actual hardware required)** | **T04 EVSE cooling (separately necessary ONLY if proven)** |
| 4 Thermal response / heat-conditioned service energy | **P05 transformer cooling (separate ONLY if proven)** | **T17 vehicle HVAC compressor (if actual hot-weather mobility demand is in QOI)** |

**Scope check:** This ranking retains the full canonical T_e system boundary (propulsion/auxiliaries still represented through physically sufficient service energy requirements). It does not claim any cross-sector thermal feedback simply from four components in each column. The actual *simultaneous installation* (a matched transformer/feeder/EVSE/vehicle/fleet) is OPEN.

**If strict physical independence is the goal:** P08 controller, P05 cooling and T04 cooling may fail the gate as distinct components/states; **DO NOT FILL 4+4 by arithmetic**. Sensors, AC meters, actual operating-control logs, environmental forcing and service deadlines are essential data, even though ranking them lower for *independent physical thermal modeling*.

## 5. Compare two valid priorities rather than silently choose one

- **Priority A — Charging-interface thermal interdependency** (closest SO1/SO2): T01 charger, T11 battery, T04 cooler (only if independent), and **T09 connector/contact** (or T08 cable if it binds). P02/P10/P08/P05 conditional.
- **Priority B — Energy efficiency and actual heat-conditioned mobility** (the user's stated performance emphasis): T01 charger, T11 battery, T04 cooler (conditional), and **T17 vehicle HVAC compressor** (conditional); P side unchanged. Requires actual vehicle duty/auxiliary-energy evidence, not just charging snapshots.

**This document ranks using Priority B**, while recording Priority A as the necessary sensitivity alternative. Neither portfolio qualifies automatic equipment admission.

### Tests required before final 4+4

1. **G0 identity:** map the incompatible 20+20 and 19+21 source lists without treating thermal checks/functions and hardware as equivalent IDs; identify nested subassemblies.
2. **G1 case:** select compatible nameplate, oil/dry technology, feeder, EVSE type, vehicle/battery/BMS, cooling, and documented control authority.
3. **G2 mechanism:** independently qualify actual device physics and thermal operating/derating rules, with appropriate primary studies/standards.
4. **G3 interface/services:** time-align actual AC input \(P_{\mathrm{AC}}, Q_{\mathrm{AC}}, I,V\), actual transformer loading and relevant temperatures, DC power, battery energy/SOC, actual trip-energy demand and deadlines where chosen.
5. **G4 evidence/model:** inspect precise source equations, units, initial/boundary conditions, manufacturer rules, identifiability and held-out measurement plan.
6. **G5 independent-model necessity:** test each candidate with a physically consistent aggregated/boundary alternative, preregistering temperature/event-time/electricity/energy-use/mobility QOI tolerances. **All tests NOT_RUN**.

Counterfactuals must use the canonical M0 (controlled independent link), M1 (qualified static/algebraic coupling) and M2 (**additional evidenced causal dynamic interface**), without inferring M2 from ordinary heat-storage ODEs. Recover event timings separately from causal propagation. A paper using a similar architecture is not installed equipment validation.

## 6. Output metrics: energy efficiency, resilience and sustainability

**Candidate energy/service quantities; boundaries must be fixed before numerical use:**

- \(E_{\mathrm{AC}}=\int_{\mathcal T} P_{\mathrm{AC,in}}(t)dt\) (kWh): measured grid-side EVSE input energy.
- \(E_{\mathrm{DC}}=\int_{\mathcal T} P_{\mathrm{DC,out}}(t)dt\) (kWh): DC energy delivered at *EVSE output*; separate from energy actually stored in battery.
- \(\eta_{\mathrm{EVSE}}=E_{\mathrm{DC}}/E_{\mathrm{AC}}\) (dimensionless) only with identical horizon, connection and consistent auxiliary power/control volume.
- \(E_{\mathrm{net,batt}}(t_{\mathrm{dep}})\) versus \(E_{\mathrm{req,trip}}\) (kWh): departure-energy readiness *proxy*, not completed trip.
- \(e_{\mathrm{mobility}}=E_{\mathrm{vehicle\,used}}/d\) (kWh/km), only with observed/reliably modeled trips \(d\); can include measured auxiliary energy and traction if available. No synthetic kilometrage counted as field travel.
- \(E_{\mathrm{loss}}\) separated into transformer/feeder/charger/auxiliaries by no-overlap control volumes; cooling input electricity may increase losses even while protecting service.
- Critical threshold crossing, actual control action, service shortfall onset, recovery and attributable propagation time distinguished; censor events not triggered.
- Electricity-service demand/delivery and vehicle service through time; priority to maintaining/recovering requirements, not maximizing delivered kWh without purpose.

**Canonical sustainability Pathway 1:** compare reference and heat-only under identical service boundary and horizon for environmental (kWh losses, credible emissions factor), economic (documented cost), social (service continuity/access) indicators.  
**Pathway 2:** rerun Improve/Adapt/Restore under same heat and compare service AND increased cooling/energy/cost/material burden. Improvement in resilience does **not** imply improvement in energy efficiency or sustainability.

**SDG interpretation:** local indicators can be *relevant* to [SDG 7 targets 7.1/7.3](https://sdgs.un.org/goals/goal7), [9 targets 9.1/9.4](https://sdgs.un.org/goals/goal9), [11 target 11.2](https://sdgs.un.org/goals/goal11), potentially climate actions in [13](https://sdgs.un.org/goals/goal13) only with justified causality. A local kWh/km efficiency, AC/DC conversion rate, ready departure or transformer service duration is **NOT** automatically one of the UN official SDG indicators (7.3.1 is energy intensity per GDP; 9.4.1 emissions per unit value added; 11.2.1 public-transit access).

## 7. Primary and official sources (boundary controlled)

- Hilshey, A. D., Hines, P. D. H., Rezaei, P., & Dowds, J. R. (2013). [*Estimating the impact of electric vehicle smart charging on distribution transformer aging*](https://doi.org/10.1109/TSG.2012.2217385). **Simulation** of EV load→transformer thermal behavior; not actual transformer thermal trip.
- Pan, C., et al. (2025). [*Distribution network planning considering active response of EVs and DTR of cables and transformers*](https://doi.org/10.1049/hve2.70024). **Numerical/optimization** dynamic ratings and EV responses; results do not establish an installed device.
- Li, Y., et al. (2024). [*Thermofluidic investigations of oil natural transformer: Closed-loop modelling and experimental validation*](https://doi.org/10.1049/hve2.12345). **110-kV** temperature-rise experiments; not small transformer parameter transfer.
- Krama, A., Kamal, N., Sezer, N., & Bayhan, S. (2026). [*Impact of extreme climatic conditions on fast EV charger performance*](https://doi.org/10.1016/j.ecmx.2026.101960). **Field** charger temperatures, efficiency, DC output and sessions; raw data available on request.
- Gao, et al. (2021). [*Implementation and evaluation of a practical electrochemical-thermal model ... EV battery management system*](https://doi.org/10.1016/j.energy.2020.119688). **Model and road tests**, battery-specific.
- Parker, N. C., Kuby, M., Liu, J., & Stechel, E. B. (2025). [*Extreme heat effects on electric vehicle energy consumption and driving range*](https://doi.org/10.1016/j.apenergy.2024.125051). **345,622 EV trips**, auxiliary/propulsion/total energy analysis; cannot attribute whole effect to one compressor.
- Li, Y., et al. (2025). [*Thermal management optimization for high power EV charging connectors*](https://doi.org/10.1016/j.applthermaleng.2025.127680). **Numerical** connector heat pipe optimization; not proof of field restriction.
- Zhang, et al. (2023). [*Study on temperature rise characteristics of DC charging cable for electric vehicles*](https://doi.org/10.1080/10407782.2023.2285374). **Experimental comparison** of a cable thermal circuit, device-specific transfer OPEN.
- ABB (2010). [*RET615 ANSI Application Manual*](https://library.e.abb.com/public/e5e9f20ae5454e14a5572a13ec67e88a/RET615ANSI_appl_201230_ENb.pdf). 49T not breaker trip by default; config-specific.
- Ball, S. J., & Fisher, S. E. (2008). [*Next Generation Nuclear Plant PIRT: Main Report*](https://www.nrc.gov/regulations-legislation/nureg-series-publications/publications-prepared-by-nrc-contractors/next-generation-nuclear-plant-phenomena-identification-and-ranking-tables-pirts-nuregcr-6944/v1). Method precedent only, not validation of this ranking.

**Bottom line:** All 40 screened and given rank positions; provisional Priority B top four per system identified; high heat release alone does not drive selection. No G0 reconciliation across registries, selected-device admission, calibrated joint thermal law, numerical ablation, or independently validated sustainable/SDG benefit exists. Frozen GO/SOs and V5/V3 remain unchanged; proposed V6 provisional.
