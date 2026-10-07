# CURRENT-SCOPE OVERRIDE — effective 2026-10-06

Before applying any older instruction in this file, load:

- `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`
- `project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`
- `project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md`
- `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`
- `project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md`

The active thesis workstream focuses **only on thermal interdependencies between the Power System and Electrified Transportation System and on their consequences through state and time**. The Electrified Transportation System composition is controlled by `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`. Battery-electric road transport and a charging context are bounded application subsets, not the thesis-wide definition of the transportation system. The September seven-stage / RQ1–RQ7 / H1–H5 / Austin-P3 architecture is retained for provenance and reusable methods but is **not current scope authority where it conflicts with the 2026-10-06 scope amendment**.

Do not silently reactivate historical Chapter-I, RQ/SO/H, P3/Austin, P+T+I+O, flood, or broad sustainability-decision scope. The final narrowed RQ/SO/H set is OPEN.

For scientific diagrams, also load:
- `.github/skills/engineering-framework-design/SKILL.md`
- `.github/skills/scientific-diagram-design/SKILL.md`
- `.github/skills/mathematical-visualization-design/SKILL.md`

---

# Historical / enduring repository instructions below

# Repository Working Instructions

## Canonical thesis-title authority

For any active thesis, proposal, manuscript, presentation, figure, README, research-identity, or repository-governance task, use the exact title controlled by:

`project/CANONICAL_THESIS_TITLE_V1.md`

The exact active title is:

> **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**

Do not silently substitute historical or exploratory titles. Historical archives and provenance snapshots remain unchanged.

## Canonical thermal-interdependency focus

For every active thesis, model, diagram, presentation, Chapter-I, research-question, objective, method, result, discussion, or conclusion task, load:

`project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`

and

`project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md`

Permanent active focus:

> **The thesis studies only thermal interdependencies between the Power System and the Electrified Transportation System and their consequences through state and time.**

Do not broaden the active thesis back to generic Power–Transportation interdependencies, generic coupled-network behavior, non-thermal dependency classes, or broad infrastructure-resilience analysis.

Non-thermal variables may appear only when they are necessary boundary conditions, coupling variables, controls, or constraints for a thermal mechanism or its consequence.

Use **qualify** consistently. In objectives and scope statements, name the physical object or variable class directly.

State and time are the primary analytical dimensions. Preserve:

```text
extreme heat
→ thermal physical state
→ thermal capability / constraint
→ thermal interdependency
→ state-time consequence
→ electricity / mobility service consequence
→ Improve / Adapt / Restore
```

This focus remains controlling unless reopened by explicit user/supervisor/chair/committee direction or by a formally versioned scope amendment under the repository decision/freeze protocol.

## Canonical Electrified Transportation System scope

For any active thesis, model, diagram, presentation, Chapter-I, research-question, or scope task involving Transportation or electrification, load:

`project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`

Use the exact system name **Electrified Transportation System**. Do not use the phrase “standards-defined electrified transportation system.”

Canonical scope statement:

> **In this thesis, the electrified transportation system comprises the electrically propelled road vehicle, its rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, the vehicle power-supply circuit, electric-vehicle supply equipment, the physical charging connection, and the communication and control functions required for electrical power transfer, including bidirectional transfer where supported (ISO 6469; ISO 5474; ISO 15118; IEC 61851; IEC 62196).**

The standards justify the technical composition and boundary. Do not infer that every listed element requires the same model fidelity. Use minimum sufficient physics. Keep the external Power System distinct. EVSE and the physical charging connection belong to the Electrified Transportation System scope; interface/coupling variables may represent exchanged quantities without becoming a third physical infrastructure system. Mobility service and transportation-operation quantities remain separate outputs/operational layers and require their own definitions and evidence.

## Research decision and freeze authority

For any task that selects, narrows, freezes, reopens, or compares thesis scope, terminology, mechanisms, models, presentation claims, or research decisions, also load and apply:

`project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md`

Its role is decision closure and reopening control. It complements the canonical reasoning protocol and EGMIV; it does not replace them. Respect `OPEN`, `WORKING-FROZEN`, `FROZEN`, and `SUPERSEDED` statuses exactly.

## 8-slide MSE presentation workstream

For the current 8-slide MSE research presentation, after loading the canonical authorities required by the task, also load:

`project/PRESENTATION_8_SLIDE_RESEARCH_BRIEF_V1.md`

Use its decision ledger, slide architecture, evidence-admission record, and freeze rules to avoid circular redefinition. Treat **OPEN** and **WORKING-FROZEN** entries exactly as labeled; do not promote them to canonical thesis authority without a versioned amendment.

## Chapter I activation rule

Whenever a task refers to **Chapter I**, **Chapter 1**, **Introduction**, the **introductory research architecture**, or asks to draft/revise/present any Chapter-I section, first load and follow:

`project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V3.md`

That file is the controlling Chapter-I authority. `CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V1.md` is provenance only.

### Required behavior

1. Preserve the 160-page thesis ceiling and the Chapter-I target of **16–18 pages** unless the user explicitly changes the allocation.
2. Preserve the Chapter-I sequence:

```text
Context → Problem → Gap → Scope → Framework → Questions → Objectives → Hypotheses → Proposed contribution
```

3. Preserve the scientific distinctions:

