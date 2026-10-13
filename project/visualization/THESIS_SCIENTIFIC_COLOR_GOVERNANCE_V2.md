# Thesis Scientific Visual Color Governance — Consolidated V2

**Effective:** 2026-10-13. **Researcher approved natural-context exception.**  
**Application:** All thesis scientific PowerPoint figures, infographic designs, academic posters, diagrams, mathematical plots, image-generation briefs, source images, and visual/rights/contrast reviews.
**Exact machine-readable color authority:** `.github/skills/deck3/references/DECK3_SRGB_PALETTE.json` policy `1.6.1`.  
**Natural environment exception authority:** `project/visualization/NATURAL_CONTEXT_COLOR_EXCEPTION_V1.md`.  
**Skill entry points:** Deck3 and Dossiya Research Expert SKILL.md and shared AI infographic scientific reasoning protocol.

## I. Authoring principle

**Scientific graphics = a controlled, semantically consistent palette. Natural contextual scene objects = physically realistic colors, restricted to context pixels.**

Natural object colors never override the meanings of approved chart colors, physical-domain highlights, source/evidence status, arrow types, engineering subject hierarchy, or white-surface policy.

## II. Official palette: exactly 13 authored sRGB tokens

| Token | Hex | Permitted scientific/communication role |
|---|---|---|
| White | `#FFFFFF` | Every background/canvas, panel and legend interior |
| Black | `#000000` | Mathematical text, axes, technical marks |
| Navy | `#12304A` | Titles/main scientific hierarchy |
| Blue | `#0072B2` | Power System and its physical connections |
| Slate Blue | `#416985` | Secondary technical distinctions |
| Teal | `#006D70` | Qualified intersystem interface distinctions |
| Cyan Blue | `#087E98` | Observations/measurements/information |
| Forest Green | `#176B42` | Electrified Transportation and services |
| Deep Red | `#B4232C` | Critical states and constraints (only when scientifically warranted) |
| Graphite | `#555D66` | Secondary labels and axes |
| ASU Maroon | `#8C1D40` | Institutional headings/identity |
| ASU Gold | `#FFC627` | Small nonessential ASU identity accent only; insufficient standalone contrast |
| Bright Turquoise | `#6ACEEE` | Nonessential, large emphasis strokes only, never critical light-on-white status text |

This table does **not** widen the approved palette. The palette JSON remains the sole exact machine-readable source of values/roles. Respect its WCAG numeric contrast requirements: 4.5:1 normal text and 3:1 essential nontext. ASU Gold and Bright Turquoise fail sufficient white-background contrast for critical marks, and require a high-contrast alternative/pairing.

## III. Color applicability by object class

| Class | Examples | Governing rule |
|---|---|---|
| Authored scientific graphic objects | Borders, native arrows, axes, legends, timelines, system vectors, editable shapes, charts, labels, citations, mathematical annotation, schematic components, research icons | **Only 13 approved sRGB token colors** |
| Authored figure surfaces | Entire slide, title band interior, diagram panel, card interior, legend fill, charts and mathematical figure background | **Pure white #FFFFFF, without fill decoration, gradient, texture or shadow** |
| Realistic apparatus/environmental *image pixels* | Actual or physically plausible illustrative metallic transformer, insulators, charging cabinets, vehicle materials, thermal exchanger | May preserve credible equipment material/paint colors; never create fake physical measurements or re-color hardware to communicate unmeasured status |
| Natural contextual pixels | Live plants, herbs, trees, flowers, leaves, grass, brown soil, rocks/gravel, water, physically necessary sky/weather snippets | **Realistic restrained natural colors** permitted in real photographs and original AI illustrations only when the objects genuinely belong in the scene and remain visually secondary |
| Decorative image features | Repeated red/purple foliage to imitate ASU brand, full-screen blue sky, oversized orange sunset, colored background mountains, symbolic abstract nature patterns | **Not permitted** as a natural-context exception |

A pink or purple flower is an acceptable natural-context pixel, even though pink/purple are restricted scientific design hues. That color **must not** be reused to encode I2, P3, model validation, a data line, a research icon or any other authored mark.

## IV. AI-generation constraints

**Equipment art prompts** may include relevant realistic vegetation, flowers, soil, gravel or landscape fragments with natural hues, but the image must have a white backdrop, no colored panel fills, restrained context and dominant engineering apparatus. Never ask AI to produce fabricated instrument readings, ASU logo, exact technical labels, calendar bars, calculated curves, source citations, documented hardware internals or P3 actions. Add those in editable native PowerPoint and source-linked code plots.

