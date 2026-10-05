# Research Decision and Freeze Protocol V1

**Status:** CANONICAL RESEARCH DECISION-CONTROL PROTOCOL  
**Effective date:** 2026-10-05  
**Repository:** `Dossiya-SE/MSE-thesis`

## 1. Purpose

This protocol prevents circular thesis development by forcing every major research decision to move from standard terminology and evidence to an explicit, testable, recorded decision.

It complements, and does not replace:
- `project/RESEARCH_REASONING_PROTOCOL.md`
- `project/EGMIV_METHOD_V1.md`

The reasoning protocol governs how claims are learned, verified, formulated, derived, tested, validated, synthesized, and advanced. EGMIV governs evidence-to-mechanism-to-model execution. This protocol governs **decision closure and reopening**.

## 2. Governing chain

```text
STANDARDIZE
→ ESTABLISH EVIDENCE
→ QUALIFY MECHANISM
→ BOUND SCOPE
→ MODEL
→ TEST
→ VALIDATE
→ FREEZE
```

Operational rule:

```text
Research once
→ decide explicitly
→ record the decision
→ advance
```

## 3. STANDARDIZE

Before thesis-specific wording is introduced, determine:

1. the standard engineering term;
2. the conventional classification;
3. the level of classification;
4. the authoritative source or standard when one exists.

Example:

```text
Transport mode
→ system/class
→ electrification technology
```

Do not mix non-equivalent levels such as road transport, BEV, rail, charging, and transportation.

## 4. ESTABLISH EVIDENCE

For every topic, answer:

```text
What exists?
→ What is supported by evidence?
→ What remains insufficiently connected or unresolved?
```

Do not begin from novelty claims.

Evidence must be classified by role where relevant:
- definition/theory;
- mechanism evidence;
- model-form evidence;
- parameterization evidence;
- validation evidence;
- standard/requirement;
- data provenance.

## 5. QUALIFY MECHANISM

Every proposed Power–Transportation interdependency must expose:

```text
direction
+ physical mechanism
+ state
+ exchange
+ service consequence
+ evidence
```

Minimum rule:

```text
connection ≠ dependency
```

and:

```text
bidirectional interdependency ≠ bidirectional electrical power flow
```

Each direction must be justified independently.

## 6. BOUND SCOPE

A mechanism enters the active thesis only if it passes the following gates:

```text
RQ relevance
+ service relevance
+ physical measurability
+ data/model feasibility
+ Master's tractability
```

A failed critical gate means:
- exclude from the active model; or
- retain only as contextual background.

This gate is used for decisions such as:
- road vs rail;
- charging vs traction;
- continuous grid-supplied traction vs battery-mediated electric mobility;
- V2G vs no V2G;
- transformer state vs omitted transformer state;
- online/real-time control vs time-resolved simulation.

## 7. MODEL

Only after scope qualification:

```text
physical reality
→ x(t)
→ F(t)
→ Q(t)
```

where:
- `x(t)` = physical state;
- `F(t)` = functionality;
- `Q(t)` = service/serviceability.

Reliability and resilience are evaluated from time-dependent performance rather than inserted without operational definition.

Every mathematical object must have:
- semantics;
- units/dimensions where applicable;
- assumptions;
- parameter provenance;
- validity domain.

## 8. TEST

Use controlled comparisons:

```text
same conditions
+ one declared modelling change
→ interpretable comparison
```

Comparator labels are governed by the current canonical model authority. If a narrower comparator architecture is proposed, it must be reconciled through a versioned amendment before replacing an existing canonical definition.

Held-constant conditions should include, where relevant:
- network;
- demand;
- initial state;
- hazard forcing;
- population/scenario;
- simulation horizon.

## 9. VALIDATE

Every important claim must follow:

```text
Definition
→ Mechanism
→ Evidence
→ Assumption
→ Test
→ Validity boundary
```

Epistemic statuses remain distinct:

```text
ESTABLISHED
≠ ADOPTED
≠ PROPOSED
≠ TESTED
≠ VALIDATED
```

Verification and validation are not interchangeable.

## 10. FREEZE

Once a decision is resolved, record:

| Field | Requirement |
|---|---|
| Item | Exact research object |
| Decision | Exact adopted wording/choice |
| Basis | Evidence, model need, standard, or thesis constraint |
| Status | OPEN / WORKING-FROZEN / FROZEN / SUPERSEDED |
| Date | Decision date |
| Reopen only if | Explicit reopening condition |
| Authority | File controlling the decision |

