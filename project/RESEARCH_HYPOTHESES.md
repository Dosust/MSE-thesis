# Research Hypotheses — Complete Seven-Stage Framework

![Framework](https://img.shields.io/badge/framework-1--7%20FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/hypothesis%20logic-FROZEN-1A7F37)
![Thresholds](https://img.shields.io/badge/numerical%20thresholds-NOT%20SET-9A6700)

**Status:** CANONICAL HYPOTHESIS ARCHITECTURE / LOGIC FROZEN  
**Date:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Framework:** complete frozen seven-stage P–T–I–O thesis framework  
**Citation standard:** APA 7th edition author–date  
**Change rule:** The scientific logic of the five primary hypotheses is frozen. Numerical thresholds $\delta_1,\ldots,\delta_5$, exact metrics, scenario ensembles, and statistical decision rules must be specified *a priori* before confirmatory testing.

> **Authority rule:** This file defines the five primary confirmatory hypotheses. `SCIENTIFIC_PROPOSITIONS.md` remains the broader proposition/falsification registry; its entries are subordinate tests, mechanisms, diagnostics, or supporting claims.

> **Notation rule:** Hypothesis-specific model variants use dedicated script symbols so they cannot be confused with the Stage-2 causal mechanism $M_{ij}$, the Stage-4 model variants $\mathscr M_k$, or the Stage-7 infrastructure regime $\mathfrak M_k$.

---

## 1. Hypothesis architecture

The thesis hypotheses follow

$$
\text{Theory}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Hypothesis}
\rightarrow
\text{Prediction}
\rightarrow
\text{Baseline}
\rightarrow
\text{Falsification}.
$$

The framework uses **five primary hypotheses**, rather than one hypothesis per stage.

---

## 2. Overarching scientific hypothesis

### $H_{\rm SYS}$

Infrastructure resilience and sustainable transformation cannot be characterized adequately from physical-network structure alone when causal interdependencies, dynamics, information, organization, and feasible control materially influence propagation, viability, and transformation pathways.

$H_{\rm SYS}$ is a theoretical organizing hypothesis. It is not accepted or rejected through one isolated $p$-value; it is decomposed into the five falsifiable hypotheses below.

---

## 3. $H_1$ — Dynamic interdependency hypothesis

### Scientific question

Does representing interdependencies as **dynamic causal mechanisms** materially change predicted disruption propagation relative to independent or static-coupling representations?

Stage 2 defines

$$
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right),
$$

and Stage 3 maps accepted mechanisms into coupled dynamics:

$$
\mathfrak I
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Y(t).
$$

### Hypothesis

**$H_1$:** Under coupled P–T disturbances, explicitly modeling dynamic interdependency mechanisms produces materially different cascade and service trajectories from independent or static-coupling models.

### Prespecified baselines

Use hypothesis-specific model labels

$$
\mathscr C_0=\text{independent }P+T,
$$

$$
\mathscr C_1=\text{static coupled }P\text{--}T,
$$

$$
\mathscr C_2=\text{dynamic causal }P\text{--}T\text{ coupling}.
$$

Let the cascade/service outcome vector be

$$
Z_C
=
\begin{bmatrix}
T_C\\
N_{\rm fail}\\
L_{\rm service}\\
T_{\rm recovery}
\end{bmatrix}.
$$

For every **prespecified** baseline $b\in\{0,1\}$ included in the confirmatory test, define

$$
D_b
=
D\!\left(
Z_C^{\mathscr C_2},
Z_C^{\mathscr C_b}
\right).
$$

The confirmatory prediction is

$$
D_b\ge\delta_1,
$$

where $D$ is a declared trajectory/performance difference metric and $\delta_1$ is a scientifically meaningful threshold fixed before final testing.

### Falsification criterion

$H_1$ is challenged when the dynamic model fails to exceed the prespecified meaningful-difference threshold against the declared baseline contrasts across the declared scenario domain. The exact aggregation rule across scenarios must be fixed in the Hypothesis Specification Matrix.

---

## 4. $H_2$ — Information–organization hypothesis

### Scientific question

Do informational and organizational states materially change feasible response and recovery relative to a physical-only representation?

The Stage-4 causal spine is

$$
X
\rightarrow y
\rightarrow I
\rightarrow\widehat X
\rightarrow O
\rightarrow u
\rightarrow X.
$$

