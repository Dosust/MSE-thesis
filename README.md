# Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Canonical title authority:** [`project/CANONICAL_THESIS_TITLE_V1.md`](project/CANONICAL_THESIS_TITLE_V1.md)  
**Current-scope authority:** [`project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md`](project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md)  
**Thermal-interdependency scope authority:** [`project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`](project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)  
**Canonical resilience authority:** [`project/CANONICAL_RESILIENCE_DEFINITION_V1.md`](project/CANONICAL_RESILIENCE_DEFINITION_V1.md)  
**Current objective authority:** [`project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`](project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)  
**Current conceptual framework:** [`project/CONCEPTUAL_FRAMEWORK_SPEC_V4_THERMAL.md`](project/CONCEPTUAL_FRAMEWORK_SPEC_V4_THERMAL.md)  
**Current mathematical framework:** [`project/MATHEMATICAL_FRAMEWORK_SPEC_V2_THERMAL.md`](project/MATHEMATICAL_FRAMEWORK_SPEC_V2_THERMAL.md)  
**Electrified Transportation scope authority:** [`project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`](project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md)  
**Current authority index:** [`project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`](project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md)  
**Current direction date:** 2026-10-07

> **Repository rule:** current work, historical work, and superseded work remain distinguishable. Earlier whole versions are preserved for provenance and are not deleted when scope changes.

> **Scientific rule:** no scope decision, model, simulation, figure, or repository status may be interpreted as empirical support unless the corresponding evidence, validation, and test gates pass.

---

## Current thesis direction

The active thesis workstream is centered **only on thermal interdependencies between the Power System and Electrified Transportation System and on their consequences through state and time**.

```text
Extreme heat
→ thermal physical state
→ thermal capability / constraint
→ Power ↔ Electrified Transportation thermal interdependency
→ state-time consequence
→ electricity + mobility service consequence
→ resilience interpretation

Supporting engineering response, when analyzed:
Improve → Adapt → Restore
```

### Active physical scope

```text
Power System P
↔
Electrified Transportation System T_e
```

Power and Electrified Transportation remain distinct coupled physical systems. The thesis does not study all interdependencies between them. Power-transfer, charging, communication/control, and bidirectional-transfer quantities are included only when required to represent a **thermal interdependency or its state-time consequence**. Interface/coupling variables do not create a third physical infrastructure system.

### Canonical Electrified Transportation System scope

> **In this thesis, the electrified transportation system comprises the electrically propelled road vehicle, its rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, the vehicle power-supply circuit, electric-vehicle supply equipment, the physical charging connection, and the communication and control functions required for electrical power transfer, including bidirectional transfer where supported (ISO 6469; ISO 5474; ISO 15118; IEC 61851; IEC 62196).**

Status: **FROZEN — CANONICAL**.

The standards justify the technical composition and boundary. The system name is simply **Electrified Transportation System**.

### Canonical thermal-interdependency focus

The thesis studies **thermal interdependencies only**.

A thermal interdependency is a qualified directional Power–Electrified Transportation dependency in which a heat- or temperature-dependent physical state, thermal capability, or thermally conditioned operating limit changes the physical or functional capability of the coupled system or changes electricity or mobility service over time.

Non-thermal Power–Transportation interdependencies are outside the active research scope except as supporting boundary conditions, coupling variables, or constraints needed to represent a thermal mechanism.

Primary analytical dimensions:

```text
state + time
```

### Current bounded application subset

```text
electrically propelled road vehicle
→ battery-electric road-transport application
→ grid-connected charging context
```

Status: **WORKING-FROZEN**.

Exact charging context remains **OPEN**:

```text
public DC fast charging
vs
fleet/depot charging
```

---

## State-time mathematical spine

```math
H(t)
\rightarrow
X_{th}(t)
\rightarrow
Z_{PT}(t)
\rightarrow
\{\tau_{th}^C,\delta_{th},Q_P(t),Q_T(t)\}.
```

with

