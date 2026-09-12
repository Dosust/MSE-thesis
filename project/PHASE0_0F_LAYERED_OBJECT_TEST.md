# Phase 0F — Layered Dependency Object Ablation

**Candidate:**

```math
\mathfrak D_e=(\mathcal C_e,\Sigma_e,\Pi_e,\Xi_e).
```

**Status:** TESTED AGAINST FROZEN `K1–K8` AND `D1–D4`.

---

## 1. Layer semantics under test

### `C_e` — compositional/interface skeleton

Candidate content:

```math
\mathcal C_e=(s_e,p_e^s,r_e,p_e^r,\chi_e),
```

where `p_e^s,p_e^r` are typed source/receiver ports or interaction points and `chi_e` is the typed carrier/signal/authority quantity.

This layer carries endpoint identity, direction and interface typing.

### `Sigma_e` — causal/domain semantics

Candidate content:

```math
\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\xi_e),
```

where:

```text
Phi_e   = causal coupling/transition operator;
gamma_e = activation/context guard;
theta_e = mechanism parameters, including delay where relevant;
xi_e    = optional internal relation state/memory.
```

A generic continuous realization is

```math
\Delta \dot x_r(t)
=
\Phi_e\!\left(
x_s^{[t-\bar\delta,t]},
x_r(t),
u(t),h(t),\xi_e(t);
\theta_e
\right).
```

For a discrete/hybrid relation, replace this by an explicitly typed transition operator.

### `Pi_e` — provenance/evidence/epistemic qualification

Candidate content:

```math
\Pi_e=(P_e,V_e,U_e),
```

where:

```text
P_e = provenance/source record;
V_e = validation/status class;
U_e = epistemic/parameter uncertainty description.
```

This is intentionally separate from physical relation state.

### `Xi_e` — executable realization

Candidate meaning:

```math
\Xi_e
=
\text{equation/model-interface/software realization of }\Sigma_e.
```

Examples include native equations, hybrid transition logic, FMI variables/model structure, HELICS publications/subscriptions, or another validated implementation.

---

## 2. Leave-one-layer-out tests

### Remove `C_e`

Without `C_e`, the model loses typed source/receiver/interface structure.

```text
K1 FAIL;
K2 FAIL;
K3 becomes ungrounded because the mechanism has no typed participants;
K8 loses receiver/service trace.
```

Therefore:

```math
\mathcal C_e\text{ is primitive.}
```

### Remove `Sigma_e`

Without `Sigma_e`, the dependency reduces to a typed connection plus evidence/implementation references but loses the actual engineering mechanism.

```text
K3 FAIL;
K4 FAIL;
K5 FAIL;
K7 cannot be scientifically justified even if software wiring exists.
```

Therefore:

```math
\Sigma_e\text{ is primitive.}
```

### Remove `Pi_e`

The physical/executable relation may still run, but the representation can no longer distinguish:

```text
validated relation;
hypothesized relation;
inferred relation;
uncertain parameterization;
unsupported relation.
```

Hence:

```text
K6 FAIL.
```

Therefore, under the evidence-aware thesis objective:

```math
\Pi_e\text{ is primitive epistemic content.}
```

### Remove `Xi_e`

Two cases must be distinguished.

#### Case A — `Sigma_e` is already a formal mathematical operator and a fixed global realization map exists

```math
\mathcal X:\Sigma_e\mapsto\Xi_e.
```

Then `Xi_e` is uniquely generated/referenced and does not need to be stored as primitive relation semantics.

`K7` remains satisfied.

#### Case B — no fixed realization map exists

Then `Xi_e` is needed to identify how the semantic mechanism is executed, and `K7` becomes ambiguous.

The minimum-contract test is performed under the globally frozen realization-map rule from the 0F protocol. Therefore:

```math
\Xi_e\text{ is not a primitive dependency property in v1.0.}
```

It remains important deployment/implementation metadata.

---

## 3. Service consequence test

The declared layered object has no separate service layer.

