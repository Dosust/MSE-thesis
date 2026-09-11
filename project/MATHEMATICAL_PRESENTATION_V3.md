# MSE Thesis Mathematical Presentation and Rendering Standard

> **Filename note:** `MATHEMATICAL_PRESENTATION_V3.md` is retained for provenance, but this content is the current rendering standard.

**Status:** CURRENT / SYNCHRONIZED WITH FROZEN STAGES 1–7  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Scientific system:** P–T–I–O  
**Purpose:** Ensure that mathematical meaning survives GitHub, thesis, slide, SVG and publication rendering without notation drift.

---

## 1. Governing principle

> **CHANGE THE VISUAL HIERARCHY, NOT THE SCIENTIFIC CONTENT.**

A renderer may change typography, spacing, orientation or graphical encoding. It may not change equations, stage boundaries, variable meaning, evidence status or scientific conclusions.

---

## 2. Canonical display hierarchy

| Stage | Visual responsibility |
|---|---|
| **1 — Multilayer Structure** | show $P,T$ as physical systems and $I,O$ as informational/organizational layers |
| **2 — Causal Mechanisms** | show directional causal interfaces and $\mathfrak I_{ij}^{\alpha\beta}$ |
| **3 — Coupled Hybrid Multiscale Dynamics** | show state evolution, modes, events, delays, topology and timescales |
| **4 — Observation, Organization, Feedback and Control** | show measurement, inference, organizational feasibility, policy and actuation |
| **5 — Viability** | show acceptability, maintainability, viability boundary and geometric/temporal margins |
| **6 — Resilience-to-Sustainability Transformation Interface** | show regime-adequacy diagnosis and translation into transformation requirements |
| **7 — Sustainable Transformation Pathways** | show alternative regimes, strategic actions, triggers, uncertainty and adaptive pathways |

No figure may collapse distinct stages into one unlabeled chain when the full framework is being represented.

---

## 3. Evidence-state notation

| Label | Meaning |
|---|---|
| `[E]` | established literature/theory or directly supported evidence |
| `[D]` | derived synthesis from established components |
| `[P]` | proposed thesis construct requiring validation |

Computed outputs, simulations or fitted parameters must be described explicitly in captions/provenance. They must not be relabeled as empirical evidence unless they are data-derived.

---

## 4. Canonical state and action notation

The integrated state is

```math
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix},
\qquad
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
```

The physical state is

```math
X(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)
\end{bmatrix}.
```

The layer labels $I$ and $O$ denote functions/layers; their time-varying states are $z_I(t)$ and $z_O(t)$.

Operational and strategic actions remain distinct:

```math
\underbrace{u(t)}_{\text{Stage-4 operational control}}
\neq
\underbrace{\mathbf a_k}_{\text{Stage-7 strategic transformation}}.
```

Stage-2 activation $a_{ij}$ is also distinct from the Stage-7 strategic vector $\mathbf a_k$.

---

## 5. GitHub mathematical rendering rules

GitHub renders Markdown mathematics with MathJax. To avoid the raw-LaTeX failure visible when a multiline dollar-delimited block is parsed as ordinary Markdown, active `.md` files use the following contract:

1. inline mathematics uses `$...$`;
2. multiline or structurally complex display mathematics uses fenced `math` blocks;
3. short display mathematics may use `$$...$$` only when the complete expression and both delimiters stay on one line;
4. do **not** use standalone opening and closing `$$` lines for multiline mathematics;
5. multiline mathematics uses `aligned`, `bmatrix`, `cases`, or other MathJax-supported environments inside a fenced `math` block;
6. avoid paragraph-length prose inside `\boxed{...}`;
7. avoid `\tag{...}` in Markdown; put **Equation Sx.y — description** above the display when an identifier is needed;
8. prefer `\mathrm{...}` for short roman mathematical labels and `\text{...}` only for brief explanatory text;
9. long taxonomies/specifications belong in Markdown tables, not arrays inside equations;
10. do not place raw URLs or Markdown links inside equations;
11. distinguish $u(t)$ from $\varepsilon(t)$ and $\mathbf a_k$ from $a_{ij}$;
12. if an expression cannot fit comfortably at normal GitHub width, split it before publication;
13. table rows must preserve the declared number of columns.

These rules are enforced automatically where possible by `tools/thesis_display_lint.py` and normalized by `tools/normalize_github_math.py`.

---

## 6. Core equations to preserve

### Stage 1 — System state

```math
\mathcal S=\{P,T,I,O\}.
```

```math
Y(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)\\z_I(t)\\z_O(t)
\end{bmatrix}.
```

### Stage 2 — Causal interdependency

```math
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right).
```

### Stage 3 — Hybrid state

```math
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
```

### Stage 4 — Feedback spine

```math
X(t)
\rightarrow y(t)
\rightarrow I(t)
\rightarrow\widehat X(t)
\rightarrow O(t)
\rightarrow u(t)
\rightarrow X(t).
```

### Stage 5 — Viability hierarchy

```math
K_{\mathrm{sus}}
\supseteq
\mathcal V_{\mathrm{sus}}^{u,T}
\rightarrow
\partial\mathcal V
\rightarrow
\{\rho,T_{\mathcal V},T_K\}.
```

### Stage 6 — Transformation diagnosis

