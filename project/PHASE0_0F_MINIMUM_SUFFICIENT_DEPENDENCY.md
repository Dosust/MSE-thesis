# Phase 0F — Minimum Sufficient Dependency Representation

**Status:** DERIVED 0F RESULT — NOT YET CANONICAL  
**Scope:** minimum sufficient representation relative to frozen capabilities `K1–K8`, dependencies `D1–D4`, fixed ontology `M_0`, and globally frozen realization/service maps.  
**Result class:** `[D/P]` mathematically derived candidate requiring later empirical validation.

---

## 1. Result

The 0F ablation supports a refined three-part dependency contract:

```math
\boxed{
\mathfrak d_e^{min}
=
(\mathcal C_e,\Sigma_e,\Pi_e)
}
```

with globally defined maps

```math
\mathcal X:\Sigma_e\mapsto\Xi_e
```

and

```math
Q=G(Y).
```

This is a **hybrid minimum**: it uses the layered separation discovered in 0C–0F, while absorbing necessary information from the original monolithic tuple into typed subobjects instead of retaining every field at the top level.

---

# 2. Primitive 1 — compositional/interface object

Define

```math
\boxed{
\mathcal C_e
=
(s_e,p_e^s,r_e,p_e^r,\chi_e)
}
```

where:

```text
s_e   = typed source entity;
p_e^s = source interaction point/port;
r_e   = typed receiver entity;
p_e^r = receiver interaction point/port;
chi_e = exchanged carrier/signal/resource/authority type.
```

The ordered pair

```math
(s_e,r_e)
```

provides direction.

`chi_e` is deliberately broader than a physical scalar quantity. It may denote:

```text
electrical power;
flow/capacity;
information/forecast;
control command;
authority/access permission;
resource/logistics constraint.
```

This avoids forcing organizational and informational dependencies into artificial physical-flow units.

### Capabilities carried

```text
K1 source/receiver;
K2 direction;
part of K3 through typed interface semantics;
receiver trace needed for K8.
```

---

# 3. Primitive 2 — causal/domain semantic object

Define

```math
\boxed{
\Sigma_e
=
(\Phi_e,\gamma_e,\theta_e,\zeta_e)
}
```

where:

```text
Phi_e   = causal coupling/transition operator;
gamma_e = activation/context guard;
theta_e = identified/calibrated mechanism parameters;
zeta_e  = optional internal dependency state/memory.
```

`zeta_e` may be empty:

```math
\zeta_e=\varnothing
```

for a dependency whose behavior is fully determined by endpoint/system states and current context.

---

## 3.1 Continuous realization

For a continuous receiving subsystem:

```math
\dot x_r(t)
=
F_r(x_r,u_r,h_r;\vartheta_r)
+
\gamma_e(t)
\Phi_e\!\left(
x_s^{[t-\bar\delta_e,t]},
x_r(t),
zeta_e(t),
u(t);
\theta_e
\right).
```

The domain-specific law `F_r` remains intact.

Thus:

```math
F_P\neq F_T
```

is preserved.

The dependency supplies a coupling contribution; it does not replace the receiving physics.

---

## 3.2 Hybrid/discrete realization

For logical, organizational, protection, switching or other event-driven relations:

```math
x_r^+
=
\Psi_e(x_s,x_r,\zeta_e,\nu;\theta_e)
```

when

```math
\gamma_e(Y,h,u,t)=1.
```

This is essential for dependencies such as road-access authority, where a continuous scalar coupling coefficient may be physically meaningless.

---

## 3.3 Internal dependency state

When a relation itself has state independent of the source/receiver states, use

```math
\dot\zeta_e
=
g_e(\zeta_e,Y,h,u;\vartheta_e).
```

Examples may include:

```text
communication-channel availability;
latent information freshness/quality;
contract/authorization state;
progressive interface degradation;
non-Markovian memory compressed into a state realization.
```

If no such independent state exists, `zeta_e` is omitted.

---

## 3.4 Delay and history

Delay is represented as a mechanism parameter and/or operator-domain property:

```math
\delta_e\in\theta_e
```

or

```math
x_s^{[t-\bar\delta_e,t]}.
```

Therefore delay/history information remains available without remaining a mandatory top-level field.

---

# 4. Primitive 3 — epistemic/provenance object

Define

```math
\boxed{
\Pi_e
=
(\mathcal P_e,V_e,\mathcal U_e)
}
```

where:

```text
P_e = provenance/source chain;
V_e = verification/validation/evidence status;
U_e = epistemic and parameter-uncertainty description.
```

Example status classes may include:

```text
EVIDENCE_SUPPORTED;
HYPOTHESIZED;
INFERRED_PENDING_VERIFICATION;
REJECTED;
UNKNOWN/UNOBSERVED.
```

This object must remain conceptually distinct from `zeta_e` or any physical failure probability.

W3C PROV-O provides an established precedent for qualified influence relations carrying provenance details; Phase 0 does not claim relation-level provenance as a new concept.

---

# 5. Executable realization is a map, not a physical primitive

Define the globally governed realization operator

```math
\boxed{
\mathcal X:\Sigma_e\mapsto\Xi_e
}
```

where `Xi_e` is an implementation such as:

```text
native equation/DAE;
hybrid transition;
optimization constraint;
FMI model-variable dependency/interface;
HELICS publication/subscription;
validated simulation function.
```

If `Sigma_e` is itself directly executable, `X` may be the identity.

