# Eight Selected Components — Physics, State–Time and Directional Interface Research Dossier V1

**Prepared:** 2026-10-10. **Status:** DEEP LITERATURE-GROUNDED SCIENTIFIC WORKING DOSSIER — NOT EXPERIMENTALLY VALIDATED EQUIPMENT MODEL.  
**Selection authority:** [Approved exact eight](SELECTED_EIGHT_COMPONENTS_WORKING_RESEARCH_BASELINE_V1.md). **Do not change names, order, or the P1–P4/T1–T4 presentation identifiers.** These identifiers are different from the legacy 20+20 screening IDs and the independent 19+21 historical reconstruction.  
**Higher authorities:** [Frozen GO/SO1–SO3](../CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md), [system/interface working architecture](WORKING_SOS_COMPONENT_FUNCTION_INTERFACE_MATRIX_V1.md), [canonical state/time](../CANONICAL_STATE_TIME_DEFINITIONS_V1.md), [two-pathway sustainability](../CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md). This document does not revise canonical conceptual V5 or mathematical V3.

## 1. Exactly the approved component roster

**Power System (P):**
1. **P1 — Distribution Transformer**
2. **P2 — Distribution Feeder**
3. **P3 — Transformer Protection/Load-Management Hardware**
4. **P4 — Transformer Cooling Equipment**

**Electrified Transportation System (T):**
1. **T1 — DC EV Charger**
2. **T2 — Vehicle Battery Pack**
3. **T3 — EVSE Cooling Equipment**
4. **T4 — Vehicle HVAC Equipment**

**Terminology:** Eight equipment research subjects do not mean eight cross-system interfaces, eight independent infrastructure systems, or eight ODE states. Equipment *membership* is not the same as an interface *relationship*. The physical EVSE and its cooling belong to Electrified Transportation; a shared ambient heat event belongs to neither physical infrastructure system. Vehicle propulsion, cable/connector, BMS and charger communications remain in the **full system boundary** but can be reduced to evidenced algebraic quantities/service requirements; they do not disappear from physical reality merely because not chosen among the eight.

## 2. What these components should explain

The thesis concerns how extreme heat acts on internal Power and Electrified Transportation thermal states, what real state-conditioned capabilities/actions arise, and what *qualified* directional effects appear in electricity and mobility services **as functions of time**. Measured energy losses/efficiency, mobility energy use, costs and emissions are bounded downstream engineering/sustainability quantities; they do not replace frozen GO/SO1–SO3.

| Outcome | Precisely defined local QOI and unit | Critical boundary |
|---|---|---|
| Y1 | EVSE energy efficiency η_EVSE = E_DC,EVSE_out / E_AC,EVSE_in, dimensionless, report as % | Same complete session/time range; AC input includes EVSE cooling/auxiliaries when behind meter |
| Y2 | Non-overlapping transformer, feeder and EVSE electrical loss energies, each kWh | Distinct control volumes and electrical port meters; non-EV demand separated |
| Y3 | Battery energy consumed during real vehicle trip per measured trip distance, kWh/km | Measured/defensible trip energy, distance and thermal/operational conditions; not solely charging output |
| Y4 | Vehicles meeting required available battery energy at *declared* departure time, count or % | Service-readiness proxy, not observed completed trips or UN transport-access indicator |
| Y5 | Electricity/mobility service trajectories, deficits (kW/kWh or readiness %), actual action/transition onset, qualified cross-sector delay, recovery time when modeled | State, threshold, operating action and achieved service are different constructs |
| Y6 | Energy (kWh), evidence-backed GHG (kg CO2e), cost (currency/period), measured access/served quantity | Two scenarios for direct thermal effect and engineering-response effect; comparable functional unit and boundary |

## 3. Four distinct types of contribution

