# H3 Algorithm Selection and Verification Specification v1.0

![Status](https://img.shields.io/badge/status-SELECTION%20GATE%20FROZEN-1A7F37)
![Solver](https://img.shields.io/badge/H3%20solver-NOT%20SELECTED-9A6700)
![Verification](https://img.shields.io/badge/reference%20verification-REQUIRED-8250DF)
![Execution](https://img.shields.io/badge/H3%20execution-BLOCKED-B42318)

**Date:** 2026-09-16  
**Hypothesis:** H3  
**Authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`, `CANONICAL_RQ_SO_HYPOTHESES_V2.md`  
**Mathematical inputs:** `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`, `H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md`  

> **Method rule:** no algorithm is selected because it is fashionable, mathematically elegant, or used in a nearby paper. The selected algorithm must match the actual H3 dynamics, state dimension, set geometry, uncertainty semantics, control authority, and guarantee required.

---

## 1. What the repository already tells us about computational difficulty

The frozen H1 dynamic model `M2` is not a static graph model. It contains the dynamic state

```math
X_k
=
[e_k,y_k,n_k,q_k,R_k,r_k]
```

with interface variables

```math
z_k
=
[p_k^{ch},\mu_k,\lambda_k,F_k^R],
```

and delayed/state-dependent interface evolution

```math
z_{ij,k+1}
=
H_{ij}(X_{k-\ell_{ij}},z_{ij,k},m_k).
```

The model therefore contains memory/delay, queue dynamics, discrete road status/modes, network states, and coupled physical mechanisms. Information and organization add further state/feasible-control structure in H2.

Consequently, directly applying a full-state grid-based viability/reachability solver without dimensionality analysis would be scientifically unjustified.

Hamilton–Jacobi reachability can accommodate nonlinear dynamics and bounded disturbances, but its classical grid-based computation scales exponentially with state dimension (Bansal et al., 2017). High-dimensional viability approximation is likewise computationally difficult; Lagrangian approaches exploit structural assumptions to obtain tractability (Maidens et al., 2013).

---

## 2. Required problem characterization before solver selection

Before selecting a numerical method, freeze the following H3 computational signature:

```math
\boxed{
\mathcal C_{H3}
=
(n_x,n_u,n_m,\mathsf{dyn},\mathsf{set},\mathsf{unc},\mathsf{obs},\mathsf{guar},\mathsf{budget}).
}
```

where:

```text
n_x      effective H3 state dimension after any validated reduction;
n_u      control dimension;
n_m      discrete/hybrid mode count;
dyn      linear / affine / nonlinear / hybrid / delayed structure;
set      convexity/smoothness/time variation of K, G_rec and F;
unc      stochastic / bounded / deep/model uncertainty structure;
obs      full-state / estimated / belief-state representation;
guar     exact set / inner bound / outer bound / probability estimate / decision-quality approximation;
budget   computational time, memory, and reproducibility constraints.
```

No candidate algorithm advances until this signature is complete.

---

## 3. State-reduction gate

Framework v1 already recognized that full P–T–I–O viability computation may require a reduced state. Framework v2 retains that possibility but strengthens the validation obligation.

A candidate projection

```math
Y_V
=
\mathcal P_V(Y)
```

is admissible only if it preserves, to a declared tolerance or conservative bound, the quantities needed for:

```text
membership in K;
membership in G_rec;
avoidance of F;
feasible control authority;
P↔T dependency mechanisms that affect H3 outcomes;
future failure/recovery labels used by the H3 comparison.
```

The reduction must be compared against the unreduced model on a verification ensemble whenever the unreduced model is computationally executable for forward simulation.

A reduced model is not considered valid merely because its trajectories look qualitatively similar.

---

## 4. Candidate algorithm families and admissibility conditions

### 4.1 Dynamic programming / stochastic viability

**Scientific basis.** Stochastic viability kernels with chance constraints can be characterized by dynamic programming for suitable discrete-time constrained stochastic systems (Doyen & De Lara, 2010).

**Admissible when:**

```text
state/action representation is sufficiently low-dimensional or otherwise tractable;
transition probability model is qualified;
K/G/F are evaluable in the chosen state;
policy optimization is computationally feasible.
```

**Primary risk:** curse of dimensionality and transition-model misspecification.

### 4.2 Hamilton–Jacobi reachability

**Scientific basis.** HJ reachability provides formal reachable/safety set computations for nonlinear dynamics and bounded disturbances, but standard gridded methods scale exponentially with state dimension (Bansal et al., 2017).

**Admissible when:**

```text
reduced continuous state is small enough;
dynamics/disturbance game semantics match the H3 question;
discrete/hybrid modes and delays are handled explicitly or conservatively;
required deterministic/robust guarantee matches the uncertainty formulation.
```

**Primary risk:** dimensionality and mismatch with stochastic probability semantics.

### 4.3 Lagrangian / set-propagation methods

Maidens et al. (2013) use reachability to approximate viability kernels and demonstrate tractable algorithms for linear systems with convex input/state constraints. Gleason et al. (2021) provide grid-free under/over approximations for stochastic target-tube reachability; their computational implementation with available set tools is limited to linear systems despite broader nonlinear set-theoretic formulations.

**Admissible when:**

```text
linear/affine or justified local/reduced dynamics pass validation;
constraint and input geometry meets method assumptions;
approximation direction (inner/outer) is compatible with the engineering decision.
```

**Primary risk:** importing guarantees outside the linear/convex assumptions under which the algorithm is computationally realized.

### 4.4 Monte Carlo / scenario simulation

Forward Monte Carlo is appropriate for estimating probabilities under a **fixed declared policy and qualified stochastic model**.

It does not, by itself, compute a viability kernel requiring

```math
\exists\pi\in\Pi_{\rm adm}
```

unless combined with a defensible policy-search/control method.

**Admissible when:**

```text
probability model is qualified;
policy is fixed or policy search is separately defined;
sample-error tolerance is frozen;
rare-event limitations are addressed when relevant.
```

**Primary risk:** confusing sampled forward reliability with optimal controlled viability/reachability.

### 4.5 Sampling-based / optimization-based stochastic reachability

A sampling, particle, scenario-optimization, or policy-optimization method may be considered when exact set computation is infeasible.

**Admissible when:**

```text
its approximation target is mathematically identical to the declared H3 object;
finite-sample/convergence behavior can be characterized;
policy feasibility is enforced;
reference problems and held-out scenarios support verification.
```

**Primary risk:** unknown coverage/conservatism and optimizer-induced bias.

### 4.6 Surrogate / learned approximation

A neural or other surrogate may approximate a value function, boundary, probability, or policy only after a nonlearned reference problem has been established.

**Admissible when:**

```text
training/test domains are separated;
reference-solver or certified bounds exist on a verification subset;
boundary error and classification/probability error are reported;
out-of-domain behavior is controlled or explicitly excluded.
```

**Primary risk:** apparent scalability without trustworthy set-boundary or probability guarantees.

---

## 5. No-solver-by-default rule

At this stage:

```text
Dynamic programming:             CANDIDATE
Hamilton–Jacobi:                CANDIDATE
Lagrangian/set propagation:     CANDIDATE
Monte Carlo/scenario:           CANDIDATE COMPONENT
Sampling/optimization methods:  CANDIDATE
Surrogate/learned method:       CANDIDATE ONLY AFTER REFERENCE VERIFICATION
SELECTED H3 ALGORITHM:          NONE
```

The algorithm is selected only after `C_H3` is frozen and each candidate receives an assumption-compatibility PASS/FAIL.

---

## 6. Algorithm-selection matrix

For each candidate method `A_j`, record:

| Gate | Question | PASS condition |
|---|---|---|
| `A1` mathematical target | Does it compute/approximate the exact declared viability/reach–avoid object? | same quantified event/control semantics |
| `A2` dynamics | Do method assumptions match the reduced H3 dynamics? | verified or conservatively bounded |
| `A3` uncertainty | Does it match stochastic/robust/deep-uncertainty semantics? | no semantic substitution |
| `A4` geometry | Are `K/G/F/U` represented without invalid assumptions? | required convexity/smoothness etc. satisfied or safely approximated |
| `A5` hybrid/delay | Are modes/delays represented or bounded? | verified handling |
| `A6` scale | Is state/control dimension computationally feasible? | benchmark runtime/memory pass |
| `A7` guarantee | Is inner/outer/probability error suitable for the engineering use? | declared decision-compatible guarantee |
| `A8` verification | Can a reference/special-case solution be produced? | yes |
| `A9` reproducibility | Can software/version/seed/tolerance be frozen? | yes |
| `A10` validation | Can approximation be checked on independent forward outcomes? | yes |

A method is **eligible** only if all mandatory gates pass.

No weighted score is used to rescue a method that fails a mandatory mathematical assumption.

---

## 7. Mandatory reference problems

Before running the full coupled H3 model, the implementation must solve at least one low-dimensional problem with independently known or reference-computable viability/reachability behavior.

The reference suite must include, as applicable:

```text
R1 deterministic constrained system with known viable set;
R2 stochastic linear/affine target-tube problem with reference probability/set;
R3 reach–avoid problem with an explicit avoid set;
R4 reduced P–T toy system preserving one bidirectional coupling mechanism.
```

The purpose is to verify the solver, not to validate the infrastructure model.

---

## 8. Structural verification identities

The selected implementation must satisfy applicable mathematical sanity checks.

### 8.1 Probability bounds

```math
0\le P_{\rm viable}^{\pi}\le1,
\qquad
0\le P_{\rm recover}^{\pi}\le1.
```

### 8.2 Confidence-set monotonicity

For identical dynamics/policy/horizon and

```math
\alpha_2>\alpha_1,
```

verify

```math
\boxed{
\mathcal V_{\alpha_2,T_V}
\subseteq
\mathcal V_{\alpha_1,T_V}.
}
```

Similarly, if

```math
\beta_2>\beta_1,
```

then

```math
\boxed{
\mathcal R_{\beta_2,T_R}
\subseteq
\mathcal R_{\beta_1,T_R}.
}
```

### 8.3 Viability-horizon monotonicity

For time-invariant constraints/dynamics over the compared interval and

```math
T_{V,2}>T_{V,1},
```

verify the expected nesting

```math
\mathcal V_{\alpha,T_{V,2}}
\subseteq
\mathcal V_{\alpha,T_{V,1}}
```

when the mathematical assumptions supporting that comparison hold.

### 8.4 Recovery-horizon monotonicity

For identical reach–avoid semantics and

```math
T_{R,2}>T_{R,1},
```

verify

```math
\mathcal R_{\beta,T_{R,1}}
\subseteq
\mathcal R_{\beta,T_{R,2}}
```

when longer time cannot reduce admissible recovery opportunity under the declared target/avoid sets.

### 8.5 Control-authority monotonicity

If

```math
\Pi_1\subseteq\Pi_2,
```

then a correctly posed optimal-control calculation should not produce a smaller achievable viability/recovery probability solely from granting additional admissible policy choices.

### 8.6 Deterministic limit

When process uncertainty is removed and observation/state uncertainty collapses consistently, the stochastic implementation must approach the corresponding deterministic viability/reachability problem within declared numerical tolerance.

### 8.7 Avoid-set integrity

Every trajectory counted as a successful recovery realization must satisfy

```math
Y_s\notin F(s)
\quad
\forall s<\tau_G.
```

### 8.8 Policy feasibility

Every control action used in viability/recovery computation must satisfy

```math
u_t\in\mathcal U(Y,z_I,z_O,t).
```

An algorithm that improves reachability by using organizationally or physically infeasible actions fails verification.

---

## 9. Numerical convergence and error budget

The final solver must expose separate numerical-error sources, such as:

```text
time discretization;
state/control discretization;
set approximation;
Monte Carlo/sample error;
optimization tolerance;
surrogate approximation error;
random-seed variability.
```

Let

```math
u_{num,H3}
```

denote the declared aggregate numerical uncertainty floor for the final H3 output/metric. Its construction must be documented rather than hidden inside `delta_3`.

The confirmatory effect threshold must satisfy a scientifically defensible separation from numerical noise; otherwise a nominal skill increase can be a solver artifact.

---

## 10. Verification before validation

The order is

```math
\boxed{
\text{reference mathematics}
\rightarrow
\text{implementation verification}
\rightarrow
\text{reduced/full-model consistency}
\rightarrow
\text{empirical/held-out validation}
\rightarrow
\text{H3 confirmatory test}.
}
```

Agreement with infrastructure data does not substitute for solver verification, and numerical convergence does not establish that the physical/stochastic model is valid.

---

## 11. Solver decision record

The final solver-selection record must contain:

```text
selected algorithm/family;
software/package/commit;
mathematical target;
state/control dimension;
assumptions;
passed selection gates A1–A10;
failed/rejected alternatives and reason;
reference problems;
convergence evidence;
error bounds/uncertainty;
computational budget;
seed/tolerance/version manifest;
validation domain;
known failure modes.
```

Until this record exists and passes, `G_alg=0`.

---

## 12. Current decision

```text
H3 computational signature C_H3:     OPEN
H3 reduced state Y_V:                OPEN
H3 solver family:                    NOT SELECTED
algorithm-selection gates:           FROZEN
reference verification suite:        REQUIRED / FROZEN STRUCTURE
numerical error budget:              REQUIRED / VALUE OPEN
H3 algorithm gate G_alg:             0
H3 confirmatory execution:           NOT AUTHORIZED
```

This is a deliberate scientific result of the method-selection audit: the present evidence supports the **selection process**, not yet a specific solver.

---

## References — APA 7

Bansal, S., Chen, M., Herbert, S. L., & Tomlin, C. J. (2017). Hamilton-Jacobi reachability: A brief overview and recent advances. In *2017 IEEE 56th Annual Conference on Decision and Control (CDC)* (pp. 2242–2253). IEEE. https://doi.org/10.1109/CDC.2017.8263977

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008

Gleason, J. D., Vinod, A. P., & Oishi, M. M. K. (2021). Lagrangian approximations for stochastic reachability of a target tube. *Automatica, 128*, 109546. https://doi.org/10.1016/j.automatica.2021.109546

Maidens, J. N., Kaynama, S., Mitchell, I. M., Oishi, M. M. K., & Dumont, G. A. (2013). Lagrangian methods for approximating the viability kernel in high-dimensional systems. *Automatica, 49*(7), 2017–2029. https://doi.org/10.1016/j.automatica.2013.03.020

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458
