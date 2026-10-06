# Historical Status Notice — effective 2026-10-06

**Status:** RETAINED LEGACY PROPOSITION / FALSIFICATION PACKAGE  
**Current scope authority:** `CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md`

The P1–P10 and H1–H5 architecture below belongs to the September broad thesis design. It is retained for provenance, falsification logic, and possible re-use.

It is **not the current narrowed RQ/SO/H authority**. The final extreme-heat state-time RQ/SO/H set remains OPEN.

The exact pre-reconciliation file is preserved at:

`../archive/readme_versions/2026-10-06_pre_reconciliation/SCIENTIFIC_PROPOSITIONS_PRE_2026-10-06.md`.

---

# Historical proposition package below

# Scientific Propositions and Falsification Plan

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)

**Status:** CURRENT / SYNCHRONIZED WITH RQ–SO–H v4  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Evidence rule:** A proposition is a testable supporting claim, diagnostic, sub-test, or conditional extension. The five primary confirmatory hypotheses are defined in [`CANONICAL_RQ_SO_HYPOTHESES_V4.md`](CANONICAL_RQ_SO_HYPOTHESES_V4.md).  
**Framework rule:** Frozen `[P]` objects remain proposed thesis constructs until their scientific value is demonstrated.

---

## 1. Hypothesis–proposition hierarchy

The primary hypothesis set is

```math
\mathbb H=\{H_1,H_2,H_3,H_4,H_5\}.
```

The propositions here are **not ten additional primary hypotheses**. They are subordinate falsifiable claims, diagnostics, or conditional extensions used to operationalize, stress-test, explain, or extend the primary research architecture:

```math
H_{\rm SYS}
\rightarrow
\{H_1,\ldots,H_5\}
\quad + \quad
\{P_1,\ldots,P_{10}\}
\rightarrow
\text{tests / diagnostics / conditional extensions / falsification}.
```

Numerical thresholds $\delta_1,\ldots,\delta_5$ remain unset until justified *a priori* in the Hypothesis Specification Matrix.

---

## 2. Proposition registry

| ID | Testable proposition | Primary hypothesis | Main object / contrast |
|---|---|---:|---|
| **P1** | Explicit P–T–I–O representation adds explanatory or predictive value beyond a physical P–T-only model when information and organizational constraints materially affect response. | $H_2$ | physical-only vs. full P–T–I–O model |
| **P2** | Dynamic interdependencies produce materially different trajectories or viability conclusions from static coupling under some operating regimes. | $H_1$ | dynamic vs. static $w_{ij},a_{ij}$ and topology |
| **P3** | Information degradation can materially alter control outcome through observability, estimation error or response delay. | $H_2$ | $z_I$, $\widehat X$, $\Sigma_X$, $\tau_{\rm response}$ |
| **P4** | Organizational constraints can materially reduce the feasible action set and alter controlled viability. | $H_2$ | $\mathcal U(z_I,z_O)$ and $\mathcal V_{\rm sus}^{u,T}$ |
| **P5** | Response timing relative to cascade/viability clocks contains decision-relevant information, but timing alone is not sufficient for successful control. | $H_2,H_3$ | $\Pi_R$, $S_{\mathcal V}$, $S_K$, $\Pi_{\mathcal V}$, $\Pi_K$ |
| **P6** | The proposed Riemannian viability margin provides information beyond normalized Euclidean/weighted distance. | $H_3$ | $\rho_E$ vs. $\rho_g$ |
| **P7** | Interdependency sensitivity can identify interfaces whose perturbation materially changes viability-related outcomes. | Supporting Stage-5/6 diagnostic; **not primary H4** | $S_{ij}^{\mathcal V}(\Delta\theta)$ |
| **P8** | Reduced viability-state models can preserve or conservatively bound conclusions of the higher-dimensional Stage-3 system. | $H_3$ / implementation validity | $Y_V=\mathcal P_V(Y)$ vs. full state |
| **P9** | A regime can be controllably viable over the Stage-5 horizon yet remain inadequate under long-horizon requirements or adaptation limits. | Supporting Stage-6/7 proposition; **not primary H5** | $\mathcal R_5$ vs. $(\Lambda_{\rm LT},\mathbf d_6)$ |
| **P10** | Persistent critical interdependencies can create regime-level lock-in that may justify testing structural adaptation/transformation against repeated recovery. | Conditional Stage-7 extension; **not primary H4/H5** | repeated $S_{ij}^{\mathcal V}$, $\mathcal D_{\mathfrak I}$ and transformation alternatives |

---

## 3. Stage-4 model comparisons

When Stage-4 information/organization effects are tested independently of the primary-H2 nested models, the frozen Stage-4 variants are

