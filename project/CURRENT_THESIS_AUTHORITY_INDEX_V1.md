# Current Thesis Authority Index V1

**Effective date:** 2026-10-07  
**Purpose:** single current entry point for humans and AI systems.

## Load first

1. `project/CANONICAL_THESIS_TITLE_V1.md`
2. `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`
3. `project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`
4. `project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`
5. `project/CANONICAL_RESILIENCE_DEFINITION_V1.md`
6. `project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`
7. `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`
8. `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1_1_SUSTAINABILITY_ALIGNMENT.md`
9. `project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md`
10. `project/MATHEMATICAL_FRAMEWORK_SPEC_V3_THERMAL_SUSTAINABILITY.md`
11. `project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md`
12. `project/RESEARCH_REASONING_PROTOCOL.md`
13. `project/EGMIV_METHOD_V1.md`
14. `thesis/00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`

## Current status matrix

| Object | Status |
|---|---|
| thesis title | **FROZEN** |
| physical core P+T | **FROZEN** |
| Electrified Transportation System composition/boundary | **FROZEN — CANONICAL** |
| active hazard: extreme heat | **FROZEN — CURRENT** |
| active interdependency class: thermal interdependencies only | **FROZEN — CANONICAL** |
| state-time analytical focus | **FROZEN — CANONICAL** |
| battery-electric road transport as bounded application subset | **WORKING-FROZEN** |
| grid-connected EV charging context | **WORKING-FROZEN** |
| resilience definition | **FROZEN — CANONICAL SERVICE-LEVEL STATE-TIME DEFINITION** |
| Improve → Adapt → Restore | **SUPPORTING ENGINEERING RESPONSE CLASSES** |
| exact charging context | **OPEN** |
| exact state variables | **OPEN** |
| exact service metrics | **OPEN** |
| exact intervention set | **OPEN — optional/supporting, thermal only** |
| general + specific objectives | **FROZEN — 3-objective thermal contract** |
| final narrowed RQ wording | **OPEN — must remain thermal/state-time only** |
| hypotheses | **OPEN — must remain thermal/state-time only** |
| final novelty claim | **OPEN** |
| September seven-stage/RQ-H/P3/Austin packages | **HISTORICAL / RETAINED** |

## Current framework authorities

- `project/CONCEPTUAL_FRAMEWORK_SPEC_V4_THERMAL.md` — current thermal-only conceptual framework.
- `project/MATHEMATICAL_FRAMEWORK_SPEC_V2_THERMAL.md` — current thermal-only mathematical framework.
- `project/CANONICAL_RESILIENCE_DEFINITION_V1.md` — frozen service-level state-time definition of resilience.
- `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md` — frozen general objective + SO1–SO3.
- Older seven-stage, V4 RQ/SO/H, broad P–T–I–O, sustainability, and decision packages are historical/provenance where they conflict with the thermal-only scope.

## Current visualization authorities

- `.github/skills/engineering-framework-design/SKILL.md`
- `.github/skills/scientific-diagram-design/SKILL.md`
- `.github/skills/mathematical-visualization-design/SKILL.md`

Permanent visualization rule:

```text
formal model
→ declared visual encoding
→ rendering
→ verification
```

## Legacy-use rule

Legacy files may be cited or reused for methodology and provenance, but must not silently override the current scope amendment.


## Electrified Transportation scope authority — 2026-10-07

For composition, terminology, and the technical boundary of the Electrified Transportation System, use `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`.

The standards justify the technical composition; the system name remains **Electrified Transportation System**. Battery-electric road transport, bus/fleet, or a specific charging context may be bounded application subsets but do not redefine the canonical system scope.




## Thermal-interdependency focus authority — 2026-10-07

The controlling active scope is:

- `project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`;
- `project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`.

The thesis studies **thermal interdependencies only** between the Power System and Electrified Transportation System and their consequences through **physical state and time**. Non-thermal interdependencies are outside the active analytical scope except as boundary conditions, constraints, or supporting variables strictly required to represent a thermal mechanism.

The active general objective and three specific objectives are controlled by `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`.


## Canonical resilience authority — 2026-10-07

For every use of **resilience** in active thesis work, use `project/CANONICAL_RESILIENCE_DEFINITION_V1.md`.

Canonical definition:

> **Resilience is the ability of the coupled Power and Electrified Transportation systems to maintain or recover required electricity and mobility services as thermal states and thermal interdependencies evolve over time.**

Resilience is evaluated at the **service level through time**. Component survival, reliability alone, robustness alone, or recovery time alone must not be substituted for resilience. Improve, Adapt, and Restore are engineering response classes that support resilience analysis; they are not the definition of resilience itself.