```math
X_{th}(t)=[X_{P,th}^\top,X_{T_e,th}^\top]^\top.
```

Where:

- `H(t)` = extreme-heat forcing;
- `X_{P,th}(t)` = Power-system thermal states required by the model;
- `X_{T_e,th}(t)` = Electrified Transportation thermal states required by the model;
- `Z_{PT}(t)` = coupling quantities and conditions required to represent the thermal interdependency; this is not a third physical system;
- `τ_{th}^C` = critical thermal transition time;
- `δ_{th}` = thermal-interdependency propagation timing;
- `Q_P(t)` = electricity-service trajectory;
- `Q_T(t)` = mobility-service trajectory.

Permanent distinctions:

```text
external heat forcing ≠ thermal state
common heat exposure ≠ thermal interdependency
thermal exposure ≠ thermal interdependency
system-scope membership ≠ active model state
state ≠ function ≠ service
transition time ≠ propagation time ≠ recovery time
physical degradation ≠ service criticality
simulation ≠ validation
```

---

## Physics-based mathematical engineering

Physics-based mathematical engineering is the **method**, not the outcome.

```text
physical mechanism
→ governing state equation
→ constraint / threshold
→ state-time trajectory
→ service consequence
→ engineering action
```

General coupled representation:

```math
\dot X=F(X,H,u;\theta).
```

Components and interfaces retain domain-specific physics:

```math
\dot X_i=f_i(X_i,H,L_i,Z_{ji},u_i;\theta_i).
```

The governing rule is **minimum sufficient physics**: include only the physical fidelity needed to change a threshold, service prediction, intervention evaluation, or engineering decision.

---

## Canonical resilience definition

> **Resilience is the ability of the coupled Power and Electrified Transportation systems to maintain or recover required electricity and mobility services as thermal states and thermal interdependencies evolve over time.**

Resilience is not component survival. It is evaluated at the **service level through time**.

```text
Extreme Heat
→ Thermal State Change
→ Capability Change
→ Thermal Interdependency
→ Service Degradation
→ Resilience Response
```

Service conditions are:

```math
Q_P(t) \ge Q_P^{req}(t),
\qquad
Q_T(t) \ge Q_T^{req}(t).
```

A service deficit occurs when:

```math
Q_k(t) < Q_k^{req}(t).
```

The central resilience question is:

> **Can required service be maintained, and if not, how quickly and effectively can it be recovered?**

Candidate state-time descriptors include minimum service level, service deficit, disruption duration, and recovery time.

Permanent distinction:

```text
Thermal State ≠ Capability ≠ Service ≠ Resilience
```

Improve, Adapt, and Restore are engineering response classes that support resilience analysis; they are not the definition of resilience itself.

## Supporting engineering-response boundary

Improve, Adapt, Restore, and Learn may be used only as **supporting interpretation or optional experiments** when they directly help explain a thermal state-time consequence. They are not primary research objectives.

The active thesis chain ends at quantified electricity and mobility service consequences.

---

## Current decision state

| Research object | Status |
|---|---|
| thesis title | **FROZEN** |
| physical core: Power + Transportation | **FROZEN** |
| Electrified Transportation System composition/boundary | **FROZEN — CANONICAL** |
| active hazard: extreme heat | **FROZEN — CURRENT** |
| thermal interdependencies only | **FROZEN — CANONICAL** |
| state-time analytical focus | **FROZEN — CANONICAL** |
| battery-electric road transportation as application subset | **WORKING-FROZEN** |
| grid-connected EV charging mechanism | **WORKING-FROZEN** |
| resilience definition | **FROZEN — CANONICAL SERVICE-LEVEL STATE-TIME DEFINITION** |
| Improve → Adapt → Restore | **SUPPORTING ENGINEERING RESPONSE CLASSES** |
| exact charging context | **OPEN** |
| exact component/interface states | **OPEN** |
| exact electricity/mobility service metrics | **OPEN** |
| exact intervention set | **OPEN — optional/supporting, thermal only** |
| general + specific objectives | **FROZEN — GO + SO1–SO3** |
| final RQ wording | **OPEN — thermal/state-time only** |
| hypotheses | **OPEN — thermal/state-time only** |
| final novelty claim | **OPEN** |

