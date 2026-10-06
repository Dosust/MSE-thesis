---
name: engineering-framework-design
description: Design, audit, and improve rigorous scientific and engineering frameworks with explicit system boundaries, environments, system-of-interest elements, interfaces, state-time dynamics, functions, services, flows, controls, outputs, arrow semantics, and validation rules. Use for thesis frameworks, systems-engineering architectures, resilience frameworks, lifecycle-style system diagrams, physics-based mathematical-engineering frameworks, and any visual or conceptual framework where every box and arrow must have a defined scientific meaning.
license: MIT
---

# Engineering Framework Design

## Purpose

Use this skill to design **frameworks**, not infographics.

A valid engineering framework must make explicit:

1. the analytical purpose;
2. the external environment;
3. the system of interest;
4. the system boundary;
5. what is inside and outside the boundary;
6. internal physical or logical elements;
7. interfaces between elements;
8. inputs, outputs, controls, and feedbacks;
9. physical flows versus causal propagation;
10. state variables and their evolution in time;
11. functions and services;
12. intervention points;
13. assumptions and validity limits;
14. the meaning of every arrow;
15. the evidence or standard supporting important semantics.

The framework must answer:

> What exists, what is outside, what crosses the boundary, what interacts, what changes state, what flows, what causes what, what is measured, what is controlled, what service is produced, and why each relationship is drawn.

---

# 1. Core Rule

Never start by drawing boxes.

Start in this order:

\[
\boxed{
\text{Purpose}
\rightarrow
\text{Boundary}
\rightarrow
\text{Elements}
\rightarrow
\text{Interfaces}
\rightarrow
\text{Flows}
\rightarrow
\text{States}
\rightarrow
\text{Functions}
\rightarrow
\text{Services}
\rightarrow
\text{Controls}
\rightarrow
\text{Visual Structure}
}
\]

A visually attractive diagram that does not satisfy these semantics is an **infographic**, not an engineering framework.

---

# 2. Authority and Evidence Hierarchy

When defining framework semantics, use the following evidence priority:

1. **Governing standards and official technical guides**
   - ISO
   - IEC
   - IEEE
   - ASME
   - NIST
   - NASA handbooks
   - recognized national/international engineering standards

2. **Systems-engineering authorities**
   - INCOSE
   - OMG SysML
   - NASA Systems Engineering Handbook
   - NIST IDEF0

3. **Peer-reviewed domain literature**
   - governing physics
   - mathematical models
   - interface definitions
   - failure/degradation mechanisms
   - service models
   - resilience models

4. **Operator/manufacturer documentation**
   - operating limits
   - derating curves
   - intervention procedures
   - service restrictions

5. **Model inference**
   - use only when evidence is insufficient;
   - label explicitly as a proposed modeling choice.

Never present a modeling convenience as an established physical fact.

---

# 3. Framework Quality Gates

A framework is not ready for visualization until all applicable gates pass.

## Gate 0 — Purpose

State one precise analytical purpose.

Template:

> The framework is designed to determine **[what changes]**, **[under what forcing/condition]**, **[through what mechanisms]**, **[with what service consequence]**, and **[for what engineering decision]**.

Reject:
- “show the system”
- “present the methodology”
- “illustrate resilience”

Prefer:
- “determine how heat-driven state transitions propagate through coupled power–transport interfaces and alter service trajectories over time.”

---

## Gate 1 — External Environment

Identify everything that affects the system but is not itself an engineered system component.

Examples:
- weather;
- extreme heat;
- flood;
- market demand;
- regulation;
- external resource supply.

Represent external forcing outside the system boundary.

General form:

\[
H(x,t)
\rightarrow
\text{System of Interest}
\]

Do not draw a hazard as if it were an internal component.

---

## Gate 2 — System of Interest and Boundary

Define the **System of Interest (SoI)** before defining internal elements.

Specify boundaries in four dimensions when relevant:

- **Physical boundary** — which assets/components are included?
- **Spatial boundary** — corridor, feeder, city, region, site?
- **Temporal boundary** — seconds, hours, days, lifecycle?
- **Operational boundary** — normal operation, disturbance, recovery?

Write explicitly:

