# Deck3 Figure-Only Generation Rule — No Embedded Explanatory Panels
**Effective:** 2026-10-09. **Status:** BINDING for Deck3 Stage 2 AI images, vector graphics, equipment illustrations and Stage 3 image review.

## User-directed rejection example
The generated electric-transport figure had an unwanted bottom strip containing three large explanatory panels:
1. **Component Functions** table;
2. **Energy, Heat and Information Flows** arrow legend;
3. **Key Thermal Interactions** numbered text summary.
These are NOT acceptable parts of a Deck3-generated scientific image. The user requires a high-resolution, visually dominant, physically meaningful illustration—not a slide-within-a-slide, educational worksheet, dashboard, legend collection or infographic summary board.

## Absolute image composition rules
- Never generate component-function tables, textual legends, numbered explanations, key-interaction boxes, bullet lists, footnotes, bibliography, methodological summaries, panel headers or other explanatory dashboard elements **inside the scientific illustration**.
- Never place a bottom information strip, or a top/bottom callout band with substantial text, under/around the equipment scene.
- The image contains only scientifically relevant depicted physical components, necessary system boundaries, genuine directional interface arrows and minimal **on-scene** labels (ideally short component name or carried quantity and unit). Whenever possible, reserve exact labels for native editable PowerPoint text; the image should work visually without them.
- Keep equipment visually large and clear, balanced within the meaningful figure area; leave only necessary whitespace and no artificial filler.
- Any flow legend, detailed equation, source citation, methods, evidence summary or component-function explanation belongs in Stage 1 editable slide text, presenter notes, thesis prose or a **separately requested** standalone table/visual—not embedded in the Stage-2 image.
- The illustrative reference does not override exact physics, palette, white authored background/interiors, citations, accessibility, boundaries or mechanism trace sidecar. The infographic target 70–80% occupancy refers to meaningful scientific illustration, **not** filling the area with tables or explanatory blocks.
- Important: user may explicitly request a table, legend or annotated explanatory scientific graphic in a distinct task; only then include the specified elements, and do not infer permission to add unsolicited ones.

## Negative prompt template for AI visual generation
"NO lower information panels; NO component-functions table; NO arrow legend; NO numbered key interactions; NO infographic dashboard; NO text-rich cards; NO footnote strip; NO decorative section headers; NO labels outside the physical scene; NO unrelated solar/wind/weather icons unless needed by current physical mechanism; NO generated citations or equations."

## QA gate
Reject any Stage-2 generated image containing any of these banned regions even if everything else appears attractive or scientifically plausible. Regenerate/recrop at source to a clean component-and-mechanism-only original image. Do not 'fix' the figure by shrinking unwanted panels. Stage 3 must not approve inclusion. Record `IMAGE_EXPLANATORY_PANEL_VIOLATION` and re-render. No previously generated image is retroactively certified by this instruction change.

## Exact design example
A high-resolution horizontal white-canvas scene with a realistic vector-like distribution transformer on the left, clearly separated EVSE and electric vehicle on the right; one strong AC supply arrow at the boundary, an appropriate internal EVSE-to-vehicle energy-transfer indicator, external thermal forcing only where necessary; few labels. **No bottom three-column strip or legend.** Full T_e definition persists in science/provenance but a bounded subset can be drawn.

## Applicability
Applies to user-initiated Deck3 illustrations and images by default. Specialized educational charts/tables requested explicitly are exempt only for the elements requested.
