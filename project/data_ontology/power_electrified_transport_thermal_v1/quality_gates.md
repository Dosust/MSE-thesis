# Scientific Admission and Quality Gates — Version 1

This is a proposed target data contract, not a statement that any matching dataset exists.

## A. Core truth/provenance
1. Preserve original raw files, hashes, source version, licensing, ownership and data-collection procedure.
2. Every observation must resolve its asset/sensor/source and an ISO-8601 UTC timestamp.
3. Distinguish **measured**, **estimated**, **modeled**, and **simulated**; do not silently mix them.
4. Missing value is missing, not zero. Record missingness reason; never invent measurements.
5. Sensor location matters: transformer top-oil, winding hot-spot, EVSE internal, inlet, heat-sink and battery temperature must not be conflated.
6. Store equipment rating/threshold provenance and validation domain before numerical use.
7. The chosen sampling period must resolve thermally relevant response and event timing; never infer seconds from a `Time_Step` index.

## B. Physical topology and boundary
8. Verify `transformer_id → power_bus_id → evse_id` connectivity with dated, source-backed wiring/mapping. EVSE belongs to T_e.
9. Check asset/time validity, charging session to connector/vehicle mappings, and meter boundary.
10. Use grid-side AC power for T_e→P coupling, not DC-only charger output without conversion losses.
11. Background (non-EV) loading must be measured/controlled or uncertainty explicitly bounded.
12. V2G export must have a documented signed-power convention; non-V2G charging cannot show unexplained negative grid power.

## C. Thermal mechanism gates
13. **P→T_e:** require source thermal state, documented transformer/circuit restriction and cause, EVSE supply/capability change and service outcome if claimed. Raw temperature vs charging correlation alone fails.
14. **T_e→P:** require thermally attributed EVSE control response, measured change in grid-side AC charging demand, resulting transformer loading/thermal response, and competing explanation checks (SOC, charge request, baseline load, ambient, operator dispatch).
15. Shared external heat forcing is a common cause, not proof of a directional interdependency.
16. Establish counterfactual/matched scenarios or a controlled test where possible. Record residual confounding explicitly.
17. Record exact detector, threshold source, event time uncertainty, and reason code for transition claims.

## D. Mathematics and service
18. Unit-check thermal energy balance, electrical power, AC/DC metering boundary and time-integrated energy. Define apparent vs active power distinctly.
19. Admit active states only when necessary for future evolution, capability, timing or service; SOC is an energy state, not a thermal one.
20. Derived capability is not physical state. Service requirement must match delivered-service numerator units and time base.
21. Distinguish thermal transition time, propagation delay, service deficit onset and recovery time.
22. Prevent zero-denominator service fractions; define service requirement even when zero demand occurs.
23. For three sustainability cases (baseline, heat without response, heat with response), keep same unit, horizon and accounting boundary.

## E. VVUQ and ethics
24. Independently evaluate model code (dimensional checks, conservation, limiting-case tests and numerical convergence).
25. Independent physical validation requires measured observations held out from parameter fitting; synthetic-to-synthetic comparison is not empirical validation.
26. Report uncertainty in sensors, time alignment, parameter estimates, modeled forcing, network mapping and service observation.
27. Do not claim global causality or extrapolate beyond equipment/ambient/charging operating ranges.
28. Avoid individual trip identifiers that expose personal travel histories; anonymize aggregated service records.

## F. Dataset admission labels
- **MECHANISM QUALIFICATION READY:** documented topology, timed source and receiver measurements, reason codes, confounder records, and credible comparison design.
- **COMPONENT MODEL READY:** a valid measured source for thermal states and loads under documented conditions; not automatically coupled-validation-ready.
- **SERVICE ASSESSMENT READY:** time-aligned required and delivered electricity/mobility services in common units.
- **SIMULATION ONLY:** coherent topology/parameter/scenarios without independent field measurements.
- **EXPLORATORY ONLY:** descriptive or synthetic records without adequate clock, physical mapping, thermal variables, or provenance.

## Standards/vocabulary references (contextual, not mandatory implementation)
- W3C SSN/SOSA observation entity/sensor/feature pattern: https://www.w3.org/TR/vocab-ssn/
- QUDT quantity/unit/quantity kind pattern: https://qudt.org/doc/2026/02/DOC_SCHEMA-QUDT.html
- Open Charge Alliance OCPP protocol device monitoring/transactions: https://openchargealliance.org/protocols/open-charge-point-protocol/

The thesis's exact frozen scientific decisions control over this proposed data-design file.