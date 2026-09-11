# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![Search](https://img.shields.io/badge/evidence%20search-FRESH%20FROM%20ZERO-1A7F37)
![FTEE](https://img.shields.io/badge/FTEE-PILOT--READY-9A6700)
![325 Corpus](https://img.shields.io/badge/325--paper%20corpus-SECONDARY%20AUDIT-9A6700)

This directory is the active mathematical/scientific specification of the MSE thesis. The seven-stage framework and five-primary-hypothesis logic are frozen. The current evidence phase now begins with a **fresh reproducible literature search from first principles**. Memory, previously selected papers, and the frozen 325-paper corpus do not determine inclusion.

> **Governing evidence rule:** A paper becomes evidence only because the new reproducible search finds it and the new eligibility protocol qualifies it.

> **Automated presentation QA:** [`../tools/thesis_display_lint.py`](../tools/thesis_display_lint.py) checks active Markdown display rules, table/fence integrity, ontology drift, and machine-readable authority registries.

---

## 1. Authority map

| Priority | File | Role | Status |
|---:|---|---|---|
| 1 | [`THESIS_SCOPE.md`](THESIS_SCOPE.md) | current scientific scope and stage boundaries | canonical / frozen |
| 2 | [`CANONICAL_7_STAGE_FRAMEWORK.md`](CANONICAL_7_STAGE_FRAMEWORK.md) | complete seven-stage architecture and mathematics | canonical / frozen |
| 3 | [`CANONICAL_SYSTEM_DEFINITION.md`](CANONICAL_SYSTEM_DEFINITION.md) | P–T–I–O system identity and state ontology | canonical |
| 4 | [`FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md) | framework-level subsystem decomposition | canonical |
| 5 | [`STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](STAGE_2_INTERDEPENDENCY_MECHANISMS.md) | Stage-2 causal interdependency specification | frozen |
| 6 | [`STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md) | Stage-3 dynamic architecture | frozen |
| 7 | [`STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md) | Stage-4 observation-to-action architecture | frozen |
| 8 | [`STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md) | Stage-5 viability architecture | frozen |
| 9 | [`STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md`](STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md) | Stage-6 transition architecture | frozen |
| 10 | [`STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md`](STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md) | Stage-7 adaptive transformation architecture | frozen |
| 11 | [`RESEARCH_HYPOTHESES.md`](RESEARCH_HYPOTHESES.md) | five primary confirmatory hypotheses | logic frozen; thresholds unset |
| 12 | [`ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md) | confirmatory operationalization and VVUQ gates | current |
| 13 | [`MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md) | demonstrator-reduction rationale and stopping rule | current methodology |
| 14 | [`FRESH_HYPOTHESIS_EVIDENCE_SEARCH_PROTOCOL.md`](FRESH_HYPOTHESIS_EVIDENCE_SEARCH_PROTOCOL.md) | fresh hypothesis-specific literature search, screening and eligibility governance | **current primary evidence-search methodology** |
| 15 | [`FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md`](FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md) | evidence-unit extraction and model-credibility qualification | pilot-ready; must follow fresh eligibility |
| 16 | [`CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md`](CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md) | old 325-paper protocol | **secondary coverage audit only** |
| 17 | [`MATHEMATICAL_FOUNDATION.md`](MATHEMATICAL_FOUNDATION.md) | cross-stage mathematical foundation | active companion |
| 18 | [`SCIENTIFIC_PROPOSITIONS.md`](SCIENTIFIC_PROPOSITIONS.md) | broader proposition/falsification registry | active companion |
| 19 | [`MATHEMATICAL_PRESENTATION_V3.md`](MATHEMATICAL_PRESENTATION_V3.md) | notation, display, color and rendering contract | current |

---

## 2. Frozen scientific chain

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
\underbrace{\Phi_{\mathrm{ST}}\rightarrow(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)}_{6}\\
&\rightarrow
\underbrace{\mathfrak P_{\mathrm{ST}}}_{7}.
\end{aligned}
```

The primary confirmatory set remains

```math
\mathbb H=\{H_1,H_2,H_3,H_4,H_5\}.
```

---

## 3. Fresh-search governance

The primary evidence workflow is now

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

Previously known and unknown papers are equivalent with respect to screening:

```math
P_{\rm known}\equiv P_{\rm unknown}.
```

The database search should be hypothesis-specific rather than one giant thesis query:

```math
\mathcal S=\{S_{H1},S_{H2},S_{H3},S_{H4},S_{H5}\}.
```

Core engineering databases are Scopus, Web of Science, Compendex and IEEE Xplore, supplemented where scientifically useful. The default temporal scope is database inception to the search date unless a narrower range is justified.

The discovery universe is

```math
\mathcal P_{\rm search}
=
\mathcal P_{\rm database}
\cup
\mathcal P_{\rm backward}
\cup
\mathcal P_{\rm forward}.
```

Citation chasing starts only after the initial database search.

---

## 4. Eligibility and PRISMA-style accounting

Eligibility must be frozen before screening:

```math
I(P)=
\begin{cases}
1,&P\text{ eligible},\\
0,&P\text{ excluded}.
\end{cases}
```

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

Every full-text exclusion receives a coded reason.

The resulting primary evidence set is

```math
\mathcal P_{\rm eligible}^{\rm NEW}.
```

---

## 5. FTEE position

FTEE begins only after the new search and eligibility process:

```math
\mathcal P_{\rm eligible}^{\rm NEW}
\rightarrow
\text{FTEE}
\rightarrow
\mathfrak M_{\rm required}
\rightarrow
\text{candidate demonstrators}.
```

FTEE extracts and qualifies evidence; it does not select papers for eligibility and it does not choose the demonstrator.

---

## 6. Role of the frozen 325-paper corpus

The 325-paper corpus is now secondary:

```math
\mathcal P_{\rm NEW}\leftrightarrow\mathcal P_{325}
```

is used only after the fresh search as a coverage audit. A previously known paper not recovered by the fresh search triggers search diagnostics, not automatic inclusion.

---

## 7. Current end-to-end workflow

```math
\begin{aligned}
&H_1-H_5\\
&\downarrow\\
&\textbf{fresh search protocol and frozen search codebook}\\
&\downarrow\\
&\textbf{database searches from zero}\\
&\downarrow\\
&\text{deduplication + title/abstract screening + full-text eligibility}\\
&\downarrow\\
&\mathcal P_{\rm eligible}^{\rm NEW}\\
&\downarrow\\
&\textbf{FTEE pilot/freeze and full-text evidence extraction}\\
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

Only after the primary evidence workflow is complete may the old 325-paper corpus be used for secondary coverage diagnostics.

---

## 8. Governing evidence rules

```math
\textbf{No paper is evidence because we remember it.}
```

```math
\textbf{No paper is evidence because it belonged to an earlier frozen corpus.}
```

```math
\textbf{A paper becomes evidence only because the new reproducible search finds it and the new eligibility protocol qualifies it.}
```

---

## 9. Immediate next step

Before executing searches, freeze the hypothesis-specific search-concept decomposition, database-specific Boolean strings, search fields, search dates, database coverage rules, deduplication logic, inclusion/exclusion criteria, screening forms, citation-chasing rules, amendment procedure and PRISMA accounting schema.

Historical/archive material remains provenance only unless explicitly reintroduced through a versioned revision.
