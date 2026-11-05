# Engineering of Power–Electrified Transportation Interdependencies for Resilience

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**AI research entry point:** [`AI_RESEARCH_INSTRUCTIONS.md`](AI_RESEARCH_INSTRUCTIONS.md)  
**Canonical title authority:** [`project/CANONICAL_THESIS_TITLE_V3.md`](project/CANONICAL_THESIS_TITLE_V3.md)  
**Current-scope authority:** [`project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`](project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md)  
**Canonical state-time authority:** [`project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`](project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md)  
**Evidence / non-invention authority:** [`project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`](project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md)  
**Thermal-interdependency scope authority:** [`project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`](project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)  
**Canonical resilience authority:** [`project/CANONICAL_RESILIENCE_DEFINITION_V1.md`](project/CANONICAL_RESILIENCE_DEFINITION_V1.md)  
**Canonical sustainability authority:** [`project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`](project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md)  
**Effectiveness / energy-efficiency authority:** [`project/CANONICAL_EFFECTIVENESS_ENERGY_EFFICIENCY_PLACEMENT_V1.md`](project/CANONICAL_EFFECTIVENESS_ENERGY_EFFICIENCY_PLACEMENT_V1.md)  
**Current objective authority:** [`project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`](project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)  
**Current conceptual framework:** [`project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md`](project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md)  
**Current mathematical framework:** [`project/MATHEMATICAL_FRAMEWORK_SPEC_V3_THERMAL_SUSTAINABILITY.md`](project/MATHEMATICAL_FRAMEWORK_SPEC_V3_THERMAL_SUSTAINABILITY.md)  
**Electrified Transportation scope authority:** [`project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`](project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md)  
**Current authority index:** [`project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`](project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md)  
**Current direction date:** 2026-10-08

> **Repository rule:** current work, historical work, and superseded work remain distinguishable. Earlier whole versions are preserved for provenance and are not deleted when scope changes.

> **Scientific rule:** no scope decision, model, simulation, figure, or repository status may be interpreted as empirical support unless the corresponding evidence, validation, and test gates pass.

---

## Evidence and non-invention rule

```text
If it cannot be traced, it is not frozen.
If it cannot be verified, it remains open.
If it is thesis-derived, it is labeled thesis-derived.
If it is transferred, transferability must be justified.
```

No bibliographic record, standard requirement, equation, threshold, parameter, material property, capability law, or numerical result may be invented to fill an evidence gap.

## Canonical state-time meaning

State/time semantics are frozen in [`project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`](project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md).

> **State in this thesis refers to the minimum set of evolving physical, operational, energy, or degradation variables required to characterize the current modeled condition of the Power System and Electrified Transportation System and to determine their subsequent evolution under extreme-heat forcing. Thermal states are primary; non-thermal states are included only when required to represent the thermal interdependency or its consequences.**

> **Time in this thesis is the independent variable through which those states evolve and through which critical thermal transitions, interdependency propagation, service consequences, and—where explicitly modeled—recovery and degradation are ordered and quantified.**

Short form:

```text
State: What modeled condition is the system in now, such that we can determine what happens next?
Time: When and how does that condition evolve, cross a meaningful boundary, propagate, and affect service?
State + Time: How thermally driven system conditions evolve and generate coupled consequences.
```

Permanent distinctions:

```text
full physical state space ≠ active reduced thesis state vector
external forcing ≠ internal state
SOC = energy state, not thermal state
aging/degradation can be a slow state, but is not automatically active
state ≠ capability ≠ service
coupling quantity ≠ state unless independent dynamics require it
transition time ≠ propagation delay ≠ service-consequence time ≠ recovery time ≠ aging/degradation horizon
```

## Active literature checkpoints — 2026-10-08

- Module 01, P01–P10: `project/module_01_transformer_thermal_state_physics/`; physics evidence audited at unequal depths; Power reduced model **NOT FROZEN**.
- Module 02, P11: `project/module_02_transformer_thermal_parameter_identification_state_estimation/MODULE_02_PAPER_AUDIT_P11_V1.md`; Souza et al. (2026), ambient-conditioned top-oil parameter identification, with explicit uncertainty/transfer limitations.
- Module 02, P12: Chen & Su (2013), DOI 10.1002/tee.21862; publisher-abstract-level evidence for Kalman HST estimation; equations/observability/quantitative metrics OPEN. See `project/module_02_transformer_thermal_parameter_identification_state_estimation/MODULE_02_PAPER_AUDIT_P12_V1.md`.
- Module 02, P13: Liu et al. (2024), DOI 10.1016/j.csite.2024.104444; **3.31 K HST surrogate-versus-CFD error** is distinct from **3.36–3.97°C measured winding-profile errors**. Audit: `project/module_02_transformer_thermal_parameter_identification_state_estimation/MODULE_02_PAPER_AUDIT_P13_V1.md`. Steady model, dynamic HST observability OPEN.
- Module 02 P14: Li et al. (2026), `10.1016/j.epsr.2026.113033`; transient sparse-sensor winding-field reconstruction with physical comparison at verification points, but **true global HST error and formal observability OPEN**. Audit: `project/module_02_transformer_thermal_parameter_identification_state_estimation/MODULE_02_PAPER_AUDIT_P14_V1.md`.
- [P14–P200 screening register](project/THERMAL_200_PAPER_EXECUTION_REGISTER_P14_P200_V1.md): **187 slots, 77 DOI first-pass candidates, 110 unfilled**; no claim of 187 complete audits.
- [Cross-module evidence decisions](project/THERMAL_200_PAPER_CROSS_MODULE_EVIDENCE_DECISIONS_V1.md): Module 02–20 source-bound findings, limitations, major model-admission barriers. **State estimate ≠ measured global HST ≠ thermal capability.**

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

