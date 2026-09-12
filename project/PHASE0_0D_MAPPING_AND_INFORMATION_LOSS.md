# Phase 0D — Mapping and Information-Loss Analysis

**Status:** FORMAL MAPPING SPECIFICATION v1.0  
**Purpose:** determine whether `M_0` and `M_1` are information-preserving translations of one another under the common reality and evidence budget.  
**Decision boundary:** this file may identify formal non-equivalence; it may not declare engineering superiority.

---

## 1. Native type spaces

For the baseline:

```math
\mathcal L_0=\{P,T,I,O\}.
```

For the candidate:

```math
\mathcal L_1=
\{
(P,Ph),(P,In),(P,Or),
(T,Ph),(T,In),(T,Or)
\}.
```

The mapping problem is therefore between a four-class mixed ontology and a six-class product ontology.

---

## 2. Forgetful map from `M_1` to `M_0`

Define

```math
\phi_{10}:\mathcal L_1\rightarrow\mathcal L_0
```

by

```math
\phi_{10}(P,Ph)=P,
```

```math
\phi_{10}(T,Ph)=T,
```

```math
\phi_{10}(P,In)=\phi_{10}(T,In)=I,
```

```math
\phi_{10}(P,Or)=\phi_{10}(T,Or)=O.
```

This map is surjective onto the used type classes but not injective.

Specifically,

```math
(P,In)\neq(T,In)
\quad\text{while}\quad
\phi_{10}(P,In)=\phi_{10}(T,In),
```

and

```math
(P,Or)\neq(T,Or)
\quad\text{while}\quad
\phi_{10}(P,Or)=\phi_{10}(T,Or).
```

Therefore `phi_10` formally forgets the domain coordinate of informational and organizational entities.

This is an exact mathematical statement about the native type systems; it is **not yet evidence that `M_0` loses engineering meaning**, because that domain information may remain recoverable from auxiliary entity context.

---

## 3. Map from `M_0` to `M_1`

A mapping from physical types is canonical:

```math
P\mapsto(P,Ph),
\qquad
T\mapsto(T,Ph).
```

For `I` and `O`, however, the layer label alone is insufficient to choose a domain coordinate.

Therefore a native map

```math
\phi_{01}:\mathcal L_0\rightarrow\mathcal L_1
```

is not well-defined without additional attribution information.

Introduce an auxiliary attribution function, derived only from the common evidence budget,

```math
\eta:\mathcal V^*\rightarrow\{P,T,\varnothing,PT\},
```

where:

```text
P  = power-affiliated entity;
T  = transport-affiliated entity;
PT = genuinely shared/cross-domain entity;
∅  = domain affiliation unresolved by the evidence.
```

Then define the evidence-conditioned map

```math
\phi_{01}^{\eta}:M_0\rightarrow M_1
```

for single-domain entities by

```math
P\mapsto(P,Ph),
```

```math
T\mapsto(T,Ph),
```

```math
(I,e)\mapsto(\eta(e),In),
\qquad \eta(e)\in\{P,T\},
```

```math
(O,e)\mapsto(\eta(e),Or),
\qquad \eta(e)\in\{P,T\}.
```

For

```math
\eta(e)\in\{PT,\varnothing\},
```

the declared `M_1` has no unique native image without duplication, arbitrary assignment, or ontology extension.

Thus `phi_01^eta` is a **partial/evidence-conditioned map**, not a canonical inverse of `phi_10`.

---

## 4. Composition tests

### 4.1 `M_1 -> M_0 -> M_1`

For a physical entity,

```math
\phi_{01}^{\eta}\circ\phi_{10}(P,Ph)=(P,Ph)
```

and similarly for `(T,Ph)`.

For informational and organizational entities, identity is recovered only if `eta` restores the original domain coordinate:

```math
\phi_{01}^{\eta}\circ\phi_{10}(\alpha,In)=(\alpha,In)
```

iff

```math
\eta(e)=\alpha.
```

The same condition applies for `Or`.

Therefore the round trip is not identity from the native type label alone.

### 4.2 `M_0 -> M_1 -> M_0`

For a single-domain entity with resolved `eta`,

```math
\phi_{10}\circ\phi_{01}^{\eta}(e)=e
```

at the coarse layer-class level.

