# Deck3 Scientific Minimal Infographic Generation Standard — V1

**Status:** Mandatory visual production and release-gate protocol; subordinate to current thesis scientific authorities.
**Coverage:** Deck3 Slides 3–12, AI equipment-scene prompts, native diagrams, editable/animated PPTX, exports, and other thesis infographics.
**Source basis:** User-supplied 2026-10-10 comparative assessments of two ten-infographic decks; `project/deck3_visual_reference_collection/samples_160.csv`; `project/deck3_visual_reference_collection/sources_13.csv`; `project/CONCEPTUAL_FRAMEWORK_CAUSAL_QUALIFICATION_APPLICATION_V1.md`; current thesis governance.
**Not a research amendment:** Do not change approved RQs, exact GO/SO1–SO3, literature conclusions, mathematical claims, system boundaries, or statuses.

## Controlled natural-context color exception — 2026-10-13

Use `project/visualization/NATURAL_CONTEXT_COLOR_EXCEPTION_V1.md` together with `DECK3_SRGB_PALETTE.json` (policy v1.6.1). The exact 13-color sRGB list continues to govern **all authored scientific graphics, headings, labels, arrows, axes, annotation, borders, diagram marks and institutional accents**; all slide/panel/box/legend backgrounds remain pure white. **Realistic natural environmental objects**—such as plants, herbs, tree foliage, flowers, grass, soil, gravel, rocks, water and strictly necessary sky context—may retain restrained physically plausible colors, in photographs **and original AI illustrative equipment scenes**. Those nonpalette pixels are allowed only as scene-specific, visually secondary **context**, never as new graphic tokens, decorative scenery, colored backgrounds or research-data encoding. Plausible equipment materials may also retain physical material colors in actual/photo-real original scenes. A naturally purple flower is allowed; a purple research arrow is not.

Before releasing any AI figure, inspect natural object purpose, saturation, size, physical plausibility, white surfaces, critical-label contrast and whether the natural depiction might imply unmeasured field/environmental evidence. Native authored marks must be checked separately from exempt scene-image pixels.

## Governing rule
**One figure → one defensible scientific message → minimum sufficient objects → explicitly typed relationships.** Simplicity is a condition of scientific interpretability, NOT a ban on necessary complexity. If removing an element compromises the mechanism, retain it; otherwise remove it.

## Input/authority sequence
1. Read `AI_RESEARCH_INSTRUCTIONS.md`, `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`, `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`, and current scope, state-time, objectives and sustainability authorities.
2. For Deck3 content read the newest explicitly approved full 14-slide canonical text source. The feature-branch text master `thesis/presentations/deck3/DECK3_CHAPTER1_14SLIDES_CANONICAL_TEXT_V1.md` can be used only after resolving its availability and branch authority; do not silently treat a divergent feature-branch copy as merged into main.
3. Retrieve the 16 records for that slide in the 160-sample catalog (8 concepts × two modes). Rank by scientific relevance, boundary fidelity, readability, citation feasibility, editability, and provenance; take the **fewest** concepts necessary. Catalog records are design briefs, NOT 160 inspected rights-cleared figures.
4. For claims, inspect the underlying paper/device/standard rather than relying on AI-generated labels, source leads or generic diagrams.

## Scientific content contract
Every approved visual brief must specify:
- Slide and **one-sentence central message**; question/objective served.
- Physical system/control-volume boundaries; what is outside.
- External forcing, physical states, electrical quantities, inputs/controls, capabilities, service outputs, and times **as distinct ontological types**.
- Minimum justified equipment and objects; evidence for topology/specifications.
- Relationship ledger: unique edge ID, origin, destination, type, direction, units if quantitative, conditional sign, scientific/evidence status, and citation/data/assumption.
- Alternative/common-cause explanation and what test would discriminate it.
- Required speaker-click sequence with persistent prior elements; every reveal has a scientific narrative purpose.
- Source asset licence/permissions, original artwork provenance, uncertainty, QA and acceptance state.

**Scientific arrow types:** (A) AC electrical energy/power flow, (B) heat-energy transfer, (C) control or intervention, (D) measurement/observation, (E) proposed directional functional/causal hypothesis, (F) research/process sequence, (G) external forcing/exposure. Use visibly distinguishable line/label styles and an explicit legend if ambiguous. Never draw AC `V,I,P,Q` as four energy transfers; they are port quantities. Never treat EVSE demand reduction as physical power export; bidirectional V2G only with explicit device capability and source. Shared heat forcing is not P↔T_e transmission. Heat transfer `W` is different from ambient temperature `°C/K`.

**States:** fast thermal ≠ energy (SOC) ≠ degradation/health ≠ algebraic coupling ≠ capability ≠ service ≠ resilience. Avoid generic rising/falling arrows, thresholds, curves, delays, dates or quantities without verified origin and applicable operating conditions.

**Mechanisms remain conditional** unless qualified: P→T_e requires real transformer thermal constraint → actual AC service/charging restriction; T_e→P requires EVSE thermal/control response → grid-side AC demand change → transformer loading/thermal state. Tests compare matched ambient heat, loading, control and EVSE cases; distinguish both directions independently. An arrow in a figure does not prove causality, novelty, validation, or quantitative effect.

