# Project Memory Entry Point

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![Matrix](https://img.shields.io/badge/confirmatory%20matrix-CURRENT-0969DA)
![Demonstrator](https://img.shields.io/badge/minimal%20sufficient%20realization-CURRENT-0969DA)
![Evidence](https://img.shields.io/badge/325--paper%20pipeline-CURRENT-0969DA)
![QA](https://img.shields.io/badge/display%20%26%20ontology-QA%20AUTOMATED-0969DA)

## Repository authority — 2026-09-11

The sole active repository for this thesis is `Dossiya-SE/MSE-thesis`.

All active thesis framework revisions, equations, figures, research notes, evidence records, validation artifacts and canonical files belong in this repository unless explicitly instructed otherwise.

`Dossiya-SE/Optimization-for-sustainability-and-resilience` is historical/reference only.

For current navigation, start with [`project/README.md`](project/README.md).

---

## Citation and evidence standard

The thesis-wide citation standard is **APA 7th edition**. A citation must not support a stronger claim than its source establishes. Proposed thesis objects remain labeled `[P]` after framework freeze until validation justifies another evidence status.

---

## Active authority order

1. [`project/README.md`](project/README.md)
2. [`project/THESIS_SCOPE.md`](project/THESIS_SCOPE.md)
3. [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md)
4. [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md)
5. [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md)
6. [`project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md`](project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md)
7. [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md)
8. [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)
9. [`project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md)
10. [`project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md)
11. [`project/STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md`](project/STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md)
12. [`project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md`](project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md)
13. [`project/RESEARCH_HYPOTHESES.md`](project/RESEARCH_HYPOTHESES.md)
14. [`project/ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](project/ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md)
15. [`project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md)
16. [`project/CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md`](project/CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md)
17. [`project/MATHEMATICAL_FOUNDATION.md`](project/MATHEMATICAL_FOUNDATION.md)
18. [`project/SCIENTIFIC_PROPOSITIONS.md`](project/SCIENTIFIC_PROPOSITIONS.md)
19. [`project/MATHEMATICAL_PRESENTATION_V3.md`](project/MATHEMATICAL_PRESENTATION_V3.md)
20. [`figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md`](figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md)

The file `project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md` is research provenance and is superseded by the frozen Stage-7 specification whenever they differ.

---

## Canonical system

```math
\mathcal S=\{P,T,I,O\},
```

where

```math
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
```

Canonical description:

> **A multilayer physical–informational–organizational interdependent Power–Transportation infrastructure system.**

---

## Frozen stage objects

| Stage | Canonical object / relation |
|---:|---|
| **1** | $\mathcal S$, $Y=[x_P,x_T,z_I,z_O]^\top$ |
| **2** | $\mathfrak I_{ij}^{\alpha\beta}$ |
| **3** | $F_{\mathcal G}^{m}$, $\widetilde Y=(Y,m)$ |
| **4** | $X\to y\to I\to\widehat X\to O\to u\to X$ |
| **5** | $K_{\rm sus}$, $\mathcal V_{\rm sus}^{u,T}$, $\rho$, $T_{\mathcal V}$, $T_K$ |
| **6** | $\Phi_{\rm ST}\mapsto(c_6,\mathcal D_6,\boldsymbol\zeta_T)$ |
| **7** | $\mathfrak P_{\rm ST}$ |

The complete frozen chain is

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
\underbrace{K_{\rm sus},\mathcal V,\rho,T_{\mathcal V},T_K}_{5}\\
&\rightarrow
\underbrace{\Phi_{\rm ST}\rightarrow(c_6,\mathcal D_6,\boldsymbol\zeta_T)}_{6}\\
&\rightarrow
\underbrace{\mathfrak P_{\rm ST}}_{7}.
\end{aligned}
```

---

## Stage-7 notation

The candidate future regime is

```math
\mathfrak M_k
=
(\mathcal S_k,\mathcal G_k,\mathfrak I_k,F_k,\Theta_k,K_{{\rm sus},k},\mathcal U_k).
```

The strategic transformation vector is

```math
\mathbf a_k
=
[a_k^P,a_k^T,a_k^I,a_k^O,a_k^{\mathfrak I}]^\top.
```

The transformation is

```math
\mathfrak M_{k+1}
=
\mathcal T_{\mathbf a_k}(\mathfrak M_k,\xi_k).
```

The fundamental Stage-7 object is

```math
\mathfrak P_{\rm ST}
=
\left(
\mathbb G_{\rm ST},
\boldsymbol\pi_{\rm ST},
\Omega,
\mathcal A^{\rm feas},
\mathbf J,
\mathbb M_{\rm sus}
\right).
```

Operational and strategic actions are distinct:

```math
\underbrace{u(t)}_{\text{operate current regime}}
\neq
\underbrace{\mathbf a_k}_{\text{transform regime}}.
```

Stage-2 activation $a_{ij}$ is also distinct from $\mathbf a_k$.

---

## Primary hypothesis status

The primary confirmatory set is

```math
\mathbb H=\{H_1,H_2,H_3,H_4,H_5\}.
```

The hypothesis logic is frozen. Numerical thresholds $\delta_1,\ldots,\delta_5$, exact scenario ensembles, metrics and confirmatory decision rules remain unfrozen until specified *a priori*.

---

## Engineering Confirmatory Hypothesis Matrix

The current operationalization specification is [`project/ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](project/ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md).

It combines confirmatory-science discipline, systems engineering, physics-based modelling and VVUQ. For each $H_i$, it stores the scientific gap, premise, mechanism, variables, estimand, baseline, strong rival, context of use, model-use domain, quantitative prediction, meaningful-effect requirement, physics/V&V gates, critical experiment, auxiliary assumptions, uncertainty architecture, decision rule and evidence/novelty status.

Its qualification rule is

```math
\mathcal Q(H_i)=\bigwedge_{r=1}^{12}Q_{ir}.
```

The exact 12-gate formulation is a derived/proposed thesis methodology `[D/P]`, not an ISO/ASME standard. The matrix explicitly leaves $\delta_1,\ldots,\delta_5$, exact $\Omega_H$ and final analysis procedures unfrozen until the reduced P–T–I–O demonstrator and available physical/data/benchmark evidence are established.

---

## Minimal Sufficient Experimental Realization

The current demonstrator-selection methodology is [`project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md).

Its foundational distinction is

```math
\text{Full scientific framework}\neq\text{experimental demonstrator}.
```

The seven-stage framework remains fully intact. Reduction applies only to the bounded experimental realization used for confirmatory evaluation.

The governing optimization principle is

```math
\mathcal M_D^*
=
\arg\min_{\mathcal M_D}C(\mathcal M_D)
```

subject to representation of $P,T,I,O$, preservation of every mechanism needed to discriminate $H_1$–$H_5$, falsifiability, $\Omega_H\subseteq\Omega_V$, sufficient identifiability, feasible V&V and UQ, and preservation of key outputs to the required accuracy.

The thesis shorthand is

```math
\boxed{\textbf{Reduce complexity, not causal content.}}
```

Reduction stops when removing another component would eliminate a hypothesis-relevant mechanism, observable, competing explanation or critical experiment. The actual demonstrator topology, component selection, hazard family, parameterization and validation domain remain **unfrozen**.

---

## Closed-corpus evidence-selection methodology

The current evidence-selection specification is [`project/CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md`](project/CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md).

The frozen 325-paper PRISMA-style + Monte Carlo protocol is now explicitly assigned the role of **evidence-selection engine** for demonstrator design:

```math
325\text{-paper corpus}
\rightarrow
\text{robust evidence ranking}
\rightarrow
\text{best records for }H_1-H_5
\rightarrow
\text{full-text evidence extraction}.
```

The ranked records then enter an evidence-to-equation extraction stage:

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

The closed-corpus ranking may support only corpus-bounded priority claims. Because that ranking stage is restricted to the CSV and excludes PDFs, abstracts, websites and external databases, it cannot establish equation-level adequacy, parameter values, physical assumptions or validation evidence. Those require second-stage full-text extraction.

The operational pipeline is:

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

---

## Automated QA

Active thesis presentation/configuration is checked by:

- `tools/thesis_display_lint.py` — Markdown math, tables/fences, active ontology drift and registry invariants;
- `.github/workflows/scientific-architecture-qa.yml` — Python, YAML, JSON Schema, SVG and Julia smoke/contract tests;
- `project/MATHEMATICAL_PRESENTATION_V3.md` — human-readable rendering contract;
- `figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md` — mandatory figure-level fidelity checks.

Historical/provenance trees are deliberately excluded from ontology rewriting. Preserving history is not the same as allowing historical content to control the active thesis.

---

## Current phase

> **STAGES 1–7: CONCEPTUAL AND MATHEMATICAL FRAMEWORK FROZEN.**

> **PRIMARY HYPOTHESIS LOGIC $H_1$–$H_5$: FROZEN; NUMERICAL THRESHOLDS NOT YET FROZEN.**

> **ENGINEERING CONFIRMATORY HYPOTHESIS MATRIX: CURRENT OPERATIONALIZATION SPECIFICATION.**

> **MINIMAL SUFFICIENT EXPERIMENTAL REALIZATION METHODOLOGY: CURRENT; ACTUAL DEMONSTRATOR NOT YET FROZEN.**

> **325-PAPER CLOSED-CORPUS EVIDENCE-SELECTION PIPELINE: CURRENT.**

The immediate next task is **Phase A: run the frozen 325-paper closed-corpus PRISMA–Monte Carlo ranking**, then form hypothesis-specific evidence sets for $H_1$–$H_5$, followed by full-text mechanism/equation extraction. Only after that evidence chain should candidate demonstrator architectures be compared and the actual minimal sufficient P–T–I–O demonstrator frozen.
