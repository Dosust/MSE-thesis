# Working SoS Component–Function–Mechanism–State–Interface Architecture V1

**Date:** 2026-10-09  
**Status:** PROPOSED WORKING RESEARCH ARCHITECTURE — NOT A FROZEN EQUIPMENT MODEL, CAUSAL CERTIFICATION, OR NOVELTY CLAIM  
**Thesis:** Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience  
**Research focus:** thermal interdependencies between the Power System (P) and Electrified Transportation System (T_e) under extreme heat, evolving through physical state and time.

## 0. Governing authorities and conflict resolution

Controlling **active** authorities:
- \`project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md\`
- \`project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md\`
- \`project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md\`
- \`project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md\`
- \`project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md\`
- \`project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md\`
- \`project/module_01_transformer_thermal_state_physics/MODULE_01_MODEL_ADMISSION_LEDGER_V1.md\`

Methodological interpretive precedents (older broad stage contracts do **not** override narrowed thermal-only scope/objectives):
- \`project/CANONICAL_SOS_INFORMATION_ARCHITECTURE_AMENDMENT_V1_2.md\`: membership ≠ causal link; physical system ≠ model ≠ information/provenance system; physical coupling ≠ API/data coupling.
- \`project/stage3/STAGE3_DESIGN_PROTOCOL_FREEZE_V2.md\`: **M0 independent P+T; M1 static/algebraic P–T coupling; M2 dynamic causal P–T coupling**; not tested, readiness required. No new DM0/DM1/DM2 definitions are frozen.
- \`project/stage3/STAGE3_DIRECTIONAL_INTERFACE_STATE_AMENDMENT_V2_2.md\`: mechanism-specific independent interface memory only when physics requires; no invented generic common interface state.

**Supersession rule:** legacy seven-objective/RQ/H1 references remain historical; they do not expand the active three-objective thermal-only contract. Frozen historical M0/M1/M2 *meanings* are respected, but any H1 experiment is not claimed executable for the selected heat/depot case.

## 1. Hierarchy and function

**SoS service mission:** evaluate the ability to maintain/recover *declared* electricity and mobility services under extreme heat.

| Level | P | T_e | Distinction |
|---|---|---|---|
| System | Power System: provide admissible electric supply | Electrified Transportation System: deliver electrically propelled road mobility | Separate missions, assets, governance and service requirements |
| Subsystem | supply boundary; transformation and distribution; operation/protection; observation | EVSE/physical transfer; onboard storage; propulsion/auxiliary circuits; charging communication/control | Major internal functional groupings |
| Component | supply boundary, transformer, feeder, protective device, sensor | charger converter, cable/connector, RESS, cooling device, inverter/motor, cabin HVAC, charge controller | Specific physical or realized control elements |
| Interface | AC electrical power supply and charging demand | AC receiving boundary, charging request, operational limits | Interface relation—not a third autonomous infrastructure system |
| Shared exposure | extreme ambient thermal forcing | extreme ambient thermal forcing | Common-cause heating alone is NOT cross-system thermal dependency |

**Canonical T_e full scope is not reduced:** road vehicle; rechargeable energy storage; electric propulsion and auxiliaries; vehicle power-supply circuit; EVSE; physical charging connection; required communications/control; bidirectional transfer only where supported. Fleet schedules are **service/operating requirements**, not new physical components. Proposed depot/charging facility is an *application subset only*.

## 2. Per-component contract

A component record shall contain:
\`ID, system/subsystem, function, source input (quantity+unit), physical transformation/constraint, output (quantity+unit+receiver), required internal state (candidate vs admitted), thermal forcing, interface direction, evidence/provenance, model fidelity, validation route\`.

The four minimal functional fields are **input, transformation, output, state/feedback**. System mission, observable output and service are distinct objects.

### 2A. Power: candidate component–function–mechanism matrix

| ID; subsystem/component | Function and input | Transformation/mechanism | Output | Heat/state/evidence decision | Active role |
|---|---|---|---|---|---|
| P1; upstream supply **boundary** | Supply voltage [V], available real/reactive power [W/var] | Network boundary delivery, not necessarily modeled upstream dynamics | available upstream supply | External supply capability; temperature-dependent upstream derating NOT assumed | Boundary |
| P2; transformer | Receive upstream electrical voltage/current, charge-related AC demand, ambient temperature | Electromagnetic transformation; electrical/core/load losses → internal heat; heat storage and rejection | secondary electrical power, thermal condition | **Core thermal physics**; candidate top-oil/hot-spot are NOT frozen. Exact reduced law, cooling mode, loss and limit OPEN | Candidate dynamic thermal |
| P3; distribution feeder | Carry transformer-side voltage/current | Impedance, conduction and electrical losses | EVSE AC input voltage and available power | Conductor temperature dynamics only if material; power-flow constraint may be algebraic | Reduced electric constraint |
| P4; operating/protection function, realized in devices | Measurements, setpoints, ratings and commands | Applicable actual thermal/electrical limit or protection rule | available capacity, control action or trip | **State→allowable power gate OPEN**; not automatic from hot-spot | Conditional rule |
| P5; measurement/estimation function | Transformer temperatures, current, voltage, measured electric power | Sensing and data treatment | observed readings [units, timestamps, uncertainty] | Reading is observation, not physical truth; model/data alignment required | Validation/information |

### 2B. Electrified transportation: candidate component–function–mechanism matrix

| ID; subsystem/component | Function and input | Transformation/mechanism | Output | Heat/state/evidence decision | Active role |
|---|---|---|---|---|---|
| T1; EVSE/DC fast charger | Receive AC power [W], charge request, ambient temperature, operating commands | Power electronics AC→DC with losses, cooling and charge control | available and delivered DC power [W] | **Core thermal candidate**; measured derating established in some devices, transferable EVSE constitutive law and needed EVSE state OPEN | Candidate dynamic/algebraic |
| T2; cable/connector | Carry DC voltage/current from EVSE | Conductor/contact loss and temperature-dependent current constraint where supported | DC vehicle inlet power [W] | Connector thermal state only if output/significance requires | Conditional constraint |
| T3; RESS/battery | Receive terminal charge power, supply vehicle operating power | Electrochemical storage/charge acceptance and loss | stored energy [J/kWh], terminal power [W], SOC | SOC is **energy state, NOT thermal state**; battery temperature model only if required | Energy balance |
| T4; battery thermal management | Receive electric auxiliary power, heat source/sink, thermal control | Heat exchange/cooling and parasitic energy consumption | allowable battery thermal condition / auxiliary load | Cooling operation or constraint only with sourced parameters | Reduced input/constraint |
| T5; traction inverter/motor | Receive battery DC energy/power, torque/speed demand | Electrical→mechanical conversion with losses | traction work/power and demand | May determine route energy; independent thermal ODE usually excluded absent material relevance | Demand model |
| T6; HVAC/auxiliaries | Receive battery electricity and ambient/cabin loads | Cabin cooling and auxiliary conversion | comfort/auxiliary energy services and electric energy demand | Heat-dependent energy use may matter; justified load model only | Demand model |
| T7; charging communication/control function | Receive SOC, requests, availability, measured/estimated limits and schedule | Charging allocations and realized command logic | EVSE power setpoint and permission | Algorithm NOT itself a separate physical infrastructure system; controls only if implementable | Operating function |
| T8; fleet mobility **service function, not physical component** | Vehicle state/availability, trips, deadlines, required energy | Trip/departure assignment and declared readiness criteria | on-time ready departures, unmet service; completed trips where observed | Readiness proxy ≠ demonstrated completed mobility; service criteria case-dependent | Service/QOI |

## 3. Directional interface register

| Interface | System direction | Source variable → receiver variable | Type | Gate |
|---|---|---|---|---|
| I1 electric supply | P→T_e | distribution-side AC supply [W,V] → EVSE AC input | ordinary electric transfer, not itself directional thermal propagation | Electrical boundary and topology |
| I2 charging-load response | T_e→P | EVSE **grid-side AC demand** [W, var] → transformer load/loss → thermal change | plausible load-to-thermal mechanism; case law not yet frozen | Time-aligned AC/DC efficiency and electrical loss/heat law |
| I3 P thermal operating restriction | P→T_e | physically admissible transformer condition → actual permissible AC power/control → EVSE input | **candidate thermal functional dependency** | Manufacturer/standard/utility policy/protection evidence; exact case OPEN |
| I4 charger thermal self-limitation | within T_e | device internal/ambient thermal state → EVSE converter DC limit and AC input response | **intra-system**, not a P→T_e mechanism | Charger device data and response law |
| I5 battery energy→mobility | within T_e | delivered charge energy / SOC → feasible departure | service mapping, not intersystem coupling | Service threshold, deadlines, vehicle operations |
| H common extreme heat | environment→P and environment→T_e | measured/sourced exposure [°C] → two independent heat-transfer processes | common forcing; **not** interdependency | Exposure source, spatial/timing boundaries |

**No reciprocal thermal-coupling claim until I2 and I3 independently qualify.** Real power direction from supply is normally P→T_e in a unidirectional DC charging application; drawing a double-headed *energy flow* arrow would imply unsupported V2G. I2 denotes **demand-induced loading response**, not reverse electrical energy flow.

## 4. Physical balance, model selection, types

Transformer *principle*, not equipment-specific adopted ODE:
\`\`\`math
\frac{dU_{th,P}}{dt}=\dot Q_{gen,P}-\dot Q_{rej,P}.
\`\`\`
Candidate constrained structure only **if** states and algebraic constraints are admitted:
\`\`\`math
\dot x_P=f_P(x_P,z,H,u_P;\theta_P),\quad
\dot x_{T_e}=f_{T_e}(x_{T_e},z,H,u_T;\theta_T),\quad
0=g(x_P,x_{T_e},z,H,u;\theta),\quad Q=h(x_P,x_{T_e},z,u).
\`\`\`

- \(H(t)\): external ambient heat forcing, not an internal state.
- \(x_P\): required Power states, potentially transformer thermal temperatures after admissibility check.
- \(x_{T_e}\): required thermal/operational/energy states, potentially EVSE state and battery SOC; SOC not temperature.
- \(z\): algebraic exchange/operating constraints unless **separate direction-specific physical memory** is demonstrated.
- \(Q_P,Q_{T_e}\): electricity and mobility *service outputs*, not states or equipment capabilities.
- AC grid input, charger DC output, battery terminal charge and loss heat must have separate power-accounting boundaries. Do not apply efficiency twice.
- Thermal limit, state, permissible electrical capability, protection actuation and delivered service are **not equivalent**.
- Thermal transition time ≠ source-to-receiver attributable delay ≠ service onset ≠ recovery duration.

## 5. Existing frozen comparator names — **no label drift**

The controlled historical meanings are exactly:
- **M0:** independent P+T; an intervention-disabled/severed-link *controlled counterfactual*, not a depiction of the actually connected depot if AC supply exists.
- **M1:** static/algebraic coupling; represent qualified instantaneous electric/operating relationships without new unverified dynamic interface memory.
- **M2:** dynamic causal coupling; only when case-specific, direction-specific dynamic mechanisms satisfy readiness and VVUQ prerequisites.

Terms **DM0/DM1/DM2 are not separately defined or frozen**, since they risk collision with canonical M0/M1/M2. **Do not label ordinary subsystem thermal dynamics alone as sufficient for M2**: M2's dynamic causal interdependency must be distinctly evidenced.

For a nested comparison control forcing, schedules, initial states, boundary and service criteria. An M1→M2 curve difference does **not** demonstrate superior prediction, directionality or causal identification without suitable independent evidence. For this thermal-only demonstrator, older H1-specific program case outcomes cannot be transferred as validated results.

## 6. Evidence gates

| Gate | Evidence necessary | Current status |
|---|---|---|
| G-A physical topology and fleet scenario | specific transformer technology/cooling, feeder-to-depot topology, EVSE rating/cooling, road-vehicle/fleet service | OPEN |
| G-B thermal mechanism | relevant energy/heat balance and device-specific temperature relations | COMPONENT PHYSICS CONCEPTS SUPPORTED; final reduced equations OPEN |
| G-C P→T_e law | standard/equipment/utility thermal operating policy/relay logic resulting in allowable EVSE power | **OPEN / BLOCKING BIDIRECTIONAL CLAIM** |
| G-D T_e→P law | charge facility AC demand, conversion accounting, loading losses and time scales | CANDIDATE / CASE OPEN |
| G-E states/parameters | minimum-sufficient physics, identifiability, evidence provenance, sensor/observation plan | OPEN |
| G-F output/service | electric supply demand and fleet route/departure energy requirement with thresholds | OPEN |
| G-G time and coupling | distinguish event transitions from directional attributable propagation; measure causally comparable alternatives | OPEN |
| G-H VVUQ | numerical tests, held-out/independent physical data or bounded benchmark, uncertainty and validity | OPEN |

Status vocabulary in active model admission: **ADMITTED CONCEPT**, **CANDIDATE**, **OPEN**, **EXCLUDED**. Model-fidelity choices above are recommendations, not authorization to freeze a state.

## 7. Deliverables and controlled execution sequence

1. **Component-function-input-transformation-output register** (this document; proposed).
2. Exact diagram of membership (vertical) versus cross-system exchange/causality (horizontal); distinguish system/subsystem/component/function/service.
3. Verify *specific* transformer/EVSE/cable/RESS technical data, cooling architecture, topology; decide vehicle/fleet schedule based on accessible measurements.
4. Audit closest source papers and equipment standards to establish I2/I3 and non-novelty boundary.
5. Admit individual model states and equations; record units, reference and applicability.
6. Implement M0/M1/M2 **only as case-readiness permits**, with controlled forcings and explicit no-unverified-causality constraint.
7. Define QOI: transformer temperature/limits, charging energy deficit, fleet required departure readiness, source/receiver event times and any justified directional delay.
8. Numerically verify, validate against independent evidence where feasible, quantify uncertainty, and interpret resilience from services. Update Deck3 from evidence rather than architecture hypotheses.

## 8. Decision needed from user + supervisor

Choose a bounded **actual** fleet service (e.g. electric buses with scheduled departures, or delivery fleet) only after checking data feasibility, along with transformer type and charger specs. If no direct case data can be obtained, disclose an explicitly synthetic/reference benchmark and do not claim empirical validation.

**No claim that this research has discovered a unique gap, finished the 26-paper full text review, admitted the P→T_e thermal law, or validated the proposed model.**

## 9. Objective traceability

- **SO1:** map and qualify P2/T1/T3 and I2/I3 state-dependent source→receiver laws.
- **SO2:** dynamically model only admitted physical/energy states and justified exchanges, with common heat input but no false coupling.
- **SO3:** time-stamp qualified thermal transitions and attributable propagation; translate constrained supply/charging to required electricity and mobility service outcomes.

The frozen active objectives remain unchanged.
