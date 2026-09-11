# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![Matrix](https://img.shields.io/badge/confirmatory%20matrix-CURRENT-0969DA)
![Thresholds](https://img.shields.io/badge/%CE%B41--%CE%B45-NOT%20SET-9A6700)

This directory is the active mathematical/scientific specification of the MSE thesis. The seven-stage framework and five-primary-hypothesis logic are frozen. The Engineering Confirmatory Hypothesis Matrix is now the current operationalization specification, while exact confirmatory thresholds, exact hypothesis domains and final analysis procedures remain to be defined *a priori*.

> **Automated presentation QA:** [`../tools/thesis_display_lint.py`](../tools/thesis_display_lint.py) checks active Markdown display rules, table/fence integrity, ontology drift, and machine-readable authority registries.

---

## 1. Framework status

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

Blue marks the canonical ontology stage; green marks frozen scientific scopes. Text labels remain authoritative without color.

---

## 2. Authority map

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
| 10 | [`STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md`](STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md) | Stage-6 regime-adequacy/translation architecture | frozen |
| 11 | [`STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md`](STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md) | Stage-7 adaptive transformation architecture | frozen |
| 12 | [`RESEARCH_HYPOTHESES.md`](RESEARCH_HYPOTHESES.md) | five primary confirmatory hypotheses | logic frozen; thresholds unset |
| 13 | [`ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md) | confirmatory operationalization, VVUQ gates, critical experiments, uncertainty and decision rules | current; numerical thresholds/domains/procedures not frozen |
| 14 | [`MATHEMATICAL_FOUNDATION.md`](MATHEMATICAL_FOUNDATION.md) | cross-stage mathematical foundation | active companion |
| 15 | [`SCIENTIFIC_PROPOSITIONS.md`](SCIENTIFIC_PROPOSITIONS.md) | broader proposition/falsification registry | active companion |
| 16 | [`MATHEMATICAL_PRESENTATION_V3.md`](MATHEMATICAL_PRESENTATION_V3.md) | notation, display, color and rendering contract | current |

The earlier `STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md` is research provenance only and cannot override the frozen Stage-7 specification.

---

## 3. Frozen mathematical chain

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

The terminal Stage-7 object is

```math
\mathfrak P_{\mathrm{ST}}
=
\left(
\mathbb G_{\mathrm{ST}},
\boldsymbol{\pi}_{\mathrm{ST}},
\Omega,
\mathcal A^{\mathrm{feas}},
\mathbf J,
\mathbb M_{\mathrm{sus}}
\right).
```

The Stage-7 regime is $\mathfrak M_k$ and its strategic action is $\mathbf a_k$. These are distinct from Stage-4 operational control $u(t)$ and Stage-2 activation $a_{ij}$.

---

## 4. Primary hypothesis architecture

The primary set is

```math
\mathbb H=\{H_1,H_2,H_3,H_4,H_5\}.
```

| Hypothesis | Main stages | Core test |
|---|---:|---|
| $H_1$ | 2 → 3 | dynamic causal coupling vs. independent/static coupling |
| $H_2$ | 3 → 4 | informational/organizational effects on feasible response and outcomes |
| $H_3$ | 4 → 5 | viability information beyond conventional service/recovery metrics |
| $H_4$ | 2 → 5 → 7 | viability-sensitive interface ranking vs. structural/flow baselines |
| $H_5$ | 5 → 6 → 7 | adaptive transformation policy vs. comparable fixed pathway under deep uncertainty |

The causal hierarchy is

```math
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
```

The scientific logic is frozen. $\delta_1,\ldots,\delta_5$ remain deliberately unset until justified before confirmatory testing.

---

## 5. Confirmatory operationalization matrix

The current operationalization layer is [`ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md). It connects each hypothesis to its scientific gap, premise, mechanism, variables, estimand, baseline, strong rival, context of use, quantitative prediction, V&V gates, critical experiment, auxiliary assumptions, uncertainty structure and decision rule.

Its governing qualification rule is

```math
\mathcal Q(H_i)=\bigwedge_{r=1}^{12}Q_{ir}.
```

The matrix explicitly keeps $\delta_1,\ldots,\delta_5$, exact $\Omega_H$ and final analysis procedures unfrozen until the reduced P–T–I–O demonstrator and available physical/data/benchmark evidence are selected.

---

## 6. Stage-6 / Stage-7 boundary

```math
\underbrace{\text{WHY / WHAT / HOW DEEP}}_{\text{Stage 6}}
\quad\longrightarrow\quad
\underbrace{\text{WHICH / ORDER / WHEN / CONDITIONS}}_{\text{Stage 7}}.
```

Stage 6 outputs $(c_6,\mathcal D_6,\boldsymbol\zeta_T)$. Stage 7 uses those requirements to generate and test adaptive strategic transformations.

---

## 7. Repository rendering contract

Active Markdown follows these rules:

1. inline mathematics uses `$...$`;
2. multiline or structurally complex display mathematics uses fenced `math` blocks;
3. short display mathematics may use `$$...$$` only when the complete expression and both delimiters remain on one line;
4. standalone `$$` delimiter lines are avoided because GitHub Markdown line-break handling can expose raw LaTeX;
5. no `\tag{...}` inside GitHub Markdown;
6. no paragraph-length text inside `\boxed{...}`;
7. long specifications use tables or multiline equations;
8. mathematical tables retain consistent columns;
9. $u(t)$, $\mathbf a_k$, $a_{ij}$ and $\varepsilon$ remain distinct;
10. color is semantic and always duplicated by text/shape/line style;
11. APA 7 author–date citations and canonical DOI URLs are preserved.

See [`MATHEMATICAL_PRESENTATION_V3.md`](MATHEMATICAL_PRESENTATION_V3.md) for the complete standard and [`../figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md`](../figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md) for figure QA.

---

## 8. Next scientific phase

The immediate sequence is

```math
\text{frozen framework}
\rightarrow
\text{frozen hypothesis logic}
\rightarrow
\text{confirmatory hypothesis matrix}
\rightarrow
\text{reduced P--T--I--O demonstrator selection}
\rightarrow
\text{benchmark/data evidence audit}
\rightarrow
\text{a-priori threshold and analysis specification}
\rightarrow
\text{case-study computation}
\rightarrow
\text{falsification}
\rightarrow
\text{validation}.
```

The next task is therefore to select the reduced P–T–I–O demonstrator and establish the physical/data/benchmark evidence needed to justify $\Omega_H$, $\Omega_V$, $\delta_i$ and the final confirmatory analysis procedures.

Historical and archived material remains provenance only unless explicitly reintroduced through a versioned revision.