```math
\Phi_{\mathrm{ST}}
:
(\mathcal R_5,\Lambda_{\mathrm{LT}},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol{\zeta}_T).
```

### Stage 7 — Transformation pathway object

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

The Stage-7 regime is $\mathfrak M_k$ and the strategic action is $\mathbf a_k$.

---

## 7. Complete mathematical chain

For a compact full-framework representation use

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

---

## 8. Semantic color system

Color is permitted only when it clarifies scientific roles.

| Scientific role | Preferred color | Hex | Required non-color cue |
|---|---|---:|---|
| Power system $P$ | Navy | `#0B1F3A` | label `P`, power geometry |
| Transportation system $T$ | Teal | `#0F766E` | label `T`, mobility/route geometry |
| Information layer $I$ | Blue | `#2563EB` | label `I`, dashed information links |
| Organizational layer $O$ | Amber | `#D97706` | label `O`, dotted decision links |
| Viable / acceptable region | Green | `#15803D` | boundary label and set notation |
| Hazard / violated constraint | Red | `#B91C1C` | warning/boundary line style |
| Proposed thesis construct `[P]` | Purple | `#7E22CE` | explicit `[P]` label |
| Historical / superseded material | Gray | `#6B7280` | `HISTORICAL` text label |

**Accessibility rule:** color is never the only encoding. Every semantic color requires a text label, shape, line style or symbol that preserves meaning in grayscale.

---

## 9. Line-style semantics

| Line style | Meaning |
|---|---|
| Solid | physical/operational coupling or executed physical effect |
| Dashed | information/sensing/communication flow |
| Dotted | organizational/decision/coordination relation |
| Double/emphasized | feedback/closed-loop relation where useful |
| Red boundary | hazard/constraint boundary only |

Do not use decorative arrows without a defined scientific meaning.

---

## 10. Mermaid usage

Mermaid is appropriate for repository navigation and simple architecture maps, not for replacing formal mathematics.

The frozen status map is

```mermaid
flowchart LR
    S1["1 · Structure"] --> S2["2 · Causal Mechanisms"]
    S2 --> S3["3 · Dynamics"]
    S3 --> S4["4 · Feedback & Control"]
    S4 --> S5["5 · Viability"]
    S5 --> S6["6 · Transformation Interface"]
    S6 --> S7["7 · Transformation Pathways"]

    classDef canonical fill:#DDF4FF,stroke:#0969DA,color:#0B1F33,stroke-width:2px;
    classDef frozen fill:#DAFBE1,stroke:#1A7F37,color:#0B1F33,stroke-width:2px;

    class S1 canonical;
    class S2,S3,S4,S5,S6,S7 frozen;
```

Compact labels may be used in navigation diagrams, but full stage names remain authoritative.

---

## 11. Figure construction contract

Every final scientific figure should identify or link to:

| Field | Requirement |
|---|---|
| Figure ID | stable identifier |
| Mathematical object | exact variable/set/operator shown |
| Evidence state | `[E]`, `[D]`, `[P]` where applicable |
| Source equation/file | canonical equation or file path |
| Parameter domain | bounds/ranges where applicable |
| Units | required for dimensional variables |
| Data status | empirical, synthetic, scenario, simulated or conceptual |
| Algorithm | required for computed results |
| Verification | numerical, analytical, cross-model or empirical check |
| Color/line semantics | defined and non-decorative |
| Limitation | main interpretation boundary |
| Provenance | source data/code/commit where relevant |

---

## 12. Geometry-specific guardrail

Differential geometry may be used only when the underlying mathematical object is actually defined:

```math
\text{geometric visual metaphor}
\neq
\text{formal Riemannian geometry}.
```

For Stage 5, $\rho_E$ is the baseline. The state-dependent metric $g_\psi$ and margin $\rho_g$ remain `[P]` until metric properties, regularity, physical interpretation and comparative value are demonstrated.

The Hamilton–Jacobi value is not automatically a geometric distance:

```math
|V_{\mathrm{HJ}}(Y)|
\neq
d(Y,\partial\mathcal V)
\quad\text{in general}.
```

---

## 13. Uncertainty-language guardrail

Keep probability, distributional ambiguity and deep uncertainty distinct. In particular,

```math
\omega\in\Omega
```

is a scenario/future representation and must not be described as a probability model unless probabilities/weights are independently justified.

Likewise, a scenario satisficing fraction is not automatically a probability of success.

---

## 14. Theme and export rules

A light/dark theme may change presentation tokens only. It must preserve topology, text, equations, numerical values, evidence status and conclusions.

Publication export should use vector output whenever possible: PDF/SVG for diagrams and plots; LaTeX/TikZ/PGFPlots for exact mathematical exposition; Python/Julia for numerical figures. Raster output is appropriate only where the underlying content is inherently raster or no vector alternative exists.

---

## 15. Tool hierarchy

| Purpose | Preferred tool |
|---|---|
| Exact thesis equations | LaTeX / Overleaf |
| Deterministic framework diagrams | TikZ, Figma, SVG, draw.io |
| Numerical plots | Python/Matplotlib or Julia/Makie |
| Repository architecture maps | Mermaid |
| High-dimensional computed geometry | PyVista/VTK/Makie where justified |
| Static repository QA | Python + YAML/JSON Schema + GitHub Actions |
| Generative image tools | concept exploration only unless audited against canonical content |

No renderer or programming language changes the scientific status of the object being represented.
