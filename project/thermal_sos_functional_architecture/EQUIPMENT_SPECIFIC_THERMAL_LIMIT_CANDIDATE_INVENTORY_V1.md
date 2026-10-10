# Full Candidate Inventory — Equipment-Specific Thermal Limits (V1)

**Date:** 2026-10-10  
**Status:** WORKING CANDIDATE REGISTER — NOT AN ADOPTED NUMERICAL THRESHOLD, DEVICE-SPECIFIC CONSTITUTIVE LAW, FROZEN STATE VECTOR, OR VALIDATED THERMAL INTERDEPENDENCY.  
**Source:** User-requested candidate inventory from 2026-10-10 conversation, with later supplied alternative inventory incorporated as candidate scope additions and technical clarifications.  
**Research scope:** Extreme-heat-conditioned thermal interdependencies between separate Power (P) and Electrified Transportation (T_e) systems; identify actual directional mechanisms, evolving physical state/time, electricity and mobility service consequences.

**Controlling authority:** [Current thesis authority index](../CURRENT_THESIS_AUTHORITY_INDEX_V1.md); [current component/function architecture](WORKING_SOS_COMPONENT_FUNCTION_INTERFACE_MATRIX_V1.md); [transformer model-admission ledger](../module_01_transformer_thermal_state_physics/MODULE_01_MODEL_ADMISSION_LEDGER_V1.md). This working inventory does **not** modify frozen thesis objectives, system boundaries, or M0/M1/M2 definitions.

## 1. Terminology and admission firewall

A thermal-limit **candidate** is an equipment-specific temperature, temperature rise, operating range, allowable-duration condition, or temperature-dependent capability restriction to investigate. It is **not** necessarily an established limit for the selected equipment.

Record these separately, rather than collapsing all as "the thermal limit":

1. **Physical thermal quantity/state** — measured/estimated temperature, temperature rise, heat flux, or ageing indicator. A state is *not automatically a limit*.
2. **Physical failure or performance criterion** — mechanism or condition associated with degraded performance/damage; often continuous, probabilistic, time-dependent, or device-specific.
3. **Manufacturer/standard/operator permissible envelope** — equipment-specific allowable operating regime, including loading duration and cooling assumptions.
4. **Control/protection threshold and implemented action** — actual controller/relay/operator rule; must distinguish warning, cooling activation, derating, trip, recovery/hysteresis, from measured execution.

The second user-proposed "three types" (physical, operating, control) is a useful conceptual grouping; the four-layer distinction above is more suitable for the thesis because it preserves actual state, prescribed rating, implemented action and observed service separately.

**Prohibition:** predicted high transformer hottest-spot temperature does not by itself prove a restriction of EVSE AC input, EV charging interruption, an enacted relay action, or decreased mobility service. Temperature response to common external heat does not alone prove P→T_e or T_e→P causal coupling.

## 2. Power System (P): full candidate thermal-limit register

| ID | Equipment or subsystem | Candidate thermal quantities, limits and restrictions | Inclusion decision |
|---|---|---|---|
| P-01 | Oil-immersed transformer — winding | Hottest-spot temperature; average winding temperature; winding temperature rise relative to ambient/oil | **CORE CANDIDATE** for selected oil-immersed device; exact states/limits OPEN |
| P-02 | Oil-immersed transformer — oil | Top-oil, bottom-oil, and winding-duct oil temperatures and temperature rises | CORE top-oil candidate; additional oil states conditional |
| P-03 | Transformer insulation and lifetime | Temperature-dependent insulation ageing / relative ageing rate; lifetime-consumption criterion; condition-dependent bubble/gas risk, if applicable | Candidate lifetime/physical-failure indicators; not automatic operational trips |
| P-04 | Transformer core and metallic parts | Core hot spots; metallic-part and stray-loss hot spots | CONDITIONAL on transformer architecture and loss model |
| P-05 | Transformer tank, bushings and terminals | Tank surface temperature; bushing and terminal contact temperature and permissible rises | CONDITIONAL on measured operational relevance |
| P-06 | Transformer cooling | Radiator capacity; oil and coolant temperatures; fan/pump operation, activation and failure; oil-flow/cooling-class limits | CONDITIONAL supporting capability / state law |
| P-07 | Transformer normal/emergency operation | Normal, cyclic, short-time/emergency loading; allowable temperatures, loss of life, duty duration, cooling capability, applicable warnings and trips | **CORE EVIDENCE GATE**: actual approved operating policy and protected equipment required |
| P-08 | Overhead feeder conductors | Conductor temperature; ambient/wind/solar-dependent thermal ampacity; emergency loading duration | CONDITIONAL to feeder type and thesis QOI |
| P-09 | Underground distribution cables | Conductor and insulation temperatures; joint/termination temperatures; continuous, cyclic and emergency ampacity | CONDITIONAL to selected feeder type |
| P-10 | Switchgear, breakers, busbars, protection | Contact/terminal/busbar/enclosure temperature rise; thermal-trip or protective settings; switching and cooldown | CONDITIONAL; electrical protection is not a new thermal state without evidence |
| P-11 | Dry-type transformer (alternative architecture) | Winding temperatures; insulation thermal classification; enclosure heat; winding protection trip | **ALTERNATIVE EQUIPMENT TYPE**, do not mix oil-immersed numerical laws or standards without qualification |
| P-12 | Upstream power-electronics / converters (if actually present) | Semiconductor junction and case temperatures; heatsink/cooling temperature; sustained/peak current capability, thermal derating and shutdown | CONDITIONAL, no implied equipment presence |

