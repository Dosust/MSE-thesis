# Deck3 AI Image Generation Authority — mandatory scientific visual release standard

**Effective:** 2026-10-09. Applies to every original or AI-generated thesis scientific image, infographic, physical-system diagram, architecture, mathematical visual, scientific poster element and slide illustration, whether standalone or destined for a PowerPoint. This standard supplements, never replaces, the `DECK3_GLOBAL_UPDATE_CONTRACT.md` and the canonical exact 13-color `DECK3_SRGB_PALETTE.json`.

## Deck3 v1.8.1 figure-media routing and fail-closed approval

**Read** `.github/skills/deck3/references/DECK3_MEDIA_ROUTING_AND_FAIL_CLOSED_IMAGE_QA_V1.md` for every Deck3 text, figures, image-generation, assemble, and release task. **A scientific diagram is not automatically an AI image.** Use equipment-centered original images only where physical objects matter; use **native editable PowerPoint** for literature/gap matrices, RQ/SO alignment, evidence-gated cross-system pathways, methodological workflows, contribution maps and chapter roadmaps. The strict no-embedded-explanatory-panels rule still applies to all images, and AI-rendered author citations are not evidence. Frozen GO/SO1–SO3 and the actual user-approved slide count must be preserved verbatim; the current 13-slide Chapter 1 baseline remains authoritative unless explicitly changed. **The prior ten AI PNG draft figures are provisional, not approved Stage 2 assets.** Do not use SVG checks, correct output dimensions, or a saved PPTX as a substitute for source review, mechanism trace, figure-only panel inspection, rendered readability, native editing and real animation playback.

## Deck3 v1.8 — scientific-mechanism traceability (binding for Deck3 outputs)

Read `.github/skills/deck3/references/DECK3_MECHANISM_TRACEABILITY_STANDARD_V1.md` (relative from repository root). Design each relevant figure to show **real components, independently defined physical/model/simulation boundaries, labeled directed interfaces, carried quantities/units or explicit OPEN, physical laws/operator status, observation/control/feedback, and state-time/service consequences**—not generic attractive boxes. Distinguish physical/electrical transport from measured data, estimates, control decisions, simulations and post-model assessments. Require independently evidenced P→T_e and T_e→P candidate mechanism gates; for T_e→P, grid-side AC behavior is a mandatory evidentiary distinction. Shared extreme heat is external forcing, not proof of interdependency. **A curved arrow is not a nonlinear equation**; two directions are two separate claims.

A scientific figure can supply a same-stem `*.trace.json` sidecar validated with Deck3 `examples/mechanism_trace_qa.py`; successful structural review does not validate the physics. Missing trace means **provisional**, and malformed/provenance-inconsistent trace blocks Deck3 image audit/assembly. Science-source checking, native-PPTX geometry, effective visual occupancy, editable object ID mapping, animation click order, exact 13-token sRGB colors and actual PowerPoint playback remain separate acceptance requirements. Keep approved slide text, real adjacent citations, full P and T_e scope, frozen GO/SO1–SO3 and white-only authored interiors unchanged. The IEEE figure supplied by the user is *design inspiration only*; do not copy its artwork or infer the paper's unverified scientific claims.

## Governing proposition

**Deck3 controls image generation before, during and after rendering.** A visually attractive image does NOT become an approved scientific figure. Treat an image generator as a rendering instrument, never as a source of scientific assertions or mechanism authority. Obtain system content and frozen wording from canonical thesis sources; never invent data, results, citations, research objectives, equations, evidence status or modeled components.

## Required image specification BEFORE generation

Record an auditable figure brief with: slide number/id, purpose and one main scientific takeaway; intended reader; canonical source/version and scientific authority; included and excluded physical objects/system boundary; state variables, mechanisms, arrow start/end and directions; evidence status for each causal claim; limits/unknowns; one-to-one label-to-object map; expected image aspect/resolution and Deck3 slot occupancy; exact approved color tokens and explicit photographic exception; meaning of every graph axis/legend symbol; and verifiable acceptance criteria. If essential scientific meaning is unresolved, do not invent a substitute.

## Scientific-mechanism review