An image that appears photorealistic is still an *illustration* unless supported by documented original photographic provenance. Natural background objects may not be misrepresented as observed Qatar, TU Wien or Norwegian field-site conditions. AI foliage and a real ambient temperature value are not interchangeable evidence.

## V. Figure production decision logic

1. **Determine medium:** Is this a physical-scene illustration, native system diagram, mathematical equation, real result plot, citation matrix or planned timeline? Select image generation only for original physically illustrative equipment scenes.
2. **Tag every colored region:** `AUTHORED_MARK`, `WHITE_SURFACE`, `EQUIPMENT_MATERIAL_PIXEL`, `NATURAL_CONTEXT_PIXEL`. Images may contain multiple pixel classes; origin/source should remain recorded.
3. **Check palette:** Verify only `AUTHORED_MARK` colors against the 13 source tokens. Do not fail photographs solely because credible soil/leaf/water colors are not in the token set; do not excuse native arrow/label violations as "nature."
4. **Check scientific meaning:** Distinct blue P / green Tₑ / teal admitted interface / red validated constraints, as applicable. Natural plant greens cannot automatically encode Tₑ.
5. **Check priority:** Is natural scenery subordinate to transformer/feeder/EVSE/vehicle science and the specific slide message? If no, reduce/remove, or recrop.
6. **Check white surfaces:** Backgrounds and every conceptual panel must remain white. A blue sky background covering an entire infographic is not permitted.
7. **Check projection:** The scene cannot obscure editable labels/ports or reduce text contrast; no artificial visual effect, gradients or irrelevant flora.
8. **Check scientific provenance:** A generated environmental scene does not document a field study. Any scientific inference, result, topology or threshold still needs its own provenance.
9. **Record status:** palette source audit; natural-pixel manual QA; physics QA; native editable object QA; final PPTX render QA; actual PowerPoint animation playback only when claimed. `PASS`, `FAIL`, `OPEN` or `NOT_RUN`; never infer certification from a policy edit.

## VI. Examples: accepted versus rejected

- **Accept:** A modest green plant and brown gravel beside a physically plausible transformer in a white-background engineering illustration; blue P arrow and green Tₑ label are separately edited according to palette.
- **Accept:** A real purple flower far in the margin if it belongs in the physical scene and does not dominate. Its color is a **natural image pixel**, not an ASU or scientific token.
- **Reject:** All trees and flowers recolored ASU maroon/gold as decorative branded foliage.
- **Reject:** Large richly saturated plants obscuring charger grid-side AC port or P1/P2 location.
- **Reject:** Full-slide blue sky/cloud fill substituted for a white scientific canvas.
- **Reject:** An orange decorative "heat wave" to illustrate a verified temperature at a transformer without relevant measured evidence.
- **Reject:** A purple I2 interface line justified by nearby naturally purple flowers.
- **Reject:** Natural-looking vegetation asserted to be documentary evidence of the selected TU Wien, Qatar or Bærug research site.

## VII. Presentation applications

Slide 2 (background) may include subtle justified plants/soil behind original equipment. Slide 3 (candidate effects) should generally keep a minimal equipment-only scene to highlight two distinct candidate pathways. Slide 5 (eight-component architecture) may include only background natural objects that do not obscure any P1–P4/T1–T4 element. Slides 4, 6, 7, 8, 9 and 10 primarily use native editable shapes/plots and generally require **no** natural environmental art. The month-accurate Oct 2026–Apr 2027 Gantt is a calendar chart, not a scenic illustration.

## VIII. Governance and change control

This V2 consolidates existing design controls **without changing** the 13 authorized tokens, exact university identity exception, frozen thesis physics, the four-plus-four component selection, citation standard, model-equipment validity restrictions, or accepted slide text. It extends an already recognized photographic physical-color principle to **original AI-generated natural-context illustrations under explicit restrained-context gates**. Existing images are not retroactively accepted or visually QA-passed; inspection is required when reused.

**Full official exception wording:**

> All engineered components, scientific annotations, and presentation elements must follow the approved project color system. Natural contextual elements such as vegetation, flowers, soil, sky, and other environmental features may retain restrained natural colors, provided they remain realistic, visually secondary, and do not interfere with the scientific hierarchy or interpretation of the figure.
