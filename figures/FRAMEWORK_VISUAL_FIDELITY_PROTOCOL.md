# Framework Visual Fidelity Protocol

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Protocol](https://img.shields.io/badge/figure%20QA-MANDATORY-0969DA)

**Status:** Mandatory QA protocol for every figure representing the frozen seven-stage thesis framework  
**Authority:** [`../project/CANONICAL_7_STAGE_FRAMEWORK.md`](../project/CANONICAL_7_STAGE_FRAMEWORK.md)  
**Rendering standard:** [`../project/MATHEMATICAL_PRESENTATION_V3.md`](../project/MATHEMATICAL_PRESENTATION_V3.md)  
**Effective date:** 2026-09-11

---

## 1. Governing principle

> **CHANGE THE VISUAL HIERARCHY, NOT THE SCIENTIFIC CONTENT.**

Visual design may improve hierarchy, spacing, grouping, color, typography and information flow. It may not silently alter stage order, notation, evidence status, causal meaning or conclusions.

---

## 2. Frozen seven-stage identity

Every authoritative full-framework figure must preserve exactly these stages and order:

| Stage | Canonical name | Scientific responsibility |
|---:|---|---|
| **1** | Multilayer Structure | define what exists and where interactions can occur |
| **2** | Causal Mechanisms | define accepted directed causal interdependencies |
| **3** | Coupled Hybrid Multiscale Dynamics | evolve accepted mechanisms through state, mode, topology and time |
| **4** | Observation, Organization, Feedback and Control | infer the system state and map knowledge/capability into feasible operational control |
| **5** | Viability | evaluate acceptability, maintainability and proximity to loss |
| **6** | Resilience-to-Sustainability Transformation Interface | diagnose regime adequacy and specify why/what/how-deep change is required |
| **7** | Sustainable Transformation Pathways | determine which strategic changes, in what order, when and under what conditions |

A reduced figure may show only a subset of stages **only when its caption explicitly states that it is a partial-stage view**.

---

## 3. Canonical mathematical chain

When the full mathematical spine is shown, use the current frozen hierarchy:

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

Do not replace this chain with older symbols such as $(\mathcal G,Y,Z)\rightarrow\mathcal C\rightarrow\cdots$ unless the figure is explicitly labeled **historical/superseded**.

---

## 4. Non-negotiable notation checks

A canonical figure must preserve the following distinctions:

| Distinction | Required notation |
|---|---|
| Physical systems vs. layers | $P,T$ physical; $I,O$ informational/organizational |
| Integrated state | $Y=[x_P,x_T,z_I,z_O]^\top$ |
| Causal interdependency | $\mathfrak I_{ij}^{\alpha\beta}$ |
| Operating mode | $m(t)$ kept separate from $Y(t)$ |
| Stage-4 control | $u(t)$ |
| Measurement noise | $\varepsilon$ |
| Acceptability vs. viability | $K_{\rm sus}\neq\mathcal V_{\rm sus}^{u,T}$ |
| Stage-6 output | $(c_6,\mathcal D_6,\boldsymbol\zeta_T)$ |
| Stage-7 regime | $\mathfrak M_k$ |
| Stage-7 strategic action | $\mathbf a_k$, distinct from Stage-2 $a_{ij}$ |
| Stage-7 policy | $\boldsymbol\pi_{\rm ST}$ or $\pi_k^{\rm ST}$ |
| Stage-7 object | $\mathfrak P_{\rm ST}$ |

A figure fails fidelity review if it merges any of these objects without an explicit derivation or approved framework revision.

---

## 5. Evidence-state display

When a figure mixes established and proposed constructs, preserve the labels:

| Label | Meaning | Visual recommendation |
|---|---|---|
| `[E]` | established literature/theory | standard line/shape |
| `[D]` | derived synthesis | standard line/shape + label |
| `[P]` | proposed thesis construct requiring validation | explicit `[P]` label; optional purple accent |

A framework freeze does **not** convert `[P]` constructs into established theory.

---

## 6. Semantic colors

Color is optional. When used, use it to clarify scientific roles rather than decorate the page.

| Scientific role | Preferred color | Hex | Mandatory redundant cue |
|---|---|---:|---|
| Power $P$ | Navy | `#0B1F3A` | `P` label / power geometry |
| Transportation $T$ | Teal | `#0F766E` | `T` label / route geometry |
| Information $I$ | Blue | `#2563EB` | `I` label / dashed link |
| Organization $O$ | Amber | `#D97706` | `O` label / dotted link |
| Viable / acceptable region | Green | `#15803D` | boundary/set label |
| Hazard / violated constraint | Red | `#B91C1C` | warning/boundary style |
| Proposed `[P]` construct | Purple | `#7E22CE` | `[P]` text label |
| Historical/superseded | Gray | `#6B7280` | `HISTORICAL` text label |

**Accessibility:** color must never be the only carrier of meaning.

---

## 7. Line-style semantics

| Line style | Meaning |
|---|---|
| Solid | physical/operational effect or executed action |
| Dashed | sensing/information/communication flow |
| Dotted | organizational/decision/coordination relation |
| Emphasized/double | closed-loop feedback when needed |
| Red boundary | hazard/constraint boundary only |

Do not use unlabeled decorative arrows in a scientific figure.

---

## 8. Stage-7 figure guardrails

Stage 7 is now frozen, so the previous prohibition on Stage-7 mathematics is obsolete. A Stage-7 figure may show

$$
\mathfrak P_{\rm ST}
=
(\mathbb G_{\rm ST},\boldsymbol\pi_{\rm ST},\Omega,\mathcal A^{\rm feas},\mathbf J,\mathbb M_{\rm sus}),
$$

provided the notation matches the canonical Stage-7 file.

The figure must preserve

$$
\underbrace{u(t)}_{\text{operate current regime}}
\neq
\underbrace{\mathbf a_k}_{\text{transform regime}}.
$$

A graph metric such as degree, betweenness or algebraic connectivity must never be presented as equivalent to resilience unless the thesis has explicitly validated that relation for the stated case.

---

## 9. Geometry guardrails

Stage-5 geometry is allowed because it is part of the frozen scope, but evidential status must remain visible.

The baseline is

$$
\rho_E
=
d(\widetilde Y,\partial\widetilde{\mathcal V}),
$$

whereas the Riemannian margin

$$
\rho_g
=
d_{g_\psi}(Y,\partial\mathcal V)
$$

remains `[P]` until validated.

Likewise,

$$
|V_{\rm HJ}(Y)|
\neq
d(Y,\partial\mathcal V)
\quad\text{in general}.
$$

Do not use curved surfaces merely as a visual metaphor and then label them as formal Riemannian geometry.

---

## 10. Text and mathematical legibility

A final framework figure must satisfy all of the following:

- no paragraph-length prose inside equations;
- no unreadably small mathematical text;
- no equation wider than the intended publication frame;
- no unexplained acronym at first appearance;
- consistent italic/roman mathematical typography;
- variables, sets and operators match canonical files exactly;
- units shown for dimensional numerical quantities;
- captions distinguish conceptual, synthetic, simulated and empirical content;
- APA 7 citations appear in the caption or surrounding thesis text where required.

---

## 11. Deterministic production workflow

For figures requiring exact wording or equations, prefer:

1. TikZ/LaTeX or PGFPlots for mathematical precision;
2. Figma, SVG or draw.io for deterministic vector layout;
3. Python/Matplotlib or Julia/Makie for computed figures;
4. Mermaid for repository navigation and simple architecture maps.

Generative image models may support design exploration, but a generated figure is not canonical until it passes this protocol word-for-word and symbol-for-symbol.

---

## 12. Mandatory final-figure metadata

Every thesis-ready scientific figure should record:

| Field | Requirement |
|---|---|
| Figure ID | stable identifier |
| Canonical source | file path + commit/tag |
| Mathematical object | exact object(s) represented |
| Evidence state | `[E]`, `[D]`, `[P]` where applicable |
| Data status | conceptual, synthetic, simulated, calibrated or empirical |
| Units/domain | where applicable |
| Algorithm/model | for computed figures |
| Verification | analytical/numerical/cross-model/empirical check |
| Color/line semantics | declared when used |
| Limitation | main interpretation boundary |

---

## 13. Figure status labels

| Status | Meaning |
|---|---|
| `CANONICAL-VERIFIED` | passed all mandatory fidelity checks |
| `DRAFT-UNVERIFIED` | design draft awaiting audit |
| `ILLUSTRATIVE-NONCANONICAL` | contains additions or simplifications and is not framework authority |
| `SUPERSEDED` | replaced by a later verified figure |

Only `CANONICAL-VERIFIED` framework figures should serve as authoritative representations in the final thesis.

---

## 14. Audit record template

```text
Figure file:
Source format:
Audit date:
Auditor:
Canonical source commit:
Stage identity: PASS / FAIL
Stage order: PASS / FAIL
Notation: PASS / FAIL
Mathematical hierarchy: PASS / FAIL
Evidence labels: PASS / FAIL
Color/line semantics: PASS / FAIL / N/A
No silent additions: PASS / FAIL
Overall status: CANONICAL-VERIFIED / DRAFT-UNVERIFIED / ILLUSTRATIVE-NONCANONICAL
Notes:
```

The audit record is part of figure provenance and should be kept with the native vector or figure-generation code.
