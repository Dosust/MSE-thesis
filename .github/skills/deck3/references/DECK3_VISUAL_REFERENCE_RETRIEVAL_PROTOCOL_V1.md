# Deck3 visual-reference retrieval protocol V1
Status: Active workflow instruction, not an asset or scientific validation.
Applies: Deck3 All Forms, Dossiya Research Expert, AI image briefs, advanced native animated PPTX, diagram and infographic skills.

## Canonical library on main
- `project/deck3_visual_reference_collection/samples_160.csv`
- `project/deck3_visual_reference_collection/sources_13.csv`
- `project/deck3_visual_reference_collection/README.md`
- `.github/skills/deck3/references/CHAPTER1_14_SLIDE_WORKING_REVISION_2026-10-10.md`

## Mandatory typography and palette contract (2026-10-10)
Use **Times New Roman** for ALL authored written content in Deck3: visible slide titles/body/captions/citations, native diagram and chart text, native editable animation layers, labels/equations where text-font applies, and text inside any newly generated AI infographic. Best practice: generate equipment-only AI scenes with NO embedded text, then place every annotation as a native Times New Roman PowerPoint text object. Never claim to change font inside a flattened raster by adjusting PPTX text runs; regenerate or reconstruct that asset. Apply the exact approved 13 sRGB colors to all authored marks, and pure #FFFFFF to all canvas/box/panel interiors; no decorative fills, gradients, or shadows. Natural authentic equipment-image pixels are exempt from palette quantization. Preserve citations, correct math typography, and source text. Audit actual rendered slides, embedded images separately, and all editable text-font runs before release; animations must retain matching TNR typography throughout reveals.

## ASU widescreen and projected readability contract (2026-10-10)
**Source:** ASU Brand Guide, Presentations standards: https://brandguide.asu.edu/execution-guidelines/presentations (ASU explicitly recommends 16:9). For every Deck3 PPTX, static infographic, AI image asset intended for a slide, animated composition and PDF export:
- **Mandatory slide geometry:** 16:9 widescreen, **13.333333 × 7.5 in** in PPTX, with target raster/export **1920 × 1080 px** or a higher exact 16:9 resolution. ASU confirms 16:9; the inch and pixel settings are the Deck3 implementation convention, not an independently stated ASU pixel requirement. Do not distort/crop scientific evidence to fit; use contain/padding/appropriate reconstruction.
- **Typeface decision:** continue the user's explicit **Times New Roman for all authored Deck3 text**, including headings, body, figures, equations where applicable, citations, and editable animated objects. General sans-serif accessibility suggestions do **not** silently override this user-specific font choice. Native equations may use mathematically necessary glyphs/OMML.
- **Audience readability:** aim for **≥24 pt primary body text**, **≥32 pt headings** and adequate contrast. Dense citations, equations, references and technical labels may need justified smaller type; never assert a universal ASU-issued 24-pt rule unless separately verified. Prefer simplifying or moving detail to notes over shrinking essential claims.
- **Brand and palette:** ASU publishes branded presentation templates; access may require an ASU account. Retain the existing 13-color Deck3 governance, pure-white slide/panel interiors, and its institutional-only ASU gold exception. Do not invent institutional approval of a custom Deck3 color theme.
- **Release gates:** assert exact slide dimensions programmatically; check all images/figures are 16:9-compatible at placement and any external photographs preserve aspect ratio; verify run-level Times New Roman and font sizes, adequate text contrast, bounding-box collision-free geometry, 1920×1080 export geometry when requested, and PowerPoint animation after final layout. Flag FAIL/OPEN/NOT_RUN truthfully; do not claim actual slideshow playback from PDF rendering.

## Mandatory execution
1. Resolve source-of-truth 14-slide chapter text and its exact GO/SO1–SO3. Infographics on Slides **3–12** only; no infographic on 1, 2, 13, 14.
2. Read `samples_160.csv`. Filter `slide` for the current target and compare its 16 entries. Do **not** call all 160 existing verified artworks: these are design briefs, and all asset reuse rights are NOT_CLEARED.
3. For each shortlisted sample_id, read its linked `source_id` in `sources_13.csv`. Inspect the actual publication/equipment/figure and check its technical relevance. Record an individual figure URL and actual permission/attribution if reuse is sought; otherwise mark scientific reference only.
4. Dossiya Expert checks real physical topology, component role, AC/DC port and power balance, extreme heat vs genuine directional propagation, state/time/controls, admissible equations, service effects and confidence level. Peer reviewed article ≠ proof of this thesis coupling.
5. Create an original scientific storyboard: single claim; source/equipment boundary; eligible controls/flows; arrow origin-destination-type-unit; image versus native editable layer; minimal necessary figure labels; source-adjacent editable citations.
6. AI image creation may illustrate independently specified equipment appearance, never determine wiring, topology, data, equations, temperatures or validity. Never copy copyright-protected reference arrangement. Authentic photograph/AI physical objects may keep natural colors; every authored diagram mark must use approved Deck3 13-token palette and pure white interiors.
7. Advanced PowerPoint builds native editable boundaries, connectors, labels and math. Set scientifically ordered presenter-click reveals only where they materially improve understanding. Layering flattened PNGs does not give independently animated internal objects.
8. Verify original text, citations, notes, objectives and 14-slide order; zero collisions/clipping; evidence/rights and arrow status; PowerPoint animation timing XML and rendered scenes. Playback in real PowerPoint remains NOT_RUN until actually tested.
9. Persist a small per-slide selection record (sample_id, source_id, evidence status, use permission, selected visual grammar, animation plan, QA status). Fail closed if a source, right, physical state or causal link is unsupported.

## Workflow routing
- **Deck3 All Forms:** Orchestrates steps 1–9 and final release decision.
- **Dossiya Expert:** Owns evidence/physics qualification and falsification; records OPEN items.
- **AI Image Generation:** Consumes qualified original scene brief, outputs illustrative assets only.
- **Animated PPTX:** Integrates those assets with editable scientific overlays and evidence-bounded on-click reveals.
- **Diagram/Infographic/Math/Framework/VisQuill:** Use the same selection IDs and approvals when used for Deck3; interaction is optional.

## Example
`Deck3 Slide 5: filter slide=5 → evaluate 16 samples → select two conditional P→T_e/T_e→P visual concepts → qualify physics → draw original separate native causal chains → animate individually → no claim of proven direction.`

**Not a background daemon:** Invocation actively reads files through connected GitHub tools. Merely naming a skill does not fetch source images, download copyrighted visuals, or validate the PPTX automatically.
