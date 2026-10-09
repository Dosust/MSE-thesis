---
name: deck3
description: Orchestrate a rigorous three-stage scientific PowerPoint workflow with a dominant scientific infographic occupying approximately 75 percent (acceptable 70–80 percent) of the usable content region on every eligible figure-bearing slide, while preserving accurate scientific claims, editable approved text, citations, exact frozen objectives, notes, and physical system boundaries. Activate for Deck3 text, figures, assemble, all, or one-slide commands.
license: MIT
metadata:
  version: "1.8.0"
  short_name: "Deck3"
---

## Mechanism-centered infographic engineering — v1.8.0 (binding across ALL Deck3 stages)

**Read `references/DECK3_MECHANISM_TRACEABILITY_STANDARD_V1.md`** before any figure brief, image prompt, math diagram, native-PowerPoint visual, animation, or final figure approval. Core design principle: **a diagram explains components, physical/model boundaries, interfaces, quantities, laws/operators, measurements, control, feedback, and service consequences—not merely a taxonomy of colored boxes**. Adapt to the slide purpose; do not force irrelevant layers.

- **Stage 1 / writing:** identify the scientific takeaway, which system/model boundary is being described, which quantities and assumptions the text establishes and any unresolved evidence gate. Do not rewrite approved slide copy or expose editorial headings.
- **Stage 2 / figures / AI images:** for every engineering connector give source, destination, directed relation *type*, carried quantity/units (or explicitly OPEN), interface/physical law if admitted, and evidence status. Separate physical electrical flows from sensor data, signals, model calculation, decision/optimization, and reporting flows. Physical P and full T_e are distinct from simulation/active-model and post-model assessment boundaries.
- **Mechanism sidecar:** write `<figure_stem>.trace.json` against `examples/mechanism_trace_qa.py` / `examples/mechanism_trace_example.json`; human source qualification stays mandatory. The 8-object sample is **conceptual**, not equipment evidence. A malformed sidecar blocks Stage 2/3; missing sidecars remain `TRACE_NOT_REGISTERED_PROVISIONAL` (older decks may assemble for review but cannot claim certified physics).
- **Stage 3 / assembly:** check trace status, approved exact 13-token palette, native text and notes, source/citation consistency, arrow-to-object identity, meaningful content occupancy and actual slide readability. PPTX shape/animation targets must match recorded object IDs where actual independent layers exist.
- **Animation:** when appropriate reveal physical boundaries → named interfaces/quantities → forcing and state-time → observation/control/feedback → evidence and service consequences, with `Appear` / presenter `On Click`, persistent prior content. Each step must remain scientifically interpretable *even before the next click*. Use progressive-slide fallback when native effects cannot be verified.
- **Never claim** physical nonlinearity from a curved arrow, empirical causality from a bidirectional diagram, validation from code passing, or scientific certification from SVG/PNG generation. The IEEE 2024 screenshot supplied by the user is design inspiration, **not** proof or permission to reproduce copyrighted material.

**Independent mechanism gate M** supplements current S/H/C/I (scientific image) and S/W/C/F/A/Q (Deck3 release) gates. An automated `STRUCTURAL_TRACE_PASS_NOT_PHYSICS_VERIFIED` is neither source-content verification nor field validation nor Microsoft PowerPoint playback certification.

## Native PPTX authored-color preflight — v1.7.1

**Binding gate on every editable text deck and assembled deck:** run `examples/pptx_color_qa.py` against the actual PPTX XML. Reject off-palette explicit `a:srgbClr` on slide shapes, unresolved `a:schemeClr`, nonwhite slide backgrounds and authored slide gradients/shadows/patterns. Stage 3 `examples/deck3.py` must now block off-palette Stage 1 native slide text BEFORE inserting otherwise compliant figures, and recheck the final PPTX after saving. This corrects the case where SVG figures passed the 13-color source check but a legacy slide's editable title/body/citations still used off-palette colors. The checker does not certify raster pixels, unrendered theme masters, scientific relations, meaningful 70–80% occupancy or Microsoft PowerPoint animation playback.

**Migration:** preserve every source string and speaker note, map old authored colors **by verified semantic role**, never by visually nearest color; create a new version rather than overwriting approved source files. Historical decks remain PROVISIONAL until source and actual assembly checks pass. In addition to this gate, apply the v1.7 AI scientific image generation S/H/C/I policy unchanged.

## Deck3-governed AI scientific image generation (mandatory)

All generated research figures, photorealistic engineering imagery, system diagrams, mathematical visualizations, poster figures and slide illustrations must follow `references/DECK3_AI_IMAGE_GENERATION_STANDARD.md` **before generation and after rendering**. First define authoritative takeaway, physical boundaries, mechanism/directional-arrow semantics, evidence/assumptions, exact 13-color authored palette and legitimate photographic exceptions, white interiors, figure geometry, and text-label requirements. Never let an image generator invent physical evidence, equations, sources or approved objectives. Evaluate generated artwork against scientific (S), human-design (H), colors/geometry (C) and image/integration (I) gates; failed/unverified figures remain PROVISIONAL and may not be certified via simple PPTX assembly. Align all downstream code, figure briefs, prompts and slide production with these requirements.


