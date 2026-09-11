# Closed-Corpus Evidence Selection Pipeline — Provenance Record

**Date:** 2026-09-11  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Source:** user-approved methodological note defining the role of the frozen 325-paper PRISMA-style + Monte Carlo protocol in demonstrator design.

## Decision recorded

The frozen 325-paper corpus will be used as the first-stage evidence-selection engine for the operationalization phase:

```math
325\text{-paper corpus}
\rightarrow
\text{robust evidence ranking}
\rightarrow
\text{best records for }H_1-H_5
\rightarrow
\text{full-text evidence extraction}.
```

The downstream full-text extraction target is:

```math
\text{paper}
\rightarrow
\text{mechanism}
\rightarrow
\text{equation}
\rightarrow
\text{parameter}
\rightarrow
\text{data/benchmark}
\rightarrow
\text{hypothesis}.
```

## Claim boundary

The closed-corpus ranking may identify priority records **within the frozen 325-record dataset only**. It must not be used to claim global literature optimality or to infer equation-level content, parameters, physical assumptions, benchmark data or validation evidence that were not available in the locked CSV.

Those questions require a separate full-text extraction stage.

## Current six-phase workflow

```math
\begin{aligned}
&\textbf{A: }325\text{-paper closed-corpus ranking}\\
&\rightarrow\textbf{B: }H_1-H_5\text{-specific evidence sets}\\
&\rightarrow\textbf{C: full-text mechanism/equation extraction}\\
&\rightarrow\textbf{D: candidate demonstrator architectures}\\
&\rightarrow\textbf{E: scientific sufficiency + V\&V feasibility comparison}\\
&\rightarrow\textbf{F: freeze the minimal sufficient }P-T-I-O\text{ demonstrator.}
\end{aligned}
```

Canonical methodology file:

`project/CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md`
