---
name: mathematical-visualization-design
description: Design mathematically driven scientific diagrams, interactive visualizations, animations, and framework figures in which geometry, color, motion, topology, and interaction are explicit encodings of model variables, relations, invariants, thresholds, and transformations. Use jointly with engineering-framework-design and scientific-diagram-design whenever a figure should be generated from mathematics rather than decorated around it.
license: MIT
---

# Mathematical Visualization Design

## Purpose

This skill enforces one principle:

[
oxed{
	ext{model} ightarrow 	ext{visual encoding} ightarrow 	ext{rendering}
}
]

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
- `engineering-framework-design`;
- `scientific-diagram-design`.

---

# 1. Model-First Rule

Before drawing anything, define the mathematical object being visualized.

Examples:

[
mathcal G=(V,E)
]

[
dot X=F(X,H,u;	heta)
]

[
T:M_1ightarrow M_2
]

[
Rsubseteq A	imes B
]

[
Q=G(X)
]

[
	au_i=inf{t:g_i(X_i(t))=0}
]

The visual is only a representation of this structure.

Reject:

[
	ext{nice-looking diagram} ightarrow 	ext{invented mathematical meaning}
]

Require:

[
	ext{defined mathematical meaning} ightarrow 	ext{visual form}
]

---

# 2. Visual Encoding Contract

Every visual channel must encode a declared mathematical or scientific quantity.

For each graphical property, define a mapping:

[
phi_k : 	ext{model quantity} ightarrow 	ext{visual channel}
]

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

[
phi_M(M_i)=	ext{node border width}
]

[
phi_	au(	au_i)=	ext{event location on timeline}
]

[
phi_delta(delta_{ij})=	ext{animation delay on edge }(i,j)
]

[
phi_Q(Q_k)=	ext{service trajectory height}
]

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

[
mathcal G=(V,E)
]

define:
- node set (V);
- edge set (E);
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

[
X_i(t)
]

not separate decorative boxes called “state” and “time”.

For the thesis:

[
H(x,t)
ightarrow
X_i(t)
ightarrow
	au_i^C
ightarrow
delta_{ij}
ightarrow
Q_k(t)
]

but do not force a serial visual chain if the mathematics is not serial.

If transition time, propagation delay, and service are parallel functionals of a state trajectory, visualize them as parallel derived quantities:

[
X(t)
ightarrow
egin{cases}
	au_i^C\
delta_{ij}\
Q_P(t),Q_T(t)
end{cases}
]

---

# 6. Continuous + Discrete Hybrid State

Use a hybrid representation when physical dynamics are continuous but operational modes are discrete.

Continuous state:

[
X_i(t)
]

Discrete mode:

[
q_i(t)in{N,D,C,F,R}
]

Transitions require explicit guards:

[
q_i:Nightarrow D
quad	ext{when}quad
g_i(X_i,t)=0
]

Visual implication:
- continuous variables control continuous visual changes;
- state transitions cause discrete visual changes;
- the guard condition must be traceable.

Do not animate a “failure” transition without a defined event condition.

---

# 7. Invariants and Constraints Must Be Visible

If a model is constrained by:

[
g(X,t)le 0
]

the visualization should distinguish:
- feasible region;
- boundary;
- violation region;
- trajectory.

For viability:

[
X(t)inmathcal V(t)
]

represent the viability set geometrically when possible.

For service:

[
Q(t)ge Q^{min}
]

make the acceptable-service threshold explicit.

This creates visuals that explain the mathematics instead of merely displaying it.

---

# 8. Transformation-Driven Diagrams

When the figure shows a model transformation, define the transformation first:

[
T:M_1ightarrow M_2
]

Then visually show:
- source object;
- transformation;
- target object;
- what is preserved;
- what changes.

Examples:
- raw physical variable (ightarrow) normalized physical margin;
- state (ightarrow) capability;
- capability (ightarrow) service;
- component event (ightarrow) system consequence;
- observation (ightarrow) state estimate;
- design variable (ightarrow) modified dynamics.

Never draw an unexplained arrow between two views.