```math
\mathscr M_0
\rightarrow
\mathscr M_1
\rightarrow
\mathscr M_2
\rightarrow
\mathscr M_3,
```

where

| Model | Assumption |
|---|---|
| $\mathscr M_0$ | perfect observation + instantaneous organization |
| $\mathscr M_1$ | imperfect/delayed information |
| $\mathscr M_2$ | imperfect information + organizational constraints |
| $\mathscr M_3$ | full closed-loop P–T–I–O representation |

The symbols $\mathscr M_k$ denote **model variants**. They are intentionally distinct from the Stage-2 mechanism $M_{ij}$ and Stage-7 infrastructure regime $\mathfrak M_k$.

---

## 4. Stage-5 baseline-versus-extension tests

The normalized geometric baseline is

```math
\rho_E(Y)
=
d\!\left(\widetilde Y,\partial\widetilde{\mathcal V}\right),
```

while the proposed extension is

```math
\rho_g(Y)
=
d_{g_\psi}\!\left(Y,\partial\mathcal V_{\rm sus}^{u,T}\right).
```

The extension is supported only if its added complexity produces reproducible value under a predeclared metric.

Likewise,

```math
S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response},
\qquad
S_K=T_K-\tau_{\rm response}
```

must be tested as diagnostics rather than assumed to be universal resilience laws.

---

## 5. Stage-6 falsification logic

Stage 6 must not infer transformation from one Stage-5 quantity:

```math
\rho\text{ small}\not\Rightarrow\text{transform},
```

```math
\mathcal V\text{ small}\not\Rightarrow\text{transform},
```

```math
\text{hazard/failure occurrence}\not\Rightarrow\text{transform}.
```

The frozen translation is

```math
\Phi_{\rm ST}
:
(\mathcal R_5,\Lambda_{\rm LT},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol\zeta_T).
```

A Stage-6 diagnosis must survive counterfactual comparisons against restoration within the current regime, feasible incremental adaptation, sensitivity to long-horizon requirements, alternative lock-in/maladaptation interpretations and uncertainty in Stage-5 evidence.

---

## 6. Stage-7 validation obligations

The Stage-7 regime transition is

```math
\mathfrak M_{k+1}
=
\mathcal T_{\mathbf a_k}(\mathfrak M_k,\xi_k),
```

with strategic action

```math
\mathbf a_k
=
\begin{bmatrix}
a_k^P\\a_k^T\\a_k^I\\a_k^O\\a_k^{\mathfrak I}
\end{bmatrix},
```

and frozen Stage-7 object

```math
\mathfrak P_{\rm ST}
=
\left(
\mathbb G_{\rm ST},
\boldsymbol\pi_{\rm ST},
\Omega,
\mathcal A^{\rm feas},
\mathbf J,
\mathbb M_{\rm sus}
\right).
```

The principal adaptive-vs-fixed performance claim is tested by $H_5$. Stage-7 implementation must additionally verify that candidate actions:

- satisfy Stage-6 requirements rather than merely improve a graph statistic;
- remain dynamically feasible after Stage-3 replay;
- respect Stage-4 information/organizational implementation limits;
- satisfy the declared Stage-5 viability/recovery requirement;
- do not create unacceptable new sustainability/equity failures;
- remain robust to the declared uncertainty/scenario assumptions.

---

## 7. Decision discipline

A hypothesis or proposition is considered **supported only within the tested model, scenarios and data** when:

1. comparisons and metrics are declared before final interpretation;
2. confirmatory thresholds/statistical rules are fixed *a priori*;
3. uncertainty is propagated when it can materially change conclusions;
4. baseline and ablation models are calibrated fairly;
5. sensitivity checks do not reverse conclusions without explanation;
6. added mathematical complexity produces measurable value;
7. inference is limited to the analyzed evidence domain.

---

## 8. Failure criteria

A thesis construct must be rejected, simplified or qualified when its critical test shows no material improvement, unstable rankings, non-identifiability, excessive sensitivity, violation of physical constraints or dependence on unsupported assumptions.

Therefore,

```math
\text{more mathematical complexity}
\not\Rightarrow
\text{better engineering explanation},
```

and

```math
\text{framework freeze}
\not\Rightarrow
\text{empirical validation}.
```

---

## 9. Next confirmatory task

Before final confirmatory simulation, construct the **Hypothesis Specification Matrix** for $H_1$–$H_5$ and freeze, for each hypothesis:

- theory and causal mechanism;
- independent/manipulated variables;
- outcome variables;
- baseline/rival model;
- boundary conditions;
- scenario/uncertainty domain;
- prediction and meaningful effect threshold $\delta_i$;
- critical test and ablation;
- falsification criterion;
- planned analysis and sensitivity checks.

The matrix is the bridge from the frozen conceptual framework to confirmatory numerical validation.