---

## Current framework and decision authorities

| File | Role |
|---|---|
| [`project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`](project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md) | canonical Electrified Transportation composition and boundary |
| [`project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`](project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md) | canonical thermal-interdependency focus |
| [`project/CANONICAL_RESILIENCE_DEFINITION_V1.md`](project/CANONICAL_RESILIENCE_DEFINITION_V1.md) | canonical service-level state-time resilience definition |
| [`project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md`](project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md) | current extreme-heat / thermal-interdependency / state-time scope precedence |
| [`project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`](project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md) | current authority entry point |
| [`project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md`](project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md) | decision closure / reopening |
| [`project/ROAD_VS_RAIL_SCOPE_GATE_DECISION_V1.md`](project/ROAD_VS_RAIL_SCOPE_GATE_DECISION_V1.md) | road-over-rail working decision |
| [`project/CONCEPTUAL_FRAMEWORK_SPEC_V4_THERMAL.md`](project/CONCEPTUAL_FRAMEWORK_SPEC_V4_THERMAL.md) | current thermal-only conceptual framework |
| [`project/WHY_LOG_2026-10-06.md`](project/WHY_LOG_2026-10-06.md) | rationale / rejected alternatives |
| [`project/RESEARCH_REASONING_PROTOCOL.md`](project/RESEARCH_REASONING_PROTOCOL.md) | reasoning / evidence discipline |
| [`project/EGMIV_METHOD_V1.md`](project/EGMIV_METHOD_V1.md) | evidence-grounded mechanism/model method |
| [`thesis/00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`](thesis/00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md) | claim / inference discipline |

---

## Current novelty boundary

The following are **not** novelty claims by themselves:

- coupling Power and Transportation;
- EV charging in coupled power–transportation networks;
- temperature-aware EV demand/charging;
- dynamic coupled-network restoration;
- V2G-supported resilience;
- physics-based modeling alone;
- Improve / Adapt / Restore wording alone.

The current candidate unresolved handoff is:

```text
explicit heat-dependent physical state/capability
→ time-varying coupled electricity + mobility service trajectories
→ measurable consequence for engineering decisions
```

Status: **candidate gap / contribution boundary only**. It remains subject to closest-literature and implementation-feasibility validation.

---

## Mathematical visualization and scientific diagram design

Scientific figures are governed by:

- [`.github/skills/engineering-framework-design/SKILL.md`](.github/skills/engineering-framework-design/SKILL.md)
- [`.github/skills/scientific-diagram-design/SKILL.md`](.github/skills/scientific-diagram-design/SKILL.md)
- [`.github/skills/mathematical-visualization-design/SKILL.md`](.github/skills/mathematical-visualization-design/SKILL.md)

Permanent rule:

```text
formal model
→ declared visual encoding
→ rendering
→ verification
```

A color, icon, arrow, shape, position, or motion with no scientific mapping is decoration and should be removed.

---

## Historical architecture retained whole

The September 2026 seven-stage / RQ-SO-H / P2-P3 / Austin / broad P+T+I+O packages are **retained for provenance and reusable methods**. They no longer control the active reader-facing scope where they conflict with the 2026-10-06 scope amendment.

Exact pre-reconciliation entry points are preserved under:

[`archive/readme_versions/2026-10-06_pre_reconciliation/`](archive/readme_versions/2026-10-06_pre_reconciliation/)

No historical scientific work was deleted.

---

## Current next work

```text
freeze final thermal RQ wording
→ freeze exact thermal states and coupling quantities
→ freeze thermal thresholds and electricity/mobility service metrics
→ qualify directional thermal mechanisms
→ implement minimum-sufficient thermal physics
→ VVUQ
→ execute only after evidence/data/model gates pass
```