Bounded sustainability assessment:
Pathway 1 — direct thermal/service consequence
Pathway 2 — engineering-response consequence
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

- `H(t)` = extreme-heat forcing; it is an external input, not a Power- or Electrified-Transportation-system state;
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

## Canonical two-pathway sustainability assessment

> **Sustainability in this thesis is assessed through two pathways: (1) the direct environmental, economic, and social consequences of thermal interdependencies on electricity and mobility services, and (2) the environmental, economic, and social consequences of engineering responses used to improve, adapt, or restore those services. Both pathways are evaluated within a declared system boundary and time horizon.**

The thesis uses **one sustainability framework with two pathways**.

### Pathway 1 — Direct consequence

```text
Extreme Heat
→ Thermal Interdependency
→ Electricity + Mobility Service Consequence
→ Environmental + Economic + Social Consequence
```

### Pathway 2 — Engineering-response consequence

```text
Improve / Adapt / Restore
→ Changed State / Capability / Service
→ Environmental + Economic + Social Consequence
```

The three sustainability dimensions are:

```text
Environmental
→ energy use
→ energy efficiency
→ electrical / conversion losses
→ GHG emissions
→ material / resource burden

Economic
→ operating cost
→ maintenance / replacement cost
→ intervention cost
→ service-disruption cost

Social
→ service access
→ service continuity
→ affordability
→ equity
→ safety
```

Only indicators that are relevant, measurable, and supported by the adopted boundary and data are activated.

The comparison architecture is:

```text
Reference / Baseline
→ Extreme Heat without Engineering Response
→ Extreme Heat with Engineering Response
```

Permanent SDG rule:

```text
Measured Sustainability Indicator
→ Sustainability Dimension
→ Relevant SDG Target / Indicator
```

Exact sustainability indicators, functional unit, accounting boundary, time horizon, and SDG targets remain OPEN until operationalized.

Permanent distinctions:

```text
Thermal State ≠ Capability ≠ Service ≠ Resilience ≠ Sustainability
Resilience improvement ≠ sustainability improvement
Direct sustainability consequence ≠ engineering-response sustainability consequence
Measured indicator ≠ sustainability dimension ≠ SDG target
```

## Effectiveness and energy-efficiency placement

```text
Effectiveness → Resilience / Engineering-Response Assessment
Energy Efficiency → Environmental Sustainability
```

**Effectiveness** asks whether Improve, Adapt, or Restore actually maintains or recovers required electricity and mobility services.

**Energy efficiency** asks how much useful electricity or mobility service is delivered relative to the energy required to provide that service. It is an environmental-sustainability indicator when relevant and measurable.

```text
Effectiveness ≠ Energy Efficiency ≠ Sustainability
Effective Resilience Response ≠ Sustainable Response
```

## Supporting engineering-response boundary

Improve, Adapt, Restore, and Learn may be used only as **supporting interpretation or optional experiments** when they directly help explain a thermal state-time consequence. They are not primary research objectives.

