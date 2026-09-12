# Phase 0E — V1–V5 Encoding and Formal Metrics

**Status:** CONTROLLED CASE TEST RESULTS v1.0  
**Inputs:** frozen `F_1,...,F_5`, common physics/evidence fixture, `M_0`, `M_1`, and preregistered 0D metrics.  
**Rule:** decoding may use only the native grammar, previously frozen global rules, and the equal shared evidence ledger. No case-specific repair is permitted.

---

# 1. Metric definitions retained without modification

For case `V_k` with fact set `F_k`,

```math
L_{sem}(M,V_k)
=
1-\frac{|Rec_M(\mathcal F_k)|}{|\mathcal F_k|}.
```

For encoded representation object `r`,

```math
\kappa_M(r)=|Dec_M(r)|,
```

and

```math
E_{amb}(M,V_k)
=
\sum_{r\in Enc_M(\mathcal F_k)}
\log_2\!\left(\max(1,\kappa_M(r))\right).
```

`N_adhoc` counts only case-specific rules/extensions introduced after the frozen grammar. Globally frozen mappings/evidence lookup rules do not count as ad hoc.

The complexity vector remains

```math
C(M,V_k)=
\left(
N_{objects},
N_{relation\ types},
N_{required\ parameters},
N_{assumptions},
N_{adhoc},
N_{external\ formalisms}
\right).
```

No scalar weighted complexity index is introduced.

---

# 2. Decoding discipline

## 2.1 `M_0`

For `P/T` entities, the native layer label supplies domain/system identity directly.

For `I/O` entities, the native label supplies aspect class while domain affiliation is reconstructed from the frozen entity/actor/subsystem facts in the equal evidence ledger through the globally defined attribution rule `eta`.

This is **not** a case-specific repair because `eta` was defined before 0E and is available uniformly to every `I/O` entity.

Therefore the test does not equate "not encoded in the layer label" with "lost from the representation".

## 2.2 `M_1`

For single-domain entities in V1–V5, domain and aspect are directly encoded as `(alpha,a)`.

The unresolved genuinely-shared-entity problem identified in 0D is not triggered by the frozen V1–V5 fixture because no test requires one single entity to possess simultaneous native `P` and `T` domain membership.

It is therefore not legitimate to penalize `M_1` for that untested edge case in 0E v1.0.

---

# 3. V1 — Reciprocal physical EV charging coupling

## 3.1 Common facts

```math
|\mathcal F_1|=10.
```

All V1 endpoints are physical Power/Transportation entities.

### `M_0` encoding

```math
P_{feeder}\rightarrow T_{FCS},
```

```math
T_{EV\ arrival}\rightarrow P_{charging\ demand}.
```

The common relation payload contains mechanism/delay/state/history information. The shared physics contains charging aggregation, feeder balance and FCS queue/service dynamics.

### `M_1` encoding

```math
(P,Ph)_{feeder}\rightarrow(T,Ph)_{FCS},
```

```math
(T,Ph)_{EV\ arrival}\rightarrow(P,Ph)_{charging\ demand}.
```

No additional physical information is introduced.

## 3.2 Reconstruction result

For both models,

```math
Rec_M(\mathcal F_1)=\mathcal F_1.
```

Therefore

```math
L_{sem}(M_0,V_1)=L_{sem}(M_1,V_1)=0.
```

Every encoded V1 fact has one admissible reconstruction under the frozen ledger, hence

```math
E_{amb}(M_0,V_1)=E_{amb}(M_1,V_1)=0.
```

No case-specific rule is needed:

```math
N_{adhoc}(M_0,V_1)=N_{adhoc}(M_1,V_1)=0.
```

### Interpretation

The 0D type-system non-isomorphism has no engineering effect in V1 because the case uses only physical `P/T` endpoint types, which both ontologies distinguish natively.

---

# 4. V2 — Information-mediated coupling

## 4.1 Common facts

```math
|\mathcal F_2|=9.
```

### `M_0` encoding

```math
I_{EV\ forecast}\rightarrow I_{power\ controller}\rightarrow P_{setpoint}.
```