### Inside
- included components;
- interfaces;
- state variables;
- functions;
- services.

### Outside
- excluded infrastructure;
- external hazards;
- external actors;
- unsupported mechanisms.

Never hide scope in the drawing.

---

# 4. Structure, Behavior, and Service Must Be Separate

A rigorous framework distinguishes at least three semantic levels:

\[
\boxed{
\text{Physical / Logical Structure}
\rightarrow
\text{State-Time Behavior}
\rightarrow
\text{Function}
\rightarrow
\text{Service}
}
\]

## Structure

Answers:

> What physically or logically exists?

Examples:
- transformer;
- conductor;
- traction substation;
- rail;
- catenary;
- battery;
- charging station;
- control center.

## Behavior

Answers:

> How does its condition evolve?

General form:

\[
\dot X_i
=
f_i(X_i,U_i,H,Z_{ji};\theta_i)
\]

## Function

Answers:

> What engineering operation does the element perform?

Examples:
- transform voltage;
- deliver traction power;
- collect electrical current;
- support guided mobility;
- store electrical energy.

## Service

Answers:

> What user/system-level outcome is delivered?

Examples:
- electricity service;
- mobility service;
- train frequency;
- passenger throughput;
- available charging service.

Never label a physical component as a service or a service as a component.

---

# 5. Interface Rule

An interface is a location or relationship through which two system elements **exchange something physically or functionally meaningful**.

For every interface \(Z_{ij}\), define:

1. source element \(i\);
2. destination element \(j\);
3. exchanged quantity;
4. direction;
5. units if applicable;
6. governing constraint or law;
7. state dependence;
8. time dependence.

Interface register template:

| ID | Source | Interface | Destination | Exchange | Direction | Governing relation |
|---|---|---|---|---|---|---|
| \(Z_{ij}\) | Element \(i\) | Interface name | Element \(j\) | power/data/material/etc. | → / ↔ | equation/constraint |

Do not connect two boxes solely because they are related conceptually.

---

# 6. Arrow Grammar

Every arrow must belong to a declared semantic class.

Default grammar:

| Visual | Semantic meaning | Use |
|---|---|---|
| **Solid single arrow →** | physical or conserved flow | energy, material, traffic, information when treated as transferred quantity |
| **Large causal arrow ⇒** | causal/state-effect propagation | state \(X_i\) changes state/capability \(X_j\) |
| **Dashed arrow ⇢** | control/intervention | command, adaptation action, design intervention |
| **Dotted return arrow ⋯→** | measurement/feedback | observations returning to estimator/controller |
| **Bidirectional ↔** | two distinct directional interactions | use only when both directions are explicitly defined |

## Arrow requirements

Every arrow must have:

- a source;
- a destination;
- a verb or exchanged quantity;
- a semantic type;
- a reason for inclusion.

Preferred arrow label format:

\[
\text{quantity / mechanism}
\]

Examples:
- `electrical power`
- `thermal forcing`
- `state propagation`
- `measurement`
- `control action`
- `mobility demand`

Never use unlabeled arrows when their meaning could be ambiguous.

Never use arrows merely to indicate reading order.

If visual reading order is needed, use layout hierarchy instead.

---

# 7. Input, Output, Control, Mechanism

Use IDEF0-style reasoning when useful.

For every analytical function, ask:

- **Input:** What is transformed?
- **Output:** What is produced?
- **Control:** What constrains or governs the transformation?
- **Mechanism:** What performs the transformation?

Generic function:

\[
Y
=
\mathcal F(X;C,M)
\]

where:
- \(X\) = input;
- \(Y\) = output;
- \(C\) = control/constraint;
- \(M\) = mechanism.

Do not mix controls with physical flows.

---

# 8. State–Time Rule

State and time are not independent decorative boxes.

Represent them jointly as:

\[
X_i(t)
\]

where \(X_i(t)\) is the minimum set of variables required to describe the condition of element \(i\) at time \(t\).

General state evolution:

\[
\dot X_i
=
f_i(X_i,H,L_i,Z_{ji},u_i;\theta_i)
\]

where:
- \(H\) = external forcing;
- \(L_i\) = operating load;
- \(Z_{ji}\) = interface input;
- \(u_i\) = control;
- \(\theta_i\) = parameters.

