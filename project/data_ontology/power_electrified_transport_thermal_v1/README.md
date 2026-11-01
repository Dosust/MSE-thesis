# Power–Electrified Transportation Thermal Data Ontology (proposed v1)

**Research:** Engineering of Power–Electrified Transportation Interdependencies for Resilience.  
**Status:** TARGET DATA SPECIFICATION, not observational evidence, model validation, or a new frozen thesis decision.  
**Physical systems:** Power P and Electrified Transportation T_e, distinct. EVSE belongs to T_e.  
**Active focus:** extreme-heat thermal interdependencies, directional qualification, physical state-time, electricity/mobility services, resilience, bounded sustainability interpretation.

## Objective alignment
- **SO1 — Qualify:** thermal source/receiver, evidence, physical topology, directional mechanism and confounders.
- **SO2 — Model:** exogenous forcing H(t), admitted states X(t), traceable input/parameter data, control events, verified interface exchange, time calibration.
- **SO3 — Quantify:** critical state/capability transitions, propagation delays, required/delivered service, recovery (only if modeled), and service consequences.

## Deliverable contents
- `ontology.ttl` — parseable proposed OWL/RDF entity and directed-relation vocabulary (not a formal full OWL DL decision theory).
- `data_dictionary.csv` — **301 uniquely registered fields across 21 normalized tables**, with units, datatype, role, and admission priority.
- `data_contract.schema.json` — JSON Schema for table rows and structural required fields. Does NOT establish physical causality or parameter validity.
- `tables/*.csv` — empty header-only import templates; **no synthetic or fake data**.
- `quality_gates.md` — requirements for evidence, physics, service, and VVUQ.

## Admission priorities
- `M` = structural/metadata mandatory **when that table is used** (IDs, provenance, time, definitions).
- `A` = mechanism-critical candidate for a **particular** P→T_e, T_e→P, or service analysis. Must be present for any dependent claim; not universally mandatory.
- `C` = conditional when the particular component model or confounder requires it.
- `O` = optional supporting field.

A **complete ontology does not imply collecting all fields**. Select the minimum sufficient coupled case; data availability and admission remain OPEN until audited.

## Why relational tables rather than one giant 150-column CSV?
- Hardware topology (`power_connection`) is versioned independently from measurement.
- `weather_observation`, `power_observation`, `evse_observation`, `vehicle_observation` and `mobility_observation` may have different sampling intervals.
- `mechanism_evidence` separates *candidate* and *qualified* thermal interactions.
- `source_provenance` prevents simulations and unverified web data from being mislabeled as field evidence.
- `scenario` permits matched reference → heat-only → heat-plus-response comparisons.
- `service_requirement` fixes the time interval, unit, scope and threshold before resilience computation.

## Preferred physical join path
`study_case.site_id → power_connection.feeder_id / transformer_id / power_bus_id → power_connection.connected_evse_id → charging_connection.charger_evse_id → charging_connection.vehicle_id → mobility_observation.vehicle_id / route_id`

Join observations by *appropriate temporal interval matching*, not by row number. Requiring an identical timestamp may discard genuine measurements with different sample periods; alignment uncertainty must be reported.

## Additional operational documents
- `implementation_and_minimum_evidence.md` — independent P→T_e/T_e→P admission bundles, questions and mathematical data use.
- `required_variable_bundles.csv` — claim-by-claim collection and validation requirements.
- `field_aliases.csv` — exact mapping of the 12 original user-requested field names to registered variables.

## Core aliases from the request
- `timestamp_utc`: UTC observation time, present in every relevant observation table.
- `transformer_id`, `evse_id`: join keys; *physical connection* additionally requires `power_connection` evidence.
- `ambient_temperature`: external forcing, not an internal dynamic state.
- `transformer_top_oil_temperature`: canonical measured variable for requested `top_oil_temperature`.
- `transformer_load`: legacy ambiguous alias; prefer **`transformer_load_current_A`** OR **`transformer_apparent_power_kVA`**, with meter and phase basis.
- `evse_temperature`: measure with documented sensor position.
- `evse_ac_power`: grid-side active power at confirmed boundary.
- `charger_power_limit`: control/capability value with documented origin.
- `battery_soc`: conditional energy state, not thermal state.
- `mobility_service_delivered` and `mobility_service_required`: share a declared `mobility_service_unit`, interval and service boundary.

## Causal qualification — distinct paths
**P→T_e**: extreme heat → transformer thermal state → justified operating constraint → constrained EVSE AC power/energy → observed mobility service deficit (where claimed).

**T_e→P**: EVSE thermal condition → verified thermal charger control/derating → grid-side AC load change → transformer load and thermal response. Control SOC, vehicle request, background load, weather, schedules and grid actions.

Common heat exposure can produce correlated thermal states without either cross-system direction being demonstrated.

## Non-negotiable distinctions
- `External forcing != system state != capability != service != resilience`
- `Physical connection != verified thermal interdependency`
- `SOC != thermal state`
- `Estimated hot-spot temperature != physically measured hot-spot temperature`
- `Simulation != independent empirical validation`
- `Service-level resilience != component survival`

## Scientific authority
Align this dataset contract with the frozen `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`, `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`, `project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md` and evidence/non-invention standard in the user's GitHub research repository.

## Next practical implementation
1. Choose a **single site or declared bounded testbed** and register topology/source provenance.
2. Inventory actually available sensors and validate timebase, equipment/connection, units and sensor location.
3. Audit model-state admission and independent P→T_e / T_e→P mechanism evidence.
4. Declare electricity and mobility service requirements, uncertainty and matched cases.
5. Admit only variables with traceable measured or model-specific justified parameter basis. Mark everything else OPEN.