**Core scientific focus is P2 in the current architecture:** transformer state → actual permissible transformer-side supply (OPEN) → EVSE AC input/service. Additional upstream and feeder thermal states are admitted only if they materially change research outputs.

## 3. Electrified Transportation (T_e): full candidate thermal-limit register

| ID | Equipment or subsystem | Candidate thermal quantities, limits and restrictions | Research priority |
|---|---|---|---|
| T-01 | EVSE enclosure/cabinet | Permitted ambient range; cabinet inlet temperature; ventilation/environmental operating envelope | CORE CANDIDATE |
| T-02 | EVSE rectifier/converter | Measured rectifier temperature; thermal derating onset; converter available output and thermal shutdown | CORE CANDIDATE |
| T-03 | EVSE semiconductor junctions | Junction maximum operating temperatures; thermal impedance; safe operating envelope | CONDITIONAL |
| T-04 | EVSE power modules | Baseplate/case temperature; heat transfer and thermal interface material limits | CONDITIONAL |
| T-05 | EVSE active cooling | Airflow, fan activation, coolant temperature/flow, pump limits, cooling capacity and failure | CORE CANDIDATE |
| T-06 | EVSE AC input stage | AC input terminals, filters, contactors, input-component thermal limits; ancillary losses | CONDITIONAL |
| T-07 | EVSE DC output stage | Temperature-conditioned sustained and peak output capability; actual delivered power and shutdown | CORE CANDIDATE |
| T-08 | Physical charging cable | Conductor temperature; insulation temperature; current and time-dependent rating | CONDITIONAL |
| T-09 | Charging connector/contact | Contact temperature; temperature sensor location; current reduction and disconnect logic | CONDITIONAL |
| T-10 | Vehicle inlet | Terminal/contact/inlet temperature; vehicle charging restriction and disconnection | CONDITIONAL |
| T-11 | Battery cells / RESS | Permissible charging and operating temperature range; thermal dependent charge acceptance | CORE CANDIDATE where charging capability materially depends on RESS |
| T-12 | Battery pack | Pack temperature extremes, gradients and thermal nonuniformity | CONDITIONAL |
| T-13 | Battery management system (BMS) | Temperature-based charge current acceptance, cooling request, inhibit/trip and recovery/hysteresis | CORE CANDIDATE |
| T-14 | Battery thermal management | Coolant inlet/outlet, heat rejection, cooling activation, cooling availability, auxiliary electricity use | CONDITIONAL |
| T-15 | Onboard charger (only if used) | Converter junction/case/heatsink temperature and thermal power limit | CONDITIONAL; do not insert by default into an off-board DC fast-charging installation |
| T-16 | Traction inverter / motor | Converter junction, motor winding, coolant temperatures; torque/power thermal limitation | SUPPORTING mobility-demand context only unless essential |
| T-17 | Vehicle HVAC / auxiliaries | Compressor/auxiliary operating temperature; cooling capacity; heat-dependent auxiliary demand | SUPPORTING if required for mobility-energy calculation |

**Boundary:** EVSE and charging connection are within T_e; charging service and fleet mobility are service outputs, not new thermal components. Include direct battery thermal dynamics only if justified by measurements or demonstrably material service outcomes.

## 4. External conditions, loads and operational constraints (NOT all equipment limits)

| Quantity | Scientific role |
|---|---|
| Ambient air temperature and exposure duration | Common external forcing on P and T_e; **not an interdependency** |
| Solar radiation, wind and ventilation | Heat-transfer boundary/forcing as applicable |
| Electrical current, apparent power, power factor, harmonics, loading duration | Thermal generation and/or electrical constraints, depending on qualified equipment |
| Cooling mode, fan/pump availability, oil/air/coolant transport, thermal time constants | State/parameter/operational conditions; cooling failure may create discrete mode changes |
| EV connection, control authority, charging power limit, required battery energy, departure deadline | Operational constraints and service requirements; not thermal limits |
| Sampling time, sensor placement, sensor error, time synchronization | Observation and independent-validation requirements |