Distinguish:

\[
\boxed{
\text{forcing}
\neq
\text{state}
\neq
\text{function}
\neq
\text{service}
}
\]

---

# 9. Continuous State and Operational State

When systems exhibit both continuous physics and discrete operating modes, use a hybrid representation.

Continuous state:

\[
X_i(t)
\]

Operational state:

\[
q_i(t)
\in
\{N,D,C,F,R\}
\]

Default interpretation:
- \(N\): nominal;
- \(D\): derated/degraded;
- \(C\): critical;
- \(F\): function lost;
- \(R\): recovering.

Transitions must be tied to explicit guards or thresholds.

Example:

\[
q_i:N\rightarrow D
\quad \text{when} \quad
g_i(X_i)\le 0
\]

Do not assume all components follow the same threshold physics.

---

# 10. Time Metrics

Use time as an analytical variable, not simply an x-axis.

Possible quantities:

## Time to derating

\[
\tau_i^D
=
\inf\{t:q_i(t)=D\}
\]

## Time to critical state

\[
\tau_i^C
=
\inf\{t:q_i(t)=C\}
\]

## Time to functional loss

\[
\tau_i^F
=
\inf\{t:q_i(t)=F\}
\]

## Propagation delay

\[
\delta_{ij}
=
\tau_j^{\mathrm{response}}
-
\tau_i^{\mathrm{transition}}
\]

## Service transition time

\[
\tau_k^S
=
\inf\{t:Q_k(t)<Q_k^{\min}\}
\]

## Recovery time

\[
\tau_k^R
=
\inf\{t>t_f:Q_k(t)\ge Q_k^{\min}\}
-
t_f
\]

Never treat:
- state transition time;
- propagation delay;
- service transition time;
- restoration time

as interchangeable.

---

# 11. Physical Margin

Do not compare heterogeneous components using raw temperature alone.

Where defensible, define a normalized physical margin:

\[
M_i(t)
=
\frac{x_i^{\lim}-x_i(t)}
{x_i^{\lim}-x_i^{\mathrm{nom}}}
\]

or another component-specific nondimensional margin derived from the governing physics.

Purpose:

\[
\text{heterogeneous physical variables}
\rightarrow
\text{comparable proximity to constraint}
\]

Do not invent a normalized margin if the physical limit is not meaningful or evidence-supported.

---

# 12. Propagation Rule

Propagation is not simply topology.

A rigorous propagation statement includes state and time:

\[
(X_i,\tau_i)
\rightarrow
(Z_{ij},\delta_{ij})
\rightarrow
(X_j,\tau_j)
\rightarrow
(Q_k,\tau_k^S)
\]

Before drawing propagation, establish:

1. causal mechanism;
2. interface;
3. direction;
4. state dependence;
5. delay/timescale;
6. service consequence.

Distinguish:

\[
\boxed{
\text{connection}
\neq
\text{dependency}
\neq
\text{feedback}
\neq
\text{cascade}
\neq
\text{instability}
}
\]

Do not label a process a cascade unless sequential dependent degradation/failure is demonstrated.

Do not label a process unstable unless a mathematical stability criterion supports it.

---

# 13. Service Rule

Component state matters only insofar as it affects function or the research objective.

Define service variables explicitly:

\[
Q_k(t)
\]

Examples:

\[
Q_P(t)=\text{power-service performance}
\]

\[
Q_T(t)=\text{mobility-service performance}
\]

Service threshold:

\[
Q_k(t)\ge Q_k^{\min}
\]

Service deficit:

\[
D_k
=
\int_{t_0}^{T}
[Q_k^{\mathrm{req}}-Q_k(t)]_+
\,dt
\]

Never rank components only by physical degradation if the objective is resilience.

Always connect:

\[
\text{physical state}
\rightarrow
\text{functional capability}
\rightarrow
\text{service consequence}
\]

---

# 14. Resilience Control Grammar

When the framework uses the sequence **Improve → Adapt → Restore**, treat these as engineering interventions or controls, not physical system layers.

## Improve

Acts primarily before disturbance.

Purpose:

\[
\text{change baseline design, parameters, capacity, or margin}
\]