This is scientifically acceptable only if the thesis preserves the system-level service functional

```math
Q(t)=G(Y(t)).
```

Then the dependency consequence is computed through

```math
\Delta \dot x_r
\xrightarrow{F_r}
\Delta X
\xrightarrow{G}
\Delta Q.
```

Thus `K8` is a system-level trace, not a quantity that must be duplicated in every edge.

If `G` is unavailable, neither the monolithic nor layered dependency object alone can establish engineering service consequence.

---

## 4. D1–D4 realizations

### D1 — feeder -> FCS

```math
\mathcal C_1
=(P_{feeder},p_P,T_{FCS},p_T,\text{electrical power}).
```

```math
\Sigma_1:
P_{avail},V,SOC,\ldots
\mapsto
\Delta \mu_{FCS}.
```

`Pi_1` records evidence/model validation; `Xi_1` may reference the charger/network simulation implementation.

### D2 — EV forecast -> controller

```math
\mathcal C_2
=(T_{forecast},p_{data},P_{controller},p_{in},\text{forecast signal}).
```

```math
\Phi_2:
\widehat d_{EV}(t-\delta_I),q_I,x_P
\mapsto
\Delta u_P.
```

Delay belongs naturally to `theta_2`; information quality can be endpoint state or optional relation state `xi_2` depending on model boundary.

### D3 — road authority -> crew access

```math
\mathcal C_3
=(T_{authority},p_{authority},P_{crew},p_{access},\text{access permission/constraint}).
```

```math
\Phi_3:
(x_T,a_R)
\mapsto
\Delta\mathcal R_T^{feas}
\mapsto
\Delta T_{crew}.
```

This demonstrates that `Sigma` need not force every relation into a scalar physical-flow equation; it may encode a hybrid/logical/optimization mechanism.

### D4 — EV charging -> feeder load

```math
\mathcal C_4
=(T_{charging},p_{electric},P_{feeder},p_{load},\text{electrical power}).
```

```math
\Phi_4:
\{\chi_n,p_n\}_{n\in\mathcal N_{EV}}
\mapsto
\Delta P_L.
```

---

## 5. Separation-of-concerns result

The layered architecture enforces three scientifically important separations:

```math
\text{who/where connected}
\neq
\text{what causal mechanism}
\neq
\text{why we believe it}.
```

Formally:

```math
\mathcal C_e\neq\Sigma_e\neq\Pi_e.
```

This is consistent with the 0C finding that semantic/model relations, executable couplings and real-world dependencies must not be conflated.

---

## 6. Layer-ablation result

| Layer | Status | Capabilities uniquely protected |
|---|---|---|
| `C_e` | **primitive** | K1, K2 and receiver trace for K8 |
| `Sigma_e` | **primitive** | K3, K4, K5 and semantic basis for K7 |
| `Pi_e` | **primitive epistemic** | K6 |
| `Xi_e` | **derived/implementation layer under fixed X-map** | K7 execution reference; not primitive if generated/referenced globally |

Therefore the four-layer object is **sufficient but not minimum** under the frozen realization-map assumption.

---

## 7. Ambiguity and semantic-loss result

With `C`, `Sigma`, `Pi` retained and fixed global realization/service maps:

```math
L_{sem}=0
```

and

```math
E_{amb}=0
```

for frozen dependencies D1–D4.

Removing any of `C`, `Sigma`, or `Pi` causes at least one frozen capability failure.

Removing stored `Xi` does not cause loss when

```math
\Xi_e=\mathcal X(\Sigma_e)
```

is fixed and unique.

---

## 8. Layered verdict

```text
Candidate B is SUFFICIENT on D1–D4.
Candidate B is NOT MINIMUM as declared because Xi is an implementation realization rather than an irreducible dependency property under the frozen global realization map.
```

The next synthesis must determine whether a three-part core `(C,Sigma,Pi)` plus global realization/service maps is the minimum sufficient contract and how the original tuple fields map into it.
