# Global Uncertainty Stage / Hypothesis Propagation Matrix v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.7 CROSS-STAGE UNCERTAINTY CONTROL

## 1. Purpose

Every material uncertainty source must be traceable from its entry stage to every downstream QOI/hypothesis/decision it can affect.

Permanent:

~~~math
\boxed{
\text{uncertainty may be transformed, reduced, aggregated, or rendered irrelevant}
\neq
\text{uncertainty may silently disappear}.
}
~~~

## 2. Global source map

| Source domain | Typical objects | Entry | Main downstream stages | Main hypotheses |
|---|---|---:|---|---|
| MEASUREMENT | sensor error, assay/traffic/power measurements | S3/S4 | S4–S7 | H1–H5 as inherited |
| INITIAL_STATE | \(Y_0,\mathcal G_0,m_0\) | S3 | S3–S7 | H1–H5 |
| PARAMETER | \(\theta\), physical/operational parameters | S2/S3 | S3–S7 | H1–H5 |
| HAZARD | \(\eta(x,t)\), event timing/intensity | S3 | S3–S7 | H1–H5 |
| DEPENDENCY | activation, response law, delay, applicability | S2/S3 | S3–S7 | H1–H5 |
| OBSERVATION | availability, missingness, latency, quality | S4 | S4–S7 | H2–H5 |
| ESTIMATION | state posterior/ensemble/interval | S4 | S4–S7 | H2–H5 |
| INFORMATION | communication topology/state/info availability | S4 | S4–S7 | H2–H5 |
| ORGANIZATION | authority, resources, response delay | S4 | S4–S7 | H2–H5 |
| MODEL_FORM | alternative equations/closures/model families | S3+ | S3–S7 | H1–H5 |
| NUMERICAL | discretization, solver, sampling, optimization | S3+ | local + downstream | H1–H5 |
| REQUIREMENT | \(K,G_{rec},F_{unsafe}\), targets | S5+ | S5–S7 | H3–H5 |
| INTERVENTION_PERFORMANCE | efficacy, implementation | S6 | S6–S7 | H4–H5 |
| RESOURCE | cost/time/crew/material/energy resources | S6 | S6–S7 | H4–H5 |
| ACCOUNTING_FACTOR | emissions/energy/cost factors/boundaries | S6 | S6–S7 | H4–H5 |
| DECISION_METHOD | normalization, robustness/regret/set construction | S7 | S7 | H5 |
| VALUE_PREFERENCE | weights/preferences/value model | S7 | S7 | H5 |

## 3. Stage handoff treatment codes

Every upstream uncertainty record receives one downstream treatment code:

~~~text
PRESERVED
PROPAGATED
REDUCED
CONDITIONED
AGGREGATED
ABSORBED_WITH_TRACE
IRRELEVANT_WITH_JUSTIFICATION
BLOCKED
~~~

DROPPED is not an authorized code.

## 4. Stage 3 → 4

Stage 3 must hand off uncertainty relevant to:
- physical state trajectories;
- mechanisms/interfaces;
- parameter/hazard uncertainty;
- model-form uncertainty;
- numerical uncertainty.

Stage 4 may update state uncertainty using observations:

~~~math
\boxed{
\mathbb U_{Y}^{prior}
\xrightarrow{\mathcal E(\mathcal I_t)}
\mathbb U_{\widehat Y,t}^{post}.
}
~~~

This update must not erase model-form or numerical uncertainty unless explicitly modeled/justified.

## 5. Stage 4 → 5

Stage 5 receives:
- state/estimation uncertainty;
- control-feasibility uncertainty;
- information/organization limitations relevant to policy feasibility;
- inherited physical/model/numerical uncertainty.

Permanent:

~~~math
\boxed{
\mathbb U_{\widehat Y}
\neq
\mathbb U_{model}
\neq
\mathbb U_{numerical}.
}
~~~

