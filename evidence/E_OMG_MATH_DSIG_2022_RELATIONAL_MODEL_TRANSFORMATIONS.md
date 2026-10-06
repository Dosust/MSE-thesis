# E-OMG-MATH-DSIG-2022 — Relational Model Transformations for SysML

**Status:** ADMITTED METHODOLOGICAL / DIAGRAM-SEMANTICS EVIDENCE  
**Date admitted:** 2026-10-06  
**Primary use:** scope-of-concerns discipline, relational model transformations, model-view traceability, mathematical foundations for systems diagrams, function-to-behavior-to-structure transformations  
**Authority:** Object Management Group Mathematical Formalism DSIG paper  
**Thesis adoption status:** SUPPORTING MODELING / VISUALIZATION EVIDENCE

## Source identity

C. E. Dickerson, S. Ji, M. K. Wilkinson.  
*SysML Model Transformations Using Relational Orientation.*  
OMG Mathematical Formalism DSIG.  
Document identifier: **mathsig/2022-09-01**.  
12 September 2022.

User-supplied filename:

```text
Math-DSIG-Paper.pdf
```

SHA-256 of the uploaded file:

```text
2a0966887b6c074762fc6c5337b016e47a6de5962dbfd22d5a8c6542ce0b1ead
```

The paper contains explicit copyright restrictions. The PDF and its figures are therefore **not republished in this repository**. This record stores only provenance and a project-specific analytical extraction.

## 1. Main methodological lesson

The paper treats graphical SysML/UML models as semantic structures and emphasizes mathematically grounded transformations between model types.

Project implication:

```text
diagram
≠
decorative image

diagram
=
semantic model view for a declared concern
```

## 2. Scope-of-concerns discipline

The paper repeatedly organizes views around a declared scope of concerns, including:
- actors;
- functionality;
- use cases and inclusions;
- actions;
- system elements and operations;
- interactions;
- control structure;
- scenario integration.

Project rule:

```text
one view should answer one principal concern
```

If several concerns are necessary, create coordinated views rather than one overloaded picture.

## 3. System and environment

The paper defines a system together with its environment and distinguishes entities that are associated with a system but not part of it.

Project rule:

```text
environment/context
≠
system-of-interest
```

This strengthens the existing framework boundary rule.

## 4. Graph and matrix interpretation

The paper states that graphical models may be represented through vertices and edges and therefore admit matrix representations.

Project use:
- relation register;
- adjacency/dependency matrices;
- traceability matrices;
- source–mapping–target model transformations.

Boundary:
- matrix relation alone does not establish physical causality.

## 5. Traceable model transformations

The paper presents a progression from:
- actors/environment;
- functionality;
- functional decomposition;
- use-case descriptions;
- activity behavior;
- functional allocation;
- system elements;
- interoperation;
- sequence behavior;
- alternative scenarios.

Project rule:

```text
when changing diagram type,
define what is being mapped and preserved
```

Do not place two diagrams beside each other with an unexplained arrow.

## 6. Functionality to behavior

The paper illustrates transformation from external actor interactions and use cases into actionable behavior.

Project relevance:
- distinguish what a system **must do** from how it **behaves**;
- distinguish function from component;
- use activity/process views for action flow rather than structural arrows.

## 7. Functional allocation to physical/logical structure

The paper associates actions with operations of system elements.

Project rule:

```text
Function
→ allocation relation
→ physical/logical element
```

Do not visually imply that a component performs a function unless the allocation is explicit.

## 8. Interaction and sequence

The paper uses sequence-oriented views when ordering of interactions and message exchange becomes important.

Project rule:
- use sequence/timeline grammar when temporal order between interacting elements is the concern;
- do not force temporal semantics into a static architecture diagram.

## 9. Alternative behavior

The paper represents alternative scenarios through extension conditions and control/decision structures.

Project rule:

```text
alternative path
requires
explicit trigger / condition
```

Do not use parallel arrows as a substitute for conditional behavior.

## 10. Mathematics from the beginning

The paper explicitly criticizes developing MBSE models without exploiting mathematical foundations until after the model has been produced.

Project rule:

```text
formal semantics first
→ graphical model second
```

For thesis diagrams, define equations, relations, constraints, states, or transformations before final rendering whenever the figure claims mathematical meaning.

## 11. Diagram-generation implications

This evidence directly supports the new skill:

```text
.github/skills/scientific-diagram-design/SKILL.md
```

Key requirements transferred into the skill:
- reference-based design;
- scope-of-concerns selection;
- viewpoint selection;
- model-transformation traceability;
- original rendering rather than figure copying;
- system/environment separation;
- structure/function/behavior distinction;
- alternative-scenario conditions;
- mathematical foundation before visual decoration.

## 12. Limits

This paper does not establish:
- the physics of extreme heat;
- resilience metrics;
- final thesis state equations;
- a universal visual style;
- that every scientific diagram must use SysML.

Use it for model semantics and transformation discipline, not as the sole visual standard.