## Deck3 global-update scope (binding)

When the user requests **"update Deck3"** or equivalent, apply the **entire linked design/production ecosystem**, not this skill in isolation. Read `references/DECK3_GLOBAL_UPDATE_CONTRACT.md` and the canonical `deck3/references/DECK3_SRGB_PALETTE.json` (relative to .github/skills). Synchronize source-faithful text and writing, independently generated scientific figures/images, photorealistic asset prompts, code/templates, PPTX assembly, slide geometry, white-only surfaces, exactly 13 authored sRGB tokens, scientific evidence/citation/arrow QA, regression tests, release checks and any impacted root instructions. Archive and natural photographic pixels are preserved. Never claim completed certification from PPTX-open success or from an unexecuted/failing GitHub workflow. If not fully validated, label the result provisional. **Required technical annex:** also load `references/DECK3_GLOBAL_UPDATE_CONTRACT_V1.md` and `references/DECK3_DEPENDENCY_REGISTRY.json`. Audit every registered route, marking REVIEWED_NO_CHANGE when unaffected. Regenerate changed source assets, update compilers/assemblers and tests, and report unrun checks. The Stage 2/3 CLI now preflights accompanying SVG colors using `examples/asset_color_qa.py`: any unauthorized vector color blocks; PNG-only scientific diagrams are COLOR_NOT_VERIFIED_RASTER_ONLY, never certified. Authentic photographs require explicit separate review.


# Deck3 — Scientific Thesis Slide Production

**Short invocation:** `Deck3` (case-insensitive in conversational requests).  
**One-command aliases:** `Deck3 text`, `Deck3 figures`, `Deck3 assemble`, `Deck3 all`.

This is a **dispatcher and end-to-end production skill**. It calls existing authoritative skills; it does not replace the repository's engineering physics, scientific evidence, or mathematical visual semantics.

## 0. The invocation contract

| Say this | Stage | Deliverable | No changes to |
|---|---|---|---|
| **Deck3 text** | **1** | A fully editable 16:9 text-only PPTX with a **genuinely empty, dominant figure region targeting 75% of usable content area** on eligible visual slides; approved copy, notes and citations | Frozen scientific text and objectives |
| **Deck3 figures** | **2** | Separate, scientifically qualified **image-free-of-slide-text** illustration assets designed for the dominant 75% region, with readability/provenance QA | Stage-1 PPTX text, master layout |
| **Deck3 figures slide 6** | **2 / selective** | Only Slide 6 standalone infographic; preserve all other illustrations unchanged | All other files |
| **Deck3 assemble** | **3** | Insert admitted assets into Stage-1 dominant regions **without distortion**; validate rendered occupancy and readability; preserve all approved text, citations and notes | Source figures and approved copy |
| **Deck3 all** | **1 → 2 → 3** | Text deck → scientific figures → final assembled PPTX + QA + previews | Entire frozen governance |

Other accepted commands: `Deck3 1`, `Deck3 2`, `Deck3 3`, `Deck3 slide 9`, `Deck3 QA`. A request naming one stage must **not** silently execute unrelated stages or revise frozen data.

If the user has already supplied approved text or completed stage artifacts, **reuse them** rather than making up a new outline. Do not automatically overwrite an accepted figure, approved baseline, or previous final deck. Establish all input/output paths from actual user-provided files or successful tool creation; never infer sandbox paths from filenames.

## 1. Binding source-of-truth order

1. `AI_RESEARCH_INSTRUCTIONS.md`
2. `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`
3. `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`
4. `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md`
5. Active frozen title, system-composition, thermal scope, state-time, resilience, sustainability and objectives documents.
6. `.github/skills/engineering-framework-design/SKILL.md`
7. `.github/skills/scientific-diagram-design/SKILL.md`
8. `.github/skills/scientific-infographic-design/SKILL.md` and reference library/storyboard.
9. `.github/skills/mathematical-visualization-design/SKILL.md` when equations, data, trajectories or code-generated plots appear.

**Absolute:** scientific citations adjacent to supported claims **on the slide** and beside evidence-bearing figure claims (APA author–date); internal frozen definitions attributed to canonical files. No arbitrary DOI, parameters, temperatures, thermal curves, or validated bidirectionality. Scope is Power P + *full* Electrified Transportation T_e, heat-conditioned directional mechanisms only; EVSE is a component of T_e, not a third infrastructure. A reduced active model never silently redefines T_e.

## 1A. AUDIENCE COPY RULE — 2026-10-09

