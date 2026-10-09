---
name: mathematical-visualization-design
description: Design mathematically driven scientific diagrams, interactive visualizations, animations, and framework figures in which geometry, color, motion, topology, and interaction are explicit encodings of model variables, relations, invariants, thresholds, and transformations. Use jointly with engineering-framework-design and scientific-diagram-design whenever a figure should be generated from mathematics rather than decorated around it.
license: MIT
---

## Deck3 global-update scope (binding)

When the user requests **"update Deck3"** or equivalent, apply the **entire linked design/production ecosystem**, not this skill in isolation. Read `../deck3/references/DECK3_GLOBAL_UPDATE_CONTRACT.md` and the canonical `deck3/references/DECK3_SRGB_PALETTE.json` (relative to .github/skills). Synchronize source-faithful text and writing, independently generated scientific figures/images, photorealistic asset prompts, code/templates, PPTX assembly, slide geometry, white-only surfaces, exactly 13 authored sRGB tokens, scientific evidence/citation/arrow QA, regression tests, release checks and any impacted root instructions. Archive and natural photographic pixels are preserved. Never claim completed certification from PPTX-open success or from an unexecuted/failing GitHub workflow. If not fully validated, label the result provisional.


# Mathematical Visualization Design

## Purpose

This skill enforces one principle:

\[
\boxed{
\text{model} \rightarrow \text{visual encoding} \rightarrow \text{rendering}
}
\]

Never reverse the order.

A valid mathematical visualization is not an illustration containing equations. It is a graphical representation whose geometry, topology, color, motion, size, opacity, or interaction is generated from an explicit mathematical object.

Use this skill for:
- thesis conceptual frameworks with formal semantics;
- state-time resilience diagrams;
- dynamic-network visualizations;
- interactive scientific computing;
- mathematical animations;
- parameter sweeps;
- phase/state-space views;
- threshold/viability visualizations;
- propagation diagrams;
- service-trajectory views;
- graph/network figures;
- scientific SVG/WebGL/Canvas renderings.