| Role | Included components | Why they matter |
|---|---|---|
| **Electricity interface pathway and thermal receiver** | P1, P2, T1 | Transfers AC power; electrical loading changes P thermal losses; charger thermal operating response can change grid-side demand |
| **Conditional implemented restriction** | P3 | May implement *actual* Power-temperature-conditioned permissible input or switching that affects EVSE operation; neither insulation ageing nor an alarm proves this |
| **Heat-transfer mechanisms inside a system** | P4, T3 | Determine physical cooling and thermal time-history; can affect electrical auxiliary load and cooldown/recovery but are **not** cross-sector interfaces themselves |
| **Energy storage / service-demand mechanisms** | T2, T4 | Converts charged energy into departure readiness and possible trip energy; HVAC heat-dependent use may affect future charging requests, not instantaneous direct transfer from a vehicle compressor to the grid |

### Actual interfaces under investigation, not eight assumed interface arrows

- **I1, ordinary electricity supply P → T:** transformer/feeder output to **T1's measured grid-side AC port**. This is an electrical transfer, **not yet a thermal interdependency**.
- **I2, candidate thermal-conditioned T → P:** T1/T3 temperature and operating/cooling response → **measured grid-side AC real/reactive demand and current** → P2/P1 loading and losses → P1 thermal trajectory. This is demand influence, **not V2G/reverse electric energy flow**.
- **I3, candidate thermal-conditioned P → T:** P1 thermal condition → **P3's real manufacturer/operator implemented protective or power-permission action** → actual available AC input to T1 → charged energy and T2 readiness. An advisory loading guide alone does not establish the action.
- **I4, within T:** T1–T3 loss/thermal rejection and actual EVSE derating.
- **I5, within T:** T1 → transferred DC energy → T2 SOC/readiness; cable/inlet/BMS losses and constraints remain real and are represented at justified reduced fidelity.
- **I6, demand-mediated (candidate, later times):** T4 hotter-weather vehicle auxiliary energy → T2 trip depletion/next required energy → charging schedule/AC demand at T1 → P loading/thermal trajectory; this is **not** a direct T4→P thermal interface and requires travel-to-charging causal evidence and control of common heat forcing.
- **H(t) environmental forcing:** ambient air/solar/wind/soil thermal forcing as appropriate. Common hot weather affecting both systems is not cross-system causation.

## 4. Eight equipment contracts: reality, physics, mathematics, evidence, service

The model statements below are **first-law/structural candidate relationships**, not claimed exact source-paper equations or admitted device constitutive coefficients. Any equipment-specific capacity, setpoint, time constant, parameter or triggering law is deliberately OPEN.

### P1 — Distribution Transformer

**Role:** physical electrical transformation; source/receiver of feeder loading and thermal condition; potential Power-side thermal capability. **Inputs:** source AC voltage, phase currents/real-reactive load, ambient heat, P4 cooling mode. **Processes:** core/load electrical losses; winding/oil heat generation; thermal inertia and rejection; insulation ageing as an optional slow consequence, not equivalent to outage.

**Minimal physical template** (when lumped physics and oil technology are justified):  
$C_w \dot T_w=P_{w,loss}(I,T_w)-\dot Q_{w\to o}$;  
$C_o \dot T_o=P_{core,loss}+\dot Q_{w\to o}-\dot Q_{P4\to amb}$.  
$C$ [J/K]; $P_{loss}$ and heat rates [W]; temperature differences [K]. Top-oil/hot-spot approximations should follow applicable IEEE/IEC *equipment-specific* equations, not these templates copied as manufacturer's law. **Do not add P4 cooling heat rejection twice.**

**Outputs:** transformer load/loss kWh, thermal state, *candidate* permissible load and first meaningful threshold time, supplied feeder power. **Observations:** rated kVA, cooling class, core/copper losses, three-phase currents/voltages/P/Q, ambient/top-oil/hot-spot or reliable hotspot estimate, timestamp, relevant operational restrictions. **Sources:** Hilshey et al. 2013 (IEEE-based simulated 25 kVA, not field proof of installed curtailment); IEEE C57.91-2025 guide (mineral-oil applicability). **Status:** class physical mechanism supported; selected thermal law/actual P3 action OPEN.

