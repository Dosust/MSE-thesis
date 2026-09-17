# H3 Uncertainty and Probability Specification v1.0

![Status](https://img.shields.io/badge/status-STRUCTURE%20FROZEN-1A7F37)
![Probability](https://img.shields.io/badge/probability%20models-OPEN-9A6700)
![AlphaBeta](https://img.shields.io/badge/alpha%20beta-OPEN-9A6700)
![Execution](https://img.shields.io/badge/H3%20execution-BLOCKED-B42318)

**Date:** 2026-09-16  
**Hypothesis:** H3  
**Authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`, `CANONICAL_RQ_SO_HYPOTHESES_V3.md`, `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  

> **Governing rule:** probability is used only when a defensible stochastic model exists. Unsupported uncertainty is represented by intervals, sets, scenarios, sensitivity analysis, or other nonprobabilistic forms rather than by invented distributions.

---

## 1. Purpose

The Stage-5 resilience core uses probability to quantify confidence in maintainability and recovery. Probability is therefore an uncertainty layer over viability and reachability, not a third independent resilience theory.

The H3 uncertainty specification must distinguish at least:

```math
\boxed{
\text{state-estimation uncertainty}
\neq
\text{parameter/model uncertainty}
\neq
\text{future process uncertainty}
\neq
\text{numerical approximation uncertainty}.
}
```

The common aleatory/epistemic distinction is useful, but its classification depends on the modeling context: epistemic uncertainty is associated with potentially reducible lack of knowledge, while aleatory uncertainty represents variability not treated as reducible within the analysis context (Der Kiureghian & Ditlevsen, 2009).

---

## 2. Uncertainty object

Let

```math
\theta
=
\left(
\theta_{\rm al},
\theta_{\rm ep}
\right)
```

denote the uncertainty partition used in a declared H3 model.

This partition is supplemented by a source tag:

```math
s_\theta
\in
\{
\text{hazard},
\text{demand},
\text{repair},
\text{interdependency},
\text{observation},
\text{organization},
\text{model form},
\text{numerical}
\}.
```

The source tag and aleatory/epistemic classification are not interchangeable. For example, a repair time can contain both observed event-to-event variability and epistemic uncertainty in a poorly estimated distribution.

---

## 3. H3 uncertainty registry

Every uncertain H3 quantity must be recorded using this schema before confirmatory execution:

| Field | Required content |
|---|---|
| Quantity | named state, parameter, process, delay, threshold, or model-form object |
| Symbol / units | explicit mathematical symbol and units |
| Source tag | hazard / demand / repair / interdependency / observation / organization / model form / numerical |
| Aleatory component | yes/no/partial + justification |
| Epistemic component | yes/no/partial + justification |
| Evidence source | dataset, experiment, paper, standard, or explicit assumption |
| Probability law | family + parameters, or `NONE` |
| Support / bounds | physical/statistical support |
| Dependence | correlations/copula/joint model or declared independence with justification |
| Calibration data | data used to estimate the model |
| Validation data | independent/held-out data if available |
| Goodness/calibration test | declared before confirmatory use |
| Sensitivity role | included/excluded + rationale |
| Status | proposed / qualified / frozen / rejected |

The initial candidate registry is:

| Quantity family | Source tag | Probability status now | H3 status |
|---|---|---|---|
| hazard intensity/timing | hazard | case-dependent | **OPEN** |
| transport/EV demand and arrivals | demand | data-dependent | **OPEN** |
| repair/restoration duration | repair | data-dependent | **OPEN** |
| P↔T coupling parameters | interdependency | evidence-dependent | **OPEN** |
| measurement/estimation error | observation | estimator/data-dependent | **OPEN** |
| communication latency/loss | observation | data-dependent | **OPEN** |
| organizational response/resource availability | organization | currently largely epistemic in Phase 1 | **OPEN / H2 gate** |
| threshold uncertainty | service requirement | authority/data-dependent | **OPEN** |
| model-form discrepancy | model form | no universal probability assumption | **OPEN** |
| solver/discretization error | numerical | bounded/estimated through convergence tests | **OPEN** |

No row in this table authorizes a probability distribution by itself.

---

## 4. State uncertainty and belief representation

The existing partial-observation specification defines

```math
b_t(y)
=
p(Y_t=y\mid\mathcal I_t),
```

when a probabilistic state estimator is scientifically justified.

A point estimate

```math
\widehat Y_t
```

may be retained as a comparator, but H3 must not treat estimator covariance or posterior spread as equivalent to future process uncertainty.

The posterior viable-mass diagnostic

```math
\pi_{\mathcal V,t}
=
\Pr(Y_t\in\mathcal V\mid\mathcal I_t)
```

is a diagnostic of uncertainty about the **current state** relative to a viable set. It is not automatically the same as

```math
P_{\rm viable}
=
\Pr^{\pi}
\left[
Y_\tau\in K(\tau)
\ \forall\tau\in[t,t+T_V]
\mid\mathcal I_t
\right],
```

which is a **future trajectory probability** under a declared dynamics/control/uncertainty model.

---

## 5. Maintainability probability

For a fixed admissible policy `pi`, define

```math
P_{\rm viable}^{\pi}(y,t)
=
\Pr^{\pi}
\left[
Y_\tau\in K(\tau),
\forall\tau\in[t,t+T_V]
\mid Y_t=y,\mathcal I_t
\right].
```

The optimal/control-authority version is

```math
\boxed{
P_{\rm viable}^{\star}(y,t)
=
\sup_{\pi\in\Pi_{\rm adm}}
P_{\rm viable}^{\pi}(y,t).
}
```

Then

```math
\boxed{
\mathcal V_{\alpha,T_V}(t)
=
\{y\in K(t):P_{\rm viable}^{\star}(y,t)\ge\alpha\}.
}
```

Stochastic viability under probability/chance constraints is an established constrained-control formulation (Doyen & De Lara, 2010).

---

## 6. Recovery probability

For a fixed admissible policy `pi`, define the first entry time

```math
\tau_G
=
\inf\{s\ge t:Y_s\in G_{\rm rec}(s)\}.
```

The reach–avoid probability is

```math
P_{\rm recover}^{\pi}(y,t)
=
\Pr^{\pi}
\left[
\tau_G\le t+T_R,
Y_s\notin F(s)\ \forall s\in[t,\tau_G)
\mid Y_t=y,\mathcal I_t
\right].
```

Define

```math
\boxed{
P_{\rm recover}^{\star}(y,t)
=
\sup_{\pi\in\Pi_{\rm adm}}
P_{\rm recover}^{\pi}(y,t)
}
```

and

```math
\boxed{
\mathcal R_{\beta,T_R}(t)
=
\{y:P_{\rm recover}^{\star}(y,t)\ge\beta\}.
}
```

Stochastic target-tube reachability formalizes probability-maximizing constrained trajectories under bounded control and contains stochastic viability and terminal hitting-time reach–avoid formulations as special cases (Vinod & Oishi, 2021).

---

## 7. Meaning of alpha and beta

`alpha` and `beta` are **decision confidence thresholds**, not universal constants:

```math
\boxed{
\alpha,\beta\in[0,1].
}
```

Their final values must be linked to:

```text
criticality of the service/function;
consequence of constraint or recovery failure;
case-specific risk tolerance or service requirement;
calibration/quality of the probability model;
available sample size and uncertainty;
engineering decision use.
```

The thesis must not use values such as `0.90`, `0.95`, or `0.99` merely because they are familiar confidence levels.

Current status:

```text
alpha: OPEN
beta:  OPEN
```

---

## 8. Probability-admissibility gate

A quantity may be modeled probabilistically in confirmatory H3 only if all applicable gates pass:

```math
\boxed{
G_{prob}
=
G_{meas}
\land
G_{sample}
\land
G_{support}
\land
G_{depend}
\land
G_{cal}
\land
G_{holdout}.
}
```

where:

```text
G_meas    = quantity is meaningfully measured/defined;
G_sample  = data support is sufficient for the intended probability model;
G_support = physical/statistical support is respected;
G_depend  = material dependence is modeled or bounded;
G_cal     = distribution/forecast calibration checks pass;
G_holdout = independent or equivalent validation evidence exists where feasible.
```

If

```math
G_{prob}=0,
```

then the quantity must use a nonprobabilistic representation such as

```math
\theta\in\Theta,
```

scenario ensemble

```math
\omega\in\Omega,
```

or interval/bounded uncertainty.

Scenario frequencies must not be called probabilities without an independently justified sampling/probability model.

---

## 9. Deep/model uncertainty rule

When evidence does not support a unique probability model, H3 must report conditional results such as

```math
\mathfrak R_T\mid M_j,
\qquad
M_j\in\mathcal M,
```

or robustness over a model set rather than collapsing model-form uncertainty into an arbitrary mixture distribution.

Similarly, epistemic ranges may be propagated through sensitivity or scenario analysis while keeping stochastic process variability conditional on each epistemic realization.

---

## 10. Numerical uncertainty is not physical uncertainty

Numerical approximation error must be estimated separately through solver/grid/sample convergence and reference problems.

The governing rule is

```math
\boxed{
\text{physical/process uncertainty}
\neq
\text{parameter uncertainty}
\neq
\text{numerical error}.
}
```

A wide Monte Carlo confidence interval due to finite sampling, for example, is not evidence of physical variability; it is estimator uncertainty and must be labeled accordingly.

---

## 11. Calibration and scoring rule

If H3 produces probabilistic forecasts for an observable binary or categorical event, their quality should be evaluated with a proper scoring rule and calibration diagnostics. Strictly proper scoring rules are designed so that truthful probabilistic forecasts optimize the expected score (Gneiting & Raftery, 2007).

This file does **not** yet freeze Brier score, log score, or another scoring rule as the H3 primary metric. That choice is deferred to the preregistration outcome-type gate.

---

## 12. What is frozen now

```text
uncertainty-source registry schema:             FROZEN
aleatory/epistemic contextual distinction:      FROZEN RULE
current-state vs future-process distinction:    FROZEN RULE
P_viable^pi and P_viable^*:                     FROZEN SEMANTICS
P_recover^pi and P_recover^*:                   FROZEN SEMANTICS
alpha/beta role as decision thresholds:         FROZEN SEMANTICS
probability-admissibility gate:                 FROZEN
nonprobabilistic fallback rule:                 FROZEN
specific probability distributions/parameters: OPEN
alpha and beta numerical values:                OPEN
correlation/dependence models:                  OPEN
primary probabilistic skill metric:             OPEN
```

---

## References — APA 7

Der Kiureghian, A., & Ditlevsen, O. (2009). Aleatory or epistemic? Does it matter? *Structural Safety, 31*(2), 105–112. https://doi.org/10.1016/j.strusafe.2008.06.020

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008

Gneiting, T., & Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation. *Journal of the American Statistical Association, 102*(477), 359–378. https://doi.org/10.1198/016214506000001437

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458

