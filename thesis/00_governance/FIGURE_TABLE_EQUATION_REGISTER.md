# Figure–Table–Equation Register

**Purpose:** prevent disconnected visuals, duplicate mathematics, notation drift, and figures without a scientific question.

## Artifact rule

Every formal artifact must answer:

```math
\boxed{
A_j=(\text{question answered},\text{scientific object/data},\text{claim},\text{chapter},\text{provenance},\text{status}).
}
```

A figure is not created merely because it is visually attractive.

## Required fields

| Field | Meaning |
|---|---|
| Artifact ID | `F#.#`, `T#.#`, or `E#.#` |
| Type | figure / table / equation |
| Working title | concise scientific title |
| Question answered | what reader should learn |
| Claim IDs | claims supported/illustrated |
| Data/object provenance | evidence/model source |
| Mathematical objects | notation used |
| Chapter/section | intended thesis location |
| Validation status | proposed / verified / result-dependent |
| Reproducibility | source code/file path if generated |
| Notes | limitations / dependencies |

## Initial figure plan

| ID | Working title | Question answered | Chapter | Status |
|---|---|---|---|---|
| F2.1 | Literature/theory synthesis map | Which established theories support each thesis problem and where are unresolved intersections? | Ch.2 | planned |
| F3.1 | Theoretical foundation of infrastructure interdependency | How do system → service/interface → dependency → interdependency → dynamic SoS compose? | Ch.3 | working |
| F3.2 | P–T–I–O / domain×aspect ontology | What entities/aspects are represented and where can interactions occur? | Ch.3 | working/proposed |
| F3.3 | Directed dependency/interdependency object | What source, receiver, mechanism, strength, delay, timescale and activation information is carried? | Ch.3 | canonical science must control final graphic |
| F3.4 | Seven-stage conceptual architecture | How do the seven stages connect? | Ch.3 | working; must use canonical stage names |
| F3.5 | Stage-to-stage mathematical handoffs | What exact mathematical/engineering objects pass between stages? | Ch.3 | planned |
| F4.1 | H1 rival-model architecture | What differs among M0/M1/M2 under matched experiments? | Ch.4 | planned |
| F4.2 | H1 data qualification and train/test gate | How do raw event data pass R1–R8 into admissible confirmatory data? | Ch.4 | planned |
| F4.3 | Verification–validation–UQ workflow | What gates must a model pass before inference? | Ch.4 | planned |
| F5.1 | H1 confirmatory result | What does the frozen H1 comparison show? | Ch.5 | BLOCKED until confirmatory execution |

## Initial table plan

| ID | Working title | Chapter | Status |
|---|---|---|---|
| T1.1 | Research questions, objectives and hypotheses | Ch.1 | planned |
| T2.1 | Literature evidence synthesis by theory/problem | Ch.2 | planned |
| T2.2 | Dependency/interdependency definitions and representations | Ch.2 | planned |
| T3.1 | Canonical notation and units | Ch.3 | planned |
| T3.2 | Seven-stage responsibilities, inputs and outputs | Ch.3 | planned |
| T4.1 | H1–H5 experimental specification matrix | Ch.4 | active via governance matrix |
| T4.2 | Parameter provenance and uncertainty domains | Ch.4 | planned |
| T5.1 | H1 confirmatory metrics and uncertainty | Ch.5 | BLOCKED |

## Initial equation families

| ID | Equation family | Chapter | Status |
|---|---|---|---|
| E3.1 | constituent system/state definition | Ch.3 | active/proposed |
| E3.2 | dependency/interdependency object | Ch.3 | active/canonical project object with theoretical refinement under study |
| E3.3 | coupled hybrid multiscale dynamics | Ch.3 | frozen project architecture |
| E3.4 | observation/estimation/control loop | Ch.3 | frozen project architecture |
| E3.5 | controlled sustainable viability | Ch.3 | frozen project architecture; proposed submetrics retain epistemic labels |
| E3.6 | transformation diagnosis map | Ch.3 | frozen project architecture |
| E3.7 | transformation pathway/regime update | Ch.3 | frozen project architecture |
| E4.1 | H1 M0/M1/M2 competing representations | Ch.4 | frozen H1 specification |

## Visual QA rules

1. White background unless an explicit thesis-design decision changes this.
2. Geometry must encode scientific meaning; arrows are not decorative.
3. Every arrow/connector must be defined in text/equations.
4. Generated-image equations are drafts only until checked against canonical notation.
5. No figure may redefine frozen stage names or mathematical objects.
6. Color is supplementary; meaning must survive grayscale reproduction.
7. Figure labels/captions must remain legible within ASU page margins.
8. Final figures require a source/reproduction path or documented manual construction procedure.

## Registry update rule

Before a new framework graphic is treated as thesis-ready, register it here and identify:

```math
\boxed{\text{Which chapter? Which claim? Which RQ? Which evidence? Which equation?}}
```