---

# 9. Mathematical Color Rule

Color is a mathematical encoding, not decoration.

Use color only when it represents a declared class or quantity.

Default thesis semantic palette:
- external hazard/forcing: vermillion `#D55E00`;
- physical/empirical system: bluish green `#009E73`;
- mathematical dynamics/analysis: blue `#0072B2`;
- engineering intervention/decision: dark amber `#B86E00`;
- neutral scientific content: black `#000000`;
- all backgrounds/interiors: pure white `#FFFFFF`.

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
- (X_i(t));
- (M_i(t));
- (	au_i);
- (delta_{ij});
- (Q_k(t));
- parameter sweep (lambda);
- control input (u(t)).

Examples:

[
X_i(t)mapsto 	ext{node geometry}
]

[
M_i(t)mapsto 	ext{border emphasis}
]

[
delta_{ij}mapsto 	ext{edge animation delay}
]

[
Q_k(t)mapsto 	ext{service trajectory}
]

Animation speed must represent time or another defined parameter when possible.

Do not use looping motion merely to look advanced.

---

# 11. Interaction Rule

Interactive controls must correspond to model parameters.

Examples:
- ambient temperature slider (ightarrow T_{mathrm{amb}});
- heat duration slider (ightarrow Delta t);
- load slider (ightarrow L_i);
- design parameter control (ightarrow 	heta);
- adaptation control (ightarrow u_A(t)).

Every interaction must update:
1. the mathematical model;
2. the derived variables;
3. the visual encoding.

This is the core interactive loop:

[
	ext{parameter}
ightarrow
	ext{model recomputation}
ightarrow
	ext{derived state}
ightarrow
	ext{visual update}
]

---

# 12. Thesis-Specific Mathematical Visualization Spine

For the extreme-heat coupled Power–Transportation thesis, use:

[
H(x,t)
ightarrow
X(t)
ightarrow
{	au_i^C,delta_{ij},Q_P(t),Q_T(t)}
ightarrow
{	ext{Improve, Adapt, Restore}}
]

where:

[
X(t)=
[X_P^	op,Z^	op,X_T^	op]^	op
]

The interface state (Z(t)) is not a decorative middle box. It represents modeled interface conditions.

Use the physical architecture:

[
mathcal P
leftrightarrow
mathcal I_{PT}
leftrightarrow
mathcal T
]

only when each direction has an explicit exchanged quantity.

Recommended mathematical views:

### A. State trajectory view
Show (X_i(t)) against time.

### B. Threshold view
Show (g_i(X_i,t)=0) and (	au_i^C).

### C. Propagation view
Show event pair and delay:

[
delta_{ij}
=
	au_j^{mathrm{response}}
-
	au_i^{mathrm{transition}}
]

### D. Service view
Show:

[
Q_P(t),Q_T(t),Q^{min}
]

### E. Intervention view
Show how:
- Improve modifies (	heta);
- Adapt modifies (u_A(t));
- Restore modifies (u_R(t)).

---

# 13. Script Architecture

For code-based scientific visualization, separate:

```text
MODEL
→ DERIVED QUANTITIES
→ VISUAL ENCODING
→ RENDERER
→ INTERACTION
→ VALIDATION
```

Recommended modules:

```text
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
```

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

[
	ext{formal specification}
ightarrow
	ext{SVG/TikZ/draw.io}
ightarrow
	ext{QA}
ightarrow
	ext{PNG/PDF export}
]

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

[
oxed{
	ext{mathematical structure drives the visual}
}
]

not:

[
	ext{imitate the source image}
]

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

# 20. Changelog

## 1.0.0

Initial release.

Established:
- model-first mathematical visualization;
- visual encoding functions;
- geometry/topology semantics;
- state-time and hybrid-state visualization;
- constraint/viability visualization;
- transformation-driven diagrams;
- mathematical color semantics;
- equation-driven animation and interaction;
- thesis-specific state-time resilience views;
- deterministic script architecture;
- renderer selection;
- mathematical-backstory requirement;
- comprehensive QA gates.