**The presentation should display scientific content, not the names of fields in the authoring template.** On all title/outline/content/reference slides, never render the literal metadata headings `MAIN MESSAGE`, `THREE KEY POINTS`, `MAIN IDEA`, or `3 BULLETS`. Keep the actual `message` text and meaningful `bullets` visible, editable, sourced and unchanged unless a separate copy revision is explicitly authorized. The manifest may continue to use one message plus three points as invisible authoring structure; the audience must not see that structure's generic labels. Real semantic headings such as `General Objective`, `Specific Objectives`, `System Boundary` and `References` are allowed.

**Use the 2026-10-09 comparative audit before the next Chapter 1 design pass:** `references/CHAPTER1_COMPARATIVE_DESIGN_LESSONS_2026-10-09.md`. Preserve strong ASU typography/evidence, restrained scientific figures, clear bidirectional-evidence gates, and ensure figures actually occupy the current §2A dominant visual target. Do not claim a legacy small-image layout satisfies 75%.

## 1B. COMPARATIVE DESIGN LESSONS — enforceable acceptance contract

**Source and limits:** The Chapter 1 comparison assigns editorial A=88/100 (ASU text-first), B=85/100 (Expert complete illustration), C=81/100 (Dossiya provisional, one required illustration missing). These grades are reviewer judgments, not psychometric measures or independent experimental evidence. A is the wording/typographic baseline, B the restrained mechanism/traceability baseline, and C an evidence-gate and mechanistic-detail reference, **not** a template for dense labels or icons. Apply the principles to other decks only when appropriate to their evidence and scientific scope.

### Gate W — audience wording and hierarchy
1. Place a **claim-bearing scientific takeaway immediately below the slide title**. Use the best approved wording, not the shortest possible claim; a headline may state the scientific result/question, but cannot assert an unverified result.
2. Treat `message` and `bullets` as **authoring fields**, not audience labels. Never display `MAIN MESSAGE`, `THREE KEY POINTS`, or similarly repetitive editorial metadata. Retain meaningful `General Objective`, `Specific Objectives`, `System Boundary`, and `References` headings.
3. Use native editable PowerPoint text for title/takeaway/supporting points and visible same-slide citations. Avoid duplicating full research questions, frozen objectives or supporting bullets inside a graphic.
4. Preserve the **complete and exact** approved objective wording and notes. Prefer a text-led objectives slide or approved companion over a miniature diagram or reduced font. Any wording reconciliation between A/B/C needs explicit approval.

### Gate F — figure semantics and visual economy
1. Choose **one question answered by each figure** and register each node, boundary, variable, causal arrow, arrow direction, label and citation. A visual item without a scientific/communication function is removed.
2. Separate full system boundary from the simulated subset; identify distinct P and T_e boundaries. Do not replace the full T_e composition with EVSE/charging alone.
3. For extreme heat, draw **two independent external-forcing pathways** unless a directional physical mechanism is explicitly qualified. Shared exposure/co-location is not evidence of cross-system causation.
4. Qualify P→T_e and T_e→P **independently**. A candidate T_e→P charging mechanism must connect thermal behavior to **grid-side AC input** before claiming a Power System consequence; DC-side output or a drawn arrow is insufficient.
5. Distinguish thermal physical state, functional capability, actual flow/power, critical service, resilience outcomes and sustainability conclusions. For sustainability, distinguish direct effects from effects mediated by intervention; neither is automatically demonstrated by resilience outputs.
6. Make verification, calibration, validation and uncertainty **distinct**. Present proposed SO→output mappings as proposed work, not achieved validated results.
7. Enlarge mechanism diagrams and readable labels instead of multiplying symbols, annotations, decorative icons or text. Large directional arrows must carry defined scientific meaning. White slide and white panel interiors remain mandatory.

### Gate L — layout and publication quality
1. On eligible figure slides use §2A's **75% effective meaningful visual area target** (70–80% acceptance range), with a concise supporting text rail. Do not score a large white PNG as meaningful visual area.
2. Check **figure font sizes, equation readability, arrowheads, reference text, overlap and clipping at actual slide size and thumbnail/projection scale**. If a 20–30% text rail cannot hold frozen wording, document a text-led exception or obtain approval for a companion slide.
3. Apply one coherent academic typography hierarchy: a substantial title; direct scientific takeaway; readable supporting points; visible source notes. Maintain full, readable bibliography entries across as many reference slides as required; separate **external scholarly/technical standards** from **internal thesis authorities**.
4. For the 16-slide Chapter 1 baseline, require **11 of 11 independently authored figures on slides 3–13**, with no silent asset substitution; missing Slide 13 chapter-sequence figure is a release blocker. For other decks derive the expected count from the manifest, never assume 11 universally.

