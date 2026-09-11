# Closed-Corpus Evidence Selection Pipeline for Demonstrator Design

**Status:** CURRENT EVIDENCE-SELECTION METHODOLOGY  
**Corpus:** frozen 325-paper dataset  
**Purpose:** use the existing PRISMA-style + Monte Carlo ranking protocol as the evidence-selection engine for demonstrator design  
**Scope rule:** ranking is restricted to the frozen 325-record corpus; full-text mechanism/equation extraction is a separate second-stage task

I reviewed the GitHub file. It is a **closed-corpus PRISMA-style + Monte Carlo ranking protocol** for the frozen 325-paper dataset, and it is methodologically useful for the next phase of the thesis.

Its strongest features are the strict **single-dataset lock**, hash/schema checks, duplicate/identity gates, anti-leakage rules, separation of scientific relevance from evidence confidence, explicit missing-data handling, Beta uncertainty on criterion scores, and Dirichlet uncertainty on ranking weights. It also correctly limits claims to “best papers within this 325-record corpus,” rather than pretending the corpus represents all global literature.

For our current work, I would use this prompt for a very specific purpose:

```math
\text{325-paper corpus}
\rightarrow
\text{robust evidence ranking}
\rightarrow
\text{best papers for }H_1-H_5
\rightarrow
\text{full-text evidence extraction}.
```

Then the selected full-text papers would feed the **reduced-demonstrator design**, especially the evidence-to-equation matrix:

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

One important limitation: because this master prompt explicitly forbids using PDFs, abstracts, external databases, websites, or information outside the CSV, its Monte Carlo score can identify **which records deserve priority**, but it cannot by itself determine whether a paper contains the governing equations, parameter values, validation data, or physical assumptions required for the demonstrator. That must be a **second-stage full-text extraction** after ranking.

So I would structure the research pipeline as:

```math
\begin{aligned}
&\textbf{Phase A: }325\text{-paper closed-corpus ranking}\\
&\downarrow\\
&\textbf{Phase B: hypothesis-specific evidence set for }H_1-H_5\\
&\downarrow\\
&\textbf{Phase C: full-text mechanism/equation extraction}\\
&\downarrow\\
&\textbf{Phase D: candidate demonstrator architectures}\\
&\downarrow\\
&\textbf{Phase E: scientific-sufficiency + V\&V feasibility comparison}\\
&\downarrow\\
&\textbf{Phase F: freeze the minimal sufficient }P-T-I-O\text{ demonstrator.}
\end{aligned}
```

The key point is that the existing PRISMA–Monte Carlo protocol can now become the **evidence-selection engine** for designing the demonstrator rather than starting a new literature search from zero.

---

## Methodological boundary

The closed-corpus ranking stage may support claims of the form:

> **highest-priority records within the frozen 325-paper corpus under the declared ranking model.**

It must not be interpreted as proving:

- that the selected records are globally the best literature;
- that every selected record contains usable governing equations;
- that equation-level parameterization or validation evidence has already been established;
- that full-text scientific adequacy can be inferred from CSV-only metadata/fields.

Those questions belong to the second-stage full-text evidence extraction.

---

## Thesis integration

This pipeline connects the current operationalization artifacts as follows:

```math
\text{Confirmatory }H_1-H_5
\rightarrow
\text{closed-corpus evidence ranking}
\rightarrow
\text{full-text evidence-to-equation extraction}
\rightarrow
\text{candidate MSER designs}
\rightarrow
\text{V\&V feasibility comparison}
\rightarrow
\mathcal M_D^*.
```

The pipeline therefore serves the **Minimal Sufficient Experimental Realization** methodology without changing the frozen seven-stage framework or the frozen primary-hypothesis logic.
