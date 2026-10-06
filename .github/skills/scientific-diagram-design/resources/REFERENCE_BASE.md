# Reference Base — Scientific Diagram Design

This file records the authoritative sources used to evolve the scientific-diagram-design skill.

The purpose is **not** to copy figures. The purpose is to learn stable modeling and visual-grammar principles.

---

## 1. OMG Math DSIG — SysML Model Transformations Using Relational Orientation (2022)

**Document identifier:** OMG mathsig/2022-09-01  
**Authors:** C. E. Dickerson, S. Ji, M. K. Wilkinson  
**Date:** 12 September 2022  
**Project evidence record:** `../../../evidence/E_OMG_MATH_DSIG_2022_RELATIONAL_MODEL_TRANSFORMATIONS.md`

Transferable principles:

- diagrams should represent semantic structures, not decoration;
- declare a scope of concerns;
- system and environment are distinct;
- graphical models can be interpreted as vertices/edges and matrices;
- transformations between model views should be traceable;
- functionality can transform into actionable behavior;
- behavior can be allocated to system elements;
- interaction/order can require sequence-type views;
- alternate scenarios require explicit control conditions;
- mathematics should be integrated into modeling from the beginning rather than added after visual model development.

Copyright rule:
- do not reproduce the paper's figures;
- use only the abstract modeling principles.

---

## 2. OMG UPR / ROSETTA v1.0 (2019)

Official:
https://www.omg.org/spec/UPR/1.0

Project evidence:
`../../../evidence/E_ROSETTA_UPR_001_OMG_2019.md`

Transferable principles:
- relational structures;
- mathematical constraints;
- design variables and objectives;
- sensitivities;
- matrix representations;
- feasible design spaces;
- relational transformations.

---

## 3. OMG SysML 2.0

Official:
https://www.omg.org/spec/SysML/2.0/

Use for:
- current systems-modeling language context;
- structure, behavior, requirements, interfaces, and model semantics;
- machine-readable model definitions when relevant.

Version note:
- SysML 2.0 became a formal OMG version after adoption in 2025.
- prefer 2.0 for current references unless project compatibility requires v1.x.

---

## 4. ISO/IEC/IEEE 42010:2022

Official:
https://www.iso.org/standard/74393.html

Use for:
- architecture description;
- stakeholder concerns;
- viewpoints;
- views;
- model kinds;
- architecture-description frameworks.

Diagram-design lesson:
- choose the view based on the concern;
- do not confuse an architecture with a drawing that describes one aspect of it.

---

## 5. NASA Systems Engineering Handbook

Official:
https://www.nasa.gov/reference/systems-engineering-handbook/

Use for:
- system boundary;
- interface definition;
- requirements and architecture traceability;
- interface-control discipline.

Diagram-design lesson:
- interfaces require explicit descriptions and responsibilities;
- figures must support an engineering definition, not replace it.

---

## 6. NIST IDEF0 / Function Modeling

FIPS 183:
https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub183.pdf

Recent NIST use of IDEF0:
https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957593

Use for:
- function decomposition;
- Input / Control / Output / Mechanism semantics;
- hierarchical decomposition;
- boundary-arrow correspondence.

Critical limitation:
- IDEF0 is primarily static function modeling;
- it does not itself represent dynamic time evolution.

Therefore:
```text
IDEF0
≠
state-time dynamics
```

---

## 7. Project Visual Rules

Persistent project preferences:

- white background;
- no colored panel backgrounds unless explicitly requested;
- no gradients, textures, or shadows;
- no gold unless explicitly requested;
- large, clear, directional arrows only when scientifically meaningful;
- every visual element must have a scientific or communication purpose;
- minimal publication-quality engineering style;
- preserve distinctions among physical systems, states, functions, services, controls, and outcomes.

---

## 8. Resource Selection Rule

Before a new figure is designed:

1. identify the diagram question;
2. identify which reference family governs that question;
3. retrieve only the relevant conventions;
4. create an original diagram for the project.

Examples:

| Need | Primary reference family |
|---|---|
| architecture concern/view | ISO 42010 |
| structure/behavior model | SysML |
| function transformation | IDEF0 |
| interface definition | NASA/INCOSE |
| relational transformation | ROSETTA / Math DSIG |
| project framework visualization | engineering-framework-design skill |
| state-time resilience | project mathematical evidence + domain physics |