### Gate Q — evidence, completeness and honest release claims
- Before Stage 1 freeze, compare the selected wording to the approved source and record frozen-string digests; check slide-by-slide against the audit in `references/CHAPTER1_COMPARATIVE_DESIGN_LESSONS_2026-10-09.md`.
- Before Stage 2 admission, verify direction, physics, model-versus-system membership, source proximity, candidate/verified status and actual minimum visual legibility for each asset.
- Before Stage 3 release, assert all required images exist, text/notes/citations are unchanged, image aspect ratios preserved, no authoring labels leaked, references complete, and **actual rendered visual occupancy** independently inspected. Report `geometry_share` and `effective_meaningful_visual_share` separately.
- **A saved PPTX, correct picture count, aspect ratio, static unit tests, or 75% image rectangle never establishes scientific validation or full visual certification.** Mark such outputs `TECHNICAL_ONLY / PROVISIONAL` until a documented final-slide inspection and evidence review pass.
- Explicitly distinguish changes to the skill, changes to the generator, generated decks and **certified** decks. Never imply an older deck was retroactively updated or certified.

## 1C–1D. Binding Deck3 v1.6 approved-color policy and exact sRGB registry

The sole authoritative **13-color authored design palette** is `references/DECK3_SRGB_PALETTE.json` (8-bit sRGB). These tokens apply to all slides, diagrams, figures, charts, legends, headings, borders, SVGs and authored presentation graphics. No approximate colors or unsanctioned substitutes.

| Token | HEX | RGB | Design role |
|---|---|---|---|
| ASU Maroon | `#8C1D40` | (140,29,64) | Primary headings and institutional identity |
| ASU Gold | `#FFC627` | (255,198,39) | Small *nonessential* institutional accents; never body text |
| Black | `#000000` | (0,0,0) | Body text, mathematical equations and axes |
| White | `#FFFFFF` | (255,255,255) | ALL authored backgrounds and box/panel interiors |
| Deep Navy | `#12304A` | (18,48,74) | Technical headings and boundaries |
| Technical Blue | `#0072B2` | (0,114,178) | Power-system annotations |
| Slate Blue | `#416985` | (65,105,133) | Secondary curves and technical distinctions |
| Deep Teal | `#006D70` | (0,109,112) | Evidence-qualified cross-system interfaces |
| Cyan-Blue | `#087E98` | (8,126,152) | Information/observation |
| Forest Green | `#176B42` | (23,107,66) | Transportation and mobility services |
| Deep Red | `#B4232C` | (180,35,44) | Critical states/constraints |
| Graphite | `#555D66` | (85,93,102) | Secondary labels, axes and source notes |
| Bright Turquoise | `#6ACEEE` | (106,206,238) | Optional *nonessential*, sufficiently large accents, never critical text/lines on white |

**Priority and explicit exceptions.** Exact ASU Maroon (`#8C1D40`) and exact ASU Gold (`#FFC627`) are now intentional branded exceptions to the older generic bans. All *other* purple/violet/pink/magenta and yellow/gold authored design colors remain prohibited. Only the 13 registered HEX/RGB codes may be chosen for authored design marks.

**White surfaces.** Entire slide, section/panel/quadrant/box/legend interior, figure canvas and title area must be pure `#FFFFFF`; no filled colored header strips, colored panel backgrounds, tinted whites, gradients, shadows, decorative texture or colored overlays. Semantic tokens are for purposeful headings, text, borders, chart lines, large meaningful arrows, labels and small accents—not filled panel interiors.

**Visibility gate.** WCAG-style contrast is evaluated against white. Standard text >=4.5:1; nontext essential information >=3:1. Gold and Bright Turquoise are **below required contrast against white** and therefore may not independently encode essential data, thin arrows, boundaries or meaningful text. Support them with high-contrast labels/lines; otherwise omit them. Don't conflate contrast-to-white with pairwise chart-series distinguishability. Add distinct markers, line patterns and direct labeling.

**Authentic imagery.** Realistic photographs and photorealistic physical objects preserve their real observed colors, whether or not present in the 13-color authored-design registry. Do not recolor nature, skin, infrastructure or equipment to obey the annotation palette. Never permit an artificial tinted photo background, posterization or decorative glow under this exception.

**QA and code.** Code generators read exact codes from the JSON; no RGB approximations or library auto-palettes. Audit authored vector/shape/chart styling separately from genuine photograph pixels; automated global photographic pixel rejection is invalid. An ASU template's geometry and type hierarchy may be adopted but colors must be remapped to this registry. Scientific mechanism labels and frozen thesis authority override visual styling. The requirements govern Stage 1, standalone Stage 2 and Stage 3 assembly.

## 1E. Advanced PowerPoint engineering and animation — installed extension

The advanced (source-grounded) implementation specification is `advanced_powerpoint/SKILL.md`, with modules `advanced_powerpoint/references/`, a machine-readable example in `advanced_powerpoint/examples/`, a deterministic geometry/manifest checker, and CI regression tests.

