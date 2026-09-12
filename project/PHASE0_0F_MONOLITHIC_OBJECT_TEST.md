# Phase 0F — Monolithic Dependency Object Ablation

**Candidate:**

```math
\mathfrak d_e=(s,r,\rho,m,q,M,z,w,\delta,c,U,\mathcal H).
```

**Status:** TESTED AGAINST FROZEN `K1–K8` AND `D1–D4`  
**Interpretation:** results concern the dependency contract, not the frozen ontology.

---

## 1. Forward construction

Begin with

```math
A_0=(s,r).
```

This preserves only endpoint identity and direction:

```text
K1 PASS;
K2 PASS;
K3–K7 FAIL;
K8 only traceable at the receiver identity level, not causally established.
```

Add mechanism:

```math
A_1=(s,r,m).
```

`K3` improves, but the mechanism may still lack dimensional/interface typing, dynamics, timing and evidence.

Add exchanged quantity/interface semantics:

```math
A_2=(s,r,m,q).
```

This improves physical/informational/organizational type discrimination and allows dimensional consistency when `q` is typed.

Add dynamic/context information:

```math
A_3=(s,r,m,q,z,\delta,c,\mathcal H).
```

This can preserve `K4–K5`, including internal relation state, activation context, latency and history where needed.

Add evidence:

```math
A_4=(s,r,m,q,z,\delta,c,U,\mathcal H).
```

This preserves `K6` when `U` is structured rather than conflated with physical-state uncertainty.

At this point the remaining original fields are

```math
\{\rho,M,w\}.
```

Their necessity is tested by leave-one-out analysis rather than assumed.

---

## 2. Leave-one-out classification

| Field | 0F status | Mathematical reason | Loss if removed |
|---|---|---|---|
| `s` | **primitive** | ordered source is required for endpoint identity and direction | `K1,K2` fail |
| `r` | **primitive** | ordered receiver identifies affected subsystem and service trace | `K1,K2,K8` fail |
| `rho` | **derived/optional metadata** | with a frozen classification map, `rho=R_class(C,Sigma)` follows from typed endpoints and mechanism semantics | no unique `K1–K8` loss on D1–D4 |
| `m` | **primitive semantic content in Candidate A** | without mechanism, edge reduces to adjacency/correlation | `K3` fails and `K7` cannot be justified |
| `q` | **necessary typed content in Candidate A; absorbable elsewhere** | carrier/signal/authority type provides dimensional/interface semantics; can later be absorbed into typed ports | K3/K7 become ambiguous if `m` lacks a typed signature |
| `M` | **derived for actual dependency set** | for `e in E`, `M_e=1_{e in E}` | no loss for actual-edge object; may be useful in potential-edge supergraphs |
| `z` | **conditional primitive** | needed only when the relation has internal availability/state not determined by endpoint states/context | D2-like degraded information channel can lose K4 if no substitute state exists |
| `w` | **derived observable** | after mechanism and metric are declared, influence can be computed, e.g. `w=||D_xs Phi||`; no universal scalar definition exists | no core loss if formal mechanism retained |
| `delta` | **necessary timing information; not necessarily top-level** | D2 requires latency; may be a parameter of the causal operator rather than a separate field | `K5` fails if timing is otherwise absent |
| `c` | **necessary context/guard information; not necessarily top-level** | D3 requires context/authority/access activation semantics | `K4` fails if mechanism has no guard/context semantics |
| `U` | **primitive epistemic content** | evidence/provenance cannot be derived from physical state | `K6` fails |
| `H` | **conditional primitive** | required for genuinely non-Markovian/path-dependent dependencies; unnecessary for a Markov closure | K4/K5 can fail for memory-dependent relation classes |

---

## 3. Explicit derivations

### 3.1 Structural existence

For an actual edge set `E`,

```math
M_e=\mathbf 1_{\{e\in E\}}.
```

Hence `M_e` should not be duplicated inside every actual dependency unless the model deliberately represents potential/nonexistent edges.

### 3.2 Relation class

With typed interface/mechanism semantics,

```math
\rho_e
=
\mathcal R_{class}(s_e,r_e,m_e,q_e).
```

Thus `rho` is useful for retrieval/reporting but not a mathematically independent dependency primitive under the frozen classification map.

### 3.3 Influence strength

If the causal realization is differentiable,

```math
w_e(t)
=
\left\|D_{x_s}\Phi_e\right\|.
```

