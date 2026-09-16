# H3 Confirmatory Preregistration v1.0

![Status](https://img.shields.io/badge/status-DRAFT%20PREREGISTRATION-9A6700)
![Execution](https://img.shields.io/badge/confirmatory%20execution-NOT%20AUTHORIZED-B42318)
![Outcome](https://img.shields.io/badge/primary%20skill%20metric-OPEN-9A6700)
![Citation](https://img.shields.io/badge/APA%207-REQUIRED-8250DF)

**Date:** 2026-09-16  
**Hypothesis:** H3 — Viability–Reachability Incremental-Information Hypothesis  
**Authority:** `CANONICAL_RQ_SO_HYPOTHESES_V2.md`  
**Set specification:** `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`  
**Uncertainty specification:** `H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md`  
**Algorithm gate:** `H3_ALGORITHM_SELECTION_AND_VERIFICATION_V1.md`  

> **Preregistration principle:** this file fixes the comparison logic and the rules by which still-open items must be selected. It deliberately does not invent `alpha`, `beta`, horizons, `delta_3`, data splits, or a primary skill metric before the required evidence/data gates are resolved.

---

## 1. Canonical question and hypothesis

### RQ3

> **Do uncertainty-aware viability and reach–avoid measures provide incremental decision-relevant information beyond conventional performance/recovery curves, and with what probabilistic confidence?**

### H3

> **For the declared Power–Transportation test domain, the combined uncertainty-aware viability–reachability resilience object provides measurable incremental predictive or decision-relevant information about future service maintainability and acceptable recovery beyond prespecified conventional performance/recovery-curve metrics.**

H3 does not test whether viability theory is mathematically valid. It tests whether adding the Stage-5 information changes prediction or engineering decision quality in the declared application.

---

## 2. Competing information sets

Define the conventional information set

```math
Q_{\rm conv}
=
\{\text{preregistered current/history performance-curve features}\},
```

and the augmented information set

```math
\boxed{
Q_{\rm VRR}
=
Q_{\rm conv}
\cup
\mathfrak R_T,
}
```

where

```math
\mathfrak R_T
=
\left(
\mathcal V_{\alpha,T_V},
\mathcal R_{\beta,T_R},
\rho_{\mathcal V},
T_{\mathcal V},
T_{\rm rec},
P_{\rm viable},
P_{\rm recover}
\right).
```

The conventional benchmark remains legitimate because resilience curves are widely used to represent degradation and recovery, but their performance measure, target, normalization, and summary metric must be stated explicitly (Poulin & Kane, 2021).

---

## 3. Matched-comparison principle

H3 is a **paired incremental-information experiment**. For each eligible scenario/state `omega`, the same physical history, disturbance realization, observation information, control authority, and evaluation label are used for both information sets. Only the Stage-5 information supplied to the prediction/decision model changes.

```math
\boxed{
\omega:
Q_{\rm conv}(\omega)
\quad\text{vs}\quad
Q_{\rm VRR}(\omega).
}
```

This prevents an apparent H3 improvement from being caused by a different disturbance, data split, control policy, or validation label.

---

## 4. Candidate confirmatory outcome families

The exact primary outcome must follow the engineering decision and the available independently observable labels. It must be frozen **before** confirmatory labels/results are inspected.

### O1 — future loss of acceptability

A candidate binary event is

```math
Y_{\rm fail}^{\Delta}(t)
=
\mathbf 1
\left\{
\exists\tau\in(t,t+\Delta]:
Y_\tau\notin K(\tau)
\right\}.
```

This tests whether Stage-5 information improves prediction of future constraint/service loss.

### O2 — successful recovery by deadline

A candidate recovery event is

```math
Y_{\rm rec}^{T_R}(t)
=
\mathbf 1
\left\{
\tau_{G_{\rm rec}}\le t+T_R,
\ Y_s\notin F(s)\ \forall s<\tau_{G_{\rm rec}}
\right\}.
```

This tests whether Stage-5 information improves prediction/classification of acceptable recovery.

### O3 — warning lead time

If the evaluation domain supports trustworthy event times but not calibrated event probabilities, a candidate outcome is warning lead time before loss of acceptability or loss of recoverability.

The primary outcome cannot be chosen after determining which outcome makes `Q_VRR` look best.

---

## 5. Primary-skill-metric selection gate

The primary skill metric is **not yet frozen**. The following pre-data decision rule is frozen instead:

```text
IF the final H3 model produces calibrated probabilistic forecasts
AND independent binary/categorical outcome labels are adequate,
THEN select a strictly proper scoring rule as the primary predictive metric,
with calibration as a secondary diagnostic.

ELSE IF the final H3 output is deterministic/set-valued with valid binary labels,
THEN select a prespecified classification/discrimination metric compatible with class prevalence and decision costs.

ELSE IF reliable event times are available but probability calibration is not defensible,
THEN select a prespecified warning-lead-time or time-to-event metric.

ELSE H3 confirmatory execution remains NOT AUTHORIZED.
```

Proper scoring rules are appropriate for probabilistic forecasts because they reward honest predictive distributions; strictly proper rules uniquely optimize the expected score at the true predictive distribution (Gneiting & Raftery, 2007).

### Candidate probabilistic metric — not yet frozen

If the probabilistic branch passes, one candidate for binary outcomes is the Brier score

```math
BS
=
\frac{1}{N}
\sum_{i=1}^{N}
(p_i-o_i)^2,
```

with lower values indicating better probability forecasts. A corresponding skill difference or skill score may be preregistered against `Q_conv`.

This formula is **candidate only** until the outcome/label/calibration gate closes.

---

## 6. Confirmatory effect form

After the primary skill metric is frozen, define its orientation so that positive `Delta_Skill` means improvement. Then

```math
\boxed{
\Delta_{\rm Skill}
=
\operatorname{Skill}(Q_{\rm VRR})
-
\operatorname{Skill}(Q_{\rm conv}).
}
```

The confirmatory H3 criterion will be

```math
\boxed{
\Delta_{\rm Skill}
\ge
\delta_3,
}
```

where `delta_3>0` is an engineering/statistical materiality threshold frozen before confirmatory execution.

If the selected native metric has lower-is-better orientation, it must be transformed or the difference reversed before freezing so that the inequality remains unambiguous.

---

## 7. Delta-3 provenance gate

`delta_3` cannot be selected from the observed confirmatory effect.

Its provenance must use one or more of:

```text
engineering decision materiality;
forecast/decision cost consequences;
measurement/label uncertainty floor;
numerical approximation floor;
independent pilot/calibration data;
published benchmark where transferability is justified.
```

The final record must state:

```text
metric;
delta_3;
units/orientation;
source;
engineering meaning;
uncertainty floor;
calibration-only evidence used;
confirmatory evidence excluded from selection.
```

Current status:

```text
delta_3 = OPEN
```

---

## 8. H3 state/scenario eligibility

An H3 scenario is eligible only when all quantities needed to evaluate both the conventional benchmark and the Stage-5 objects are available or generated by a verified model.

Each scenario must have:

```text
identical initial physical state across comparator information sets;
identical disturbance/hazard realization;
identical Stage-4 feasible-control semantics;
identical observation stream and information assumptions;
identical K/G_rec/F definitions;
independently evaluable future outcome label;
no confirmatory-label leakage into Stage-5 feature computation;
complete provenance and reproducible seed/version state.
```

The existing H1/H2 Phase-1 scenarios are a **candidate upstream basis**, not automatically the final H3 confirmatory sample. H3 eligibility must be audited separately after H1/H2 closure.

---

## 9. Data separation rule

The final H3 workflow must preserve at least:

```math
D_{dev/cal}
\cap
D_{test}
=
\varnothing.
```

`D_dev/cal` may be used for:

```text
parameter estimation;
probability-model fitting;
state-estimator calibration;
algorithm tuning;
threshold/horizon decisions when justified by calibration evidence;
model-selection steps explicitly allowed by preregistration.
```

`D_test` is reserved for the frozen H3 comparison. No H3 method, outcome, `delta_3`, threshold, or feature definition may be retuned after inspecting the confirmatory labels/results.

If real-event data are too limited for a clean holdout, an alternative predeclared resampling or nested validation design must be justified before execution; a post hoc split is prohibited.

---

## 10. Nested feature-ablation diagnostics

The primary H3 comparison is `Q_conv` versus `Q_VRR`. Secondary ablations may identify which Stage-5 objects carry information:

```math
Q_{V}
=
Q_{\rm conv}\cup
\{\mathcal V_{\alpha,T_V},\rho_{\mathcal V},T_{\mathcal V},P_{\rm viable}\},
```

```math
Q_{R}
=
Q_{\rm conv}\cup
\{\mathcal R_{\beta,T_R},T_{\rm rec},P_{\rm recover}\},
```

```math
Q_{VR}
=
Q_{\rm conv}\cup
\{\text{all viability + reachability quantities}\}.
```

Unless promoted in a future preregistered version, these are explanatory diagnostics and do not replace the primary H3 decision.

---

## 11. Uncertainty reporting

Every H3 result must distinguish:

```text
state-estimation uncertainty;
future process variability;
parameter uncertainty;
model-form sensitivity;
finite-sample uncertainty;
numerical approximation error.
```

If probability models are not justified for a given source of uncertainty, use conditional/scenario/robust reporting rather than converting the source into an artificial random variable.

---

## 12. Falsification and non-support

H3 is **not supported in the declared domain** if

```math
\Delta_{\rm Skill}<\delta_3
```

under the preregistered primary metric and qualified test data.

A negative result implies that the added Stage-5 mathematical complexity has not demonstrated incremental predictive/decision value for the tested application. It does not invalidate viability or reachability theory in general.

If a prerequisite data/model/algorithm gate fails, the correct status is

```text
H3 = NOT TESTED
```

rather than unsupported.

---

## 13. Confirmatory execution gates

H3 confirmatory execution is authorized only if all are true:

```math
\boxed{
G_{H3}
=
G_{H1/2}
\land
G_K
\land
G_U
\land
G_{\Pi}
\land
G_{alg}
\land
G_{metric}
\land
G_{\delta_3}
\land
G_{data}
=1.
}
```

Definitions:

```text
G_H1/2      upstream physical + I/O verification/qualification closed for the H3 realization;
G_K         K, G_rec, F, T_V, T_R frozen;
G_U         uncertainty/probability models qualified;
G_Pi        admissible policy family and control semantics frozen;
G_alg       selected H3 algorithm verified;
G_metric    primary outcome and skill metric frozen;
G_delta3    materiality threshold frozen with provenance;
G_data      development/test roles and labels frozen.
```

Current state:

```text
G_H1/2   = 0
G_K      = 0
G_U      = 0
G_Pi     = 0
G_alg    = 0
G_metric = 0
G_delta3 = 0
G_data   = 0

H3 CONFIRMATORY EXECUTION = NOT AUTHORIZED
```

---

## 14. What this preregistration freezes now

```text
H3 question and hypothesis:                   FROZEN
Q_conv vs Q_VRR comparison architecture:      FROZEN
paired/matched scenario principle:            FROZEN
candidate outcome families O1/O2/O3:          FROZEN MENU
pre-data metric-selection decision rule:      FROZEN
primary skill metric itself:                  OPEN
positive-improvement orientation rule:        FROZEN
delta_3 selection/provenance rule:            FROZEN
delta_3 numerical value:                      OPEN
data-separation/no-retuning rule:             FROZEN
falsification vs NOT-TESTED distinction:      FROZEN
execution-gate conjunction:                   FROZEN
```

The preregistration becomes **CONFIRMATORY-FROZEN** only after all open entries are completed through evidence and data qualification, before confirmatory test labels/results are inspected.

---

## References — APA 7

Gneiting, T., & Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation. *Journal of the American Statistical Association, 102*(477), 359–378. https://doi.org/10.1198/016214506000001437

Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926
