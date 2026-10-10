# Deck3 — ASU 16:9 Widescreen and Projection Readability Standard V1
**Status:** Mandatory on every Deck3 All Forms / Dossiya Expert Deck3 / AI infographic / animated PowerPoint / slide assembly / exported projection image and presentation QA.
**Date:** 2026-10-10.
**Primary external source:** ASU official Presentation standards and guidelines: https://brandguide.asu.edu/execution-guidelines/presentations (consulted 2026-10-10). This official page explicitly recommends **16:9 ratio templates**; it links to access-controlled ASU PowerPoint and Google Slides templates. It does **not** in its visible presentation section specify an exact 13.333-in dimension, 1920×1080 output, minimum 24-point body type or mandate a sans-serif font. Treat those as thesis presentation engineering targets/user preferences, **not authenticated ASU rules**.

## Canonical slide geometry — MUST
- PPTX aspect ratio: **16:9 widescreen**, specified as exactly **13 1/3 in × 7.5 in** when possible; equivalently 13.333... in by 7.5 in. Validate slide XML `p:sldSz` ratio `cx/cy=16/9` within rounding tolerance. Do not trust property labels only.
- Render preview at **1920×1080** (or integral higher 16:9 such as 3840×2160); pixels describe raster rendering, not inherent dimensions of vector PowerPoint slides. Do not stretch, crop or distort scientific components to fill.
- Do not change to 4:3 for a purported lecture-video exception without a specific explicit external institutional or event requirement **and user approval**. A separate 4:3 deliverable must not overwrite canonical widescreen Deck3.
- Keep 14 approved slides (3–12 infographics, references slide 14) subject to explicit newer user version authority. Reserve usable 70–80% content visual zone for eligible figure-bearing slides only when readability/approved text can be preserved.

## Typography and projection QA
- **Times New Roman** is the user's mandatory Deck3 font for all text, infographic labels, mathematical text where appropriate, citations, native animated shapes, visuals and notes. Do not replace with the examples Arial/Calibri/Verdana solely because generic presentation advice suggests sans-serif.
- **24 pt minimum target for ordinary projected body text**, with headings preferably >=32 pt and key mechanisms/labels ideally >=24 pt. This is a deck readability **target**, not a font size officially verified from ASU's page. Unavoidable dense journal references, citations, equations, small variable symbols/axis ticks may need accessible compact exceptions; record their point sizes and inspect at final projection scale rather than claim 24 pt compliance. Where constraints conflict, first reduce content, redistribute into presenter notes, enlarge scientific artwork, or recompose the figure without changing frozen objectives or the approved slide count. Never silently shrink to illegibility.
- Font-size QA: enumerate all native slide text runs, inheritance and equations; record counts below 24 pt and explicit exceptions. Validate visual readability at projection scale, not solely XML nominal font size. Images: avoid AI-drawn text; add Times New Roman native overlays and check actual raster glyphs if any.
- Support UTF-8 scientific characters/Math OMML. Never alter mathematical meaning to satisfy typography.

## Design and science compatibility
- Load exact 13-token sRGB palette from `.github/skills/deck3/references/DECK3_SRGB_PALETTE.json`; authored canvas, panels and boxes **#FFFFFF**; accent colors only on lines/borders/arrows/headings/technical marks; no decorative gradients, shadows or colored fills. Genuine photographs may show authentic physical colors.
- All directional arrows must be meaningful and source/target/quantity/evidence traceable. 40-class P/T_e inventory and physical boundaries; extreme heat as common forcing not proof of causal propagation; P→T_e and T_e→P separately conditional; T_e→P measured grid-side AC.
- Preserve 14-slide thesis content and exact GO/SO1–SO3, adjacent author–year references, final slide peer-reviewed **articles only**, and animation step meaning.

## Release gates
A: 16:9 p:sldSz XML size — PASS/FAIL.
B: slide and infographic counts — PASS/FAIL.
C: Times New Roman theme/master/native text and visual text — PASS/FAIL/NOT_RUN.
D: Body type >=24 pt target and separately documented exceptions — PASS/EXCEPTIONS/FAIL.
E: Full-HD 16:9 raster and projected readability — PASS/FAIL/NOT_RUN.
F: color and white surface audit — PASS/FAIL.
G: physical mechanism/source rights and citations — PASS/FAIL/OPEN.
H: animation targets/XML and **actual PowerPoint playback separately** — PASS/FAIL/NOT_RUN.
No single gate implies all others passed. Do not call a saved PPTX scientific or ASU-certified without executing required tests.