Information degradation changes latency, freshness, availability and estimation error; organizational limitations change authority, coordination, resources and mobilization. These mechanisms restrict

$$
\mathcal U(z_I,z_O)
$$

and alter response timing, action quality and the resulting physical trajectory.

### Hypothesis

**$H_2$:** Information degradation and organizational constraints materially alter the feasible response set, cascade–response competition, and recovery of the coupled infrastructure system relative to a physical-only representation.

### Nested models

Use a dedicated H2 notation:

$$
\mathscr N_0=P+T,
$$

$$
\mathscr N_1=P+T+I,
$$

$$
\mathscr N_2=P+T+I+O.
$$

Then

$$
\mathscr N_1-\mathscr N_0
=\text{information-layer effect},
$$

$$
\mathscr N_2-\mathscr N_1
=\text{organizational-layer effect}.
$$

Representative intermediate responses are

$$
\operatorname{RMSE}(\widehat X,X),
\qquad
\tau_{\rm response},
\qquad
u(t),
$$

with downstream outcomes such as

$$
L_{\rm service},
\qquad
T_C,
\qquad
T_{\rm recovery}.
$$

For a prespecified resilience-output vector $Z_R$,

$$
D\!\left(
Z_R^{\mathscr N_2},
Z_R^{\mathscr N_0}
\right)
\ge\delta_2.
$$

For sequential non-overlapping response processes,

$$
\begin{aligned}
\tau_{\rm response}={}&
\tau_{\rm sense}
+\tau_{\rm comm}
+\tau_{\rm est}
+\tau_{\rm decision}\\
&+\tau_{\rm coord}
+\tau_{\rm mobilization}
+\tau_{\rm act}.
\end{aligned}
$$

Overlapping processes require the corresponding critical-path completion time rather than the arithmetic sum.

### Falsification criterion

$H_2$ is challenged if prespecified perturbations of $I$ and $O$ produce changes below the declared meaningful-effect threshold in $\mathcal U$, response timing, and downstream system outcomes over the test domain.

---

## 5. $H_3$ — Controlled-viability hypothesis

### Scientific question

Do Stage-5 viability quantities add decision-relevant information beyond conventional service-loss and recovery metrics?

Two states may have similar current service,

$$
S(Y_1)\approx S(Y_2),
$$

but different future maintainability:

$$
Y_1\in\mathcal V,
\qquad
Y_2\notin\mathcal V.
$$

Thus

$$
\text{current performance}
\neq
\text{future maintainability}.
$$

### Hypothesis

**$H_3$:** Controlled-viability quantities distinguish impending loss of maintainability that is not fully captured by conventional instantaneous service or recovery metrics.

### Competing predictor sets

$$
Q_{\rm conventional}
=
\{S(t),L_{\rm service},T_{\rm recovery}\},
$$

$$
Q_{\rm viability}
=
\{\rho,T_{\mathcal V},T_K,S_{\mathcal V}\}.
$$

For a declared future-failure outcome

$$
Y_{\rm fail}
=
\mathbf 1\!\left\{Y(t+\Delta)\notin K_{\rm sus}\right\},
$$

the confirmatory prediction is

$$
\operatorname{Skill}
\!\left(Q_{\rm conventional}\cup Q_{\rm viability}\right)
-
\operatorname{Skill}
\!\left(Q_{\rm conventional}\right)
\ge\delta_3.
$$

`Skill` must be defined *a priori* through a justified prediction-error, discrimination, calibration, warning-lead-time, or related metric.

A matched-state test should seek $Y_a,Y_b$ satisfying

$$
S(Y_a)\approx S(Y_b),
\qquad
\rho(Y_a)\neq\rho(Y_b),
$$

and then test whether their subsequent futures differ as predicted.

### Falsification criterion

If viability quantities fail to improve the prespecified predictive/decision metric beyond conventional service measures by at least $\delta_3$, their additional complexity is not supported for the tested application.

---

## 6. $H_4$ — Interface-criticality hypothesis

### Scientific question

Can viability-sensitive interface rankings identify more valuable intervention targets than static structural rankings?

For Stage-2 interface parameters

$$
\theta_{ij}
=(w_{ij},\delta_{ij},\tau_{ij},a_{ij}),
$$

