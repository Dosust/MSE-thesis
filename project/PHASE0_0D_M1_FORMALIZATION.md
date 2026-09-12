# Phase 0D — Formalization of Candidate `M_1`

**Status:** CONTROLLED CANDIDATE FORMALIZATION v1.0  
**Model:** domain × aspect ontology proposed in Phase 0.  
**Rule:** `M_1` receives no additional evidence, state, physics, relation payload, or service variable unavailable to `M_0`.

---

## 1. Ontology

The candidate representation is

```math
M_1:\qquad \mathcal S_1=\mathcal D\times\mathcal A,
```

with

```math
\mathcal D=\{P,T\},
\qquad
\mathcal A=\{Ph,In,Or\}.
```

Therefore the available native type coordinates are

```math
\mathcal L_1=
\{
(P,Ph),(P,In),(P,Or),
(T,Ph),(T,In),(T,Or)
\}.
```

Interpretation:

```text
first coordinate  = infrastructure domain identity;
second coordinate = physical / informational / organizational aspect.
```

---

## 2. Entity typing

Each entity is represented as

```math
v_i^{(1)}=(id_i,\alpha_i,a_i),
```

with

```math
\alpha_i\in\mathcal D,
\qquad
a_i\in\mathcal A.
```

The native type map is

```math
\lambda_1:\mathcal V^*\rightarrow\mathcal D\times\mathcal A.
```

Examples:

```math
\lambda_1(e_{feeder})=(P,Ph),
```

```math
\lambda_1(e_{EV\ forecast})=(T,In),
```

```math
\lambda_1(e_{power\ controller})=(P,In),
```

```math
\lambda_1(e_{road\ authority})=(T,Or),
```

```math
\lambda_1(e_{power\ crew})=(P,Or).
```

This type system makes infrastructure affiliation and system aspect separate coordinates.

---

## 3. State representation

`M_1` may regroup the common state by domain/aspect, but it may not change its content.

One admissible bookkeeping representation is

```math
Y_1(t)=
\left[
Y_P^{Ph},
Y_P^{In},
Y_P^{Or},
Y_T^{Ph},
Y_T^{In},
Y_T^{Or}
\right]^\top,
```

provided there exists a pure re-indexing map

```math
\rho_Y:Y^*(t)\leftrightarrow Y_1(t)
```

that introduces no new state variable and removes none.

The physical subsystem states remain

```math
Y_P^{Ph}=x_P,
\qquad
Y_T^{Ph}=x_T.
```

Informational and organizational variables from `z_I,z_O` must be allocated using only facts already contained in the common evidence budget.

---

## 4. Relation representation

0D keeps the relation payload identical to `M_0`.

For relation `e`, define

```math
r_e^{(1)}=
\left(
(id_s,\lambda_1(s)),
(id_r,\lambda_1(r)),
\mathcal R_e^*
\right),
```

where

```math
\mathcal R_e^*=
(M_e,w_e,\delta_e,\tau_e,a_e,m_e,\mathcal H_{e,t})
```

is exactly the common Stage-2 payload.

Therefore the experiment changes endpoint typing only.

---

## 5. Encoding the frozen verification cases

### V1 — reciprocal physical EV charging relation

Power-to-transport:

```math
(P,Ph)_{feeder}\rightarrow(T,Ph)_{FCS/mobility}.
```

Transport-to-power:

```math
(T,Ph)_{EV\ arrival}\rightarrow(P,Ph)_{charging\ demand}.
```

### V2 — information-mediated relation

```math
(T,In)_{EV\ forecast}
\rightarrow
(P,In)_{power\ controller}
\rightarrow
(P,Ph)_{setpoint}.
```

The transport origin of the forecast and power affiliation of the controller are represented natively in the type coordinates.

### V3 — organizational relation

```math
(T,Or)_{road\ authority}
\rightarrow
(T,Ph)_{access}
\rightarrow
(P,Or)_{power\ crew}
\rightarrow
(P,Ph)_{restoration}.
```

### V4 — mediated feedback

A component path may be encoded as

```math
(P,Ph)
\rightarrow
(T,Ph)
\rightarrow
(P,Or)
\rightarrow
(P,Ph),
```

or with informational/organizational intermediate aspects where supported by the common evidence set.

### V5 — third-domain extension

The domain set extends as

```math
\mathcal D'=\{P,T,W\},
```

while

```math
\mathcal A=\{Ph,In,Or\}
```

is unchanged.

The new native types are

```math
(W,Ph),(W,In),(W,Or),
```

and the same relation payload is retained.

---

## 6. Native strengths of `M_1`

The candidate explicitly separates:

```text
- domain identity;
- physical/informational/organizational aspect;
- power information from transport information;
- power organization from transport organization;
- extensible domain membership from reusable aspect classes.
```

These are formal capabilities, not yet evidence of engineering superiority.

---

## 7. Important unresolved edge case — shared/cross-domain entities

The declared candidate uses a single domain coordinate

```math
\alpha_i\in\{P,T\}.
```

Therefore a genuinely shared entity such as a cross-sector emergency coordination body, shared data exchange, or joint operating platform may not have a unique native domain label.

Three possible treatments exist:

```text
1. choose P or T;
2. duplicate the entity into domain-specific views;
3. extend the domain coordinate to allow a shared/multi-domain value.
```

Options 2–3 change the representation beyond the currently declared `M_1` and are **not automatically allowed** in 0D.

This edge case is retained as a possible countervailing weakness of `M_1` and must be tested rather than repaired in advance.

---

## 8. No hidden relation advantage

`M_1` is prohibited from attaching richer relation semantics merely because its endpoint types are richer.

In particular, it does not receive extra:

```text
- evidence confidence;
- causal mechanism fields;
- state variables;
- delays;
- service mappings;
- uncertainty terms;
- execution metadata.
```

Those remain identical to `M_0` in 0D.

---

## 9. Complexity signature

The structural complexity vector is

```math
C(M_1)=
\left(
N_{domain\ classes}=2,
N_{aspect\ classes}=3,
N_{native\ type\ combinations}=6,
N_{entity\ coordinates}=2,
N_{relation\ payload\ forms}=1,
N_{shared\ entity\ exceptions},
N_{external\ formalisms}
\right).
```

No scalar penalty is assigned in 0D.

---

## 10. Validity statement

`M_1` is a candidate representation only. This file establishes its native grammar sufficiently for controlled mapping and testing. It does not establish that `M_1` is more correct, more useful, more extensible in practice, or suitable to replace the canonical thesis ontology.