Mathematical effect:

\[
\theta_i
\rightarrow
\theta_i'
\]

Desired outcome:

\[
\tau_i^{C\prime}>\tau_i^C
\]

or critical transition is avoided.

## Adapt

Acts during disturbance.

Purpose:

\[
\text{steer the state trajectory while forcing persists}
\]

Mathematical form:

\[
\dot X
=
F(X,H,u_A,t)
\]

Desired outcome:

\[
X(t)\in\mathcal K_{\mathrm{safe}}
\]

or delay/avoid critical transitions.

## Restore

Acts after unacceptable service or function loss.

Purpose:

\[
\text{return physical/function/service state to acceptable region}
\]

Desired outcome:

\[
Q_k(t)\ge Q_k^{\min}
\]

as quickly and robustly as possible.

Controls should point **into** the system using the declared control-arrow style.

---

# 15. Decision Layer

Mathematical engineering converts physical models into decisions.

Possible decision problem:

\[
u^*
=
\arg\min_u
\left[
D_{\mathrm{service}}(u)
+
C_{\mathrm{intervention}}(u)
\right]
\]

subject to:

\[
\dot X=F(X,H,u,t)
\]

\[
g(X,u,t)\le 0
\]

The framework must show where decision variables act.

Do not draw optimization/control as if it were physical infrastructure.

---

# 16. Feedback and Observation

If state estimation, sensing, monitoring, or a digital twin is in scope, show it explicitly as a feedback path.

Observation:

\[
y(t)=h(X(t))+\varepsilon(t)
\]

Estimator:

\[
y(t)\rightarrow\hat X(t)
\]

Controller:

\[
\hat X(t)\rightarrow u(t)
\]

Use dotted return arrows for measurement/feedback unless the project specifies a different legend.

Do not add a digital twin merely for visual sophistication.

---

# 17. Framework Construction Workflow

When asked to design a framework, execute the following workflow.

## Step 1 — Read the research objective

Extract:
- system;
- disturbance/forcing;
- states;
- interfaces;
- services;
- decisions;
- scope exclusions.

## Step 2 — Write the purpose sentence

Do not draw yet.

## Step 3 — Create a boundary table

| Category | Inside | Outside | Reason |
|---|---|---|---|

## Step 4 — Create an element register

| ID | Element | Type | State variables | Function | Service contribution |
|---|---|---|---|---|---|

Types may include:
- physical component;
- interface;
- external forcing;
- function;
- service;
- controller;
- observer.

## Step 5 — Create an interface register

Use the template in Section 5.

## Step 6 — Create an arrow register

| ID | Source | Destination | Arrow type | Label | Scientific meaning |
|---|---|---|---|---|---|

No arrow may enter the final diagram unless it appears in this register.

## Step 7 — Define state-time equations

Only as detailed as necessary.

Prefer **minimum sufficient physics**.

## Step 8 — Define service mapping

\[
X
\rightarrow
C
\rightarrow
Q
\]

## Step 9 — Define controls

Specify where Improve, Adapt, Restore act.

## Step 10 — Build the framework architecture

Use hierarchy and geometry before decoration.

## Step 11 — Add a compact legend

Include:
- boundary meaning;
- arrow meaning;
- symbol meaning;
- color meaning if used.

## Step 12 — Audit against the quality checklist

Only after passing the audit may the framework be rendered as an image, slide, SVG, Mermaid diagram, draw.io diagram, Figma design, or other visual.

---

# 18. Framework Output Structure

When producing a framework specification, return in this order:

## A. Framework purpose

One sentence.

## B. System boundary

Inside / outside.

## C. Core elements

Only elements necessary for the objective.

## D. Interfaces

Explicit exchanges.

## E. State-time spine

\[
H(x,t)
\rightarrow
X_i(t)
\rightarrow
\tau_i
\rightarrow
Z_{ij}(t)
\rightarrow
Q_k(t)
\]

or the domain-specific equivalent.

## F. Controls

Improve / Adapt / Restore if applicable.

## G. Arrow legend

Mandatory.

## H. Visual layout

Describe exact spatial placement.

## I. Evidence basis

Cite standards/literature supporting major semantics.

