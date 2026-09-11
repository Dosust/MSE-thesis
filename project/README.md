# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/framework-7--stage%20canonical-0969DA)
![Frozen](https://img.shields.io/badge/stages%202--6-FROZEN-1A7F37)
![Research](https://img.shields.io/badge/Stage%207-DEEP%20RESEARCH-9A6700)

This directory contains the **active mathematical and scientific specification** of the MSE thesis. Historical material is retained separately for provenance and must not override the canonical files listed below.

> **Latest cross-audit:** [`../provenance/2026-09-11_PROJECT_MATHEMATICAL_DISPLAY_CONTENT_AUDIT.md`](../provenance/2026-09-11_PROJECT_MATHEMATICAL_DISPLAY_CONTENT_AUDIT.md)

## Current framework status

```mermaid
flowchart LR
    S1["1 · Multilayer Structure"] --> S2["2 · Causal Mechanisms"]
    S2 --> S3["3 · Coupled Hybrid Multiscale Dynamics"]
    S3 --> S4["4 · Observation, Organization, Feedback and Control"]
    S4 --> S5["5 · Viability"]
    S5 --> S6["6 · Resilience-to-Sustainability Transformation Interface"]
    S6 --> S7["7 · Sustainable Transformation Pathways"]

    classDef canonical fill:#DDF4FF,stroke:#0969DA,color:#0B1F33,stroke-width:2px;
    classDef frozen fill:#DAFBE1,stroke:#1A7F37,color:#0B1F33,stroke-width:2px;
    classDef research fill:#FFF8C5,stroke:#9A6700,color:#0B1F33,stroke-width:2px;

    class S1 canonical;
    class S2,S3,S4,S5,S6 frozen;
    class S7 research;
```

**Color semantics:** blue = canonical system definition; green = frozen scientific scope; amber = active research/not-yet-frozen scope. Color is never the sole carrier of meaning.

## Canonical authority map

| Priority | File | Role | Status |
|---:|---|---|---|
| 1 | [`THESIS_SCOPE.md`](THESIS_SCOPE.md) | Current scientific scope and stage boundaries | Canonical |
| 2 | [`CANONICAL_7_STAGE_FRAMEWORK.md`](CANONICAL_7_STAGE_FRAMEWORK.md) | Seven-stage architecture and current status map | Canonical |
| 3 | [`CANONICAL_SYSTEM_DEFINITION.md`](CANONICAL_SYSTEM_DEFINITION.md) | P–T–I–O system identity and state ontology | Canonical |
| 4 | [`FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md) | Framework-level subsystem decomposition | Canonical |
| 5 | [`STAGES_1_2_APA7_EVIDENCE_GROUNDED.md`](STAGES_1_2_APA7_EVIDENCE_GROUNDED.md) | Literature-grounded Stages 1–2 companion | Canonical companion |
| 6 | [`STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](STAGE_2_INTERDEPENDENCY_MECHANISMS.md) | Stage-2 causal interdependency specification | Frozen |
| 7 | [`STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md) | Stage-3 dynamic architecture | Frozen |
| 8 | [`STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md) | Stage-4 observation-to-action architecture | Frozen |
| 9 | [`STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md) | Stage-5 viability architecture | Frozen |
| 10 | [`STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md`](STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md) | Stage-6 regime-adequacy/translation architecture | **Frozen** |
| 11 | [`STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md`](STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md) | Stage-7 ten-pass deep research and candidate mathematics | **Research — not frozen** |
| 12 | [`MATHEMATICAL_FOUNDATION.md`](MATHEMATICAL_FOUNDATION.md) | Cross-stage mathematical foundation | Synchronized through Stage 6 |
| 13 | [`SCIENTIFIC_PROPOSITIONS.md`](SCIENTIFIC_PROPOSITIONS.md) | Falsifiable thesis propositions | Synchronized through Stage 6 |
| 14 | [`MATHEMATICAL_PRESENTATION_V3.md`](MATHEMATICAL_PRESENTATION_V3.md) | Mathematical display and visual-encoding standard | Synchronized |

## Canonical state and control notation

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix},
\qquad
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
$$

The physical state is

$$
X(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)
\end{bmatrix}.
$$

The Stage-4 feedback spine is

$$
X(t)\rightarrow y(t)\rightarrow I(t)\rightarrow\widehat X(t)\rightarrow O(t)\rightarrow u(t)\rightarrow X(t).
$$

The Stage-5 core is

$$
K_{\mathrm{sus}}
\supseteq
\mathcal V_{\mathrm{sus}}^{u,T}
\rightarrow
\partial\mathcal V
\rightarrow
\{\rho,T_{\mathcal V},T_K\}.
$$

The frozen Stage-6 translation is

$$
\Phi_{\mathrm{ST}}
:
(\mathcal R_5,\Lambda_{\mathrm{LT}},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol{\zeta}_T).
$$

Stage 7 begins from

$$
(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)
\longrightarrow
\text{candidate interventions and transformation pathways}.
$$

Its exact terminal mathematical object remains under research and is not frozen.

## Mathematical rendering standard

For GitHub-facing project files:

1. use inline math with `$...$` and display math with `$$...$$`;
2. use `aligned`, `bmatrix`, `cases`, or short equations for multiline mathematics;
3. do not place long prose sentences inside `\boxed{...}`;
4. avoid equation `\tag{...}` in Markdown; use a Markdown label immediately above the display when an equation ID is required;
5. use `\widehat X`, `\mathcal V`, `\partial\mathcal V`, `\mathrm{...}`, and other notation consistently across files;
6. keep intervention/control as $u(t)$ and measurement noise as $\varepsilon_k(t)$;
7. use tables when a long equation is really a specification or taxonomy;
8. use Mermaid only for architecture/topology, never as a substitute for a mathematical definition;
9. use color only for semantic categories and always duplicate meaning with text labels;
10. preserve APA 7 author–date citations and canonical DOI URLs.

## Historical material

[`research_memory/`](research_memory/) and [`ADAPTIVE_VISUAL_CI_EXCEPTION_2026-08-22.md`](ADAPTIVE_VISUAL_CI_EXCEPTION_2026-08-22.md) are historical/provenance material. They may contain superseded P–W–T–SW or earlier architectures and are not current scientific authority.

The active project files above override historical material whenever a conflict occurs.
