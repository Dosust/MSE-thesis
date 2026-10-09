---
name: procedural-mathematical-art
description: Optional educational techniques for independently defined shader coordinate transforms, seeded tilings, analytic distributions, and labeled synthetic animation; never infer thesis physics, stochastic calibration, or causal interfaces from procedural output.
license: MIT
metadata:
  version: "1.0.0"
  deck3_compatibility: ">=1.6.0,<2.0.0"
---

# Procedural Mathematical Art — teaching method only

Use only for a direct request to learn GLSL/coordinate mathematics, or when an already-authorized mathematical figure benefits from procedural local geometry. Do not activate automatically for research claims, physical framework illustrations, charts of measured quantities, scientific diagrams or Deck3 slide creation. This skill is a **rendering/educational helper**, not a scientific authority.

Read the [cross-skill router](../scientific-visual-orchestration/SKILL.md) and [Chapter 10 mathematical transfer](../scientific-visual-orchestration/references/CHAPTER_10_TRANSFER.md). Original reference code in the independent mathematics-art repository is a source to learn from, **not** a mandatory graphics dependency.

## Seven-stage lesson and verification procedure

1. Pixel coordinates and GLSL fragment semantics: normalized, aspect-correct coordinates; clearly separate display pixels from physical coordinates and units.
2. `floor`, `fract`, sine-based deterministic transforms: calculate negative-coordinate behavior and continuity/discontinuity explicitly; check finite inputs.
3. Power transform: assume `U~Uniform(0,1)` *only when explicitly true*; derive CDF/density/mean, then test monotonicity and endpoints.
4. 2D cell hashing: seed recorded, algorithm versioned, collision/dependence acknowledged, CPU/GPU precision difference documented.
5. Tiled geometry: explicit glyph paths, row/column cell indexing and reproducible static fallback. Never infer a causal or physical network.
6. Time-indexed motion: derive displacement by integrating velocity where velocity is intended; distinguish synthetic display parameter from physical time, and include pause/seek/reset/reduced motion.
7. Optional smooth value interpolation: mathematically define the interpolation and check boundaries; **not** a calibrated spatial covariance or physically modeled heat field.

For each requested output record: learning objective, function and input domain, exact mathematical statement, GLSL/CPU reference, coordinate transform, seed, relative/absolute tolerance, test cases (including invalid and negative inputs), color-token remapping to Deck3 13-color palette, accessibility/static alternative, and evidence/provenance status.

### Supported output types

- **Animation:** only motion justified by stated `x(t)` or `F_t(x)`, with controls/fallback.
- **Diagram:** geometry may help layout; nodes and edge meanings must be sourced from diagram/framework skills. No random causal arrows.
- **Mind map:** stable deterministic positioning only; conceptual hierarchy is authored.
- **Chart:** genuine measurements or declared analytical/synthetic values with units; never random hash as data.
- **Mathematical figure:** original vector paths and derivations with exceptions and properties checked.

**Stop** if visual noise would be mistaken for observed temperature, outage likelihood, traffic behavior, recovery or sustainability benefit. The mathematical art is not a physical demonstration. The MSE thesis' heat/P/T_e scope and frozen equations remain authoritative. Under Deck3, this skill never mutates Stage-1 copy, objectives, figure occupancy contract, or color registry.

### QA and release

Read [routing acceptance gates](../scientific-visual-orchestration/references/ACCEPTANCE_MATRIX.md). Report separate statuses for code tests, mathematical correctness, shader pixel equivalence, browser playback, PowerPoint playback, communication evaluation and physical validation. Only certify a status when that specific verification was actually completed. The Book of Shaders Chapter 10 is a conceptual educational reference; do not reproduce extensive copyrighted source or graphics.
