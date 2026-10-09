# Deck3 visual-reference adaptation: Magnific electric transportation vector gallery

**Status:** DESIGN INSPIRATION ONLY — NO SOURCE ASSET CAPTURE OR VERIFIED SINGLE-IMAGE ANALYSIS
**Reference supplied:** https://www.magnific.com/vectors/electric-transportation-system/3#uuid=705402e0-a394-4556-8f16-a2177df8d5f6
**Checked:** 2026-10-09. Direct resource did not return inspectable image content; page/UUID artwork, individual composition, creator, license and visual content are UNVERIFIED.
**Related independently accessible site context:** Magnific electric transport/transportation vector category pages and its download documentation; platform describes stock formats potentially including SVG/EPS/AI and individual licensing. These platform descriptions do not verify that the URL's selected image has any particular appearance, scientific accuracy or reusable license.

## Usage contract
Use the supplied URL as a **visual reference category** for electric-transportation component illustration, NOT as an authoritative engineering reference. Do not assert having analyzed the selected UUID image. Do not copy, trace, redraw close variations of, or embed the site's specific stock image without license review and an authorized source asset. Instead create an independently composed scientific illustration from the research mechanism and current Deck3 rules.

## Illustration style recommendation, NOT a description of inspected artwork
- Physically recognizable, proportionate vector-like depictions of transformer/distribution equipment, AC feeder, DC EVSE, connector, electrified vehicle and vehicle battery ONLY if those components are material to the slide and source-qualified.
- Show **Power P** and **full Electrified Transportation T_e** as clearly distinct conceptual system boundaries. The EVSE and connector belong to T_e, never a third infrastructure.
- Favor a component-illustration hybrid: recognizable equipment silhouettes paired with rigorous source/destination electrical interfaces and small, precise scientific labels. Realistic drawings are not substitutes for dimensionality, units or qualified laws.
- Keep authored canvas and every panel/interior **pure white**; no gradients, shadows, textured backgrounds, color-filled regions or decorative scenery. Use exact live Deck3 13-token palette exclusively for authored headings, outlines, arrows, icons, strokes and small accents. No guessed stock palette and no arbitrary stock vector recolor from a raster.
- Large, legible, directional arrows only for genuine flow: AC electrical power P→T_e at the equipment interface; a **separate** T_e→P influence arrow only where grid-side AC load and its resulting P state response are qualified; no unsupported causal symmetry. Extreme heat may point independently at each affected component; two exposures do not establish P↔T_e thermal interdependency.
- Provide exact source/receiver and exchanged quantity. E.g. `P_AC,in [W]` at EVSE input, `P_DC,out [W]` at charger output, battery energy `E_B [J/kWh]` as distinct; actual values left OPEN where unsupported. Avoid labeling component temperatures as electricity service.
- Distinguish **PHYSICAL SYSTEM**, **ACTIVE PHYSICS MODEL**, **MEASUREMENTS**, **CONTROLS**, and **SERVICE OUTPUT** when present; do not make a picture of a connected EV and transformer prove any thermal feedback.
- The visual need not show the entire full Te hardware at equal fidelity. State if active illustrations are only a *bounded subset*; do not redefine the full system.

## Reusable Stage-2 AI figure brief (example, independent design)
**Slide scientific takeaway:** 'Power supplies charging through an electrical interface; thermal state may influence component capability only where the mechanism is evidenced.'
**Canvas:** 16:9 white, optional 75% meaningful content region, clear margin for editable PPTX title and real adjacent citations.
**Scientific figure:** On left, concise vector-outline distribution transformer and feeder inside Power (P). On right, DC charger, cable, EV and internal battery symbol inside Electrified Transportation (T_e). Draw one prominent P→T_e AC electrical-power arrow crossing the system boundary at the EVSE AC input. Show EVSE DC output → vehicle battery as an *internal Te* energy-transfer relation. A separate thin-but-legible ambient-heat input may point independently toward transformer and charger, clearly labeled *external forcing*. If the slide is about T_e→P, depict an independent explanatory influence path `EVSE temperature → accepted/available power → measured grid-side AC input → transformer loading` but mark it **CANDIDATE / OPEN** absent source evidence. Do NOT imply automatic transformer derating, V2G, service outage, physical thermal transfer between transformer and EVSE, or genuine bidirectional dynamic causality merely from a pair of arrows.
**Visual discipline:** crisp, recognizable vector-like silhouettes, ample negative space, high contrast, no stock-watermark, 100% white authored background/interiors, 13-color palette tokens loaded from the canonical JSON (not copied color values here), readable text only, labels matched to units and arrow physics, no decorative elements. Avoid generating slide title/body text inside the image if native editable PPTX text is supplied separately.
**Expected outputs:** editable SVG/native vector where achievable; separate raster image if specifically requested; a reviewed mechanism trace sidecar with source/receiver, relation kind, quantity/units and status; final rendered QA before inclusion in PowerPoint.

## Staged acceptance and test
1. SOURCE: URL recorded. Exact selected artwork **NOT INSPECTED**; no source-specific design or license assertions.
2. SCIENCE: physical boundary, applicable laws and arrow meaning traced to frozen thesis authority and supported equipment sources.
3. COLORS: verify authored SVG and the eventual PPTX against canonical 13-token palette JSON and pure-white surfaces.
4. VISUAL: inspect actual rendered asset for legibility, scientific meaning and geometry; no asset rendered in this skill-reference change.
5. TRACE: `DECK3_MECHANISM_TRACEABILITY_STANDARD_V1.md` and `examples/mechanism_trace_qa.py`; structural PASS never proves physics.
6. COPYRIGHT: independently generated original composition; if stock content is actually licensed and used, store precise asset ID/license/attribution and check reuse scope.
7. RELEASE: in absence of rendered/tested asset, this change is **SOURCE_GUIDANCE_ONLY**, never an image QA PASS.

## Scope impact
- CHANGED: Deck3 AI image generation / scientific figure briefing (inspiration → rigorous original generation).
- CHANGED: Deck3 dispatcher routes for figures.
- REVIEWED_NO_CHANGE: frozen science, in-text citation authority, official 13-color palette, mathematical model/physics, native PPTX code, animation, existing files and assets, accessibility/export QA. They remain binding; no generated output was modified.
- Tests: runtime generation/color/trace/PPTX playback **NOT RUN** because request was to teach skill using example, not generate a slide or picture.
