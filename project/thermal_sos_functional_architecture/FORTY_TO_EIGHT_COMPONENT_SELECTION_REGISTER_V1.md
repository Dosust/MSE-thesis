# 40-to-8 Component Selection Register — Version 1 (2026-10-10)

**Status: NEW WORKING UNIVERSE; 40 CLASS CANDIDATES; 8 PROVISIONAL; 0 FULLY ADMITTED.** This is not a frozen 40-item canonical inventory, not a completed physical selection and not 40 dynamic state variables.

## Rationale
The existing working architecture itemizes five Power component/functions and eight Electrified Transportation component/functions. This document **extends these to a provisional research universe** of 20 P and 20 T_e equipment/subassemblies/realized controllers and instruments. Candidate categories are mixed hierarchy and may overlap as parent/subassembly: account for this explicitly; avoid counting device losses twice. System scope remains complete; research scope remains strictly extreme-heat thermal interdependencies, state and time. Four per system is a proposed design constraint, not a proven minimum.

## Non-compensatory screening protocol
| Gate | Evidence that must be produced | Current status |
|---|---|---|
| G0 Classification | Physical device, subassembly or realized controller, belongs to correct system; hazard, power interface, datasets and service are not components | Candidate taxonomy only |
| G1 Reality | Identified selected device + topology/nameplate, compatible kVA/kW, cooling configuration, legal control authority | ALL OPEN |
| G2 Thermal physics | Applicable loss/storage/rejection/derating and exact source-backed operating limit, not generic standard title | ALL device-specific OPEN |
| G3 Directional relevance | Participates in qualified source-to-receiver P→T_e or T_e→P mechanism, or essential mobility/electricity-service mapping; component alone need not cause cross-system effect | OPEN for full causal law |
| G4 Materiality | State, event, response, service or uncertainty changes when candidate included vs defensible reduced model | TEST NOT RUN |
| G5 Validation feasibility | Traceable parameter/observations, identification, independent holdout/VVUQ route | ALL OPEN |

**Admission rule:** admit only if G0–G5 pass. Never add scores that compensate for missing source/operating-law/validation evidence. Use PIRT relevance vs knowledge (US NRC 2008, NUREG/CR-6944) and observability/identifiability (Villaverde 2019) as methodological precedents.

## Provisional eight (subject to actual case and evidence)

**Power:** P02 oil transformer; P05 cooling assembly (only if fitted, otherwise P04 or aggregate); P08 actual protective/loading controller; P10 distribution feeder conductor/cable.

**Electrified Transportation:** T01 offboard DC converter; T04 EVSE cooling; T09 connector/contact (only if thermal limit material, otherwise screen T08/T12); T11 vehicle battery pack.

Eight candidate classes do NOT require eight ODEs; two cooling subassemblies may be integral to parent equipment; sensors are mandatory for validation even when not selected as modeled components. If no eight satisfy G0–G5, record the blocked quota rather than fabricate missing component dynamics.

## Full provisional 40-row register