### P2 — Distribution Feeder

**Role:** physical path transformer → EVSE; network voltage/current condition, resistive losses and (if binding) conductor heat and ampacity. **Inputs:** transformer secondary voltage, phase currents, topology, temperature-dependent resistance, ambient air/wind/solar or soil as **appropriate for exact technology**.

**Minimal representation:** AC network Kirchhoff/impedance relationships; $P_{feeder,loss}(t)=\sum_\phi I_\phi^2(t) R_\phi(T)$ for correct conductor/phase segment definitions. Extra feeder thermal state **only when** transient conductor temperature changes allowed current, losses, SO3 critical time or service beyond reduced constraints. For a lumped segment under properly defined assumptions: $C_f\dot T_f=P_{feeder,loss}+\dot Q_{environment,in}-\dot Q_{environment,out}$; this is **not interchangeable** between overhead lines and buried cables.

**Outputs:** actual EVSE AC voltage/current and power availability, feeder loss kWh, conditional thermal current limit. **Data:** feeder schematic, actual overhead/buried technology, conductor material/length/section, impedance, current/voltage/real/reactive power, thermal surroundings and rating. **Literature:** Pan et al. 2025 dynamic thermal rating of cables and transformers for EV charging planning; method is scenario-specific. **Status:** network transfer/loss physics strong; extra feeder thermal ODE conditional.

### P3 — Transformer Protection/Load-Management Hardware

**Role:** *real physical controller/protection and actuation chain*, not an abstract mathematical governance rule; receives estimated/measured thermal/electrical conditions and may create permissible AC-load commands or protective switching. **Inputs:** actual sensed transformer condition, load, settings, timers, current hardware mode, operator commands. **Outputs:** documented permissible EVSE AC power, actuation/setpoint/status/event time where installed.

**Candidate mathematical class:** finite-state or hybrid logical rule $m_P(t^+)=\mathcal R_{\mathrm{installed}}(T_{sensed},I,\mathrm{timers},m_P,u_P)$ with **only source-proven** switching/curtailment logic. Do **not** prescribe arbitrary temperature threshold/hysteresis or classify a hypothetical temperature advisory as physical breaker tripping. **Observations:** relay/controller model and wiring, transformer sensor-to-controller link, enabled protection setting, permission/dispatch channel to charger, event and command log.

**Evidence:** ABB RET615 application manual explicitly notes default 49T transformer thermal function not configured to trip a breaker in a described configuration; Hilshey simulated *smart charging controller*, not field installed relay. **Status:** strongest unresolved **P→T thermal interface control gate**. P3 can be in the selected research roster but cannot be declared an active state-conditioned supply restriction until the actual rule is supported.

### P4 — Transformer Cooling Equipment

**Role:** heat rejection inside Power, perhaps passive tank/radiator, natural-oil circulation or forced-air fan/pump **only if the selected unit actually fits it**. **Inputs:** oil/winding thermal condition, ambient air, geometry, heat-transfer properties, fan/pump actuation, available auxiliary power. **Outputs:** heat rejection [W] and, where powered, cooling auxiliary draw [W], actual cooling mode.

**Candidate representation:** $\dot Q_{P4}=\mathcal H_P(T_o,T_a,\text{geometry},u_{\mathrm{cool,P}})$; no standalone ODE unless coolant/fan/internals possess necessary identifiable state and meaningful thermal memory. Coupling into P1 thermal equation is **one sink term**. Do not count discharged heat as additional electricity loss: any fan/pump electrical demand is counted **at its own meter/control-volume boundary**.

**Evidence:** Li et al. 2024 experimentally tested a 110-kV ONAF transformer cooling model using temperature-rise observations; 110-kV geometry and coefficients **do not transfer** to a smaller distribution unit. IEEE oil-transformer loading guide discusses different cooling modes. **Status:** thermal-process rationale strong, independent hardware dynamics/site transfer OPEN.