**Use when requested:** `Deck3 native-shapes`, `Deck3 vector-icons`, `Deck3 curved-arrows`, `Deck3 math`, `Deck3 animate`, `Deck3 morph`, `Deck3 chart`, `Deck3 accessibility`, `Deck3 playback-QA`, `Deck3 export`, or `Deck3 advanced all`. These are *design and capability routes*, not blanket claims of implemented production backends. Before asserting any generated native animation or 3D capability, actually build, import and test it.

**Authority:** Every generated or animated shape MUST obey the exact `references/DECK3_SRGB_PALETTE.json` 13-token 8-bit sRGB source of truth (current policy v1.6); all authored canvases/boxes/legends/headers are white. The extension cannot authorize any new color, background fill, thermal causal arrow, model parameter, result, objective, or unverified source. Never duplicate the palette in code. Preserve approved slide text/citations/notes and exact frozen research objectives; presenter-controlled `Appear / OnClick` remains the default requested mode, with no automatic timing, no disappearing prior steps and a progressive-slide fallback. Follow evidence + arrow semantics, accessibility, aspect-ratio and effective figure occupancy gates in this core skill.

**Release distinctions:** `SPECIFIED` and `STRUCTURAL_TEST_PASS` are not `POWERPOINT_PLAYBACK_VERIFIED` or `PHYSICALLY_VALIDATED`. The advanced Python example validates registries and geometry only. Native effects and actual desktop playback require their own evidence. Current 3-stage Deck3 commands remain unchanged unless the user requests an advanced stage.

## 2. The slide architecture (text versus illustration)

- **Slide text stays in native PowerPoint text shapes:** title, **one unlabeled scientific statement**, **exactly three concise supporting points with no visible metaheading** on substantive slides, in-text source/footer, slide number, and detailed notes. An approved frozen objective requiring long text remains **verbatim**, not abbreviated to force layout.
- **Standalone figure asset:** a scientific mechanism, boundary, research comparison, or method figure inserted into a **dominant dedicated region**. It is not a screenshot or mockup of the whole slide, and it must not repeat the slide title, main message, or three points.
- **Reserved visual space:** pure white, truly blank; no gray rectangle, text saying `PLACEHOLDER`, decorative dashed outline, or filler symbol in the delivered text stage.
- **Graphics belong only where they improve comprehension.** Title, outline and references may remain text-only. For active 16-slide Chapter 1, designated figure slots default to Slides **3–13**; Slide 2 has no compulsory figure.
- **Typography:** Times New Roman on editable slide text; use Times New Roman wherever figure text is generated deterministically (SVG/TikZ). If unavailable, preserve the declared name and disclose visual font substitution.
- **Visual:** white canvas/boxes only; black readable text, restrained semantic color on borders/large arrows/small accents. No gold unless explicitly requested, no panel fills, glows, gradients, shadows, gray/colored cards, or ornament.
- **Arrow and status register:** each scientific arrow states source, target, physical transfer/cause/control, citation and `ESTABLISHED`/`THESIS-DEFINED`/`CANDIDATE`/`OPEN`. The drawn line style denotes **relationship**, never unverified status. Never add user-facing badges like `CANDIDATE—not case-qualified` if the user asked to omit presenter-only warnings; retain the qualifying semantics in QA/notes and never imply validation in the visual.
- **Responsive figure fitting:** retain source aspect ratio, contain/center inside the dominant reserved slot, never distort or crop essential evidence to hit an arbitrary quota. Prefer a source figure with the correct final aspect ratio and minimal internal blank margins. High-resolution PNG for reliable PPTX rendering; retain SVG/editable source when available.

## 2A. MANDATORY 75% SCIENTIFIC FIGURE DOMINANCE — 2026-10-09

**User-directed layout contract.** For each eligible **figure-bearing** content slide, a meaningful scientific infographic/diagram/chart/framework must be the dominant communication object, targeting **75% of usable slide content area** (default acceptance band **70–80%**). This overrides the legacy small right-side illustration convention but **does not** override exact frozen research wording, evidence truthfulness, citation visibility or source readability.

### Define the denominator correctly

- **Usable content region (U):** the slide rectangle within agreed horizontal margins **below the native slide title/main-message header and above the citation/footer strip**. Define and save its numeric [x, y, width, height] in the manifest or QA report. The title, slide number, outer margins, fixed header and reference-footer areas are **excluded**.
- **Actual visual region (V):** the rectangular visible bounds of the **meaningful infographic** as placed on the slide, clipped to U. A mostly white graphic with a tiny object at its center must **not** receive full-area credit; measure/visually inspect its **effective occupied graphic content**, not just a blank PNG canvas.
- **Coverage:** visual_share = area(V ∩ U)/area(U); aim for **0.75** and accept **0.70–0.80** only if physical readability, citation preservation and text accuracy pass. Record actual achieved fraction, not only reserved slot fraction.
- **Text budget:** supporting main-message text, native editable bullets, captions and other content use the remaining approximately **20–30%**. The visual dominates; **scientific relationships, evidence, service meanings and necessary numerical labels may reside inside the figure** without copying the whole slide's native text.
- **Exceptions:** title, outline, reference slides, and explicitly text-only slides have no 75% requirement. Dense exact-wording objectives or evidence tables may require a separate text-only companion or approved slide split rather than illegible content or an inaccurate figure. Record reason, approved layout and figure occupancy. **No fabricated filler or forced large decorative image solely to meet 75%.**

