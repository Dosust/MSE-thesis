# Phase 0D — Controlled Comparison Protocol

**Status:** PREREGISTERED COMPARISON PROTOCOL v1.0  
**Purpose:** define how `M_0` and `M_1` will be compared without allowing post hoc changes that favor either ontology.  
**Scope:** formal representation only; no resilience-performance, cascade-loss, recovery-time, or viability calculation in 0D.

---

## 1. Scientific question

Can `M_0` and `M_1` represent the same Power–Transportation infrastructure reality using the same information, and where do their formal capabilities differ?

---

## 2. Competing models

Baseline:

```math
M_0:\quad \mathcal S_0=\{P,T,I,O\}.
```

Candidate:

```math
M_1:\quad \mathcal S_1=\mathcal D\times\mathcal A,
```

with

```math
\mathcal D=\{P,T\},
\qquad
\mathcal A=\{Ph,In,Or\}.
```

Only the ontology/type system changes.

---

## 3. Controlled variables

The following are fixed and identical:

```text
- entity universe V*;
- x_P and x_T;
- F_P and F_T;
- informational and organizational state facts;
- relation payload R_e*;
- evidence/provenance fact set E*;
- service set Q*;
- frozen requirements R1–R12;
- frozen cases V1–V5.
```

Any comparison violating this equality is invalid.

---

## 4. Experimental variable

The only intended treatment variable is endpoint/system typing:

```math
\lambda_0(e)\in\{P,T,I,O\}
```

versus

```math
\lambda_1(e)\in\mathcal D\times\mathcal A.
```

No dependency-contract redesign is allowed before 0F.

---

## 5. Comparative proposition

### Null proposition

`H_0D`:

> After controlling for the information budget, `M_0` and `M_1` are representationally equivalent for the declared Power–Transportation problem; apparent differences are only notational or recoverable without case-specific exceptions.

### Alternative proposition

`H_1D`:

> At least one required distinction cannot be represented by one ontology without semantic loss, ambiguity, or ad hoc construction under the same information budget.

This is a formal model-comparison proposition, not a frequentist statistical hypothesis.

---

## 6. Stepwise comparison procedure

### Step D1 — verify fixture equality

Before each case, confirm

```math
\mathcal E_{M_0}=\mathcal E_{M_1}=\mathcal E^*.
```

Confirm identical `F_P,F_T,R_e*,Q*`.

Failure -> case cannot be scored.

### Step D2 — encode case under `M_0`

Record:

```text
- entity labels;
- relation endpoints;
- relation payload;
- auxiliary semantic context required;
- any ambiguity;
- any case-specific convention.
```

### Step D3 — encode the same case under `M_1`

Record the same fields and no additional facts.

### Step D4 — decode engineering facts

Attempt to reconstruct the frozen fact set `F_k` from each encoded representation using only:

```text
- the ontology's native grammar;
- previously frozen global rules;
- the shared evidence ledger.
```

No new case-specific inference rule may be introduced after encoding.

### Step D5 — calculate formal metrics

For each model and case, record:

```math
L_{sem}(M,V_k),
```

```math
E_{amb}(M,V_k),
```

```math
N_{adhoc}(M,V_k),
```

and

```math
C(M,V_k).
```

### Step D6 — score frozen requirements

For each `R_j`, assign

```math
s_j(M)\in\{0,1,2\}
```

using the frozen definitions in `REPRESENTATION_REQUIREMENTS_MATRIX.md`.

Every nonzero score requires a derivation/evidence note.

### Step D7 — gate audit

Check non-compensable gates `G1–G5`.

No diagnostic total may override a complete gate failure.

---

## 7. Formal metrics

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

### Ad hoc additions

```math
N_{adhoc}(M,V_k)
=
\text{count of case-specific rules/extensions beyond frozen grammar}.
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

No scalar weighted objective is permitted in v1.0.

---

## 8. Formal mapping audit

The mapping specification has already established

```math
\phi_{10}:M_1\rightarrow M_0
```

as a many-to-one forgetful map for informational/organizational domain coordinates, while

```math
\phi_{01}^{\eta}:M_0\rightarrow M_1
```

requires an auxiliary domain-attribution function `eta` for `I/O` entities.

The mapping result

```math
M_0\not\cong M_1
```

at the native type-system level is therefore retained as a mathematical result.

This does **not** reject `H_0D` at the engineering level until the frozen cases show that the non-isomorphism causes material semantic loss, ambiguity, or ad hoc construction.

---

## 9. Required case table

For each of `V1–V5`, fill:

| Field | `M_0` | `M_1` |
|---|---|---|
| facts available | identical | identical |
| native encoding | TBD | TBD |
| facts uniquely recoverable | TBD | TBD |
| `L_sem` | TBD | TBD |
| `E_amb` | TBD | TBD |
| `N_adhoc` | TBD | TBD |
| complexity vector | TBD | TBD |
| R1–R12 implications | TBD | TBD |

---

## 10. Stopping and interpretation rule for 0D

0D is complete when:

```text
1. common reality is frozen;
2. both ontologies are formally specified;
3. phi_10 and phi_01^eta are defined;
4. information-loss/ambiguity metrics are frozen;
5. the comparison procedure is preregistered;
6. no ontology is modified after seeing V1–V5 results.
```

The permitted 0D result is one of:

```text
A. NATIVE TYPE SYSTEMS FORMALLY EQUIVALENT;
B. NATIVE TYPE SYSTEMS FORMALLY DIFFERENT.
```

For v1.0, the mapping analysis yields:

```text
B. NATIVE TYPE SYSTEMS FORMALLY DIFFERENT.
```

This does **not** imply:

```text
- M1 is better;
- M0 should be revised;
- M1 should replace M0.
```

Those conclusions remain blocked until 0E–0G.

---

## 11. Transition condition to 0E

0E becomes permitted once this protocol and the four supporting 0D specification files are committed and the execution log is updated.

0E will then test the engineering significance of the formal difference using only V1–V5 and R1–R12.
