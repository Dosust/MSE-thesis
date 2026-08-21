# Decision Log — Current Thesis Architecture

This log distinguishes **explicitly frozen/current working decisions** from recommendations and unresolved alternatives.

## D1 — Sector set

**State:** current working/frozen for the architecture.

```text
Power + Water/Drainage + Transportation + Solid Waste
```

Rationale preserved in the project: this four-sector system supports coupled infrastructure physics and the urban-flood/drainage-waste feedback demonstrator.

## D2 — Primary demonstrator

**State:** current working/frozen.

```text
urban flooding with drainage–solid-waste feedback
```

The demonstrator should expose cross-sector mechanisms, not merely co-occurring failures.

## D3 — Forcing/hazard distinction

**State:** frozen conceptual distinction.

```text
xi = exogenous climate forcing
eta = realized local hazard/stress acting on infrastructure
```

Do not collapse rainfall forcing and local inundation into one variable without justification.

## D4 — Interface versus interdependency

**State:** frozen conceptual requirement, operational definition still to be completed.

```text
connection != interdependency != interface mechanism
```

The thesis should represent actual cross-sector mechanisms and, where justified, interface states `Z_ij(t)` rather than only static edges.

## D5 — Admissible set

**State:** frozen architecture; thresholds pending.

```text
K_R = K_phys ∩ K_service ∩ K_sus ∩ K_eq
```

Sustainability and equity are intended to enter as admissibility/constraint structure, not only as post hoc descriptive scores.

## D6 — Viability/recovery separation

**State:** frozen conceptual distinction.

```text
V_R = states that can remain admissible
C_R = states from which V_R can be reached in finite time
```

Do not use “resilience,” “viability” and “recovery” interchangeably.

## D7 — Central geometric object

**State:** current scientific center.

```text
partial V_R = viability boundary
```

The thesis asks what moves this boundary, how uncertain it is, and how control/design changes it.

## D8 — Six-chain ontology

**State:** current frozen ontology for organizing literature/mathematics.

1. Physical System
2. Observation–Inference–Prediction
3. Hazard–Failure–Consequence
4. Resilience–Viability–Recovery–Control
5. Engineering Lifecycle / Action
6. Sustainability–Evaluation–Decision

Cross-cutting methods such as optimization/UQ/ML/numerical analysis should not be mislabeled as physical layers.

## D9 — Three thesis alternatives

**State:** alternatives retained; not all simultaneously primary.

- Type I — Theory-First
- Type II — Digital Twin / Inference-to-Decision
- Type III — Resilience-by-Design

Current recommendation: Type-I-centered MSE with Type-II upstream identification/UQ and limited Type-III downstream demonstration.

## D10 — Scientific proposition family

**State:** frozen working falsification family.

P1/H0 through P7/T1 as recorded in `03_MATHEMATICAL_OBJECTS_AND_PROPOSITIONS.md` and `project/SCIENTIFIC_PROPOSITIONS.md`.

## D11 — Evidence authority

**State:** frozen methodological rule.

Literature evidence can falsify/narrow the proposed architecture. A direct precedent is a successful review result, not a project failure.

## D12 — PRISMA versus Monte Carlo

**State:** frozen methodological distinction.

- PRISMA = search/screening/accounting.
- Monte Carlo ranking = corpus-relative robustness ranking.

Neither proves global novelty.

## D13 — 325-record lock

**State:** frozen for the closed-corpus ranking already executed.

File: `Thesis_Final_Unique_Papers_325_2026-08-20(1).csv`

SHA-256: `047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f`

Do not retroactively mix earlier corpora into that run.

## D14 — Numerical architecture code

**State:** implemented but explicitly synthetic/reference QA.

Do not call it calibrated, validated or operational without a later documented calibration/validation stage.

## D15 — Mathematical-art style

**State:** design rule.

Prefer scientific geometric displays:

- state-space surfaces;
- vector fields;
- reachable/viable boundaries;
- network/interface operators;
- uncertainty density/credible regions;
- sensitivity maps;
- recovery-time level sets;
- Pareto fronts only where optimization is actually defined.

Avoid decorative stock-style diagrams as substitutes for mathematical content.

## D16 — Programming-language rule

**State:** frozen implementation principle.

Use each language only where it contributes scientifically/reproducibly. Current roles: Markdown/LaTeX, SVG, Mermaid, Python, Julia, YAML, JSON Schema and GitHub Actions.

## D17 — Next deep scientific task

**State:** current next priority unless explicitly redirected.

Deeply decompose **Chain I** sector-by-sector with equations, assumptions, literature anchors and unresolved mathematical questions before freezing the coupled forward model.

## D18 — Scope guardrail

**State:** strong recommendation, not an irrevocable user freeze.

One MSE thesis should have one coherent original mathematical center. Full theory → digital twin → design → policy is a long-term program; downstream stages may be demonstrations rather than independent novelty claims.