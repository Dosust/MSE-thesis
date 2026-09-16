# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207%20MANDATORY-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-v2.0-1A7F37)
![Reasoning](https://img.shields.io/badge/reasoning-v1.2-0969DA)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![Traceability](https://img.shields.io/badge/RQ--SO--H-v2.0%20FROZEN-1A7F37)
![H1](https://img.shields.io/badge/H1-RAW%20DATA%20GATE-B42318)
![H2](https://img.shields.io/badge/H2-EMPIRICAL%20QUALIFICATION%20OPEN-9A6700)
![H3](https://img.shields.io/badge/H3-PREREG%20PREPARATION-9A6700)

This directory is the active scientific and mathematical source of truth for the MSE thesis.

**Framework authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**RQ–SO–H authority:** `CANONICAL_RQ_SO_HYPOTHESES_V2.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Execution method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation  
**Citation rule:** externally sourced scientific claims require adjacent verified APA 7 author–date citations  
**Novelty rule:** literature support justifies relevance, mechanisms, mathematics and comparators; novelty is tested separately  

---

## 1. Frozen scientific chain

```math
\boxed{
RQ_i
\rightarrow
SO_i
\rightarrow
H_i
\rightarrow
\text{mechanism}
\rightarrow
\text{metric}
\rightarrow
\text{baseline}
\rightarrow
\text{experiment}
\rightarrow
\text{uncertainty}
\rightarrow
\text{falsification}
\rightarrow
\text{result}
\rightarrow
\text{engineering conclusion}.
}
```

The five primary hypothesis contrasts are

```math
\boxed{H_1:\ M_2\ \text{vs}\ M_1\ \text{vs}\ M_0}
```

```math
\boxed{H_2:\ P+T\ \text{vs}\ P+T+I\ \text{vs}\ P+T+I+O}
```

```math
\boxed{H_3:\ R_{\rm curve}\ \text{vs}\ R_{\rm curve}+\mathfrak R_T}
```

```math
\boxed{H_4:\ a_k\rightarrow(\Delta\mathfrak R^{a_k},\Delta\mathbf J_{\rm sus}^{a_k})}
```

```math
\boxed{H_5:\ \mathcal A_R^{\star}\ \text{vs}\ \mathcal A_{R,S}^{\star}}
```

Interface criticality is a Stage-6 supporting diagnostic. Adaptive transformation pathways are a Stage-7 supporting extension unless separately promoted through preregistration.

---

## 2. Stage-5 resilience core

```math
\boxed{
\text{Resilience}
=
\underbrace{\text{remain acceptable}}_{\text{viability}}
+
\underbrace{\text{return to acceptable operation}}_{\text{reachability}}
+
\underbrace{\text{quantify confidence}}_{\text{probability}}
}
```

where `+` denotes conceptual composition rather than scalar addition.

The active H3 resilience object is

```math
\boxed{
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
}
```

Conventional performance/recovery curves remain the H3 benchmark. Incremental value must be tested rather than assumed.

---

## 3. Current execution architecture

The project now proceeds on two controlled tracks:

```math
\boxed{
\begin{array}{lll}
\text{Track A} &:& \text{H1/H2 empirical and model qualification}\\
\text{Track B} &:& \text{H3 mathematical specification and preregistration readiness}
\end{array}
}
```

Track B may develop H3 definitions and algorithms, but may not execute H3 confirmatorily until upstream and H3-specific gates close.

### Track A — H1/H2

H1 remains governed by

```math
\boxed{
M_0=\text{independent},
\qquad
M_1=\text{static/algebraic coupling},
\qquad
M_2=\text{dynamic causal coupling}.
}
```

Current H1 state:

```text
M0 implementation:                  VERIFIED
M1 implementation:                  VERIFIED
M2 implementation/regression:       VERIFIED
row-level acquisition plan:         FROZEN
offline acquisition/audit tests:    4/4 PASS
raw row-level qualification R1–R8:  PENDING
candidate train/test split:          NOT FROZEN
confirmatory H1 execution:           NOT AUTHORIZED before data gates
```

H2 has a structured organization-to-feasible-control model and partial-observation/state-estimation bridge, but empirical organizational/information qualification remains incomplete. Phase-1 H2 execution remains gated.

### Track B — H3

The H3 readiness audit found substantial reusable v1 theory but no complete v2 H3 package. The following files now control H3 preparation:

| File | Role | Status |
|---|---|---|
| [`H3_READINESS_AUDIT_V1.md`](H3_READINESS_AUDIT_V1.md) | audit of existing Stage-5/service/control/uncertainty assets and v2 corrections | **AUDIT COMPLETE** |
| [`H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`](H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md) | semantics of `K`, `G_rec`, `F`, degraded states, `T_V/T_R`, threshold provenance | **STRUCTURE FROZEN / VALUES OPEN** |
| [`H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md`](H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md) | uncertainty taxonomy, probability admissibility, `P_viable`, `P_recover`, alpha/beta semantics | **STRUCTURE FROZEN / MODELS OPEN** |
| [`H3_PREREGISTRATION_V1.md`](H3_PREREGISTRATION_V1.md) | paired comparator, candidate outcomes, pre-data metric rule, falsification and execution gates | **DRAFT PREREG / METRIC OPEN** |
| [`H3_ALGORITHM_SELECTION_AND_VERIFICATION_V1.md`](H3_ALGORITHM_SELECTION_AND_VERIFICATION_V1.md) | solver eligibility, state reduction, reference problems, convergence and verification | **SELECTION GATE FROZEN / SOLVER OPEN** |
| [`RESILIENCE_SUSTAINABILITY_EXECUTION_STATUS_V1.md`](RESILIENCE_SUSTAINABILITY_EXECUTION_STATUS_V1.md) | current cross-stage execution dashboard | **CURRENT v1.1** |

---

## 4. H3 acceptability-set correction under framework v2

The active H3 default is

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

Sustainability outcomes are not inserted into `K(t)` merely because they matter to the thesis. Unless independently justified as hard admissibility requirements, they remain Stage-6 consequences.

The degraded region is

```math
\boxed{D(t)=K(t)^c\setminus F(t)}
```

and the recovery target satisfies

```math
\boxed{G_{\rm rec}(t)\subseteq K(t).}
```

The maintainability and recovery horizons are kept semantically distinct:

```math
\boxed{
T_V=\text{maintainability horizon},
\qquad
T_R=\text{recovery horizon}.
}
```

No numerical service threshold, `T_V`, `T_R`, `alpha`, `beta`, or `delta_3` is frozen without evidence/provenance.

---

## 5. H3 execution gate

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
G_{data}.
}
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

A failed prerequisite gate produces `H3 = NOT TESTED`, not scientific falsification.

---

## 6. H3 algorithm rule

No solver is currently selected.

Candidate families include dynamic programming, Hamilton–Jacobi reachability, Lagrangian/set-propagation methods, Monte Carlo/scenario evaluation under fixed policies, sampling/optimization methods, and verified surrogates.

Selection must follow the frozen H3 computational signature:

```math
\boxed{
\mathcal C_{H3}
=
(n_x,n_u,n_m,\mathsf{dyn},\mathsf{set},\mathsf{unc},\mathsf{obs},\mathsf{guar},\mathsf{budget}).
}
```

A solver is eligible only after its mathematical assumptions, uncertainty semantics, geometry, hybrid/delay handling, scalability, guarantee, verification, reproducibility, and validation gates pass.

---

## 7. Cross-cutting authorities

| File | Role | Status |
|---|---|---|
| [`CANONICAL_7_STAGE_FRAMEWORK_V2.md`](CANONICAL_7_STAGE_FRAMEWORK_V2.md) | seven-stage scientific framework | **CANONICAL v2.0** |
| [`CANONICAL_RQ_SO_HYPOTHESES_V2.md`](CANONICAL_RQ_SO_HYPOTHESES_V2.md) | RQ0 + general objective + SO1–SO5 + RQ1–RQ5 + H1–H5 | **CANONICAL v2.0** |
| [`RESEARCH_REASONING_PROTOCOL.md`](RESEARCH_REASONING_PROTOCOL.md) | reasoning, citation, falsification and evidence discipline | **CURRENT v1.2** |
| [`CANONICAL_SPATIOTEMPORAL_PROPAGATION_REQUIREMENT_V1.md`](CANONICAL_SPATIOTEMPORAL_PROPAGATION_REQUIREMENT_V1.md) | mandatory time + location preservation for spatial mechanisms | **FROZEN v1.0** |
| [`MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md) | reduced-demonstrator and state-reduction rationale | **CURRENT METHODOLOGICAL RATIONALE** |
| [`../thesis/00_governance/RQ_SO_H_TRACEABILITY_V2.md`](../thesis/00_governance/RQ_SO_H_TRACEABILITY_V2.md) | thesis-facing traceability | **CURRENT v2.0** |

Legacy v1 Stage-5 files remain useful theoretical/provenance resources but do not override framework v2.0 or the H3 package.

---

## 8. Immediate next executable work

### Track A

```math
\boxed{
\text{retrieve raw H1 event/source data}
\rightarrow
R1{:}R8
\rightarrow
\text{freeze/reject split}
\rightarrow
\text{H1 verification/validation}.
}
```

### Track B

```math
\boxed{
\text{qualify threshold/horizon evidence}
\rightarrow
(K,G_{\rm rec},F,T_V,T_R)
\rightarrow
\text{qualify uncertainty models}
\rightarrow
\Pi_{\rm adm}
\rightarrow
\mathcal C_{H3}
\rightarrow
\text{select + verify solver}.
}
```

Do not revise the conceptual framework, choose familiar probability levels, or select a reachability solver merely by popularity. The next progress comes from closing evidence and computation gates.