Native layer labels alone do not encode whether each `I` entity is transport- or power-affiliated. However, the equal evidence ledger contains the frozen facts

```text
EV forecast -> Transportation affiliation;
power controller -> Power affiliation.
```

The global attribution map `eta` therefore reconstructs

```math
I_{EV\ forecast}\rightsquigarrow(T,In),
```

```math
I_{power\ controller}\rightsquigarrow(P,In)
```

without adding any case-specific rule.

### `M_1` encoding

```math
(T,In)_{EV\ forecast}
\rightarrow
(P,In)_{power\ controller}
\rightarrow
(P,Ph)_{setpoint}.
```

The same mechanism, delay and control equations are used.

## 4.2 Reconstruction result

Because the shared ledger is part of the preregistered decoding information,

```math
Rec_{M_0}(\mathcal F_2)=Rec_{M_1}(\mathcal F_2)=\mathcal F_2.
```

Hence

```math
L_{sem}(M_0,V_2)=L_{sem}(M_1,V_2)=0.
```

and

```math
E_{amb}(M_0,V_2)=E_{amb}(M_1,V_2)=0.
```

with

```math
N_{adhoc}(M_0,V_2)=N_{adhoc}(M_1,V_2)=0.
```

### Interpretation

`M_1` makes the domain affiliation **native in the type coordinate**, whereas `M_0` requires a frozen auxiliary lookup. Under the equal-information protocol this is an explicitness difference, not semantic loss or ambiguity.

A different protocol that intentionally removed actor/subsystem evidence would produce a different question and is not allowed post hoc.

---

# 5. V3 — Organizational coupling

## 5.1 Common facts

```math
|\mathcal F_3|=9.
```

### `M_0` encoding

```math
O_{road\ authority}
\rightarrow
T_{access}
\rightarrow
O_{power\ crew}
\rightarrow
P_{restoration}.
```

The global `O` label does not itself distinguish transportation authority from power-utility crew, but those actor identities and affiliations are already frozen in the evidence ledger.

### `M_1` encoding

```math
(T,Or)_{road\ authority}
\rightarrow
(T,Ph)_{access}
\rightarrow
(P,Or)_{power\ crew}
\rightarrow
(P,Ph)_{restoration}.
```

## 5.2 Reconstruction result

The actor evidence makes each affiliation uniquely recoverable under `M_0` and native under `M_1`.

Therefore

```math
L_{sem}(M_0,V_3)=L_{sem}(M_1,V_3)=0,
```

```math
E_{amb}(M_0,V_3)=E_{amb}(M_1,V_3)=0,
```

and

```math
N_{adhoc}(M_0,V_3)=N_{adhoc}(M_1,V_3)=0.
```

### Interpretation

The test demonstrates a bookkeeping difference, not a demonstrated engineering-capability difference. Both representations preserve authority, access, crew mobilization, timing and restoration meaning under the controlled evidence budget.

---

# 6. V4 — Mediated `P->T->P` feedback

## 6.1 Common facts

```math
|\mathcal F_4|=10.
```

### `M_0` encoding

A representative typed path is

```math
P
\rightarrow
T
\rightarrow
O
\rightarrow
P.
```

The entity-level identities and relation payload distinguish transport degradation, crew organization and restoration.

### `M_1` encoding

```math
(P,Ph)
\rightarrow
(T,Ph)
\rightarrow
(P,Or)
\rightarrow
(P,Ph).
```

Additional intermediate `In/Or` states may appear only when already present in the common fact set.

## 6.2 Reconstruction result

Both models preserve the mediated path, causal ordering and distinction between common-cause exposure and induced propagation using the identical relation payload.

Thus

```math
L_{sem}(M_0,V_4)=L_{sem}(M_1,V_4)=0,
```

```math
E_{amb}(M_0,V_4)=E_{amb}(M_1,V_4)=0,
```

and

```math
N_{adhoc}(M_0,V_4)=N_{adhoc}(M_1,V_4)=0.
```

### Interpretation

The ability to represent mediated reciprocity comes from the directed relation/path semantics, not from the domain–aspect product alone. `M_0` does not require direct pairwise reciprocal edges and therefore does not fail V4.

---