However, if `M_0` entity identity contains richer actor/domain semantics, the coarse class round trip does not prove preservation of all semantic metadata; it proves only recovery of the original `P/T/I/O` layer label.

---

## 5. Formal non-isomorphism result

At the native type-system level,

```math
M_0\not\cong M_1
```

under the declared mappings because:

1. `phi_10` is many-to-one for informational and organizational types;
2. `phi_01` is not uniquely defined for `I` and `O` without the auxiliary attribution function `eta`;
3. shared/cross-domain informational or organizational entities have no unique image in the declared single-domain `M_1` type space.

This establishes **formal representational difference**, not superiority.

---

## 6. Common-fact encoding framework

For each frozen case `V_k`, let

```math
\mathcal F_k=\{f_{k1},\ldots,f_{kn_k}\}
```

be the set of engineering facts supplied identically to both models.

Define an encoder

```math
Enc_M:\mathcal F_k\rightarrow\mathcal R_M
```

and a decoder/reconstruction relation

```math
Dec_M:\mathcal R_M\rightrightarrows\mathcal F_k.
```

A reconstruction relation rather than a simple function is used because one encoded object may admit several semantically plausible interpretations.

---

## 7. Semantic-loss measure

Define the facts uniquely recoverable from representation `M` as

```math
Rec_M(\mathcal F_k)
=
\{f\in\mathcal F_k:\;Dec_M(Enc_M(f))=\{f\}\}.
```

The normalized semantic-loss fraction is

```math
L_{sem}(M,V_k)
=
1-
\frac{|Rec_M(\mathcal F_k)|}{|\mathcal F_k|}.
```

Interpretation:

```text
0 = every declared fact is uniquely recoverable;
1 = no declared fact is uniquely recoverable.
```

This measure is used only after the `F_k` fact sets are frozen in 0E.

---

## 8. Ambiguity measure

For encoded object `r`, let

```math
\kappa_M(r)=|Dec_M(r)|
```

be the number of admissible factual reconstructions consistent with the representation and the declared grammar.

Define ambiguity information

```math
E_{amb}(M,V_k)
=
\sum_{r\in Enc_M(\mathcal F_k)}
\log_2\!\bigl(\max(1,\kappa_M(r))\bigr).
```

Thus:

```text
E_amb = 0  -> every encoded object has one admissible interpretation;
E_amb > 0 -> at least one representation admits multiple interpretations.
```

This is a representation-level ambiguity measure, not a probability distribution over physical states.

---

## 9. Ad hoc construction count

Define

```math
N_{adhoc}(M,V_k)
```

as the number of case-specific rules, exceptions, duplications, external attribution maps, or ontology extensions required to encode and decode `V_k` beyond the model's frozen native grammar.

Examples that count as ad hoc if required only after a case is encountered:

```text
- introducing a hidden domain coordinate into M_0;
- creating a new Shared domain in M_1;
- duplicating one shared organization into P and T copies;
- adding a special relation type used only for V3;
- adding case-specific recovery rules not used elsewhere.
```

Rules already frozen in the ontology before the case do not count as ad hoc.

---

## 10. Complexity vector

Use the frozen component-wise complexity audit:

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

No scalar complexity weighting is permitted in 0D/0E v1.0.

---

## 11. Equal-information audit

For every case, construct a two-column ledger:

| Fact | Available to `M_0`? | Available to `M_1`? |
|---|---:|---:|
| source identity | yes | yes |
| receiver identity | yes | yes |
| domain affiliation evidence | yes | yes |
| informational/organizational function | yes | yes |
| mechanism | yes | yes |
| delay/state/history payload | yes | yes |
| evidence/provenance | yes | yes |
| service consequence definition | yes | yes |

If any row differs, the case is invalid for comparative scoring until corrected.

---

## 12. 0D result

The controlled mapping analysis establishes one result only:

> **`M_0` and `M_1` are not isomorphic as native type systems.**

The difference is structurally specific:

```text
M_0 compresses domain affiliation for I/O into auxiliary context;
M_1 encodes that affiliation natively but has a potential single-domain-label problem for genuinely shared entities.
```

Whether either difference matters for explanation, identifiability, prediction, or engineering decision remains an empirical/formal case question for 0E.