FMI demonstrates that executable model structure/dependencies can be standardized separately from the real-world evidence that a dependency exists. Therefore `Xi_e` is retained as implementation metadata/reference, not an irreducible physical dependency property.

---

# 6. Service consequence is a system-level map

Keep the thesis service functional outside each edge:

```math
\boxed{
Q(t)=G(Y(t))
}
```

Then an individual dependency participates in the chain

```math
\boxed{
\Delta\mathfrak d_e
\rightarrow
\Delta\dot X_r
\rightarrow
\Delta X
\rightarrow
\Delta Q.
}
```

One possible controlled comparison is

```math
\Delta Q_e(t)
=
G(Y_e(t))-G(Y_{-e}(t)),
```

where `Y_e` and `Y_{-e}` are otherwise identical trajectories with the dependency enabled/disabled or perturbed under a declared intervention.

This avoids storing duplicate service semantics on every relation.

---

# 7. Mapping of original tuple fields into the minimum contract

| Original field | 0F disposition | Minimum representation |
|---|---|---|
| `s` | retain | `C_e` |
| `r` | retain | `C_e` |
| `rho` | derive/report | `R_class(C_e,Sigma_e)` |
| `m` | retain but formalize | replaced by causal operator semantics in `Sigma_e` |
| `q` | retain as typed interface/carrier | `chi_e` and typed ports in `C_e` |
| `M` | derive | edge-set/potential-edge membership outside core |
| `z` | conditional | optional internal state `zeta_e` in `Sigma_e` |
| `w` | derive | influence functional of `Phi_e` under declared metric |
| `delta` | retain information, absorb | parameter/domain semantics in `Sigma_e` |
| `c` | retain information, absorb | guard `gamma_e` in `Sigma_e` |
| `U` | retain and structure | `Pi_e` |
| `H` | conditional, absorb | history-domain or state realization in `Sigma_e` |

---

# 8. Derived quantities

## 8.1 Relation class

```math
\rho_e
=
\mathcal R_{class}(\mathcal C_e,\Sigma_e).
```

This is useful for literature extraction, indexing and reporting but is not a primitive if the full mechanism semantics are already known.

## 8.2 Structural existence

For actual relation set `E`,

```math
M_e=\mathbf 1_{\{e\in E\}}.
```

For candidate/potential dependencies, define a separate admissibility universe rather than overloading the physical dependency object.

## 8.3 Activation

```math
 a_e(t)
=
\mathbf 1_{\{\gamma_e(Y,h,u,t)=1\}}.
```

## 8.4 Influence strength

When differentiable:

```math
w_e(t;\|\cdot\|)
=
\left\|D_{x_s}\Phi_e\right\|.
```

Because `w_e` depends on coordinate scaling, operating point and chosen norm, it must always report its definition. For non-smooth/hybrid mechanisms, use another explicitly defined functional rather than forcing this derivative.

---

# 9. Minimum-sufficiency proof relative to K1–K8

Let

```math
R^*=(\mathcal C_e,\Sigma_e,\Pi_e)
```

with global maps `X` and `G` fixed.

### Remove `C_e`

Then source/receiver/direction cannot be uniquely recovered.

```math
K1,K2\text{ fail.}
```

Receiver/service trace for `K8` also fails.

### Remove `Sigma_e`

Then the representation has typed endpoints and evidence but no causal mechanism, state/time semantics or justified executable mapping.

```math
K3,K4,K5,K7\text{ fail.}
```

### Remove `Pi_e`

Then physical/executable behavior may remain but evidence status is lost.

```math
K6\text{ fails.}
```

### No fourth per-edge primitive required under the frozen global maps

`K7` is recovered through

```math
\Xi_e=\mathcal X(\Sigma_e),
```

and `K8` through

```math
Q=G(Y).
```

Therefore every retained top-level component is necessary and all frozen capabilities are preserved.

Within the declared test domain:

```math
\boxed{
L_{sem}(R^*,D_i)=0,
\qquad
E_{amb}(R^*,D_i)=0,
\qquad i=1,\ldots,4.
}
```

---

# 10. Case realization summary

| Dependency | `C_e` | `Sigma_e` | `Pi_e` | Service trace |
|---|---|---|---|---|
| D1 feeder -> FCS | electrical-power ports | charger availability/service coupling | standard/model/data evidence | `Q_mobility` |
| D2 forecast -> controller | typed data ports | delayed information-to-control law | data/controller-use provenance | `Q_electricity`, charging service |
| D3 authority -> crew access | authority/access interaction | guard + feasible-route/restoration logic | rule/authority/operational evidence | restoration -> `Q_electricity` |
| D4 charging -> feeder load | electrical-demand ports | charging aggregation -> feeder balance | charging/model/data provenance | `Q_electricity`, potentially `Q_mobility` |

---

# 11. Result category

The original tuple is not minimum.

The four-layer object is sufficient but stores `Xi` at a level that can be generated/referenced globally.

Therefore 0F yields:

```math
\boxed{
\text{HYBRID MINIMUM OBJECT REQUIRED}
}
```

with the candidate minimum

```math
\boxed{
\mathfrak d_e^{min}
=(\mathcal C_e,\Sigma_e,\Pi_e).
}
```

---

## 12. Scientific boundary

This is a **relative minimality theorem for the frozen Phase-0 test fixture**, not a universal theorem over every infrastructure dependency conceivable.

Empirical work must still test whether the proposed `Phi`, guards, parameters and evidence states are identifiable and predictive in a calibrated Power–Transportation case study.
