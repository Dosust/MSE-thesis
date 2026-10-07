## 1.6 Scope, Boundaries, Assumptions, and Validity Domain

The active thesis scope is controlled by:

- `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`;
- `project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`;
- `project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`;
- `project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`;
- `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`;
- `project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`;
- `project/CANONICAL_EFFECTIVENESS_ENERGY_EFFICIENCY_PLACEMENT_V1.md`.

| Boundary | Included | Outside active analytical scope |
|---|---|---|
| Physical systems | Power System + Electrified Transportation System | Other infrastructure sectors |
| Hazard | Extreme heat | Flood, storm, earthquake, other hazards |
| Interdependency class | Thermal interdependencies only | Generic non-thermal P–T interdependencies |
| Analytical dimensions | Canonical state + time: evolving physical/operational states and timing of transitions/propagation/service consequences | Broad social/institutional dynamics |
| Active consequences | Electricity + mobility service | Economy-wide welfare/GDP modeling |
| Transportation application | Battery-electric road transport with grid-connected charging | All transportation modes |
| Modeling fidelity | Minimum sufficient thermal physics | Full component-detail modeling by default |
| Sustainability | Two bounded pathways: direct thermal/service consequences and engineering-response consequences, each across environmental, economic, and social dimensions | Broad sustainability optimization, full LCA/social LCA, economy-wide analysis, automatic scalar aggregation |
| Effectiveness | Resilience / engineering-response assessment | Sustainability dimension or energy-efficiency substitute |
| Energy efficiency | Environmental sustainability indicator when relevant and measurable | Resilience-effectiveness substitute |

A thermal interdependency is admitted only when temperature or thermal state changes the activation, magnitude, capacity, timing, or consequence of a directional cross-system dependency.

Common heat exposure is not sufficient:

```text
common heat exposure ≠ thermal interdependency
```

The Electrified Transportation System includes EVSE and the physical charging connection according to the canonical system-boundary definition. System-scope membership does not require equal model fidelity for every component.

State/time semantics are controlled by `project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`. SOC is an operational/energy state rather than a thermal state. Aging/degradation may be a legitimate slow state, but it is activated only when its evolution over the declared horizon materially changes the admitted thermal mechanism or consequence. External heat is forcing, capability is generally derived from state, and electricity/mobility service remains an output rather than a physical state.

Sustainability comparison must preserve the same indicator definition, unit, accounting boundary, and time horizon across the reference, extreme-heat, and engineering-response cases. Exact indicators, functional unit, and SDG targets remain OPEN until operationalized.

The SDG interpretation rule is:

```text
Measured Sustainability Indicator
→ Sustainability Dimension
→ Relevant SDG Target / Indicator
```

The canonical state-time rules are:

```text
external forcing ≠ system state
physical quantity ≠ state variable ≠ active thesis state
thermal state ≠ operational/energy state
state ≠ capability ≠ service
```

Exact active state variables remain OPEN until qualified by the application case, mechanism evidence, and minimum-sufficient-physics rule.

The principal temporal quantities are distinct:

```text
critical transition time ≠ propagation delay ≠ service-consequence time ≠ recovery time
```

All claims are restricted to the mechanisms, components, parameter ranges, heat conditions, observations, service definitions, and validation evidence actually examined.

The governing inference rule remains:

```math
\boxed{\operatorname{Strength}(\text{claim})\le\operatorname{Strength}(\text{supporting evidence}).}
```