### T1 — DC EV Charger

**Role:** the Electrified Transportation-side receiving equipment at the AC port; AC–DC conversion, converter losses, thermal storage/rejection, controlled/offered DC power, heat-dependent derating. **Inputs:** three-phase AC $P,Q,V,I$, charging request, ambient, rectifier/semiconductor temperature, T3 cooling mode, T2 battery/BMS accepted power and P3 actual permission. **Outputs:** **measured AC demand**, DC available/offered power, delivered DC energy and thermal state, charger loss/efficiency. A charger **offered** 40 kW is not proof a battery **accepted** 40 kW.

**Port energy balance:** $P_{AC,EVSE}=P_{DC,EVSE}+P_{conv,loss}+P_{EVSE,aux}$ at correctly defined time-averaged or steady-state control-volume boundaries. If cabinet thermal energy storage is appreciable, instantaneous *power* balance must additionally account for electromagnetic/internal stored-energy change, whereas long-session measured energy balance uses integrated residuals. **T3 fan/cooling input is part of EVSE auxiliary AC consumption if behind charger meter.** Converter heat $P_{conv,loss}$ supplies internal thermal generation; **do not add rejected cooling heat to converter loss**.

**Candidate thermal structure:** $C_e\dot T_e=P_{conv,heat}-\dot Q_{T3}$ with other exchange/sources included as required; $P_{DC,offered}\le C_E(T_e,T_a,u_e)$ only from a real device rule. **Data:** actual model, rated power, instantaneous synchronized AC P/Q, DC offered/delivered P, rectifier sensor, cooling status/auxiliary P, per-session energy and battery requests.

**Evidence:** Krama et al. 2026 field tested a commercial 50 kW air-cooled charger in Qatar and observed thermal derating, energy-efficiency change, rectifier temperature and charging-duration differences; cannot transfer a paper-specific threshold, coefficient or percent saving to our device. **Status:** strongest T thermal equipment-level evidence precedent; selected converter law and P-facing AC response OPEN.

### T2 — Vehicle Battery Pack

**Role:** store electrochemical energy accepted from charging and power subsequent vehicle service. **Inputs:** actual **battery terminal** power/current, cell/pack temperature where measured, SOC and BMS charge acceptance, charging time and declared departure/mission requirement. **Outputs:** energy/SOC trajectory, actual accepted power, departure readiness indicator; thermal acceptance **only** if relevant. **The DC energy measured at EVSE output can exceed energy accepted at the pack** due to physical DC cable, contact and onboard charging path losses; those paths are retained as sourced reduced terms even though not among selected eight.

**Minimal representation:** $\dot{SOC}(t)=I_{cell,equiv}(t)/Q_{\mathrm{nom}}$ (sign-convention and charge efficiency must be declared); alternatively a **calibrated usable energy state** $\dot E_{useful}=\eta_{store}(SOC,T_B,I) P_{B,terminal}$ during charging. These are alternative modeling conventions, NOT two independent ways to count received kWh. **Do not assert terminal power is identical to chemical stored energy.** Detailed battery-thermal energy balance (Bernardi et al. 1985) and conditional BMS $P_{B,accept}\le C_B(T_B,SOC)$ are added only if they change the studied heat-conditioned service.

**Data:** battery chemistry/capacity, signed DC terminal I,V, actual SOC estimates/BMS current limit, temperature, initial state, charging profile, $t_{departure}$ and trip energy requirement. **Status:** essential energy/service bridge, battery thermal differential state optional; **readiness is a proxy, not measured travel completion**.

### T3 — EVSE Cooling Equipment

