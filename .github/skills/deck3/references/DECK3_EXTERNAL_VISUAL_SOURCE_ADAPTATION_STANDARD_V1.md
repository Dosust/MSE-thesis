# Deck3 — External Scientific Visual Sourcing and Adaptation Standard V1
**Status:** Binding design/sourcing gate for Deck3 All Forms, Dossiya Research Expert when authoring Deck3, scientific infographic, AI imagery, native PPTX, assembly, animation and release QA.
**Authority:** Subordinate to thesis scientific authorities, exact frozen objectives, active 14-slide user-supplied chapter-1 source (13 content + articles-only References), canonical 13-color Deck3 palette, mechanism traceability, and figure-media fail-closed QA. Does not grant copyright permission or scientific validation.

## Governing principles
1. External images and diagrams can **ground** structure, realism and scientific interpretation; do **not** copy a figure into the final deck unless exact reuse rights are verified. Distinguish independently developed scientific concepts from copyrightable illustration expression.
2. Every visual item must communicate the slide's single scientific message: component, physical mechanism, interface, boundary, quantity, evidence relationship, research stage or service consequence.
3. AI may create *new* equipment visuals; it cannot determine the feeder topology, equipment ratings, physical control volumes, causal direction, validated parameters, mathematical laws, evidence strength or numerical results.
4. Prefer **source-grounded redraws** for mechanisms, architecture, thermal diagrams, evidence synthesis, control-volume figures and workflows. Use original/authorized physical photos for real equipment only when they improve physical comprehension. Keep scientific labels, arrows, equations, citations and animation targets native/editable wherever possible.
5. Maintain all authored backgrounds/panels white; read exact `DECK3_SRGB_PALETTE.json` at runtime; only its 13 named sRGB colors for authored marks. Authentic object colors in photographs remain exempt. No colored surface fills, shadows, textures, gradients or decorative connections.
6. Every published factual claim needs accurate adjacent author–year citation. For adapted visuals credit the actual source in editable figure caption/notes. The terminal reference slide holds **journal articles only**, per current user baseline; benchmark documentation and image license attribution remain in slide notes/provenance unless a distinct source-credits artifact is authorized.

## Four source statuses — mandatory
- `REFERENCE_ONLY`: original material informs technical analysis; do not display the source figure.
- `ADAPTED_REDRAWN`: derive scientific structure/relationship and produce a substantially original thesis-specific drawing. Cite the real source; inspect possible licensing/derivative-right issues if recognizable expressive elements persist.
- `DIRECT_REUSE_LICENSED`: embed original only with explicit verified license/permission, terms and attribution. A citation alone is NOT reuse permission.
- `INSPIRATION_ONLY`: derive generic compositional inspiration; AI visual must be independently composed, meaningfully distinct and scientifically audited.
- `BLOCKED_RIGHTS` or `BLOCKED_SCIENCE`: do not publish.

## Required source record per asset
Register: slide ID; central scientific message; source URL/DOI and title/creator; source type; access date; original figure identifier; source claim; source media rights and evidence/permission URL; usage status; adaptation transformation notes; physical equipment/ports/boundaries; each arrow with source, destination, meaning, quantity/units and evidence status; eligible citations; exact palette QA; pixel/geometry QA; editable element IDs; animation sequence; independent visual reviewer; status PASS/FAIL/OPEN/NOT_RUN.
Use a human-readable ledger and a machine-readable sidecar when supported. Mechanism sidecars `<figure_stem>.trace.json` are still required by established Deck3 standards; do not substitute this source register for physical traceability.

## Sourcing→publication pipeline (fail closed)
1. **Select** academically/technically credible original source for a specific mechanism or equipment depiction; avoid scraped or unattributed reuploads.
2. **Extract** source-supported physical and observational information; separate facts from conjectures and visual style.
3. **Decide** one of the source statuses above; obtain permission for direct reproduction or choose an original redesign.
4. **Compose** thesis-specific visual: physical objects and measurement/control interfaces first, only meaningful directional arrows, minimal exact labels, no prose panels inside image.
5. **Integrate** independently editable slide text, citations, arrows, equations, boundaries and speaker notes. Avoid flattened AI-text infographics.
6. **Animate** to reveal scientific reasoning: system boundary→physical mechanism→measured interface→state/time→conditional service consequences, as appropriate; click-to-reveal with persistent previous content. Avoid decorative motion.
7. **Verify** rights/provenance, physics, source semantics, citations, palette, 40-entry inventory dispositions, slide text fidelity, no overlap, projection readability, correct native animation targets and actual desktop PowerPoint playback. Report NOT_RUN for unperformed tests.

