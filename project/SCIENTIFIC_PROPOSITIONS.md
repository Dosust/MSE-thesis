# Scientific Propositions and Falsification Plan

**Status:** CURRENT / SYNCHRONIZED WITH STAGES 1–7  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Evidence rule:** A proposition is a testable thesis claim, not a statement of truth before analysis.  
**Framework rule:** Stage-7 objects are now frozen as framework definitions but retain `[P]` status where they are thesis constructs and must be tested numerically.

The propositions below are aligned with the current P–T–I–O architecture and the frozen seven-stage mathematical framework.

## 1. Proposition registry

| ID | Testable proposition | Mathematical object / contrast | Primary falsification or stress test |
|---|---|---|---|
| **P1** | Explicit P–T–I–O representation adds explanatory or predictive value beyond a physical P–T-only model when information and organizational constraints materially affect response. | $\mathscr M_{PT}$ vs. $\mathscr M_{PTIO}$ | Hold scenario/data conditions fixed; compare out-of-sample state, timing, service and intervention outcomes. Reject/qualify if added layers do not improve justified metrics after complexity control. |
| **P2** | Dynamic interdependencies produce materially different trajectories or viability conclusions from static coupling under some operating regimes. | $\mathcal G(t)$ / $w_{ij}(t),a_{ij}(t)$ vs. static counterparts | Freeze coupling parameters/topology and compare $Y(t)$, event order, $T_C(j)$, $\mathcal V$ and margins. Reject/qualify if differences remain below prespecified tolerances. |
| **P3** | Information degradation can materially alter control outcome through observability, estimation error or response delay. | $z_I$, $\widehat X$, $\Sigma_X$, $\tau_{\rm response}$ | Sweep delay, loss, freshness and availability; compare estimation error and closed-loop outcomes against full-information baselines. |
| **P4** | Organizational constraints can materially reduce the feasible action set and alter controlled viability. | $\mathcal U(z_I,z_O)$ and $\mathcal V_{\rm sus}^{u,T}$ | Compare ideal organization with realistic authority, resource, workforce, coordination and mobilization limits. Reject/qualify if viable-set/outcome differences are negligible. |
| **P5** | Response timing relative to cascade/viability clocks contains decision-relevant information, but timing alone is not sufficient for successful control. | $\Pi_R$, $S_{\mathcal V}$, $S_K$, $\Pi_{\mathcal V}$, $\Pi_K$ | Test whether timing diagnostics discriminate successful/failed response after conditioning on observability, controllability, resource feasibility and action quality. |
| **P6** | The proposed Riemannian viability margin provides information beyond normalized Euclidean/weighted distance. | $\rho_E$ vs. $\rho_g=d_{g_\psi}(Y,\partial\mathcal V)$ | Compare warning performance, boundary proximity, intervention ranking, robustness and out-of-sample usefulness. Reject if $\rho_g$ does not outperform justified simpler baselines. |
| **P7** | Interdependency sensitivity can identify interfaces whose perturbation materially changes viability-related outcomes. | $S_{ij}^{\mathcal V}(\Delta\theta)$ | Perturb $\theta_{ij}=(w_{ij},\delta_{ij},\tau_{ij},a_{ij})$, recompute viability functionals and test ranking stability under uncertainty and perturbation size. |
| **P8** | Reduced viability-state models can preserve or conservatively bound conclusions of the higher-dimensional Stage-3 system. | $Y_V=\mathcal P_V(Y)$ and reduced/full viability outputs | Compare constraint violations, viable-set classification, temporal margins and interface rankings. Reject a reduction that creates unjustified false-safe classifications or unstable conclusions. |
| **P9** | A regime can be controllably viable over the Stage-5 horizon yet remain inadequate under longer-horizon sustainability, equity, lock-in or adaptation-limit requirements. | Stage-5 $\mathcal R_5$ vs. Stage-6 $(\Lambda_{\rm LT},\mathbf d_6)$ | Construct matched cases in which Stage-5 viability is satisfactory while one or more long-horizon requirements remain materially violated. Reject/qualify if Stage-6 diagnosis adds no decision-relevant distinction beyond Stage 5. |
| **P10** | Persistent critical interdependencies can create a regime-level lock-in that makes repeated recovery inferior to structural adaptation/transformation. | repeated $S_{ij}^{\mathcal V}$ + interdependency-lock-in cycle + $\mathcal D_{\mathfrak I}$ | Compare repeated restoration of the original mechanism against admissible structural modifications under matched hazards; test long-horizon viability, sustainability, equity, cost and new-vulnerability effects. |

These ten propositions remain the current registered falsifiable claims. Freezing Stage 7 does **not** automatically create additional empirical claims. Any Stage-7-specific performance proposition must be separately registered before testing.

---

## 2. Core model comparisons

The Stage-4 nested control comparison is

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
| $\mathscr M_0$ | Perfect observation + instantaneous organization |
| $\mathscr M_1$ | Imperfect/delayed information |
| $\mathscr M_2$ | Imperfect information + organizational constraints |
| $\mathscr M_3$ | Full closed-loop P–T–I–O representation |

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

