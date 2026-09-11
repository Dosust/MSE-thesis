# Scientific Propositions and Falsification Plan

**Status:** CURRENT / SYNCHRONIZED WITH STAGES 1–5  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Evidence rule:** A proposition is a testable thesis claim, not a statement of truth before analysis.

The propositions below are aligned with the current P–T–I–O architecture and the frozen Stage-2 to Stage-5 mathematical objects.

## 1. Proposition registry

| ID | Testable proposition | Mathematical object / contrast | Primary falsification or stress test |
|---|---|---|---|
| **P1** | Explicit P–T–I–O representation adds explanatory or predictive value beyond a physical P–T-only model when information and organizational constraints materially affect system response. | $\mathscr M_{PT}$ vs. $\mathscr M_{PTIO}$ | Hold scenario/data conditions fixed; compare out-of-sample state, timing, service, and intervention outcomes. Reject or qualify if added layers do not improve justified metrics after complexity control. |
| **P2** | Dynamic interdependencies produce materially different trajectories or viability conclusions from static coupling under some operating regimes. | $\mathcal G(t)$ / $w_{ij}(t),a_{ij}(t)$ vs. static counterparts | Freeze coupling parameters/topology and compare $Y(t)$, event order, $T_C(j)$, $\mathcal V$, and margins. Reject or qualify if differences remain below prespecified tolerances. |
| **P3** | Information degradation can materially alter control outcome through observability, estimation error, or response delay. | $z_I$, $\widehat X$, $\Sigma_X$, $\tau_{\rm response}$ | Sweep delay, loss, freshness, and availability; compare estimation error and closed-loop outcomes against full-information baselines. |
| **P4** | Organizational constraints can materially reduce the feasible action set and alter controlled viability. | $\mathcal U(z_I,z_O)$ and $\mathcal V_{\rm sus}^{u,T}$ | Compare unconstrained/ideal organization with realistic authority, resource, workforce, coordination, and mobilization limits. Reject or qualify if viable-set or outcome differences are negligible. |
| **P5** | Response timing relative to cascade/viability clocks contains decision-relevant information, but timing alone is not sufficient for successful control. | $\Pi_R$, $S_{\mathcal V}$, $S_K$, $\Pi_{\mathcal V}$, $\Pi_K$ | Test whether timing diagnostics discriminate successful/failed response across scenarios after conditioning on observability, controllability, resource feasibility, and action quality. |
| **P6** | The proposed Riemannian viability margin provides information beyond normalized Euclidean/weighted distance. | $\rho_E$ vs. $\rho_g=d_{g_\psi}(Y,\partial\mathcal V)$ | Compare boundary proximity, warning performance, intervention ranking, robustness, and out-of-sample usefulness. Reject if $\rho_g$ does not outperform justified simpler baselines. |
| **P7** | Interdependency sensitivity can identify interfaces whose perturbation materially changes viability-related outcomes. | $S_{ij}^{\mathcal V}(\Delta\theta)$ | Perturb $\theta_{ij}=(w_{ij},\delta_{ij},\tau_{ij},a_{ij})$, recompute selected viability functionals, and test ranking stability under uncertainty and perturbation size. |
| **P8** | Reduced viability-state models can preserve or conservatively bound conclusions of the higher-dimensional Stage-3 system. | $Y_V=\mathcal P_V(Y)$ and reduced/full viability outputs | Compare constraint violations, viable-set classification, temporal margins, and interface rankings. Reject a reduction that creates unjustified false-safe classifications or unstable conclusions. |

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

and

$$
\mathscr M_3-\mathscr M_0=\text{full coupled-response effect}.
$$

The symbols $\mathscr M_k$ denote model variants and are intentionally distinct from the Stage-2 causal mechanism symbol $M_{ij}$.

---

## 3. Stage-5 baseline-versus-extension tests

The geometric baseline and proposed extension are

$$
\rho_E(Y)
=
d\!\left(\widetilde Y,\partial\widetilde{\mathcal V}\right),
$$

and

$$
\rho_g(Y)
=
d_{g_\psi}\!\left(Y,\partial\mathcal V\right).
$$

The proposed extension is supported only if its added complexity produces reproducible value under a declared metric.

Likewise, the timing diagnostics

$$
S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response},
\qquad
S_K=T_K-\tau_{\rm response}
$$

must be tested as diagnostics rather than assumed to be laws of resilience.

---

## 4. Decision discipline

A proposition is considered **supported under the tested model, scenarios, and data** only when all of the following hold:

1. the mathematical comparison and evaluation metric are declared before interpreting results;
2. numerical tolerances or statistical decision rules are reported;
3. uncertainty is propagated where it can materially change the result;
4. baseline and ablation models are calibrated fairly;
5. sensitivity checks do not reverse the conclusion without explanation;
6. added model complexity is justified by measurable explanatory, predictive, control, or viability value;
7. the scope of inference is limited to the evidence actually analyzed.

---

## 5. Failure criteria

A thesis construct must be **rejected, simplified, or qualified** when the corresponding falsification test shows no material improvement, unstable rankings, non-identifiability, excessive sensitivity, violation of physical constraints, or dependence on unsupported assumptions.

In particular,

$$
\text{more mathematical complexity}
\not\Rightarrow
\text{better engineering explanation}.
$$

---

## 6. Non-claims

The thesis does not infer novelty from literature counts, repository size, visual complexity, or the mere combination of established methods. Novelty and contribution must be demonstrated through explicit comparison, falsification, and evidence.

Historical P–W–T–SW or waste–drainage propositions are superseded and are not part of the current P–T–I–O proposition registry.