---

# 19. Visual Design Rules

Default to scientific, publication-quality design.

## Canvas

- white background;
- no gradients;
- no textures;
- no shadows;
- no decorative background panels;
- no gold unless explicitly requested.

## Color

Use color only for:
- borders;
- headings;
- icons;
- arrows;
- lines;
- small semantic accents.

Avoid large filled colored regions.

## Arrows

- large enough to read;
- directional;
- minimal;
- scientifically meaningful;
- labeled when needed;
- visually differentiated by semantic class.

Never use many small decorative arrows.

## Boxes

Every box must represent one semantic category:
- component;
- interface;
- function;
- service;
- state model;
- control;
- environment.

Do not use boxes merely to fill space.

## Density

Prefer fewer, more meaningful elements.

If the framework contains too much text to understand at normal presentation size, simplify the architecture and move explanation into notes/caption.

---

# 20. Domain Adaptation Rule

This skill is domain-general.

Do not hard-code components from one project into all future frameworks.

Instead:

1. preserve the grammar;
2. replace domain elements;
3. replace governing equations;
4. replace interfaces;
5. replace service variables;
6. preserve arrow semantics unless a documented reason requires extension.

Example domains:
- coupled infrastructure;
- energy systems;
- transportation;
- water systems;
- manufacturing;
- lifecycle assessment;
- cyber-physical systems;
- healthcare systems;
- environmental systems.

---

# 21. Anti-Patterns

Reject or revise any framework that does one or more of the following:

- starts from visual boxes before defining purpose;
- lacks a system boundary;
- mixes external hazards with internal components;
- uses arrows without defined semantics;
- uses arrows only for reading order;
- treats a component as a function;
- treats a function as a service;
- mixes state with forcing;
- represents time as a decorative box;
- labels every relationship “interdependency”;
- assumes bidirectionality without two defined mechanisms;
- compares heterogeneous assets only by raw temperature;
- calls propagation a cascade without evidence;
- calls behavior unstable without stability analysis;
- places Improve/Adapt/Restore inside the physical architecture as components;
- adds digital twin, AI, optimization, or control without analytical need;
- uses large colored backgrounds or decorative effects that obscure semantics;
- contains more text than the diagram can communicate visually;
- reproduces an infographic when the task requires a framework.

---

# 22. Scientific Audit Checklist

Before finalizing, answer **yes** to all applicable items.

### Boundary
- [ ] Is the system of interest explicitly named?
- [ ] Is the boundary visibly drawn?
- [ ] Is the external environment outside the boundary?
- [ ] Are exclusions stated?

### Structure
- [ ] Are physical/logical elements distinct from functions?
- [ ] Are interfaces represented explicitly?
- [ ] Are services separate from components?

### Dynamics
- [ ] Are relevant state variables identified?
- [ ] Is time embedded in state evolution?
- [ ] Are state transitions defined where needed?
- [ ] Are propagation delays/timescales explicit where relevant?

### Arrows
- [ ] Does every arrow have one semantic meaning?
- [ ] Is the arrow type in the legend?
- [ ] Is bidirectionality justified?
- [ ] Are control and feedback arrows distinct from physical flow?

### Resilience
- [ ] Is service performance defined?
- [ ] Can the framework identify when service degrades?
- [ ] Are Improve, Adapt, Restore placed as interventions?
- [ ] Is recovery represented as service/state restoration rather than only repair?

### Evidence
- [ ] Are important definitions tied to authoritative references?
- [ ] Are governing physics supported?
- [ ] Are assumptions distinguished from established facts?
- [ ] Are validity boundaries stated?

### Visual
- [ ] Is the diagram readable without explanatory paragraphs?
- [ ] Does every visual element have a scientific purpose?
- [ ] Is the white-background/minimal design rule respected?
- [ ] Can a reader explain every arrow after reading the legend?

If any critical item fails, revise before rendering.

---

# 23. Improvement and Versioning Protocol

This skill is intended to evolve.

## Versioning

Use semantic versioning:

\[
\text{MAJOR.MINOR.PATCH}
\]

