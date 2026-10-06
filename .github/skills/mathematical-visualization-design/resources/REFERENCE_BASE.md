# Mathematical Visualization Reference Base

## Purpose

This file records transferable principles for mathematically driven visualization. It is not a license to copy source figures.

## Reference classes

### Visual and interactive complex analysis
Transferable lessons:
- mathematical functions directly generate visual output;
- visual changes should be controlled by model variables;
- parameter changes should trigger recomputation rather than cosmetic animation;
- domain/state mappings can be encoded through geometry and color;
- interaction should expose mathematical structure.

Use for:
- model-to-visual encoding;
- parameter interaction;
- dynamic scientific computing;
- mathematical animation.

Do not copy:
- distinctive page layouts;
- source-specific artwork;
- copyrighted diagrams.

### Scientific computing / dynamic visualization
Transferable lessons:
- separate model, solver, encoding, renderer, and interaction;
- prefer deterministic visual states;
- make temporal evolution traceable to simulation time;
- expose thresholds and invariants visually.

### Systems engineering diagrams
Transferable lessons:
- boundary, interface, state, service, control, and arrow semantics remain authoritative;
- mathematical visualization does not replace systems-engineering semantics.

## Project integration

Use jointly with:
- `../SKILL.md`;
- `../../engineering-framework-design/SKILL.md`;
- `../../scientific-diagram-design/SKILL.md`.

## Permanent project rule

[
oxed{
	ext{Scientific diagram}
=
	ext{formal model}
+
	ext{declared visual encoding}
+
	ext{verified rendering}
}
]

A visual effect without a mathematical or scientific mapping is decoration and should be removed.
