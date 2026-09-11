# H1 Fresh Evidence Search Protocol — Frozen v1.0

![Status](https://img.shields.io/badge/status-FROZEN%20v1.0-1A7F37)
![Hypothesis](https://img.shields.io/badge/hypothesis-H1-0969DA)
![Search](https://img.shields.io/badge/search-DE%20NOVO-1A7F37)
![Execution](https://img.shields.io/badge/database%20execution-PENDING-9A6700)

**Status:** FROZEN FOR INITIAL EXECUTION  
**Hypothesis:** $H_1$ — dynamic causal power–transportation interdependency  
**Primary discovery rule:** $Q_{H_1}^{\rm CORE}=B_P\land B_T\land B_I$  
**Dynamic block:** diagnostic/tagging only; not a mandatory discovery filter  
**Databases:** Scopus, Web of Science Core Collection, Compendex, IEEE Xplore  
**Search interval:** database inception to 11 September 2026, subject to database/platform coverage  
**Version-control rule:** v1.0 is immutable after execution; any modification creates a new version with a reason-for-change record  
**Source-preservation rule:** scientific content is preserved from the supplied protocol; GitHub display structure, equation labels, and malformed table headers were normalized only.  
**Source SHA-256:** `aedf57f2fd0d4614ba57f5911a598c3a63b25e9f57c3d48a74e1fbf5325a1c59`

## 0. Freeze rationale

The first executable search protocol for $H_1$ is now frozen. A fresh sensitivity pilot was used to test whether the vocabulary retrieves the intended mechanism families without using the previous 325-paper corpus as the search universe.

A key methodological correction is that the fourth dynamic/cascade block is **not mandatory in the primary discovery query**. Requiring it could exclude static-coupling comparator studies and foundational coupling models that do not use resilience vocabulary. The primary discovery query therefore uses power + transportation + interdependency, while the dynamic block is retained as a diagnostic/tagging query. This prioritizes recall without abandoning the hypothesis.

---

## 1. Confirmatory target

```math
\boxed{H_1:\ \text{Explicit dynamic causal }P-T\text{ coupling produces materially different and more defensible cascade/service trajectories than independent or static-coupling representations.}}
```

The mechanism is

```math
\boxed{P\leftrightarrow T\rightarrow\mathfrak I_{PT}(t,Y,m)\rightarrow F_{\mathcal G}\rightarrow\{T_C,L_{\rm service},T_{\rm recovery},\ldots\}.}
```

The search must recover evidence for all three competing representations:

```math
\boxed{M_0=\text{independent},\qquad M_1=\text{static coupling},\qquad M_2=\text{dynamic causal coupling}.}
```

Searching only for `dynamic` or `cascading` is therefore scientifically too restrictive.

---

## 2. Search architecture

The primary discovery query is

**Equation H1-Q1 — Core discovery query**

```math
\boxed{Q_{H_1}^{\rm CORE}=B_P\land B_T\land B_I.}
```

A fourth block is retained for diagnostic classification:

**Equation H1-Q2 — Dynamic diagnostic query**

```math
\boxed{Q_{H_1}^{\rm DYN}=B_P\land B_T\land B_I\land B_D\subseteq Q_{H_1}^{\rm CORE}.}
```

Therefore:

- `CORE` constructs the candidate evidence corpus;
- `DYN` identifies records explicitly advertising dynamic/cascade/recovery behavior;
- CORE records absent from DYN are **not discarded**.

This prevents

```math
\boxed{\text{search terminology}\rightarrow\text{premature scientific exclusion}.}
```

---

## 3. Frozen concept block `B_P`: electrical power infrastructure

```text
"power system*"
OR "electric power system*"
OR "electrical power system*"
OR "power grid*"
OR "electric grid*"
OR "electrical grid*"
OR "electricity grid*"
OR "power network*"
OR "electricity network*"
OR "power distribution system*"
OR "power distribution network*"
OR "distribution grid*"
```

Generic `energy system*` is deliberately excluded from v1.0 because it would introduce gas, thermal, petroleum, and other non-electric systems.

No specific power technology is required. Therefore

```math
P_G,\;P_{Tr},\;P_D,\;P_{DER},\;P_C,\;P_{TP}
```

can all potentially be recovered.

---

## 4. Frozen concept block `B_T`: transportation infrastructure

```text
"transportation system*"
OR "transport system*"
OR "transportation network*"
OR "transport network*"
OR "road transportation"
OR "road network*"
OR "traffic network*"
OR "traffic system*"
OR "intelligent transportation system*"
OR "electrified transportation"
OR "electric vehicle*"
OR "electric mobility"
OR "e-mobility"
OR railway*
OR "rail transit"
OR subway*
OR metro*
```

The search is deliberately not restricted to EVs. Otherwise, the demonstrator would be implicitly preselected before the evidence establishes whether EV-mediated coupling should dominate the model.

---

## 5. Frozen interdependency block `B_I`

```text
interdependen*
OR coupled
OR coupling
OR integrat*
OR interaction*
OR "cross-system"
OR "cross-network"
OR multilayer
OR "multi-layer"
OR bidirectional
OR "bi-directional"
```

This spans several terminology traditions:

```math
\boxed{\text{interdependency}\cup\text{coupling}\cup\text{integration}\cup\text{interaction}\cup\text{multilayer representation}.}
```

Generic `dependen*` is intentionally avoided because it is too nonspecific.

---

## 6. Diagnostic dynamic/mechanism block `B_D`

```text
dynam*
OR tempor*
OR spatiotemporal
OR "spatio-temporal"
OR "time-varying"
OR "time varying"
OR "time-dependent"
OR "time dependent"
OR "state-dependent"
OR "state dependent"
OR cascade*
OR propagat*
OR disrupt*
OR failur*
OR outage*
OR resilience
OR recover*
OR restor*
OR vulnerab*
OR static
OR topolog*
```

`static` and `topolog*` are intentionally retained because $M_1$ is a legitimate rival representation.

---

## 7. Frozen master query

Conceptually:

```text
(
    B_P
)
AND
(
    B_T
)
AND
(
    B_I
)
```

The primary discovery query is **not**

```text
B_P AND B_T AND B_I AND B_D
```

because the fourth block is diagnostic rather than exclusionary.

---

## 8. Scopus — executable translation

Use **Advanced Search**, not semantic search.

Scopus supports `TITLE-ABS-KEY`, Boolean operators, and proximity operators. The strategy is intentionally split into auditable concept blocks.

### `H1_SCOPUS_BP_v1`

```text
TITLE-ABS-KEY(
    "power system*" OR
    "electric power system*" OR
    "electrical power system*" OR
    "power grid*" OR
    "electric grid*" OR
    "electrical grid*" OR
    "electricity grid*" OR
    "power network*" OR
    "electricity network*" OR
    "power distribution system*" OR
    "power distribution network*" OR
    "distribution grid*"
)
```

### `H1_SCOPUS_BT_v1`

```text
TITLE-ABS-KEY(
    "transportation system*" OR
    "transport system*" OR
    "transportation network*" OR
    "transport network*" OR
    "road transportation" OR
    "road network*" OR
    "traffic network*" OR
    "traffic system*" OR
    "intelligent transportation system*" OR
    "electrified transportation" OR
    "electric vehicle*" OR
    "electric mobility" OR
    "e-mobility" OR
    railway* OR
    "rail transit" OR
    subway* OR
    metro*
)
```

### `H1_SCOPUS_BI_v1`

```text
TITLE-ABS-KEY(
    interdependen* OR
    coupled OR
    coupling OR
    integrat* OR
    interaction* OR
    "cross-system" OR
    "cross-network" OR
    multilayer OR
    "multi-layer" OR
    bidirectional OR
    "bi-directional"
)
```

Final combination:

```text
#BP AND #BT AND #BI
```

or equivalently paste the three `TITLE-ABS-KEY(...)` clauses joined by `AND`.

Use straight quotation marks and preserve the query exactly as executed.

---

## 9. Web of Science Core Collection

Use **Core Collection → Advanced Search / Query Builder → Boolean results**, not Smart Search.

Topic `TS=` covers title, abstract, author keywords, and Keywords Plus.

### `H1_WOS_BP_v1`

```text
TS=(
    "power system*" OR
    "electric power system*" OR
    "electrical power system*" OR
    "power grid*" OR
    "electric grid*" OR
    "electrical grid*" OR
    "electricity grid*" OR
    "power network*" OR
    "electricity network*" OR
    "power distribution system*" OR
    "power distribution network*" OR
    "distribution grid*"
)
```

### `H1_WOS_BT_v1`

```text
TS=(
    "transportation system*" OR
    "transport system*" OR
    "transportation network*" OR
    "transport network*" OR
    "road transportation" OR
    "road network*" OR
    "traffic network*" OR
    "traffic system*" OR
    "intelligent transportation system*" OR
    "electrified transportation" OR
    "electric vehicle*" OR
    "electric mobility" OR
    "e-mobility" OR
    railway* OR
    "rail transit" OR
    subway* OR
    metro*
)
```

### `H1_WOS_BI_v1`

```text
TS=(
    interdependen* OR
    coupled OR
    coupling OR
    integrat* OR
    interaction* OR
    "cross-system" OR
    "cross-network" OR
    multilayer OR
    "multi-layer" OR
    bidirectional OR
    "bi-directional"
)
```

Final combination:

```text
#1 AND #2 AND #3
```

No proximity condition is imposed in v1.0 because the three blocks are already restrictive and proximity could discard legitimate abstracts that describe the infrastructures in separate sentences.

---

## 10. Compendex — Engineering Village

Compendex `KY` is used for Subject/Title/Abstract searching.

### `H1_COMPENDEX_CORE_v1`

```text
(
  (
    "power system*" OR
    "electric power system*" OR
    "electrical power system*" OR
    "power grid*" OR
    "electric grid*" OR
    "electrical grid*" OR
    "electricity grid*" OR
    "power network*" OR
    "electricity network*" OR
    "power distribution system*" OR
    "power distribution network*" OR
    "distribution grid*"
  ) WN KY
)
AND
(
  (
    "transportation system*" OR
    "transport system*" OR
    "transportation network*" OR
    "transport network*" OR
    "road transportation" OR
    "road network*" OR
    "traffic network*" OR
    "traffic system*" OR
    "intelligent transportation system*" OR
    "electrified transportation" OR
    "electric vehicle*" OR
    "electric mobility" OR
    "e-mobility" OR
    railway* OR
    "rail transit" OR
    subway* OR
    metro*
  ) WN KY
)
AND
(
  (
    interdependen* OR
    coupled OR
    coupling OR
    integrat* OR
    interaction* OR
    "cross-system" OR
    "cross-network" OR
    multilayer OR
    "multi-layer" OR
    bidirectional OR
    "bi-directional"
  ) WN KY
)
```

Proximity operators remain available for later versioned refinement if the initial set proves too noisy.

Ei controlled-vocabulary terms are not invented in v1.0. They must be obtained from the actual Compendex thesaurus after the first run; any augmentation becomes a new version with a recorded reason.

---

## 11. IEEE Xplore

Use **Command Search with metadata search**, not full text.

### `H1_IEEE_CORE_v1`

```text
(
  "power system*" OR
  "electric power system*" OR
  "electrical power system*" OR
  "power grid*" OR
  "electric grid*" OR
  "electrical grid*" OR
  "electricity grid*" OR
  "power network*" OR
  "electricity network*" OR
  "power distribution system*" OR
  "power distribution network*" OR
  "distribution grid*"
)
AND
(
  "transportation system*" OR
  "transport system*" OR
  "transportation network*" OR
  "transport network*" OR
  "road transportation" OR
  "road network*" OR
  "traffic network*" OR
  "traffic system*" OR
  "intelligent transportation system*" OR
  "electrified transportation" OR
  "electric vehicle*" OR
  "electric mobility" OR
  "e-mobility" OR
  railway* OR
  "rail transit" OR
  subway* OR
  metro*
)
AND
(
  interdependen* OR
  coupled OR
  coupling OR
  integrat* OR
  interaction* OR
  "cross-system" OR
  "cross-network" OR
  multilayer OR
  "multi-layer" OR
  bidirectional OR
  "bi-directional"
)
```

The concept blocks remain within IEEE Command Search term limits as specified in the source protocol.

---

## 12. Diagnostic dynamic query

After running CORE in each database, append:

```text
AND
(
    dynam* OR
    tempor* OR
    spatiotemporal OR
    "spatio-temporal" OR
    "time-varying" OR
    "time-dependent" OR
    "state-dependent" OR
    cascade* OR
    propagat* OR
    disrupt* OR
    failur* OR
    outage* OR
    resilience OR
    recover* OR
    restor* OR
    vulnerab* OR
    static OR
    topolog*
)
```

Record

```math
N_{\rm CORE},\qquad N_{\rm DYN}.
```

The discovery set remains

```math
\boxed{\mathcal P_{\rm discovery}=\mathcal P_{\rm CORE},}
```

not $\mathcal P_{\rm DYN}$. `DYN` is a sensitivity diagnostic.

---

## 13. Fresh search-sensitivity pilot

The source protocol records a fresh web sensitivity pilot conducted without using the old 325-paper corpus as the search universe. It recovered multiple mechanism families rather than a single predetermined architecture, including:

- post-storm power/transport recovery where transport accessibility constrains power repair;
- coupled power–transport operation with information propagation and traffic/power feedback;
- spatial-temporal coupled electricity/transport modelling;
- explicit bidirectional cascading effects in coupled transportation–power systems;
- road-transportation/electric-power interdependency combining traffic assignment, power-flow cascading, and recovery;
- static/structural and resilience-oriented coupled-network formulations.

The pilot therefore supports the methodological decision that $B_D$ should not be compulsory: CORE must retain foundational planning, operation, and static/routine coupling models needed to define $M_1$, while DYN preferentially tags cascading, resilience, and recovery studies.

The pilot is a **search-sensitivity check**, not evidence eligibility or hypothesis confirmation.

---

## 14. PRESS audit

The source protocol applies PRESS-style checks and PRISMA-S reproducibility principles.

| PRESS domain | Result |
|---|---|
| Research question translated correctly | **PASS** |
| Main concepts represented | **PASS** |
| Synonyms/text words | **PASS — provisional until database term-frequency audit** |
| Boolean structure | **PASS** |
| Proximity use | **PASS — deliberately not imposed** |
| Controlled vocabulary | **PENDING for Compendex thesaurus; version-controlled augmentation only** |
| Spelling/variants | **PASS** |
| Unjustified limits | **PASS — none** |
| Year restriction | **NONE** |
| Hazard restriction | **NONE** |
| EV-only restriction | **NONE** |
| Geography restriction | **NONE** |

Therefore

```math
\boxed{Q_{H_1}^{MASTER,v1}\text{ is frozen for initial execution.}}
```

Frozen means it is never silently edited:

```math
Q^{v1}\neq Q^{v2}.
```

Any modification creates a new version and a reason-for-change record.

---

## 15. Eligibility criteria — frozen before screening

A record becomes potentially eligible for $H_1$ only if all three mandatory conditions hold:

```math
\boxed{I_1\land I_2\land I_3.}
```

### `I_1` — system condition

Both an electrical-power infrastructure and a transportation infrastructure are substantively represented.

### `I_2` — causal coupling condition

At least one genuine cross-system relationship exists:

```math
\boxed{P\rightarrow T\quad\lor\quad T\rightarrow P\quad\lor\quad P\leftrightarrow T.}
```

Shared exposure alone fails this criterion:

```math
\boxed{h\rightarrow P,\quad h\rightarrow T\not\Rightarrow P\leftrightarrow T.}
```

### `I_3` — technical evidence condition

The study provides at least one of:

```math
\boxed{\text{quantitative mechanism}\vee\text{mathematical model}\vee\text{computational model}\vee\text{empirical coupling estimate}\vee\text{parameterization}\vee\text{validation}\vee\text{comparator/baseline}.}
```

---

## 16. H1 evidence-role tags

Eligible studies receive one or more tags:

```math
\boxed{R(P_i)\subseteq\{R_{\rm dyn},R_{\rm static},R_{\rm independent},R_{\rm mechanism},R_{\rm parameter},R_{\rm validation},R_{\rm baseline}\}.}
```

A static model is not excluded merely for being static. It may be exactly the comparator needed for $M_1$.

---

## 17. Frozen exclusion codes for H1

| Code | Exclusion |
|---|---|
| `H1-EX01` | no electrical-power system represented |
| `H1-EX02` | no transportation system represented |
| `H1-EX03` | both sectors mentioned but no cross-system mechanism |
| `H1-EX04` | common hazard only; no causal $P\leftrightarrow T$ transmission |
| `H1-EX05` | single-sector EV/load study without transportation-network coupling |
| `H1-EX06` | qualitative discussion only; no usable technical evidence |
| `H1-EX07` | wrong study/report type for primary evidence |
| `H1-EX08` | duplicate study/report |
| `H1-EX09` | full text unavailable for final technical adjudication |
| `H1-EX10` | mechanism outside the hypothesis domain |

A review may be retained as

```text
SECONDARY_SEARCH_SOURCE
```

for terminology and citation chasing while remaining excluded from the primary quantitative evidence set.

---

## 18. Screening rule

At title/abstract stage:

```math
D_i^{TA}\in\{\text{INCLUDE},\text{EXCLUDE},\text{UNCERTAIN}\}.
```

Use a liberal inclusion rule:

```math
\boxed{\text{uncertainty}\Rightarrow\text{retain for full text}.}
```

At full text:

```math
D_i^{FT}\in\{\text{ELIGIBLE},\text{EXCLUDED}\}.
```

Every exclusion must have exactly one primary exclusion code plus optional notes.

---

## 19. No restrictions at initial search

For the first execution:

```math
\begin{aligned}
\text{year} &: \text{database inception--11 Sep 2026},\\
\text{geography} &: \text{unrestricted},\\
\text{hazard} &: \text{unrestricted},\\
\text{transport mode} &: \text{unrestricted},\\
\text{power subsystem} &: \text{unrestricted},\\
\text{language search filter} &: \text{none},\\
\text{open-access filter} &: \text{none}.
\end{aligned}
```

This prevents pre-selecting flood, EV, road traffic, or distribution systems before the evidence has been generated.

---

## 20. Search execution record

For every database create

```math
\boxed{r_d=(ID,\,database,\,platform,\,query,\,date,\,coverage,\,filters,\,N).}
```

| Search ID | Database | Query version | Search date | Coverage | Fields/filters | Results |
|---|---|---|---|---|---|---|
| `H1_SCOPUS_CORE_v1` | Scopus | frozen | 2026-09-11 | inception–present | none beyond declared field search | pending |
| `H1_WOS_CORE_v1` | WoS Core | frozen | 2026-09-11 | subscription depth | none beyond declared field search | pending |
| `H1_COMPENDEX_CORE_v1` | Compendex | frozen | 2026-09-11 | database coverage | `KY`; no substantive filter | pending |
| `H1_IEEE_CORE_v1` | IEEE Xplore | frozen | 2026-09-11 | database coverage | metadata search; no substantive filter | pending |

No fake counts are entered. Actual $N$ must come from authenticated execution of the frozen strings in the four databases. Counts inferred from ordinary web search are not valid PRISMA records.

---

## 21. Frozen state and next operation

The following are complete:

```math
\begin{aligned}
&\checkmark\ H_1\text{ scientific search target},\\
&\checkmark\ \text{concept decomposition},\\
&\checkmark\ \text{synonym vocabulary},\\
&\checkmark\ \text{fresh sensitivity pilot},\\
&\checkmark\ \text{revision from four mandatory blocks to three},\\
&\checkmark\ Q_{H_1}^{MASTER,v1},\\
&\checkmark\ Q_{H_1}^{Scopus,v1},\\
&\checkmark\ Q_{H_1}^{WoS,v1},\\
&\checkmark\ Q_{H_1}^{Compendex,v1},\\
&\checkmark\ Q_{H_1}^{IEEE,v1},\\
&\checkmark\ \text{PRESS audit},\\
&\checkmark\ \text{eligibility criteria},\\
&\checkmark\ \text{exclusion taxonomy},\\
&\checkmark\ \text{screening rule}.
\end{aligned}
```

The scientific state is therefore

```math
\boxed{\textbf{H1 search protocol = FROZEN v1.0}}
```

The next operation is execution of the exact four database strings, export of every retrieved record, and construction of

```math
\boxed{\mathcal P_{H_1}^{raw}=P_{\rm Scopus}\cup P_{\rm WoS}\cup P_{\rm Compendex}\cup P_{\rm IEEE}.}
```

Only then proceed to DOI/database-ID/title deduplication and title–abstract screening.

---

## 22. Execution integrity rules

1. **Do not edit v1.0 in place after execution.** Any changed term, field, operator, filter, or coverage rule creates a new version.
2. **Archive every exact executed string.** The text in this file is the pre-execution authority; the execution registry records the exact database/platform form actually submitted.
3. **Record platform and date.** Database content and interfaces change over time.
4. **Record result counts before deduplication.** These are required for reproducible flow accounting.
5. **Preserve all raw exports and hashes.** Deduplication must never destroy source provenance.
6. **Do not use remembered papers as seeds.** Citation chasing begins only from newly eligible records under the fresh-search protocol.
7. **Do not use the old 325-paper corpus for automatic inclusion.** It remains a post hoc coverage audit only.
8. **Do not use DYN as the discovery universe.** $\mathcal P_{\rm discovery}=\mathcal P_{\rm CORE}$.

This file is the frozen executable authority for the first $H_1$ database search.