**Role:** internal Electrified Transportation heat rejection and auxiliary AC demand; its effectiveness alters converter temperature history, thermal capability and charger recovery. **Inputs:** converter/cabinet and ambient temperatures, fan speed/duty or coolant flow and air/thermal geometry. **Outputs:** rejected thermal power [W], electrical fan/pump/cooling power [W], if fitted actual cooling mode; impacts T1 energy balance and converter derating.

**Candidate model:** $\dot Q_{T3}=\mathcal H_E(T_e,T_a,u_{\mathrm{cool,E}})$ and $P_{cool,E}=f_{\mathrm{aux}}(u_{\mathrm{cool,E}},T_a)$ where equipment supports those functions. Extra cooling state requires independent physical memory and observations. **Ensure conservation:** T3 rejects heat generated in T1; it is not a second independent conversion loss. Powered cooling contributes to T1 measured AC input.

**Evidence:** Krama et al. 2026 field study shows an **air-cooled whole EVSE** thermal response, not independently identified cooling-device dynamics; Rahman et al. 2024 is a general converter thermal-management review, not selected device validation. **Status:** selected as literature-supported mechanism, independent detailed model conditional.

### T4 — Vehicle HVAC Equipment

**Role:** **mobility-service energy demand** during extreme heat; compressor/HVAC draws power from the battery while providing vehicle cooling, and may modify trip energy and future charging requirements. **Inputs:** heat exposure, cabin thermal conditions, setpoint, passenger/route/driving time, measured compressor/auxiliary electric load where available. **Outputs:** HVAC energy per trip, trip energy/distance, post-trip SOC, charging demand needed by next deadline. **Charging-station AC power is not instantaneously equal to compressor consumption during a road trip.**

**Candidate representation:** $E_{HVAC,trip}=\int_{trip} P_{HVAC}(T_a,T_{cabin},u_{HVAC},t)\,dt$; $E_{vehicle,trip}=E_{traction}+E_{HVAC}+E_{other}$ at consistent vehicle battery terminals. A cabin temperature ODE is OPTIONAL; a sourced empirical load map can suffice. Coupling to P requires a **later charging schedule and energy requirement**; absent those, T4 is a downstream service-demand component only.

**Evidence:** Parker et al. 2025 analyzed 345,622 trips from 300 BEVs in Phoenix and quantified heat-associated total/auxiliary energy effects, **not the isolated compressor performance of our selected vehicle**. **Status:** strong *vehicle demand-level* reason to study; device-level HVAC identification, trip data and next-charge interface closure OPEN.

## 5. Energy and thermal accounting: conservation must be checked end-to-end

For an EVSE circuit served by one transformer and feeder, define consistent signed and metered AC flow control volumes. For a correctly isolated branch:

1. $P_{transformer,out}=P_{feeder,loss}+P_{AC,EVSE}+P_{other,feeder\ loads}$, adjusted for storage, measurement locations, line shunt effects and reactive-power model details as required. The AC input at the transformer primary also includes **transformer loss**. Do not assume total transformer current is solely charging demand.
2. $P_{AC,EVSE}=P_{DC,EVSE}+P_{conv,loss}+P_{cool,E}+P_{other,EVSE,aux}$ for matched charger boundaries. At energy-level integrate each source term over exactly the same period.
3. $P_{DC,EVSE}=P_{battery,terminal}+P_{cable/inlet,loss}+P_{other,vehicle\ charge\ input}$ after reconciling any vehicle-side auxiliary/charging consumption.
4. Battery terminal electrical energy and chemical/usable energy are **not the same**; keep battery round-trip/loss definition consistent.
5. $E_{vehicle,trip}=E_{traction}+E_{HVAC}+E_{other}$ at the stated battery-energy basis and trip window. The later EVSE AC energy required to replenish the trip includes charging and distribution losses; it is **not** automatically equal to $E_{vehicle,trip}$.
6. Cooling energy accounting: rejected thermal power $\dot Q_{cool}$ and fan electrical power $P_{cool}$ have **different meanings and cannot be summed** as if both are electrical losses.
7. The three-phase feeder has real $P$, reactive $Q$, apparent $S$, actual measured $V,I$; ampacity and transformer heating depend on **current**, not real power alone. If load harmonics matter, use the equipment-applicable heating relation and total RMS/harmonic data; no unjustified simplified 3I²R under harmonics.

