# Canonical Scientific State — v2

## 1. Thesis identity

**Working title:** Mathematical Physics of Sustainable Infrastructure Resilience.

**Current precise formulation:** *Equity-Constrained Viability of Coupled Power–Water–Transportation–Solid-Waste Systems with Dynamic Interfaces under Climate Stress*.

**Current sector set:**

- Power (P)
- Water / drainage (W)
- Transportation (T)
- Solid Waste (SW)

**Primary demonstrator:** **urban flooding with waste–drainage–transport feedbacks**.

The formal P6 proposition remains narrower: **waste–drainage–flood feedback shifts P–W–T–SW resilience boundaries**. The broader demonstrator may additionally include transport accessibility effects on waste removal and recovery.

## 2. Core MSE contribution

The authoritative scope states that the core mathematical contribution is centered on:

```text
dynamic coupling
→ admissibility
→ viability
→ recovery
```

Identification / inverse problems / UQ are upstream support. Control and design are structured extensions.

The governing core architecture is:

```text
D_obs
→ (G_hat, theta_hat, Sigma_theta)
→ F_dyn
→ K_R
→ V_R
→ C_R
→ U_recovery
```

The broad research program may continue to design, optimization and decision, but those are not automatically part of the central original MSE contribution.

## 3. Central scientific object

The principal geometric object is:

```text
∂V_R
```

where `V_R` is the sustainability/equity-constrained viability kernel.

The three governing questions are:

1. What moves the viability boundary?
2. How uncertain is that boundary?
3. What interventions or designs move it in a favorable direction?

The current central research question in the authoritative scope is:

> How accurately must dynamic cross-infrastructure interfaces be identified and represented before sustainable/equitable viability and recovery predictions can be trusted?

## 4. Governing state variables

```text
X(t) = [X_P(t), X_W(t), X_T(t), X_SW(t)]^T
```

with:

- `Z(t)` — dynamic interface state;
- `m(t)` — discrete operating/failure mode;
- `u(t)` — intervention/recovery control;
- `xi(t)` — exogenous climate forcing;
- `eta(t)` — realized local hazard/stress;
- `theta` — uncertain physical/interface parameters;
- `Y(t)` — partial observations.

## 5. Governing hybrid multiscale model

```text
X_dot = F(X,Z,m,u,eta;theta)
epsilon Z_dot = G(X,Z,m,eta;theta)
m+ = Phi(X,Z,m,eta)
Y = H(X,Z;theta) + epsilon_Y
```

This is a general reduced mathematical architecture, not yet a fully calibrated sector-specific model.

## 6. Forcing versus realized hazard

The distinction is frozen conceptually:

```text
xi(t) → eta(t)
```

For the demonstrator:

```text
rainfall forcing → realized flood/inundation stress
```

Candidate endogenous mechanism:

```text
X_SW → B_drain → eta_flood → (X_P,X_W,X_T,X_SW)
```

Transport accessibility may influence waste-removal capacity, producing an additional feedback.

## 7. Admissibility

```text
K_R = K_phys ∩ K_service ∩ K_sus ∩ K_eq
```

This means admissibility is not merely technical operation. The final thesis must operationalize all four components with measurable constraints and units.

## 8. Viability

Current formal definition:

```text
V_R = {x0 in K_R : exists admissible u(.) such that X(t;x0,u,eta,theta) remains in K_R for the declared viability horizon}
```

The current mathematical-foundation file uses `forall t >= 0`. A later finite-horizon or time-varying formulation must be documented as an amendment rather than silently substituted.

## 9. Recovery / capture geometry

```text
C_R = {x0 : exists admissible u(.), exists finite T, such that X(T;x0,u) is in V_R}
```

```text
tau_R(x0) = inf {T : exists admissible u(.), X(T;x0,u) is in V_R}
```

State classes:

```text
viable
| recoverable but nonviable
| nonrecoverable under the declared model/control/hazard assumptions
```

## 10. Dynamic interface comparison

```text
V_dyn = V(Z(t))
V_static = V(Z_bar)
```

Candidate deformation metric:

```text
Delta_V = d_H(V_dyn,V_static)
```

Timescale ratio:

```text
rho_ij = tau_interface,ij / tau_system
```

The intended test is whether fast/commensurate/slow interface regimes explain when static coupling is an acceptable approximation.

## 11. Upstream inverse problem

```text
D_obs → p(G,theta,Z | D_obs)
```

Candidate deterministic diagnostic:

```text
E_inv = d_H(V(theta_star),V(theta_hat))
```

Probabilistic extension:

```text
P(x in V_R | D_obs)
```

## 12. Control and design status

Control is an extension built on viable/recovery geometry. A formal viability-preserving control condition may be expressed through a tangent-cone condition where assumptions permit.

Design variables may include topology, capacity, redundancy, storage and interface hardening:

```text
d → F_d → V_R(d), C_R(d)
```

This is a downstream extension; the present MSE does not need original contributions at every design/optimization/policy layer.

## 13. Evidence architecture

Two linked but non-interchangeable tracks remain:

1. **PRISMA / evidence falsification and precedent search**;
2. **mathematical development and falsification**.

A direct precedent is a successful falsification/narrowing result, not a failure.

## 14. Current scope discipline

The preferred MSE emphasis is:

```text
identify uncertain/dynamic interfaces
→ model coupled dynamics
→ define sustainable/equitable admissibility
→ analyze viability boundary
→ analyze recovery/capture geometry
→ demonstrate admissible control and, if feasible, limited design consequences
```

This is the strongest current interpretation of the authoritative repository state.