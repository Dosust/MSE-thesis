# Implementation, minimum evidence bundles and competency questions

**Status: PROPOSED.** This file operationalizes the current frozen SO1–SO3. An ontology is a data definition, not an acquired or validated dataset.

## 1. The entities we must be able to identify

```
CASE --at_site--> SITE --has--> WEATHER EXPOSURE
SITE --contains--> POWER FEEDER --contains--> POWER BUS
POWER BUS --supplies via verified connection--> EVSE --has--> CONNECTOR
CONNECTOR --charging session with--> ELECTRIC VEHICLE --has--> RESS/BATTERY
ELECTRIC VEHICLE --performs--> TRIP / MOBILITY SERVICE
TRANSFORMER + EVSE + VEHICLE + SERVICE --each has--> TIMED OBSERVATIONS
OBSERVATION --measured by--> SENSOR --documented by--> PRIMARY SOURCE
MECHANISM --source event--> RECEIVER EVENT --assessed against--> CONFOUNDERS
CASE --has--> SERVICE REQUIREMENTS + SCENARIOS + VALIDATION TESTS
```

EVSE is a component of the **Electrified Transportation System**; power buses, feeders and transformers remain part of the **Power System**. An electrical connection is physical topology, not a claim of causal thermal dependence.

## 2. Bundle A — Minimum data to attempt P → T_e thermal mechanism qualification

**Necessary physical chain:** transformer ambient/thermal state → source-side restriction → electrical capability to EVSE → charger behavior → service consequence *if* service is claimed.

| Needed item | Target field / table | Why | Evidence status if absent |
|---|---|---|---|
| Dated physical connection | `power_connection.transformer_id`, `power_bus_id`, `connected_evse_id`, `connection_evidence_id` | Identify the real electrical path | Mechanism not qualifiable |
| Common timestamps | observation `timestamp_utc`, sensor `sampling_interval_s`, timebase | Compare thermal and electrical timing | Transition/lag unidentifiable |
| Heat exposure | `weather_observation.ambient_temperature` | External forcing and shared-cause control | Extreme-heat interpretation OPEN |
| Transformer thermal condition | `power_observation.transformer_top_oil_temperature` or independently qualified thermal state | Source thermal state | Thermal source unobserved |
| Transformer load and confounders | `transformer_load_current_A`, `feeder_non_ev_load_kW`, and relevant status | Separate load-induced heating/constraints | Attribution weak/OPEN |
| Verified thermal restriction | `transformer_restriction_active`, `transformer_restriction_reason`, `event`, `control_action` | Qualify source effect on operating capability | Correlation only |
| Receiving-side electrical response | `evse_observation.evse_ac_power`, `charger_power_limit`, charging request | Show actual receiver consequence | P→T_e effect OPEN |
| Charging service consequences (when claimed) | charging session energy, vehicle readiness, `mobility_service_required` and `mobility_service_delivered` | Quantify SO3 | Only interface consequence supported |
| Independent observation/source | sensor ID, source record, calibration, control log | Prevent unjustified inference | Validation not supported |

## 3. Bundle B — Minimum data to attempt T_e → P thermal mechanism qualification

**Necessary physical chain:** heat-conditioned EVSE state → verified *thermal* charger response → grid-side AC power change → transformer loading/thermal effect.

| Needed item | Target field / table | Why | Evidence status if absent |
|---|---|---|---|
| Connection | Same dated `power_connection` linking EVSE to transformer/bus | Establish physical path | Not qualifiable |
| EVSE temperature | `evse_observation.evse_temperature` + `sensor.sensor_location` | Receiver/source thermal state context | Thermal source unobserved |
| Verified charger cause | `evse_derating_reason`, `evse_derating_active`, `action`, event log | Rule out SOC/grid/dispatch limits | No thermally attributed effect |
| Request and control | `requested_charging_power_kW`, `charger_power_limit`, `commanded_charging_power_kW` where applicable | Separate demand change from control | Confounded |
| Grid-side response | `evse_ac_power` + meter boundary | Actual cross-system electrical exchange | T_e→P effect OPEN |
| Background load and heat | `feeder_non_ev_load_kW`, weather | Control external and other load changes | Confounded |
| Transformer response | `transformer_load_current_A` and thermal state if claimed | Establish physical receiving consequences | T_e→P thermal consequence OPEN |
| Matched controls/test | `scenario.matching_protocol`, `mechanism_evidence.confounder_evaluation` | Support directional attribution | Association only |

