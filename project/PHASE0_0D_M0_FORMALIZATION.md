# Phase 0D — Formalization of Baseline `M_0`

**Status:** CONTROLLED BASELINE FORMALIZATION v1.0  
**Model:** current frozen thesis ontology.  
**Rule:** this file does not improve `M_0` beyond what the current canonical thesis already allows.

---

## 1. Ontology

The baseline is

```math
M_0:\qquad \mathcal S_0=\{P,T,I,O\},
```

with layer/index set

```math
\mathcal L_0=\{P,T,I,O\}.
```

Interpretation:

```text
P = physical Power infrastructure system;
T = physical Transportation infrastructure system;
I = informational layer;
O = organizational layer.
```

The ontology deliberately mixes two category types already frozen in the thesis:

```text
P,T = constituent physical infrastructure systems;
I,O = cross-system functional layers.
```

This mixture is not treated as an error a priori; 0D tests whether it causes actual information loss or ambiguity.

---

## 2. Entity typing

Each entity is represented as

```math
v_i^{(0)}=(id_i,\ell_i),
\qquad \ell_i\in\mathcal L_0.
```

The native type projection is

```math
\lambda_0:\mathcal V^*\rightarrow\mathcal L_0.
```

Examples:

```math
\lambda_0(e_{feeder})=P,
```

```math
\lambda_0(e_{road})=T,
```

```math
\lambda_0(e_{EV\ forecast})=I,
```

```math
\lambda_0(e_{road\ authority})=O.
```

The layer label itself does **not** distinguish whether an informational entity is primarily associated with Power or Transportation, nor whether an organizational entity belongs to a power utility, road authority, or shared emergency organization. Such distinctions can still exist in the entity identifier, actor identity, subsystem membership, or relation context because the frozen thesis already permits detailed decompositions of `I` and `O`.

For 0D, those additional factual distinctions are counted as **auxiliary semantic context**, not as native information in `lambda_0`.

---

## 3. State representation

The baseline state remains exactly the frozen thesis state:

```math
Y_0(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\z_I(t)\\z_O(t)
\end{bmatrix}.
```

No state variable is added or removed for the comparison.

The physical state is

```math
X_0(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)
\end{bmatrix}.
```

---

## 4. Relation representation

The canonical Stage-2 object is retained:

```math
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,
E_j^\beta,
M_{ij},
w_{ij},
\delta_{ij},
\tau_{ij},
a_{ij},
m,
\mathcal H_t
\right),
```

with

```math
\alpha,\beta\in\{P,T,I,O\}.
```

For the controlled 0D comparison, its endpoint labels are generated through `lambda_0`, while the remaining relation payload is identical to the common payload `R_e*` defined in the common-reality specification.

Thus a baseline relation can be written compactly as

```math
r_e^{(0)}=
\left(
(id_s,\lambda_0(s)),
(id_r,\lambda_0(r)),
\mathcal R_e^*
\right).
```

---

## 5. Encoding the frozen verification cases

### V1 — physical reciprocal EV charging relation

Power-to-transport:

```math
(P_{feeder})\rightarrow(T_{FCS/mobility}).
```

Transport-to-power:

```math
(T_{EV\ arrival})\rightarrow(P_{charging\ demand}).
```

This is natively distinguishable at the layer level because endpoints are typed `P` and `T`.

### V2 — information-mediated relation

Native layer form:

```math
I_{EV\ forecast}\rightarrow I_{power\ controller}\rightarrow P_{setpoint}.
```

The fact that the first informational entity is transport-origin information and the second is power-control information is not encoded by the global `I` layer label alone. It must be recovered from entity identity/subsystem semantics or relation context.

### V3 — organizational relation

Native layer form:

```math
O_{road\ authority}\rightarrow T_{access}\rightarrow O_{power\ crew}\rightarrow P_{restoration}.
```

The global `O` label distinguishes organization from physical systems but does not itself distinguish `transport organization` from `power organization`.

### V4 — mediated system feedback

The baseline can encode a path

```math
P\rightarrow T\rightarrow O\rightarrow P
```

or a more detailed component path using canonical relation objects. Direct reciprocal edges between identical component pairs are not required by the frozen Stage-2 object, so mediated feedback is formally possible.

### V5 — third-domain extension

The current ontology would require extending the set to include the new physical infrastructure system:

```math
\mathcal S_0' = \{P,T,W,I,O\}.
```

The relation payload need not change, but the canonical layer/system set changes by adding `W`.

This is not automatically a failure: 0E must determine whether such set extension counts as ordinary composability or ontology redesign under frozen `R12`.

---

## 6. Native strengths of `M_0`

The baseline explicitly preserves:

```text
- separate P and T physical-system identity;
- global informational state and functions;
- global organizational state and functions;
- cross-layer directed relations;
- the frozen thesis state Y(t);
- the existing seven-stage interpretation.
```

These are baseline capabilities and must not be understated to favor `M_1`.

---

## 7. Native compression in `M_0`

The type map

```math
\lambda_0(e)\in\{P,T,I,O\}
```

compresses domain affiliation for informational and organizational entities:

```math
(P,In)\mapsto I,
\qquad
(T,In)\mapsto I,
```

and

```math
(P,Or)\mapsto O,
\qquad
(T,Or)\mapsto O.
```

Whether this compression causes **material** semantic loss is not decided here. It becomes a mapping/information-loss question and then an engineering case question in 0E.

---

## 8. Auxiliary semantic context allowed under `M_0`

Because the frozen thesis already decomposes `I` and `O` into functions and actors, the following are permitted without changing the ontology:

```text
- entity identifiers that name the owning operator/domain;
- subsystem/actor metadata already part of the frozen decomposition;
- relation mechanisms already present in the canonical Stage-2 object;
- cross-sector organizational actor identities;
- evidence/provenance records from the common evidence budget.
```

However, these are not counted as additional native layer coordinates. If domain affiliation of an `I` or `O` entity can be recovered only from such context, the recovery rule must be recorded explicitly in the mapping audit.

---

## 9. Complexity signature

For `M_0`, 0D records the structural complexity vector rather than a scalar score:

```math
C(M_0)=
\left(
N_{layer\ classes}=4,
N_{entity\ coordinates}=1,
N_{relation\ payload\ forms}=1,
N_{auxiliary\ domain\ attribution\ rules},
N_{ad\ hoc\ exceptions},
N_{external\ formalisms}
\right).
```

The last three entries are not assigned numerical values until the common cases are encoded under the comparison protocol.

---

## 10. Validity statement

`M_0` is the current canonical thesis ontology and remains authoritative during 0D. This formalization is a controlled baseline, not a critique and not a decision to retain it.
