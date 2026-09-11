# Stage 4 Display and Rendering Audit

**Date:** 2026-09-11  
**Scope:** `project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md` and all current thesis entry-point summaries that reproduce Stage-4 notation.  
**Purpose:** eliminate GitHub Markdown/LaTeX display defects without changing the frozen Stage-4 scientific scope.

---

## 1. Audit principle

The audit distinguishes **scientific content** from **rendering form**.

The following remain unchanged:

- the seven-stage framework;
- the Stage-4 research question;
- the P–T–I–O system ontology;
- the Stage-3/Stage-4/Stage-5 boundaries;
- the observation–inference–organization–control logic;
- the proposed response-to-cascade diagnostic status;
- the 31-study evidence basis;
- APA 7th edition as the citation standard.

Only display, notation clarity, and GitHub rendering structure were corrected.

---

## 2. Defects found and corrections applied

| Defect | Why it was a problem | Correction |
|---|---|---|
| Malformed evidence-table headers in the source draft | Column boundaries were merged and could render as broken tables. | Rebuilt all tables with explicit Markdown columns and consistent pipe counts. |
| Oversized single-line boxed equations | Long `\boxed{...}` expressions can overflow horizontally and become difficult to read on GitHub/mobile. | Replaced long boxes with multiline display equations, compact tables, or prose callouts. |
| Very long final Stage-4 scope equation | The original final scope was approximately one large mathematical block and was not suitable for repository display. | Converted the frozen scope to a two-column Markdown specification table. |
| Long stage-progression underbrace chains | Excessive width reduced readability and could clip on narrow displays. | Replaced with stage-role tables and shorter compact mathematical chains. |
| Fenced `math` blocks mixed with Markdown display equations | Mixed rendering styles created inconsistent visual behavior. | Canonical Stage 4 now uses GitHub-compatible `$$ ... $$` display blocks consistently. |
| Equation tags embedded inside large display blocks | `\tag{...}` support can vary and increases rendering fragility. | Equation identifiers are now plain bold Markdown captions (`Equation S4.x`) immediately above each display equation. |
| Potential confusion between control `u` and Greek measurement-noise `ν` | In some fonts, `u` and `ν` are visually similar and can be misread in dense equations. | Control remains exclusively `u`; measurement noise is displayed as `\varepsilon`. |
| Inconsistent `I/O` layer labels versus dynamic states | Using `I(t)`/`O(t)` inside operators can blur layer identity and state variables. | Conceptual spine retains `I`/`O`; mathematical operators use `z_I(t)`/`z_O(t)`. |
| Inconsistent action-set brackets | Mixed `\mathcal U[...]` and `\mathcal U(...)` reduced notation consistency. | Mathematical action-set expressions use `\mathcal U(z_I,z_O)` consistently. |
| Raw source links with tracking parameters in the draft | Long URLs inflated tables and damaged readability. | Removed tracking/source links from the canonical scientific text. |
| Legacy `doi:...` reference form | Not consistent with the fixed APA 7 thesis rule and visually inconsistent. | All references use canonical `https://doi.org/...` DOI URLs. |
| Numbered reference list in the source draft | APA 7 reference lists are alphabetized, not numbered. | Canonical Stage-4 references are unnumbered and alphabetized. |
| Repeated long Stage-3/4/5 boundary boxes | Redundant display math increased visual density. | Replaced with compact responsibility tables. |
| Long response-time expression | Single-line form was difficult to read. | Split into a two-line `aligned` equation while preserving the same decomposition. |
| Model-variant notation colliding visually with Stage-2 mechanism notation | Plain `M_0,...` could be confused with Stage-2 `M_{ij}`. | Model variants remain `\mathscr M_0,...,\mathscr M_3`. |

---

## 3. Canonical notation after the display audit

### Physical state and observation

$$
X(t)\rightarrow y(t),
$$

$$
y_k(t)=H_k[X(t-\delta_k)]+\varepsilon_k(t).
$$

### State estimation

$$
(\widehat X(t),\Sigma_X(t))
=
\mathcal E(y_{[0,t]},z_I(t)).
$$

### Organizationally feasible control

$$
\mathcal U_{\rm available}(t)
=
\mathcal U(z_I(t),z_O(t)),
$$

$$
u(t)=\pi[\widehat X(t),z_I(t),z_O(t)],
\qquad
u(t)\in\mathcal U(z_I(t),z_O(t)).
$$

Here the line break before `u(t)` is intentional Markdown source formatting; the rendered mathematical variable is the Latin control variable $u$, not Greek $\nu$.

### Closed loop

$$
X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u\rightarrow X.
$$

### Response time

$$
\begin{aligned}
\tau_{\rm response}={}&
\tau_{\rm sense}+\tau_{\rm comm}+\tau_{\rm est}+\tau_{\rm decision}\\
&+\tau_{\rm coord}+\tau_{\rm mobilization}+\tau_{\rm act}.
\end{aligned}
$$

### Proposed diagnostic

$$
\Pi_R=\frac{\tau_{\rm response}}{\tau_{\rm cascade}},
\qquad
\Pi_R<1\not\Rightarrow\text{successful control}.
$$

---

## 4. Files synchronized

The display audit was propagated to:

1. `project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`
2. `README.md`
3. `project/THESIS_SCOPE.md`
4. `PROJECT_MEMORY.md`

These files now use the same Stage-4 control notation, stage status, stage boundary, and GitHub-friendly rendering conventions.

---

## 5. Freeze rule after audit

The display audit does **not** reopen Stage 4 scientifically.

> **Stage 4 remains CANONICAL / FROZEN.**

Future modifications that change equations, scientific meaning, variables, scope, evidence interpretation, or stage boundaries require an explicit versioned scientific revision. Pure typographic/rendering fixes may be applied only if they preserve the canonical content.
