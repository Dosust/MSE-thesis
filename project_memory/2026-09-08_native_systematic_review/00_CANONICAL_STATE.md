# Canonical thesis + systematic-review state — updated 2026-09-09

## Thesis title
**Dynamic Physical–Organizational Resilience of Interdependent Power–Transportation Systems: Causal Events, Timescales, Critical Transitions, and Viability**

## FINAL CANONICAL THESIS FRAMEWORK

**Status:** FINAL / CANONICAL from 2026-09-09 onward until explicitly changed by the author.

| Stage | Role | Main question |
|---|---|---|
| **1. Multilayer Structure** | P–T–I–O architecture | **What exists?** |
| **2. Causal Mechanisms** | Cross-layer cause-effect pathways | **Why does disruption propagate?** |
| **3. Coupled Hybrid Multiscale Dynamics** | Coupling + continuous dynamics + discrete events + timescales | **How and when does it evolve?** |
| **4. Feedback & Control** | Information, organization, decisions, intervention | **How does the system respond?** |
| **5. Viability** | Survival/recoverability under constraints | **Can it survive?** |
| **6. Resilience-to-Sustainability Transformation Interface** | Translate resilience findings into transformation requirements | **What do the resilience results imply for sustainability?** |
| **7. Sustainable Transformation Pathways** | Technical, organizational, environmental and policy transformation | **What should be changed for long-term sustainability?** |

Canonical flow:
`Multilayer Structure -> Causal Mechanisms -> Coupled Hybrid Multiscale Dynamics -> Feedback & Control -> Viability -> Resilience-to-Sustainability Transformation Interface -> Sustainable Transformation Pathways`

Governance rule: **Stages 1–5 remain the core resilience framework. Sustainability is connected downstream through Stages 6–7 and must not be inserted inside or used to rename/reorder Stages 1–5 unless the author explicitly requests a change.**

Dedicated framework record:
`project_memory/2026-09-09_final_framework/FINAL_FRAMEWORK.md`

## Scientific framing
Resilience is treated as the causal, temporal, hybrid-dynamical, feedback-controlled viability of the interdependent Power–Transportation system, with information and organization represented explicitly.

State:
`Y(t) = [X_P(t), X_T(t), Z(t), I(t), O(t)]^T`

with physical Power and Transportation states `X_P, X_T`, interdependency/interface states `Z`, information/observability `I`, and organizational capability `O`.

Core dynamics:
- `dY/dt = F_q(Y,u,h;theta,tau)` between events
- `Y(t_k+) = J_{e_k}(Y(t_k-))` at discrete events
- `u = pi(O,I,X_hat)`

Causal mechanism:
`e_i^(alpha) --[z_ij^(alpha beta), tau_ij]--> e_j^(beta)`

Core feedback:
`X -> I -> O -> u -> X`

Timescale ratio:
`Gamma = tau_response / tau_cascade`

Viability:
`K = K_phys ∩ K_service ∩ K_org ∩ K_sus`
`V = Viab(K)`

Sustainability transformation bridge:
`Resilience outputs -> Phi_sus -> Sustainable transformation requirements -> Technical/organizational/environmental/policy pathways`

## Central causal chain
`HAZARD -> CAUSAL EVENT -> CROSS-LAYER INTERFACE -> HYBRID MULTISCALE PROPAGATION -> INFORMATION/ORGANIZATION FEEDBACK -> CONTROL -> VIABILITY -> RESILIENCE-TO-SUSTAINABILITY TRANSLATION -> SUSTAINABLE TRANSFORMATION`

## Systematic-review architecture
PRISMA is the evidence system, not the resilience model.

Use:
`PRISMA 2020 + PRISMA-S + PRESS`

Corpus:
`C = C_D ∪ C_M ∪ C_T`, with reviews/context separate.

Streams:
1. C1 physical P–T coupling
2. C2 physical–organizational coupling
3. C3 causal + temporal dynamics
4. C4 complex-system transitions
5. C5 viability/resilience mathematics
6. C6 intervention/control/validation

## Frozen Scopus phase
All nine Scopus families are frozen:
`Q0,Q3,Q5,Q6A,Q6B,M1,M2,T1,T2`.

## Frozen IEEE phase
All nine IEEE families are frozen:
- Q0: N=189; dev 40.0%; val 40.0%
- Q3: N=103; dev 53.3%; val 63.3%
- Q5: N=65; dev 56.7%; val 46.7%
- Q6A: N=7; strict 2/7=28.6%
- Q6B: N=9; strict 1/9=11.1%
- M1: N=33; strict 12/33=36.4%
- M2: N=57; strict 20/57=35.1%
- T1: native N=2651; dev 9/30=30.0%; val 8/30=26.7%
- T2: native N=4699; dev 3/30=10.0%; val 5/30=16.7%

IEEE phase = 9/9 complete.

## Compendex phase
CPX-Q0 v2.2 = **FROZEN**
- final native/export N=245
- dev 20/30=66.7%
- val 16/30=53.3%
- anchors 3/3
- final raw SHA-256: `2c15662b02f27a085dc39f50245d33c4f2166c63839050feb8fc2eb22f7816a8`
- execution deviation `RD-CPX-Q0-SET-01` accepted
- Compendex phase = 1/9 frozen

Remaining Compendex:
`Q3,Q5,Q6A,Q6B,M1,M2,T1,T2`

Next run:
**CPX-Q3 v1.1**

## Latest master files
- `PRISMA_Native_Pilot_Controller_v6_7_CPX_Q0_Frozen.xlsx`
- `PRISMA_Frozen_Search_Database_Translation_Package_v2_7_CPX_Q0_Frozen.xlsx`
- `Compendex_Q0_v2_2_Native_Translation_Validation_and_Freeze.xlsx`
- `2026-09-08_COMPENDEX_Q0_v2_2_RAW_N0245.csv`
