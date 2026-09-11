# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/framework-7--stage%20canonical-0969DA)
![Frozen](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/primary%20hypotheses-H1--H5%20LOGIC%20FROZEN-1A7F37)
![Next](https://img.shields.io/badge/next-Hypothesis%20Specification%20Matrix-9A6700)

This directory contains the **active mathematical and scientific specification** of the MSE thesis. The seven-stage conceptual and mathematical framework is frozen. The five-primary-hypothesis logic is also frozen, while numerical thresholds and exact confirmatory test specifications remain to be fixed *a priori*.

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

    class S1 canonical;
    class S2,S3,S4,S5,S6,S7 frozen;
```

**Color semantics:** blue = canonical system definition; green = frozen scientific scope. Color is never the sole carrier of meaning.

## Canonical authority map

| Priority | File | Role | Status |
|---:|---|---|---|
| 1 | [`THESIS_SCOPE.md`](THESIS_SCOPE.md) | Current scientific scope and stage boundaries | Canonical / frozen |
| 2 | [`CANONICAL_7_STAGE_FRAMEWORK.md`](CANONICAL_7_STAGE_FRAMEWORK.md) | Complete seven-stage architecture and mathematics | Canonical / frozen |
| 3 | [`CANONICAL_SYSTEM_DEFINITION.md`](CANONICAL_SYSTEM_DEFINITION.md) | P–T–I–O system identity and state ontology | Canonical |
| 4 | [`FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md) | Framework-level subsystem decomposition | Canonical |
| 5 | [`STAGES_1_2_APA7_EVIDENCE_GROUNDED.md`](STAGES_1_2_APA7_EVIDENCE_GROUNDED.md) | Literature-grounded Stages 1–2 companion | Canonical companion |
| 6 | [`STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](STAGE_2_INTERDEPENDENCY_MECHANISMS.md) | Stage-2 causal interdependency specification | Frozen |
| 7 | [`STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md) | Stage-3 dynamic architecture | Frozen |
| 8 | [`STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md) | Stage-4 observation-to-action architecture | Frozen |
| 9 | [`STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md) | Stage-5 viability architecture | Frozen |
| 10 | [`STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md`](STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md) | Stage-6 regime-adequacy/translation architecture | Frozen |
| 11 | [`STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md`](STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md) | Stage-7 adaptive transformation architecture | **Frozen** |
| 12 | [`RESEARCH_HYPOTHESES.md`](RESEARCH_HYPOTHESES.md) | Five primary confirmatory hypotheses and falsification logic | **Logic frozen; thresholds not set** |
| 13 | [`MATHEMATICAL_FOUNDATION.md`](MATHEMATICAL_FOUNDATION.md) | Cross-stage mathematical foundation | Active companion |
| 14 | [`SCIENTIFIC_PROPOSITIONS.md`](SCIENTIFIC_PROPOSITIONS.md) | Broader falsifiable proposition registry | Active companion |
| 15 | [`MATHEMATICAL_PRESENTATION_V3.md`](MATHEMATICAL_PRESENTATION_V3.md) | Mathematical display and visual-encoding standard | Synchronized |

The former [`STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md`](STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md) is retained as research provenance and does not override the frozen Stage-7 file.

## Frozen mathematical chain

$$
\boxed{
\underbrace{\mathcal S}_{1}
\rightarrow
\underbrace{\mathfrak I}_{2}
\rightarrow
\underbrace{F_{\mathcal G}^{m}}_{3}
\rightarrow
\underbrace{X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u}_{4}
\rightarrow
\underbrace{K_{\rm sus},\mathcal V,\rho,T_{\mathcal V},T_K}_{5}
\rightarrow
\underbrace{\Phi_{\rm ST}\rightarrow(c_6,\mathcal D_6,\boldsymbol\zeta_T)}_{6}
\rightarrow
\underbrace{\mathfrak P_{\rm ST}}_{7}
}.
$$

The frozen Stage-7 fundamental object is

$$
\mathfrak P_{\rm ST}
=
(\mathbb G_{\rm ST},\boldsymbol\pi,\Omega,\mathcal A^{\rm feas},\mathbf J,\mathbb M_{\rm sus}).
$$

Stage 7 is interpreted as an **adaptive, viability-constrained, many-objective reachability problem over a graph of evolving P–T–I–O infrastructure architectures**.

## Primary hypothesis architecture

The frozen primary hypothesis set is

$$
\mathbb H=\{H_1,H_2,H_3,H_4,H_5\},
$$

with the causal hierarchy

$$
\mathfrak I
\rightarrow
F
\rightarrow
(I,O,u)
\rightarrow
\mathcal V
\rightarrow
S_{ij}^{\mathcal V}
\rightarrow
\text{adaptive transformation}.
$$

The five primary tests are:

| Hypothesis | Main stages | Core test |
|---|---:|---|
| $H_1$ | 2 → 3 | dynamic causal coupling vs. independent/static coupling |
| $H_2$ | 3 → 4 | informational/organizational effects on feasible response and outcomes |
| $H_3$ | 4 → 5 | viability information beyond conventional service/recovery metrics |
| $H_4$ | 2 → 5 → 7 | viability-sensitive interface ranking vs. structural centrality |
| $H_5$ | 5 → 6 → 7 | adaptive pathway vs. best comparable fixed pathway under deep uncertainty |

The scientific logic is frozen. The thresholds $\delta_1,\ldots,\delta_5$ are deliberately **not** assigned until justified *a priori*.

## Stage-6 / Stage-7 separation

$$
\underbrace{\text{WHY / WHAT / HOW DEEP}}_{\text{Stage 6}}
\quad\rightarrow\quad
\underbrace{\text{WHICH / ORDER / WHEN / UNDER WHAT CONDITIONS}}_{\text{Stage 7}}.
$$

Stage-4 operational control $u(t)$ is distinct from Stage-7 structural transformation action $a_k$.

## Mathematical rendering standard

For GitHub-facing project files:

1. use inline math with `$...$` and display math with `$$...$$`;
2. use `aligned`, `bmatrix`, `cases`, or short equations for multiline mathematics;
3. avoid long prose inside mathematical boxes;
4. use tables when a long expression is primarily a taxonomy/specification;
5. preserve notation consistently across files;
6. keep operational control as $u(t)$ and transformation action as $a_k$;
7. use Mermaid only for architecture/topology;
8. use color only with redundant textual labels;
9. preserve APA 7 author–date citations and canonical DOI URLs.

## Next scientific phase

The conceptual framework is closed, but confirmatory simulation should not begin until the hypotheses are fully specified. The immediate sequence is

$$
\text{frozen framework}
\rightarrow
\text{frozen hypothesis logic}
\rightarrow
\textbf{Hypothesis Specification Matrix}
\rightarrow
\text{case-study design}
\rightarrow
\text{computation}
\rightarrow
\text{falsification}
\rightarrow
\text{validation}.
$$

The Hypothesis Specification Matrix must predefine theory, mechanism, variables, baselines, boundary conditions, predictions, rival hypotheses, critical tests, falsification criteria, uncertainty domains, and justified $\delta_i$ thresholds before confirmatory numerical testing.

Historical material remains provenance only unless explicitly reintroduced through a versioned revision.
