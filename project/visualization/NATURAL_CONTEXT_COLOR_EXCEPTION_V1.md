# Natural Context Color Exception for Scientific Visuals — V1

**Researcher authorization:** 2026-10-13. **Status:** USER-APPROVED VISUAL-GOVERNANCE RULE; pending review/integration via PR #78.
**Scope:** All thesis scientific illustrations, presentations, AI-generated equipment scenes, figures, graphics, posters and slide exports produced with Deck3/Dossiya Research Expert.
**Compatibility:** `.github/skills/deck3/references/DECK3_SRGB_PALETTE.json`; `project/visualization/AI_INFOGRAPHIC_SCIENTIFIC_REASONING_AND_PRODUCTION_PROTOCOL_V1.md`; `.github/skills/deck3/references/DECK3_SCIENTIFIC_MINIMAL_INFOGRAPHIC_STANDARD_V1.md`; existing thesis scientific and evidence hierarchy.

## 1. Official rule — verbatim approved interpretation

> **Color governance rule:** All engineered components, scientific annotations, and presentation elements must follow the approved project color system. Natural contextual elements such as vegetation, flowers, soil, sky, and other environmental features may retain restrained natural colors, provided they remain realistic, visually secondary, and do not interfere with the scientific hierarchy or interpretation of the figure.

**Short operative rule:** Natural objects may keep realistic natural colors; they must remain visually secondary and must not override scientific color hierarchy.

## 2. Exactly what is governed and what is exempt

**Governed authored design marks (13 existing sRGB tokens only):**
- headings, editable text, mathematical symbols, citations, arrows, measurement/constraint marks, data series, line/box borders, equipment-schema vector colors, icons, timelines, axes, diagrams, legends and semantic condition highlighting;
- authorship-designed panels, backgrounds and figure containers are **always white #FFFFFF**, without gradients, textures, shadows or colored fills;
- institutional headings may use approved ASU Maroon #8C1D40; ASU Gold #FFC627 remains restricted to nonessential identity accents, not data/status encoding or low-contrast type.

**Natural contextual objects (realistic natural hues permitted):**
- live plants, herbs, grass, flowers, trees, vegetation and foliage;
- soil, rocks, gravel, earth and naturally occurring surface features;
- water, physically justified sky portions and environmental weather/lighting context;
- authentic photographs **and original AI illustrative depictions** of the above, as long as the object is genuine to the relevant scene, natural colors are plausible and the visual purpose is physical context.
- Examples: green foliage; a naturally purple/pink/red flower; muted brown soil; blue water; physically relevant sky fragment. Their pixel values do **not** need to be rounded to the authored 13-token palette.

**Preserved equipment-material realism exception:** Authentic/photorealistic *equipment materials* may retain natural photographic colors (metal, insulators, charging cabinet, vehicle paint). For vector-authored schematic marks, color codes remain governed; do not recolor real equipment to fictitious status colors or present AI-rendered hardware as a verified field photograph.

## 3. Explicit limits and collision rules

1. **Context must be real to the illustration:** No random flowers, plants, red trees, ornamental shrubs or sky elements as filler for empty design space. Every natural object must have a necessary environmental or physically contextual role.
2. **White canvas remains authoritative:** A sky-colored whole-slide background, landscape photograph replacing a white panel, large color-filled nature box, gradient sunset or full-bleed environmental backdrop is NOT authorized by this exception.
3. **Natural colors cannot redefine research semantics:** Do not use an actual flower's red/purple as a critical-state data encoding or borrow a green leaf's color for unapproved research arrows/icons.
4. **Visibility and saturation:** Context remains behind and subordinate to research subjects; avoid oversaturated or numerous natural objects, hard neon greens, comic-flower patterns and dominant scenic foregrounds.
5. **Physical credibility:** Depicted natural object and its environmental state must be plausible for the scene. Do not infer a species, actual observed vegetation, geographic climate or heat damage from AI illustrative scenery; avoid fabricated wilted/damaged plants presented as experimental findings.
6. **Scientific truth:** Realistic heat/sunlight/ambient exposure is external forcing, not a proved intersystem interface or invented temperature threshold. Decorative sunrays/waves must not look like measured energy-transfer arrows.
7. **Photo vs AI attribution:** Generated equipment/environmental scenes are illustrations, not documentary evidence of TU Wien, Qatar CPC50, Bærug field sites, ASU locations or installed apparatus.
8. **Rights and citations:** Third-party photographs require appropriate usage rights and source attribution where they provide evidence; generated original contextual artwork still needs factual, physics and rights review.
9. **No widening of color authority:** This exception authorizes natural contextual *pixel colors*, not new sRGB tokens for authored figures, labels, plots, arrows, panels or branded UI.
10. **Accessibility:** Native scientific labels still require readable contrasts; natural scenery must never obscure eight-component P1–P4/T1–T4 architecture labels or arrow meanings.

## 4. Design-time decision test (Deck3 + Research Expert)

For EACH nonpalette color visible in a generated output, determine:

- Does it occur **within a physically plausible natural-context object or authentic material region**, rather than a coded annotation/graphic mark?
- Is this object **actually needed** to explain the environment, natural hazard or hardware placement?
- Is the hue **realistic, restrained, locally bounded, subordinate**, and clear of critical labels/equipment ports?
- Is it **not being used** to imply a measured phenomenon, prove causality, or communicate an unauthorized color-coded scientific status?
- Does the overall composition remain **white background and white panel interiors**?

A colored flower may PASS as naturally colored context; the same purple assigned to a research arrow FAILS. An authentic blue water body may PASS as context; a whole-slide blue sky panel FAILS.

If any fail, remove/reduce the object or separate natural image pixels from native science graphics. A source-level palette scan must evaluate native drawing styles independently of exempt natural image pixels. Do not call a generated raster palette-certified merely because every color visually resembles a token.

## 5. Infographic prompt addition (equipment scenes only)

"Use restrained realistic natural colors for any environmentally relevant live plants, herbs, flowers, trees, grass, rocks, soil or water. These objects must look physically plausible and stay small/secondary; never use decorative or artificially maroon vegetation to fit ASU branding. Keep the full backdrop and all panel areas pure white. Leave engineered schematic arrows, numbers, textual labels, citations, state/delay curves, thresholds, institutional logo and caption to separately editable PowerPoint layers. Do not invent context-specific flora, geographic claims, field observations or scientific outcomes."

**Status of existing infographic images:** This rule is prospective. Previously generated images do not become approved, editable, scientific, or rights-reviewed by virtue of this instruction. Review/redesign only when requested or before release.