The symbols $\mathscr M_k$ denote model variants and are intentionally distinct from the Stage-2 mechanism symbol $M_{ij}$ and Stage-7 infrastructure-regime symbol $\mathcal M_k$.

---

## 3. Stage-5 baseline-versus-extension tests

The geometric baseline and proposed extension are

$$
\rho_E(Y)=d\!\left(\widetilde Y,\partial\widetilde{\mathcal V}\right),
$$

$$
\rho_g(Y)=d_{g_\psi}\!\left(Y,\partial\mathcal V\right).
$$

The proposed extension is supported only if its added complexity produces reproducible value under a declared metric.

Likewise,

$$
S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response},
\qquad
S_K=T_K-\tau_{\rm response}
$$

must be tested as diagnostics rather than assumed to be laws of resilience.

---

## 4. Stage-6 falsification logic

Stage 6 is not allowed to infer transformation from one Stage-5 quantity alone. In particular,

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

A Stage-6 transformation diagnosis must survive counterfactual comparisons against restoration within the current regime, feasible incremental adaptation, sensitivity to long-horizon requirements, alternative lock-in/maladaptation interpretations, and uncertainty in Stage-5 evidence.

---

## 5. Stage-7 frozen framework objects and validation obligations

Stage 7 is now frozen around the infrastructure-regime object

$$
\mathcal M_k
=
(\mathcal S_k,\mathcal G_k,\mathfrak I_k,F_k,\boldsymbol\theta_k,\mathcal U_k),
$$

and the strategic transformation

$$
\mathcal M_{k+1}
=
\mathcal T_{a_k}(\mathcal M_k,\xi_k),
$$

where

$$
a_k=[a_k^P,a_k^T,a_k^I,a_k^O,a_k^{\mathfrak I}].
$$

The Stage-7 fundamental object is

$$
\mathfrak P_{\rm ST}
=
(\mathbb G_{\rm ST},\boldsymbol\pi,\Omega,\mathcal A^{\rm feas},\mathbf J,\mathbb M_{\rm sus}).
$$

These are framework definitions. Their `[P]` status means their scientific value must still be tested. At minimum, Stage-7 implementation must check:

- whether adaptive policies outperform or materially improve upon justified fixed-sequence baselines under the tested uncertainty set;
- whether transformation actions satisfy Stage-6 requirements rather than merely improve a topology metric;
- whether candidate regimes remain physically/dynamically feasible after Stage-3 replay;
- whether information and organizational constraints preserve implementability;
- whether Stage-5 viability and Stage-6 adequacy improve without unacceptable new vulnerabilities;
- whether robust-Pareto results are stable to objective definitions, scenario sets and uncertainty assumptions;
- whether removing/postponing a pathway intervention changes outcomes materially in counterfactual ablation.

Freezing the framework therefore fixes **what must be tested**, not the outcome of those tests.

---

## 6. Decision discipline

A proposition is considered **supported under the tested model, scenarios and data** only when all of the following hold:

1. the mathematical comparison and evaluation metric are declared before interpreting results;
2. numerical tolerances or statistical decision rules are reported;
3. uncertainty is propagated where it can materially change the result;
4. baseline and ablation models are calibrated fairly;
5. sensitivity checks do not reverse the conclusion without explanation;
6. added model complexity is justified by measurable explanatory, predictive, control, viability, transition-diagnostic or transformation-pathway value;
7. the scope of inference is limited to the evidence actually analyzed.

---

## 7. Failure criteria

A thesis construct must be **rejected, simplified or qualified** when its falsification test shows no material improvement, unstable rankings, non-identifiability, excessive sensitivity, violation of physical constraints or dependence on unsupported assumptions.

In particular,

$$
\text{more mathematical complexity}
\not\Rightarrow
\text{better engineering explanation}.
$$

and

$$
\text{framework freeze}
\not\Rightarrow
\text{empirical validation}.
$$

---

## 8. Complete framework context

The frozen chain is

$$
\boxed{
\underbrace{\mathcal S}_{1}
\rightarrow
\underbrace{\mathfrak I}_{2}
\rightarrow
\underbrace{F_{\mathcal G}^{m}}_{3}
\rightarrow
\underbrace{X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u}_{4}
\rightarrow
\underbrace{K_{\rm sus},\mathcal V,\rho,T_{\mathcal V},T_K}_{5}
\rightarrow
\underbrace{\Phi_{\rm ST}\rightarrow(c_6,\mathcal D_6,\boldsymbol\zeta_T)}_{6}
\rightarrow
\underbrace{\mathfrak P_{\rm ST}}_{7}
}.
$$

Every Stage-7 candidate must be replayed through Stages 1–6 before acceptance.

---

## 9. Non-claims

The thesis does not infer novelty from literature counts, repository size, visual complexity, framework freeze or the mere combination of established methods. Novelty and contribution must be demonstrated through explicit comparison, falsification and evidence.

Historical P–W–T–SW or waste–drainage propositions are superseded and are not part of the current P–T–I–O proposition registry.
