# Theoretical Decision Gate — Execution Log

**Purpose:** auditable record of Phase-0 gate execution.  
**Rule:** completion status reflects accepted outputs, not activity. Retrospective edits must not make later choices appear preregistered.

## Gate identity

```text
Protocol: THEORETICAL_DECISION_GATE_PROTOCOL_V1.md
Definition register: INTERDEPENDENCY_DEFINITION_REGISTER.md
Requirement matrix: REPRESENTATION_REQUIREMENTS_MATRIX.md
0C source register: PHASE0_0C_SOURCE_REGISTER.md
0C core benchmark: PHASE0_0C_THEORY_BENCHMARK_V1.md
0C saturation R1–R4: PHASE0_0C_SATURATION_SEARCH_ROUND1.md ... ROUND4.md
0C closure: PHASE0_0C_CLOSURE_MEMO.md
0D common reality: PHASE0_0D_COMMON_REALITY_SPECIFICATION.md
0D baseline: PHASE0_0D_M0_FORMALIZATION.md
0D candidate: PHASE0_0D_M1_FORMALIZATION.md
0D mapping: PHASE0_0D_MAPPING_AND_INFORMATION_LOSS.md
0D comparison: PHASE0_0D_COMPARISON_PROTOCOL.md
Repository: Dossiya-SE/MSE-thesis
Branch: main
```

## Current status

| Phase | State | Evidence of completion | Scientific meaning |
|---|---|---|---|
| 0A — definitions | `Frozen_v1.0` | definition register committed before scoring | terminology and boundaries fixed |
| 0B — requirements | `Frozen_v1.0` | R1–R12, G1–G5, V1–V5 and score rules committed before scoring | criteria cannot be changed to favor a result |
| 0C — theory benchmark | `Closed__bounded_saturation` | core benchmark + R1–R4 + closure memo | predecessor envelope stabilized sufficiently for controlled comparison; no novelty claim |
| 0D — formalize M0/M1 | `Complete__formal_difference_found` | five 0D artifacts committed under equal information/physics controls | native type systems are formally non-isomorphic; no superiority claim |
| 0E — V1–V5 tests | `Ready` | 0D complete and comparison protocol preregistered | engineering significance of the formal difference may now be tested |
| 0F — dependency-contract ablation | `Blocked_by_0E` | none | monolithic vs layered relation objects remain provisional |
| 0G — RETAIN/REVISE/REPLACE | `Blocked` | 0E–0F incomplete | no canonical ontology decision permitted |

---

## 0C retained bounded conclusions

The evidence already establishes as prior art, within the bounded search:

```text
multilayer infrastructure structure;
physical + information/control + organization modeling;
dynamic/time-aware interdependency;
shared-state SoS representations;
semantic/ontology interoperability;
HLA/FMI/HELICS execution interoperability;
relation-as-object + metadata;
SysML/ontology/executable bridges;
compositional open systems and syntax/semantics separation;
behavioral/safety contracts on compositional architectures.
```

Therefore none of those may be used alone as the thesis novelty claim.

The stable predecessor envelope remains:

```math
\mathcal P^*=\{
\text{SoS},
\text{interdependency theory},
\text{multilayer networks},
\text{CPS/socio-technical models},
\text{ontologies},
\text{shared-state models},
\text{temporal models},
\text{semantic interoperability},
\text{FMI/HLA/HELICS},
\text{knowledge graphs},
\text{compositional open systems},
\text{contracts}
\}.
```

---

# 0D controlled formalization — completed

## D0 — common reality frozen

The two ontologies use exactly the same:

```text
entity universe V*;
physical states x_P,x_T;
domain laws F_P,F_T;
informational/organizational state facts z_I,z_O;
relation payload R_e*;
evidence set E*;
service set Q*;
verification cases V1–V5.
```

The control condition is

```math
\mathcal E_{M_0}=\mathcal E_{M_1}=\mathcal E^*.
```

Only endpoint/system typing changes.

## D1 — baseline frozen

```math
M_0:\qquad \mathcal S_0=\{P,T,I,O\}.
```

Entity type:

```math
v_i^{(0)}=(id_i,\ell_i),
\qquad
\ell_i\in\{P,T,I,O\}.
```

`I` and `O` are global layer labels; domain affiliation of informational/organizational entities may remain available through entity/actor context but is not a separate native type coordinate.

## D2 — candidate frozen

```math
M_1:\qquad \mathcal S_1=\mathcal D\times\mathcal A,
```

with

```math
\mathcal D=\{P,T\},
\qquad
\mathcal A=\{Ph,In,Or\}.
```

Entity type:

```math
v_i^{(1)}=(id_i,\alpha_i,a_i).
```

`M_1` natively separates infrastructure affiliation from physical/informational/organizational aspect.

A countervailing unresolved issue is retained: a genuinely shared/cross-domain information or organization entity may not have a unique single-domain coordinate in the declared `M_1` grammar.

## D3 — mappings frozen

The forgetful map

```math
\phi_{10}:M_1\rightarrow M_0
```

is defined by

```math
(P,Ph)\mapsto P,
\qquad
(T,Ph)\mapsto T,
```

```math
(P,In),(T,In)\mapsto I,
```

```math
(P,Or),(T,Or)\mapsto O.
```

It is many-to-one for information and organization.

A reverse map requires evidence-conditioned domain attribution:

```math
\phi_{01}^{\eta}:M_0\rightarrow M_1,
```

where

```math
\eta(e)\in\{P,T,PT,\varnothing\}.
```

For `eta(e)=PT` or unresolved affiliation, the declared `M_1` has no unique native image without duplication, arbitrary assignment, or extension.

## D4 — mathematical result

At the native type-system level:

```math
M_0\not\cong M_1.
```

Reason:

```text
1. phi_10 is non-injective for informational/organizational types;
2. phi_01 is not canonical from M0 labels alone;
3. shared/cross-domain entities expose a potential inverse problem for M1.
```

This is the **only accepted comparative conclusion from 0D**.

It does not imply that `M_1` is better.

---

## 0D metrics preregistered for 0E

For each case `V_k`:

### Semantic loss

```math
L_{sem}(M,V_k)
=
1-
\frac{|Rec_M(\mathcal F_k)|}{|\mathcal F_k|}.
```

### Ambiguity

```math
E_{amb}(M,V_k)
=
\sum_{r\in Enc_M(\mathcal F_k)}
\log_2\!\left(\max(1,\kappa_M(r))\right).
```

### Ad hoc construction

```math
N_{adhoc}(M,V_k)
=
\text{count of case-specific rules/extensions beyond the frozen grammar}.
```

### Complexity

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

No scalar complexity weighting is allowed in v1.0.

---

## 0D proposition state

Null:

> `M_0` and `M_1` are representationally equivalent for the declared P–T problem after controlling for available information.

Alternative:

> At least one required distinction cannot be represented by one ontology without semantic loss, ambiguity, or ad hoc construction.

0D establishes native **formal non-isomorphism**, but the engineering form of the null remains open until V1–V5 are executed in 0E.

---

## Frozen decision prohibition

Until 0E and 0F are complete, the following claims remain prohibited:

```text
"M1 is better than M0";
"M0 should be revised";
"M1 should replace M0";
"the domain × aspect ontology is canonical";
"the Phase-0 dependency contract is novel";
"the seven-stage framework should be changed".
```

---

## Next release target

```text
0E — encode and test V1–V5 under both ontologies using the frozen fact sets, R1–R12, L_sem, E_amb, N_adhoc and component-wise complexity.
```

0F remains blocked until the ontology-only comparison has been completed, preserving causal attribution between ontology effects and dependency-contract effects.
