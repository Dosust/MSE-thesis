# Conceptual Framework Specification V3

**Status:** CURRENT WORKING-FROZEN CONCEPTUAL SPECIFICATION  
**Date:** 2026-10-06  
**Supersedes for active conceptual-figure work:** \`CONCEPTUAL_FRAMEWORK_SPEC_V2.md\`  
**Scope authorities:** \`CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md\` + \`CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V2.md\`

## 1. Purpose

Show the global scientific logic of the thesis without mathematical notation and without drifting into methodology.

The conceptual framework answers:

> What happens in the system, what are the main scientific relationships, and how can resilience responses lead to sustainable and resilient outcomes?

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
      Physical System of Interest
Power System ↔ Electrified Transportation System
                ↓
         State-Time Response
                ↓
     Interdependency Propagation
                ↓
        Service Consequences
 Electricity Service + Mobility Service
                ↓
        Engineering Response
      Improve | Adapt | Restore
           ↙             ↘
 Resilience Outcome   Sustainability Impacts
                       Social
                       Environmental
                       Economic
           ↘             ↙
    Sustainable and Resilient Outcome
                ↓
       SDG Relevance / Alignment
\`\`\`

## 4. Scientific meaning of each phase

### Extreme Heat
External physical forcing. It may affect relevant Power-system states and relevant components of the Electrified Transportation System. Common heat exposure is not itself an interdependency.

### Physical System of Interest
Current scope:
- Power System;
- Electrified Transportation System.

The Electrified Transportation System comprises the electrically propelled road vehicle, rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, vehicle power-supply circuit, EVSE, physical charging connection, and the communication/control functions required for electrical power transfer, including bidirectional transfer where supported.

Power-transfer, charging, communication/control, and bidirectional-transfer relations are represented as interdependencies/coupling conditions between the two physical systems; they are not drawn as a third physical infrastructure system.

A battery-electric road-transport or fleet/depot case remains a bounded application subset and does not redefine the thesis-wide system composition.

### State-Time Response
How physical conditions evolve over time under heat.

### Interdependency Propagation
How a physically qualified change in one subsystem/interface influences another through an admitted dependency.

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

### Sustainability Impacts
Evaluate the consequences of both the resilience outcome and the intervention burden through three dimensions:

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

### Sustainable and Resilient Outcome
A system outcome is not called sustainable merely because it is resilient. The final interpretation requires both:
- acceptable resilience/service performance;
- acceptable social, environmental, and economic consequences.

### SDG Relevance / Alignment
SDGs are an interpretation layer, not a causal system layer.

Do not draw:
\`\`\`text
Social → SDG 3
\`\`\`
as an automatic causal claim.

Use:
\`\`\`text
measured sustainability indicator
→ relevant SDG target/indicator
\`\`\`

after the indicator mapping is evidence-supported.

## 5. Arrow semantics

- hazard forcing → subsystem: external physical forcing;
- solid physical arrow: delivered physical capability/energy;
- dashed physical arrow: demand/dependency imposed on another subsystem;
- downward conceptual arrows: consequence / conceptual progression;
- branch from Engineering Response: decomposition into resilience outcome and sustainability impacts;
- convergence into Sustainable and Resilient Outcome: joint interpretation;
- SDG arrow: policy-facing relevance/alignment only.

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
- sustainability dimensions are clearly visible;
- SDG language is relevance/alignment rather than unsupported causal mapping;
- the figure passes grayscale and semantic QA.
