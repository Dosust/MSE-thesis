# Scientific State of the Thesis

## 1. Research identity

The thesis currently sits primarily across **Dynamics → Resilience/Viability → Control**, with **Representation, inverse problems and uncertainty quantification upstream**, and **Design/Optimization/Decision downstream**.

The intended contribution is not a generic resilience score. The thesis asks which climate-stressed trajectories of a dynamically coupled P–W–T–SW system are physically feasible, service-preserving, sustainable and equitable; which states remain viable; which disrupted states remain recoverable; how these sets depend on uncertain/dynamic interfaces; and which admissible interventions preserve or restore viability.

## 2. Governing state and interface representation

Coupled state:

```text
X(t) = [X_P(t), X_W(t), X_T(t), X_SW(t)]^T
```

Dynamic interface state: `Z(t)`.

Hybrid mode: `m(t)`.

Control: `u(t)`.

Exogenous forcing: `xi(t)`.

Realized local hazard: `eta(t)`.

Unknown/uncertain model/interface parameters: `theta`.

Observation equation:

```text
Y = H(X,Z;theta) + epsilon_Y
```

Reduced hybrid multiscale dynamics:

```text
X_dot = F(X,Z,m,u,eta;theta)
epsilon Z_dot = G(X,Z,m,eta;theta)
m+ = Phi(X,Z,m,eta)
```

This formulation intentionally separates continuous state evolution, interface evolution, discrete failure/operating modes, control, hazard and observation.

## 3. Physics → service distinction

`X(t)` is the physical infrastructure state. `S(t)` is the delivered service state.

A generic service mapping is

```text
S(t) = Psi(X(t),m(t),Z(t))
```

A functioning physical component does not automatically imply adequate service. This distinction is necessary before equity or population impacts can be defined.

## 4. Admissibility

The current conceptual admissible region is

```text
K_R = K_phys ∩ K_service ∩ K_sus ∩ K_eq
```

Hence technical operation alone is not sufficient for sustainable-equitable admissibility.

Important scientific statement:

```text
operational recovery does not imply sustainable-equitable recovery
```

Final thesis inference requires each component of `K_R` to be operationalized by explicit measurable constraints.

## 5. Viability

The viability kernel is

```text
V_R = {x0 in K_R : exists admissible u(.) such that X(t;x0,u,eta,theta) in K_R for all relevant t}
```

The central geometric object is the boundary `∂V_R`.

This converts resilience from only a performance-area metric into a state-space feasibility question.

## 6. Recovery / capture geometry

Recovery is distinct from viability:

```text
C_R = {x0 : exists u(.), exists finite T such that X(T;x0,u) in V_R}
```

Minimum recovery time:

```text
tau_R(x0) = inf {T : exists u(.), X(T;x0,u) in V_R}
```

State classes:

1. viable;
2. recoverable but not currently viable;
3. nonrecoverable under the declared model/control/hazard assumptions.

## 7. Dynamic-interface proposition

Static approximation:

```text
V_static = V(Z_bar)
```

Dynamic interface model:

```text
V_dynamic = V(Z(t))
```

Candidate deformation diagnostic:

```text
Delta_V = d_H(V_dynamic, V_static)
```

Timescale ratio:

```text
rho_ij = tau_interface,ij / tau_system
```

The research question is to identify conditions/regimes under which replacing `Z(t)` by a static coupling is acceptable or materially misleading.

## 8. Inverse problem / identifiability

The thesis architecture does not assume hidden interfaces are perfectly known.

Upstream inference:

```text
D_obs → p(G,theta,Z | D_obs)
```

Regularized estimation template:

```text
theta_hat = argmin_theta ||Y_obs - G(theta)||^2_{Sigma^-1} + lambda R(theta)
```

Identifiability asks whether

```text
G(theta_1) = G(theta_2)  =>  theta_1 = theta_2
```

under the declared observation model.

A central proposed reliability diagnostic is

```text
E_inv = d_H(V(theta_star), V(theta_hat))
```

or a probabilistic analogue when posterior uncertainty is propagated.

## 9. Hazard/failure chain

Separate climate forcing from realized hazard:

```text
xi(t) → eta(t)
```

For the demonstrator:

```text
rainfall forcing → inundation/flood stress
```

Candidate solid-waste feedback:

```text
X_SW → drainage blockage → eta_flood → (X_P,X_W,X_T,X_SW)
```

Transportation accessibility may also affect waste-removal capacity, producing another feedback.

Failure can be represented as mode switching/topology change:

```text
m_i(t-) → m_i(t+)
A(t-) → A(t+)
F(X;A-) → F(X;A+)
```

## 10. Control

First-order control question:

```text
Does an admissible control exist?
```

before solving a full optimal-control problem.

A viability-preserving control set can be written conceptually as

```text
U_V(x) = {u : F(x,u,eta) belongs to the admissible tangent direction at x}
```

where tangent-cone formulations are used only where mathematical assumptions are satisfied.

## 11. Design and optimization

Design vector:

```text
d = {topology, capacity, redundancy, storage, interface hardening, backup/flexibility}
```

Design changes the dynamic system and therefore resilience geometry:

```text
d → F_d → V_R(d), C_R(d)
```

A downstream design problem can then minimize cost/carbon/service loss/inequity/recovery time subject to physical, sustainability, equity, budget and viability/recovery constraints.

## 12. Mathematical-rigor hierarchy

The intended hierarchy is:

```text
Model definition
→ existence
→ uniqueness / well-posedness
→ stability
→ sensitivity
→ identifiability / observability
→ computability / numerical convergence
→ uncertainty propagation
→ validation
```

A numerical optimizer returning one point is not evidence of mathematical uniqueness.

## 13. Scope control

For the current MSE, the scientifically coherent center remains **dynamic-interface identification + coupled dynamics + sustainable/equitable viability/recovery geometry**, with control as an enabling layer and design/optimization as limited demonstration or future extension.

A full theory-to-policy treatment across all stages is a long-term research program rather than a requirement that every layer contain equal original novelty in one MSE thesis.