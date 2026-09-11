# Full-Text Evidence-to-Equation Extraction Protocol — FTEE v1.0

![Status](https://img.shields.io/badge/status-PILOT--READY-0969DA)
![Freeze](https://img.shields.io/badge/protocol-NOT%20YET%20FROZEN-9A6700)
![Scope](https://img.shields.io/badge/phase-full--text%20evidence%20extraction-8250DF)

**Status:** PILOT-READY / NOT YET FROZEN  
**Position in workflow:** first operational protocol after completion of the frozen 325-paper ranking  
**Purpose:** auditable source-to-mechanism-to-equation evidence extraction for demonstrator design  
**Freeze rule:** pilot the extraction table/codebook on a deliberately heterogeneous ranked-paper subset, resolve ambiguities, then freeze FTEE before full-scale extraction.  
**Preservation rule:** this file preserves the scientific logic, evidence rules, VVUQ separation, uncertainty treatment, hypothesis mapping, and acceptance gates of the supplied FTEE v1.0 specification while normalizing Markdown/math for GitHub rendering.

The protocol is not a paper-summary workflow. It establishes the auditable transformation

```math
\text{scientific paper}
\rightarrow
\text{mechanism}
\rightarrow
\text{mathematical representation}
\rightarrow
\text{parameters}
\rightarrow
\text{validation evidence}
\rightarrow
\text{hypothesis}
\rightarrow
\text{candidate model component}.
```

---

## 1. Scientific objective

Let the post-ranking full-text priority set be

```math
\mathcal P^\star=\{P_1,\ldots,P_N\}.
```

For every paper $P_i$, extract only source-supported information and create evidence units.

**Equation FTEE-1 — Evidence-unit definition**

```math
\boxed{
e_{ij}
=
(S_i,L_{ij},C_{ij},M_{ij},F_{ij},X_{ij},\theta_{ij},A_{ij},\Omega_{ij},V_{ij},U_{ij},H_{ij})
}
```

with

```math
\begin{aligned}
S_i&=\text{source identity},\\
L_{ij}&=\text{exact source location},\\
C_{ij}&=\text{scientific claim},\\
M_{ij}&=\text{mechanism},\\
F_{ij}&=\text{mathematical representation},\\
X_{ij}&=\text{state/input/output variables},\\
\theta_{ij}&=\text{parameters},\\
A_{ij}&=\text{assumptions},\\
\Omega_{ij}&=\text{domain/boundary conditions},\\
V_{ij}&=\text{verification/validation evidence},\\
U_{ij}&=\text{uncertainty information},\\
H_{ij}&=\text{mapping to }H_1-H_5.
\end{aligned}
```

The extraction unit is therefore the **evidence unit**, not merely the paper:

```math
P_i\rightarrow\{e_{i1},e_{i2},\ldots,e_{im}\}.
```

One paper may provide a mechanism, another a governing equation, another parameterization, and another validation benchmark.

---

## 2. Methodological foundations

FTEE combines structured systematic-review extraction with computational-model credibility practice. The governing principles are

```math
\text{traceability}
+
\text{source fidelity}
+
\text{VVUQ separation}
+
\text{explicit uncertainty}
+
\text{hypothesis relevance}.
```

The supplied methodology grounds these principles in structured extraction guidance, ASME VVUQ terminology/context-of-use discipline, NASA-STD-7009B model-credibility practice, and explicit uncertainty characterization.

---

## 3. Evidence-phase lock

FTEE starts **only after** completion of the frozen 325-paper Monte Carlo ranking:

```math
\text{frozen ranking}
\rightarrow
\text{priority papers}
\rightarrow
\text{full-text extraction}.
```

The demonstrator must not be selected first and then used to select preferred evidence. The prohibited sequence is

```math
\text{desired model}
\rightarrow
\text{preferred evidence}
\rightarrow
\text{apparent confirmation}.
```

The full-text phase may use the selected paper, supplements, corrections/errata, and clearly linked reports of the same study, but each source remains individually traceable.

---

## 4. Master extraction schema

| Block | Required fields |
|---|---|
| **A. Provenance** | EvidenceUnitID, PaperID, DOI, title, year, source file, page, section, equation/table/figure identifier |
| **B. Scientific role** | current hypothesis $H_1$–$H_5$, research question, mechanism type, infrastructure layers |
| **C. Mechanism** | source entity/state, causal process, receiver, effect, directionality, delay, mode/history dependence |
| **D. Mathematics** | exact equation, equation family, variables, parameters, constraints, IC/BC, units, timescale, numerical method |
| **E. Model domain** | assumptions, parameter range, topology/system scale, hazard, operating regime, demonstrated-use domain |
| **F. Credibility** | calibration data, benchmark, verification, validation referent, error metric, sensitivity/UQ, limitations |
| **G. Thesis transfer** | canonical variable mapping, P/T/I/O applicability, evidence role, adaptation required, inclusion decision |

---

## 5. Exact provenance is mandatory

No equation enters the thesis model registry without

```math
\text{PaperID}
+
\text{page}
+
\text{section}
+
\text{equation/table/figure identifier}.
```

Use a unique evidence-unit ID such as `H1-P023-EQ04`. If there is no equation number, record an exact location such as `p.12, Methods, paragraph 3`.

A generic note such as “Equation from Smith et al.” is not sufficiently reproducible.

---

## 6. Preserve source notation before canonicalization

Raw source notation must be stored before mapping into thesis notation.

If the source reports

```math
\dot z_i=f_i(z_i,z_j,\lambda_{ij}),
```

store it first as

```math
F_{\rm raw}=\dot z_i=f_i(z_i,z_j,\lambda_{ij}).
```

Then define a separate thesis mapping such as

```math
\phi_i:(z_i,z_j,\lambda_{ij})
\mapsto
(E_i^\alpha,E_j^\beta,w_{ij}).
```

The source equation and thesis equation are not the same object:

```math
F_{\rm source}\neq F_{\rm thesis}.
```

**Equation FTEE-2 — Source-to-thesis mapping**

```math
F_{\rm thesis}=\mathcal T_{\rm map}(F_{\rm source}).
```

This prevents thesis choices from being incorrectly attributed to the source.

---

## 7. Provenance classes

Every mathematical object receives a provenance class.

| Class | Meaning | Rule |
|---|---|---|
| **R — Reported** | explicitly reported by the source | may be attributed directly |
| **C — Calculated/Reconstructed** | algebraically reconstructed from reported source information | reconstruction must be shown |
| **T — Transferred** | adapted from another domain/system into P–T–I–O | transfer assumptions must be explicit |
| **P — Proposed** | introduced by this thesis | must never be attributed to the source |

This is distinct from the scientific status system `[E]`, `[D]`, `[P]`. For example, a transferred object may have

```math
\text{Provenance}=T,
\qquad
\text{Scientific status}=[D].
```

---

## 8. Mechanism extraction precedes equation extraction

Do not begin by searching for equations. First identify

```math
\text{Source}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Receiver}
\rightarrow
\text{Effect}.
```

Map the mechanism to the Stage-2 object

```math
\mathfrak I_{ij}^{\alpha\beta}
=
(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t).
```

For every component, record `reported`, `not reported`, or `not applicable`. Never infer a value solely because the thesis framework contains the corresponding field. For example,

```math
\delta_{ij}=\mathrm{NR}
```

is preferable to inventing a delay.

---

## 9. Keep mechanism, mathematical-form, and validation evidence separate

Define

```math
E_M=\text{mechanism evidence},
\qquad
E_F=\text{mathematical-form evidence},
\qquad
E_V=\text{validation evidence}.
```

Do not collapse them into one score.

| Level | $E_M$: mechanism | $E_F$: mathematical form | $E_V$: validation |
|---|---|---|---|
| **0 — None** | mechanism absent | no equation/model | no validation |
| **1 — Indirect** | discussed or assumed | mathematical form referenced/implicit | qualitative/internal comparison |
| **2 — Explicit** | explicitly modeled/analyzed | equation/model fully specified | benchmark/calibration comparison reported |
| **3 — Strong direct evidence** | mechanism directly investigated under controlled/data-supported conditions | full mathematical specification plus assumptions/domain | independent empirical/benchmark validation with quantitative discrepancy/error |

Retain the triplet

```math
(E_M,E_F,E_V)
```

rather than a weighted aggregate. A paper with $(3,3,0)$ is mathematically useful but is not thereby validated.

---

## 10. Equation extraction rules

**Equation FTEE-3 — Governing-equation extraction tuple**

```math
\mathcal E_{ij}
=
(F_{\rm raw},X,U,\theta,A,B,IC,BC,\Omega,N),
```

where $X$ are states, $U$ inputs/controls, $\theta$ parameters, $A$ algebraic constraints, $B$ physical bounds, $IC$ initial conditions, $BC$ boundary conditions, $\Omega$ the validity/application domain, and $N$ the numerical procedure.

The governing rule is

```math
\text{equation without its assumptions/domain}
\neq
\text{fully extracted model}.
```

---

## 11. Units and dimensional audit

Every physical variable and parameter must record

```math
\text{name}
+
\text{symbol}
+
\text{physical interpretation}
+
\text{unit}.
```

If units are absent, use `UnitStatus = NR`; do not infer silently. If the equation is dimensional, check

```math
[\mathrm{LHS}]=[\mathrm{RHS}].
```

Any per-unit or normalized formulation must record the normalization explicitly.

---

## 12. Parameter extraction

For each parameter $\theta_k$, record

```math
\Theta_k
=
(\text{value},\text{unit},\text{source},\text{range/distribution},\text{calibration method}).
```

A parameter does not enter the model merely as a nominal number. If only a nominal value is reported, record only that. Do not fabricate uncertainty distributions.

---

## 13. Timescale extraction

Explicitly track

```math
\boldsymbol\tau
=
[\tau^{op},\tau^{dist},\tau^{prop},\tau^{ctrl},\tau^{rec},\tau^{adapt}].
```

Use `NR` for absent timescales. Preserve the distinction

```math
\text{physical timescale}
\neq
\text{numerical time step}.
```

---

## 14. Assumption registry

For every evidence unit classify assumptions as

```math
A
=
A_{\rm explicit}
\cup
A_{\rm mathematical}
\cup
A_{\rm physical}
\cup
A_{\rm numerical}.
```

Only assumptions explicitly stated or unavoidably implied mathematically are entered as source assumptions. If an assumption is an extractor interpretation, set

```math
\mathrm{ExtractorInference}=\mathrm{TRUE}.
```

---

## 15. Validation extraction follows VVUQ terminology

Use separate fields for:

| Evidence | Question |
|---|---|
| **Code verification** | Was the mathematical model implemented correctly? |
| **Solution verification** | Were discretization/convergence/numerical errors assessed? |
| **Conceptual validation** | Are assumptions and governing equations appropriate for the intended phenomenon? |
| **Empirical validation** | Were predictions compared with an independent referent? |
| **Calibration** | Were parameters fitted to data? |
| **Sensitivity analysis** | Which inputs dominate outputs? |
| **UQ** | How were uncertain quantities propagated? |

The protocol enforces

```math
\text{calibration}\neq\text{validation}.
```

A model calibrated and evaluated only on the same dataset is not recorded as independently validated.

---

## 16. Validation referent

**Equation FTEE-4 — Validation-evidence tuple**

```math
V=(R,D_{\rm cal},D_{\rm val},M_V,\varepsilon_V),
```

where $R$ is the referent, $D_{\rm cal}$ calibration data, $D_{\rm val}$ validation data, $M_V$ the validation metric, and $\varepsilon_V$ the reported discrepancy/error.

Possible referents include field data, laboratory data, benchmark solutions, and in appropriate cases higher-fidelity models.

---

## 17. Validation domain

Never record only “validated.” Record

```math
\Omega_V
=
\text{domain for which validation evidence was demonstrated}.
```

Later confirmatory testing should satisfy

```math
\Omega_H\subseteq\Omega_V,
```

or explicitly disclose extrapolation.

---

## 18. Uncertainty extraction

Record

```math
U
=
\{U_\theta,U_{\rm IC},U_D,U_M,U_N,U_h\},
```

where these denote parameter, initial-condition, measurement/data, model-form, numerical, and hazard/scenario uncertainty.

For each uncertainty record:

```math
\text{source}
+
\text{type}
+
\text{representation}
+
\text{propagation method}
+
\text{output impact}.
```

If uncertainty is not quantified, record `UQ = NR`, not zero.

---

## 19. Transferability to P–T–I–O

Every evidence unit must answer whether it can legitimately transfer to the thesis system.

```math
T_{ij}
\in
\{\mathrm{Direct},\mathrm{Conditional},\mathrm{Conceptual},\mathrm{Not\ transferable}\}.
```

- **Direct:** same or essentially equivalent mechanism.
- **Conditional:** requires explicit assumptions or parameter adaptation.
- **Conceptual:** useful for theory/method only, not direct transplantation.
- **Not transferable:** cannot support the proposed model component.

Do not convert this classification into an arbitrary scalar score.

---

## 20. Hypothesis mapping

Every retained evidence unit must support at least one element of

```math
H_i
\rightarrow
M_i
\rightarrow
X_i
\rightarrow
Y_i
\rightarrow
P_i.
```

If the evidence cannot be connected to a hypothesis-relevant mechanism, baseline, output, parameter, or validation requirement, it may remain background literature but does not enter the demonstrator-construction evidence set.

---

## 21. Extraction quality-control procedure

1. **Pilot the extraction form** on papers covering all five hypotheses and multiple model families; revise ambiguous definitions, then freeze the codebook.
2. **Extract every priority paper at evidence-unit level**, preserving raw notation and exact locations.
3. **Duplicate all critical fields independently** where feasible: mechanism, equation, variables, parameters, assumptions, validation evidence, quantitative outputs.
4. **Compare extracts before discussion** and retain both raw records.
5. **Resolve discrepancies from the paper itself**, not memory; if unresolved, use adjudication or `UNRESOLVED`.
6. **Freeze a consensus extraction** while preserving raw versions and the disagreement log.
7. **Run equation-specific audit:** notation, units, IC/BC, assumptions, parameter provenance, domain, mathematical consistency.
8. **Run VVUQ audit:** verification, validation referent, calibration independence, uncertainty sources, numerical error, model limitations.
9. **Map to $H_1$–$H_5$ only after raw source extraction is complete** so thesis notation does not contaminate source extraction.
10. **Assign final evidence-use classes** and retain excluded evidence units with explicit reasons.

If only one human extractor is available, a time-separated second extraction plus supervisor/expert verification of critical equations is an acceptable practical fallback but is weaker than independent duplicate extraction.

---

## 22. Evidence-use decision classes

| Status | Meaning |
|---|---|
| **MODEL-CANDIDATE** | mechanism + mathematical form + adequate traceability; eligible for candidate demonstrator |
| **MODEL-CANDIDATE-CONDITIONAL** | useful model but adaptation/validation/domain issue unresolved |
| **MECHANISM-EVIDENCE** | supports causal mechanism but not a specific equation |
| **PARAMETER-EVIDENCE** | supports parameter/range/distribution only |
| **VALIDATION-EVIDENCE** | provides benchmark/data/referent for validation |
| **BASELINE-EVIDENCE** | supplies competing model or conventional baseline |
| **BACKGROUND-ONLY** | scientifically relevant but does not operationalize current hypotheses |
| **UNUSABLE-FOR-MODELING** | insufficient traceability, inaccessible definition, irreconcilable inconsistency, or domain mismatch |

Different evidence units from the same paper may receive different roles.

---

## 23. Missingness rules

Never encode missingness as zero:

```math
NR\neq0.
```

Use distinct codes:

```math
NR=\text{not reported},
\quad
NA=\text{not applicable},
\quad
UC=\text{unclear/cannot determine},
\quad
UNR=\text{unresolved discrepancy}.
```

Thus

```math
\text{parameter not reported}
\neq
\text{parameter equal to zero}.
```

---

## 24. No silent equation completion

If a source reports

```math
\dot x=f(x,u)
```

but does not define $f$, record

```math
F=\text{functional form unspecified}.
```

Do not reconstruct $f$ from another source or from thesis reasoning inside the same raw evidence unit. If a second source provides the form, retain separate evidence units and document later synthesis:

```math
e_A\oplus e_B\rightarrow F_{\rm candidate}.
```

---

## 25. Model synthesis occurs after extraction

The fundamental separation is

```math
\underbrace{\text{source extraction}}_{\text{what literature says}}
\neq
\underbrace{\text{model synthesis}}_{\text{what thesis constructs}}.
```

Only after source evidence is frozen should the thesis construct

```math
F_{\mathcal G}^{\rm thesis}
=
\mathcal S(F_1,F_2,\ldots,F_n).
```

Each synthesized component then receives `[E]`, `[D]`, or `[P]` scientific status.

---

## 26. Required FTEE outputs

| Output | Purpose |
|---|---|
| **Master Evidence Ledger** | one row per evidence unit |
| **Mechanism Registry** | supported causal P–T–I–O mechanisms |
| **Equation Registry** | candidate mathematical forms |
| **Variable/Parameter Dictionary** | symbols, meanings, units, ranges and sources |
| **Assumption Registry** | explicit/inferred modeling assumptions |
| **Validation Registry** | referents, metrics, domains and discrepancies |
| **Uncertainty Registry** | uncertainty sources and treatments |
| **Hypothesis Evidence Matrix** | evidence supporting $H_1$–$H_5$ components |
| **Conflict/Disagreement Log** | unresolved or reconciled extraction conflicts |
| **Candidate-Model Ledger** | equations/mechanisms eligible for demonstrator design |

The extraction phase ends **before choosing the demonstrator**.

---

## 27. Formal evidence-unit acceptance gate

An evidence unit enters candidate model construction only when

```math
Q_E(e_{ij})=1.
```

**Equation FTEE-5 — Evidence-unit acceptance gate**

```math
Q_E
=
Q_{\rm provenance}
\land
Q_{\rm mechanism}
\land
Q_{\rm interpretation}
\land
Q_{\rm domain}
\land
Q_{\rm hypothesis}.
```

with

```math
\begin{aligned}
Q_{\rm provenance}&=1 &&\text{if exact source/location is recorded},\\
Q_{\rm mechanism}&=1 &&\text{if the modeled mechanism is identifiable},\\
Q_{\rm interpretation}&=1 &&\text{if source fact and thesis inference are separated},\\
Q_{\rm domain}&=1 &&\text{if applicability/limitations are documented},\\
Q_{\rm hypothesis}&=1 &&\text{if evidence has a defined role in }H_1-H_5.
\end{aligned}
```

Validation evidence is not required for every evidence unit. Foundational mechanism papers may remain useful even when $E_V$ is low. Validation adequacy is assessed at the candidate-model level.

---

## 28. Higher gate for governing equations

**Equation FTEE-6 — Governing-model acceptance gate**

```math
Q_F(F_j)
=
Q_E
\land
Q_{\rm variables}
\land
Q_{\rm assumptions}
\land
Q_{\rm parameters}
\land
Q_{\rm mathematical}
\land
Q_{\rm credibility}.
```

If any required component fails, the equation may remain in the registry but is labeled

```math
\mathrm{MODEL\mbox{-}CANDIDATE\mbox{-}CONDITIONAL}.
```

This places model-credibility requirements inside evidence extraction rather than postponing them until after implementation.

---

## 29. Final FTEE logic

```math
\begin{aligned}
P_i
&\rightarrow e_{ij}
\rightarrow M_{ij}
\rightarrow F_{ij}\\
&\rightarrow(X,\theta,A,\Omega)
\rightarrow(V,U)
\rightarrow H_k\\
&\rightarrow Q_E
\rightarrow Q_F
\rightarrow\text{candidate demonstrator component}.
\end{aligned}
```

The methodological boundary is

```math
\textbf{FTEE extracts and qualifies evidence; it does not yet choose the demonstrator.}
```

Demonstrator choice follows only after deriving

```math
\mathfrak M_{\rm required}
=
\bigcup_{i=1}^{5}\mathfrak M(H_i)
```

from the completed evidence base.

---

## Protocol status

FTEE v1.0 is sufficiently specified to be **piloted**. It is not yet frozen. The next action is to create the actual **Evidence-to-Equation extraction table/codebook**, pilot it on a deliberately heterogeneous subset of ranked papers spanning $H_1$–$H_5$ and multiple model types, resolve ambiguities, and then freeze FTEE before full-text extraction begins.