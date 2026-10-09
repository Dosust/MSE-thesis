# Component Function, Thermal Behavior and Data Roles — SoS Summary V1

**Date:** 2026-10-09  
**Status:** FINALIZED CONCEPTUAL SUMMARY for current working architecture; **NOT** an admitted equipment-specific model or verified coupling result.  
**Thesis:** Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience  
**Active scope:** extreme-heat thermal interdependencies between Power (P) and Electrified Transportation (T_e), evaluated through physical state and time.

**Relationship to authority:** This concise companion summarizes \`WORKING_SOS_COMPONENT_FUNCTION_INTERFACE_MATRIX_V1.md\` and preserves \`CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md\`, \`CANONICAL_STATE_TIME_DEFINITIONS_V1.md\`, frozen GO/SO1–SO3 and the transformer model-admission ledger. The complete system boundary is **not** reduced to the components explicitly modeled.

## Rule for every component

**Input → physical transformation → output**, with a separately defined **state-dependent behavior** (where dynamically necessary). The input may comprise physical flow, external forcing or control requests; *data records* represent/measure these quantities but are not physical components. Function ≠ state ≠ capability ≠ delivered service.

## Power System (P)

| Component or realized function | Function | Physical inputs / data needed | Transformation and possible thermal behavior | Output |
|---|---|---|---|---|
| Distribution transformer | Transform and deliver electrical power | Voltage [V], current [A], load profile [W or VA], ambient temperature [°C] | Electrical/core/loading losses produce heat; heat is stored and rejected with thermal inertia. Exact thermal states and operating law **not frozen** | Transformed power, physical thermal condition |
| Distribution feeder | Deliver power to EVSE supply boundary | Voltage, current, impedance, topology | Conduction, voltage drop, electrical losses; thermal capability only where demonstrated and material | Available AC electrical power |
| Protection and operating control | Apply actual admissible operating conditions | Measurements, equipment ratings, implemented settings/policies | Authorized protections/controls may curtail or interrupt supply; **no automatic temperature→curtailment assumption** | Permitted operation, actual command/interruption where established |
| Sensor/observation function | Observe Power conditions | Real electrical/thermal quantities at sensor locations | Sensing, sampling, uncertainty and time stamps; observation ≠ true physical state | Measured data for model checking |

Upstream supply is an explicit boundary condition/input at this application level, not removed from the full Power System.

**Sources to audit:** Hilshey et al. (2013), DOI: 10.1109/TSG.2012.2217385 (charging-driven transformer thermal modeling); Visakh & Selvan (2023), DOI: 10.1016/j.segan.2023.101096 (transformer service-disruption and charging constraints). These provide precedents, **not** complete selected-case proof of a thermal operating law.

## Electrified Transportation System (T_e)

| Component or realized function | Function | Physical inputs / data needed | Transformation and possible thermal behavior | Output |
|---|---|---|---|---|
| EVSE DC charging converter | Convert grid-side AC into controlled DC charging power | AC supply [W, V], charging request, ambient conditions, device operating data | Conversion losses and heat rejection; temperature-dependent derating where evidenced for selected hardware | DC charger power |
| Physical charging connection | Transfer DC energy to the vehicle | Voltage/current, connector rating | Resistive/contact losses; heat-conditioned current restriction if evidenced | Vehicle inlet power |
| Rechargeable energy-storage system (RESS) | Store energy for propulsion | Terminal charging/discharging power, initial SOC, relevant temperatures | Energy accumulation and losses; thermal charging acceptance only if qualified. SOC is **energy state** | Stored energy / SOC and terminal electrical output |
| Battery thermal management | Keep battery inside permissible operating conditions | Battery heat, ambient temperature, cooling commands/power | Cooling/heating with electrical consumption; possible capability limitation | Thermal regulation, auxiliary energy demand |
| Traction motor and inverter | Provide propulsion | Battery power, vehicle duty/traction demand | Electrical-to-mechanical energy conversion; losses and documented derating where relevant | Mechanical propulsion output |
| HVAC and vehicle auxiliaries | Provide cabin/auxiliary service | Ambient and cabin loads, battery supply | Cooling/auxiliary electricity demand; may rise in heat | Cabin/auxiliary function and energy demand |
| Charging/fleet control **function** | Coordinate charging and departures | SOC, capacity, actual constraints and schedules | Feasible charging allocation and commands (implemented software/hardware/organization, not separate infrastructure system) | Charging setpoints and assignments |
| Fleet mobility **service function** | Assess fulfillment of transportation obligations | Vehicle availability, energy, route demands and deadlines | Apply declared service criteria; readiness is not necessarily completed trip delivery | Ready departures / fulfilled trips, if observed |

The canonical T_e includes vehicle power-supply circuits and communication/control for power transfer; bidirectional transfer requires actual technology evidence. Fleet services and schedules are service functions/requirements, not physical components.

**Source to audit:** Krama et al. (2026), DOI: 10.1016/j.ecmx.2026.101960, documents heat-sensitive fast-charging performance for particular field equipment; general device transferability is open.

## Four distinct roles of data

| Role | Examples | Why |
|---|---|---|
| Model inputs and initial conditions | Extreme ambient temperature, time-varying charging demand, initial SOC | Drive an admitted physical model under declared exposure/operation |
| Physical/model parameters | Thermal capacitance, resistance, efficiency and equipment limits | Specify laws, loss mechanisms and validity domain; values **must be sourced** |
| Independent observations | Measured temperatures, voltage, current, AC/DC power | Parameter estimation and independent validation with separation of calibration/test sets |
| Service requirements | Departure deadline, energy needed for route, declared electricity demand | Define adequacy and measurable resilience outcomes |

**Do not conflate:** actual physical inputs with stored data; measured values with truth; calibration data with independent validation data; thermal states with battery SOC; internal power-electronic dissipation with the entire EVSE charging power transfer.

## Conditional SoS mechanisms

- **T_e → P:** EVSE grid-side AC demand changes transformer loading and associated thermal response, using physically valid electrical accounting.
- **P → T_e:** transformer heat-dependent *actual operational constraint* changes available EVSE power and delivered vehicle energy **only if** corresponding operating/protection law is established.
- **Common external extreme heat:** affects both systems but does not alone prove interdependence.
- **Within T_e:** EVSE self-derating or battery charge acceptance is not automatically P→T_e coupling.

Potential nonlinear feedback/thresholds/propagation are **hypotheses to test**, not attributes assigned to the architecture in advance.

## Minimum-sufficient active-model recommendation

- P: evidence-admitted transformer thermal response, AC electrical boundary and applicable protection/capability law.
- T_e: evidence-admitted EVSE temperature-dependent capability, battery energy balance and declared fleet mobility requirement.
- Environment: sourced high-temperature profile; external forcing rather than a modeled internal infrastructure state.
- Outcomes: thermal transition times, only *attributable* cross-system delays, delivered charging energy, electricity adequacy and mobility service.
- Complexity: use nonlinear/hybrid/causal mechanisms only if required by observed physical operation and independently supported.
- Existing comparators: **M0 = independent P/T_e, M1 = static/algebraic coupled, M2 = qualified dynamic causal coupled**; no unqualified DM label introduced.

## Scientific references / source status

1. Hilshey et al. (2013), *Estimating the Impact of Electric Vehicle Smart Charging on Distribution Transformer Aging*. https://doi.org/10.1109/TSG.2012.2217385
2. Visakh & Selvan (2023), *Analysis and mitigation of the impact of electric vehicle charging on service disruption of distribution transformers*. https://doi.org/10.1016/j.segan.2023.101096
3. Krama et al. (2026), *Impact of extreme climatic conditions on fast EV charger performance: field experimental insights from Qatar*. https://doi.org/10.1016/j.ecmx.2026.101960

Bibliographic linkage is established from the working review; **this concise summary does not assert full-text equation-level verification, case-specific parameter validation, identified novelty or certified bidirectional thermal propagation**.

## Next gate, not part of this closure

Choose equipment topology and fleet service with feasible observations; complete closest-paper full-text and standards audits; admit model states, constitutive equations and state→capability handoffs; verify and validate before promoting numerical claims.