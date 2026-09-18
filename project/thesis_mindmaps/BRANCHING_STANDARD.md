# Branching Standard for the Seven-Stage Thesis Mind Maps

## 1. Repeated scientific branch grammar

Every stage uses the same ten branches:

~~~text
STAGE ROOT
|-- A. Scientific responsibility
|   |-- canonical RQ
|   `-- canonical SO
|-- B. Inputs
|-- C. Mathematical / physical objects
|-- D. Mechanism or method
|-- E. Evidence and provenance
|-- F. Assumptions and uncertainty
|-- G. Verification / validation / falsification
|-- H. Gate state
|-- I. Output / scientific handoff
`-- J. Explicit non-claims / exclusions
~~~

This grammar prevents a stage from being represented only as a list of equations. Each stage must show what question it answers, what evidence it consumes, how its objects are tested, and what is legally passed to the next stage.

## 2. Handoff rule

For Stage `k`, define a handoff object `Z_k`. The next stage may consume `Z_k` but may not silently reinterpret its semantics.

~~~math
\boxed{
Z_k
\xrightarrow{\text{declared transformation + gate}}
Z_{k+1}
}
~~~

Every handoff therefore has four controls:

~~~text
semantic compatibility
+ provenance continuity
+ uncertainty continuity
+ gate continuity
~~~

## 3. Status vocabulary

~~~text
PASS — FROZEN     scientific object is immutable without amendment
PASS — WORKING    scientifically admissible but not frozen
OPEN              required work remains
BLOCKED           evidence/execution needed but unavailable
FAIL / REVISE     stated gate is not satisfied
NOT TESTED        no scientific test has yet been executed
~~~

`BLOCKED` must never be converted into `FAIL`; `OPEN` or `NOT TESTED` must never be written as `PASS`.

## 4. Evidence-state separation

Across all maps:

~~~math
\boxed{
\text{established evidence}
\neq
\text{thesis construction}
\neq
\text{hypothesis}
\neq
\text{validated result}
}
~~~

Stage-specific candidate objects are explicitly marked as candidates until their admission gate passes.

## 5. Cross-stage VVUQ

Verification, validation, uncertainty quantification, falsification, provenance, and reproducibility are cross-cutting controls, not an eighth scientific stage.

~~~math
\boxed{\text{Stages }1\text{--}7\subset\text{VVUQ + falsification + provenance}}
~~~

## 6. Hypothesis traceability

| Stage | Canonical mapping |
|---|---|
| 1 | RQ1 / SO1 — developmental qualification supporting H1 |
| 2 | RQ2 / SO2 — developmental qualification supporting H1 |
| 3 | RQ3 / SO3 — H1 |
| 4 | RQ4 / SO4 — H2 |
| 5 | RQ5 / SO5 — H3 |
| 6 | RQ6 / SO6 — H4 |
| 7 | RQ7 / SO7 — H5 |

## 7. Visual conventions

Each Mermaid map uses one central stage node with outward branches. Branches encode semantics rather than decorative hierarchy. Labels remain short enough for GitHub rendering; exact equations and controlled vocabularies are written below each map.

## 8. Stage-1 protection rule

Stage 1 is frozen. These mind maps may **represent** the frozen Stage-1 ontology but may not redefine it. Any contradiction with `STAGE1_FRAMEWORK_FREEZE_2026-09-18.md` is an error in the visualization, not an amendment to Stage 1.