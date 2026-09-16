# Canonical Notation Reconciliation — Novelty Audit

**Date:** 2026-09-16  
**Status:** ACTIVE INTERPRETATION RULE for 2026-09-16 novelty-audit artifacts  
**Canonical authority:** `project/CANONICAL_DEPENDENCY_CONTRACT_V1.md`

## Purpose

The public novelty audit and ASU prior-work audit were produced after the thesis dependency contract had already been canonicalized. Some working novelty expressions nevertheless reused the older flat dependency notation. This file prevents those working expressions from overriding the canonical representation.

## 1. Canonical dependency object

All active thesis reasoning uses

```math
\boxed{\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)}
```

with

```math
\mathcal C_e=(s_e,p_e^s,r_e,p_e^r,\chi_e),
```

```math
\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e),
```

```math
\Pi_e=(\mathcal P_e,V_e,\mathcal U_e).
```

The former flat object

```math
\mathfrak I_{ij}^{\alpha\beta}
=(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t)
```

is legacy provenance only.

## 2. Correct interpretation of the residual novelty candidate N1

The working N1 residual is therefore not the legacy tuple. It is the unresolved question whether the canonical contract can be evidence-qualified and shown useful as a reusable mechanistic interface representation:

```math
\boxed{
N_1':
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)
\longrightarrow
\Xi_e
\longrightarrow
F_{\mathcal G}^{m}
}
```

across physical, informational and organizational dependency classes, with matched ablation against weaker representations.

The contract is canonical **within this thesis**. Its global novelty remains `UNRESOLVED_GLOBAL`.

## 3. Correct interpretation of viability-sensitive dependency criticality

A universal scalar edge weight `w_e` is not a primitive field of the canonical dependency contract. Therefore active Stage-5 sensitivity must be taken with respect to a declared physically meaningful perturbation of `Sigma_e`, normally through one or more components of `theta_e`, `gamma_e`, `Phi_e`, or a declared intervention on the dependency mechanism.

Let

```math
\rho_g(Y;\Theta)
=
d_{g}(Y,\partial\mathcal V_{\rm sus}(\Theta)),
```

where `Theta` denotes the full declared model/dependency parameterization. For a differentiable parameterization, a local diagnostic may be defined as

```math
\boxed{
S_{e,v}^{\mathcal V}(Y)
=
- D_{\theta_e}\rho_g(Y;\Theta)[v]
}
```

for a declared, physically interpretable perturbation direction `v`.

If differentiability is not established, use a finite perturbation or intervention effect rather than inventing a derivative:

```math
\boxed{
S_{e,v,\varepsilon}^{\mathcal V}(Y)
=
-\frac{
\rho_g(Y;\Theta_{e,\varepsilon v})
-
\rho_g(Y;\Theta)
}{\varepsilon}.
}
```

For confirmatory intervention ranking, the primary quantity should be an actual viability/service improvement under matched intervention budgets, not the derivative alone.

## 4. Metric rule

Distance to a viability boundary and geometric robustness are prior art. A non-Euclidean metric `g_psi` is therefore not assumed to be a contribution and is not automatically preferred.

The minimum valid comparison is

```math
\boxed{
g_0\;(\text{declared baseline metric})
\quad\text{vs}\quad
g_\psi\;(\text{candidate learned/physics-informed metric}).}
```

`g_psi` is retained only if its assumptions, invariances, scaling and decision value survive matched tests.

## 5. Partial-observation rule

Partial-observation safety, estimator-aware safety, belief-space control, stochastic viability and probabilistic safe-set methods are established prior art. The thesis cannot claim novelty for

```math
D_{0:t}\to p(Y_t\mid D_{0:t})
```

or probabilistic safety/viability in isolation.

The narrower unresolved question is infrastructure-specific integration of heterogeneous `P,T,I,O` observations, mechanistic coupled dynamics, organizationally constrained feasible controls and sustainability-constrained viability.

## 6. Precedence

Whenever the following files conflict in notation,

1. `project/CANONICAL_DEPENDENCY_CONTRACT_V1.md` governs dependency semantics;
2. `project/CANONICAL_7_STAGE_FRAMEWORK.md` governs stage boundaries;
3. this reconciliation governs interpretation of 2026-09-16 novelty artifacts;
4. older novelty/audit formulas are treated as working provenance, not active notation.