Use together with:
- \`engineering-framework-design\`;
- \`scientific-diagram-design\`.

---

## CURRENT CANONICAL STATE-TIME OVERRIDE + EXECUTABLE EXAMPLES — 2026-10-08

**Current thesis scope** is *only qualified extreme-heat thermal interdependencies* between separate Power P and the **full** Electrified Transportation T_e systems; the reduced model uses only minimum-sufficient evidence-admitted states. For current figures, **do not automatically treat an interface quantity \(Z_{PT}(t)\) as a dynamic state**. It remains a coupling/transfer quantity unless an independently justified dynamic evolution equation admits it as an actual state. Likewise, external extreme heat is a forcing, not an internal state.

Use \`project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md\` and \`project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md\` as current authorities; any older broad conceptual chain/automatic intervention emphasis in this file is illustrative **only**, not a frozen active mathematical model or required thesis result.

**Task examples** (all exact code/authority controls in the companion):
- "Plot a threshold-event time": first define admitted \(g(X(t),t)\), state units, threshold provenance, time horizon and interpolation; run \`../scientific-infographic-design/examples/mathematical_metrics.py\` for **synthetic software verification only**; real visualization must use cited real or validated model arrays.
- "Compute a propagation delay": \(\delta=\tau_{\rm receiver}-\tau_{\rm source}\) only if the two events, common time basis, and **causal directional mechanism** are separately defined; code arithmetic does not qualify mechanism.
- "Compute service deficit": use the documented positive-part integral and declared service/time units; it is not automatically a resilience index.
- "Generate a mathematical/engineering SVG": \`../scientific-infographic-design/examples/figures.py\` demonstrates deterministic vector bounds, arrows, status and source labels; these specific figures are conceptual, **not numerical state solutions**.
- "Create editable PowerPoint from model-defined relations": \`../scientific-infographic-design/examples/pptx_builder.py\` makes three example slides with editable native shapes and adjacent citations.
- "Check the code": run \`python -m unittest discover -s ../scientific-infographic-design/tests -v\` from this skill's directory; the suite checks mathematical edge cases and figure semantic invariants.

**Rendering contract:** derived numerical values → mathematical checks → independent physical validation status → typed visual encodings → caption with in-text scientific citations → rendering QA. Never invent numeric plots or promote interface quantities into dynamic state variables to beautify a diagram. These are worked coding **templates**, not final governing equations.

---
# 1. Model-First Rule

Before drawing anything, define the mathematical object being visualized.

Examples:

\[
\mathcal G=(V,E)
\]

\[
\dot X=F(X,H,u;\theta)
\]

\[
T:M_1\rightarrow M_2
\]

\[
R\subseteq A\times B
\]

\[
Q=G(X)
\]

\[
\tau_i=\inf\{t:g_i(X_i(t))=0\}
\]

The visual is only a representation of this structure.

Reject:

\[
\text{nice-looking diagram} \rightarrow \text{invented mathematical meaning}
\]

Require:

\[
\text{defined mathematical meaning} \rightarrow \text{visual form}
\]

---

# 2. Visual Encoding Contract

Every visual channel must encode a declared mathematical or scientific quantity.

For each graphical property, define a mapping:

\[
\phi_k : \text{model quantity} \rightarrow \text{visual channel}
\]

Possible channels:
- position;
- length;
- angle;
- line width;
- line style;
- node size;
- border style;
- color;
- opacity;
- shape;
- motion;
- animation speed;
- temporal delay;
- path curvature.

Example:

\[
\phi_M(M_i)=\text{node border width}
\]

\[
\phi_\tau(\tau_i)=\text{event location on timeline}
\]

\[
\phi_\delta(\delta_{ij})=\text{animation delay on edge }(i,j)
\]

\[
\phi_Q(Q_k)=\text{service trajectory height}
\]

A channel with no mapping is decorative and should be removed.

---

# 3. Geometry Must Mean Something

Position is semantic.

Possible meanings:
- graph coordinates;
- physical coordinates;
- state-space coordinates;
- time;
- hierarchy;
- containment;
- source-target transformation;
- subsystem partition;
- feasible/unsafe region.

Do not move objects merely to make the image feel dynamic.

If a node position changes in an animation, define what mathematical quantity drives the movement.

---

# 4. Topology Before Style

If the system is represented as a graph:

\[
\mathcal G=(V,E)
\]

define:
- node set \(V\);
- edge set \(E\);
- edge direction;
- edge type;
- edge state;
- edge weight if applicable.

Visual network rules:
- node exists because a modeled entity exists;
- edge exists because a modeled relation exists;
- arrow direction follows the mathematical relation;
- edge thickness must map to a defined magnitude if varied;
- color must map to a defined class/value if varied.

Never add edges for symmetry.

---

# 5. State-Time Visualization Rule

When state and time are central, the visual spine is:

\[
X_i(t)
\]

not separate decorative boxes called “state” and “time”.

For the thesis:

\[
H(x,t)
\rightarrow
X_i(t)
\rightarrow
\tau_i^C
\rightarrow
\delta_{ij}
\rightarrow
Q_k(t)
\]

but do not force a serial visual chain if the mathematics is not serial.

If transition time, propagation delay, and service are parallel functionals of a state trajectory, visualize them as parallel derived quantities:

\[
X(t)
\rightarrow
\begin{cases}
\tau_i^C\\
\delta_{ij}\\
Q_P(t),Q_T(t)
\end{cases}
\]

---

# 6. Continuous + Discrete Hybrid State

Use a hybrid representation when physical dynamics are continuous but operational modes are discrete.

Continuous state:

\[
X_i(t)
\]

Discrete mode:

\[
q_i(t)\in\{N,D,C,F,R\}
\]

Transitions require explicit guards:

\[
q_i:N\rightarrow D
\quad\text{when}\quad
g_i(X_i,t)=0
\]

Visual implication:
- continuous variables control continuous visual changes;
- state transitions cause discrete visual changes;
- the guard condition must be traceable.

Do not animate a “failure” transition without a defined event condition.

---

# 7. Invariants and Constraints Must Be Visible

If a model is constrained by:

\[
g(X,t)\le 0
\]

the visualization should distinguish:
- feasible region;
- boundary;
- violation region;
- trajectory.

For viability:

\[
X(t)\in\mathcal V(t)
\]

represent the viability set geometrically when possible.

For service:

\[
Q(t)\ge Q^{\min}
\]

make the acceptable-service threshold explicit.

This creates visuals that explain the mathematics instead of merely displaying it.

---

# 8. Transformation-Driven Diagrams

When the figure shows a model transformation, define the transformation first:

\[
T:M_1\rightarrow M_2
\]

Then visually show:
- source object;
- transformation;
- target object;
- what is preserved;
- what changes.

Examples:
- raw physical variable \(\rightarrow\) normalized physical margin;
- state \(\rightarrow\) capability;
- capability \(\rightarrow\) service;
- component event \(\rightarrow\) system consequence;
- observation \(\rightarrow\) state estimate;
- design variable \(\rightarrow\) modified dynamics.

Never draw an unexplained arrow between two views.

---

# 9. Mathematical Color Rule

**Binding across all figures:** the exclusive 13-token authored palette is `.github/skills/deck3/references/DECK3_SRGB_PALETTE.json`. Exact ASU Maroon and ASU Gold are the only exceptions to older maroon/gold-family bans. No other invented design hues. White-only authored backgrounds and panel interiors; real photographs retain real-world colors. Gold and Bright Turquoise may only be nonessential accents on white. Examples below are role illustrations, not permission to add other hex codes.


Color is a mathematical encoding, not decoration.

Use color only when it represents a declared class or quantity.

Default thesis semantic palette:
- external hazard/forcing: deep red `#B4232C`;
- physical/empirical system: forest green `#176B42`;
- mathematical dynamics/analysis: blue \`#0072B2\`;
- engineering intervention/decision: ASU maroon `#8C1D40`;
- neutral scientific content: black \`#000000\`;
- all backgrounds/interiors: pure white \`#FFFFFF\`.

Rules:
- no colored panel fills;
- use color on borders, arrows, headings, icons, small accents;
- never rely on color alone;
- pair color with labels, line style, or shape;
- if color has no semantic class, remove it;
- preserve grayscale interpretability.

---

# 10. Motion and Animation Grammar

Animation must be generated by equations or event logic.

Allowed motion drivers:
- \(X_i(t)\);
- \(M_i(t)\);
- \(\tau_i\);
- \(\delta_{ij}\);
- \(Q_k(t)\);
- parameter sweep \(\lambda\);
- control input \(u(t)\).

Examples:

\[
X_i(t)\mapsto \text{node geometry}
\]

\[
M_i(t)\mapsto \text{border emphasis}
\]

\[
\delta_{ij}\mapsto \text{edge animation delay}
\]

\[
Q_k(t)\mapsto \text{service trajectory}
\]

Animation speed must represent time or another defined parameter when possible.

Do not use looping motion merely to look advanced.

---

# 11. Interaction Rule

Interactive controls must correspond to model parameters.

Examples:
- ambient temperature slider \(\rightarrow T_{\mathrm{amb}}\);
- heat duration slider \(\rightarrow \Delta t\);
- load slider \(\rightarrow L_i\);
- design parameter control \(\rightarrow \theta\);
- adaptation control \(\rightarrow u_A(t)\).

Every interaction must update:
1. the mathematical model;
2. the derived variables;
3. the visual encoding.

This is the core interactive loop:

\[
\text{parameter}
\rightarrow
\text{model recomputation}
\rightarrow
\text{derived state}
\rightarrow
\text{visual update}
\]

---

# 12. Thesis-Specific Mathematical Visualization Spine

For the extreme-heat coupled Power–Transportation thesis, use:

\[
H(x,t)
\rightarrow
X(t)
\rightarrow
\{\tau_i^C,\delta_{ij},Q_P(t),Q_T(t)\}
\rightarrow
\{\text{Improve, Adapt, Restore}\}
\]

where:

\[
X_{\mathrm{th}}(t)=
[X_{P,\mathrm{th}}^\top,X_{T_e,\mathrm{th}}^\top]^\top
\]

The interface variable \(Z_{PT}(t)\) is a coupling quantity by default, **not an active dynamic state** unless a separate, physically evidenced evolution law admits it. Do not insert \(Z_{PT}\) into \(X_{\mathrm{th}}\) merely because it crosses a system boundary. Exact active states and interface laws remain OPEN.

Use the physical architecture:

\[
\mathcal P
\leftrightarrow
\mathcal I_{PT}
\leftrightarrow
\mathcal T
\]

only when each direction has an explicit exchanged quantity.

Recommended mathematical views:

### A. State trajectory view
Show \(X_i(t)\) against time.

### B. Threshold view
Show \(g_i(X_i,t)=0\) and \(\tau_i^C\).

### C. Propagation view
Show event pair and delay:

\[
\delta_{ij}
=
\tau_j^{\mathrm{response}}
-
\tau_i^{\mathrm{transition}}
\]

### D. Service view
Show:

\[
Q_P(t),Q_T(t),Q^{\min}
\]

### E. Intervention view
Show how:
- Improve modifies \(\theta\);
- Adapt modifies \(u_A(t)\);
- Restore modifies \(u_R(t)\).

---

# 13. Script Architecture

For code-based scientific visualization, separate:

\`\`\`text
MODEL
→ DERIVED QUANTITIES
→ VISUAL ENCODING
→ RENDERER
→ INTERACTION
→ VALIDATION
\`\`\`

Recommended modules:

\`\`\`text
model/
  dynamics.py|ts
  thresholds.py|ts
  service.py|ts
  interventions.py|ts

viz/
  encodings.py|ts
  layout.py|ts
  arrows.py|ts
  labels.py|ts

render/
  svg.py|ts
  canvas.py|ts
  webgl.py|ts

interaction/
  controls.py|ts
  timeline.py|ts

validation/
  semantic_checks.py|ts
  math_checks.py|ts
  visual_checks.py|ts
\`\`\`

Do not mix model equations and arbitrary drawing commands in one script.

---

# 14. Renderer Selection

Prefer:

### SVG
For:
- exact thesis figures;
- arrows;
- equations;
- graph/network diagrams;
- publication-quality export.

### Canvas / p5.js
For:
- state-time animation;
- parameter-driven interaction;
- moderate graph animation.

### D3.js
For:
- graph/network layouts;
- data-linked geometry;
- service trajectories;
- interaction.

### Three.js / WebGL / GLSL
For:
- high-dimensional fields;
- surfaces;
- large dynamic systems;
- shader-based state fields.

### MathJax / KaTeX
For:
- exact mathematics in web visualizations.

Use the least complex renderer that faithfully represents the mathematics.

---

# 15. Deterministic Layout Rule

Static thesis figures should be deterministically generated when possible.

Preferred pipeline:

\[
\text{formal specification}
\rightarrow
\text{SVG/TikZ/draw.io}
\rightarrow
\text{QA}
\rightarrow
\text{PNG/PDF export}
\]

Generative image tools may be used for exploratory composition, but not as the scientific authority.

If a generated figure changes:
- equation;
- arrow direction;
- label;
- topology;
- boundary;
- color semantics;

it fails QA.

---

# 16. Mathematical Backstory Requirement

Every diagram must have a backstory that can be stated in one paragraph:

1. What mathematical object exists?
2. What variables evolve?
3. What transformations are computed?
4. What each visual channel encodes?
5. What event/threshold changes the visual state?
6. What engineering decision the figure supports?

If this paragraph cannot be written, the figure is not mathematically grounded enough.

---

# 17. Visual Compression Rule

A mathematically grounded figure can still be visually simple.

Do not display all equations.

Use:
- exact variables;
- minimal equations;
- compact labels;
- mathematically meaningful arrows;
- one dominant mechanism.

Move full derivations to the caption, appendix, or interactive view.

Simplification is allowed only if the mathematical semantics remain traceable.

---

# 18. Reference-Learning Rule

Learn from mathematical visualization resources by extracting:
- model-to-visual mapping;
- parameter interaction logic;
- transformation grammar;
- state-space logic;
- domain-coloring principles;
- topology preservation;
- deterministic rendering patterns.

Do not copy:
- distinctive layouts;
- protected illustrations;
- source-specific artistic composition.

The reusable principle is:

\[
\boxed{
\text{mathematical structure drives the visual}
}
\]

not:

\[
\text{imitate the source image}
\]

---

# 19. QA Gates

## Mathematical QA
- [ ] every visual object maps to a model object;
- [ ] every varied visual property has a defined mapping;
- [ ] equations are correct;
- [ ] thresholds/events are defined;
- [ ] time semantics are explicit;
- [ ] no invented causality;
- [ ] no fake instability/cascade claims.

## Visual QA
- [ ] pure white background;
- [ ] color is semantic;
- [ ] geometry reflects meaning;
- [ ] arrows reflect actual relations;
- [ ] no decorative motion;
- [ ] readable at intended size;
- [ ] no generic AI aesthetic.

## Interaction QA
- [ ] controls map to model parameters;
- [ ] parameter updates recompute model outputs;
- [ ] animation follows model time;
- [ ] visual changes are deterministic.

## Thesis QA
- [ ] selected components only;
- [ ] interface is distinguished from subsystem;
- [ ] common heat exposure is not mislabeled as interdependency;
- [ ] state, threshold time, propagation delay, service, and recovery are distinct;
- [ ] Improve/Adapt/Restore act on different mathematical targets.

---


# 20. Two-Figure Separation Rule

For this thesis, do not collapse the conceptual framework and mathematical framework into one overloaded figure.

## A. Conceptual framework

Purpose:

\[
\boxed{
\text{scientific meaning and global thesis logic}
}
\]

Rules:
- no equations;
- no Greek variables;
- no state-vector notation;
- no solver, estimation, calibration, VVUQ, or computational workflow;
- show only the global scientific phases and their scientifically defined relations;
- show sustainability as Social, Environmental, and Economic consequences;
- show SDG relevance/alignment only as a later interpretation layer;
- do not imply that resilience automatically produces sustainability.

Canonical conceptual chain:

\[
\text{Extreme Heat}
\rightarrow
\text{Coupled Physical System}
\rightarrow
\text{State-Time Response}
\rightarrow
\text{Interdependency Propagation}
\rightarrow
\text{Service Consequences}
\rightarrow
\text{Improve / Adapt / Restore}
\rightarrow
\begin{cases}
\text{Resilience Outcome}\\
\text{Sustainability Impacts}
\end{cases}
\rightarrow
\text{Sustainable + Resilient Outcome}
\rightarrow
\text{SDG Relevance / Alignment}.
\]

The visible conceptual figure must express this chain in words, not formulas.

## B. Mathematical framework

Purpose:

\[
\boxed{
\text{formalize the conceptual framework into testable mathematical objects}
}
\]

Rules:
- equations are allowed and expected;
- show only the minimum equations needed to define state, evolution, transition time, propagation, service, intervention, resilience, sustainability, and SDG-indicator mapping;
- do not add component inventory text when the mathematical object already identifies the subsystem;
- preserve the same topology as the conceptual framework;
- mathematical arrows must be transformations, dependencies, or control actions with explicit semantics.

The conceptual and mathematical frameworks must be isomorphic at the level of scientific meaning, but not identical in visual content.

---

# 21. Reference-Derived Mathematical Visualization Principle

The public work of Juan Carlos Ponce Campuzano on *Complex Analysis: A Visual and Interactive Introduction* demonstrates a reusable design principle: mathematical structure should generate the visual behavior, and interaction should expose mathematical properties rather than decorate them.

For this project, transfer only the principle:

\[
\boxed{
\text{mathematical object}
\rightarrow
\text{computed state}
\rightarrow
\text{visual encoding}
\rightarrow
\text{interaction}
}
\]

Do not copy source-specific layouts, artwork, applets, code, or domain-coloring aesthetics into thesis figures.

For interactive thesis visualizations:
- a slider changes a model parameter;
- the model is recomputed;
- derived quantities are recomputed;
- the visualization updates from those quantities;
- animation time must correspond to model time;
- visual changes must remain deterministic and auditable.

Source notes and permitted transfer are documented in:
\`resources/JCPONCE_COMPLEX_ANALYSIS_REFERENCE.md\`.

---

# 22. Changelog

## 1.2.0 — 2026-10-08

Added current canonical thermal-only state-time override, corrected automatic interface-as-state implication, and linked runnable event-time/SVG/PPTX examples.

## 1.1.0

Added:
- explicit separation of conceptual and mathematical frameworks;
- no-mathematics rule for the conceptual framework;
- formal-isomorphism rule between conceptual and mathematical frameworks;
- source-derived mathematical-visualization principle from the public J.C. Ponce complex-analysis project;
- explicit prohibition on copying source-specific visual style or applet implementation.

## 1.0.0

Initial release.

---

## Optional VisQuill companion — 2026-10-08

When interactive **2D geometry, dragging or reactive constraints** are scientifically necessary and the user requests a browser tool, consider `../visquill-interactive-visualization/SKILL.md` *after* passing its `references/TOOL_FIT_DECISION.md` gate. This vendor-licensed TypeScript/SVG tool handles **display and interaction only**; use independent scientific modeling, parameter/evidence provenance, and VVUQ. Standard plots, static thesis SVG figures and editable PowerPoint diagrams should continue using simpler established tools by default.

The canonical minimum-sufficient active state vector remains OPEN. Do not interpret generic visuals in this skill as admission of an interface state, full feedback loop, numerical threshold, or documented mechanism without the current authoritative scope/evidence tests. Treat symbolic examples as candidates unless established. The required vendor attribution remains visible for permitted noncommercial use.
