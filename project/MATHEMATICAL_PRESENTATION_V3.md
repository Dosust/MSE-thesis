# MSE Thesis Mathematical Presentation and Rendering Standard

> **Filename note:** `MATHEMATICAL_PRESENTATION_V3.md` is retained for provenance, but this content is the current rendering standard.

**Status:** CURRENT / SYNCHRONIZED  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Scientific system:** P–T–I–O  
**Purpose:** Ensure that mathematical meaning survives GitHub, thesis, slide, SVG, and publication rendering without notation drift.

---

## 1. Governing principle

> **CHANGE THE VISUAL HIERARCHY, NOT THE SCIENTIFIC CONTENT.**

A renderer may change typography, spacing, orientation, or graphical encoding. It may not change equations, stage boundaries, variable meaning, evidence status, or scientific conclusions.

---

## 2. Canonical display hierarchy

The presentation hierarchy follows the frozen framework:

| Stage | Visual responsibility |
|---|---|
| **1 — Multilayer Structure** | Show $P,T$ as physical systems and $I,O$ as informational/organizational layers. |
| **2 — Causal Mechanisms** | Show directional causal interfaces and the interdependency object $\mathfrak I_{ij}^{\alpha\beta}$. |
| **3 — Coupled Hybrid Multiscale Dynamics** | Show state evolution, modes, events, delays, topology, and timescales. |
| **4 — Observation, Organization, Feedback and Control** | Show measurement, inference, organizational feasibility, policy, and actuation. |
| **5 — Viability** | Show acceptability, maintainability, viability boundary, geometric and temporal margins. |
| **6 — Transformation Interface** | Show translation from validated resilience evidence to sustainability requirements. |
| **7 — Sustainable Transformation Pathways** | Show long-term transformation alternatives and consequences. |

No figure may collapse distinct stages into one unlabeled arrow chain.

---

## 3. Evidence-state notation

The canonical thesis evidence labels are:

| Label | Meaning |
|---|---|
| `[E]` | Established literature/theory or directly supported evidence |
| `[D]` | Derived synthesis from established components |
| `[P]` | Proposed thesis construct requiring validation |

Computed outputs, simulations, or fitted parameters must be described explicitly in the figure caption or provenance record; they must not be relabeled as empirical evidence unless they are actually data-derived.

---

## 4. Canonical state notation

The integrated state is

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)\\z_I(t)\\z_O(t)
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

The labels $I$ and $O$ denote layers/functions; the time-varying states are $z_I(t)$ and $z_O(t)$.

---

## 5. GitHub mathematical rendering rules

For `.md` files in the repository:

1. inline math uses `$...$`;
2. display math uses `$$...$$`;
3. multiline mathematics uses `aligned`, `bmatrix`, `cases`, or multiple short display equations;
4. avoid long prose inside `\boxed{...}` because it produces oversized or clipped expressions;
5. avoid `\tag{...}` in Markdown; place **Equation Sx.y — description** immediately above the display;
6. prefer `\mathrm{...}` for roman mathematical labels and `\text{...}` only for short explanatory text;
7. long taxonomies belong in Markdown tables, not arrays inside math;
8. do not place raw Markdown links or long URLs inside equations;
9. distinguish the intervention $u(t)$ from measurement noise $\varepsilon_k(t)$;
10. if a formula cannot fit comfortably on a normal GitHub page width, split it before publication.

---

## 6. Core equations to preserve exactly

### Stage 2 — Causal interdependency

$$
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right).
$$

### Stage 3 — State architecture

$$
Y(t)=
\begin{bmatrix}
x_P\\x_T\\z_I\\z_O
\end{bmatrix},
\qquad
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
$$

### Stage 4 — Feedback spine

$$
X(t)
\rightarrow y(t)
\rightarrow I(t)
\rightarrow\widehat X(t)
\rightarrow O(t)
\rightarrow u(t)
\rightarrow X(t).
$$

### Stage 5 — Viability hierarchy

$$
K_{\mathrm{sus}}
\supseteq
\mathcal V_{\mathrm{sus}}^{u,T}
\rightarrow
\partial\mathcal V
\rightarrow
\{\rho,T_{\mathcal V},T_K\}.
$$

---

## 7. Semantic color system

Color is permitted only when it clarifies scientific roles. Use these defaults for vector figures, Mermaid diagrams, and presentation graphics:

