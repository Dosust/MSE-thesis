# Canonical thesis + systematic-review state — updated 2026-09-10

## Thesis title
**Dynamic Physical–Organizational Resilience of Interdependent Power–Transportation Systems: Causal Events, Timescales, Critical Transitions, and Viability**

## FINAL CANONICAL THESIS FRAMEWORK

**Status:** FINAL / CANONICAL from 2026-09-10 onward until explicitly changed by the author.

Authoritative full specification:
`project_memory/2026-09-10_canonical_framework/FINAL_CANONICAL_7_STAGE_PTIO_FRAMEWORK.md`

| Stage | Role | Main question |
|---|---|---|
| **1. Multilayer Structural Knowledge Base** | Evidence-qualified P–T–I–O structure, interfaces, admissible relations | **What exists, what can interact, and what is known?** |
| **2. Causal Mechanisms** | Evidence-supported cross-layer cause-effect pathways | **Why and through which mechanism does disruption propagate?** |
| **3. Coupled Hybrid Multiscale Dynamics** | Physical/interface plant, continuous dynamics, discrete events, heterogeneous timescales | **How and when does the coupled physical system evolve?** |
| **4. Observation, Organization, Feedback & Control** | Measurement, information, state estimation, organizational capability, decisions, intervention | **How does the system observe, coordinate, and respond?** |
| **5. Controlled Viability** | Finite-horizon and robust nonanticipative viability, boundary geometry, interface criticality | **Can acceptable service survive and recover?** |
| **6. Resilience-to-Sustainability Transformation Interface** | Translate resilience diagnosis into explicit long-term sustainability requirements | **What sustainability requirements follow from the resilience results?** |
| **7. Sustainable Transformation Pathways** | Technical, informational, organizational, environmental and policy/planning transformation | **What should be changed, where, when, and in what sequence?** |

Canonical flow:
`Structure -> Causality -> Hybrid Multiscale Dynamics -> Observation, Organization & Control -> Controlled Viability -> Sustainability Translation -> Transformation Pathways`

Canonical mathematical chain:
`(𝔊₁,𝔈₁) -> (ℰ,𝒜cause,m,p) -> (X,Fq,J,τ) -> (y,H,Eest,X̂,I,O,π,u) -> (KR,𝒱Tᴿ,∂𝒱,ρ𝒱,C𝒱) -> (Bsus,Tsus,Φsus,Sreq) -> (a₀:H,Ψtr,𝒫trans)`

Canonical conceptual chain:
`evidence-qualified structure -> causal mechanisms -> physics -> feedback -> viability -> engineering requirements -> system transformation`

Governance rules:
1. The seven-stage order is authoritative until explicitly changed by the author.
2. Stage 1 separates structural representation from evidence qualification; no visible edge is automatically interpreted as no dependency.
3. Stage 2 distinguishes structural dependency from causal mechanism and propagation form.
4. Stage 3 is the physical/interface plant with `X=(XP,XT,Z)`; Stage 4 contains observation, information, organization, estimation, and control.
5. Stage 5 begins from finite-horizon controlled viability and may use robust nonanticipative viability. `KR` is a resilience/service admissible set, not a sustainability set.
6. CARe/Hamilton–Jacobi methods are candidate computational routes for boundary computation/certification, not the theoretical definition of viability geometry or signed distance.
7. Sustainability translation is explicit in Stage 6 and does not redefine Stages 1–5.
8. Stage 7 contains candidate transformation pathways; an optimal star is introduced only after a formal objective and selection rule are defined.
9. Future literature, data, simulations, and visualizations must map into this architecture rather than silently redefining it.
10. Any substantive framework change must be recorded as an explicit canonical amendment/version.

## Scientific framing
Resilience is treated as the evidence-qualified, causal, hybrid-dynamical, multiscale, observed, organizationally controlled viability of an interdependent Power–Transportation system, with Information and Organization represented explicitly.

Plant state:
`X(t) = [X_P(t), X_T(t), Z(t)]^T`