```text
structure ≠ causality ≠ dynamics ≠ control ≠ resilience outcome
```

4. Preserve the current scientific seven-stage architecture:

```text
Spatiotemporal SoS Structure
→ Evidence-Qualified Directional Dependencies
→ Complex Spatiotemporal Coupled Dynamics
→ Observation/Estimation/Organization/Feasible Control
→ Uncertainty-Aware Spatiotemporal Service Resilience
→ Targeted Intervention Consequences
→ Defensible Engineering Decision
```

5. A reader-facing simplified chain may be used for communication only if it preserves the exact scientific meaning of framework v2.
6. Preserve `P,T` as physical infrastructure systems and `I,O` as supporting informational/organizational domains unless an explicit model revision changes that definition.
7. Preserve the distinction between operational control `u(t)` and strategic intervention `a_k`.
8. Preserve:

```text
effectiveness ≠ efficiency ≠ sustainability
```

9. Preserve `RQ1–RQ7 ↔ SO1–SO7` traceability and the current H1–H5 architecture. RQ1/RQ2 carry developmental/evidence obligations; RQ3–RQ7 map to H1–H5.
10. Interface criticality is a supporting diagnostic by default; do not silently make it H4.
11. Adaptive/sequential transformation is a supporting Stage-7 extension by default; do not silently make it H5.
12. Do not infer novelty from silence. Research-gap and novelty statements must remain evidence-qualified.
13. Keep detailed mathematical derivations primarily in Chapter 3 and detailed experiments/VVUQ primarily in Chapter 4.
14. Never silently rewrite a canonical authority. Record material changes as explicit versioned amendments.

## Thesis-wide research-question authority

For any research-question, objective, hypothesis-mapping, outline, figure, result or conclusion task, load:

- `project/CANONICAL_RESEARCH_QUESTIONS_V4.md`
- `project/CANONICAL_7_STAGE_FRAMEWORK_V2_1_ALIGNMENT_AMENDMENT.md`
- `project/CANONICAL_RQ_SO_HYPOTHESES_V4.md`
- `thesis/00_governance/RQ_SO_H_TRACEABILITY_V4.md`

Use RQ0 + RQ1–RQ7, SO1–SO7 and H1–H5. Do not equate question and hypothesis indices or revert to superseded five-question files.

## Thesis-wide scientific writing and inference rule

For substantive thesis drafting, revision, evidence synthesis, mathematical exposition, results, discussion or conclusions, load:

`thesis/00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`

Preserve the internal epistemic separation:

```text
[E] external evidence
[D] thesis derivation
[H] hypothesis
[P] proposal/construct
[A] assumption
[U] unresolved uncertainty
[R] declared result
```

Final prose does not need to display these labels, but it must preserve their meaning.

No factual scientific claim without admissible evidence; no mathematical object without semantics; no model without assumptions/validity domain; no confirmatory hypothesis without comparator/metric/falsification; no result without uncertainty where relevant; no conclusion beyond the validation domain.

## ASU/SSEBE precedence

Repository conventions remain subordinate to current ASU Graduate College requirements, the SSEBE Sustainable Engineering MSE requirements, committee/chair decisions and the approved style guide. Internal files must never be presented as university policy when they are internal scientific controls.

## Thesis-wide grading authority

Whenever a task asks to **grade, score, rate, assess, evaluate, or compare** thesis work, first load and apply:

- `thesis/00_governance/THESIS_WRITING_GRADING_STANDARD_V1.md`
- `thesis/00_governance/SIMPLE_THESIS_WRITING_GRADING.xlsx`

Use the grading standard as the baseline for thesis writing and scientific communication. Apply its fixed 100-point weighting:

```text
Useful information                    10%
Scientific precision                  15%
Academic / human writing              10%
Infrastructure terminology            10%
Thesis alignment                      15%
Scope and validity control            10%
Systems thinking                      10%
Engineering / design thinking          5%
Research-method rigor                 10%
Evidence / argument quality            5%
```

For mathematical models, simulations, code, experiments, datasets, figures, or other technical thesis artifacts, add the relevant task-specific technical criteria, but do not omit this baseline communication/scientific-argument grading standard when an overall thesis-work grade is requested.

Before grading, also load any canonical authority governing the object being graded. A high writing score cannot compensate for scientific, scope, evidence, or governance noncompliance.

Report the overall grade out of 100 together with criterion-level scores and clearly distinguish writing-quality deductions from scientific-content deductions.

## Thesis-wide citation and reference authority

For substantive thesis drafting, revision, literature synthesis, research-gap writing, source attribution, bibliography/reference work, or any task that asks whether a claim needs a citation, first load:

`thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md`

Apply APA 7 author–date formatting together with the thesis evidence rules. Preserve:

```text
correct citation format ≠ adequate scientific evidence
```

Externally sourced scientific claims require adjacent qualified citations. Thesis-defined scope, research questions, objectives, hypotheses, assumptions, derivations, proposed framework objects, and proposed contributions must not be padded with irrelevant citations merely for appearance. Every in-text citation must map to a verified reference entry, every reference entry must be cited, and a citation must support the exact proposition and validity domain claimed.

For Chapter I citation work, also use the current Chapter-I evidence sources and claim/evidence registers. Citation completion does not authorize silent changes to frozen GO/RQ/SO/H wording.

