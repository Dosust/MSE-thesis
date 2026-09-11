# Scientific Propositions and Falsification Plan

**Status:** CURRENT / SYNCHRONIZED WITH STAGES 1–7 AND PRIMARY HYPOTHESES  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Evidence rule:** A proposition is a testable supporting claim, diagnostic, or sub-test. The five primary confirmatory hypotheses are defined separately in [`RESEARCH_HYPOTHESES.md`](RESEARCH_HYPOTHESES.md).  
**Framework rule:** Frozen framework objects remain `[P]` where they are thesis constructs until their scientific value is demonstrated through the prespecified hypothesis tests.

---

## 1. Relationship between hypotheses and propositions

The canonical primary hypothesis set is

$$
\mathbb H=\{H_1,H_2,H_3,H_4,H_5\}.
$$

The propositions in this file are **not ten additional primary hypotheses**. They are subordinate falsifiable claims used to operationalize, stress-test, explain, or decompose the five primary hypotheses.

The hierarchy is therefore

$$
\text{theoretical hypothesis }H_{\rm SYS}
\rightarrow
\{H_1,\ldots,H_5\}
\rightarrow
\{P_1,\ldots,P_{10}\}
\rightarrow
\text{tests / ablations / falsification}.
$$

Numerical thresholds $\delta_1,\ldots,\delta_5$ remain unset until justified *a priori* in the Hypothesis Specification Matrix.

---

## 2. Proposition registry

| ID | Testable proposition | Primary hypothesis supported | Main mathematical object / contrast |
|---|---|---:|---|
| **P1** | Explicit P–T–I–O representation adds explanatory or predictive value beyond a physical P–T-only model when information and organizational constraints materially affect response. | $H_2$ | physical-only vs. full P–T–I–O models |
| **P2** | Dynamic interdependencies produce materially different trajectories or viability conclusions from static coupling under some operating regimes. | $H_1$ | $\mathcal G(t)$, $w_{ij}(t)$, $a_{ij}(t)$ vs. static counterparts |
| **P3** | Information degradation can materially alter control outcome through observability, estimation error, or response delay. | $H_2$ | $z_I$, $\widehat X$, $\Sigma_X$, $\tau_{\rm response}$ |
| **P4** | Organizational constraints can materially reduce the feasible action set and alter controlled viability. | $H_2$ | $\mathcal U(z_I,z_O)$ and $\mathcal V_{\rm sus}^{u,T}$ |
| **P5** | Response timing relative to cascade/viability clocks contains decision-relevant information, but timing alone is not sufficient for successful control. | $H_2$, $H_3$ | $\Pi_R$, $S_{\mathcal V}$, $S_K$, $\Pi_{\mathcal V}$, $\Pi_K$ |
| **P6** | The proposed Riemannian viability margin provides information beyond normalized Euclidean/weighted distance. | $H_3$ | $\rho_E$ vs. $\rho_g$ |
| **P7** | Interdependency sensitivity can identify interfaces whose perturbation materially changes viability-related outcomes. | $H_4$ | $S_{ij}^{\mathcal V}(\Delta\theta)$ |
| **P8** | Reduced viability-state models can preserve or conservatively bound conclusions of the higher-dimensional Stage-3 system. | $H_3$, implementation validity | $Y_V=\mathcal P_V(Y)$ vs. full model |
| **P9** | A regime can be controllably viable over the Stage-5 horizon yet remain inadequate under longer-horizon sustainability, equity, lock-in, or adaptation-limit requirements. | $H_5$ / Stage-6 validity | $\mathcal R_5$ vs. $(\Lambda_{\rm LT},\mathbf d_6)$ |
| **P10** | Persistent critical interdependencies can create regime-level lock-in that makes repeated recovery inferior to structural adaptation/transformation. | $H_4$, $H_5$ | repeated $S_{ij}^{\mathcal V}$, $\mathcal D_{\mathfrak I}$, transformation alternatives |

---

## 3. Core model comparisons

For information/organization effects, nested comparisons may use

$$
\mathscr M_0
\rightarrow
\mathscr M_1
\rightarrow
\mathscr M_2
\rightarrow
\mathscr M_3,
$$

where

| Model | Assumption |
|---|---|
| $\mathscr M_0$ | perfect observation + instantaneous organization |
| $\mathscr M_1$ | imperfect/delayed information |
| $\mathscr M_2$ | imperfect information + organizational constraints |
| $\mathscr M_3$ | full closed-loop P–T–I–O representation |