### Conflict resolution: scientific truth > forced geometry

1. Preserve the **full official GO/SO1–SO3, approved bullet text, citations and notes exactly**. Never shorten a frozen objective, erase a required source, or hide evidence limitations to gain space.
2. Keep the one-message/three-point requirement when the source deck/manifest specifies it; make *supporting* bullets as concise as permitted **before freezing the Stage-1 source**. Do not silently rewrite or remove already approved text.
3. If the required text cannot fit legibly into the remaining 20–30%, **block or request an approved re-layout, split, or companion text slide**. Do not shrink text to illegibility or overlap it with the figure.
4. Do not stretch, distort, artificially upscale small type, crop scientific arrows, or surround a small diagram with white padding to fake occupancy. Adapt the **source artwork and figure aspect ratio** to the reserved region.
5. Preserve **white (#FFFFFF) full slide and white interiors** for all boxes/panels; no gradients, colored fills, texture, shadows, gold or decorative components. Colors may label headings, meaningful lines, arrow classes and small scientific accents only. Use **large, semantically justified directional arrows**, never ornamental arrows.
6. A large figure that misstates physics, adds an unqualified thermal link, invents data or uses unreadable labels **fails** regardless of measured coverage.

### Required Stage-by-Stage acceptance

**Deck3 text / Stage 1**
- Reserve the 75%-target region **at authoring time**, with true empty white space and no drawn placeholder. Store usable-content bounds, intended visual bounds and target in the manifest/QA.
- Put native title/message and three key points in a readable remaining region **only if they physically fit**. Keep the source/footer visible and the objective wording verbatim.
- **Do not claim an old Stage-1 deck with legacy 35–50% figure boxes satisfies this revised requirement.** A previously accepted deck must be explicitly re-laid out before compliant assembly; preserve the old baseline as an archive.

**Deck3 figures / Stage 2**
- Produce **standalone** source graphics optimized for the final dominant slot; omit slide titles, original three bullets, duplicated message and unrelated decorative text **inside** the artwork.
- Validate scientific object membership, directions, evidence statuses, source claims, equations, typography, labels and arrow readability **at the actual insertion dimensions**, not merely when the PNG is opened fullscreen.
- Check whether the content effectively uses the target area. Redesign oversparse compositions, do not magnify whitespace or introduce extraneous information just to fill a box.

**Deck3 assemble / Stage 3**
- Insert only a figure whose correct science/evidence and source geometry have passed the Stage-2 gate.
- Quantify **actual final effective visual occupancy** as well as saved slot geometry. Preserve original aspect ratio and editable slide text/notes/citations exactly. An existing approved 35%-figure deck is **non-compliant** until re-layout is explicitly authorized.
- Render and visually inspect **every figure-bearing slide** at full-slide and presentation/thumbnail size. Reject clutter, illegible figure labels, scientific misstatements, clipping and overlap, even if area is 75%.
- If a compulsory figure is missing, or a generated figure paraphrases a frozen objective, contains a wrong physical state/variable or falsely asserts causal evidence, **release status is BLOCKED / PROVISIONAL**. Do not label it approved.

### Manifest and implementation compatibility

Every figure-bearing slide should eventually store fields logically equivalent to:

```json
{
  "figure": {
    "file": "Slide_03_physical_interface.png",
    "alt": "Specific scientific mechanism description",
    "layout_role": "primary",
    "target_usable_area_fraction": 0.75,
    "acceptance_fraction_min": 0.70,
    "acceptance_fraction_max": 0.80
  },
  "usable_content_bounds_in": [0.7, 1.9, 12.0, 4.9],
  "figure_slot_bounds_in": [3.75, 1.9, 8.95, 4.9]
}
```

Coordinates shown here are **illustrative only**, not an automatically validated layout; actual ratios must be computed from the chosen bounds and slide content. These are **design/QA metadata**, not a claim that the current `examples/deck3.py` supports the fields.

**Implementation gate:** The current repository `examples/deck3.py` uses a legacy smaller fixed image slot. A documentation update **alone does not upgrade its geometry**. Until the runtime and tests are independently updated, block 75%-compliance claims made by the old CLI and perform/verify custom layout authoring where necessary. Never report a geometry QA PASS solely from file save/reopen or slide-picture count.

## 3. Stage 1 — Text / blank visual spaces

**Command:** `Deck3 text`.

1. Read actual approved source content or a manifest of slides; separate `title`, `outline`, `content`, `references`.
2. Verify every externally supported claim has an adjacent verified citation. Full bibliography on final slides and internal canonical authority where applicable.
3. Use one main statement + **three** concise points for each substantive slide **as invisible manifest/authoring structure**; never draw `MAIN MESSAGE` or `THREE KEY POINTS` text boxes; preserve any frozen GO/SO1–SO3 exact text, even if its bullets are necessarily longer.
4. Build 16:9 editable PowerPoint with **no pictures or decorative diagrams**. For every eligible figure-bearing slide reserve the **75%-target primary visual region** (definition in §2A), truly empty/white. Keep required native wording, slide citations and footer fully readable. If the geometry cannot fit, BLOCK and re-author/split only with approval; do not pretend a legacy small slot meets the new rule.
5. Speaker notes carry full evidence qualification and verbal explanation; they do not replace same-slide references.
6. For Chapter 1, the default is 16 slides, with 11 figures on Slides 3–13; generalize according to the provided manifest rather than hard-coding future slide counts.
7. Reopen and render slides. Reject clipping, overlap, unreadable 25% text rail, low contrast, absent citations, non-compliant figure-slot geometry, or changed frozen wording. Record baseline text/notes digests, usable-region bounds, intended figure fraction and any approved exceptions.

**Output:** `*_stage1_text.pptx` + slide manifest + render preview.

## 4. Stage 2 — Standalone figure-by-figure science

**Command:** `Deck3 figures` or `Deck3 figures slide N`.

For each figure: (1) read slide message/three points, actual figure-slot **size and ratio**, and active scientific authority; (2) choose one mechanism/question; (3) build object and arrow registers; (4) choose figure family (architecture, independent forcing, directional mechanisms, literature evidence, boundaries, VVUQ, service outcomes or chapter sequence); (5) generate **only the standalone image asset**, not a slide screenshot; (6) fit the meaningful content to the **75%-target** final region without internal filler whitespace; (7) visually inspect actual presentation-size labels, physics, citations and dimensions; (8) save source PNG/SVG and figure metadata.

**Scientific figure gate:** shared extreme heat alone ≠ proven two-way thermal coupling; candidate T_e→P chain needs grid-side **AC input** evidence; full T_e != active reduced subset; state != function/capability != service/resilience; sustainability requires separately qualified direct and intervention pathways. Never show fake numerical observations.

Do not add presentation-only disclaimers, extra presenter notes, or `CANDIDATE / OPEN` banners into the illustration when these have been expressly excluded from the visible design. Such statuses remain explicit in the manifest / scientific review and figure citation documentation.

**Output:** one source-named `Slide_NN_*.png` per intended slide, optional same-base SVG, per-figure QA record and source files. Existing approved figure assets must not be silently replaced.

**Important automation boundary:** The included Python helper does **not generate domain-correct scientific illustrations out of thin air**; the agent must actually draw/produce them, via original vector code or the appropriate image-generation tool, and verify each before Stage 3. If assets are missing, `Deck3 all` stops with an actionable missing-file report, not substituted clip art.

## 5. Stage 3 — Compose, verify, export

**Command:** `Deck3 assemble`.

1. Reopen Stage-1 PPTX and manifest.
2. For each designated slide, require the **exact file** listed in the manifest; do not guess a file path.
3. Verify SVG/PNG integrity, image dimensions and graphic provenance. Prefer PNG insertion in PowerPoint and keep SVG original separately.
4. Place each image in the **Stage-1 dominant, 75%-target region** with contain fitting, centered and undistorted, without rewriting original textbox runs or notes. Where source aspect ratio would make actual figure occupancy fall below the accepted band, block and remake/re-layout before accepting.
5. Preserve citation/footer, frozen objectives, slide order and reference slides.
6. Assert exact Stage-1 vs final slide text and notes equality, expected picture count per slide, PPTX archive integrity, no images on forbidden slides, correct white interiors, and unchanged source figure hashes.
7. Render *every* slide and inspect at full and thumbnail/presentation scale. On every eligible slide report the intended vs actual **effective visual occupancy** and whether it lies in the 70–80% band. Programmatic boxes alone cannot prove meaningful graphic coverage, label readability or scientific correctness.
8. Deliver final PPTX, contact sheet/preview, Stage-1 PPTX if requested, and archived independent source graphics.

**Output:** `*_final.pptx` and QA JSON including figure occupancy/bounds and exceptions; a high-resolution preview is mandatory. **Do not claim full Deck3 figure-dominance compliance unless the actual PPTX, not merely this skill text, was tested.**

## 6. Runnable orchestrator and manifest contract

- `examples/deck3.py`: generic deterministic Stage 1 / Stage 2 asset audit / Stage 3 / all utility; standard-slide slot geometry targets §2A and measures rectangle coverage, **but does not automatically certify effective visual occupancy, text-fit, or scientific correctness**; no invented domain data.
- `examples/deck3_manifest_example.json`: small demonstration schema only; reuse a real approved outline instead of treating sample content as thesis authority.
- `references/WORKFLOW.md`: exact input/output usage examples, common scientific figure failures, checkpoint/revision protocol.
- `tests/test_deck3.py`: deterministic regression checks for editable text, slide structure, image aspect ratio, missing-figure blockers, and unchanged text/notes.

**Running (from the skill directory):**

```bash
python -m pip install python-pptx Pillow
python examples/deck3.py text --manifest examples/deck3_manifest_example.json --out build/example_text.pptx
python examples/deck3.py figures --manifest examples/deck3_manifest_example.json --figures build/figures
python examples/deck3.py assemble --manifest examples/deck3_manifest_example.json --text-pptx build/example_text.pptx --figures build/figures --out build/example_final.pptx
python examples/deck3.py all --manifest examples/deck3_manifest_example.json --figures build/figures --output-dir build
python -m unittest discover -s tests -v
```

Stage `figures` is an **audit of actual independently generated assets**, not an image-generation substitute; use ChatGPT image generation or a scientific vector renderer to create each image before this CLI stage.

### Strict minimal manifest

```json
{
  "deck_name": "Example thesis chapter",
  "slides": [
    {"kind": "title", "title": "A scientific topic", "subtitle": "Chapter introduction", "notes": ""},
    {"kind": "content", "title": "Scientific context", "message": "One defensible scientific message.", "bullets": ["Point one.", "Point two.", "Point three."], "source_note": "Thesis canonical authority / exact verified author-year citation.", "notes": "", "figure": {"file": "Slide_02_context.png", "alt": "Independent scientific figure explaining the topic."}},
    {"kind": "references", "title": "References", "entries": ["Verified full citation or canonical source record"], "notes": ""}
  ]
}
```

Only `kind=content` with `figure` reserves a figure. A long frozen objective can specify `"layout":"long_objectives"`. Under §2A, a dense objectives slide may require a text-only or split-slide exception, **never an inaccurate figure paraphrase of a frozen objective**. The standard generator now reserves a dominant figure slot and reports placed-picture geometry, but **full 75% compliance remains unverified until effective graphic occupancy and projection legibility have been inspected on the actual deck**. The generator may reject text that cannot fit safely; **never silently truncate frozen research content**.

## 7. Hard-stop gates, release checklist, and user-facing response

**Stop / fail:** missing approved source deck; missing/misidentified figure; evidence/claim mismatch; altered frozen text; changed full T_e boundary; fake numerical data; incorrect arrow semantics; cropped text; illegible scaled labels; or **figure-bearing slides missing a measured, documented 70–80% effective visual share without an authorized scientific/layout exception**.

**PASS checks:**
- file open/save/reopen; original notes and exact text preserved through assembly;
- correct independent figure for each designated slide;
- no image becomes a full-slide screenshot when the intent is supporting illustration;
- source aspect ratio unchanged; no box clipping; **dominant figure occupancy measured against U, not assumed from a rectangle**;
- exact citation-to-claim mapping verified manually and by source registry;
- white panels, Times New Roman style, readable projection size;
- every designed scientific relation passes diagram and evidence gates.

**User response:** provide exact links to verified newly created files; record passes and limitations honestly. Do not say a physical model is validated because image generation, PPTX integrity checks, or numerical code tests passed.

## 8. Version

1.6.2 — 2026-10-09. Defines ecosystem-wide update scope using the primary contract, technical annex and dependency registry; SVG source color preflight integrated into Stage 2/3 with raster-only quarantine; cross-skill tests/CI extended.


1.6.1 — 2026-10-09. Integrates advanced PowerPoint skill as evidence-gated submodule; exact canonical v1.6 sRGB palette remains sole color authority; adds animation, vector, arrow and QA routing without claiming untested backends.


1.5.0 — 2026-10-09. Defines exact sRGB hex/8-bit RGB registry, white-background contrast, and canonical palette-file authority for Deck3 authored design.

1.3.0 — 2026-10-09. Adds explicit comparative A/B/C design learning and four production gates W/F/L/Q, source-bound claims, typography and citation checks, complete 11-asset Chapter 1 requirement, and correct distinction between generator geometry and validated effective occupancy.


1.2.0 — 2026-10-09. Remove on-slide authoring category labels; preserve actual editable wording. Adds Chapter 1 comparative-design lessons and generator regression gate.\n\n1.1.0 — 2026-10-09. User-directed 75% dominant-scientific-figure rule (70–80% band), denominator/meaningful-occupancy definition, safe frozen-content conflict gates, stage-specific QA and explicit warning that existing Deck3 CLI geometry remains legacy until separately updated and tested.

1.0.0 — 2026-10-09. Introduced single short-name three-stage reusable slide workflow. Older scientific-design skills remain authoritative; this skill only orchestrates artifacts and QA.
