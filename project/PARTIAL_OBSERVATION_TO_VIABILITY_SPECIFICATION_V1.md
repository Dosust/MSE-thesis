# Partial Observation to Viability Specification v1.0

**Date:** 2026-09-16  
**Status:** WORKING MATHEMATICAL SPECIFICATION — not a novelty claim and not yet empirically validated  
**Stages:** 3 → 4 → 5  
**Authority:** subordinate to `CANONICAL_7_STAGE_FRAMEWORK.md`, `CANONICAL_DEPENDENCY_CONTRACT_V1.md`, and the frozen hypothesis files

## 1. Scientific purpose

Formalize the minimum admissible bridge from heterogeneous observations to uncertain infrastructure state and then to viability-relevant diagnostics without confusing state estimation with resilience or claiming partial-observation safety as novel.

The working chain is

```math
\boxed{
D_{0:k}
\rightarrow
b_k(Y)
\rightarrow
\text{coupled prediction}
\rightarrow
\mathcal V_{\rm sus}
\rightarrow
\text{viability-relevant uncertainty diagnostics}.
}
```

Here

```math
b_k(y)=p(Y_k=y\mid D_{0:k},u_{0:k-1})
```

is a belief/posterior state representation.

## 2. Prior-art boundary

The thesis does **not** claim novelty for any of the following:

- Bayesian filtering or belief states;
- stochastic viability;
- partially observable safety control;
- estimator-aware barrier functions;
- belief-space reach-avoid control;
- probabilistic safe-set certification.

Relevant prior art includes partially observed stochastic control with barrier functions, incomplete-information stochastic CBFs, risk-aware CBFs using state-estimation error bounds, and belief-space safety/reach-avoid control.

Representative anchors:

- Jahanshahi, Jagtap & Zamani (2020), *Synthesis of Stochastic Systems with Partial Information via Control Barrier Functions*, IFAC-PapersOnLine, DOI `10.1016/j.ifacol.2020.12.187`.
- Clark (2021), *Control barrier functions for stochastic systems*, Automatica 130, 109688, DOI `10.1016/j.automatica.2021.109688`.
- IEEE Control Systems Letters (2025), *Conformal Prediction in the Loop: Risk-Aware Control Barrier Functions for Stochastic Systems With Data-Driven State Estimators*, DOI `10.1109/LCSYS.2025.3571828`.
- Vahs, Verhagen & Tumova (2026), *Safety-critical Control Under Partial Observability: Reach-Avoid POMDP meets Belief Space Control*, arXiv:2603.10572.

Therefore the admissible thesis question is narrower:

> Does explicit propagation of heterogeneous infrastructure observation uncertainty through validated `P-T-I-O` dynamics and organizationally constrained controls materially change sustainable-viability diagnosis or engineering decisions?

## 3. State and observation model

Use the canonical state

```math
Y_k=
\begin{bmatrix}
x_{P,k}\\x_{T,k}\\z_{I,k}\\z_{O,k}\end{bmatrix}.
```

A general discrete-time prediction form is

```math
Y_{k+1}
=
f_k(Y_k,u_k,h_k;\Theta)+\omega_k,
```

where `Theta` includes constituent-system parameters and canonical dependency semantics.

Observations are represented as

```math
D_k
=
h_k^{obs}(Y_{k-\ell_k};z_{I,k})+\nu_k,
```

where the information state may affect:

```text
sensor availability;
latency ell_k;
data freshness;
measurement noise/error;
packet/report loss;
observation resolution.
```

No Gaussian assumption is imposed globally. Distributional assumptions must follow the selected data/estimator.

## 4. Belief update

The abstract Bayesian prediction is

```math
b_{k|k-1}(y)
=
\int
p(y\mid y',u_{k-1},h_{k-1};\Theta)
\,b_{k-1}(y')\,dy'.
```

The abstract measurement update is

```math
b_k(y)
=
\frac{
p(D_k\mid y,z_{I,k})b_{k|k-1}(y)
}{
\int p(D_k\mid \xi,z_{I,k})b_{k|k-1}(\xi)d\xi
}.
```

This notation does not prescribe an EKF, UKF, particle filter, ensemble method or learned estimator. Estimator choice must be based on the state equations, observation nonlinearity, data volume, uncertainty structure and validation evidence.

## 5. Estimator outputs required by Stage 4

At minimum, the implementation must make available either a full numerical belief representation or a declared approximation sufficient to report:

```math
\widehat Y_k=\mathbb E[Y_k\mid D_{0:k}],
```

and an uncertainty object such as

