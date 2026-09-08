# Final Thesis Framework — Canonical as of 2026-09-09

**Status:** FINAL / CANONICAL until explicitly changed by the author.

## Seven-stage framework

| Stage | Role | Main question |
|---|---|---|
| **1. Multilayer Structure** | P–T–I–O architecture | **What exists?** |
| **2. Causal Mechanisms** | Cross-layer cause-effect pathways | **Why does disruption propagate?** |
| **3. Coupled Hybrid Multiscale Dynamics** | Coupling + continuous dynamics + discrete events + timescales | **How and when does it evolve?** |
| **4. Feedback & Control** | Information, organization, decisions, intervention | **How does the system respond?** |
| **5. Viability** | Survival/recoverability under constraints | **Can it survive?** |
| **6. Resilience-to-Sustainability Transformation Interface** | Translate resilience findings into transformation requirements | **What do the resilience results imply for sustainability?** |
| **7. Sustainable Transformation Pathways** | Technical, organizational, environmental and policy transformation | **What should be changed for long-term sustainability?** |

## Canonical flow

`Multilayer Structure -> Causal Mechanisms -> Coupled Hybrid Multiscale Dynamics -> Feedback & Control -> Viability -> Resilience-to-Sustainability Transformation Interface -> Sustainable Transformation Pathways`

## Core mathematical interpretation

### 1. Multilayer Structure
- Physical layers: Power `P` and Transportation `T`.
- Information `I` and Organization `O` are represented as explicit interacting subsystems/states; they are treated as network layers only when their own topology is modeled.
- Unified state:
  `Y(t) = [X_P(t), X_T(t), Z(t), I(t), O(t)]^T`
- Directed interdependencies are represented through cross-layer interfaces `Z`.

### 2. Causal Mechanisms
`e_i^(alpha) --[z_ij^(alpha beta), tau_ij]--> e_j^(beta)`

This stage identifies what causes what, through which cross-layer interface, in which direction, and after what propagation delay.

### 3. Coupled Hybrid Multiscale Dynamics
Between events:
`dY/dt = F_q(Y,u,h;theta,tau)`

At discrete events:
`Y(t_k+) = J_{e_k}(Y(t_k-))`

Core objects: `Z + F + J + tau`.

### 4. Feedback & Control
Core feedback:
`X -> I -> O -> u -> X`

Decision/control:
`u(t) = pi(O(t), I(t), X_hat(t))`

### 5. Viability
Admissible set:
`K = K_phys ∩ K_service ∩ K_org ∩ K_sus`

Viability:
`V = Viab(K)`

This stage evaluates whether the coupled system can remain within acceptable operating and recovery conditions under disturbance and control.

### 6. Resilience-to-Sustainability Transformation Interface
This stage does **not** change Stages 1–5. It translates their outputs into sustainability transformation requirements.

`R = resilience-analysis outputs`

`S = Phi_sus(R, baseline, sustainability targets)`

Typical translated quantities include service reliability, recovery time, critical interfaces, intervention cost, energy use, emissions, resource demand, mobility accessibility, and organizational capability.

### 7. Sustainable Transformation Pathways
The translated requirements become actionable long-term transformation pathways across:
- technical infrastructure,
- organizational capability,
- environmental performance,
- governance/policy.

## Scientific logic

`WHAT exists? -> WHY does disruption propagate? -> HOW and WHEN does it evolve? -> HOW does the system respond? -> CAN it survive? -> WHAT do the resilience results imply for sustainability? -> WHAT should be changed for long-term sustainability?`

## Canonical empirical data strategy

The framework is now paired with a dedicated evidence/data architecture:

`project_memory/2026-09-09_final_framework/02_CANONICAL_DATASET_DATABASE_STRATEGY.md`

Core rule:

`framework -> data requirements -> multi-source observations -> causal/hybrid inference -> viability outputs -> sustainability transformation`

The preferred empirical design is a **California-centered, multi-source, multi-rate data-fusion case**, using PeMS, EAGLE-I, CAISO OASIS, CEC/AFDC charging data, NOAA hazards, DOE-417, FEMA/OpenFEMA, FCC BDC, and eGRID/GREET according to the construct and evidence limitations documented in the canonical data strategy.

No source is allowed to redefine the seven-stage framework. No proxy is treated as a direct state without explicit justification, and no correlation is treated as a cross-layer causal mechanism without temporal, spatial, mechanistic, confounder, and robustness checks.

## Governance rule

This seven-stage architecture is the authoritative thesis framework from 2026-09-09 onward. It should not be replaced, reordered, or renamed in project artifacts unless the author explicitly requests a change. Sustainability is connected downstream through Stages 6–7; it does not alter the internal architecture of Stages 1–5.
