# Conceptual Framework Specification V3

**Status:** CURRENT WORKING-FROZEN CONCEPTUAL SPECIFICATION  
**Date:** 2026-10-07  
**Supersedes for active conceptual-figure work:** \`CONCEPTUAL_FRAMEWORK_SPEC_V2.md\`  
**Scope authorities:** \`CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md\` + \`CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md\` + \`CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md\`

## 1. Purpose

Show the global scientific logic of the thesis without mathematical notation and without drifting into methodology.

The conceptual framework answers:

> How do thermal interdependencies between the Power System and Electrified Transportation System evolve through state and time, what service consequences result, and how can resilience responses change those consequences?

It does not answer:

> How will data be processed, parameters calibrated, simulations executed, or uncertainty quantified?

Those belong to methodology.

## 2. No-mathematics rule

The visible conceptual framework must contain:
- no equations;
- no variables;
- no Greek symbols;
- no state-vector notation;
- no numerical algorithm;
- no calibration/estimation workflow;
- no VVUQ workflow.

Words may still express the concepts of state, time, propagation, service, resilience, sustainability, and SDG relevance.

## 3. Global conceptual chain

\`\`\`text
External Environment — Extreme Heat Forcing
                ↓
         Thermal Physical State
                ↓
      Thermal Capability / Constraint
                ↓
Power System ↔ Electrified Transportation System
       Thermal Interdependency
                ↓
       State-Time Consequence
                ↓
        Service Consequences
 Electricity Service + Mobility Service
                ↓
        Engineering Response
      Improve | Adapt | Restore
                ↓
        Resilience Outcome
                ↓
   Bounded Sustainability Consequences
\`\`\`

## 4. Scientific meaning of each phase

### Extreme Heat
External physical forcing. It may change thermal states in the Power System and Electrified Transportation System. Common heat exposure is not itself a thermal interdependency.

### Physical System of Interest
Current scope:
- Power System;
- Electrified Transportation System.

The Electrified Transportation System comprises the electrically propelled road vehicle, rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, vehicle power-supply circuit, EVSE, physical charging connection, and the communication/control functions required for electrical power transfer, including bidirectional transfer where supported.

Power-transfer, charging, communication/control, and bidirectional-transfer relations are represented only when they are required to express a thermal interdependency or its consequence. They are not drawn as a third physical infrastructure system.

A battery-electric road-transport or fleet/depot case remains a bounded application subset and does not redefine the thesis-wide system composition.

### Thermal Physical State
The temperature-dependent physical states required to explain the thermal mechanism.

### Thermal Capability / Constraint
How thermal state changes capability, limits, or operating feasibility.

### Thermal Interdependency
How a qualified directional thermal mechanism in one coupled system changes the physical or functional capability of the other system or changes service over time.

### State-Time Consequence
How the thermal interdependency changes state trajectories, critical transitions, propagation timing, and service trajectories.

### Service Consequences
Consequences for:
- electricity service;
- mobility service.

### Engineering Response
Three distinct response classes:
- Improve;
- Adapt;
- Restore.

### Resilience Outcome
Whether acceptable electricity and mobility service can be maintained or recovered, including disruption duration and recovery performance.

### Bounded Sustainability Consequences
Evaluate only sustainability consequences that arise from the bounded resilience interventions and are supported by declared data and accounting boundaries. Candidate dimensions may include:

#### Social
Candidate constructs:
- access;
- safety;
- equity;
- service availability.

#### Environmental
Candidate constructs:
- energy use;
- emissions;
- resource use;
- environmental/heat burden.

#### Economic
Candidate constructs:
- intervention cost;
- service-loss cost;
- recovery cost;
- productivity consequence.

These are candidate constructs until operational indicators are frozen.

Do not interpret resilience improvement as automatic sustainability improvement. Sustainability remains a bounded consequence assessment, not a second broad thesis domain.

## 5. Arrow semantics

- hazard forcing → thermal state: external heat forcing;
- thermal state → capability/constraint: thermophysical consequence;
- Power ↔ Electrified Transportation arrow: qualified thermal interdependency only;
- downward arrows: state-time consequence or service consequence;
- Engineering Response → Resilience Outcome: effect of Improve / Adapt / Restore;
- Resilience Outcome → Bounded Sustainability Consequences: consequence assessment only, not automatic causality.

No arrow may exist merely to make the composition look connected.

## 6. Color semantics

- authentic red: extreme heat/external hazard only;
- green: physical infrastructure and physical exchange/dependency;
- blue: state-time/service, resilience, sustainability assessment;
- black: neutral scientific text/combined outcome;
- engineering response: black or ASU maroon when specifically requested;
- all backgrounds and panel interiors: pure white \`#FFFFFF\`.

No gradient, shadow, gray fill, cream fill, or paper effect.

## 7. Exit gate

The conceptual framework is ready for canonical freeze only when:
- every arrow has a defined scientific meaning;
- all visible terms belong to the current scope;
- no methodology step is embedded;
- no mathematics appears;
- thermal interdependency is explicit and non-thermal interdependencies are excluded from the active figure;
- sustainability remains bounded to consequences of the resilience interventions;
- the figure passes grayscale and semantic QA.