```math
\Sigma_{Y,k}=\operatorname{Cov}(Y_k\mid D_{0:k})
```

when second moments are meaningful.

A covariance matrix is not an adequate uncertainty representation for strongly multimodal or bounded/discrete organizational states unless the approximation is explicitly justified.

## 6. Connection to feasible control

Information uncertainty and organizational feasibility are distinct mechanisms.

Information affects what is known:

```math
z_I
\rightarrow
b_k(Y).
```

Organization affects what can be done:

```math
z_O
\rightarrow
\mathcal U_k(z_I,z_O).
```

The operational policy is therefore written as

```math
u_k
=
\pi_k(b_k,z_{I,k},z_{O,k}),
\qquad
u_k\in\mathcal U_k(z_{I,k},z_{O,k}).
```

Point-estimate control

```math
u_k=\pi_k(\widehat Y_k)
```

is a baseline approximation, not the assumed truth.

## 7. Viability under uncertain state knowledge

The canonical state-space controlled viability set remains

```math
\mathcal V_{\rm sus}^{u,T}
=
\left\{
Y_0\in K_{\rm sus}:
\exists u(\cdot),\
Y^u(t)\in K_{\rm sus}\ \forall t\in[0,T]
\right\}.
```

This file does not redefine the viability kernel as a posterior distribution.

Given a validated state-space viability set, a minimum observation-aware diagnostic is posterior viable mass:

```math
\boxed{
\pi_{\mathcal V,k}
=
\Pr\!\left(
Y_k\in\mathcal V_{\rm sus}^{u,T}
\mid D_{0:k}
\right)
=
\int_{\mathcal V_{\rm sus}^{u,T}} b_k(y)dy.
}
```

This is a diagnostic of current-state uncertainty relative to the viable set. It is **not** a new viability kernel and must not be interpreted as a future safety probability unless the dynamics/control/uncertainty model justifies that interpretation.

A credible or conformal state region `C_k` may support the stronger diagnostic

```math
C_k\subseteq\mathcal V_{\rm sus}^{u,T},
```

but any probability/coverage interpretation requires independently justified calibration and coverage assumptions.

## 8. Propagated viability uncertainty

For uncertain parameters/model forms `Theta`, define the viability object explicitly as conditional on the model realization:

```math
\mathcal V_{\rm sus}^{u,T}(\Theta).
```

Then uncertainty in viability may be characterized by an ensemble or posterior over derived quantities such as

```math
\rho(Y;\Theta),
\qquad
\mu(\mathcal V(\Theta)),
\qquad
T_{\mathcal V}(Y;\Theta),
```

provided each quantity is well-defined.

The thesis must distinguish:

```math
\boxed{
\text{uncertainty in current state}
\neq
\text{uncertainty in model/parameters}
\neq
\text{future process uncertainty}.
}
```

## 9. H2/H3 ablation design

The minimum nested information experiment is:

```math
\mathscr N_0=P+T,
```

```math
\mathscr N_1=P+T+I,
```

```math
\mathscr N_2=P+T+I+O.
```

For the inference pathway, compare at least:

```text
B0: perfect/current state assumption;
B1: point estimate from noisy/delayed observations;
B2: uncertainty-aware belief/ensemble representation.
```

Under matched physical scenarios, quantify whether the richer observation model materially changes:

```math
\widehat Y,
\quad
\pi_{\mathcal V},
\quad
\rho,
\quad
\text{selected }u,
\quad
\text{service/recovery outcomes}.
```

## 10. Verification and validation gates

Before any inference-to-viability conclusion:

1. observation timestamps/latencies must be verified;
2. measurement-error assumptions must be evidence-supported;
3. estimator must be validated on held-out observations or equivalent independent tests;
4. uncertainty calibration/coverage must be checked, not assumed;
5. prediction dynamics must pass the constituent/coupling verification gates;
6. viability set must be independently defensible;
7. estimator uncertainty must not be counted twice in model/process uncertainty;
8. the simpler point-estimate baseline must be retained.

## 11. Current status

```text
MATHEMATICAL BRIDGE: SPECIFIED
ESTIMATOR FAMILY: NOT FROZEN
OBSERVATION DATA: H1 ROW-LEVEL GATE PENDING / LATER H2 DATA NOT YET QUALIFIED
UNCERTAINTY CALIBRATION: NOT EXECUTED
VIABILITY COMPUTATION: DEFERRED
NOVELTY: NOT CLAIMED
```

This specification permits later implementation without pretending that the evidence or empirical validation already exists.