perturbation propagates through

$$
\theta_{ij}
\rightarrow
F
\rightarrow
\mathcal V
\rightarrow
\rho,
$$

and produces the Stage-5 sensitivity $S_{ij}^{\mathcal V}$.

### Hypothesis

**$H_4$:** Interfaces ranked as highly critical by viability sensitivity identify interventions that improve a prespecified controlled-viability functional more effectively than rankings based only on static structural centrality.

### Competing rankings

$$
R_1=\text{degree-based ranking},
\qquad
R_2=\text{betweenness-based ranking},
$$

$$
R_3=\text{flow-based ranking},
\qquad
R_4=S_{ij}^{\mathcal V}.
$$

Because $\mathcal V$ is a set, the confirmatory comparison must use a **declared scalar viability functional** $\mathcal M_{\mathcal V}$, for example a normalized viable-set measure, a boundary margin, or another justified scalar summary.

For ranking $R_r$ define

$$
\Delta\mathcal M_{\mathcal V}^{(r)}
=
\mathcal M_{\mathcal V}^{\rm after}(R_r)
-
\mathcal M_{\mathcal V}^{\rm before}.
$$

Additional secondary outcomes may include

$$
\Delta\rho,
\qquad
\Delta T_{\mathcal V},
\qquad
\Delta L_{\rm service}.
$$

Let $\operatorname{Agg}_{\Omega}$ denote a **prespecified scenario aggregation rule**. The confirmatory prediction is

$$
\operatorname{Agg}_{\Omega}
\!\left[\Delta\mathcal M_{\mathcal V}^{(4)}\right]
-
\max_{r\in\{1,2,3\}}
\operatorname{Agg}_{\Omega}
\!\left[\Delta\mathcal M_{\mathcal V}^{(r)}\right]
\ge\delta_4.
$$

If scenarios have justified probabilities or weights, $\operatorname{Agg}_{\Omega}$ may be an expectation. Under deep uncertainty, it must instead be a declared nonprobabilistic robustness/satisficing statistic.

### Falsification criterion

If structural or flow-based rankings perform equally well or better under equal intervention budgets according to the prespecified viability functional and scenario rule, $S_{ij}^{\mathcal V}$ has not demonstrated additional targeting value.

---

## 7. $H_5$ — Adaptive-transformation-pathway hypothesis

### Scientific question

Under deep uncertainty, do adaptive trigger-based transformation policies produce more robust resilience–sustainability–equity trade-offs than fixed intervention sequences with comparable resources?

The fixed comparator is

$$
\Pi_F
=
[(\mathbf a_1,t_1),\ldots,(\mathbf a_N,t_N)],
$$

whereas the adaptive Stage-7 policy uses

$$
\mathbf a_k
=
\pi_k^{\rm ST}
\!\left(
\widehat X_k,
z_{I,k},
z_{O,k},
\mathfrak M_k,
\mathcal H_k
\right).
$$

Plausible futures satisfy

$$
\omega\in\Omega.
$$

### Hypothesis

**$H_5$:** Across deeply uncertain futures, adaptive transformation policies provide a more robust resilience–sustainability–equity trade-off than fixed intervention sequences with comparable resources.

### Comparison

Compare

$$
\Pi_F=\text{best prespecified fixed-pathway baseline}
$$

with

$$
\boldsymbol\pi_{\rm ST}=\text{adaptive trigger-based transformation policy}.
$$

The Stage-7 objective vector is

$$
\mathbf J
=
\begin{bmatrix}
J_{\rm risk}\\
J_{\rm service}\\
J_{\rm cost}\\
J_{\rm carbon}\\
J_{\rm inequity}\\
J_{\rm time}\\
J_{\rm flexibility}
\end{bmatrix}.
$$

The hypothesis does **not** require adaptive policy dominance on every objective in every scenario.

For a finite deep-uncertainty scenario ensemble, define a satisficing fraction

$$
R_{\rm sat}(\Pi)
=
\frac{1}{|\Omega|}
\sum_{\omega\in\Omega}
\mathbf 1\!\left[
\Pi\text{ satisfies the declared criteria in }\omega
\right].
$$

This is a scenario-coverage statistic, **not a probability**, unless scenario probabilities/weights are justified independently.