**Direction must be assessed independently.** Evidence for P→T_e does not automatically establish T_e→P.

## 4. Bundle C — Minimum data for mathematics and service-level resilience

- Thermally relevant initial conditions and valid timestamps/time units; component model, source-qualified parameters and independent checks.
- `service_requirement` fixes **what service**, spatial/fleet boundary, interval and threshold.
- Paired delivered services use the **same numerator/denominator unit, time interval and physical/service boundary**.
- `event` separates onset of heat exposure, component threshold crossing, receiver response, service disruption and recovery (only if observed or modeled).
- `analysis_output` stores T1-derived values with code commit, traceable inputs and explicit verification/validation status.
- `scenario` stores matched **baseline**, **extreme heat without response**, and **extreme heat with response** for resilience-response and bounded sustainability comparisons.

**Candidate mathematical relationships (structures, not calibrated laws):**

```math
\dot X_P^{th}=f_P(X_P^{th}, I_P, H, u_P;\theta_P),
\qquad
\dot X_{T_e}^{th}=f_T(X_{T_e}^{th}, P_{EVSE,AC}, H,u_T;\theta_T).
```

An interface exchange may be defined from actual metering, e.g. `P_EVSE,AC(t)`, subject to boundary and sign conventions. An algebraic capability `C(t)` may be derived from the admitted state; capability is not automatically a state. Recovery time, lag and critical-transition time are separate outputs.

The concrete component laws, active state vector, thermal parameters, thresholds, derivative definitions, and site-specific power limits are all OPEN until independent evidence is admitted.

## 5. Competency questions the dataset must answer

1. Which Power bus and transformer supplied a given EVSE at a given UTC time, with verifiable connection evidence?
2. What was the external ambient temperature at the transformer and EVSE during the relevant episode?
3. Did transformer top-oil/hot-spot temperature change before a documented *thermal* operating restriction?
4. Did that restriction reduce actual supply or charging capability compared with the matched operating condition?
5. Did EVSE thermal control change its *grid-side AC* load independent of the vehicle's SOC and requested power?
6. Did the EVSE AC load change the connected transformer's loading and subsequent thermal trajectory?
7. What were the temperature, constraint, receiver-response, service-onset and recovery event times and their uncertainties?
8. What electricity was required and delivered within the declared essential service boundary?
9. What mobility departures/trips were required and delivered during matching intervals?
10. Can a model calibrated with one period predict independent held-out thermal and electrical observations?
11. Did an engineering response improve service, and did it increase or decrease a *separately defined* sustainability indicator?
12. Are the results still supported if ambient temperature, background load, control actions and vehicle SOC are accounted for?

## 6. Joining independent datasets: evidence cautions

- A weather file and an unrelated transformer file can jointly inform physical submodels or scenario forcing; they do not constitute a measured coupled system.
- A charger dataset without transformer identity cannot validate transformer↔EVSE influence.
- A transport-delay dataset without electrification and service requirements cannot validate an EV charging thermal effect.
- A standard-compliant telemetry field is not proof the studied charger records that field.
- Never turn missing measured states into fabricated proxy observations; physically justified modeled estimates must be labeled separately.

## 7. Sensor/measurement semantics

Use W3C SOSA/SSN's **sensor — observation — observed property — feature of interest — result time** design pattern; QUDT's unit vocabulary where mapped. Neither standard defines this thesis's causal mechanisms or case-specific physical laws.