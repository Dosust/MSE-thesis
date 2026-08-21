# Mathematical Model and Core Objects — v2

This file mirrors the current authoritative mathematical foundation while marking which expressions are definitions, generic templates, or proposed diagnostics.

## 1. Coupled state

```text
X(t)=[X_P(t),X_W(t),X_T(t),X_SW(t)]^T in X_space
```

This is a block state, not four scalars by assumption. Each sector block may contain multiple physical state variables.

## 2. Dynamic interfaces

`Z(t)` represents time-varying cross-sector interface states. The thesis should not equate a graph edge with a complete interface law.

A valid interface term should correspond to a specified mechanism such as capacity exchange, dependency, delay, switching, access, transfer, common-resource constraint, or failure/recovery coupling.

## 3. Governing hybrid multiscale architecture

```text
X_dot = F(X,Z,m,u,eta;theta)
epsilon Z_dot = G(X,Z,m,eta;theta)
m+ = Phi(X,Z,m,eta)
Y = H(X,Z;theta) + epsilon_Y
```

Status: **MATHEMATICAL_DEFINITION / WORKING ARCHITECTURE**, not empirical validation.

`epsilon` is used as an interface/system timescale parameter in the current foundation. A later nondimensional derivation should justify its scaling.

## 4. Coupling operator

```text
A(t)=
[A_PP  A_PW  A_PT  A_PSW
 A_WP  A_WW  A_WT  A_WSW
 A_TP  A_TW  A_TT  A_TSW
 A_SWP A_SWW A_SWT A_SWSW]
```

Diagonal blocks represent intra-sector structure; off-diagonal blocks represent declared cross-sector interface/interdependency terms.

## 5. Climate forcing and endogenous hazard modification

Frozen conceptual distinction:

```text
xi(t) → eta(t)
```

Candidate demonstrator mechanism:

```text
X_SW → B_drain → eta_flood → X
```

Transport accessibility can affect waste-removal operations and therefore may close an additional feedback loop in the demonstrator.

Status: **PROPOSED_MECHANISM until calibrated/verified**.

## 6. Service mapping

The physical state should be mapped to service before equity/population consequences are calculated:

```text
S(t)=Psi(X(t),m(t),Z(t))
```

This service mapping is conceptually required but not yet frozen in sector-specific form.

## 7. Admissible set

```text
K_R=K_phys ∩ K_service ∩ K_sus ∩ K_eq
```

Status: **FROZEN ARCHITECTURE, OPERATIONAL THRESHOLDS PENDING**.

The final model must define units, thresholds and aggregation rules for each component.

## 8. Viability kernel

Current repository definition:

```text
V_R={x0 in K_R : exists admissible u(.) such that X(t;x0,u,eta,theta) in K_R for all t>=0}
```

Status: **MATHEMATICAL_DEFINITION**.

If the final demonstrator uses a finite time horizon, moving admissible set, stochastic viability, or nonanticipative disturbance formulation, that must be documented as a formal amendment.

Central object:

```text
∂V_R
```

## 9. Capture/recovery set

```text
C_R={x0 : exists admissible u(.), exists finite T, X(T;x0,u) in V_R}
```

Minimum recovery-time map:

```text
tau_R(x0)=inf{T : exists admissible u(.), X(T;x0,u) in V_R}
```

These are distinct from classical area-under-performance-curve resilience metrics.

## 10. Dynamic/static interface comparison

```text
V_dyn=V(Z(t))
V_static=V(Z_bar)
```

Candidate set-distance diagnostic:

```text
Delta_V=d_H(V_dyn,V_static)
```

This does not force Hausdorff distance to be the only metric. Boundary distance, volume/measure change, critical-state changes and service/recovery effects may also be needed.

## 11. Timescale ratio

```text
rho_ij=tau_interface,ij/tau_system
```

Candidate regimes:

```text
rho_ij << 1  : fast interface
rho_ij ~ 1   : commensurate dynamics
rho_ij >> 1  : slow interface
```

The final nondimensional interpretation must be tied to explicit characteristic timescales.

## 12. Inverse problem

Upstream architecture:

```text
D_obs → p(G,theta,Z | D_obs)
```

Generic regularized estimator:

```text
theta_hat=argmin_theta ||Y_obs-G(theta)||^2_{Sigma^-1}+lambda R(theta)
```

Generic Bayesian form:

```text
p(theta|Y) proportional to p(Y|theta)p(theta)
```

Identifiability question:

```text
G(theta1)=G(theta2) => theta1=theta2 ?
```

## 13. Viability reliability under identification error

Current proposed diagnostic:

```text
E_inv=d_H(V(theta_star),V(theta_hat))
```

Probabilistic extension:

```text
P(x in V_R | D_obs)
```

Status: **PROPOSED THESIS DIAGNOSTIC**.

## 14. Reachability / HJ-HJI family

Representative PDE family:

```text
partial_t V + H(x,grad V)=0
```

A representative game Hamiltonian may use a min/max over control and disturbance, but the sign and optimization order depend on the exact target, control and disturbance convention. The final thesis must derive the correct convention rather than copy a generic formula.

## 15. Viability-preserving control

Current formal template:

```text
U_V(x)={u : F(x,u,eta) in T_{K_R}(x)}
```

where the tangent-cone formulation is valid only under the assumptions required by viability theory.

## 16. Design dependence

```text
d={capacity,topology,redundancy,storage,interface hardening,...}
```

```text
d → V_R(d)
d → C_R(d)
```

A downstream optimization can be defined only after physical and admissibility constraints are frozen.

## 17. Mathematical-rigor ladder

For each final model component, future work should address:

```text
model definition
→ existence
→ uniqueness / well-posedness
→ stability
→ sensitivity
→ observability / identifiability
→ numerical consistency/convergence
→ uncertainty propagation
→ calibration/validation
```

Do not infer mathematical uniqueness from one numerical optimizer result.

## 18. Primary distinction to preserve

```text
state trajectory X(t)
!= delivered service S(t)
!= resilience performance metric
!= viability kernel V_R
!= recovery/capture set C_R
!= optimal design d*
```

These are related but scientifically different objects.