A candidate confirmatory form is

$$
R_{\rm sat}(\boldsymbol\pi_{\rm ST})
-
R_{\rm sat}(\Pi_F)
\ge\delta_5.
$$

An alternative robustness metric may be used if it is fixed before confirmatory testing.

### Falsification criterion

If adaptive transformation does not materially improve the prespecified robustness/satisficing measure, or if flexibility gains are offset by excessive cost, delay, or implementation burden under the declared decision rule, $H_5$ is not supported.

---

## 8. Causal hierarchy

The hypotheses are linked rather than independent stage-by-stage statements:

$$
H_1:\quad \mathfrak I\rightarrow F,
$$

$$
H_2:\quad I,O\rightarrow\mathcal U,u\rightarrow F,
$$

$$
H_3:\quad F+\mathcal U\rightarrow\mathcal V,
$$

$$
H_4:\quad
\mathfrak I
\rightarrow S_{ij}^{\mathcal V}
\rightarrow\text{intervention value},
$$

$$
H_5:\quad
\mathcal V+\Phi_{\rm ST}
\rightarrow\boldsymbol\pi_{\rm ST}
\rightarrow\mathbb M_{\rm sus}.
$$

Together,

$$
\mathfrak I
\rightarrow
F
\rightarrow
(I,O,u)
\rightarrow
\mathcal V
\rightarrow
S_{ij}^{\mathcal V}
\rightarrow
\text{adaptive transformation}.
$$

---

## 9. Hypothesis-to-stage map

| Hypothesis | Main stages tested | Core scientific claim |
|---|---:|---|
| $H_1$ | 2 → 3 | Dynamic causal coupling matters. |
| $H_2$ | 3 → 4 | Information and organization alter physical resilience. |
| $H_3$ | 4 → 5 | Controlled viability adds information beyond performance curves. |
| $H_4$ | 2 → 5 → 7 | Viability-sensitive interfaces provide better intervention targets. |
| $H_5$ | 5 → 6 → 7 | Adaptive pathways improve robustness relative to fixed pathways under deep uncertainty. |

---

## 10. Numerical thresholds are deliberately unfrozen

Do not assign arbitrary values such as a 20% improvement threshold without scientific justification.

For now retain

$$
\delta_1,\ldots,\delta_5.
$$

Each threshold must be determined before confirmatory testing using one or more defensible sources:

- engineering standards;
- literature-derived meaningful effects;
- baseline variability;
- pilot-study evidence;
- decision significance.

Choosing $\delta_i$ after observing final results would undermine confirmatory rigor.

---

## 11. Hypothesis Specification Matrix contract

The primary hypothesis set is

$$
\mathbb H
=
\{H_1,H_2,H_3,H_4,H_5\}.
$$

Each hypothesis will be represented by

$$
\mathscr H_i
=
\left(
T_i,M_i,X_i,Y_i,B_i,\Omega_i,\delta_i,P_i,A_i,C_i,F_i,U_i
\right).
$$

The tuple fields are intentionally abstract until the Hypothesis Specification Matrix is frozen. The matrix must define them explicitly and include at least:

| Required field | Scientific purpose |
|---|---|
| Theory | theoretical basis being tested |
| Mechanism | explicit causal mechanism |
| Variables | inputs, states, controls and outcomes |
| Baseline / rival | competing explanation or simpler model |
| Boundary conditions | domain over which inference is valid |
| Scenario / uncertainty set | $\Omega_i$ or probabilistic alternative |
| Prediction | directional or quantitative expectation |
| Meaningful threshold | $\delta_i$, fixed *a priori* |
| Critical test | experiment/ablation/comparison |
| Falsification criterion | result that counts against the hypothesis |
| Analysis rule | statistical, robust or deterministic decision rule |
| Uncertainty treatment | propagation and reporting requirements |

---

## 12. Next scientific task

The next rigorous step is **not confirmatory simulation yet**. It is to construct the Hypothesis Specification Matrix for $H_1$–$H_5$, define every field, justify $\delta_i$ *a priori*, and only then begin confirmatory numerical testing.

> **PRIMARY HYPOTHESIS LOGIC: FROZEN. NUMERICAL THRESHOLDS AND TEST SPECIFICATIONS: NOT YET FROZEN.**
