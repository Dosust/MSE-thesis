# Project Memory Entry Point

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
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
14. [`project/MATHEMATICAL_FOUNDATION.md`](project/MATHEMATICAL_FOUNDATION.md)
15. [`project/SCIENTIFIC_PROPOSITIONS.md`](project/SCIENTIFIC_PROPOSITIONS.md)
16. [`project/MATHEMATICAL_PRESENTATION_V3.md`](project/MATHEMATICAL_PRESENTATION_V3.md)
17. [`figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md`](figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md)

The file `project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md` is research provenance and is superseded by the frozen Stage-7 specification whenever they differ.

---

## Canonical system

$$
\mathcal S=\{P,T,I,O\},
$$

where

$$
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
$$

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

$$
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
$$

---

## Stage-7 notation

The candidate future regime is

$$
\mathfrak M_k
=
(\mathcal S_k,\mathcal G_k,\mathfrak I_k,F_k,\Theta_k,K_{{\rm sus},k},\mathcal U_k).
$$

The strategic transformation vector is

$$
\mathbf a_k
=
[a_k^P,a_k^T,a_k^I,a_k^O,a_k^{\mathfrak I}]^\top.
$$

The transformation is

$$
\mathfrak M_{k+1}
=
\mathcal T_{\mathbf a_k}(\mathfrak M_k,\xi_k).
$$

The fundamental Stage-7 object is

$$
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
$$

Operational and strategic actions are distinct:

$$
\underbrace{u(t)}_{\text{operate current regime}}
\neq
\underbrace{\mathbf a_k}_{\text{transform regime}}.
$$

Stage-2 activation $a_{ij}$ is also distinct from $\mathbf a_k$.

---

## Primary hypothesis status

The primary confirmatory set is

$$
\mathbb H=\{H_1,H_2,H_3,H_4,H_5\}.
$$

The hypothesis logic is frozen. Numerical thresholds $\delta_1,\ldots,\delta_5$, exact scenario ensembles, metrics and confirmatory decision rules remain unfrozen until specified *a priori* in the Hypothesis Specification Matrix.

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

The next task is the Hypothesis Specification Matrix, followed by numerical case-study design, computation, falsification and validation.
