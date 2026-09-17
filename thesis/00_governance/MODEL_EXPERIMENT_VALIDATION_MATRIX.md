# Model–Experiment–Validation Matrix

**Status:** CURRENT / SYNCHRONIZED WITH RQ–SO–H v3.0  
**Scientific authority:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Framework authority:** `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`

**Purpose:** enforce preregistration, rival-model comparison, physical admissibility, uncertainty quantification, practical significance and falsification before scientific inference.

## Generic test object

```math
\boxed{
\mathcal T_i=
(H_i,M_i,B_i,\Omega_i,D_i,\theta_i,X_i,T_i,Z_i,\delta_i,\mathcal F_i,V_i,U_i)
}
```

where:

- `H_i`: hypothesis;
- `M_i`: proposed model/representation/treatment;
- `B_i`: baseline or rival model;
- `\Omega_i`: test/scenario domain;
- `D_i`: evidence/data and declared calibration/validation role;
- `\theta_i`: parameters and provenance;
- `X_i`: held-constant initial/exogenous conditions;
- `T_i`: treatment or changed factor;
- `Z_i`: preregistered response vector;
- `\delta_i`: prespecified practical/engineering significance threshold or decision criterion;
- `\mathcal F_i`: falsification/non-support condition;
- `V_i`: verification and validation protocol;
- `U_i`: uncertainty/sensitivity protocol.

## Universal EGMIV requirements

Every confirmatory comparison must preserve, unless explicitly defined as the treatment:

```math
\boxed{
\text{same relevant initial conditions}
+
\text{same hazards/scenarios}
+
\text{same exogenous inputs}
+
\text{same resource/accounting assumptions}
}
```

No preferred model is validated alone. Calibration, verification and validation evidence must retain distinct roles.

### Verification gate

```math
\text{definitions/dimensions}
\rightarrow\text{conservation/physics}
\rightarrow\text{limiting cases}
\rightarrow\text{numerical convergence}
\rightarrow\text{regression/unit tests}.
```

### Validation gate

```math
\text{benchmark/observed behavior}
\rightarrow\text{independent or held-out comparison where feasible}
\rightarrow\text{declared validation domain}
\rightarrow\text{uncertainty-aware adequacy judgment}.
```

Verification and validation are not interchangeable.

## H1 — Dynamic causal interdependency

| Element | H1 specification / current state |
|---|---|
| Question/objective | RQ3/SO3, with developmental inputs from RQ1/SO1 and RQ2/SO2 |
| Claim | dynamic causal P–T coupling provides meaningful incremental explanatory/predictive information relative to simpler representations |
| Baselines | `M0` independent; `M1` static/algebraic coupling |
| Proposed representation | `M2` dynamic causal coupling |
| Nested-limit requirement | `M2→M1` as dynamic memory/delay effects vanish; `M1,M2→M0` when interface maps are removed |
| Held constants | matched hazards, initial states, service requirements and exogenous conditions |
| Treatment | coupling representation (`M0/M1/M2`) |
| Response family | preregistered cascade, service-loss, spatial-propagation and recovery outcomes |
| Current model state | M0/M1/M2 implementations verified under current project authority |
| Confirmatory design | frozen as specified by H1 authority |
| Raw data | row-level retrieval/qualification pending |
| Candidate split | not frozen until R1–R8 qualification passes |
| Calibration authorization | BLOCKED until raw-row qualification passes |
| Confirmatory run authorization | BLOCKED until prerequisite data/activation gates pass |
| Falsification/non-support | M2 fails the preregistered meaningful incremental-information criterion relative to M1 or violates physical/nested-limit requirements |

## H2 — Information, organization and feasible control

| Element | Required specification |
|---|---|
| Question/objective | RQ4/SO4 |
| Claim | under matched physical conditions, information availability and organizational conditions materially alter estimation, feasible action, response timing and downstream recovery/resilience |
| Nested representations | `P+T`, `P+T+I`, `P+T+I+O` |
| Mechanisms | observation availability/error, communication delay, estimation uncertainty, authority, coordination, resource and response-delay constraints |
| Held constants | physical initial state, hazard, physical model, service requirements and exogenous resources except the organizational factor being tested |
| Treatment | declared information/organizational perturbation |
| Primary responses | estimation quality, feasible-control set, response delay, service/recovery and Stage-5 outcomes |
| Data/domain | NOT YET FROZEN |
| Threshold/decision rule | NOT YET FROZEN |
| V&V/UQ | MUST BE FROZEN BEFORE CONFIRMATORY EXECUTION |
| Falsification/non-support | declared I/O contrasts fail to produce the prespecified meaningful effect over the declared domain |

