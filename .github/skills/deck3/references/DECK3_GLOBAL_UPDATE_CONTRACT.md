## Deck3-governed AI scientific image generation (mandatory)

All generated research figures, photorealistic engineering imagery, system diagrams, mathematical visualizations, poster figures and slide illustrations must follow `references/DECK3_AI_IMAGE_GENERATION_STANDARD.md` **before generation and after rendering**. First define authoritative takeaway, physical boundaries, mechanism/directional-arrow semantics, evidence/assumptions, exact 13-color authored palette and legitimate photographic exceptions, white interiors, figure geometry, and text-label requirements. Never let an image generator invent physical evidence, equations, sources or approved objectives. Evaluate generated artwork against scientific (S), human-design (H), colors/geometry (C) and image/integration (I) gates; failed/unverified figures remain PROVISIONAL and may not be certified via simple PPTX assembly. Align all downstream code, figure briefs, prompts and slide production with these requirements.

# Deck3 Global Update Contract — binding cross-skill authority

**Effective 2026-10-09.** User meaning: when the user says **"update Deck3"**, **"update Deck3 and all"**, or equivalent, the scope is the **entire Deck3 production ecosystem**, not just `deck3/SKILL.md`.

**Implementation annex and dependency registry:** `DECK3_GLOBAL_UPDATE_CONTRACT_V1.md` is the detailed technical/QA annex to this primary contract, **not a competing policy**. `DECK3_DEPENDENCY_REGISTRY.json` is the machine-readable map for updating every stage and skill. Color/source enforcement examples and the associated tests reside in `../examples/asset_color_qa.py`, `../tests/`, and linked scientific generators. A nonapproved SVG authored stroke must block assembly; raster-only images and PowerPoint rendering require explicit additional review.

## Deck3 v1.8 — scientific-mechanism traceability (binding for Deck3 outputs)

Read `.github/skills/deck3/references/DECK3_MECHANISM_TRACEABILITY_STANDARD_V1.md` (relative from repository root). Design each relevant figure to show **real components, independently defined physical/model/simulation boundaries, labeled directed interfaces, carried quantities/units or explicit OPEN, physical laws/operator status, observation/control/feedback, and state-time/service consequences**—not generic attractive boxes. Distinguish physical/electrical transport from measured data, estimates, control decisions, simulations and post-model assessments. Require independently evidenced P→T_e and T_e→P candidate mechanism gates; for T_e→P, grid-side AC behavior is a mandatory evidentiary distinction. Shared extreme heat is external forcing, not proof of interdependency. **A curved arrow is not a nonlinear equation**; two directions are two separate claims.

A scientific figure can supply a same-stem `*.trace.json` sidecar validated with Deck3 `examples/mechanism_trace_qa.py`; successful structural review does not validate the physics. Missing trace means **provisional**, and malformed/provenance-inconsistent trace blocks Deck3 image audit/assembly. Science-source checking, native-PPTX geometry, effective visual occupancy, editable object ID mapping, animation click order, exact 13-token sRGB colors and actual PowerPoint playback remain separate acceptance requirements. Keep approved slide text, real adjacent citations, full P and T_e scope, frozen GO/SO1–SO3 and white-only authored interiors unchanged. The IEEE figure supplied by the user is *design inspiration only*; do not copy its artwork or infer the paper's unverified scientific claims.

## Mandatory coverage and authority

1. **Text/writing:** source-faithful wording, editable PowerPoint text, titles, messages, 3-point content structure, references, exact frozen GO/SO1–SO3; synchronize with `dossiya-writing` as appropriate. Do not invent citations.
2. **Scientific content:** thesis scope, P and full Electrified Transportation (`T_e`) system definitions, selected model subset, external extreme heat, evidence-qualified directionality, state/function/service distinctions, timing, and explicit uncertainty. Shared heat is not evidence of coupling. T_e→P requires a grid-side AC mechanism; V2G is conditional.
3. **Figure and image generation:** scientific-infographic-design, scientific-diagram-design, mathematical-visualization-design, engineering-framework-design, image prompts, source SVG/PNG, human review of photorealistic imagery, and exact arrow meaning.
4. **Assembly/output:** Deck3 Stage 1 native text, Stage 2 independent figures, Stage 3 PPTX assembly; target 70–80% of usable region in figure-bearing slides, nominal 75% *meaningful* infographic footprint, with legitimate objective-slide exceptions; preserve source citations, notes, alt text and editability.
5. **Visual design:** canonical exact 13-token sRGB registry at `deck3/references/DECK3_SRGB_PALETTE.json`; white #FFFFFF authored canvas AND every box/panel interior; no colored panel/header fills, decorative gradients or shadows. Exact ASU Maroon and ASU Gold exemptions only; gold and bright turquoise nonessential on white. Genuine objects/photographs retain authentic real-world coloration.
6. **Runtime and QA:** relevant generators, templates, scripts, automated palette auditing, color/geometry/scientific/VVUQ checks, GitHub workflows, manifests, tests and documented example outputs. Verify rendered PPTX slides and actual image pixels/overlays before claiming certification. Saving/reopening a PPTX proves only structural validity.
7. **Governance and provenance:** update related root contributor/agent guidance, skill references and all actively maintained downstream design instructions affected by a policy change; inspect for contradictions; record scope, blockers and residual risks. Never blindly recolor scientific data plots, photographs, archived evidence or independent non-Deck3 research artifacts. Escalate any conflicting scientific authority instead of silently changing it.

## Execution protocol

- **Discover** impacted active files and downstream callers using repository tree and content search.
- **Classify** each as authoritative source, direct consumer, integration test, generated binary, third-party asset, historical record, or independent project.
- **Change** source of truth first, migrate all affected active consumers including examples/assembly scripts, update tests and CI.
- **Validate** static color/structure plus image-semantic quality and real PPTX layout. Stop certification on unresolved failed checks; explicitly distinguish verified, not run and failed.
- **Commit and merge** through a PR when requested and admissible. Merge status never means CI passed.
- **Report** exact paths/commit/PR, tested commands and results, unverified image assets, remaining exceptions.
- **Memory scope:** use this convention in future project conversations. GitHub is durable project authority; a chat reply is not an account-memory write. Memory mechanisms cannot be claimed updated unless confirmed by the product.

## Completion definition

An update is **fully applied** only when all impacted active files are synchronized, tests and visual QA genuinely pass, generated presentation assets are rebuilt when requested, and unresolved exceptions are documented. Otherwise report **partial implementation** rather than "all done."

For a text-only or single-figure request, execute that stage but still load *all* applicable cross-skill rules.