- **MAJOR** — changes the framework grammar or core semantics.
- **MINOR** — adds a new supported method, arrow type, validation gate, or domain pattern without breaking existing rules.
- **PATCH** — clarifies wording, fixes errors, improves examples, or updates references.

Current conceptual version:

`1.0.0`

## Update rule

Update this skill when:

- a governing standard changes;
- a stronger systems-engineering convention is identified;
- repeated framework failures reveal a missing quality gate;
- a new domain requires a genuinely new semantic relation;
- an arrow type is consistently needed and cannot be represented by existing grammar;
- validation shows a rule causes ambiguity or scientific error.

Do **not** change the core rules merely because a new visual style is preferred.

## Update procedure

1. identify the observed problem;
2. state which existing rule is insufficient;
3. collect authoritative evidence;
4. propose the smallest change;
5. test the change against at least:
   - one existing framework;
   - one new framework;
6. verify backward compatibility;
7. increment version;
8. record the change in the changelog.

---

# 24. Changelog

## 1.0.0

Initial release.

Established:
- boundary-first framework construction;
- external environment versus system-of-interest distinction;
- structure / behavior / function / service separation;
- explicit interface register;
- semantic arrow grammar;
- state-time modeling;
- hybrid operational states;
- propagation delay;
- service mapping;
- Improve / Adapt / Restore as control semantics;
- framework quality gates;
- scientific audit checklist;
- visual minimalism rules;
- version/update protocol.

---

# 25. Foundational References

Use the latest applicable edition when executing the skill.

- NASA Systems Engineering Handbook  
  https://www.nasa.gov/reference/systems-engineering-handbook/

- INCOSE Systems Engineering resources  
  https://www.incose.org/

- OMG Systems Modeling Language (SysML)  
  https://www.omg.org/sysml/

- NIST IDEF0 / FIPS 183  
  https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub183.pdf

- ISO 14040 — Life Cycle Assessment principles and framework  
  https://www.iso.org/standard/37456.html

- GitHub Agent Skills documentation  
  https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills

- OpenAI Skills documentation  
  https://developers.openai.com/api/docs/guides/tools-skills

---

# 26. Thesis-Specific Profile: Physics-Based State-Time Resilience

Apply this profile only when the task concerns physics-based resilience of coupled infrastructure.

Canonical analytical spine:

\[
\boxed{
H(x,t)
\rightarrow
X_i(t)
\rightarrow
\text{state transition}
\rightarrow
(Z_{ij},\delta_{ij})
\rightarrow
Q_k(t)
\rightarrow
\text{Improve / Adapt / Restore}
}
\]

Interpretation:

- \(H(x,t)\): external hazard forcing;
- \(X_i(t)\): continuous physical state;
- \(q_i(t)\): operational state;
- \(\tau_i\): transition time;
- \(Z_{ij}\): physical/functional interface;
- \(\delta_{ij}\): propagation delay;
- \(Q_k(t)\): service trajectory;
- Improve: modify baseline design/state;
- Adapt: modify trajectory during disturbance;
- Restore: recover acceptable state/service.

Core conceptual distinctions:

\[
\boxed{
\text{forcing}
\neq
\text{state}
\neq
\text{function}
\neq
\text{service}
}
\]

\[
\boxed{
\text{connection}
\neq
\text{dependency}
\neq
\text{feedback}
\neq
\text{cascade}
\neq
\text{instability}
}
\]

\[
\boxed{
\text{Physical element}
\rightarrow
\text{Function}
\rightarrow
\text{Service}
}
\]

Use component-specific physics and unify only at the level required by the research question. Never replace different governing laws with a fake universal physical equation.

---

# 27. Final Instruction to the Agent

When this skill is active:

**Do not immediately generate the framework image.**

First produce and internally validate:

1. purpose;
2. boundary;
3. inside/outside;
4. element register;
5. interface register;
6. arrow register;
7. state-time spine;
8. service mapping;
9. control mapping;
10. evidence basis.

Only then create the visual.

If the user asks directly for an image and the framework semantics are already established in the conversation, reuse those established semantics rather than restarting.

The standard of success is not visual attractiveness.

The standard is:

\[
\boxed{
\textbf{Every boundary, box, interface, arrow, state, function, service, and control has one clear scientific meaning.}
}
\]