**Energy residual:** For each instrumented control volume define $\epsilon_E=E_{in}-E_{out}-E_{dissipated}-\Delta U$; unmeasured subsidiary paths and uncertainty must be included, not forced to zero by calibration.

## 6. Minimum-sufficient candidate state–time system

A **model-family proposal** only, not frozen equations:

$\dot x_P=f_P(x_P,z,H,u_P;\theta_P)$  
$\dot x_T=f_T(x_T,z,H,u_T;\theta_T)$  
$0=g(x_P,x_T,z,H,u)$  
$Q_P(t),Q_T(t)=h(x_P,x_T,z,u,requirements)$

- Candidates for **thermal states**, not all mandatory: transformer top-oil or winding/estimated hot-spot; EVSE rectifier/cabinet; *maybe* feeder conductor and battery or coolant when active evidence necessitates.
- **Battery SOC/usable energy** is an energy state, not a thermal state. Relay controller modes may be discrete states. HVAC trip demand is a load mapping unless cabin temperature memory is essential.
- $z$ contains **algebraic** AC interface variables ($P,Q,V,I$), permissible operating constraints, charge-power allocation; no invented interdependency differential state.
- External extreme-heat forcing $H(t)$, non-EV load and actual charging/route schedules are separate exogenous inputs.
- **Timing:** qualified temperature/capability threshold time $\tau_C$ is distinct from controller actuation time, intersystem attributed receiver response delay $\delta_{ij}^{th}$, service shortfall onset, departure deadline and genuine service recovery.
- **M0:** controlled severed influence / independent-system counterfactual; **M1:** static/algebraic qualified coupling; **M2:** dynamic *physically causal, directional* thermal interdependency. Two separate thermal ODEs under same ambient heat do **not** constitute M2.

## 7. Literature-backed distinction: what is supported, and what remains a hypothesis

| Evidence source | Published scope and defensible support | Not proven for our project |
|---|---|---|
| Hilshey et al. 2013 | IEEE-based modeled EV load → transformer thermal/aging dynamics and *simulated* temperature-based smart charging | Selected breaker trip or P1→T1 thermal restriction in one actual depot |
| Pan et al. 2025 | Joint *modeling* of transformer/cable dynamic thermal ratings and EV demand in distribution planning | Our overhead/underground physical site/parameter ratings |
| Li et al. 2024 | Factory validated CFD/thermal of **110 kV** transformer oil/air cooling geometry | Our distribution P4 configuration or separate cooling ODE |
| ABB RET615 manual | Thermal protection function class, and example default thermal function **not set to breaker trip** | P3 actuation at our installation |
| Krama et al. 2026 | Qatar charger experiment: rectifier T, offered/delivered DC, derating, efficiency, charging-duration effects | Joint measured transformer response, our EVSE law and thresholds |
| Rahman et al. 2024 | Review of power-electronic thermal management/cooling principles | Our charger cooling hardware test |
| Bernardi et al. 1985 | First-principles battery system thermal balance | Any specific vehicle BMS thermal charge-acceptance curve |
| Parker et al. 2025 | Phoenix trip records show strong heat-associated total/auxiliary energy-use change | HVAC compressor-specific law or same-fleet later charging feedback |
| IEEE C57.91-2025 | Oil-immersed transformer thermal loading/cooling criteria and guidance | Automatic protective action or public access to all paid clauses |

## 8. Scientific research hypotheses — explicitly NOT results

