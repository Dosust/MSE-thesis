# Dossiya Research Expert — Final Component Four-Element and Data-Role Reasoning Standard V1

**Status:** FINAL FOR SKILL REASONING METHOD (not a freeze of case-specific physical models, states, equations, thresholds, or data).  
**Effective:** 2026-10-09.  
**Authority:** subordinate to frozen title, system boundary, thermal state-time definitions, three objectives, research evidence and citation standards. Supersedes earlier ambiguity about the intended four elements in the component-reasoning skill.

## Governing four elements — exact

For each actual *physical component*, explicitly define:

**INPUT → PHYSICAL TRANSFORMATION → OUTPUT → STATE-DEPENDENT BEHAVIOR.**

Also record its **function** (why it exists), **system/subsystem membership**, and **contribution to required electricity or mobility service**. These are contextual descriptors, not substitutions for the four elements. Explain every link. External ambient heat is a forcing; state-dependent capability is not identical to an internal dynamic state.

## Component matrix: Power System P

| Component | Function | Input (candidate measured/input quantities) | Physical transformation | Output | State-dependent behavior to qualify |
|---|---|---|---|---|---|
| Transformer | Change voltage and transfer electrical power | Upstream voltage/current, aggregate load, ambient temperature | Electromagnetic transfer and electrical losses produce heat; cooling and thermal inertia govern internal thermal evolution | Electrical supply, thermal condition and losses | Temperature-conditioned allowable operation only under verified equipment/standard/control rules |
| Distribution feeder | Transfer power to EVSE | Voltages, currents, conductor/line impedance | Power flow, voltage drop and electrical losses; heating where material | Available voltage/power, losses | Limits conditional on specified ratings and conditions |
| Protection/control | Maintain admissible operation | Sensors, settings, operational commands, ratings | Enforces actual operating and protection logic | Permitted supply, commands or interruption | Switching, derating or trips **only** with documented rule and activation conditions |
| Sensors | Observe physical quantities | Voltage/current/temperature and measurement conditions | Transduction, sampling and measurement errors | Observations/time series | Sensor response, uncertainty or drift if material |

## Component matrix: Electrified Transportation System T_e

| Component | Function | Input (candidate quantities) | Physical transformation | Output | State-dependent behavior to qualify |
|---|---|---|---|---|---|
| EVSE (DC charger in proposed application) | Condition and deliver vehicle charging power | AC power, ambient temperature, requested charging, cooling/control inputs | AC/DC conversion, electrical losses, heat rejection, temperature-conditioned controls where documented | DC charging power actually delivered, losses/heat | Thermal derating only under equipment/experimental evidence |
| Charging connection | Transfer power to vehicle | Current, voltage, connector ratings | Conduction/contact resistance, possible heating | Vehicle-inlet electrical power | Current reduction or shutdown only when actual limit mechanism established |
| Rechargeable battery (RESS) | Store energy | Accepted charging power, initial SOC, thermal conditions if relevant | Energy accumulation with losses, electrothermal effects where material | Stored energy/SOC, available discharge capability | Temperature-sensitive acceptance/operation conditionally admitted |
| Battery cooling | Regulate battery temperature | Battery heat, ambient/coolant conditions and controls | Heat extraction with auxiliary energy consumption | Cooling rate, auxiliary load | State-conditioned cooling capacity where supported |
| Traction motor/inverter | Convert electrical energy into propulsion | Battery power, drive command | Electrical-to-mechanical conversion and heat losses | Mechanical power | Thermal torque/power restrictions only if relevant to actual selected service |
| Vehicle HVAC | Maintain cabin thermal conditions | Ambient conditions, cooling demand, electrical supply | Thermal exchange and auxiliary electrical consumption | Cabin cooling, auxiliary load | Performance and demand may depend on thermal conditions |
| Fleet control | Allocate power and schedule vehicle operation | Energy/SOC, charging availability, schedules | Decision/control logic subject to actual constraints | Charging commands, allocations | Feedback/mode decisions only if specified and evidenced |

**Fleet service is an outcome/functionality layer, not automatically a hardware component:** inputs include vehicle readiness, route/departure requirements; output is a declared measured service proxy (departure readiness) or actual trips provided. A SOC threshold alone does not establish full mobility-service provision.

**Power vs energy:** Charger input throughput is not charger self-consumption, and battery energy storage is not a conventional end-use consumption load. Distinguish AC input, EVSE losses, DC output, battery accepted power, SOC, propulsion/auxiliary demand; use compatible measurement boundaries and units.

## Four distinct data roles

| Role | Examples | Scientific role |
|---|---|---|
| Model inputs / forcing / initial conditions | Ambient time series, charging request, initial SOC | Drive evolution under declared conditions |
| Physical parameters | Thermal capacitance, electric resistance, efficiencies | Specify constitutive and dynamical laws; record source/calibration/uncertainty |
| Observations | Measured transformer/EVSE temperatures, actual AC/DC power | Estimate/calibrate and **independently validate** appropriately partitioned predictions |
| Service requirements | Departure time, required energy, electricity service threshold | Determine the adequacy of actual service outputs |

A dataset is **not** an infrastructure component. Its role is determined by how it enters the governing model and evidence workflow. Calibration measurements and independent validation data must not be silently conflated.

## Reasoning flow — scientifically qualified

Component function → four elements → conservation/operating law → necessary dynamic states and algebraic constraints → directional mechanism → state/time transitions → actual power/energy service consequences → independent verification/validation.

The conceptual chain
```
Model inputs + physical parameters
   → physics and evolving states
   → predicted outputs
   ↔ measured observations for calibration and independent validation
   → service requirements comparison
```
is **not** an assertion that validation observations physically transform predicted outputs. Observations test predictions; service requirements define adequacy.

Candidate bounded demonstrator only (not model freeze):
- P: transformer thermal dynamics + qualified electrical supply/operating constraints.
- T_e: EVSE thermal capability + battery energy accounting + declared fleet requirements.
- Shared heat: measured or justified exogenous exposure.
- Outputs: justified thermal transitions, attributable interface propagation if demonstrated, actual delivered energy and service adequacy.

## Citations and scientific guardrails

Candidate external grounding to verify at exact claim/equation level:
- Hilshey et al. (2013), *Estimating the Impact of Electric Vehicle Smart Charging on Distribution Transformer Aging*, https://doi.org/10.1109/TSG.2012.2217385 — transformer thermal dynamics under EV charging.
- Visakh and Selvan (2023), https://doi.org/10.1016/j.segan.2023.101096 — distribution-transformer operating/service restrictions under EV charging.
- Krama et al. (2026), https://doi.org/10.1016/j.ecmx.2026.101960 — field evidence on charger performance in hot conditions.

Do not assert a model equation, parameter, threshold, validation result, or application transfer based solely on these titles/DOIs; retrieve and cite the primary section or figure before claim-level use. Follow `project/RESEARCH_REASONING_PROTOCOL.md`, `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md` and `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md` (APA 7 adjacent author–date citations).

## End state / completion acceptance

1. Every included physical component has function + exact four elements + system/subsystem classification.
2. All technical input quantities have correct physical/data roles and units.
3. All thermal changes and cross-system arrows have evidence or OPEN status.
4. Model states, capabilities, delivered flows and services remain distinct.
5. Active modeling complexity is minimum sufficient for SO1–SO3; fleet/depot boundary does not override full T_e scope.
6. Maintain frozen research direction and no invention. This reasoning standard is final unless the user explicitly revises it.
