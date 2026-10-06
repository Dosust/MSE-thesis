# Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Canonical title authority:** [`project/CANONICAL_THESIS_TITLE_V1.md`](project/CANONICAL_THESIS_TITLE_V1.md)  
**Current-scope authority:** [`project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md`](project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md)  
**Current authority index:** [`project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`](project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md)  
**Current direction date:** 2026-10-06

> **Repository rule:** current work, historical work, and superseded work remain distinguishable. Earlier whole versions are preserved for provenance and are not deleted when scope changes.

> **Scientific rule:** no scope decision, model, simulation, figure, or repository status may be interpreted as empirical support unless the corresponding evidence, validation, and test gates pass.

---

## Current thesis direction

The active thesis workstream is now centered on **extreme-heat consequences in coupled Power–Electrified Transportation systems**, with **physical state and time** as the primary analytical variables.

```text
Extreme heat
→ selected physical states
→ state-time evolution
→ critical transition timing
→ interface-mediated propagation timing
→ electricity + mobility service consequence
→ Improve / Adapt / Restore
→ Learn
```

### Active physical scope

```text
Power System P
↔
Physical Power–Transport Interfaces I_PT
↔
Electrified Transportation T
```

### Active transportation mode

```text
Road transport
→ battery-electric road transportation
→ grid-connected EV charging
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
H(x,t)
\rightarrow
X(t)
\rightarrow
\{\tau_i^C,\delta_{ij},Q_P(t),Q_T(t)\}
\rightarrow
\{\text{Improve},\text{Adapt},\text{Restore}\}.
```

with

```math
X(t)=[X_P^\top,Z^\top,X_T^\top]^\top.
```

Where:

- `H(x,t)` = extreme-heat forcing;
- `X_P(t)` = selected Power-system states;
- `Z(t)` = selected interface states;
- `X_T(t)` = selected battery-electric transportation states;
- `τ_i^C` = critical transition time;
- `δ_ij` = propagation delay between defined events;
- `Q_P(t)` = electricity-service trajectory;
- `Q_T(t)` = mobility-service trajectory.

Permanent distinctions:

```text
external forcing ≠ system state
common heat exposure ≠ Power–Transportation interdependency
interface architecture ≠ interface state
state ≠ function ≠ service
transition time ≠ propagation delay ≠ recovery time
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

Selected components/interfaces retain domain-specific physics:

```math
\dot X_i=f_i(X_i,H,L_i,Z_{ji},u_i;\theta_i).
```

The governing rule is **minimum sufficient physics**: include only the physical fidelity needed to change a threshold, service prediction, intervention evaluation, or engineering decision.

---

## Engineering resilience cycle

The thesis-defined engineering cycle is:

```text
Improve → Adapt → Restore → Learn → Improve
```

- **Improve:** change baseline design/parameters before a future event.
- **Adapt:** change operation while the heat event and states evolve.
- **Restore:** recover acceptable function/service after unacceptable degradation.
- **Learn:** use event evidence, validation, intervention performance, and recovery to improve future models and decisions.

This is a thesis-specific engineering architecture, not a claim of a universal resilience definition.

---

## Current decision state

| Research object | Status |
|---|---|
| thesis title | **FROZEN** |
| physical core: Power + Transportation | **FROZEN** |
| active hazard: extreme heat | **WORKING-FROZEN / CURRENT** |
| battery-electric road transportation | **WORKING-FROZEN** |
| grid-connected EV charging mechanism | **WORKING-FROZEN** |
| state-time analytical focus | **WORKING-FROZEN / CURRENT** |
| Improve → Adapt → Restore → Learn | **WORKING-FROZEN / CURRENT** |
| exact charging context | **OPEN** |
| exact component/interface states | **OPEN** |
| exact electricity/mobility service metrics | **OPEN** |
| exact intervention set | **OPEN** |
| final narrowed RQ/SO/H | **OPEN** |
| final novelty claim | **OPEN** |

---

## Current framework and decision authorities

| File | Role |
|---|---|
| [`project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md`](project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md) | current scope precedence |
| [`project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`](project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md) | current authority entry point |
| [`project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md`](project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md) | decision closure / reopening |
| [`project/ROAD_VS_RAIL_SCOPE_GATE_DECISION_V1.md`](project/ROAD_VS_RAIL_SCOPE_GATE_DECISION_V1.md) | road-over-rail working decision |
| [`project/CONCEPTUAL_FRAMEWORK_SPEC_V2.md`](project/CONCEPTUAL_FRAMEWORK_SPEC_V2.md) | current conceptual-framework specification |
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
freeze exact charging context
→ freeze selected physical state variables
→ freeze service variables
→ rewrite/freeze narrowed RQ / objectives / hypotheses
→ finalize conceptual + mathematical framework
→ define minimum-sufficient physics
→ define matched baselines
→ VVUQ
→ execute only after data/model gates pass
```
