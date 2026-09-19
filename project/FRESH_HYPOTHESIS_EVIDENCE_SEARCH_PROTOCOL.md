# Fresh Hypothesis Evidence Search Protocol

> **AUTHORITY-DRIFT CLEANUP 2026-09-19 — METHODOLOGICAL PROVENANCE / H4–H5 MAPPING SUPERSEDED**
>
> The database-first, outcome-blind search principles in this file remain useful methodological provenance, but its H4/H5 construct labels are obsolete.  
> **Current H4:** intervention effectiveness/efficiency/sustainability consequence heterogeneity.  
> **Current H5:** resilience-only versus joint resilience–sustainability engineering decision.  
> Interface-criticality superiority is a separate optional diagnostic; adaptive-pathway superiority is a conditional Stage-7 extension.  
> Do not execute new H4/H5 searches from the old query families below without a versioned v2 search protocol aligned to `CANONICAL_RQ_SO_HYPOTHESES_V3.md`.


![Status](https://img.shields.io/badge/status-METHOD%20PROVENANCE%20%7C%20H4--H5%20MAPPING%20SUPERSEDED-9A6700)
![Search](https://img.shields.io/badge/evidence%20search-FROM%20ZERO-1A7F37)
![Old Corpus](https://img.shields.io/badge/325--paper%20corpus-SECONDARY%20COVERAGE%20CHECK-9A6700)

**Status:** METHODOLOGICAL PROVENANCE — H4/H5 MAPPING SUPERSEDED; VERSIONED V2 REQUIRED BEFORE NEW H4/H5 SEARCH  
**Purpose:** establish a new reproducible evidence base for $H_1$–$H_5$ and the P–T–I–O demonstrator from first principles  
**Primary rule:** previously known papers, memory, prior rankings, and the frozen 325-paper corpus do **not** determine inclusion  
**Old-corpus role:** secondary coverage audit only, after the fresh search and eligibility process  
**Execution rule:** exact search strings, eligibility criteria, databases, search dates, screening codebook, and exclusion reasons must be frozen *before* screening begins

The governing principle is

```math
\textbf{New scientific question}
\Rightarrow
\textbf{new evidence search from first principles}.
```

The evidence base for the hypotheses and demonstrator is therefore built from a fresh reproducible search, not from previously selected literature.

---

## 1. Governing inclusion rule

For every hypothesis $H_i$:

```math
H_i
\rightarrow
\text{mechanisms/constructs}
\rightarrow
\text{search concepts}
\rightarrow
\text{database searches}
\rightarrow
\text{screening}
\rightarrow
\text{full text}
\rightarrow
\text{evidence extraction}.
```

The following are prohibited as primary evidence-selection logics:

```math
H_i
\rightarrow
\text{look only inside papers already known},
```

and

```math
\text{memory}
\rightarrow
\text{preferred papers}
\rightarrow
\text{model}.
```

A paper becomes part of the new evidence base only because the new search finds it and the new eligibility protocol qualifies it.

---

## 2. What “start from zero” means

Previously known and previously unknown papers are treated identically during screening:

```math
P_{\rm known}\equiv P_{\rm unknown}
```

with respect to eligibility.

If an important paper from the old 325-paper corpus is rediscovered and passes the new criteria, it enters normally. If it is not rediscovered or fails eligibility, it does not enter merely because it was previously used.

This prevents prior familiarity from becoming an inclusion criterion.

---

## 3. Freeze research questions before papers

The current five primary hypotheses remain the search anchors:

| Hypothesis | Search focus |
|---|---|
| $H_1$ | dynamic interdependency and propagation |
| $H_2$ | information–organization effects |
| $H_3$ | controlled viability |
| $H_4$ | interface criticality |
| $H_5$ | adaptive transformation |

Each hypothesis must be decomposed into searchable scientific concepts before the databases are queried.

For example, $H_1$ begins conceptually with

```math
\text{power}
+
\text{transportation}
+
\text{interdependency}
+
\text{dynamic/cascade/coupling},
```

but final database queries must systematically expand synonyms, controlled vocabulary, spelling variants, and indexing terminology.

---

## 4. Database-first discovery

The core multi-database engineering search should use

```math
\text{Scopus}
+
\text{Web of Science}
+
\text{Compendex}
+
\text{IEEE Xplore},
```

with specialized databases added where scientifically useful, including transportation-specific databases for transport mechanisms.

Google Scholar should be treated primarily as a supplementary source for citation chasing, locating difficult papers, and coverage checks rather than as the sole systematic-search database.

Every search must record at least:

- database/platform;
- exact query string;
- search fields;
- filters;
- date searched;
- database coverage/date range;
- number of results returned;
- export format and file hash where applicable.

---

## 5. Publication-time rule

The default evidence-search period is

```math
\text{database inception}
\rightarrow
\text{search date},
```

unless a narrower interval is justified by a specific scientific question.

This is required because foundational evidence relevant to viability theory, reachability, interdependent networks, traffic flow, power-system dynamics, cascading failure, robust decision making, and related mathematical foundations may predate recent review windows.

Recent literature can later be analyzed as a separate current-developments subset without excluding older foundational work from the primary search.

---

## 6. Search by mechanism, not by expected solution

Search concepts must describe the scientific mechanism broadly enough to avoid forcing the thesis formulation into the search.

For example, if the thesis may eventually use $S_{ij}^{\mathcal V}$, the search should not be restricted to “viability interface criticality.” Instead, the search should recover the broader mechanism space, such as

```math
\text{interdependency}
+
\text{critical interface}
+
\text{sensitivity}
+
\text{failure propagation}
+
\text{intervention}.
```

The literature may then reveal centrality, sensitivity, controllability, reachability, fragility, importance measures, or other approaches not anticipated by the thesis.

The search protocol must therefore discover candidate methods rather than encode the desired answer.

---

## 7. Three discovery routes

The fresh evidence universe is

```math
\mathcal P_{\rm search}
=
\mathcal P_{\rm database}
\cup
\mathcal P_{\rm backward}
\cup
\mathcal P_{\rm forward}.
```

### Database search

The primary systematic discovery route.

### Backward citation search

For an eligible paper $P_i$:

```math
P_i\rightarrow\text{its references}.
```

### Forward citation search

For an important eligible paper $P_i$:

```math
P_i\rightarrow\text{papers citing }P_i.
```

Citation chasing begins **after** the initial database search so that remembered or famous papers do not determine the starting evidence set.

---

## 8. Separate hypothesis-specific searches

Do not use one giant thesis query. Define

```math
\mathcal S
=
\{S_{H1},S_{H2},S_{H3},S_{H4},S_{H5}\}.
```

The hypothesis-specific search families should be constructed independently and later deduplicated/combined.

### $S_{H1}$ — dynamic interdependency and propagation

```math
(P\text{ terms})
\land
(T\text{ terms})
\land
(\text{interdependency/coupling terms})
\land
(\text{dynamic/cascade/propagation terms}).
```

### $S_{H2}$ — information and organizational response

```math
(\text{infrastructure terms})
\land
(\text{information/communication/state-estimation terms})
\land
(\text{organization/coordination/crew/resource terms})
\land
(\text{resilience/recovery/control terms}).
```

### $S_{H3}$ — controlled viability

```math
(\text{infrastructure/energy/transport terms})
\land
(\text{viability/reachability/invariant-set terms})
\land
(\text{control/resilience/safety terms}).
```

### $S_{H4}$ — interface criticality

Search the broader family of interdependency/interface importance, sensitivity, propagation, controllability, fragility, intervention targeting, and related engineering-importance constructs without prespecifying the thesis metric.

### $S_{H5}$ — adaptive transformation

Search adaptive pathways, robust decision making, staged/real-options planning, transformation pathways, infrastructure transition, multistage decisions under uncertainty, and related feasibility/equity/sustainability constructs without assuming one preferred policy formulation.

The exact final syntax for each database must be separately documented because field syntax and controlled vocabularies differ across platforms.

---

## 9. Eligibility is predetermined

Before screening any result, define and freeze

```math
I(P)
=
\begin{cases}
1,&P\text{ eligible},\\
0,&P\text{ excluded}.
\end{cases}
```

Candidate inclusion criteria include:

- peer-reviewed research or authoritative technical standard;
- relevant mathematical, physical, or engineering model;
- relevant infrastructure mechanism;
- sufficient methodological description for the intended evidence role;
- relevance to at least one $H_i$;
- language that can be assessed reliably;
- full text obtainable when equation-level extraction is required.

Candidate exclusion criteria include:

- purely rhetorical resilience discussion without usable mechanism/model evidence;
- no relevant infrastructure system or transferable mechanism;
- duplicate record/study;
- nontechnical commentary;
- application outside the transferability domain with no useful transferable mathematics;
- insufficient full-text access when full-text evidence is required for the intended role.

The exact operational criteria and exclusion hierarchy must be frozen before title/abstract screening.

---

## 10. PRISMA-style accounting

The fresh search records

```math
N_{\rm identified}
\rightarrow
N_{\rm deduplicated}
\rightarrow
N_{\rm title/abstract}
\rightarrow
N_{\rm fulltext}
\rightarrow
N_{\rm eligible}.
```

Every full-text exclusion receives a coded reason. A candidate scheme is

```math
\begin{aligned}
E_1&:\ \text{wrong infrastructure domain},\\
E_2&:\ \text{no relevant mechanism},\\
E_3&:\ \text{no usable mathematical/engineering model},\\
E_4&:\ \text{insufficient evidence for intended role},\\
E_5&:\ \text{duplicate study},\\
E_6&:\ \text{full text unavailable}.
\end{aligned}
```

The final codes and ordering must be frozen with the screening codebook.

---

## 11. Fresh eligible evidence set

The fresh eligible set is

```math
\mathcal P_{\rm eligible}^{\rm NEW}.
```

Only after eligibility is established does full-text evidence extraction begin:

```math
\mathcal P_{\rm eligible}^{\rm NEW}
\rightarrow
\text{FTEE}.
```

FTEE then extracts

```math
\text{mechanism}
+
\text{equation}
+
\text{parameters}
+
\text{assumptions}
+
\text{domain}
+
\text{validation}
+
\text{UQ}.
```

Thus search/screening determines **which papers are eligible evidence sources**, while FTEE determines **what those sources can legitimately contribute to the demonstrator**.

---

## 12. Role of the old 325-paper corpus

The frozen 325-paper corpus becomes a **secondary coverage audit**, not a primary search universe.

After completion of the fresh search, compare

```math
\mathcal P_{\rm NEW}
\cap
\mathcal P_{325}
```

for overlap and

```math
\mathcal P_{325}
\setminus
\mathcal P_{\rm NEW}
```

for previously known records that were not recovered.

A missing old paper triggers a **search-diagnostics question**, not automatic inclusion:

> Why was this previously important paper not recovered?

Possible explanations include:

1. incomplete new query;
2. absent database coverage;
3. different indexing terminology;
4. changed relevance to the current hypothesis;
5. prior corpus inclusion that is not justified under the new protocol.

If a diagnostic reveals a search weakness, revise and rerun the **search method** according to a documented amendment; do not manually insert the remembered paper into the evidence set.

---

## 13. Complete revised workflow

```math
\begin{aligned}
&H_1-H_5\\
&\downarrow\\
&\textbf{Fresh search protocol}\\
&\downarrow\\
&\textbf{Database searches from zero}\\
&\downarrow\\
&\text{deduplication}\\
&\downarrow\\
&\text{title/abstract screening}\\
&\downarrow\\
&\text{full-text eligibility}\\
&\downarrow\\
&\mathcal P_{\rm eligible}^{\rm NEW}\\
&\downarrow\\
&\textbf{Evidence-to-Equation extraction (FTEE)}\\
&\downarrow\\
&\mathfrak M_{\rm required}\\
&\downarrow\\
&\text{candidate demonstrators}\\
&\downarrow\\
&\text{V\&V + identifiability + UQ gates}\\
&\downarrow\\
&\mathcal M_D^*.
\end{aligned}
```

Only after the primary evidence workflow is complete may

```math
\mathcal P_{\rm NEW}
\leftrightarrow
\mathcal P_{325}
```

be used as a secondary coverage audit.

---

## 14. Governing rules

```math
\textbf{No paper is evidence because we remember it.}
```

```math
\textbf{No paper is evidence because it belonged to an earlier frozen corpus.}
```

```math
\textbf{A paper becomes evidence only because the new reproducible search finds it and the new eligibility protocol qualifies it.}
```

These rules govern the new evidence base for $H_1$–$H_5$, FTEE, demonstrator construction, parameterization, benchmark selection, and subsequent confirmatory analysis.

---

## 15. Immediate next protocol-development step

Before running any database search, freeze:

1. the searchable construct decomposition for each $H_i$;
2. database-specific Boolean queries and field restrictions;
3. search dates and coverage rules;
4. deduplication/identity rules;
5. inclusion/exclusion criteria and exclusion-code hierarchy;
6. title/abstract screening form;
7. full-text eligibility form;
8. backward/forward citation-chasing rules;
9. amendment/version-control procedure;
10. PRISMA-style accounting schema.

Only then should the new database searches be executed.