The core thermal modeling chain ends at quantified electricity and mobility service consequences. Resilience is interpreted from those service trajectories, and the bounded two-pathway sustainability assessment follows as a downstream assessment where the required indicators and data are available.

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
| canonical state/time definitions | **FROZEN — CANONICAL** |
| battery-electric road transportation as application subset | **WORKING-FROZEN** |
| grid-connected EV charging mechanism | **WORKING-FROZEN** |
| resilience definition | **FROZEN — CANONICAL SERVICE-LEVEL STATE-TIME DEFINITION** |
| sustainability assessment | **FROZEN — CANONICAL TWO-PATHWAY FRAMEWORK** |
| sustainability dimensions | **FROZEN — ENVIRONMENTAL + ECONOMIC + SOCIAL** |
| effectiveness placement | **FROZEN — RESILIENCE / ENGINEERING-RESPONSE ASSESSMENT** |
| energy-efficiency placement | **FROZEN — ENVIRONMENTAL SUSTAINABILITY INDICATOR** |
| SDG linkage rule | **FROZEN — INDICATOR → DIMENSION → RELEVANT SDG TARGET/INDICATOR** |
| Improve → Adapt → Restore | **SUPPORTING ENGINEERING RESPONSE CLASSES** |
| exact charging context | **OPEN** |
| exact component/interface states | **OPEN** |
| exact electricity/mobility service metrics | **OPEN** |
| exact intervention set | **OPEN — optional/supporting, thermal only** |
| exact sustainability indicators / functional unit / time horizon | **OPEN — bounded and measurable** |
| exact SDG targets | **OPEN — after indicator definition and measurement** |
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
| [`project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`](project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md) | canonical two-pathway sustainability assessment |
| [`project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`](project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md) | current extreme-heat / thermal-interdependency / state-time scope precedence |
| [`project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`](project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md) | current authority entry point |
| [`project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md`](project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md) | decision closure / reopening |
| [`project/ROAD_VS_RAIL_SCOPE_GATE_DECISION_V1.md`](project/ROAD_VS_RAIL_SCOPE_GATE_DECISION_V1.md) | road-over-rail working decision |
| [`project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md`](project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md) | current thermal/resilience/two-pathway sustainability conceptual framework |
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
→ freeze sustainability indicators, functional/accounting basis, and time horizon
→ map only measured indicators to relevant SDG targets/indicators
→ execute only after evidence/data/model gates pass
```

---

## Spring 2027 thesis conversation handoff (2026-10-08)

For a new conversation or research-agent session, start with [the high-priority handoff index](project/handoffs/README.md), then the [full new-chat starter prompt](project/handoffs/NEW_CHAT_STARTER_PROMPT_2026-10-08.md). These are **working continuity documents**, not canonical scientific authorities, supervisor approval, or established model findings. Always load `AI_RESEARCH_INSTRUCTIONS.md` and the current thesis authority index first.

---

## Optional VisQuill interactive visualization skill

An opt-in research-visualization companion is available at [`.github/skills/visquill-interactive-visualization/SKILL.md`](.github/skills/visquill-interactive-visualization/SKILL.md). It describes when reactive TypeScript/SVG geometry is warranted, how to scaffold the GDK in a separate approved browser project, source and licensing restrictions, reproducibility tests, and thesis-science safeguards. It does **not** install VisQuill or change the scientific scope, mathematical model, or status of current validation evidence. Standard static thesis charts/figures do not require VisQuill.

---

## Dossiya Expert — on-demand research skill

[Open Dossiya Expert v1.1](.github/skills/dossiya-research-expert/SKILL.md) · [Examination record](.github/skills/dossiya-research-expert/references/LESSON_LEDGER_2026-10-09.md) · [Optional learning curriculum](.github/skills/dossiya-research-expert/references/REMAINING_CURRICULUM_TO_2026-10-23.md).

**Default use:** "Dossiya Expert, analyze this thermal interdependency" or "Expert Dossiya, derive this physics-based model." The skill **does the requested research work immediately**; it does not continue lessons, test the user, or enforce the learning plan.

**Only on explicit request:** "Dossiya Expert, continue Lesson 12", "quiz me", "evaluate my answer out of 100", or "make my mastery plan" activates learning mode.

The existing [Dossiya writing skill](.github/skills/dossiya-writing/SKILL.md) is a separate voice/editing workflow. Neither skill is a separate model or an automatic global installation. Scientific authority, evidence status and current thesis scope remain unchanged. Lessons 01–11 document written chat passes, not validated physics or independent research competence.


---

## Data acquisition checkpoint — 2026-11-05

[Open the step-by-step dataset acquisition and evidence index](data/field_candidates/2026-11-05/README.md). The dated record covers **KIT 110/20/0.4 kV multivoltage EV measurements** (local search, interrupted downloads, successful resume, publisher MD5 checks, Parquet schemas and 50-day timestamp-range check), the **US/UK/EU/Africa EVSE extreme-heat thermal replacement search**, and a [read-only full-row timestamp QA script](tools/kit_oltc_timestamp_audit.py).

[Run the new KIT 110/20/400 V electrical-response analysis](tools/kit_oltc_electrical_response_analysis.py) · [Scientific analysis protocol](data/field_candidates/2026-11-05/KIT_OLTC_ELECTRICAL_RESPONSE_ANALYSIS_PROTOCOL_V1.md). The program has passed syntax and synthetic-function tests, but measured voltage and EV-power results remain **pending execution against the original Mac files**.

**Evidence status:** All three KIT original Parquet files were downloaded and checksum-verified on the user's Mac, **not uploaded to GitHub**. The user's complete **129,600,000-row timestamp-grid check PASSED with zero mismatches** across the three files. Physical topology, independent sensor-clock accuracy, site provenance, signal QA, and thermal interdependency validation remain **OPEN**. No new thermal coupled-field claim or frozen research objective follows from this acquisition.