Full closed-loop state:
`Y(t) = [X(t), I(t), O(t)]^T`

Core plant dynamics:
- `dX/dt = F_q(X,u,eta;theta)` between events
- `X(t_k+) = J_{e_k}(X(t_k-))` at discrete events
- hybrid DAE form `F_q(dX/dt,X,lambda,u,eta;theta)=0` when algebraic subsystem constraints require it

Observation/control:
- `y_m(t) = H_m(X(t-tau_m)) + nu_m(t)`
- `X_hat(t) = E_est(y_[0,t], I(t))`
- `u(t) = pi(X_hat(t), I(t), O(t))`

Controlled viability:
- `KR = KP ∩ KT ∩ KZ ∩ KI ∩ KO ∩ Kservice`
- `V_T^R(KR) = {Y0 : exists pi in Pi_NA, for all eta in H, Y^{pi,eta}(t) in KR for all t in [0,T]}`
- signed margin `rho_V(Y) = sdist(Y, partial V_T^R)`
- normalized interface criticality `C_ij^V = - partial rho_tilde_V / partial z_tilde_ij` or a standardized finite-difference equivalent

Sustainability transformation bridge:
`R_out -> Phi_sus(R_out, B_sus, T_sus) -> S_req -> candidate transformation pathways P_trans`

## Central causal chain
`HAZARD -> EVENT -> EVIDENCE-SUPPORTED CAUSAL MECHANISM -> CROSS-LAYER INTERFACE -> HYBRID MULTISCALE PROPAGATION -> OBSERVATION/INFORMATION -> ORGANIZATION -> CONTROL -> VIABILITY -> RESILIENCE-TO-SUSTAINABILITY TRANSLATION -> SUSTAINABLE TRANSFORMATION`

## CANONICAL EMPIRICAL DATA STRATEGY

Dedicated record:
`project_memory/2026-09-09_final_framework/02_CANONICAL_DATASET_DATABASE_STRATEGY.md`

**Status:** canonical data strategy from 2026-09-09 onward, subordinate to the final seven-stage framework.

Preferred empirical design:

`California-centered multi-source, multi-rate data fusion`

Primary sources:
- Caltrans PeMS — transportation state, incidents, closures, propagation and recovery.
- ORNL EAGLE-I — county-level power outage and restoration trajectories.
- CAISO OASIS — bulk-power operating context, demand and transmission outage/capacity status.
- CEC EV-CARR + DOE/NREL AFDC — charging infrastructure and direct Power–Transportation interface evidence.
- NOAA Storm Events + Event Footprint Catalog — disturbance `h(x,t)` and event timing/footprints.
- DOE-417 — event-level cause, impact, response/restoration evidence.

Supporting sources:
- FEMA TEMPO/POST — cross-infrastructure impact validation.
- OpenFEMA Public Assistance — organizational recovery/investment evidence.
- FCC Broadband Data Collection — structural information/communications availability proxy.

Sustainability translation:
- EPA eGRID — electricity emissions/generation characteristics.
- DOE/Argonne R&D GREET — lifecycle energy, emissions, air-pollutant and water implications of transformation pathways.

Controlled benchmark:
- 47-node transportation + modified IEEE 69-bus distribution dataset — mathematical/model verification only, not empirical validation.

Data governance rules:
1. No dataset is allowed to redefine the thesis framework.
2. Do not merge unrelated datasets as an observed coupled system unless event, space and time overlap are demonstrated.
3. Use asynchronous/multi-rate observation models rather than false interpolation across incompatible temporal scales.
4. Structural/administrative proxies must not be reported as direct dynamic `I(t)` or `O(t)` states without justification.
5. Correlation is not accepted as a cross-layer causal mechanism without temporal precedence, spatial plausibility, mechanism, lag consistency, confounder control, baseline/counterfactual comparison and robustness testing.
6. Stages 6–7 use resilience outputs as inputs to sustainability transformation; sustainability data do not alter Stages 1–5.

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