## Minimalist visual grammar
1. Use the **simplest faithful representation**: equipment scene only if recognizing apparatus helps; schematic for topology, state diagrams for dynamics, flow sequence for methods, side-by-side conditional chains for competing directions.
2. One principal mechanism group per figure. Up to two symmetric groups only if the contrast itself IS the single message (e.g., candidate P→T_e vs T_e→P, sustainability pathway 1 vs 2).
3. Text budget is **guidance not universal law**: aim for ≤6 primary labels, typically 2–5 words each, plus essential mathematical notation, citation and evidence tags; do not hide scientifically necessary conditions.
4. Remove decorative icons, shadows, textures, gradients, shaded panels, pseudo-data plots, redundant arrows, repeated legends and filler captions.
5. Strong hierarchy: title/message → system/operation → conditional relation → consequence. Use ample white space; no small arrowheads or unlabeled ambiguous crossings.
6. Prefer one strong composition over a mosaic of cards. 160 samples are a search/selection library, not permission to put 16 concepts on one figure.
7. Every arrow earns admission through its registered scientific role. No connector solely to make layout seem continuous.

## Render / editing contract
- **Canvas:** white `#FFFFFF`; every conceptual panel/interior white. No colored panel fills, decorative gradients, shadows or texture.
- **Palette:** exactly the existing 13 approved authored sRGB colors: `#FFFFFF #000000 #12304A #0072B2 #416985 #006D70 #087E98 #176B42 #B4232C #555D66 #8C1D40 #FFC627 #6ACEEE`. ASU gold `#FFC627` reserved for restricted institutional branding, not decorative science. Natural equipment photo pixels do not need artificial quantization.
- **Typography:** Times New Roman for all authored text and native labels, citations, annotations and animations. Mathematical glyphs may use appropriate Office equation font when necessary; match surrounding presentation typographic character. Avoid text rendered inside AI images; any unavoidable baked-in text must be inspected for fidelity and is not natively editable.
- **Geometry:** 16:9, 13.333333 × 7.5 in PPTX. Images preserved without distortion; target export 1920 × 1080 or higher exact 16:9 when requested. Body target ≥24 pt, headings ≥32 pt, justified technical labels/citations may be smaller when legible. These are Deck3 targets, not falsely attributed ASU mandates.
- **AI generation:** generate original *equipment-only* scenes on white/transparent backgrounds with correct category, port arrangement and physically plausible scale; never invent device model, thermal curve, bus wiring, numerical reading, field result or citation. Scientific boxes/arrows, evidence marks, equations, citations and text belong in native editable layers.
- **PowerPoint:** editable text/lines/annotations/relations and native equations if supported. Flattened output alone cannot meet native editability or independently animated scientific layer criteria. Staged on-click Appear/Retain reveals only when narratively justified; test playback in actual PowerPoint separately from package XML and PDF render.

## Known defects: explicit rejection tests
- Reject invented category totals instead of canonical 19 Power + 21 T_e **candidate register entries**.
- Reject paper names, publication years, curves, specifications, time scales, temperature thresholds, test results or citations inserted by image generation without authoritative verification.
- Reject opposite AC arrows implying reverse electrical energy transfer when only grid-demand feedback is proposed.
- Reject unconditional decreases in charging power, increases in transformer temperature, or guaranteed cascading service loss.
- Reject heat-generation → cooling serial diagrams if they conceal independent boundary heat rejection.
- Reject methodological checkmarks and success badges on B0/B1, coupled thermal validation, causality or animation when tests are NOT_RUN.
- Reject layouts with illegible tiny labels, clipped content, invalid approved color values, distorted apparatus, ambiguous arrowhead directions, or false source permission claims.

## Slide-by-slide recommended single-message grammars
| Chapter slide | Minimal figure message | Priority catalog sample IDs (conceptual leads, NOT approved assets) |
|---|---|---|
| 3 | Two physical systems share a **defined grid-side AC interface** | D3-005, D3-011, D3-015 |
| 4 | Common extreme heat changes separate equipment thermal conditions | D3-017, D3-021, D3-029 |
| 5 | P→T_e and T_e→P are **two unqualified candidate transmission paths** | D3-033, D3-035, D3-039, D3-041, D3-045 |
| 6 | What component literature shows versus what integration remains OPEN | D3-049, D3-051, D3-057, D3-063 |
| 7 | RQ1 qualify → RQ2 model → RQ3 quantify supported outcomes | D3-065, D3-067, D3-069 |
| 8 | Exact general objective governs SO1, SO2 and SO3 | D3-081, D3-089, D3-095 |
| 9 | 40-candidate full register versus bounded active AC model | D3-097, D3-099, D3-103, D3-105 |
| 10 | Thermal conservation → admissible dynamics/constraints | D3-113, D3-121, D3-123 |
| 11 | Evidence → B0 → B1 → thermal qualification → IEEE 123-node tests; all gates honest | D3-129, D3-131, D3-133, D3-139 |
| 12 | Two bounded sustainability consequence pathways from defined service trajectories | D3-145, D3-147, D3-149, D3-151, D3-153 |

## Release gate (non-compensatory)
**G0 Authority:** canonical text/objective fidelity. **G1 Science:** every object/edge scoped, typed and supported or clearly OPEN. **G2 Evidence and rights:** citations/permissions checked. **G3 Simplicity:** every item is necessary and visually legible. **G4 Rendering:** no collision, distortion or clipping; correct typography/colors/16:9. **G5 Native semantics:** editable annotations, equations, labels, arrows and preserved layers. **G6 Animation:** timing XML present AND independent actual PowerPoint click-by-click playback demonstrated. **G7 Output/provenance:** record selected sample IDs, final asset hashes/rights, slide QA and status.

G0–G7 each recorded PASS / FAIL / OPEN / NOT_RUN with evidence. A composite numerical score cannot override a scientific, rights or animation FAIL. If a test cannot be performed, release remains PROVISIONAL. This standard is enforceable through repository skill loading, audits and workflows, not by claiming the model has learned persistent independent skills.
