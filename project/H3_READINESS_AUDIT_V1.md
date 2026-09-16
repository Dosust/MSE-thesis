# H3 Readiness Audit v1.0

![Status](https://img.shields.io/badge/status-AUDIT%20COMPLETE-1A7F37)
![H3](https://img.shields.io/badge/H3-SPECIFICATION%20OPEN-9A6700)
![Execution](https://img.shields.io/badge/confirmatory%20execution-BLOCKED-B42318)
![Citation](https://img.shields.io/badge/APA%207-REQUIRED-8250DF)

**Date:** 2026-09-16  
**Purpose:** determine what Stage-5/H3 mathematics, service definitions, uncertainty semantics, control semantics, and computational rules already exist before creating any new H3 specification.  
**Framework authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**RQ/SO/H authority:** `CANONICAL_RQ_SO_HYPOTHESES_V2.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Execution method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation  

> **Audit rule:** reuse valid prior work; supersede only what conflicts with framework v2.0; never invent a new threshold, probability law, or solver merely to complete the specification.

---

## 1. H3 target

The canonical H3 question is whether uncertainty-aware viability and reach–avoid quantities add measurable prediction or decision information beyond conventional performance/recovery-curve metrics.

The Stage-5 resilience object is

```math
\mathfrak R_T(t)
=
\left(
\mathcal V_{\alpha,T},
\mathcal R_{\beta,T},
\rho_{\mathcal V},
T_{\mathcal V},
T_{\rm rec},
P_{\rm viable},
P_{\rm recover}
\right).
```

The benchmark is

```math
Q(t)\rightarrow R_{\rm curve}.
```

The confirmatory logic remains

```math
\operatorname{Skill}(Q_{\rm conv}\cup\mathfrak R_T)
-
\operatorname{Skill}(Q_{\rm conv})
\overset{?}{\ge}
\delta_3.
```

No superiority is assumed.

---

## 2. Repository audit — what already exists

| Existing object | What is already scientifically usable | v2.0 decision |
|---|---|---|
| `CANONICAL_7_STAGE_FRAMEWORK_V2.md` | final remain + return + confidence Stage-5 concept | **AUTHORITATIVE / REUSE** |
| `CANONICAL_RQ_SO_HYPOTHESES_V2.md` | SO3/RQ3/H3, benchmark logic, unresolved H3 quantities | **AUTHORITATIVE / REUSE** |
| `H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md` | physical P–T state equations and service maps | **REUSE; do not modify H1** |
| `H1_VALIDATION_OBSERVATION_SERVICE_REQUIREMENT_ARCHITECTURE_V1.md` | case-specific service-requirement structure and threshold-provenance rule | **REUSE as input to H3 `K(t)`** |
| `H1_THRESHOLD_PROVENANCE_V1.md` | explicit prohibition on arbitrary engineering thresholds; only numerical solver floors currently frozen | **REUSE provenance discipline** |
| `ORGANIZATION_TO_FEASIBLE_CONTROL_SPECIFICATION_V1.md` | typed organizational state, authorization/resource/route/precedence constraints, feasible-control set `\mathcal U(Y,z_I,z_O,t)` | **REUSE structurally; H2 empirical qualification still required** |
| `PARTIAL_OBSERVATION_TO_VIABILITY_SPECIFICATION_V1.md` | belief-state bridge, separation of state/model/process uncertainty, posterior viable-mass diagnostic | **REUSE concepts; update notation to v2 Stage-5 object** |
| `STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md` | viability theory, finite-horizon viability, robust/stochastic distinction, state-reduction obligation, solver neutrality | **LEGACY v1 STAGE-5 AUTHORITY; retain as provenance/theory, not active v2 Stage-5 definition** |
| `SUSTAINABLE_VIABILITY_CONSTRAINT_PROTOCOL_V1.md` | constraint registry, hard-vs-soft rule, horizon provenance, chance-constraint evidence gate | **PARTLY REUSE; sustainability constraints require v2 separation rule below** |
| `VIABILITY_INTERFACE_SENSITIVITY_SPECIFICATION_V1.md` | viability-boundary/interface perturbation diagnostics | **RECLASSIFIED: Stage-6 supporting diagnostic, not primary H3** |
| `PHASE1_CONFIRMATORY_H1_H2_MATRIX_V1.md` | bounded H1/H2 mechanism experiments and explicit advance gate into Stage 5 | **UPSTREAM GATE / REUSE** |
| H3-specific service/state-set file | absent | **CREATE** |
| H3 uncertainty/probability file | absent | **CREATE** |
| H3 preregistration file | absent | **CREATE** |
| H3 algorithm-selection/verification file | absent | **CREATE** |

The audit therefore finds that H3 is **not starting from zero**. Its theoretical pieces already exist, but they are distributed across files created under the earlier viability-only Stage-5 architecture.

---

## 3. Scientific corrections required by framework v2.0

### 3.1 Stage-5 acceptability must not silently equal a sustainability objective set

The v1 files use `K_{\rm sus}`. Framework v2.0 now treats sustainability primarily as an emergent consequence of trajectories and interventions in Stage 6. Therefore the default H3 acceptability set is redefined structurally as

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

where:

- `K_phys`: physical/safety/operating admissibility;
- `K_svc`: critical electricity and mobility service requirements;
- `K_op`: hard operational requirements that genuinely define acceptable operation.

A carbon, cost, energy-intensity, accessibility-equity, or other sustainability quantity enters `K(t)` only if an independent requirement makes it a **hard admissibility condition**. Otherwise it remains a Stage-6 outcome in `\mathbf J_{\rm sus}`.

This preserves the valid v1 rule that

```math
\text{must remain satisfied}
\neq
\text{prefer to improve}.
```

### 3.2 Viability and recovery are now separate primary objects

The v1 Stage-5 document already notes that viability and recoverability after violation are different problems. Framework v2.0 promotes that distinction into the canonical resilience core. Stochastic target-tube reachability provides a formal umbrella in which stochastic viability and stochastic reach–avoid are related but distinct constrained-control problems (Vinod & Oishi, 2021).

Hence H3 must contain both

```math
\mathcal V_{\alpha,T_V}
```

and

```math
\mathcal R_{\beta,T_R},
```

rather than extending viability language to cover post-violation recovery implicitly.

### 3.3 The failure set cannot be defined as all of `K^c`

If recovery is allowed after temporary loss of acceptable service, define a degraded-but-recoverable region

```math
\boxed{
D(t)=K(t)^c\setminus F(t),
}
```

where `F(t)` is a declared unacceptable/hard-failure region. If instead `F=K^c`, a reach–avoid problem starting from a degraded state would be infeasible by definition. This is a logical requirement of the H3 set architecture, not an empirical result.

### 3.4 Recovery target is not automatically the pre-event state

Resilience curves are sensitive to how performance measures and recovery targets are defined; there is no universal single best performance metric or target across infrastructures and scenarios (Poulin & Kane, 2021). Therefore the H3 recovery set will satisfy

```math
G_{\rm rec}(t)\subseteq K(t)
```

but it will be defined from case-specific service and operational requirements rather than automatically requiring return to the exact initial state.

---

## 4. Existing service and threshold assets

The repository already defines normalized service maps for the minimal demonstrator:

```math
0\le S_P(t)\le1,
\qquad
0\le S_T(t)\le1.
```

The existing service-requirement architecture permits constraints such as

```math
S_P(t)\ge s_P^{\min}(t),
\qquad
S_T(t)\ge s_T^{\min}(t),
```

as well as case-specific maximum outage/recovery durations, critical OD service, emergency-corridor throughput, or other documented requirements.

However, the repository explicitly states that **no universal power-service threshold and no universal completed-OD/requested-OD threshold are currently frozen**. Numerical values must therefore remain open until the final demonstrator and requirement authority are qualified.

This means H3 can freeze the mathematical structure of `K`, `G_rec`, and `F` now without fabricating their numerical thresholds.

---

## 5. Existing control and observation assets

The Stage-4 feasible operational control set is already structurally specified as

```math
\mathcal U(Y,z_I,z_O,t)
=
\left\{
u\in\mathcal U_{\rm phys}(Y,t):
A_O\nu\le b_O(z_O),
B_u\nu\le r_O(z_O),
\Gamma_O(\nu,z_O)=1
\right\}.
```

with policy

```math
\nu(t)
=
\pi\!\left(\widehat X(t),z_I(t),z_O(t)\right),
\qquad
\nu(t)\in\mathcal U(Y,z_I,z_O,t).
```

Therefore H3 **does not need to invent a new control ontology**. It inherits `\mathcal U` from Stage 4. What remains open is empirical qualification of organizational quantities and the exact H3 admissible policy family `\Pi_{\rm adm}`.

The partial-observation specification already enforces

```math
\text{uncertainty in current state}
\neq
\text{uncertainty in model/parameters}
\neq
\text{future process uncertainty}.
```

That distinction is retained and extended in the H3 uncertainty specification.

---

## 6. Existing upstream execution gate

The frozen Phase-1 H1/H2 matrix already states that Stage-5 resilience experiments may not advance until the required verification/component-validation gates are passed. In particular, H1/H2 failures caused by unqualified data/software are classified as **NOT TESTED**, not as scientific falsification.

Therefore H3 confirmatory execution is blocked by the conjunction

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
G_{data}.
}
```

where:

```text
G_H1/2 = upstream H1/H2 verification/qualification gate;
G_K    = K, G_rec, F and horizons frozen with provenance;
G_U    = uncertainty/probability model qualified;
G_Pi   = admissible H3 policy/control family frozen;
G_alg  = selected H3 algorithm passes verification suite;
G_data = H3 evaluation/holdout data and outcome labels frozen.
```

Confirmatory H3 execution is authorized only if

```math
G_{H3}=1.
```

---

## 7. Literature basis used for this audit

Stochastic viability formalizes constrained stochastic control through chance/probability conditions and dynamic programming (Doyen & De Lara, 2010). Stochastic target-tube reachability maximizes the probability of satisfying a time-varying sequence of state constraints under bounded control authority and includes stochastic viability and terminal hitting-time reach–avoid formulations as special cases (Vinod & Oishi, 2021). Infrastructure resilience curves remain a legitimate conventional benchmark, but their interpretation depends on the performance measure, performance target, normalization, and summary metric selected (Poulin & Kane, 2021).

High-dimensional viability/reachability computation is method-dependent and can be computationally difficult. Lagrangian viability methods provide scalable approximations for particular system classes, while Hamilton–Jacobi methods face exponential scaling with state dimension (Maidens et al., 2013; Bansal et al., 2017). Consequently no H3 computational solver is selected by this audit.

---

## 8. Audit decision

```text
H3 SCIENTIFIC QUESTION:                    FROZEN
H3 VIABILITY + REACHABILITY ARCHITECTURE: FROZEN
H3 SERVICE-MAP FOUNDATION:                 AVAILABLE
H3 THRESHOLD VALUES:                       OPEN / EVIDENCE GATE
H3 CONTROL-SET STRUCTURE:                  AVAILABLE
H3 H2 EMPIRICAL CONTROL QUALIFICATION:     OPEN
H3 UNCERTAINTY TAXONOMY:                   PARTIALLY AVAILABLE / SPECIFY NEXT
H3 ALPHA, BETA:                            OPEN
H3 HORIZONS:                               OPEN
H3 PRIMARY SKILL METRIC:                   OPEN
H3 DELTA_3:                                OPEN
H3 COMPUTATIONAL METHOD:                   OPEN
H3 CONFIRMATORY EXECUTION:                 BLOCKED
```

The next admissible files are therefore:

```text
H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md
H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md
H3_PREREGISTRATION_V1.md
H3_ALGORITHM_SELECTION_AND_VERIFICATION_V1.md
```

---

## References — APA 7

Bansal, S., Chen, M., Herbert, S. L., & Tomlin, C. J. (2017). Hamilton-Jacobi reachability: A brief overview and recent advances. In *2017 IEEE 56th Annual Conference on Decision and Control (CDC)* (pp. 2242–2253). IEEE. https://doi.org/10.1109/CDC.2017.8263977

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008

Maidens, J. N., Kaynama, S., Mitchell, I. M., Oishi, M. M. K., & Dumont, G. A. (2013). Lagrangian methods for approximating the viability kernel in high-dimensional systems. *Automatica, 49*(7), 2017–2029. https://doi.org/10.1016/j.automatica.2013.03.020

Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458