# 7. V5 — Water extension

## 7.1 Common facts

```math
|\mathcal F_5|=10.
```

## 7.2 Conservative-extension test

### `M_0`

Extend

```math
\mathcal L_0=\{P,T,I,O\}
```

to

```math
\mathcal L_0'=\{P,T,W,I,O\}.
```

Define the inclusion

```math
\iota_0:\mathcal L_0\hookrightarrow\mathcal L_0'
```

by identity on all old symbols.

The relation payload remains unchanged and all old `P/T/I/O` interpretations remain unchanged. Therefore this is a **conservative signature extension** for the frozen V5 problem, not a redesign of the relation grammar.

### `M_1`

Extend

```math
\mathcal D=\{P,T\}
```

to

```math
\mathcal D'=\{P,T,W\},
```

while retaining

```math
\mathcal A=\{Ph,In,Or\}.
```

The inclusion is

```math
\iota_1:\mathcal D\times\mathcal A
\hookrightarrow
\mathcal D'\times\mathcal A.
```

Again, all old meanings and the relation payload remain unchanged.

## 7.3 Reconstruction result

Both conservative extensions encode all ten frozen Water facts.

Therefore

```math
L_{sem}(M_0,V_5)=L_{sem}(M_1,V_5)=0,
```

```math
E_{amb}(M_0,V_5)=E_{amb}(M_1,V_5)=0,
```

and, because V5 extension behavior was preregistered before the test,

```math
N_{adhoc}(M_0,V_5)=N_{adhoc}(M_1,V_5)=0.
```

### Structural difference

The extension burdens are different but not ordered by the frozen metrics:

```text
M_0: top-level type classes 4 -> 5; entity type coordinate remains one-dimensional.
M_1: domain classes 2 -> 3; product types 6 -> 9; entity type coordinates remain two-dimensional.
```

`M_1` generates domain-aspect combinations systematically; `M_0` remains more compact but keeps `I/O` global. Neither fact alone establishes superior engineering capability.

---

# 8. Complexity calculation

Let `n_k` be the number of engineering entity instances required by the frozen case, `p_k` the common number of physical/relation parameter classes, and `a_k` the common number of engineering assumptions.

Because 0E changes only endpoint typing,

```math
C(M_0,V_k)
=
C(M_1,V_k)
=
(n_k,1,p_k,a_k,0,0)
```

for the preregistered complexity vector components

```math
(N_{objects},N_{relation\ types},N_{required\ parameters},N_{assumptions},N_{adhoc},N_{external\ formalisms}).
```

This equality follows from the experimental control: both models use the same entity universe, one common relation-payload form, identical physics/parameters, identical assumptions, no post-hoc exceptions and no additional external formalism.

The native ontology signatures remain descriptively different:

```text
M_0: 4 native classes and 1 type coordinate in P–T;
M_1: 6 native product types and 2 type coordinates in P–T.
```

These 0D structural signatures are reported but are not inserted into the frozen complexity vector after the fact.

---

# 9. Aggregate formal result across V1–V5

For every frozen case,

```math
L_{sem}(M_0,V_k)=L_{sem}(M_1,V_k)=0,
\qquad k=1,\ldots,5,
```

and

```math
E_{amb}(M_0,V_k)=E_{amb}(M_1,V_k)=0,
```

with

```math
N_{adhoc}(M_0,V_k)=N_{adhoc}(M_1,V_k)=0.
```

Thus the formal non-isomorphism established in 0D does **not**, under the equal-information V1–V5 fixture, produce measurable semantic loss, representation ambiguity or case-specific repair.

This is a falsification-relevant result: the domain × aspect ontology has not yet demonstrated a necessary engineering representation capability unavailable to the frozen ontology.

---

# 10. Validity boundary

The zero-loss result depends explicitly on the frozen equal-information condition. It does not imply that `M_0` and `M_1` are universally equivalent, nor that domain-indexed information/organization is never useful.

It establishes only:

> For the declared V1–V5 mechanism fixtures, with identical actor/subsystem/evidence context available to both representations, the 0D native type-system difference does not cause semantic information loss, ambiguity or ad hoc repair under the preregistered metrics.