## Slide routing — current 14-slide Chapter 1
| Slide | Visual source | Recommended final construction | Meaningful reveal |
| --- | --- | --- | --- |
| 1 | None | Native title text | None |
| 2 | None | Native outline | None |
| 3 Engineering background | Licensed photo or independent AI illustrations of transformer, EVSE and vehicle; feeder source | Hybrid equipment imagery + editable AC interface and complete P/T_e boundaries | P→AC interface→T_e |
| 4 Extreme heat | Thermal principles, equipment studies | Redrawn separate control volumes under common external forcing | heat→P response→T_e response |
| 5 Research problem | Prior thermal/load studies for evidence, not copied figure | Original dual **candidate** P→T_e and T_e→P mechanisms, real AC variables | physical setup→direction 1→direction 2→open consequence |
| 6 Existing knowledge | Verifiable article findings | Native evidence-synthesis categories → open research need; no article diagram copied | established findings→research opportunity |
| 7 Research questions | No external figure needed | Native RQ1→RQ2→RQ3 | ordered stages |
| 8 Objectives | Canonical frozen text | Native hierarchy; exact GO/SO wording retained | SO1→SO2→SO3 |
| 9 System/interface | IEEE feeder documentation with separate provenance; physical images | Native full P and T_e boundaries, reduced XFM1–AC–EVSE–vehicle subsystem | full systems→active subset→measurement plane |
| 10 Mathematical model | Textbook thermodynamics and peer-reviewed component balance | Original control-volume diagram + true editable equations; do not imply calibrated model | control volume→inputs/losses→state law |
| 11 Methodology | Verified benchmark documentation | Native B0→B1→thermal qualification→IEEE123→services and QA gates | stage by stage |
| 12 Resilience/sustainability | Source-supported service evidence | Original two-pathway assessment, environmental/economic/social separately | direct→responses→outcomes |
| 13 | None | Native organization and priorities | None |
| 14 | Verified journal-article bibliography | Articles-only references slide | None |

## Component and mechanism integrity
- The full 40-entry register has 19 P and 21 T_e records; not all are installed devices or unique state variables. Every entry needs a disposition (active device, equivalent aggregate, environmental boundary, control/observation, conditional capability or service).
- In Slide 5, a transformer thermal limit does NOT necessarily cause supply curtailment; show conditional control/protection. EVSE derating may REDUCE transformer losses; never imply guaranteed worsening. For T_e→P carry actual **grid-side AC** V/I/P/Q, not vehicle battery-side DC output.
- External heat is common forcing, not proof of mutual thermal causality. Time and physical-state distinction remain explicit.
- No fictional simulation curves, invented measurements, copied IEEE figure artwork, pseudo-validations or invented evidence.

## Release gate
A visual is `APPROVED_FOR_DECK` only if copyright/license status, scientific mechanisms, palette, source citations, physical-port trace, no image-only narrative panels, rendered readability and editable/animation target audit pass. PPTX saved ≠ playback verified. A blocked or unreviewed visual is `PROVISIONAL`; do not quietly substitute it for a validated asset.

## Conflict resolution
This standard adds external-source governance; it does **not** replace the research-authority index, `DECK3_MECHANISM_TRACEABILITY_STANDARD_V1.md`, `DECK3_MEDIA_ROUTING_AND_FAIL_CLOSED_IMAGE_QA_V1.md`, `DECK3_AI_IMAGE_GENERATION_STANDARD.md`, color palette, or frozen objective text. User-approved 14-slide version supersedes older default-13-slide rule *for this presentation only*; no additional infographic on slides 1, 2, 13 or 14.