| Scientific role | Preferred color | Hex | Required non-color cue |
|---|---|---:|---|
| Power system $P$ | Navy | `#0B1F3A` | label `P`, power icon/geometry |
| Transportation system $T$ | Teal | `#0F766E` | label `T`, mobility/route geometry |
| Information layer $I$ | Blue | `#2563EB` | label `I`, dashed information links |
| Organizational layer $O$ | Amber | `#D97706` | label `O`, dotted/decision links |
| Viable / acceptable region | Green | `#15803D` | boundary label and set notation |
| Hazard / violated constraint | Red | `#B91C1C` | warning symbol / line style |
| Proposed thesis construct `[P]` | Purple | `#7E22CE` | explicit `[P]` label |
| Historical / superseded material | Gray | `#6B7280` | `HISTORICAL` text label |

**Accessibility rule:** color must never be the only encoding. Every semantic color requires a text label, shape, line style, or symbol that preserves the meaning in grayscale.

---

## 8. Line-style semantics

For framework diagrams:

| Line style | Meaning |
|---|---|
| Solid | Physical/operational coupling or executed physical effect |
| Dashed | Information/sensing/communication flow |
| Dotted | Organizational/decision/coordination relation |
| Double or emphasized | Feedback/closed-loop relation when needed |
| Red boundary | Constraint violation or hazard boundary only |

Do not use decorative arrows without a defined causal or informational meaning.

---

## 9. Mermaid usage

Mermaid is appropriate for architecture and navigation, not for replacing formal equations. A valid stage-status map should pair color with text labels, for example:

```mermaid
flowchart LR
    S1["1 · Structure"] --> S2["2 · Causal Mechanisms"] --> S3["3 · Dynamics"] --> S4["4 · Feedback & Control"] --> S5["5 · Viability"] --> S6["6 · Transformation Interface"] --> S7["7 · Transformation"]

    classDef canonical fill:#DDF4FF,stroke:#0969DA,color:#0B1F33;
    classDef frozen fill:#DAFBE1,stroke:#1A7F37,color:#0B1F33;
    classDef next fill:#FFF8C5,stroke:#9A6700,color:#0B1F33;
    classDef downstream fill:#F6F8FA,stroke:#57606A,color:#24292F;

    class S1 canonical;
    class S2,S3,S4,S5 frozen;
    class S6 next;
    class S7 downstream;
```

The full canonical stage names remain authoritative even when compact labels are used in a small navigation graphic.

---

## 10. Figure construction contract

Every final scientific figure should identify or link to the following metadata:

| Field | Requirement |
|---|---|
| Figure ID | Stable identifier |
| Mathematical object | Exact variable/set/operator shown |
| Evidence state | `[E]`, `[D]`, or `[P]` where applicable |
| Source equation/file | Canonical equation or file path |
| Parameter domain | Bounds/ranges where applicable |
| Units | Required for dimensional variables |
| Data status | empirical, synthetic, scenario, or conceptual |
| Algorithm | Required for computed results |
| Verification | numerical, analytical, cross-model, or empirical check |
| Color/line semantics | Defined and non-decorative |
| Limitation | Main interpretation boundary |
| Provenance | Source data/code/commit where relevant |

---

## 11. Geometry-specific guardrail

The thesis may use differential geometry only when the underlying mathematical object is actually defined. In particular,

$$
\text{geometric visual metaphor}
\neq
\text{formal Riemannian geometry}.
$$

For Stage 5, the normalized Euclidean/weighted distance $\rho_E$ is the baseline. The state-dependent metric $g_\psi$ and margin $\rho_g$ remain proposed `[P]` constructs until regularity, metric properties, physical interpretation, and comparative value are demonstrated.

The Hamilton–Jacobi value function is also not automatically a geometric distance:

$$
|V_{\mathrm{HJ}}(Y)|
\neq
d(Y,\partial\mathcal V)
\quad\text{in general}.
$$

---

## 12. Theme and export rules

A light/dark theme may change presentation tokens only. It must preserve topology, text, equations, numerical values, evidence status, and conclusions.

Publication export should use vector output whenever possible: PDF/SVG for diagrams and plots; LaTeX/TikZ/PGFPlots for exact mathematical exposition; Python/Julia for numerical figures. Raster images are acceptable only when the underlying content is inherently raster or no vector representation exists.

---

## 13. Tool hierarchy

| Purpose | Preferred tool |
|---|---|
| Exact thesis equations | LaTeX / Overleaf |
| Deterministic framework diagrams | TikZ, Figma, SVG, draw.io |
| Numerical plots | Python/Matplotlib or Julia/Makie |
| Repository architecture maps | Mermaid |
| High-dimensional computed geometry | PyVista/VTK/Makie where justified |
| Generative image tools | Concept inspiration only unless fully audited against canonical content |

No renderer changes the scientific status of the underlying object.
