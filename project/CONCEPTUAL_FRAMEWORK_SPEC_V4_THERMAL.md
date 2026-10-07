# Conceptual Framework Specification V4 — Thermal Interdependency State-Time Focus

**Status:** SUPERSEDED FOR ACTIVE CONCEPTUAL WORK — RETAINED FOR PROVENANCE  
**Effective date:** 2026-10-07  
**Scope authorities:** `CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md` + `CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md`  
**Objective authority:** `CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`  
**Resilience authority:** `CANONICAL_RESILIENCE_DEFINITION_V1.md`  
**System-boundary authority:** `CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`  
**Superseded by:** `CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md`  
**Previously superseded:** `CONCEPTUAL_FRAMEWORK_SPEC_V3.md`

## 1. Purpose

Represent only the active thesis problem:

> **thermal interdependencies between the Power System and the Electrified Transportation System, and their consequences through physical state and time.**

The conceptual framework must not reintroduce non-thermal interdependency families, broad organizational/information architectures, generic sustainability assessment, or multiobjective decision logic.

## 2. Canonical conceptual chain

```text
Extreme Heat Forcing
        ↓
Thermal / Temperature-Dependent Physical States
   Power System P        Electrified Transportation T_e
        ↘                    ↙
      Qualified Thermal Interdependency
                 ↓
          State-Time Evolution
                 ↓
 Critical Transition + Propagation Timing
                 ↓
 Electricity-Service + Mobility-Service Consequences
                 ↓
         Resilience Interpretation
```

## 3. Scientific meaning

### Extreme heat forcing

Extreme heat is external forcing. It is not itself a system state and does not by itself establish interdependency.

### Thermal physical states

Only physical states whose temperature dependence matters to the cross-system mechanism are active.

Examples may include temperature-dependent capacity, derating, thermal limits, charging capability, energy-state consequences, or other thermally justified physical quantities.

### Qualified thermal interdependency

A cross-system relation is active only if temperature or thermal state changes its activation, magnitude, capacity, timing, or consequence.

```text
common heat exposure ≠ thermal interdependency
connection ≠ dependency
```

### State-time evolution

The thesis follows how thermally relevant states change through time and how a qualified cross-system consequence propagates.

### Critical transition and propagation timing

Two different temporal objects are preserved:

```text
critical transition time ≠ interdependency propagation delay
```

### Service consequences

The final active consequences are:
- electricity service;
- mobility service.

Physical-state change is not automatically service loss.

### Resilience interpretation

> **Resilience is the ability of the coupled Power and Electrified Transportation systems to maintain or recover required electricity and mobility services as thermal states and thermal interdependencies evolve over time.**

Resilience is evaluated at the service level through time. It is not component survival.

The conceptual distinction is:

```text
Thermal State ≠ Capability ≠ Service ≠ Resilience
```

The resilience question is:

> **Can required service be maintained, and if not, how quickly and effectively can it be recovered?**

Improve, Adapt, and Restore may be used as engineering response classes when needed, but they do not define resilience.

## 4. Directional pathways

### Power → Electrified Transportation

```text
Power thermal state / temperature-dependent capability
→ electrical capability available to T_e
→ charging capability
→ vehicle energy state / availability
→ mobility consequence
```

### Electrified Transportation → Power

```text
T_e thermal state / temperature-dependent charging or transfer capability
→ electrical demand or supported reverse transfer
→ Power-system state/capability consequence
```

Only evidence-qualified pathways are retained.

## 5. Electrified Transportation boundary

The Electrified Transportation System includes the canonical components defined in `CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`, including EVSE.

System-scope membership does not require detailed modeling of every component.

## 6. Explicit exclusions from the conceptual figure

Do not include as active causal layers:
- generic Information;
- generic Organization;
- repair-crew logistics;
- non-thermal restoration dependencies;
- flooding or other hazards;
- broad sustainability dimensions;
- SDGs;
- economic-development modeling;
- generic intervention portfolios;
- multiobjective engineering decision stages.

These may appear in literature context or future work, not in the active conceptual framework.

## 7. Visual rule

The active figure should contain only:

```text
Heat
→ thermal state
→ thermal interdependency
→ state-time propagation
→ service consequence
→ resilience interpretation
```

Every arrow must correspond to a physically interpretable relation.