An estimator posterior/covariance is not a complete system uncertainty model.

## 6. Stage 5 → 6

Stage 6 receives:
- resilience-object uncertainty;
- requirement uncertainty;
- diagnosis uncertainty;
- active mechanism/model uncertainty;
- feasible-control uncertainty.

Stage 6 adds:
- intervention-performance uncertainty;
- resource uncertainty;
- lifecycle/accounting-factor/boundary uncertainty.

## 7. Stage 6 → 7

Stage 7 receives, without collapse:
- \(\Delta\mathfrak R\) uncertainty;
- effectiveness uncertainty;
- efficiency/resource uncertainty;
- sustainability-vector uncertainty;
- feasibility uncertainty;
- requirement uncertainty;
- model-form/numerical uncertainty;
- scenario/domain uncertainty.

Stage 7 then adds decision-method and value/preference uncertainty where applicable.

## 8. H1 map

| H1 uncertainty | Required treatment |
|---|---|
| parameter/IC/hazard | matched propagation across M1/M2; common draws when semantically valid |
| dependency | readiness/activation/response-law sensitivity and mechanism ablation |
| model form | rival model-family sensitivity where plausible |
| numerical | refinement/convergence below prospectively justified materiality scale |
| validation reference | reference uncertainty included in predictive comparison |
| calibration | matched evidence/budget across rival models |

H1 cannot attribute an M2 advantage to causal dynamics if it is explainable by unequal calibration, numerical error, or different uncertainty draws.

## 9. H2 map

| H2 uncertainty | Required treatment |
|---|---|
| measurement | observation-error model/UQ |
| missingness/latency | stress/sensitivity analysis |
| estimation | state-error/coverage/calibration assessment |
| information | availability/topology uncertainty |
| organization | resource/authority/delay assumptions |
| physical upstream | inherited and held matched |

An H2 effect is not credible if organizational assumptions are changed together with physical conditions outside the preregistered treatment.

## 10. H3 map

| H3 uncertainty | Required treatment |
|---|---|
| state estimate | propagate into viability/reachability object |
| requirement | threshold/target/unsafe-set sensitivity |
| algorithm | grid/time/set convergence |
| probability | sampling uncertainty and semantics |
| model form | inherited sensitivity |
| outcome label | independent qualification/no leakage |

H3 information gain must exceed/withstand relevant numerical and label uncertainty under the preregistered materiality rule.

## 11. H4 map

| H4 uncertainty | Required treatment |
|---|---|
| intervention performance | propagate to resilience/effectiveness/sustainability |
| resource inventory | propagate to efficiency and cost/resource outcomes |
| lifecycle boundary | boundary sensitivity |
| emissions/energy factors | source qualification + factor uncertainty |
| accessibility/social | preserve distributional/group uncertainty |
| resilience improvement | eligibility stability around \(\delta_R\) |
| sustainability threshold | materiality-threshold sensitivity |

H4 cannot infer material consequence heterogeneity from inconsistent functional units, boundaries, or factor versions.

## 12. H5 map

| H5 uncertainty | Required treatment |
|---|---|
| inherited Stage 3–6 | preserved to decision input |
| requirement | admissible-set sensitivity |
| scenario/domain | scenario-set sensitivity/robustness |
| normalization | normalization sensitivity |
| decision method | Pareto/regret/robustness-construction sensitivity |
| value/preference | weight/value sensitivity only when valid model exists |
| numerical | set membership/regret/set-distance stability |

The H5 sustainability-information contrast must remain fixed while non-target uncertainties are perturbed.

## 13. Claim impact

Every uncertainty record must identify which claim ceiling it can reduce:

~~~math
\boxed{
UID_j
\rightarrow
\{\Lambda_3,\Lambda_4,\Lambda_5,\Lambda_6,\Lambda_7,H_i\}.
}
~~~

No downstream report may state a claim whose material uncertainty source is BLOCKED or omitted.