- **H-P:** A source-qualified transformer thermal state and installed power-permission rule changes charging availability and service timing relative to heat-matched electrical-only M1.
- **H-T:** An admissible EVSE heat/cooling/derating relationship changes measured AC input $P,Q,I$ and hence P1 loss/state relative to heat-matched M1.
- **H-C:** Distinct modeling of P4 or T3 improves a named independently checked threshold time, charger efficiency or recovery quantity relative to a single combined heat-rejection law.
- **H-M:** Hot-weather HVAC auxiliary energy changes trip-level energy demand, and *if* schedules/route energy close the loop, downstream next-charge timing and eventual P load.
- **H-S:** A documented Improve/Adapt/Restore response can improve one declared service resilience quantity but may trade off with auxiliary electrical consumption, cost or emissions.

These are *investigation hypotheses*, not added canonical research objectives, frozen formal H1/H2/H3 or findings.

## 9. Objective and sustainability trace

SO1 = establish component physics and qualified I2/I3 mechanisms, with each direction documented independently.  
SO2 = minimum-sufficient conservation-based thermal/electrical model with identified states, constraints and uncertainty.  
SO3 = validated/predictive state–time transitions, attributable coupling delays and **actual service** consequences.  
Resilience = maintain/recover specified electricity and mobility service requirements; thermal equipment survival and EV readiness are not complete resilience evidence by themselves.  
Sustainability **Path 1:** reference versus extreme heat without response; **Path 2:** heat-only versus matched heat plus physically available Improve/Adapt/Restore intervention; parallel environmental/economic/social indicators without a fabricated aggregate score.  
SDG 7.3, 9.4, 11.2 and 13-related targets may be discussed as **target-level relevance** after measured local indicator attribution, not mislabeled as official UN metrics; source: https://unstats.un.org/sdgs/metadata/.

## 10. Bibliographic sources (the cited works and their actual role)

- Hilshey, Hines, Rezaei & Dowds (2013), *Estimating the Impact of Electric Vehicle Smart Charging on Distribution Transformer Aging*, IEEE Transactions on Smart Grid. https://doi.org/10.1109/TSG.2012.2217385
- Pan et al. (2025), *Distribution network planning considering active response of EVs and DTR of cables and transformers*, High Voltage. https://doi.org/10.1049/hve2.70024
- Li et al. (2024), *Thermofluidic investigations of oil natural transformer: Closed-loop modelling and experimental validation*, High Voltage. https://doi.org/10.1049/hve2.12345
- ABB, RET615 ANSI application manual (manufacturer, **not** experimental research): https://library.e.abb.com/public/e5e9f20ae5454e14a5572a13ec67e88a/RET615ANSI_appl_201230_ENb.pdf
- Krama, Kamal, Sezer & Bayhan (2026), *Impact of extreme climatic conditions on fast EV charger performance: field experimental insights from Qatar*, Energy Conversion and Management: X. https://doi.org/10.1016/j.ecmx.2026.101960
- Rahman et al. (2024), *Emerging Trends and Challenges in Thermal Management of Power Electronic Converters: A State of the Art Review*, IEEE Access. https://doi.org/10.1109/ACCESS.2024.3385429
- Bernardi, Pawlikowski & Newman (1985), *A General Energy Balance for Battery Systems*, Journal of the Electrochemical Society. https://doi.org/10.1149/1.2113792
- Parker, Kuby, Liu & Stechel (2025), *Extreme heat effects on electric vehicle energy consumption and driving range*, Applied Energy. https://doi.org/10.1016/j.apenergy.2024.125051
- IEEE Std C57.91-2025, Guide for Loading Mineral-Oil-Immersed Transformers and Step-Voltage Regulators. https://standards.ieee.org/ieee/C57.91/7163/
- UN official SDG target/indicator metadata. https://unstats.un.org/sdgs/metadata/

**Literature provenance:** research papers were inspected at publisher/author publication text or abstract level; not all equipment-standard normative clauses or full raw datasets have been accessed. No paper is a full validation of **all eight plus both cross-sector thermal mechanisms**. 