### Status meanings

- **OPEN** — unresolved; may change through evidence and analysis.
- **WORKING-FROZEN** — fixed for the active workstream but not yet promoted to thesis-wide canonical authority.
- **FROZEN** — authoritative for the declared scope; do not reopen casually.
- **SUPERSEDED** — retained for provenance but no longer controls active work.

## 11. Reopening rule

A FROZEN decision may be reopened only because of:

1. new contradictory evidence;
2. infeasibility discovered in data/model implementation;
3. supervisor/chair/committee instruction;
4. formal scope change;
5. conflict with a higher authority such as ASU/SSEBE requirements.

A frozen decision is **not** reopened because:
- a new phrase sounds better;
- another AI suggests a different framing;
- an exploratory idea appears interesting;
- the same conceptual question is asked again without new evidence.

## 12. Current working decision ledger

This table records the current 2026-10-05 presentation/thesis-narrowing workstream. It does not silently override older canonical scientific authorities.

| Item | Decision | Status | Reopen only if |
|---|---|---|---|
| Thesis title | Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience | **FROZEN** | Formal title amendment |
| Core systems | Power + Transportation | **FROZEN** | Formal scope amendment |
| Hazard | Extreme heat | **WORKING-FROZEN** | New evidence, infeasibility, supervisor instruction, or canonical amendment |
| Performance focus | Functioning, serviceability, reliability | **WORKING-FROZEN** | Literature/operationalization requires correction |
| Primary outcome | Electricity and mobility service trajectories / resilience | **WORKING-FROZEN** | RQ or model contract changes |
| Transport electrification mechanism | Under qualification | **OPEN** | — |
| Road vs rail | Under qualification | **OPEN** | — |
| Exact resilience-capacity label | Not selected | **OPEN** | — |
| V2G | Not active by default | **OPEN / excluded unless justified** | Mechanism and scope gates pass |
| Energy efficiency | Secondary criterion after service is defined | **WORKING-FROZEN** | Research question changes |
| Real-time operation | Term not adopted unless online/live control is modeled | **OPEN** | Implementation justifies it |
| Engineering action sequence | Improvement/enhancement → adaptation → restoration | **WORKING-FROZEN** | Evidence or implementation shows a different sequence is required |

## 12A. Engineering action sequence

The current thesis workstream uses the following engineering progression:

```text
IMPROVEMENT / ENHANCEMENT
→ ADAPTATION
→ RESTORATION
```

Interpretation:

- **Improvement / enhancement** is the starting engineering objective. Physics-based mathematical engineering is used to identify where performance can be improved relative to a declared baseline. It is not treated as a separate standard resilience type.
- **Adaptation** is the time-dependent operational adjustment made while extreme-heat conditions and system states are evolving.
- **Restoration** is the recovery of degraded electricity and mobility service toward a declared acceptable or reference level after or as the disturbance relaxes.

This sequence must remain service-centered:

```text
physical state
→ functioning
→ serviceability
→ reliability
→ improvement/adaptation/restoration action
→ service-resilience consequence
```

The thesis must measure improvement against explicit service metrics and a comparator rather than assume that a more detailed model or more control automatically improves resilience.

## 13. Presentation integration

For the 8-slide MSE presentation, every new strong result must be mapped to one slide and logged with:

```text
ID
→ statement
→ epistemic status
→ source/authority
→ mechanism
→ service relevance
→ assumptions
→ validity boundary
→ slide
→ admission decision
→ freeze status
```

Use:
`project/PRESENTATION_8_SLIDE_RESEARCH_BRIEF_V1.md`

as the active presentation ledger.

## 14. Human / AI continuation rule

Any human or AI continuing the thesis must:

1. load the current canonical authorities;
2. inspect the decision ledger before reopening a question;
3. distinguish OPEN from FROZEN items;
4. preserve exact frozen wording where required;
5. add new evidence rather than restart old debates;
6. create a versioned amendment when a frozen decision must change;
7. retain superseded decisions for provenance.

## 15. Governing principle

```text
Research is cumulative only when decisions have memory.
```

Therefore:

```text
No repeated conceptual reset without new evidence or an explicit reopening condition.
```
