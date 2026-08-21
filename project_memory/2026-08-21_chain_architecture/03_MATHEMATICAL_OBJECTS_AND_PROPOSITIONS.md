# Mathematical Objects, Definitions and Propositions

This file preserves the mathematical language that future chats should reuse unless a documented amendment changes it.

## 1. State, interfaces, modes and observations

```text
X(t)=[X_P(t),X_W(t),X_T(t),X_SW(t)]^T
```

Dynamic interface state: `Z(t)`.

Discrete operating/failure mode: `m(t)`.

Control/intervention: `u(t)`.

Climate forcing: `xi(t)`.

Realized hazard: `eta(t)`.

Unknown/uncertain parameters: `theta`.

Observation model:

```text
Y=H(X,Z;theta)+epsilon_Y
```

## 2. Coupled hybrid multiscale dynamics

```text
X_dot=F(X,Z,m,u,eta;theta)
epsilon Z_dot=G(X,Z,m,eta;theta)
m+=Phi(X,Z,m,eta)
```

Interpretation:

- `F` = coupled sector dynamics;
- `G` = dynamic interface evolution;
- `epsilon` = relative interface/system timescale parameter where appropriate;
- `Phi` = hybrid switching/failure/recovery rule.

## 3. Coupling operator

A useful block representation is

```text
A(t)=
[A_PP  A_PW  A_PT  A_PSW
 A_WP  A_WW  A_WT  A_WSW
 A_TP  A_TW  A_TT  A_TSW
 A_SWP A_SWW A_SWT A_SWSW]
```

Diagonal blocks are intra-sector relations; off-diagonal blocks represent declared cross-sector mechanisms. Adjacency alone must not be treated as the full interface law.

## 4. Service mapping

```text
S(t)=Psi(X(t),m(t),Z(t))
```

Service deficit:

```text
D_i(t)=[S_i^req-S_i(t)]_+
```

Cumulative weighted consequence:

```text
L=∫_0^T sum_i w_i D_i(t) dt
```

## 5. Sustainable-equitable admissibility

```text
K_R=K_phys ∩ K_service ∩ K_sus ∩ K_eq
```

Each set must ultimately be given measurable operational definitions.

## 6. Viability kernel

```text
V_R={x0 in K_R : exists admissible u(.) such that X(t;x0,u,eta,theta) remains in K_R over the declared horizon}
```

Central object:

```text
∂V_R
```

The viability boundary is the primary geometric object whose deformation/sensitivity is studied.

## 7. Recovery / capture basin

```text
C_R={x0 : exists admissible u(.), exists finite T, X(T;x0,u) in V_R}
```

Minimum recovery time:

```text
tau_R(x0)=inf{T : exists admissible u(.), X(T;x0,u) in V_R}
```

## 8. Reachability / Hamilton–Jacobi family

Representative PDE family:

```text
∂_t V + H(x,∇V)=0
```

A common game Hamiltonian form is

```text
H(x,p)=min_u max_d p^T f(x,u,d)
```

but the precise sign and min/max convention must be derived from the declared target, control and disturbance formulation. Do not copy this formula mechanically into a final model without verifying conventions.

## 9. Dynamic/static interface comparison

```text
V_static=V(Z_bar)
V_dynamic=V(Z(t))
```

Candidate boundary-deformation metric:

```text
Delta_V=d_H(V_dynamic,V_static)
```

where `d_H` is a declared Hausdorff-type set distance or another explicitly justified metric.

Timescale ratio:

```text
rho_ij=tau_interface,ij/tau_system
```

## 10. Inverse problem

Regularized estimator template:

```text
theta_hat=argmin_theta ||Y_obs-G(theta)||^2_{Sigma^-1}+lambda R(theta)
```

Bayesian form:

```text
p(theta|Y) ∝ p(Y|theta)p(theta)
```

Identifiability condition/question:

```text
G(theta1)=G(theta2) => theta1=theta2 ?
```

Viability reliability diagnostic:

```text
E_inv=d_H(V(theta_star),V(theta_hat))
```

Probabilistic extension:

```text
P(x in V_R | D_obs)
```

## 11. Viability-preserving control

Conceptual tangent condition:

```text
U_V(x)={u : F(x,u,eta) points into an admissible tangent direction of K_R at x}
```

A formal tangent-cone expression may be used only under the appropriate viability-theory assumptions.

## 12. Design dependence

```text
d={capacity,topology,redundancy,storage,interface hardening,...}
```

```text
d → F_d → V_R(d), C_R(d)
```

Optimization follows only after the feasible/viable geometry is defined.

## 13. Frozen proposition family

### P1 / H0 — Dynamic interfaces matter

Test whether

```text
V(Z(t)) materially differs from V(Z_bar)
```

under prespecified deformation criteria.

### P2 / H1 — Identifiability → viability reliability

Test propagation

```text
D_obs → theta_hat / Sigma_theta → uncertainty/error in V_R
```

### P3 / H2 — Timescale regime

Test whether `rho_ij` predicts static-approximation error.

### H3 — Viability-based interface criticality

Define interface criticality using deformation/sensitivity of `V_R` or `∂V_R`, then compare it with conventional topology/flow criticality.

### P4 / H4 — Sustainability/equity geometry

Compare

```text
V(K_technical)
```

with

```text
V(K_sus,eq)
```

to quantify constraint-induced deformation.

### P5 / H5 — Recovery is not viability

Compute and interpret

```text
C_R \ V_R
```

and `tau_R`.

### P6 / H6 — Waste–drainage–flood feedback

Compare otherwise matched P–W–T–SW models with the feedback mechanism enabled/disabled.

### H7 — Time-varying admissibility / nonanticipative recovery

Optional extension if the MSE scope permits time-varying constraints or nonanticipative recovery policies.

### P7 / T1 — Conservative reduction

For a reduced model `r`, require a preservation/bounding statement such as

```text
V_r approximately preserves or conservatively bounds the projected full-order viability geometry
```

with an explicit set/error metric.

## 14. Mathematical-rigor requirements

For any proposed forward model, future work should explicitly ask:

1. Does a solution exist?
2. Is it unique / well posed under declared assumptions?
3. Is the solution stable / continuously dependent on inputs?
4. What is parameter/state sensitivity?
5. Are unknown quantities identifiable/observable?
6. Can the mathematical object be computed with a convergent numerical method?
7. How does uncertainty propagate to the viability/recovery outputs?
8. Can the model be validated against real or accepted benchmark behavior?

## 15. No false uniqueness

Do not claim a “unique infrastructure solution” because an optimizer returns one point. Distinguish:

- uniqueness of a physical trajectory;
- identifiability of inverse parameters;
- uniqueness of an optimal control;
- uniqueness of a design optimum;
- uniqueness of a viscosity solution to an HJ/HJI equation.

Each requires different assumptions and proof/verification.