# Phase 0E — Frozen R1–R12 Score Matrix

**Status:** 0E COMPARATIVE RESULT v1.0  
**Inputs:** `PHASE0_0E_ENGINEERING_FACT_SETS_AND_PHYSICS.md`, `PHASE0_0E_CASE_ENCODING_AND_METRICS.md`, frozen `REPRESENTATION_REQUIREMENTS_MATRIX.md`.  
**Rule:** no requirement definition, score scale or verification case is changed after results are observed.

---

# 1. Scoring scale

```math
s_j(M)\in\{0,1,2\},
```

where:

```text
0 = cannot represent without ontology change or external formalism;
1 = representable only implicitly, ambiguously or through ad hoc convention;
2 = represented explicitly/consistently under the frozen representation architecture without case-specific repair.
```

The diagnostic sum is descriptive only:

```math
S_{diag}(M)=\sum_{j=1}^{12}s_j(M).
```

A gate failure cannot be compensated by the total score.

---

# 2. Requirement-by-requirement result

| Requirement | `M_0` | `M_1` | Derivation / evidence | Frozen case(s) |
|---|---:|---:|---|---|
| `R1` Constituent-system identity | 2 | 2 | both preserve `P` and `T` as independent physical systems with unchanged `x_P,x_T,F_P,F_T`; `M_1` adds aspect coordinates but does not create the constituent identity | V1, V4, V5 |
| `R2` Mechanism explicitness | 2 | 2 | both use the identical Stage-2 mechanism payload `M_e,m_e,...`; endpoint typing does not create or remove the mechanism | V1–V4 |
| `R3` Directionality | 2 | 2 | both encode distinct directed relations and mediated paths; neither forces symmetry | V1, V4 |
| `R4` Informational relations | 2 | 2 | `M_0` has an explicit `I` layer and `M_1` explicit `In` aspects; V2 is uniquely reconstructable under both with the frozen evidence ledger | V2 |
| `R5` Organizational relations | 2 | 2 | `M_0` has explicit `O`; `M_1` has domain-indexed `Or`; V3 authority/access/crew/restoration semantics are uniquely recoverable under both | V3 |
| `R6` State dependence | 2 | 2 | both receive identical time/state-dependent `w_e,a_e,H_t` and physical state variables; ontology does not freeze functional influence | V1, V4 |
| `R7` Time and delay | 2 | 2 | both retain identical `delta_e,tau_e,H_t`; V2–V4 distinguish information delay, travel/response timing and event ordering | V2–V4 |
| `R8` Feedback and mediated reciprocity | 2 | 2 | both represent `P->T->...->P` as a directed path without requiring reciprocal asset-pair edges | V4 |
| `R9` Evidence/uncertainty status | 2 | 2 | both use the same explicit evidence/provenance ledger separate from physical state; neither is given hidden confidence information | V1–V5 |
| `R10` Service consequence | 2 | 2 | common service functionals `Q_k=G_k(Y*)` and common physics allow `Delta relation -> Delta X -> Delta Q` under both | V1, V4, V5 |
| `R11` Physics preservation | 2 | 2 | both retain `F_P != F_T`; V5 additionally retains independent `F_W`; ontology changes only endpoint typing | V1, V4, V5 |
| `R12` Extensibility/composability | 2 | 2 | both admit conservative Water extension without changing the relation payload or reclassifying existing P–T meanings; `M_0` extends its type set, `M_1` extends its domain set | V5 |

---

# 3. Diagnostic totals

```math
S_{diag}(M_0)=24,
```

```math
S_{diag}(M_1)=24.
```

This equality is not an assertion that the ontologies are mathematically identical. 0D already proved

```math
M_0\not\cong M_1
```

as native type systems.

It means only that the frozen V1–V5 requirements do not expose a required engineering capability that one model can represent and the other cannot under the equal-information protocol.

---

# 4. Non-compensable gate audit

## G1 — Ontological correctness

Requirements:

```math
\{R_1,R_2,R_3\}.
```

Result:

```text
M_0: PASS
M_1: PASS
```

Reason: both preserve constituent P/T identity, mechanism payload and directionality.

## G2 — Dynamic causal adequacy

Requirements:

```math
\{R_2,R_3,R_6,R_7,R_8\}.
```

Result:

```text
M_0: PASS
M_1: PASS
```

Reason: the dynamic causal capabilities are carried by the common relation payload and governing dynamics, not by the endpoint type coordinates alone.

## G3 — Socio-technical adequacy

Requirements:

```math
\{R_4,R_5\}.
```

Result:

```text
M_0: PASS
M_1: PASS
```

Reason: both explicitly represent information and organization as active modeled functions/states. `M_1` makes domain affiliation native; `M_0` recovers it from frozen actor/subsystem context without ambiguity in V2–V3.

## G4 — Engineering adequacy

Requirements:

```math
\{R_{10},R_{11}\}.
```

Result:

```text
M_0: PASS
M_1: PASS
```

Reason: both preserve domain physics and service mappings.

## G5 — Reusability and evidence discipline

Requirements:

```math
\{R_9,R_{12}\}.
```

Result:

```text
M_0: PASS
M_1: PASS
```

Reason: the evidence ledger is explicitly separated from physical state for both, and both pass the conservative Water-extension test.

---

# 5. Comparative proposition

The preregistered null was:

> After controlling for the information budget, `M_0` and `M_1` are representationally equivalent for the declared Power–Transportation problem; apparent differences are only notational or recoverable without case-specific exceptions.

The alternative required at least one frozen distinction to generate semantic loss, ambiguity or ad hoc construction in one ontology.

Observed 0E result:

```math
L_{sem}=0,
\qquad
E_{amb}=0,
\qquad
N_{adhoc}=0
```

for both ontologies on all five frozen cases.

Therefore:

```text
H_0D IS NOT REJECTED by V1–V5 under the declared equal-information fixture.
```

This wording is deliberate. It does not prove universal equivalence.

---

# 6. What remains different

The score equality does not erase the 0D structural difference.

### `M_0`

```text
- smaller native type vocabulary;
- one type coordinate;
- P/T physical domains explicit;
- I/O domain affiliation stored in auxiliary actor/subsystem context.
```

### `M_1`

```text
- two-coordinate type system;
- domain affiliation of I/O entities explicit in the native type;
- larger number of native type combinations;
- systematic product construction when a new domain is added.
```

The frozen cases show that these are currently differences in **where information is stored**, not differences in recoverable engineering meaning.

---

# 7. Scientific conclusion of the score matrix

The central 0E result is:

> The formal non-isomorphism `M_0 != M_1` is mathematically real, but its engineering significance is not demonstrated by the controlled V1–V5 representation tests when both ontologies receive identical actor, subsystem, mechanism, evidence, physics and service information.

Consequently, 0E provides **no scientific basis for replacing the canonical ontology solely because the domain × aspect form is more explicit**.

This is not yet the final Phase-0 decision. 0F must still test whether the dependency representation itself — not the ontology — can be simplified or improved.