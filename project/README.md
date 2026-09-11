# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/framework-7--stage%20canonical-0969DA)
![Frozen](https://img.shields.io/badge/stages%202--5-FROZEN-1A7F37)
![Next](https://img.shields.io/badge/next-Stage%206-9A6700)

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
    classDef next fill:#FFF8C5,stroke:#9A6700,color:#0B1F33,stroke-width:2px;
    classDef downstream fill:#F6F8FA,stroke:#57606A,color:#24292F,stroke-width:1.5px;

    class S1 canonical;
    class S2,S3,S4,S5 frozen;
    class S6 next;
    class S7 downstream;
```

**Color semantics:** blue = canonical system definition; green = frozen scientific stage; amber = next formalization stage; gray = downstream stage. Color is never the sole carrier of meaning; every node is also labeled textually.

## Canonical authority map

| Priority | File | Role | Status |
|---:|---|---|---|
| 1 | [`THESIS_SCOPE.md`](THESIS_SCOPE.md) | Current scientific scope and stage boundaries | Canonical |
| 2 | [`CANONICAL_7_STAGE_FRAMEWORK.md`](CANONICAL_7_STAGE_FRAMEWORK.md) | Frozen seven-stage architecture | Canonical |
| 3 | [`CANONICAL_SYSTEM_DEFINITION.md`](CANONICAL_SYSTEM_DEFINITION.md) | P–T–I–O system identity and state ontology | Canonical |
| 4 | [`FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md) | Framework-level subsystem decomposition | Canonical |
| 5 | [`STAGES_1_2_APA7_EVIDENCE_GROUNDED.md`](STAGES_1_2_APA7_EVIDENCE_GROUNDED.md) | Literature-grounded Stages 1–2 companion | Canonical companion |
| 6 | [`STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](STAGE_2_INTERDEPENDENCY_MECHANISMS.md) | Stage-2 causal interdependency specification | Frozen |
| 7 | [`STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md) | Stage-3 dynamic architecture | Frozen |
| 8 | [`STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md) | Stage-4 observation-to-action architecture | Frozen |
| 9 | [`STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md) | Stage-5 viability architecture | Frozen |
| 10 | [`MATHEMATICAL_FOUNDATION.md`](MATHEMATICAL_FOUNDATION.md) | Cross-stage mathematical foundation | Synchronized |
| 11 | [`SCIENTIFIC_PROPOSITIONS.md`](SCIENTIFIC_PROPOSITIONS.md) | Falsifiable thesis propositions | Synchronized |
| 12 | [`MATHEMATICAL_PRESENTATION_V3.md`](MATHEMATICAL_PRESENTATION_V3.md) | Mathematical display and visual-encoding standard | Synchronized |

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

## Mathematical rendering standard

For GitHub-facing project files:

1. use inline math with `$...$` and display math with `$$...$$`;
2. use `aligned`, `bmatrix`, `cases`, or short equations for multiline mathematics;
3. do not place long prose sentences inside `\boxed{...}`;
4. avoid equation `\tag{...}` in Markdown; use a Markdown label such as **Equation S3.1** immediately above the display;
5. use `\widehat X`, `\mathcal V`, `\partial\mathcal V`, `\mathrm{...}`, and other notation consistently across files;
6. keep the intervention/control variable as $u(t)$ and measurement noise as $\varepsilon_k(t)$;
7. use tables when a long equation is really a specification or taxonomy rather than a mathematical identity;
8. use Mermaid only for architecture/topology, never as a substitute for a mathematical definition;
9. use color only for semantic categories and always duplicate the meaning with text labels;
10. preserve APA 7 author–date citations and canonical DOI URLs.

## Historical material

[`research_memory/`](research_memory/) and [`ADAPTIVE_VISUAL_CI_EXCEPTION_2026-08-22.md`](ADAPTIVE_VISUAL_CI_EXCEPTION_2026-08-22.md) are **historical/provenance material**. They may contain superseded P–W–T–SW or earlier six-chain concepts and therefore are not current scientific authority.

The active project files above override historical material whenever a conflict occurs.