For non-smooth/hybrid relations, `w_e` requires another explicitly selected influence functional. Because its value depends on the chosen norm, state coordinates and influence definition, a generic scalar `w` cannot be treated as universally primitive.

### 3.4 Activation

If context is expressed by a guard,

```math
a_e(t)
=
\mathbf 1_{\{\gamma_e(Y,h,u,t)\ge0\}}.
```

The activation indicator is derived; the guard semantics are fundamental.

---

## 4. Case tests

### D1 — feeder -> FCS

Necessary content:

```text
s,r;
electrical-power mechanism/typed carrier;
operating-state/context dependence;
evidence/provenance;
formal mapping to charger model.
```

`rho`, `M`, and an independently stored generic `w` add no unique frozen capability.

### D2 — EV forecast -> controller

Necessary content:

```text
s,r;
information mechanism/type;
latency delta_I;
information-quality/availability state where not contained in endpoint state;
evidence that the controller consumes the forecast;
formal mapping to pi_P.
```

This is the strongest case for a conditional internal relation state and explicit timing.

### D3 — road authority -> crew access

Necessary content:

```text
s,r;
authority/access mechanism;
context/guard that changes the feasible route set;
decision/communication timing where relevant;
institutional provenance;
formal mapping to Gamma_R/restoration logic.
```

A generic scalar `w` is particularly weak here because organizational influence need not admit one natural dimensionless strength.

### D4 — EV charging -> feeder load

Necessary content:

```text
s,r;
typed electrical charging quantity;
mechanism entering feeder balance;
state-dependent charging behavior;
provenance/model evidence;
formal mapping to power equations.
```

---

## 5. Engineering-value ablation summary

Use binary change indicators only; no arbitrary magnitude is assigned.

| Component removed | Explanation `V_E` | Identification `V_I` | Prediction-readiness `V_P` | Decision semantics `V_D` | Core verdict |
|---|---:|---:|---:|---:|---|
| `s` | 1 | 1 | 1 | 1 | keep |
| `r` | 1 | 1 | 1 | 1 | keep |
| `rho` | 0 | 0 | 0 | 0 | derive/tag |
| `m` | 1 | 1 | 1 | 1 | keep semantic mechanism |
| `q` | 1 | 1 | 1 | 1 | keep typed carrier, but may be nested in interface |
| `M` | 0 | 0 | 0 | 0 | derive from edge-set membership |
| `z` | conditional | conditional | conditional | conditional | optional internal state |
| `w` | 0 if `Phi` retained | 0 | 0 if derived | 0 | derive application-specific influence metric |
| `delta` | 0/1 by relation | 1 when delayed | 1 when delayed | 1 when delayed | mechanism parameter |
| `c` | 1 for guarded relation | 1 | 1 | 1 | mechanism guard/context |
| `U` | 1 | 1 | 0/1 | 1 | keep separate epistemic object |
| `H` | conditional | conditional | conditional | conditional | optional memory/history extension |

`1` means removal causes a capability loss in at least one frozen dependency. `conditional` means the loss occurs only for a defined relation class.

---

## 6. Redundancy result

Three original fields are guaranteed non-primitive under the frozen derivations:

```math
\{\rho,M,w\}.
```

Therefore the conservative redundancy lower bound is

```math
R_{red}^{LB}
=
\frac{3}{12}
=
0.25.
```

This is a lower bound, not a claim that only three fields can be refactored. `q`, `delta`, `c`, `z` and `H` may remain necessary **information** while being absorbed into a formal mechanism/interface object rather than stored as separate top-level fields.

---

## 7. K7 problem in the raw tuple

The raw tuple contains `m`, but does not specify that `m` is an executable mathematical operator.

Therefore Candidate A alone does not guarantee

```math
m\longrightarrow \Phi_e\longrightarrow \Delta F_r.
```

It becomes sufficient for `K7` only if a fixed realization library/map is added.

Similarly, service consequence `K8` is not a top-level tuple field; it requires the system-level service map

```math
Q=G(Y).
```

This is not a defect by itself—system-level functions should not necessarily be duplicated on every relation—but it proves that the monolithic tuple is not a self-contained mathematical model.

---

## 8. Monolithic verdict

```text
Candidate A is REPRESENTATIONALLY SUFFICIENT ON D1–D4 only when supplemented by fixed realization and service maps.
Candidate A is NOT MINIMUM as declared.
Candidate A contains at least 25% guaranteed top-level redundancy under the frozen derivations.
```

The next test asks whether the layered candidate removes that redundancy without introducing unnecessary implementation layers.