The intended contrasts are

$$
\mathscr M_1-\mathscr M_0=\text{information effect},
$$

$$
\mathscr M_2-\mathscr M_1=\text{organizational effect},
$$

$$
\mathscr M_3-\mathscr M_0=\text{full coupled-response effect}.
$$

The symbols $\mathscr M_k$ denote model variants and are intentionally distinct from the Stage-2 mechanism symbol $M_{ij}$ and Stage-7 regime symbol $\mathcal M_k$.

---

## 4. Stage-5 baseline-versus-extension tests

The geometric baseline and proposed extension are

$$
\rho_E(Y)
=
d\!\left(\widetilde Y,\partial\widetilde{\mathcal V}\right),
$$

$$
\rho_g(Y)
=
d_{g_\psi}\!\left(Y,\partial\mathcal V\right).
$$

The proposed extension is supported only if the added complexity produces reproducible value under a declared metric.

Likewise,

$$
S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response},
\qquad
S_K=T_K-\tau_{\rm response}
$$

must be tested as diagnostics rather than assumed to be universal laws.

---

## 5. Stage-6 falsification logic

Stage 6 must not infer transformation from a single Stage-5 quantity:

$$
\rho\text{ small}\not\Rightarrow\text{transform},
$$

$$
\mathcal V\text{ small}\not\Rightarrow\text{transform},
$$

$$
\text{hazard/failure occurrence}\not\Rightarrow\text{transform}.
$$

The frozen translation is

$$
\Phi_{\rm ST}
:
(\mathcal R_5,\Lambda_{\rm LT},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol\zeta_T).
$$

A Stage-6 diagnosis must survive counterfactual comparisons against restoration within the current regime, feasible incremental adaptation, sensitivity to long-horizon requirements, alternative lock-in/maladaptation interpretations, and uncertainty in Stage-5 evidence.

---

## 6. Stage-7 validation obligations

Stage 7 is frozen around

$$
\mathcal M_{k+1}
=
\mathcal T_{a_k}(\mathcal M_k,\xi_k),
$$

with

$$
a_k=[a_k^P,a_k^T,a_k^I,a_k^O,a_k^{\mathfrak I}],
$$

and

$$
\mathfrak P_{\rm ST}
=
(\mathbb G_{\rm ST},\boldsymbol\pi,\Omega,\mathcal A^{\rm feas},\mathbf J,\mathbb M_{\rm sus}).
$$

The principal Stage-7 performance claim is no longer an unregistered proposition: it is explicitly tested by **$H_5$**, which compares adaptive trigger-based pathways against the best comparable fixed pathway under deep uncertainty.

At minimum, Stage-7 implementation must also verify that transformation actions satisfy Stage-6 requirements, remain physically/dynamically feasible after Stage-3 replay, respect information/organizational implementation limits, improve or preserve Stage-5 viability as required, and do not create unacceptable new sustainability/equity failures.

---

## 7. Decision discipline

A hypothesis or proposition is considered **supported under the tested model, scenarios, and data** only when:

1. the comparison and metric are declared before interpreting final results;
2. numerical thresholds or statistical decision rules are fixed *a priori*;
3. uncertainty is propagated where it can materially change conclusions;
4. baseline and ablation models are calibrated fairly;
5. sensitivity checks do not reverse conclusions without explanation;
6. added mathematical complexity is justified by measurable value;
7. inference is limited to the analyzed evidence domain.

---

## 8. Failure criteria

A thesis construct must be **rejected, simplified, or qualified** when its critical test shows no material improvement, unstable rankings, non-identifiability, excessive sensitivity, violation of physical constraints, or dependence on unsupported assumptions.

Therefore,

$$
\text{more mathematical complexity}
\not\Rightarrow
\text{better engineering explanation},
$$

and

$$
\text{framework freeze}
\not\Rightarrow
\text{empirical validation}.
$$

---

## 9. Next confirmatory task

Before final simulation, construct the **Hypothesis Specification Matrix** for $H_1$–$H_5$ and freeze, for each hypothesis:

- theory;
- causal mechanism;
- independent/manipulated variables;
- outcome variables;
- baselines;
- boundary conditions;
- scenario/uncertainty domain;
- prediction;
- rival hypothesis;
- critical test;
- falsification criterion;
- justified effect threshold $\delta_i$;
- planned analysis and sensitivity checks.

This matrix is the bridge from the frozen conceptual framework to confirmatory numerical validation.