| ID | System | Equipment or realized hardware | Candidate relevant phenomenon | Decision | G1 / G5 |
|---|---|---|---|---|---|
| P01 | Power | Upstream supply terminal | boundary supply | reserve/boundary | OPEN / OPEN |
| P02 | Power | Oil-immersed distribution transformer | winding/oil temperature, actual load limit | PROVISIONAL_4 | OPEN / OPEN |
| P03 | Power | Dry-type transformer | alternative insulation thermal model | alternative | OPEN / OPEN |
| P04 | Power | Tank/passive radiator | passive heat rejection | reserve | OPEN / OPEN |
| P05 | Power | Transformer cooling assembly | fan/pump/cooling mode if fitted | PROVISIONAL_4 | OPEN / OPEN |
| P06 | Power | Bushings/terminals | contact thermal rise | reserve | OPEN / OPEN |
| P07 | Power | Transformer thermal sensor | observe temperature | support | OPEN / OPEN |
| P08 | Power | Transformer protection/loading controller | temperature-to-permitted-power rule | PROVISIONAL_4 | OPEN / OPEN |
| P09 | Power | Feeder head breaker | protective trip/current heating | reserve | OPEN / OPEN |
| P10 | Power | Distribution feeder conductor/cable | AC transfer/Joule heat/ampacity | PROVISIONAL_4 | OPEN / OPEN |
| P11 | Power | Cable termination | contact temperature | reserve | OPEN / OPEN |
| P12 | Power | Cable splice/line joint | joint temperature | reserve | OPEN / OPEN |
| P13 | Power | Distribution busbar/switchgear | contact heating | reserve | OPEN / OPEN |
| P14 | Power | Pole-mounted recloser | event/switching response | reserve | OPEN / OPEN |
| P15 | Power | Voltage regulator | voltage and optional thermal limit | reserve | OPEN / OPEN |
| P16 | Power | Capacitor bank | reactive electrical boundary | boundary | OPEN / OPEN |
| P17 | Power | AC power meter | observe actual load | support | OPEN / OPEN |
| P18 | Power | SCADA/RTU hardware | observe actual controls | support | OPEN / OPEN |
| P19 | Power | DER inverter | alternative source thermal derating | boundary | OPEN / OPEN |
| P20 | Power | Grid battery inverter | optional response thermal condition | boundary | OPEN / OPEN |
| T01 | Electrified Transportation | Off-board DC EVSE converter | conversion loss and thermal derating | PROVISIONAL_4 | OPEN / OPEN |
| T02 | Electrified Transportation | EVSE input contactor/filter | contact/filter heating | reserve | OPEN / OPEN |
| T03 | Electrified Transportation | EVSE DC output module | converter submodule heating | support | OPEN / OPEN |
| T04 | Electrified Transportation | EVSE cooling system | fan/liquid cooling capacity and auxiliary draw | PROVISIONAL_4 | OPEN / OPEN |
| T05 | Electrified Transportation | EVSE cabinet/ventilation | thermal boundary conditions | reserve | OPEN / OPEN |
| T06 | Electrified Transportation | EVSE rectifier T sensor | observe EVSE temperature | support | OPEN / OPEN |
| T07 | Electrified Transportation | EVSE AC meter | measure AC demand P/Q | support | OPEN / OPEN |
| T08 | Electrified Transportation | DC charging cable | conductor heating/current limit | reserve | OPEN / OPEN |
| T09 | Electrified Transportation | Charging connector/contact | contact T-dependent restriction if binding | PROVISIONAL_4 | OPEN / OPEN |
| T10 | Electrified Transportation | Vehicle charging inlet | inlet thermal limits | reserve | OPEN / OPEN |
| T11 | Electrified Transportation | Vehicle battery pack | SOC and thermal charge acceptance | PROVISIONAL_4 | OPEN / OPEN |
| T12 | Electrified Transportation | Battery management ECU | actual charge-current rules | support | OPEN / OPEN |
| T13 | Electrified Transportation | Battery cooling circuit | battery heat rejection | reserve | OPEN / OPEN |
| T14 | Electrified Transportation | Onboard AC charger | alternative AC-charging configuration | alternative | OPEN / OPEN |
| T15 | Electrified Transportation | Traction inverter | conditional drive thermal derating | reserve | OPEN / OPEN |
| T16 | Electrified Transportation | Traction motor | winding thermal limitation | reserve | OPEN / OPEN |
| T17 | Electrified Transportation | Vehicle HVAC compressor | heat-dependent auxiliary energy | reserve | OPEN / OPEN |
| T18 | Electrified Transportation | Cabin HVAC blower | auxiliary energy demand | support | OPEN / OPEN |
| T19 | Electrified Transportation | Vehicle DC-DC converter | conversion losses | reserve | OPEN / OPEN |
| T20 | Electrified Transportation | Charging communications controller | charging setpoint evidence | support | OPEN / OPEN |

## Mandatory evidence record for each row
Record **physical function, specific thermal mechanism, directional interface/service path, proposed mathematical representation, timestamped variables, equipment/source/standard clause, G0–G5 results, selected/rejected status, SO1–SO3 traceability** before promotion. Every row still needs selected-case data; the table above is **screening**, not law verification.

## Required physical pathway tests
**P→T_e candidate:** transformer thermal state → implemented loading/relay policy → actual permissible EVSE AC input → delivered charging energy and mobility. **T_e→P candidate:** EVSE internal thermal control → actual measured AC input → transformer current/loss/temperature. Common ambient heat and ordinary electrical supply alone do not prove either thermal interdependency. AC input and DC output must not be conflated.

## Research and downstream assessment
SO1 evidence qualify; SO2 conservation/AC interface ODE-DAE with minimal states; SO3 transitions/attributable propagation/service consequences. Compare M0 independent controlled counterfactual, M1 static/algebraic coupling, M2 only evidence-qualified dynamic causal coupling. Evaluate resilience via required electricity/mobility service; optional Improve/Adapt/Restore interventions; direct and engineering-response sustainability pathways and measured-indicator-to-SDG link only when supported.

## Source references and limits
- Architecture: https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/thermal_sos_functional_architecture/WORKING_SOS_COMPONENT_FUNCTION_INTERFACE_MATRIX_V1.md
- Thermal limit candidates: https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/thermal_sos_functional_architecture/EQUIPMENT_SPECIFIC_THERMAL_LIMIT_CANDIDATE_INVENTORY_V1.md
- Frozen scope: https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md
- Hilshey et al. 2013 https://doi.org/10.1109/TSG.2012.2217385
- Krama et al. 2026 https://doi.org/10.1016/j.ecmx.2026.101960
- IEEE C57.91-2025 https://standards.ieee.org/ieee/C57.91/7163/
- IEC 61851-23:2023 https://webstore.iec.ch/en/publication/32973
- PIRT US NRC 2008 https://www.nrc.gov/regulations-legislation/nureg-series-publications/publications-prepared-by-nrc-contractors/next-generation-nuclear-plant-phenomena-identification-and-ranking-tables-pirts-nuregcr-6944/v1
- Villaverde 2019 https://doi.org/10.1155/2019/8497093
- IEA 2025 https://www.iea.org/reports/electricity-2025/emissions and https://www.iea.org/reports/breakthrough-agenda-report-2025/road-transport (scope motivation, not device evidence)

**No numerical threshold, temperature-to-allowable-transformer-power law, EVSE-to-grid AC response, or reciprocal physical thermal propagation is established by this inventory.**
