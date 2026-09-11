# MSE Thesis — Multilayer Interdependent Power–Transportation Infrastructure Resilience

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![Search](https://img.shields.io/badge/evidence%20search-FRESH%20FROM%20ZERO-1A7F37)
![FTEE](https://img.shields.io/badge/FTEE-PILOT--READY-9A6700)
![325 Corpus](https://img.shields.io/badge/325--paper%20corpus-SECONDARY%20AUDIT-9A6700)

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** active thesis source of truth  
**Framework status:** complete seven-stage conceptual and mathematical framework frozen  
**Hypothesis status:** five-primary-hypothesis logic frozen; numerical thresholds/test specifications not yet frozen  
**Evidence-search status:** new primary evidence search must start from zero for $H_1$–$H_5$  
**Old 325-paper corpus:** secondary coverage audit only  
**Citation standard:** APA 7th edition author–date  
**Updated:** 2026-09-11

> **Repository rule:** active thesis development belongs in `Dossiya-SE/MSE-thesis`. Historical/archive material is provenance only and cannot override current canonical files.

---

## Canonical entry points

| File | Role |
|---|---|
| [`project/README.md`](project/README.md) | active mathematical/project dashboard |
| [`project/THESIS_SCOPE.md`](project/THESIS_SCOPE.md) | frozen thesis scope |
| [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md) | frozen seven-stage framework |
| [`project/RESEARCH_HYPOTHESES.md`](project/RESEARCH_HYPOTHESES.md) | five primary confirmatory hypotheses |
| [`project/ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](project/ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md) | confirmatory operationalization and VVUQ gates |
| [`project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md) | demonstrator-reduction methodology |
| [`project/FRESH_HYPOTHESIS_EVIDENCE_SEARCH_PROTOCOL.md`](project/FRESH_HYPOTHESIS_EVIDENCE_SEARCH_PROTOCOL.md) | fresh hypothesis-specific evidence search from first principles |
| [`project/FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md`](project/FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md) | full-text evidence-to-equation extraction protocol |
| [`project/CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md`](project/CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md) | 325-paper secondary coverage audit only |
| [`project/MATHEMATICAL_PRESENTATION_V3.md`](project/MATHEMATICAL_PRESENTATION_V3.md) | GitHub math/rendering standard |
| [`tools/thesis_display_lint.py`](tools/thesis_display_lint.py) | automated Markdown/math/ontology QA |

---

## Frozen scientific framework

```math
\begin{aligned}
\underbrace{\mathcal S}_{1}
&\rightarrow
\underbrace{\mathfrak I}_{2}
\rightarrow
\underbrace{F_{\mathcal G}^{m}}_{3}\\
&\rightarrow
\underbrace{X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u}_{4}\\
&\rightarrow
\underbrace{K_{\mathrm{sus}},\mathcal V,\rho,T_{\mathcal V},T_K}_{5}\\
&\rightarrow
\underbrace{\Phi_{\mathrm{ST}}\rightarrow(c_6,\mathcal D_6,\boldsymbol\zeta_T)}_{6}\\
&\rightarrow
\underbrace{\mathfrak P_{\mathrm{ST}}}_{7}.
\end{aligned}
```

The primary confirmatory set is

```math
\mathbb H=\{H_1,H_2,H_3,H_4,H_5\}.
```

The seven-stage architecture and H1–H5 scientific logic are frozen. Exact thresholds $\delta_i$, hypothesis domains $\Omega_H$, validation domains $\Omega_V$, and final analysis procedures remain to be specified *a priori* from the fresh evidence base and selected demonstrator.

---

## Fresh evidence-search rule

The governing search logic is

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
\text{FTEE}.
```

Previously known and unknown papers are treated identically during screening:

```math
P_{\rm known}\equiv P_{\rm unknown}.
```

The primary database strategy is hypothesis-specific and multi-database, using Scopus, Web of Science, Compendex, IEEE Xplore, and specialized databases where scientifically useful. The default time span is database inception to the search date unless a narrower period is scientifically justified.

Searches target mechanisms rather than preferred solutions.

---

## Discovery, screening and eligibility

The fresh discovery universe is

```math
\mathcal P_{\rm search}
=
\mathcal P_{\rm database}
\cup
\mathcal P_{\rm backward}
\cup
\mathcal P_{\rm forward}.
```

Database search is primary; backward and forward citation chasing begin only after the initial database search.

Eligibility must be frozen before screening:

```math
I(P)=
\begin{cases}
1,&P\text{ eligible},\\
0,&P\text{ excluded}.
\end{cases}
```

PRISMA-style accounting records

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

The primary eligible set is

```math
\mathcal P_{\rm eligible}^{\rm NEW}.
```

---

## FTEE position

Only the newly eligible set enters FTEE:

```math
\mathcal P_{\rm eligible}^{\rm NEW}
\rightarrow
\text{FTEE}
\rightarrow
\mathfrak M_{\rm required}
\rightarrow
\text{candidate demonstrators}.
```

FTEE extracts mechanism, equations, parameters, assumptions, domain, validation, and uncertainty. It does not determine search eligibility and it does not choose the demonstrator.

---

## Role of the old 325-paper corpus

The frozen 325-paper corpus is no longer the primary evidence universe. It is used only after the fresh search for coverage diagnostics:

```math
\mathcal P_{\rm NEW}
\leftrightarrow
\mathcal P_{325}.
```

A previously known paper not recovered by the new search triggers a search-method diagnostic, not automatic inclusion.

---

## Current end-to-end workflow

```math
\begin{aligned}
&H_1-H_5\\
&\downarrow\\
&\textbf{fresh search protocol and frozen search codebook}\\
&\downarrow\\
&\textbf{database searches from zero}\\
&\downarrow\\
&\text{deduplication + screening + full-text eligibility}\\
&\downarrow\\
&\mathcal P_{\rm eligible}^{\rm NEW}\\
&\downarrow\\
&\textbf{FTEE pilot/freeze and evidence extraction}\\
&\downarrow\\
&\mathfrak M_{\rm required}\\
&\downarrow\\
&\text{candidate P--T--I--O demonstrators}\\
&\downarrow\\
&\text{V\&V + identifiability + UQ gates}\\
&\downarrow\\
&\mathcal M_D^*.
\end{aligned}
```

---

## Governing evidence rules

```math
\textbf{No paper is evidence because we remember it.}
```

```math
\textbf{No paper is evidence because it belonged to an earlier frozen corpus.}
```

```math
\textbf{A paper becomes evidence only because the new reproducible search finds it and the new eligibility protocol qualifies it.}
```

The immediate task is to freeze the hypothesis-specific search concepts, database-specific Boolean queries, database coverage/date rules, deduplication procedure, eligibility criteria, screening forms, citation-chasing rules, amendment procedure, and PRISMA accounting schema before any new search is executed.
