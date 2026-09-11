# MSE Thesis — Multilayer Interdependent Power–Transportation Infrastructure Resilience

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![Matrix](https://img.shields.io/badge/confirmatory%20matrix-CURRENT-0969DA)
![MSER](https://img.shields.io/badge/minimal%20sufficient%20realization-CURRENT-0969DA)
![Evidence](https://img.shields.io/badge/325--paper%20pipeline-CURRENT-0969DA)
![FTEE](https://img.shields.io/badge/FTEE%20v1.0-PILOT--READY-9A6700)

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** active thesis source of truth  
**Framework status:** complete seven-stage conceptual and mathematical framework frozen  
**Hypothesis status:** five-primary-hypothesis logic frozen; numerical thresholds/test specifications not yet frozen  
**Current operational phase:** closed-corpus evidence selection → FTEE pilot/freeze → full-text evidence extraction → demonstrator synthesis  
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
| [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md) | P–T–I–O identity and state ontology |
| [`project/RESEARCH_HYPOTHESES.md`](project/RESEARCH_HYPOTHESES.md) | five primary confirmatory hypotheses |
| [`project/ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](project/ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md) | confirmatory operationalization and VVUQ gates |
| [`project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md) | demonstrator-reduction methodology |
| [`project/CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md`](project/CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md) | 325-paper evidence-selection engine |
| [`project/FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md`](project/FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md) | full-text evidence-to-equation extraction protocol |
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

The seven-stage architecture and H1–H5 scientific logic are frozen. Exact thresholds $\delta_i$, hypothesis domains $\Omega_H$, validation domains $\Omega_V$, and final analysis procedures remain to be specified *a priori* from the evidence base and selected demonstrator.

---

## Evidence-to-demonstrator operational pipeline

The frozen 325-paper corpus is used as a closed evidence-selection engine:

```math
325\text{-paper corpus}
\rightarrow
\text{robust ranking}
\rightarrow
H_1-H_5\text{ priority evidence sets}.
```

FTEE v1.0 then governs full-text evidence extraction:

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

The end-to-end operational sequence is

```math
\begin{aligned}
&\textbf{Phase A: }325\text{-paper closed-corpus ranking}\\
&\downarrow\\
&\textbf{Phase B: }H_1-H_5\text{-specific evidence sets}\\
&\downarrow\\
&\textbf{Phase C1: FTEE extraction-table/codebook pilot and freeze}\\
&\downarrow\\
&\textbf{Phase C2: full-text evidence-unit extraction}\\
&\downarrow\\
&\textbf{Phase D: candidate P--T--I--O demonstrator architectures}\\
&\downarrow\\
&\textbf{Phase E: scientific sufficiency + V\&V feasibility comparison}\\
&\downarrow\\
&\textbf{Phase F: freeze the minimal sufficient demonstrator }\mathcal M_D^*.
\end{aligned}
```

---

## FTEE v1.0 status

[`project/FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md`](project/FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md) is **PILOT-READY / NOT YET FROZEN**.

It enforces:

- evidence-unit rather than paper-level extraction;
- exact source-location provenance;
- source notation before thesis canonicalization;
- separate mechanism, mathematical-form and validation evidence;
- units/dimensions, parameters, timescales and assumptions;
- verification, validation, calibration, sensitivity and UQ separation;
- validation-domain tracking;
- explicit missingness and uncertainty handling;
- P–T–I–O transferability and $H_1$–$H_5$ mapping;
- no silent equation completion;
- extraction before model synthesis;
- explicit evidence-unit and governing-equation acceptance gates.

Its boundary is

```math
\textbf{FTEE extracts and qualifies evidence; it does not yet choose the demonstrator.}
```

The next operational deliverable is the **Evidence-to-Equation extraction table/codebook**, followed by a deliberately heterogeneous pilot across ranked papers before FTEE is frozen for full-scale extraction.

---

## Repository rendering and QA

Active Markdown follows `project/MATHEMATICAL_PRESENTATION_V3.md`: fenced `math` blocks for multiline/complex displays, inline `$...$`, no fragile `\tag{...}`, no paragraph-length boxes, consistent tables, and explicit notation separation.

`tools/thesis_display_lint.py` and `.github/workflows/scientific-architecture-qa.yml` enforce the machine-checkable presentation and ontology rules.
