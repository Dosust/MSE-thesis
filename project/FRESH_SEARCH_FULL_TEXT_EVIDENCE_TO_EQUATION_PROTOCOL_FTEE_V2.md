# Fresh-Search Full-Text Evidence-to-Equation Protocol — FTEE v2.0

![Status](https://img.shields.io/badge/status-CURRENT%20WORKING%20PROTOCOL-0969DA)
![Search](https://img.shields.io/badge/evidence%20search-DE%20NOVO-1A7F37)
![Old Corpus](https://img.shields.io/badge/325--paper%20corpus-COVERAGE%20AUDIT%20ONLY-9A6700)
![Freeze](https://img.shields.io/badge/FTEE%20v2.0-NOT%20YET%20FROZEN-9A6700)

**Status:** CURRENT WORKING PROTOCOL / NOT YET FROZEN  
**Purpose:** de novo evidence discovery, screening, full-text evidence-to-equation extraction, and traceable support for demonstrator design  
**Primary evidence rule:** prior memory, historical corpora, and earlier rankings are not inclusion criteria  
**Historical-corpus rule:** the frozen 325-paper corpus is secondary coverage-audit material only after the fresh corpus is constructed  
**Citation standard:** APA 7th edition  
**Version-control rule:** FTEE v1.0 is superseded for active methodology; its Git history remains provenance.

## 0. Governing principle

The evidence base for the confirmatory hypotheses and demonstrator shall be reconstructed **de novo**.

```math
\boxed{ \textbf{No paper enters because it is remembered, previously ranked, or belonged to an earlier corpus.} }
```

A paper becomes admissible evidence only through:

```math
\boxed{ \text{new reproducible search} \rightarrow \text{eligibility screening} \rightarrow \text{full-text qualification}. }
```

Therefore:

```math
\boxed{ P_{\rm known}\equiv P_{\rm unknown} }
```

with respect to discovery, screening, and evidence qualification.

The previous 325-paper corpus is **not**:

- a search universe;
- a seed list;
- a source of automatic inclusions;
- a source of ranking weights;
- a reason to retain a paper;
- evidence of relevance by itself.

It may be used only **after the fresh evidence corpus has been constructed** for secondary coverage diagnostics.

---

## 1. Complete research pipeline

The revised order is:

**Equation FTEE-0**

```math
\boxed{ \begin{aligned} &H_1-H_5 \\ &\downarrow \\ &\text{mechanism decomposition} \\ &\downarrow \\ &\textbf{fresh systematic search from zero} \\ &\downarrow \\ &\text{deduplication} \\ &\downarrow \\ &\text{title/abstract screening} \\ &\downarrow \\ &\text{full-text eligibility} \\ &\downarrow \\ &\mathcal P_{\rm eligible}^{\rm NEW} \\ &\downarrow \\ &\textbf{FTEE extraction} \\ &\downarrow \\ &\mathfrak M_{\rm required} \\ &\downarrow \\ &\text{candidate demonstrators} \\ &\downarrow \\ &\text{V\&V + identifiability + UQ gates} \\ &\downarrow \\ &\boxed{\mathcal M_D^\star}. \end{aligned} }
```

Only after this sequence may we compare:

```math
\boxed{ \mathcal P_{\rm eligible}^{\rm NEW} \leftrightarrow \mathcal P_{325} }
```

as a coverage audit.

---

## 2. Scientific objective

Let the newly eligible corpus be

```math
\boxed{ \mathcal P_{\rm eligible}^{\rm NEW} = \{P_1,\ldots,P_N\}. }
```

The purpose of FTEE is to transform each eligible paper into traceable **evidence units**, not paper summaries.

For each `P_i`:

**Equation FTEE-1**

```math
\boxed{ e_{ij} = ( S_i,L_{ij},C_{ij},M_{ij},F_{ij},X_{ij}, \theta_{ij},A_{ij},\Omega_{ij},V_{ij},U_{ij},H_{ij} ) }
```

with

```math
\begin{aligned} S_i &= \text{source identity},\\ L_{ij} &= \text{exact source location},\\ C_{ij} &= \text{scientific claim},\\ M_{ij} &= \text{mechanism},\\ F_{ij} &= \text{mathematical representation},\\ X_{ij} &= \text{states/inputs/outputs},\\ \theta_{ij} &= \text{parameters},\\ A_{ij} &= \text{assumptions},\\ \Omega_{ij} &= \text{domain/boundary conditions},\\ V_{ij} &= \text{verification/validation evidence},\\ U_{ij} &= \text{uncertainty information},\\ H_{ij} &= \text{relationship to }H_1-H_5. \end{aligned}
```

One paper can yield:

```math
\boxed{ P_i \rightarrow \{e_{i1},e_{i2},\ldots,e_{im}\}. }
```

This retains the strongest feature of v1.0: the extraction unit is an **evidence unit rather than the whole paper**.

---

## 3. Methodological foundations

The protocol combines:

```math
\boxed{ \text{systematic evidence discovery} + \text{full-text extraction} + \text{physics/mathematical audit} + \text{VVUQ} + \text{hypothesis traceability}. }
```

The governing principles remain:

```math
\boxed{ \text{traceability} + \text{source fidelity} + \text{VVUQ separation} + \text{explicit uncertainty} + \text{hypothesis relevance}. }
```

These principles were already established in v1.0.

The major change is that **systematic evidence discovery now precedes FTEE**.

---

## 4. Fresh-search independence lock

Before searching, impose:

```math
\boxed{ \mathcal P_{\rm prior} \not\rightarrow \mathcal P_{\rm NEW}. }
```

Do not use:

- remembered titles;
- remembered authors;
- remembered DOIs;
- the 325-paper list;
- older 207/259/164/141/76 collections;
- earlier paper rankings;
- previous inclusion decisions;

to populate the new evidence corpus.

Search concepts must derive from:

```math
\boxed{ H_i \rightarrow \text{scientific mechanism} \rightarrow \text{concept blocks} \rightarrow \text{search terms}. }
```

Not:

```math
\boxed{ \text{known paper} \rightarrow \text{query designed to recover it}. }
```

This is the principal protection against literature-selection confirmation bias.

---

## 5. Hypothesis-first search decomposition

The five confirmatory hypotheses define five search families:

```math
\boxed{ \mathcal S = \{ S_{H_1},S_{H_2},S_{H_3},S_{H_4},S_{H_5} \}. }
```

### `H_1`: Dynamic interdependency

Search concepts must cover:

```math
\boxed{ P + T + \text{interdependency/coupling} + \text{dynamic propagation/cascade}. }
```

Scientific target:

```math
\mathfrak I \rightarrow F_{\mathcal G}.
```

### `H_2`: Information–organization

Concepts:

```math
\boxed{ \text{infrastructure} + \text{information/observation/estimation} + \text{organization/coordination/resources} + \text{response/control/recovery}. }
```

Target:

```math
(I,O) \rightarrow (\widehat X,\mathcal U,u) \rightarrow Y.
```

### `H_3`: Controlled viability

Concepts:

```math
\boxed{ \text{infrastructure} + \text{viability/reachability/invariance} + \text{control} + \text{resilience/safety/constraints}. }
```

Target:

```math
(F,\mathcal U) \rightarrow \mathcal V.
```

### `H_4`: Interface criticality

Concepts:

```math
\boxed{ \text{interdependent infrastructure} + \text{interface/dependency} + \text{sensitivity/criticality/importance} + \text{intervention}. }
```

Target:

```math
\mathfrak I \rightarrow S_{ij}^{\mathcal V} \rightarrow \Delta\mathcal V.
```

### `H_5`: Adaptive transformation

Concepts:

```math
\boxed{ \text{infrastructure} + \text{adaptive pathways/robust decision} + \text{deep uncertainty} + \text{transformation/planning}. }
```

Target:

```math
\mathcal V \rightarrow \Phi_{\rm ST} \rightarrow \mathfrak P_{\rm ST}.
```

---

## 6. Mechanism-first search rule

Do not design search strings around our preferred proposed mathematical objects.

For example, do **not** search only:

```math
S_{ij}^{\mathcal V}.
```

Instead search the broader phenomenon:

```math
\boxed{ \text{interface} + \text{criticality} + \text{sensitivity} + \text{failure propagation} + \text{intervention}. }
```

This allows the evidence to reveal competing mathematical approaches such as:

```math
\text{centrality}, \quad \text{fragility}, \quad \text{sensitivity}, \quad \text{controllability}, \quad \text{reachability},
```

rather than forcing our own construct onto the literature.

---

## 7. Search sources

The primary engineering evidence search should use multiple bibliographic databases.

Recommended core:

```math
\boxed{ \text{Scopus} \cup \text{Web of Science} \cup \text{Compendex} \cup \text{IEEE Xplore}. }
```

Additional specialized databases may be added where a hypothesis requires them.

The search record must contain:

**Equation FTEE-2**

```math
\boxed{ ( \text{database}, \text{platform}, \text{query}, \text{fields}, \text{filters}, \text{date}, N_{\rm returned} ) }
```

for every search.

No database result may be silently added without a recorded query.

---

## 8. Time-window rule

The default search interval should be:

```math
\boxed{ \text{database inception} \rightarrow \text{final search date}. }
```

No arbitrary 2022–2026 restriction should be applied to mathematical or physics foundations.

Older work may be essential for:

- viability theory;
- reachability;
- power-flow theory;
- traffic dynamics;
- cascading failure;
- network interdependency;
- control;
- robust decision making.

A narrower year restriction may be introduced only if the scientific rationale is documented beforehand.

---

## 9. Search routes

Construct the discovery set from three routes:

**Equation FTEE-3**

```math
\boxed{ \mathcal P_{\rm discovered} = \mathcal P_{\rm database} \cup \mathcal P_{\rm backward} \cup \mathcal P_{\rm forward}. }
```

But sequence them rigorously:

```math
\boxed{ \text{database search first} \rightarrow \text{eligible anchor papers} \rightarrow \text{citation chasing}. }
```

Backward and forward searching should not use remembered papers as initial anchors.

---

## 10. Search-version control

Each query receives an immutable identifier:

```math
\boxed{ Q_{H_i,d}^{(v)} }
```

where:

- `H_i` = hypothesis;
- `d` = database;
- `v` = query version.

Example:

```text
H1_SCOPUS_Q01_v1
H1_COMPEDEX_Q01_v1
H2_IEEE_Q03_v2
```

If a search is modified:

```math
Q^{(v)} \rightarrow Q^{(v+1)}
```

both versions remain in the audit log.

Never overwrite an earlier query.

---

## 11. Search sensitivity pilot

Before freezing the search strings, test whether each query retrieves papers that clearly represent the **scientific concepts**, not specific remembered publications.

Pilot questions:

```math
\boxed{ \begin{aligned} &\text{Does the query retrieve relevant mechanisms?}\\ &\text{Does it retrieve multiple modeling traditions?}\\ &\text{Is one concept block dominating?}\\ &\text{Are obvious terminology variants missing?}\\ &\text{Is precision so poor that screening becomes unmanageable?} \end{aligned} }
```

Revise the concept vocabulary based on terminology found in search results, while preserving a change log.

---

## 12. Eligibility protocol

Before substantive screening, define:

```math
I(P)= \begin{cases} 1,&\text{eligible},\\ 0,&\text{excluded}. \end{cases}
```

Primary inclusion requires that the paper contribute to at least one of:

```math
\boxed{ \text{mechanism}, \text{mathematical model}, \text{parameterization}, \text{benchmark}, \text{validation}, \text{baseline}, \text{UQ}, \text{transformation method}. }
```

A paper does not have to supply all of these.

---

## 13. Inclusion categories

Use explicit eligibility roles:

```math
\boxed{ \mathcal R_P \in \{ R_M,R_F,R_\theta,R_V,R_B,R_U,R_T \} }
```

where:

```math
\begin{aligned} R_M &= \text{mechanism evidence},\\ R_F &= \text{mathematical-form evidence},\\ R_\theta &= \text{parameter evidence},\\ R_V &= \text{validation/benchmark evidence},\\ R_B &= \text{baseline/comparator evidence},\\ R_U &= \text{uncertainty/VVUQ evidence},\\ R_T &= \text{transformation/pathway evidence}. \end{aligned}
```

This avoids excluding important theoretical papers merely because they contain no field dataset.

---

## 14. Exclusion reasons

Every full-text exclusion receives one primary coded reason.

For example:

```math
\boxed{ \begin{aligned} EX01 &: \text{wrong system/domain},\\ EX02 &: \text{no relevant mechanism},\\ EX03 &: \text{no relevant mathematics/methodology},\\ EX04 &: \text{insufficient technical detail},\\ EX05 &: \text{duplicate report},\\ EX06 &: \text{not transferable to research question},\\ EX07 &: \text{not retrievable in assessable full text},\\ EX08 &: \text{publication type not eligible}. \end{aligned} }
```

Do not invent a new exclusion reason after looking at an undesirable result without documenting the protocol amendment.

---

## 15. PRISMA accounting

Track:

```math
N_{\rm identified} \rightarrow N_{\rm deduplicated} \rightarrow N_{\rm screened} \rightarrow N_{\rm fulltext} \rightarrow N_{\rm eligible}.
```

Also track separately:

```math
N_{\rm backward}, \qquad N_{\rm forward}.
```

This fresh search may legitimately be called a PRISMA-style or systematic evidence search only to the degree that the actual search protocol meets those requirements.

---

## 16. Deduplication gate

Use hierarchical identity matching:

```math
\boxed{ \text{DOI} \rightarrow \text{database identifier} \rightarrow \text{normalized title} \rightarrow \text{manual adjudication}. }
```

Never automatically merge two records solely on fuzzy-title similarity when author/year/DOI evidence conflicts.

Every merge should preserve:

```math
\boxed{ \text{all source records} \rightarrow \text{one canonical study record}. }
```

---

## 17. Screening independence

Where feasible:

```math
\boxed{ \text{Reviewer A} \perp \text{Reviewer B}. }
```

Independent screening should be used especially for:

- full-text eligibility;
- mechanism relevance;
- equation/model qualification.

Disagreement resolution must be documented.

If only one primary researcher is available, use a second time-separated screening plus supervisor/expert audit for critical decisions and report this limitation explicitly.

---

## 18. Fresh eligible corpus

Only after screening do we define:

```math
\boxed{ \mathcal P_{\rm eligible}^{\rm NEW}. }
```

This is the sole primary input to FTEE.

No paper may enter FTEE directly from:

```math
\mathcal P_{325}, \quad \mathcal P_{259}, \quad \mathcal P_{207},
```

unless independently rediscovered and newly eligible.

---

## 19. FTEE extraction schema

The seven extraction blocks from v1.0 remain valid.

| Block | Required information |
|---|---|
| **A. Provenance** | EvidenceUnitID, PaperID, DOI, title, year, file, page, section, equation/table/figure |
| **B. Scientific role** | hypothesis, scientific question, mechanism type, infrastructure layer |
| **C. Mechanism** | source state, mechanism, receiving state, effect, direction, delay, mode/history |
| **D. Mathematics** | raw equation, family, variables, parameters, constraints, IC/BC, units, timescale, solver |
| **E. Domain** | assumptions, parameter ranges, system scale, topology, hazard, operating regime |
| **F. Credibility** | calibration, verification, validation referent, errors, sensitivity, UQ |
| **G. Thesis transfer** | mapping into `P,T,I,O`, adaptation required, evidence role, inclusion status |

---

## 20. Exact provenance requirement

No equation enters the model registry unless we know:

```math
\boxed{ \text{PaperID} + \text{page} + \text{section} + \text{equation/table/figure identifier}. }
```

This requirement from v1.0 remains unchanged.

Use evidence IDs such as:

```text
NEW-H1-P004-EQ02
NEW-H2-P017-MECH03
NEW-H3-P011-VAL01
```

---

## 21. Source notation lock

Always preserve:

```math
\boxed{ F_{\rm source} }
```

before constructing:

```math
\boxed{ F_{\rm thesis}. }
```

If a source gives

```math
\dot z_i=f_i(z_i,z_j,\lambda_{ij}),
```

store that exact form first.

Then define separately:

```math
\phi_i: (z_i,z_j,\lambda_{ij}) \mapsto (E_i^\alpha,E_j^\beta,w_{ij}).
```

Thus:

```math
\boxed{ F_{\rm thesis} = \mathcal T_{\rm map}(F_{\rm source}). }
```

This separation is already correctly established in v1.0 and must remain.

---

## 22. Provenance classes

Retain:

```math
\boxed{ \{R,C,T,P\}. }
```

| Class | Meaning |
|---|---|
| **R** | reported explicitly |
| **C** | calculated/reconstructed |
| **T** | transferred/adapted |
| **P** | proposed by thesis |

Keep this independent from:

```math
[E],[D],[P].
```

The two classifications answer different questions:

```math
\boxed{ \text{Where did the mathematical object come from?} }
```

versus

```math
\boxed{ \text{What is its scientific status?} }
```

---

## 23. Mechanism-first extraction

Before equations, determine:

```math
\boxed{ \text{Source} \rightarrow \text{Mechanism} \rightarrow \text{Receiver} \rightarrow \text{Effect}. }
```

Map interdependency evidence where appropriate to:

```math
\boxed{ \mathfrak I_{ij}^{\alpha\beta} = ( E_i^\alpha, E_j^\beta, M_{ij}, w_{ij}, \delta_{ij}, \tau_{ij}, a_{ij}, m, \mathcal H_t ). }
```

Every field is:

```math
\{\text{reported},\text{NR},\text{NA},\text{UC}\}.
```

Do not fill missing terms from framework expectations.

---

## 24. Separate mechanism, mathematical-form and validation evidence

Retain:

```math
\boxed{ E_M,\qquad E_F,\qquad E_V. }
```

The attached protocol correctly emphasizes that these must not be collapsed into one number.

Use:

| Level | Mechanism $E_M$ | Mathematical form $E_F$ | Validation $E_V$ |
|---:|---|---|---|
| 0 | absent | absent | absent |
| 1 | indirect | referenced/implicit | qualitative/internal |
| 2 | explicit | completely specified | benchmark/calibration comparison |
| 3 | directly investigated | full specification + domain | independent quantitative validation |

Preserve:

```math
\boxed{ (E_M,E_F,E_V) }
```

rather than inventing:

```math
w_ME_M+w_FE_F+w_VE_V.
```

---

## 25. Equation extraction object

For every mathematical model:

**Equation FTEE-4**

```math
\boxed{ \mathcal E_{ij} = ( F_{\rm raw}, X,U,\theta,A,B,IC,BC,\Omega,N ) }
```

with:

```math
\begin{aligned} X&=\text{states},\\ U&=\text{inputs/controls},\\ \theta&=\text{parameters},\\ A&=\text{algebraic constraints},\\ B&=\text{physical bounds},\\ IC&=\text{initial conditions},\\ BC&=\text{boundary conditions},\\ \Omega&=\text{application domain},\\ N&=\text{numerical method}. \end{aligned}
```

Fundamental rule:

```math
\boxed{ \text{equation without assumptions/domain} \neq \text{fully extracted model}. }
```

This is retained directly from the earlier protocol.

---

## 26. Dimensional and physical audit

For every variable/parameter record:

```math
\boxed{ \text{name} + \text{symbol} + \text{meaning} + \text{unit} + \text{normalization}. }
```

Check:

```math
\boxed{ [\mathrm{LHS}]=[\mathrm{RHS}]. }
```

If dimensions cannot be established:

```math
\texttt{UNIT\_STATUS=UC}.
```

Do not silently assign units.

---

## 27. Parameter extraction

For each:

```math
\theta_k
```

store:

**Equation FTEE-5**

```math
\boxed{ \Theta_k = ( \text{nominal value}, \text{unit}, \text{source location}, \text{range/distribution}, \text{estimation/calibration method} ). }
```

Distinguish:

```math
\boxed{ \text{reported parameter} \neq \text{estimated parameter} \neq \text{assumed parameter}. }
```

No uncertainty distribution may be fabricated.

---

## 28. Timescale extraction

Record where applicable:

```math
\boxed{ \boldsymbol\tau = [ \tau^{op}, \tau^{dist}, \tau^{prop}, \tau^{ctrl}, \tau^{rec}, \tau^{adapt} ]. }
```

Keep:

```math
\boxed{ \text{physical timescale} \neq \text{numerical timestep}. }
```

The earlier protocol correctly requires this distinction.

---

## 29. Assumption registry

For each evidence unit:

```math
\boxed{ A= A_{\rm explicit} \cup A_{\rm mathematical} \cup A_{\rm physical} \cup A_{\rm numerical}. }
```

If an assumption is inferred by the extractor:

```text
ExtractorInference = TRUE
```

and provide justification.

Never present an extractor inference as something the authors stated.

---

## 30. VVUQ extraction

Keep distinct:

```math
\boxed{ \text{code verification} }
```

```math
\boxed{ \text{solution verification} }
```

```math
\boxed{ \text{calibration} }
```

```math
\boxed{ \text{validation} }
```

```math
\boxed{ \text{sensitivity analysis} }
```

```math
\boxed{ \text{uncertainty quantification}. }
```

In particular:

```math
\boxed{ \text{calibration}\neq\text{validation}. }
```

The attached v1.0 already establishes this separation and it remains unchanged.

---

## 31. Validation object

For each validation claim:

**Equation FTEE-6**

```math
\boxed{ V= ( R,D_{\rm cal},D_{\rm val}, M_V,\varepsilon_V,\Omega_V ) }
```

where:

```math
\begin{aligned} R &= \text{validation referent},\\ D_{\rm cal} &= \text{calibration dataset},\\ D_{\rm val} &= \text{validation dataset},\\ M_V &= \text{validation metric},\\ \varepsilon_V &= \text{reported discrepancy},\\ \Omega_V &= \text{demonstrated validation domain}. \end{aligned}
```

Later require:

```math
\boxed{ \Omega_H\subseteq\Omega_V }
```

or explicitly label use outside `\Omega_V` as extrapolation.

---

## 32. Uncertainty extraction

For every model:

```math
\boxed{ U= \{ U_\theta, U_{\rm IC}, U_D, U_M, U_N, U_h \}. }
```

where:

```math
\begin{aligned} U_\theta &= \text{parameter},\\ U_{\rm IC} &= \text{initial-condition},\\ U_D &= \text{data/measurement},\\ U_M &= \text{model-form},\\ U_N &= \text{numerical},\\ U_h &= \text{hazard/scenario}. \end{aligned}
```

For each uncertainty:

```math
\boxed{ \text{source} + \text{type} + \text{representation} + \text{propagation} + \text{output effect}. }
```

Missing uncertainty reporting is:

```math
U=\text{NR},
```

not `U=0`.

---

## 33. Transferability assessment

For each evidence unit:

```math
\boxed{ T_{ij} \in \{ \text{Direct}, \text{Conditional}, \text{Conceptual}, \text{Not transferable} \}. }
```

This classification remains useful exactly as defined in v1.0.

But **transferability is assessed only after raw source extraction**.

We must avoid reading the paper through the lens of the desired thesis model.

---

## 34. Hypothesis mapping occurs after extraction

This is a particularly important correction.

The raw extraction sequence is:

```math
\boxed{ P_i \rightarrow e_{ij}^{\rm raw}. }
```

Only afterwards:

```math
\boxed{ e_{ij}^{\rm raw} \rightarrow H_k. }
```

Do not pre-label passages as belonging to `H_1`, `H_2`, etc. before extracting what they actually say.

This maintains:

```math
\boxed{ \text{source interpretation} \perp \text{desired hypothesis support}. }
```

The v1.0 quality-control procedure already recommended mapping to `H_1-H_5` after source extraction; retain this rule.

---

## 35. Rival and contrary evidence

FTEE v2.0 should explicitly add something v1.0 did not emphasize enough:

```math
\boxed{ \textbf{extract evidence against our hypothesis as carefully as evidence supporting it.} }
```

For every evidence unit include:

```text
Relation_to_Hypothesis =
SUPPORTIVE
CONTRADICTORY
NULL_OR_NEGLIGIBLE
CONDITIONAL
NOT_APPLICABLE
```

For example, a study showing:

```math
\text{dynamic coupling} \approx \text{static coupling}
```

under some domain is scientifically valuable for `H_1`.

Do not classify it as low relevance because it contradicts the expected hypothesis.

---

## 36. Baseline extraction

Every paper should be checked for competing models or baselines.

Record:

```math
\boxed{ B_{ij} = \text{baseline/comparator used by source}. }
```

Examples:

```math
\text{uncoupled}, \quad \text{static coupling}, \quad \text{centrality ranking}, \quad \text{fixed policy}.
```

This is essential because our confirmatory hypotheses depend on discriminatory comparisons, not only preferred models.

---

## 37. Evidence-use classes

Retain:

- `MODEL-CANDIDATE`
- `MODEL-CANDIDATE-CONDITIONAL`
- `MECHANISM-EVIDENCE`
- `PARAMETER-EVIDENCE`
- `VALIDATION-EVIDENCE`
- `BASELINE-EVIDENCE`
- `BACKGROUND-ONLY`
- `UNUSABLE-FOR-MODELING`

One paper may produce multiple evidence units with different classifications.

---

## 38. Missingness

Retain explicit:

```math
\boxed{ NR=\text{not reported}, }
```

```math
\boxed{ NA=\text{not applicable}, }
```

```math
\boxed{ UC=\text{unclear}, }
```

```math
\boxed{ UNR=\text{unresolved disagreement}. }
```

And enforce:

```math
\boxed{ NR\neq0. }
```

The earlier protocol correctly makes this distinction.

---

## 39. No silent model completion

If the source states:

```math
\dot x=f(x,u)
```

but does not specify `f`, record exactly:

```math
\boxed{ F=\text{functional form unspecified}. }
```

Do not silently complete it using memory or another source.

If another source supplies the mathematical form:

```math
e_A\oplus e_B \rightarrow F_{\rm candidate}
```

must be explicitly documented as **model synthesis**, not raw extraction.

This distinction is already present in v1.0 and should remain fundamental.

---

## 40. Independent extraction quality control

Use this sequence:

```math
\boxed{ \text{pilot} \rightarrow \text{freeze codebook} \rightarrow \text{independent extraction} \rightarrow \text{comparison} \rightarrow \text{adjudication} \rightarrow \text{consensus freeze}. }
```

Critical fields requiring duplicate verification:

- mechanisms;
- equations;
- variable interpretation;
- parameters;
- assumptions;
- validation;
- uncertainty;
- quantitative outputs;
- hypothesis relationship.

Preserve original extractor records.

Never replace them with only the consensus version.

---

## 41. Extraction pilot

Before full extraction, choose a deliberately heterogeneous pilot set containing:

```math
\boxed{ \begin{aligned} &\text{one strong dynamics paper},\\ &\text{one information/organization paper},\\ &\text{one viability/reachability paper},\\ &\text{one intervention/criticality paper},\\ &\text{one adaptive-pathway paper},\\ &\text{one paper with weak/incomplete mathematical reporting}. \end{aligned} }
```

The purpose is to stress-test the **extraction form**, not the hypotheses.

After the pilot:

```math
\boxed{ \text{revise schema} \rightarrow \text{freeze FTEE codebook}. }
```

Then start production extraction.

---

## 42. Required registries

FTEE v2.0 produces:

```math
\boxed{ \begin{array}{l} \text{Search Registry}\\ \text{Screening Registry}\\ \text{Full-Text Exclusion Registry}\\ \text{Master Evidence Ledger}\\ \text{Mechanism Registry}\\ \text{Equation Registry}\\ \text{Variable/Parameter Dictionary}\\ \text{Assumption Registry}\\ \text{Validation Registry}\\ \text{Uncertainty Registry}\\ \text{Baseline/Rival Registry}\\ \text{Hypothesis Evidence Matrix}\\ \text{Conflict Log}\\ \text{Candidate-Model Ledger}. \end{array} }
```

The first three are new relative to the earlier FTEE formulation because we are now responsible for generating the evidence base from zero.

---

## 43. Evidence-unit acceptance gate

Retain:

```math
\boxed{ Q_E(e_{ij})=1 }
```

only if:

**Equation FTEE-7**

```math
\boxed{ Q_E = Q_{\rm provenance} \land Q_{\rm mechanism} \land Q_{\rm interpretation} \land Q_{\rm domain} \land Q_{\rm relevance}. }
```

where:

```math
\begin{aligned} Q_{\rm provenance}&=1 &&\text{exact source location known},\\ Q_{\rm mechanism}&=1 &&\text{scientific mechanism identifiable},\\ Q_{\rm interpretation}&=1 &&\text{source and inference separated},\\ Q_{\rm domain}&=1 &&\text{application limits recorded},\\ Q_{\rm relevance}&=1 &&\text{defined research role exists}. \end{aligned}
```

The early gate uses `Q_relevance` rather than `Q_hypothesis` because useful evidence may provide validation or a baseline without directly supporting one hypothesis.

---

## 44. Equation qualification gate

Retain the stronger governing-model gate:

**Equation FTEE-8**

```math
\boxed{ Q_F(F_j) = Q_E \land Q_{\rm variables} \land Q_{\rm assumptions} \land Q_{\rm parameters} \land Q_{\rm mathematical} \land Q_{\rm credibility}. }
```

Failure does not delete an equation.

It becomes:

```text
MODEL-CANDIDATE-CONDITIONAL
```

with the unresolved condition explicitly recorded.

---

## 45. Mechanism inventory

Only after production extraction is sufficiently complete do we define:

```math
\boxed{ \mathfrak M_i = \mathfrak M(H_i) }
```

and:

**Equation FTEE-9**

```math
\boxed{ \mathfrak M_{\rm required} = \bigcup_{i=1}^{5}\mathfrak M_i. }
```

This is the first point at which the literature evidence begins determining the demonstrator architecture.

Not before.

---

## 46. Evidence triangulation

Do not choose an equation merely because one paper reports it.

For important mechanisms, build:

```math
\boxed{ \mathcal E(M_j) = \{ e_{1j}, e_{2j}, \ldots \}. }
```

Then determine whether evidence converges on:

- mechanism existence;
- equation family;
- parameter range;
- validity domain;
- limitations.

The goal is not majority voting.

It is to understand:

```math
\boxed{ \text{where evidence agrees} + \text{where models differ} + \text{why}. }
```

---

## 47. Model-family comparison

When multiple mathematical forms represent the same mechanism:

```math
F_1,\quad F_2,\quad \ldots,\quad F_r,
```

do not immediately choose one.

Create:

```math
\boxed{ \mathcal F(M_j) = \{F_1,\ldots,F_r\}. }
```

Compare:

```math
\boxed{ \text{assumptions}, \text{fidelity}, \text{parameters}, \text{validation}, \text{computational cost}, \text{domain}, \text{hypothesis discrimination}. }
```

Only candidate-demonstrator qualification should select among them.

---

## 48. Old 325-paper corpus: new role

After the new evidence corpus has been frozen:

```math
\boxed{ \mathcal P_{\rm NEW} }
```

compare against:

```math
\mathcal P_{325}.
```

Compute conceptually:

```math
\boxed{ \mathcal P_{\rm overlap} = \mathcal P_{\rm NEW} \cap \mathcal P_{325}. }
```

And:

```math
\boxed{ \mathcal P_{\rm old-only} = \mathcal P_{325} \setminus \mathcal P_{\rm NEW}. }
```

But an old-only paper is **not automatically added**.

Instead assign a diagnostic:

```text
NOT_RECOVERED_QUERY_TERMINOLOGY
NOT_INDEXED_IN_SELECTED_DATABASES
OUTSIDE_CURRENT_ELIGIBILITY
DUPLICATE_REPORT
SEARCH_PROTOCOL_GAP
UNKNOWN
```

If an important old paper reveals a genuine query weakness:

```math
\boxed{ \text{repair search} \rightarrow \text{rerun systematically}, }
```

not:

```math
\boxed{ \text{manually insert remembered paper}. }
```

This is a major methodological safeguard.

---

## 49. Search saturation and stopping

Do not stop because:

> “we have enough papers.”

Stop according to a predefined rule involving:

- all planned databases executed;
- all query families executed;
- deduplication complete;
- specified backward/forward citation rounds complete;
- no unresolved search-protocol defects;
- final search update performed near analysis freeze.

The number of papers is an outcome, not a stopping target.

---

## 50. Search update before freeze

Because the thesis develops over time, perform a final update:

```math
\boxed{ t_0=\text{initial search} }
```

```math
\boxed{ t_1=\text{update search before evidence freeze}. }
```

The update must reuse the frozen search logic and document only the new time interval.

This prevents the literature base from becoming stale during a long modeling phase.

---

## 51. Complete scientific traceability

Every final demonstrator component must be traceable backwards:

**Equation FTEE-10**

```math
\boxed{ \mathcal M_D \leftarrow F_j \leftarrow e_{ij} \leftarrow P_i \leftarrow Q_d \leftarrow H_k. }
```

Thus for any model component we should be able to answer:

1. Which hypothesis requires it?
2. Which search found its evidence?
3. Why was the paper eligible?
4. Where exactly is the mechanism/equation reported?
5. What assumptions accompany it?
6. What evidence validates it?
7. What transformation did the thesis apply?

That is full auditability.

---

## 52. Final methodological architecture

The updated complete architecture is:

**Equation FTEE-11**

```math
\boxed{ \begin{aligned} H_i &\rightarrow \text{mechanism concepts} \\ &\rightarrow \text{fresh database search} \\ &\rightarrow \text{screening} \\ &\rightarrow P_i \\ &\rightarrow e_{ij} \\ &\rightarrow M_{ij} \\ &\rightarrow F_{ij} \\ &\rightarrow (X,\theta,A,\Omega) \\ &\rightarrow (V,U) \\ &\rightarrow \mathfrak M_{\rm required} \\ &\rightarrow \text{candidate demonstrators} \\ &\rightarrow \text{V\&V/UQ/identifiability gates} \\ &\rightarrow \boxed{\mathcal M_D^\star}. \end{aligned} }
```

---

## 53. Methodological boundary

The protocol must now state explicitly:

```math
\boxed{ \textbf{FTEE v2.0 does not start from a previously selected paper corpus.} }
```

Instead:

```math
\boxed{ \textbf{the evidence corpus itself is an output of the new research protocol.} }
```

And:

```math
\boxed{ \textbf{FTEE extracts and qualifies the newly discovered evidence; it does not choose the demonstrator.} }
```

The demonstrator is chosen only after:

```math
\mathfrak M_{\rm required}
```

has been established from that fresh evidence base.

---

## Methodological preservation note

This v2.0 file supersedes the active role previously assigned to the closed 325-paper ranking and to FTEE v1.0. It preserves the strongest v1.0 extraction controls—evidence-unit granularity, exact provenance, source-notation lock, mechanism/form/validation separation, VVUQ discipline, missingness codes, transferability assessment, no silent equation completion, and governing-equation qualification—while replacing the upstream evidence-selection logic with a de novo hypothesis-first search.

## 54. Final rule to freeze

The following is the formal non-negotiable methodological statement:

> **Fresh-evidence rule.** All primary scientific evidence used to operationalize the confirmatory hypotheses, select mathematical models, define mechanisms, determine parameters, identify validation benchmarks, or design the experimental demonstrator shall be identified through a new, documented and reproducible literature search constructed from the current hypotheses and scientific mechanisms. Prior memories, previous literature corpora and earlier rankings shall not constitute evidence-selection criteria. Previously known papers may contribute only if independently rediscovered and qualified under the new protocol. Historical corpora may subsequently be used for coverage auditing but shall not be used for automatic inclusion.

In mathematical form:

```math
\boxed{ \text{Hypotheses} \rightarrow \text{fresh evidence} \rightarrow \text{models}, }
```

never:

```math
\boxed{ \text{old models/papers} \rightarrow \text{evidence justification}. }
```

That is the **full methodological correction to FTEE v1.0**. The most important next task is now no longer piloting extraction on previously ranked papers; it is to build and freeze the **Fresh Literature Search Protocol for** **`H_1-H_5`**, beginning with `H_1`.