## 5. Scientific evidence record — one record for **every** candidate

| Mandatory field | Record precisely |
|---|---|
| Candidate ID / equipment identity | Manufacturer, model, rating, equipment configuration and cooling architecture |
| Thermal quantity and units | State/temperature sensor, location, °C/K, rise, heat-generation term and timebase |
| Type of condition | Measured state; damage/performance mechanism; continuous/cyclic/emergency permissible condition; warning/derating/trip/recovery |
| Governing envelope | Value **only when verified**; units, duration, loading/cooling mode, operating conditions, uncertainty |
| Operating/control action | Actual relay/operator/manufacturer control threshold, duty delay, hysteresis, action and permissible AC/DC power consequence |
| Governing evidence | Exact published standard edition + clause; manufacturer manual/test report; utility/operating policy; field observation; full source/page |
| Observable validation | Independent measured state and timestamps; P_AC vs P_DC vs battery terminals; device/control event logs; sensor calibration and time alignment |
| Model-admission verdict | ADMITTED CONCEPT / CANDIDATE / OPEN / EXCLUDED; parameter transfer and VVUQ limits; SO1/SO2/SO3 mapping |

**Blank threshold ≠ zero threshold.** Do not invent numerical ratings, generic IEC/IEEE thresholds, hysteresis/debounce or physical sensor accuracy. Parameters from other equipment cannot be silently reused.

## 6. Priority thermal interfaces and provisional laws

Power-side candidate permitted electrical capability:

\[
C_P(t)=\mathcal C_P\bigl(x_P^{th}(t),\text{applicable operating rules},\text{cooling and history}\bigr).
\]

EVSE-side candidate available DC output power:

\[
C_E(t)=\mathcal C_E\bigl(x_E^{th}(t),T_a(t),\text{verified device controls and battery limitations}\bigr).
\]

Both functions are **UNIDENTIFIED / NOT VALIDATED for our eventual selected equipment**. They are structural representations only.

**I3, P→T_e (conditional):** transformer thermal state → verified permissible loading / protection or control action → actual available EVSE AC input → service.

**I2, T_e→P (conditional):** internal EVSE heat and temperature-dependent control → *measured or justified grid-side AC demand* → transformer current/loss → transformer thermal trajectory.

**Common heat:** ambient temperature raises or changes P and T_e equipment temperatures independently and does not prove either direction. **EVSE DC derating is not numerically equal to AC demand change** without conversion-loss/auxiliary accounting.

## 7. Candidate reference standards (scope/edition/clauses MUST be independently audited)

**Power System:** IEEE C57.91-2025 (oil-immersed transformer loading), IEC 60076-7:2018 (oil-immersed transformer loading), IEEE C57.169-2023 (hot-spot determination), IEEE C57.12.90-2026 and IEC 60076-2:2011 (applicable transformer testing/temperature rise), IEEE 738-2023 (overhead conductor thermal current rating), IEC 60287-1-1:2023 (cable continuous current rating where applicable), IEEE C57.110-2018 and IEEE 519-2022 (harmonics if required).

**Electrified Transportation:** IEC 61851-23:2023 (DC EVSE), IEC 61851-24:2023 (DC charging communication), IEC 62196-3:2026 (connector compatibility), ISO 5474-1:2024 (vehicle conductive transfer), ISO 15118-20:2022 (vehicle/EVSE communication), ISO 6469 family (vehicle electrical/RESS safety).

These named references are **candidate authorities**; a scope summary is not a full standard audit. Verify whether the exact edition and individual clause govern the selected type/installation; standards availability does not guarantee unrestricted full-text access, and a connector dimensional standard alone does not supply dynamic thermal equations.

## 8. Next scientific decision and thesis transfer

1. Identify the **actual** transformer (oil-immersed vs dry, kVA, cooling system) and actual EVSE/vehicle/battery architecture. Never combine incompatible examples (e.g. Hilshey 25 kVA transformer with a nominal 50 kW charger as one presumed installation).
2. Admit only candidate thermal quantities affecting critical transition times, an actual permitted-power rule, energy delivery, electricity service or mobility readiness; distinguish operating restrictions from internal physical states.
3. Establish I2 and I3 separately with source, receiver, physical interface quantity, mechanism, response time and evidence.
4. Numerically verify physically justified M0/M1/M2 matched comparisons and independently validate the necessary state and power trajectories, or report blocked validation.
5. Preserve the resilience definition at **required service through time**, and evaluate downstream environmental/economic/social sustainability consequences through the two canonical pathways only when indicator data support them.

**Decisive OPEN gate:** transformer thermal-state → operator/manufacturer/standard-qualified permissible supply power, and EVSE thermal state → measured input-power response. This file supplies candidate inventory, not proof of either directional thermal interdependency.
