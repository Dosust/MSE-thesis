# Architecture Methods

**Role:** software QA and numerical scaffolds only.

## Current scientific authority

The active thesis does **not** use the historical P–T–I–O seven-stage architecture as its research scope.

Load these authorities first:

- [Thermal interdependency scope](../../project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)
- [Extreme-heat thermal state-time amendment](../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md)
- [Canonical state-time definitions](../../project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md)
- [Thermal objectives](../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)
- [Electrified Transportation boundary](../../project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md)
- [Thermal/resilience/sustainability conceptual framework](../../project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md)
- [Thermal/resilience/sustainability mathematical framework](../../project/MATHEMATICAL_FRAMEWORK_SPEC_V3_THERMAL_SUSTAINABILITY.md)

## Active scientific chain

```text
Extreme heat
→ thermal physical state
→ thermal capability / constraint
→ qualified thermal P ↔ T_e interdependency
→ state-time evolution
→ transition / propagation timing
→ electricity + mobility service consequence
```

## Legacy code and models

Files such as `CoupledInfrastructure.jl`, `viability_geometry.py`, historical P–T–I–O examples, Stage-1–7 objects, old hypothesis registries, and generic viability/sustainability utilities remain available for software testing and provenance.

They are **not active thesis evidence** and may not be used to redefine the current thermal-only scope.

## State-admission rule

Before a variable is implemented as an active state, verify:

```text
legitimate state under adopted physics
+ current value needed for subsequent evolution
+ participation in qualified thermal mechanism
+ material effect over declared horizon
+ sufficient observability/estimability/evidence
```

`SOC` may be an energy state; aging may be a slow degradation state; a coupling quantity is not a state unless independent dynamics require it.

## Implementation admission gate

Before any code becomes part of the active thesis:

1. it must represent a qualified thermal mechanism;
2. its variables must map to thermally active states/coupling quantities;
3. units and thresholds must be explicit;
4. numerical verification must pass;
5. validation evidence must be declared;
6. uncertainty and validity limits must be reported.

## Governing rule

```text
legacy scaffold
≠
active thermal model
≠
validated scientific result
```
