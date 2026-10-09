---
name: scientific-diagram-design
description: Design, generate, audit, and improve rigorous resource-grounded scientific and engineering diagrams, figures, framework images, architecture views, mechanism diagrams, mathematical diagrams, state-time diagrams, workflows, and system visualizations. Use whenever a user asks to design, draw, visualize, render, improve, or generate a scientific/engineering diagram or framework image. Prevent generic AI-style visuals by selecting a justified diagram grammar, defining semantics before rendering, grounding the design in authoritative resources, and validating every boundary, object, arrow, label, equation, and transformation.
license: MIT
---

# Scientific Diagram Design

## Binding visual-color restrictions for Dossiya thesis designs

- Scientific canvas and every authored panel/box/header/legend background **must be pure white (#FFFFFF)**; no colored fills, beige/off-white backgrounds, gradients, artificial glows, textures or shadows.
- **Never use purple, violet, pink or magenta** in designed marks (borders, text, headers, arrows, diagrams, chart series or icons).
- **Never use designed yellow or gold**; yellow may appear only when an authentic feature of a real/natural depicted object (such as sunlight). Do not use yellow/gold as an annotation color.
- Authentic colors of photographic/photorealistic objects remain, including vehicles and infrastructure, natural landscapes, vegetation, or sky. This exception is **not** permission for colored presentation blocks, fake color treatments or photo overlays.
- Only restrained black/charcoal, navy/blue, green or red may distinguish purposeful headings, text, scientific lines, arrows, chart series, outlines and small accents. Maintain readable shape/line-style encoding independent of color.
- QA must examine styled vector/design elements separately from photographs. Reject visual designs with prohibited authored colors even if diagram physics is correct. Do not erase valid natural pixels simply because their hue resembles a forbidden designed color.
- If an older palette guide conflicts, these stricter rules override it for the specified work.

## Mission

Create diagrams that behave as **model views**, not decorative pictures.

A strong scientific diagram must be:

- semantically defined;
- resource-grounded;
- mathematically or physically consistent when applicable;
- explicit about viewpoint and scope;
- traceable to source knowledge;
- visually economical;
- reproducible or auditable;
- original rather than copied from a reference;
- readable without relying on decorative effects.

The default standard is:

```text
meaning first
→ visual grammar second
→ rendering third
```

Never reverse this order.

---

## Companion infographic skill — current routing (2026-10-08)

For **presentation-ready scientific infographics**, load `../scientific-infographic-design/SKILL.md`, its curated `references/FIGURE_REFERENCE_LIBRARY.md`, and any relevant chapter storyboard. This companion adds message selection, slide readability, visual-reference transfer, scientific citation placement, and PPTX accessibility; this scientific-diagram skill remains authoritative for boundaries, elements, models, and arrow semantics.

**Do not repurpose an established arrow line style as evidence status.** In particular, **dashed = control/intervention**, and an unqualified thermal dependency must be labeled `CANDIDATE / OPEN` independently of the arrow style. Use validated evidence provenance on the particular physical effect; a published design figure is not a domain-science source. The internal frozen full P/T_e system scope must not be narrowed to EVSE in infographic compression.

Three fixture requirements for infographic figures:
- shared extreme heat must not generate an imaginary P↔T_e coupling arrow;
- a proposed T_e→P charger effect must pass the grid-side AC-input evidence gate;
- a bounded EVSE application remains a subset of the full T_e system.

Ref sources: Jambor & Bornhäuser (2024), https://doi.org/10.1371/journal.pcbi.1011789 (Figs 1,5,6); Rougier et al. (2014), https://doi.org/10.1371/journal.pcbi.1003833 (Figs 3,7). Source/diagram citation protocol remains mandatory under `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md`.

---

## Executable diagram construction examples — 2026-10-08

To turn this semantic skill into code:
- **Architecture diagram:** read \`../scientific-infographic-design/examples/WORKED_FIGURE_RECIPES.md\` Recipe A; register P, full T_e and actual electrical exchange; render via \`../scientific-infographic-design/examples/figures.py\` scene 03 or \`examples/pptx_builder.py\`.
- **Forcing diagram:** Recipe B; register heat OUTSIDE both systems and exactly two independent forcing→state→capability lanes; SVG scene 04. Semantic fixture rejects imaginary thermal coupling.
- **Mechanism diagram:** Recipe C; define P→T_e and T_e→P with distinct case evidence gates; SVG scene 05. The grid-side AC-input gate is compulsory for EVSE→Power thermal claims.
- **Research gap matrix:** Recipe D; each literature row must specify what was established, the study limits, and the bounded thesis test; cite the relevant row.
- **State-time math:** Recipe H + \`examples/mathematical_metrics.py\`; real state trajectories need model/data validation; synthetic test outputs must never resemble actual measurements.
- **High-rigor code / PPTX:** \`../scientific-infographic-design/examples/README.md\`; choose SVG, native PowerPoint or numerical plots according to the declared view, run tests, then inspect rendering.

**Source distinction:** published Figure 5/6 of Jambor & Bornhäuser (2024) teaches layout and arrows (https://doi.org/10.1371/journal.pcbi.1011789); it does not justify case-specific physical arrows. For all evidence-bearing figures, the repository's current in-text APA citation rule is mandatory.

---
# 1. Core Principle

A diagram is not a collection of boxes and arrows.

A diagram is a **view of a model for a declared concern**.

Before drawing, answer:

1. What question must this diagram answer?
2. Who is the audience?
3. What is the system or subject?
4. What is inside the view?
5. What is outside the view?
6. Which objects are real modeled entities?
7. Which relations are physically, mathematically, or logically justified?
8. What does each arrow mean?
9. Is time represented?
10. Is state represented?
11. Is the diagram structural, behavioral, functional, relational, mathematical, or mixed?
12. What authoritative resources establish the visual/modeling grammar?
13. What must not be introduced?

If these answers are not available from the conversation, source material, or project files, retrieve the needed evidence before rendering.

---

# 2. Resource-Grounded Rule

Do not invent the visual architecture from aesthetic intuition alone.

Use a **reference basis** before rendering.

Evidence priority:

1. user-provided source documents and approved figures;
2. formal standards and official modeling specifications;
3. authoritative systems-engineering handbooks;
4. peer-reviewed literature;
5. operator or manufacturer diagrams;
6. previously approved project figures;
7. only then, general visual-design judgment.

For each diagram, internally record:

```text
REFERENCE BASIS
- source:
- what is learned:
- what is reused conceptually:
- what is NOT copied:
```

References provide:

- diagram grammar;
- semantic conventions;
- hierarchy;
- model transformations;
- boundary logic;
- arrow meaning;
- notation;
- layout precedent.

References do **not** authorize copying protected figures.

---

# 3. Copyright-Safe Learning Rule

When learning from a published figure:

Allowed:
- identify its diagram type;
- identify its semantic grammar;
- identify how it separates scope, system, environment, structure, function, behavior, or sequence;
- identify general layout principles;
- identify transformation logic;
- create a new diagram for the user's system.

Do not:
- reproduce the exact figure;
- trace the original geometry;
- reuse protected illustrations;
- preserve distinctive copyrighted arrangement merely with new labels;
- imitate a proprietary figure so closely that the new figure is effectively a copy.

The goal is:

```text
learn the modeling principle
≠
copy the picture
```

---

# 4. Lessons from OMG Math DSIG Relational Model Transformations

The project evidence record is:

```text
evidence/E_OMG_MATH_DSIG_2022_RELATIONAL_MODEL_TRANSFORMATIONS.md
```

Apply these lessons when relevant.

## 4.1 Scope of concerns

Each diagram should declare or internally identify the concern it addresses.

Examples:
- actors;
- functionality;
- decomposition;
- actions;
- system elements;
- interactions;
- control structure;
- scenario integration.

Do not make one diagram simultaneously carry every concern.

## 4.2 Model transformations

Prefer traceable transformations between views:

```text
environment / actors
→ functionality
→ actionable behavior
→ functional allocation
→ system structure
→ interoperation
→ sequence / scenario behavior
```

This sequence is not mandatory for every project, but the principle is permanent:

```text
a new view should preserve traceability to the previous view
```

## 4.3 Mathematics before graphics

Where a diagram represents formal relationships, define the mathematical or logical structure before drawing it.

For a relation:

```math
R\subseteq A\times B
```

For a graph:

```math
\mathcal G=(V,E)
```

For a transformation:

```math
T:M_1\rightarrow M_2
```

For state dynamics:

```math
\dot X=F(X,u,t)
```

The image is the graphical interpretation of the formal structure, not the source of the formal structure.

## 4.4 Environment is not the system

External actors, hazards, and context remain outside the system boundary unless explicitly modeled as constituent elements.

## 4.5 Alternative behavior needs conditions

Alternative scenarios require:
- explicit trigger/condition;
- decision point;
- alternate path;
- resulting interaction or state.

Do not draw alternative scenarios as parallel arrows with no condition.

---

# 5. Diagram-Type Selection Matrix

Choose the diagram family from the scientific question.

| Question | Preferred diagram family |
|---|---|
| What is inside/outside? | system context / boundary diagram |
| What physically exists? | block / component / internal-structure diagram |
| What depends on what? | dependency graph / relational matrix |
| What transforms inputs to outputs? | IDEF0-style functional diagram |
| What happens in what order? | activity / process flow |
| Who interacts with whom over time? | sequence diagram |
| How does a system change modes? | state machine / hybrid-state diagram |
| How does a disturbance propagate? | causal state-flow / dynamic network |
| How are requirements mapped to variables? | relation / traceability / transformation diagram |
| How are models transformed? | source–mapping–target transformation diagram |
| How do variables relate mathematically? | equation-centered / mathematical dependency diagram |
| How does a system evolve through time? | state-time trajectory / event timeline |
| What is optimized subject to constraints? | decision / feasible-region diagram |
| What is the thesis logic? | layered conceptual framework |
| What do data show? | statistical chart, not a framework diagram |

If no family fits, define a custom grammar explicitly.

---

# 6. Viewpoint Rule

Every diagram must have one primary viewpoint.

Allowed viewpoint classes:

- **Context**
- **Structure**
- **Function**
- **Behavior**
- **Interaction**
- **State**
- **Causality**
- **Relation**
- **Mathematical transformation**
- **Service**
- **Decision/control**
- **Evidence/provenance**

If a diagram mixes viewpoints, the mix must be purposeful and visually separated into layers or panels.

Reject accidental mixes such as:

```text
component icons
+ equations
+ workflow arrows
+ resilience stages
+ charts
```

all floating at the same semantic level.

---

# 7. Diagram Specification Contract

Before rendering, create this internal specification.

```yaml
purpose:
audience:
main_message:
viewpoint:
scope_of_concerns:
system_of_interest:
inside_boundary:
outside_boundary:
elements:
relations:
arrow_semantics:
state_variables:
time_semantics:
functions:
services:
controls:
equations:
layout_logic:
label_text:
reference_basis:
prohibited_content:
rendering_mode:
validation_checks:
```

Do not render until the specification is internally coherent.

---

# 8. Element Register

Every object must have a reason to exist.

| ID | Element | Semantic type | Why included | Source/evidence |
|---|---|---|---|---|

Semantic types may include:

- physical component;
- actor;
- environment;
- interface;
- function;
- state;
- service;
- control;
- requirement;
- design variable;
- design objective;
- hazard;
- measurement;
- mathematical object.

Do not use visual objects with no semantic type.

---

# 9. Relation and Arrow Register

Every line or arrow must be registered before rendering.

| ID | Source | Target | Relation | Direction | Visual encoding | Evidence |
|---|---|---|---|---|---|---|

Default semantic classes:

| Encoding | Meaning |
|---|---|
| solid arrow | physical/information/material transfer |
| heavy causal arrow | cause/effect or state propagation |
| dashed arrow | control/intervention |
| dotted return arrow | observation/feedback |
| thin association line | structural relation without flow |
| bidirectional relation | two independently justified directions |
| boundary crossing arrow | external input/output |

Never use a bidirectional arrow as shorthand for “related”.

Never use arrows merely as decoration or reading-order markers.

---

# 10. Layout Must Encode Meaning

Position is semantic.

Use spatial conventions deliberately.

Examples:

- outside boundary = environment/context;
- inside boundary = system of interest;
- left-to-right = transformation or physical flow only when justified;
- top-to-bottom = hierarchy or decomposition;
- vertical lifelines = time/interaction when using sequence grammar;
- concentric regions = containment only;
- parallel lanes = actors/domains;
- aligned columns = source → mapping → target transformation;
- lower control layer = controller/decision only when clearly distinct from physics.

Do not center everything around one box unless the system is genuinely hub-centric.

Do not use symmetry if the underlying system is asymmetric.

---

# 11. Boundary Design

A system boundary must answer:

```text
what belongs to the system?
what interacts with it?
what crosses the boundary?
```

Represent:
- system of interest;
- external environment;
- external actors/hazards;
- inputs;
- outputs;
- interfaces.

The boundary line itself has semantic meaning.

Do not use a large rectangle only as decoration.

---

# 12. Labeling Rule

Labels must be:

- exact;
- short;
- domain-correct;
- consistent with project notation;
- large enough to read;
- free of invented terminology.

Use:
- noun phrases for components;
- verb–noun phrases for functions;
- physical quantities for flows;
- equations/symbols for mathematical objects.

Avoid vague labels:
- “process”;
- “system logic”;
- “smart layer”;
- “optimization”;
- “AI”;
- “resilience engine”;

unless specifically defined.

---

# 13. Equation Rule

Use equations only when they perform a visual function.

Good uses:
- defining state evolution;
- defining threshold;
- defining mapping;
- defining optimization objective;
- defining a relation.

Bad use:
- decorative formulas around the canvas;
- equations too small to read;
- equations unrelated to the arrows;
- using mathematics as visual decoration.

Every displayed equation must connect to an object, relation, or decision in the diagram.

---

# 14. Color Rule

Default:

- **pure white canvas exactly `#FFFFFF` / `RGB(255,255,255)`**;
- every panel, box, enclosure, and unused interior region must also remain `#FFFFFF` unless a scientifically justified exception is explicitly requested;
- black/dark charcoal text;
- restrained line colors;
- color only for semantic differentiation;
- no large colored panel backgrounds;
- no gray tint or off-white cast;
- no cream;
- no vignette;
- no shading;
- no texture;
- no gradients;
- no shadows;
- no paper/canvas effect;
- no gold unless explicitly requested.

When a generative image model is used, include the following instruction verbatim or equivalently strongly:

> **Pure white #FFFFFF background across the entire canvas and inside every panel/box. No gray, cream, off-white, shading, texture, gradient, shadow, vignette, or paper effect. Only semantically required text, lines, arrows, equations, and small color accents.**

A background that is visually gray, cream, off-white, shaded, textured, vignetted, or paper-like is a rendering defect and must be corrected before delivery.

Color must answer:

```text
what semantic distinction does this color encode?
```

If there is no answer, remove the color.

Maintain sufficient contrast.

Do not rely on color alone; combine with labels, line style, or shape.

---

# 15. Shape Rule

Use few shape classes.

Default:
- rectangle = component/system/function depending on declared grammar;
- rounded rectangle = only when the chosen notation assigns it meaning;
- ellipse = actor/use case/state only if notation requires;
- boundary = enclosure;
- line/arrow = relation;
- small annotation = equation/constraint/evidence note.

Do not vary shape for decoration.

A shape should not change meaning between different parts of the same diagram.

---

# 16. No Generic AI Aesthetic

Reject these defaults unless scientifically justified:

- neon glow;
- dark futuristic background;
- blue-purple gradients;
- glassmorphism;
- isometric city/utility scenes;
- random infrastructure icons;
- holographic rings;
- floating dashboards;
- decorative particles;
- circuit textures;
- 3D arrows;
- tiny repeated arrows;
- generic “brain/AI/cloud” symbols;
- oversized central circle with radial cards;
- ornamental shields, leaves, lightning bolts, gears, or globes;
- arbitrary colored quadrants;
- fake data charts;
- unreadable micro-text.

The visual should look like it came from a careful engineering or scientific modeling process.

---

# 17. Rendering Mode Selection

## 17.1 Deterministic vector mode

Prefer when:
- topology must be exact;
- labels must be exact;
- equations must be correct;
- arrow direction matters;
- figure will be published;
- user needs editable output.

Preferred outputs:
- SVG;
- TikZ;
- Mermaid;
- Graphviz;
- PlantUML;
- SysML-capable tooling;
- draw.io;
- Figma vector reconstruction.

## 17.2 Generative image mode

Use when:
- the user explicitly requests a generated image;
- conceptual illustration is useful;
- photorealistic or illustrative physical context is needed;
- exact topology is not the sole information carrier.

When generative rendering is used:

1. freeze the diagram specification first;
2. supply exact layout constraints;
3. use minimal decorative language;
4. preserve white background and semantic line styles;
5. inspect the output;
6. reject/regenerate if objects, labels, or arrows are invented or altered.

Do not trust a generative image as the authority for scientific content.

## 17.3 Hybrid mode

For high-value scientific figures:
- generate or draft the visual concept;
- reconstruct the final version deterministically as vector graphics;
- verify every semantic object.

---

# 18. Visual Hierarchy

Use hierarchy in this order:

1. title/main message;
2. system boundary or principal structure;
3. primary mechanism/flow;
4. secondary relations;
5. controls/feedback;
6. equations/annotations;
7. legend/source note.

Do not allow legends, decorative labels, or icons to compete with the mechanism.

---

# 19. Density Rule

A single diagram should usually communicate:

- one primary mechanism;
- one primary hierarchy;
- or one primary transformation.

If the diagram needs paragraphs to be understood, split it.

If more than one major question is being answered, create a figure family:

```text
A. Context
B. Structure
C. State-time behavior
D. Service consequence
E. Decision/control
```

---

# 20. Transformation Diagrams

For source-model → target-model transformations, use three explicit regions:

```text
SOURCE VIEW
→ MAPPING / TRANSFORMATION
→ TARGET VIEW
```

The transformation region must say what is preserved or mapped.

Examples:
- function → allocated component;
- activity → operation;
- use case → action;
- state → service capability;
- requirement → design variable;
- physical variable → normalized margin.

This avoids the common error of drawing two different views with an unexplained arrow between them.

---

# 21. State-Time Diagrams

When state and time are central:

Represent:

```math
X_i(t)
```

not separate decorative boxes named “STATE” and “TIME”.

Show when relevant:
- forcing (H(x,t));
- state trajectory (X_i(t));
- transition threshold;
- transition time (	au_i);
- propagation delay (delta_{ij});
- service trajectory (Q_k(t));
- recovery time.

A valid state-time visual should distinguish:

```text
forcing time
≠
state-transition time
≠
propagation delay
≠
service-transition time
≠
recovery time
```

---

# 22. Alternative Scenario Rule

For alternate behaviors:

```text
condition
→ decision point
→ alternate path
→ resulting state/interaction
```

Do not represent scenario alternatives by merely duplicating arrows.

Every alternate branch needs a trigger.

---

# 23. Scientific Figure QA

Before delivery, audit:

## Semantic QA
- [ ] one declared main message;
- [ ] correct viewpoint;
- [ ] correct scope of concerns;
- [ ] correct system boundary;
- [ ] no invented elements;
- [ ] every relation justified;
- [ ] every arrow has one meaning;
- [ ] no unsupported bidirectionality;
- [ ] functions distinct from components;
- [ ] state distinct from service;
- [ ] forcing distinct from internal state.

## Mathematical QA
- [ ] equations are correct;
- [ ] symbols are defined;
- [ ] units are compatible;
- [ ] transformations are traceable;
- [ ] no claim of instability without stability analysis;
- [ ] no claim of cascade without sequential dependent mechanism.

## Visual QA
- [ ] readable at intended size;
- [ ] background is exactly pure white `#FFFFFF / RGB(255,255,255)` unless explicitly changed;
- [ ] panel and box interiors are also pure white unless a scientific exception is explicitly justified;
- [ ] no gray/off-white tint, vignette, shading, texture, gradient, shadow, or paper effect;
- [ ] no decorative gradients/shadows;
- [ ] no generic AI visual motifs;
- [ ] arrows are large and clear;
- [ ] line crossings minimized;
- [ ] color is semantic;
- [ ] typography is consistent;
- [ ] alignment and spacing communicate hierarchy.

## Source QA
- [ ] source basis recorded;
- [ ] copyrighted figure not copied;
- [ ] source-derived concepts separated from project-specific modeling choices;
- [ ] current standards preferred over superseded standards.

## Rendering QA
- [ ] no misspelled labels;
- [ ] no duplicated objects;
- [ ] no missing arrowheads;
- [ ] no false connections;
- [ ] no clipped text;
- [ ] no unreadable equations;
- [ ] no image-generator hallucinations.

If any critical check fails, revise before delivery.

---

# 24. Workflow When the User Says “Design the Framework/Diagram”

If the semantics are already established in the conversation:

1. retrieve the relevant project/source context;
2. identify the main message;
3. select viewpoint;
4. build element and relation registers internally;
5. define the visual grammar;
6. freeze exact labels;
7. choose rendering mode;
8. render;
9. inspect against the QA checklist;
10. revise until valid.

Do not burden the user with the internal workflow unless they ask.

If semantics are not established, ask only the smallest necessary clarification.

---

# 25. Resource-Learning Workflow

When a user gives a paper, standard, screenshot, or reference image and says “learn from this”:

1. identify the source and copyright status;
2. extract the diagram grammar;
3. identify scope/boundary conventions;
4. identify semantic types;
5. identify arrow meanings;
6. identify transformations;
7. identify layout logic;
8. identify what is domain-specific versus generalizable;
9. record the transferable principles;
10. update the skill only when the lesson is broadly reusable.

Do not memorize a source-specific visual artifact as a universal style.

---

# 26. Improvement Protocol

Use semantic versioning.

Current version:

```text
1.0.1
```

Update when:
- a stronger standard supersedes a current reference;
- repeated rendering errors reveal a missing rule;
- new diagram families become necessary;
- user feedback establishes a stable design preference;
- a new evidence source provides a generally reusable modeling principle.

Do not update merely for one-off aesthetic preferences.

For every update:
1. state the observed problem;
2. identify the evidence;
3. change the smallest necessary rule;
4. test on at least two diagram types;
5. update changelog.

---

# 27. Foundational Resource Set

Read `resources/REFERENCE_BASE.md` for the maintained resource registry.

Core authorities include:
- ISO/IEC/IEEE 42010:2022;
- OMG SysML 2.0;
- NASA Systems Engineering Handbook;
- NIST IDEF0 / function-modeling guidance;
- OMG UPR / ROSETTA;
- OMG Math DSIG relational model-transformation work;
- project-approved visual rules.

---

# 28. Changelog

## 1.0.1

Pure-white rendering enforcement.

Added:
- exact `#FFFFFF / RGB(255,255,255)` canvas requirement;
- pure-white panel/box interior rule;
- explicit ban on gray, cream, off-white, vignette, shading, texture, gradients, shadows, and paper effects;
- exact generative-rendering instruction;
- QA failure condition for non-white scientific backgrounds.

## 1.0.0

Initial release.

Established:
- resource-grounded diagram generation;
- scope-of-concerns and viewpoint selection;
- diagram-type selection matrix;
- element/relation registers;
- transformation traceability;
- state-time visualization;
- boundary semantics;
- anti-generic-AI design rules;
- deterministic / generative / hybrid rendering modes;
- copyright-safe learning from references;
- scientific, mathematical, visual, source, and rendering QA.
