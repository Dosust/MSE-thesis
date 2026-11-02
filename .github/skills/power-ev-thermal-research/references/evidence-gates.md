# Scientific gates — explicit admissibility and fail conditions

All gates independently assessed `PASS`, `FAIL`, `BLOCKED_EVIDENCE`, `BLOCKED_EXTERNAL_ACCESS`, `DEFERRED_DEPENDENCY`, or `NOT_RUN`. A missing item is never an implied PASS.

| Gate | Admissibility test | Failure/block consequence |
|---|---|---|
| G0 Origin | original source, DOI/URL, rights, exact dataset version and SHA-256 | `BLOCKED_EVIDENCE` source still metadata-only |
| G1 Measurements | sensor/metric semantics, unit, time, physical boundary, missing/interpolation status | cannot treat readings as direct comparable observations |
| G2 Topology | same physical system, transformer→feeder→EVSE connectivity documented and IDs crosswalked | no verified coupled electrical/thermal field assertion |
| G3 Synchronization | clock domains, overlap, time tolerance, aggregation and uncertainty documented | no joint event inference |
| G4 Directional physical mechanism | actual thermal state → capable limit/action → measurable counterpart consequence, confounders assessed, direction separately justified | electrical load/temporal correlation only |
| G5 Mathematical admissibility | derived/literature equation class, units, assumptions, boundary/initial conditions, parameters and physical limiting cases | model remains candidate or OPEN |
| G6 Component VVUQ | independent real data, baseline, no leakage, numerical convergence, parameter identifiability and UQ | component conditionally studied but not physically validated |
| G7 Coupled **field** VVUQ | G0–G6 + synchronized same-site transformer/EVSE thermal/electrical channels + independent directional challenge/test | `BLOCKED_EVIDENCE`, not coupled field-validated |
| G8 Resilience & bounded sustainability | evidenced required electricity/mobility services, thresholds, horizon, state-time propagation and relevant indicator provenance | no quantitative resilience or SDG effect claim |

## Mandatory cross-system claim predicates

A record labeled `CONNECTED_THERMAL_FIELD_VALIDATED` must show **all**: `same_site_verified=true`, `physical_topology_verified=true`, `clock_sync_verified=true`, `transformer_thermal_measured=true`, `evse_thermal_measured=true`, `independent_test_pass=true`, `directional_mechanism_verified=true`, and actual sources/circuit paths.

A **measured same-premises EV–grid electricity dataset** may pass electrical association without demonstrating transformer identity or direct thermal coupling. `connected_electrical` and `connected_thermal` are distinct evidence levels. Never infer both arrows by naming a bidirectional model.

**Conditional model** = model using observed future forcing, not actionable future performance. **Synthetic test** = internal software/physics verification, never field validation. **Correlated traces** = observation, not a causal mechanism. **Identifiability** = cannot be inferred solely from an optimizer's successful termination.

When BLOCKED, record missing evidence, source URL, next retrieval experiment, owner/contact (if known), affected output(s), and a viable independent research task. Do not replace absent observations with invented numbers.
