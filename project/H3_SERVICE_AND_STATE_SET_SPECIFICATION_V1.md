# H3 Service and State-Set Specification v1.0

![Status](https://img.shields.io/badge/status-STRUCTURE%20FROZEN-1A7F37)
![Thresholds](https://img.shields.io/badge/numerical%20thresholds-OPEN-9A6700)
![Execution](https://img.shields.io/badge/H3%20execution-BLOCKED-B42318)
![Citation](https://img.shields.io/badge/APA%207-REQUIRED-8250DF)

**Date:** 2026-09-16  
**Hypothesis:** H3 — viability–reachability incremental-information hypothesis  
**Framework stage:** 5 — Uncertainty-Aware Viability and Reachability Resilience  
**Authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md` + `CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Upstream inputs:** `H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md`, `H1_VALIDATION_OBSERVATION_SERVICE_REQUIREMENT_ARCHITECTURE_V1.md`, `H1_THRESHOLD_PROVENANCE_V1.md`, `ORGANIZATION_TO_FEASIBLE_CONTROL_SPECIFICATION_V1.md`  

> **Freeze boundary:** this file freezes the mathematical semantics of `K(t)`, `G_rec(t)`, `F(t)`, degraded states, and horizon roles. It does **not** freeze numerical service thresholds, horizon lengths, or case-specific recovery criteria.

---

## 1. Purpose

H3 requires four distinct objects before viability or reachability can be computed:

```math
\boxed{
K(t),
\qquad
G_{\rm rec}(t),
\qquad
F(t),
\qquad
(T_V,T_R).
}
```

They answer different engineering questions:

| Object | Question |
|---|---|
| `K(t)` | What counts as acceptable coupled operation at time `t`? |
| `G_rec(t)` | What counts as sufficiently recovered operation? |
| `F(t)` | What state is unacceptable enough that the recovery trajectory is not allowed to enter it? |
| `T_V` | Over what horizon must acceptable operation be maintainable? |
| `T_R` | By what horizon must acceptable recovery be achieved? |

These meanings must be fixed before a solver is selected.

---

## 2. State and service maps inherited from upstream models

The H3 state is the Stage-5 state required to evaluate constraints and controls. It may be the full P–T–I–O state

```math
Y(t)
=
\begin{bmatrix}
x_P(t)\\x_T(t)\\z_I(t)\\z_O(t)
\end{bmatrix},
```

or a validated projection

```math
Y_V=\mathcal P_V(Y)
```

when computational reduction is required.

The minimal demonstrator already defines normalized power and transport service maps:

```math
0\le S_P(Y,t)\le1,
\qquad
0\le S_T(Y,t)\le1.
```

The power-service fraction is based on served versus demanded load, and the transport-service fraction is based on completed versus requested weighted OD trips in the frozen H1 architecture. H3 inherits those definitions rather than introducing new service variables.

---

## 3. Canonical acceptable-operation set

Framework v2.0 separates resilience state admissibility from sustainability outcome evaluation. The H3 acceptable set is therefore

```math
\boxed{
K(t)
=
K_{\rm phys}(t)
\cap
K_{\rm svc}(t)
\cap
K_{\rm op}(t).
}
```

Equivalently,

```math
K(t)
=
\left\{
Y:
\begin{array}{l}
g_r^{\rm phys}(Y,t;\kappa_r)\le0,\\
g_j^{\rm svc}(Y,t;\kappa_j)\le0,\\
g_l^{\rm op}(Y,t;\kappa_l)\le0
\end{array}
\right\}.
```

### 3.1 Physical admissibility

`K_phys` contains only physically or safety-relevant hard bounds required by the selected demonstrator, for example power-system operating limits, component-capacity limits, flow/queue/storage bounds, nonnegativity requirements, protection/safety constraints, and physical mode consistency. The exact list is frozen only after the final H3 state/model realization is selected.

### 3.2 Critical service admissibility

The repository already permits service requirements of the form

```math
S_P(Y,t)\ge s_P^{\min}(t),
```

```math
S_T(Y,t)\ge s_T^{\min}(t),
```

and more specific requirements such as critical-load service, critical-OD service, emergency-corridor throughput, interruption-duration limits, or recovery deadlines when supported by the selected case authority.

Infrastructure resilience curves and metrics are meaningful only relative to explicitly defined performance measures and targets; target choice materially affects interpretation (Poulin & Kane, 2021). Therefore `s_P^{min}` and `s_T^{min}` are case-specific engineering requirements, not universal resilience constants.

### 3.3 Operational admissibility

`K_op` contains only operational conditions that are truly required for acceptable system operation. Information freshness, reserve, or resource conditions enter here only when the selected engineering problem treats them as hard requirements rather than explanatory variables.

---

## 4. Sustainability separation rule

The old Stage-5 notation `K_sus` is retained in legacy files for provenance, but the active H3 default is `K`.

```math
\boxed{
\text{Stage-5 acceptability constraint}
\neq
\text{Stage-6 sustainability preference/objective}.
}
```

Hence

```math
J_{\rm energy},
\quad
J_{\rm carbon},
\quad
J_{\rm cost},
\quad
J_{\rm access}
```

remain Stage-6 sustainability consequences unless an independently documented requirement makes one of them a hard admissibility constraint.

---

## 5. Degraded-but-recoverable region

H3 distinguishes acceptable operation from degraded operation and hard failure:

```math
\boxed{
D(t)=K(t)^c\setminus F(t).
}
```

Interpretation:

```text
K(t) = acceptable operation;
D(t) = current service/operation is unacceptable but recovery remains admissible;
F(t) = hard/unacceptable failure region that reach–avoid trajectories must not enter.
```

If `F(t)=K(t)^c`, every degraded state is already in the avoid set, making post-degradation reach–avoid recovery inconsistent by definition. Therefore `F` is a declared hard-failure subset, not automatically all of `K^c`.

---

## 6. Failure / avoid set

Define

```math
\boxed{
F(t)
=
\left\{
Y:
\exists r\in R_F
\text{ such that }
f_r(Y,t)>0
\right\}.
}
```

Eligible criteria may include case-specific safety/protection violations, critical service below an emergency minimum, irreversible/absorbing failure modes, resource exhaustion that prevents admissible recovery, or another explicitly prohibited state. Every criterion requires units, provenance, uncertainty, and a validity domain.

---

## 7. Recovery target set

The recovery target satisfies

```math
\boxed{
G_{\rm rec}(t)\subseteq K(t).
}
```

A general representation is

```math
G_{\rm rec}(t)
=
\left\{
Y\in K(t):
\begin{array}{l}
S_P(Y,t)\ge s_{P,\rm rec}(t),\\
S_T(Y,t)\ge s_{T,\rm rec}(t),\\
g_q^{\rm rec}(Y,t)\le0,\ q=1,\ldots,n_G
\end{array}
\right\}.
```

The recovery target is **not automatically the pre-event state**. Resilience-curve interpretation depends on the chosen performance target, which can be system- and scenario-specific (Poulin & Kane, 2021).

When the engineering requirement demands persistent recovery rather than transient crossing, use a dwell condition:

```math
\boxed{
Y_s\in G_{\rm rec}(s)
\quad
\forall s\in[\tau_G,\tau_G+\tau_{\rm dwell}].
}
```

The numerical dwell time remains open until supported by the selected service/recovery requirement.

---

## 8. Viability horizon and recovery horizon

A single framework symbol `T` is refined into two H3 semantics:

```math
\boxed{
T_V=\text{maintainability horizon},
\qquad
T_R=\text{recovery deadline/horizon}.
}
```

Only if the final engineering problem supports the same horizon for both questions may one set

```math
T_V=T_R=T.
```

Finite-horizon viability is appropriate when the engineering question is tied to a declared disturbance, response, and recovery interval (Aubin et al., 2011). No universal H3 horizon is assumed.

---

## 9. Canonical H3 set definitions

### 9.1 Probabilistic viability

```math
\boxed{
\mathcal V_{\alpha,T_V}(t)
=
\left\{
y\in K(t):
\exists\pi\in\Pi_{\rm adm}
\text{ such that }
\Pr^{\pi}
\left[
Y_\tau\in K(\tau),
\forall\tau\in[t,t+T_V]
\mid\mathcal I_t
\right]
\ge\alpha
\right\}.
}
```

Stochastic viability kernels under chance/probability constraints are established in constrained stochastic control and can be characterized by dynamic programming for suitable systems (Doyen & De Lara, 2010).

### 9.2 Probabilistic reach–avoid recovery

```math
\boxed{
\mathcal R_{\beta,T_R}(t)
=
\left\{
y:
\exists\pi\in\Pi_{\rm adm}
\text{ such that }
\Pr^{\pi}
\left[
\tau_{G_{\rm rec}}\le t+T_R,
Y_s\notin F(s)\ \forall s\in[t,\tau_{G_{\rm rec}})
\mid\mathcal I_t
\right]
\ge\beta
\right\}.
}
```

Stochastic target-tube reachability treats constrained stochastic systems under bounded control and includes stochastic viability and terminal hitting-time reach–avoid as related special cases (Vinod & Oishi, 2021).

---

## 10. Threshold provenance registry

Every threshold entering `K`, `G_rec`, `F`, `T_V`, or `T_R` must have one provenance class:

```math
\boxed{
\text{standard/regulation}
\;|\;
\text{case-specific operator/service requirement}
\;|\;
\text{empirical evidence}
\;|\;
\text{explicit thesis assumption}.
}
```

| ID | Object | Threshold | Units | Provenance class | Source/authority | Time aggregation | Spatial aggregation | Uncertainty | Status |
|---|---|---|---|---|---|---|---|---|---|
| `K-P-*` | `K_phys` | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN | unfrozen |
| `K-SP` | power service | `s_P^{min}` | fraction | case-specific requirement | OPEN | OPEN | OPEN | OPEN | unfrozen |
| `K-ST` | transport service | `s_T^{min}` | fraction | case-specific requirement | OPEN | OPEN | OPEN | OPEN | unfrozen |
| `G-P` | recovered power service | `s_{P,rec}` | fraction | case-specific requirement | OPEN | OPEN | OPEN | OPEN | unfrozen |
| `G-T` | recovered transport service | `s_{T,rec}` | fraction | case-specific requirement | OPEN | OPEN | OPEN | OPEN | unfrozen |
| `F-*` | hard failure | OPEN | OPEN | case-specific safety/emergency requirement | OPEN | OPEN | OPEN | OPEN | unfrozen |
| `T-V` | viability horizon | `T_V` | time | decision/service horizon | OPEN | horizon | system | OPEN | unfrozen |
| `T-R` | recovery horizon | `T_R` | time | recovery requirement | OPEN | horizon | system | OPEN | unfrozen |

No placeholder value may migrate into confirmatory code as if it were evidence-supported.

---

## 11. Required logical consistency tests

Before the state-set registry closes, verify

```math
\boxed{G_{\rm rec}(t)\subseteq K(t),}
```

```math
\boxed{K(t)\cap F(t)=\varnothing,}
```

and, when degraded recovery is part of the domain,

```math
\boxed{D(t)=K(t)^c\setminus F(t)\neq\varnothing.}
```

The initial H3 domain should include intended examples of viable acceptable, acceptable-but-nonviable if such states exist, degraded-but-recoverable, and hard-failure/excluded states. If a class is empty under the final model, report it rather than changing thresholds after inspection.

---

## 12. Freeze state

```text
K = K_phys ∩ K_svc ∩ K_op:                FROZEN STRUCTURE
sustainability hard-vs-soft separation:    FROZEN
degraded region D = K^c \ F:               FROZEN STRUCTURE
G_rec ⊆ K:                                 FROZEN STRUCTURE
recovery target not automatically pre-event:FROZEN RULE
optional dwell semantics:                  AVAILABLE / VALUE OPEN
separate T_V and T_R roles:                FROZEN STRUCTURE
threshold provenance schema:               FROZEN
numerical thresholds and horizons:         OPEN
```

H3 computation remains blocked until the numerical registry is closed through evidence and preregistration.

---

## References — APA 7

Aubin, J.-P., Bayen, A. M., & Saint-Pierre, P. (2011). *Viability theory: New directions* (2nd ed.). Springer. https://doi.org/10.1007/978-3-642-16684-6

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008

Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458