- Identify **Power P**, full **Electrified Transportation T_e**, their physical/electrical interface, active model subset, and the supporting information/organization domains correctly for the slide scope.
- Keep *external extreme heat* distinct from physical interdependency; concurrent heat impacts on P and T_e do not prove P↔T_e propagation.
- Specify each causal arrow in text as (source, target, transferred influence or conserved quantity, direction, interface, evidence state); never infer a reverse arrow simply for symmetry.
- Separate **physical state**, **functionality**, **serviceability**, **reliability**, **resilience**, and (when within scope) **sustainability**. Distinguish physical impacts from hypothesized dynamic coupling and demonstrated effects.
- Treat T_e→P directional thermal mechanisms as *candidates* until supported by grid-side AC power/thermal state evidence. DC charging power alone is insufficient; V2G requires actual compatible equipment/operation.
- Preserve frozen GO/SO1/SO2/SO3 exactly where applicable. No invented SO4 or unsupported findings, validated guarantees, fitted coefficients or sources. Explicitly label hypotheses, conceptual links, mechanisms awaiting qualification and expected (not completed) results.

## Human-quality information and visual design

- One interpretable takeaway; only necessary information communicating mechanism, hierarchy, evidence, mathematical meaning, or relationship. No decorative collage, random icons, overly complex effects, redundant labels, meaningless arrows or AI-looking ornamental decorations.
- Entire *authored* canvas, headings, diagram panels, box interiors, legends, captions and section backgrounds must be pure white `#FFFFFF`; no colored bars/fills, tinted wash, gradient, shadow, glow or texture.
- Use only the **13 exact sRGB design tokens** from `DECK3_SRGB_PALETTE.json` for designed marks. ASU Maroon `#8C1D40` and Gold `#FFC627` are the ONLY branded exceptions to older hue bans. Gold and Bright Turquoise `#6ACEEE` must not independently encode essential information on white.
- Photographs and photorealistic engineering objects retain authentic observed real-world colors and are not palette-quantized. This exception does not allow false-color overlays, artificially tinted panels or invented equipment colors.
- Maintain large, clearly directed arrows **only** for documented scientific paths. Use high-contrast labels, direct labeling and distinguishable line patterns; color alone is not a sufficient code. Meet 4.5:1 normal text and 3:1 essential graphic contrast on white.
- Avoid text artifacts: independently inspect ALL image labels, abbreviations, mathematics, units, arrows, spelling, clipping and legibility at actual slide size. Prefer native editable PPTX labels laid over clean diagrams when image-rendered text cannot be verified.
- **Resolution:** match target format and physical slide slot; verify pixel dimensions, effective DPI under cropping and rendered legibility. Calling an image "high resolution" does not prove it stays sharp at arbitrary zoom; preserve SVG/native vectors where possible. Do not stretch or distort scientific objects.
- For figure-bearing Deck3 slides, target ~75% of usable below-header region as **meaningful actual figure area** (acceptable 70–80%, subject to approved long-objective exceptions), not a padded white screenshot or mere image bounding box.

## Four mandatory review gates

1. **Scientific (S):** scope, interfaces, mechanism and evidence qualification; accurate labels/units; no unsupported inference.
2. **Human design (H):** structure, hierarchy, visual economy, legibility, truthful photograph and object representation.
3. **Exact colors and geometry (C):** every authored mark from exact approved palette; all authored interiors white; check contrast, no prohibited fills; meaningful occupancy and correct aspect.
4. **Image and integration (I):** zoom/fit readout, source fidelity, native text accessibility, citations, notes, alt text, semantic figure-slide fit and PPTX rendering.

A figure advances from `GENERATED` to `REVIEWED` only after its gate results are recorded. If unresolved, mark `PROVISIONAL / REQUIRES_QA`. **Never** assert that an image generation tool itself verified physical mechanisms, image semantics, or full Deck3 color compliance. Regenerate/repair failed assets, then re-audit; do not simply embed the same unverified image in Stage 3.

## Required workflow and downstream propagation

**Stage 1 (text authority) → pre-render scientific figure brief → Stage 2 (independent controlled rendering) → S/H/C/I audit → Stage 3 (PPTX assembly) → actual render and final verification.** Apply this contract to scientific infographic, scientific diagram, mathematical visualization, engineering framework, reusable prompts and generators, deck3 PPTX assembly, and repository root agent instructions. An instruction to "update Deck3" triggers checking and synchronizing all impacted active consumers; historical assets and third-party photographs require review, not automatic global recoloring.

## Release record for each image

Minimum manifest: `slide_id`, `source_authority`, `takeaway`, `system_boundary`, `mechanisms`, `evidence_state`, `asset_file`, `dimensions_px`, `svg_available`, `authored_color_audit`, `white_surface_audit`, `text_label_review`, `physics_review`, `assembly_geometry_review`, `limitations`, `reviewer_status`. Preserve a reason for any waiver.
