# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![Matrix](https://img.shields.io/badge/confirmatory%20matrix-CURRENT-0969DA)
![MSER](https://img.shields.io/badge/minimal%20sufficient%20realization-CURRENT-0969DA)
![Evidence](https://img.shields.io/badge/325--paper%20pipeline-CURRENT-0969DA)
![FTEE](https://img.shields.io/badge/FTEE%20v1.0-PILOT--READY-9A6700)

This directory is the active mathematical/scientific specification of the MSE thesis. The seven-stage framework and five-primary-hypothesis logic are frozen. The confirmatory matrix, minimal-sufficient demonstrator methodology, closed-corpus evidence-selection pipeline, and FTEE v1.0 now define the operationalization sequence.

> **Automated presentation QA:** [`../tools/thesis_display_lint.py`](../tools/thesis_display_lint.py) checks active Markdown display rules, table/fence integrity, ontology drift, and machine-readable authority registries.

---

## 1. Authority map

| Priority | File | Role | Status |
|---:|---|---|---|
| 1 | [`THESIS_SCOPE.md`](THESIS_SCOPE.md) | current scientific scope and stage boundaries | canonical / frozen |
| 2 | [`CANONICAL_7_STAGE_FRAMEWORK.md`](CANONICAL_7_STAGE_FRAMEWORK.md) | complete seven-stage architecture and mathematics | canonical / frozen |
| 3 | [`CANONICAL_SYSTEM_DEFINITION.md`](CANONICAL_SYSTEM_DEFINITION.md) | P–T–I–O system identity and state ontology | canonical |
| 4 | [`FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md) | framework-level subsystem decomposition | canonical |
| 5 | [`STAGES_1_2_APA7_EVIDENCE_GROUNDED.md`](STAGES_1_2_APA7_EVIDENCE_GROUNDED.md) | literature-grounded Stages 1–2 companion | canonical companion |
| 6 | [`STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](STAGE_2_INTERDEPENDENCY_MECHANISMS.md) | Stage-2 causal interdependency specification | frozen |
| 7 | [`STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md) | Stage-3 dynamic architecture | frozen |
| 8 | [`STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md) | Stage-4 observation-to-action architecture | frozen |
| 9 | [`STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md) | Stage-5 viability architecture | frozen |
| 10 | [`STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md`](STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md) | Stage-6 transition architecture | frozen |
| 11 | [`STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md`](STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md) | Stage-7 adaptive transformation architecture | frozen |
| 12 | [`RESEARCH_HYPOTHESES.md`](RESEARCH_HYPOTHESES.md) | five primary confirmatory hypotheses | logic frozen; thresholds unset |
| 13 | [`ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md) | confirmatory operationalization and VVUQ gates | current |
| 14 | [`MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md) | demonstrator-reduction rationale and stopping rule | current methodology |
| 15 | [`CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md`](CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md) | 325-paper evidence-selection engine | current methodology |
| 16 | [`FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md`](FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md) | evidence-unit extraction, equation/parameter/VVUQ qualification, hypothesis mapping | **pilot-ready; not frozen** |
| 17 | [`MATHEMATICAL_FOUNDATION.md`](MATHEMATICAL_FOUNDATION.md) | cross-stage mathematical foundation | active companion |
| 18 | [`SCIENTIFIC_PROPOSITIONS.md`](SCIENTIFIC_PROPOSITIONS.md) | broader proposition/falsification registry | active companion |
| 19 | [`MATHEMATICAL_PRESENTATION_V3.md`](MATHEMATICAL_PRESENTATION_V3.md) | notation, display, color and rendering contract | current |

The earlier `STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md` is provenance only and cannot override the frozen Stage-7 specification.

---

## 2. Frozen mathematical chain

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

## 3. Confirmatory operationalization

[`ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md) connects each $H_i$ to its scientific gap, mechanism, variables, estimand, baseline, strong rival, context of use, V&V gates, critical experiment, auxiliary assumptions, uncertainty architecture and decision rule.

Its qualification rule is

```math
\mathcal Q(H_i)=\bigwedge_{r=1}^{12}Q_{ir}.
```

Exact $\delta_1,\ldots,\delta_5$, $\Omega_H$, and final confirmatory procedures remain unfrozen until the demonstrator and evidence base are established.

---

## 4. Minimal Sufficient Experimental Realization

[`MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md) governs demonstrator reduction.

```math
\text{Full scientific framework}\neq\text{experimental demonstrator}.
```

The target is

```math
\mathcal M_D^*
=
\text{minimum-complexity realization preserving the discriminatory power of }H_1-H_5.
```

Reduction concerns resolution, not causal scope. The actual demonstrator remains unfrozen.

---

## 5. Closed-corpus evidence-selection engine

[`CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md`](CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md) assigns the frozen 325-paper PRISMA-style + Monte Carlo protocol a specific role:

```math
325\text{-paper corpus}
\rightarrow
\text{robust evidence ranking}
\rightarrow
\text{best records for }H_1-H_5
\rightarrow
\text{full-text extraction}.
```

The ranking can prioritize records within the frozen corpus; it cannot establish governing equations, parameter values, physical assumptions or validation adequacy without full-text extraction.

---

## 6. FTEE v1.0 — full-text evidence-to-equation extraction

[`FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md`](FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md) is the first operational protocol after ranking.

Its central transformation is

```math
\text{paper}
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

The evidence unit is

```math
 e_{ij}=(S_i,L_{ij},C_{ij},M_{ij},F_{ij},X_{ij},\theta_{ij},A_{ij},\Omega_{ij},V_{ij},U_{ij},H_{ij}).
```

FTEE enforces exact provenance, source notation before thesis canonicalization, separate mechanism/form/validation evidence, units and dimensional checks, parameter/timescale provenance, assumptions, VVUQ separation, validation domains, uncertainty treatment, transferability, hypothesis mapping, explicit missingness, and no silent equation completion.

Its methodological boundary is

```math
\textbf{FTEE extracts and qualifies evidence; it does not yet choose the demonstrator.}
```

**Status:** PILOT-READY / NOT FROZEN. The codebook must be piloted on a heterogeneous ranked-paper subset before FTEE is frozen for full-scale extraction.

---

## 7. Evidence-to-demonstrator pipeline

```math
\begin{aligned}
&\textbf{A: }325\text{-paper ranking}\\
&\rightarrow\textbf{B: }H_1-H_5\text{ evidence sets}\\
&\rightarrow\textbf{C1: FTEE codebook pilot and freeze}\\
&\rightarrow\textbf{C2: full-text evidence-unit extraction}\\
&\rightarrow\textbf{D: candidate demonstrator architectures}\\
&\rightarrow\textbf{E: scientific sufficiency + V\&V feasibility comparison}\\
&\rightarrow\textbf{F: freeze }\mathcal M_D^*.
\end{aligned}
```

Only after this evidence chain should $\Omega_H$, $\Omega_V$, $\delta_i$, acceptance criteria, and final confirmatory analysis procedures be frozen *a priori*.

---

## 8. Repository rendering contract

Active Markdown follows [`MATHEMATICAL_PRESENTATION_V3.md`](MATHEMATICAL_PRESENTATION_V3.md): inline `$...$`; fenced `math` for multiline/complex display mathematics; no fragile `\tag{...}`; no paragraph-length boxes; consistent tables; and distinct notation for $u(t)$, $\mathbf a_k$, $a_{ij}$ and $\varepsilon$.

Historical/archive material remains provenance only unless explicitly reintroduced through a versioned revision.