## H3 — Viability/reachability incremental information

| Element | Required specification |
|---|---|
| Question/objective | RQ5/SO5 |
| Claim | uncertainty-aware viability/reachability quantities add meaningful predictive or decision information beyond conventional service/performance and recovery curves |
| Baseline information set | conventional performance/recovery metrics `R_curve` |
| Proposed information set | `R_curve + \mathfrak R_T` where `\mathfrak R_T` includes declared viability, reachability, margin/time and probability quantities |
| Held constants | matched system states/scenarios and downstream prediction/decision task |
| Treatment | addition of the Stage-5 resilience information set |
| Outcome | preregistered future maintainability/recovery/decision target |
| Mandatory preregistration | `K`, `G_rec`, `F`, `T_V`, `T_R`, `alpha`, `beta`, uncertainty semantics, Skill metric and `delta_3` |
| Interface criticality | supporting diagnostic only unless separately preregistered as a superiority test |
| Falsification/non-support | no meaningful incremental skill/decision value under the preregistered criterion after declared complexity/uncertainty controls |

## H4 — Intervention effectiveness, efficiency and sustainability consequences

| Element | Required specification |
|---|---|
| Question/objective | RQ6/SO6 |
| Claim | interventions with comparable or improved resilience outcomes can differ materially in resource efficiency and sustainability consequence vectors |
| Candidate intervention set | MUST BE DECLARED before confirmatory execution |
| Resilience-effectiveness criterion | MUST BE FROZEN (`\delta_R` or equivalent) |
| Efficiency definition | benefit/resource denominator and accounting boundary MUST BE FROZEN |
| Sustainability vector | evidence-supported outcomes such as accessibility, operational energy, carbon and cost, with explicit accounting boundaries |
| Held constants | matched disturbance/scenario domain and comparable resource/accounting assumptions where required by contrast |
| Treatment | intervention `a_k` |
| Primary object | `a_k→(\Delta\mathfrak R^{a_k},\Delta\mathbf J_{sus}^{a_k})` plus declared effectiveness/efficiency quantities |
| Distance/materiality rule | `D_J` and `delta_4` NOT YET FROZEN |
| Falsification/non-support | resilience-effective interventions do not exhibit the preregistered material differences in efficiency or sustainability outcomes over the declared domain |

## H5 — Joint resilience–sustainability engineering decision

| Element | Required specification |
|---|---|
| Question/objective | RQ7/SO7 |
| Claim | incorporating sustainability consequences into resilience-based evaluation materially changes the feasible/nondominated decision set or declared regret relative to resilience-only evaluation |
| Baseline decision set | `\mathcal A_R^{\star}` |
| Joint decision set | `\mathcal A_{R,S}^{\star}` |
| Inputs | H4 intervention-performance consequences plus feasibility and uncertainty |
| Held constants | same candidate actions, scenario ensemble and feasibility/resource rules across decision formulations |
| Treatment | inclusion of declared sustainability consequence dimensions in the decision rule |
| Set/regret metric | NOT YET FROZEN |
| Materiality threshold | `delta_5` NOT YET FROZEN |
| Sequential/adaptive pathway | supporting extension only; requires separate activation/preregistration if tested |
| Falsification/non-support | joint evaluation fails the preregistered material-change/regret criterion over the declared uncertainty domain |

## Supporting diagnostics and extensions

### Interface criticality

Interface criticality belongs to the Stage-5/6 diagnostic chain and may support RQ5/RQ6. It is not H4 by default. Any claim that a proposed criticality ranking outperforms structural/flow baselines requires its own declared comparator, equal-budget rule, metric, uncertainty treatment and falsification condition.

### Adaptive/sequential transformation

Adaptive or sequential transformation belongs to Stage 7 as a supporting extension. It must not be presented as the primary H5 test unless scope and preregistration are explicitly amended before results are observed.

## Parameter provenance rule

```math
\boxed{
\text{measured/site data}
>
\text{peer-reviewed/full-text evidence}
>
\text{qualified benchmark data}
>
\text{sensitivity-only assumption}.
}
```

No sensitivity-only value may later be described as empirical calibration.

## Amendment rule

Any post-freeze change to a confirmatory threshold, scenario domain, baseline, data split, primary metric, accounting boundary, treatment, or falsification rule requires a dated amendment stating:

1. reason for change;
2. whether relevant results were already observed;
3. whether the affected analysis becomes exploratory;
4. downstream thesis sections and claims affected.
