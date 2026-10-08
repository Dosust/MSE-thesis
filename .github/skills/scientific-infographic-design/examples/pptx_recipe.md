# Evidence-Controlled Editable PowerPoint Recipe

Use this when the output is a **PowerPoint presentation**, not simply a static picture. Design theory from Jambor & Bornhäuser (2024) and Rougier et al. (2014) supports selecting a layout appropriate to audience and scientific relation. Source methodology alone does not substantiate a thesis physical claim.

## Choosing a renderer

| Output | Renderer | Editability | Validation |
|---|---|---|---|
| System boundary/process/candidate pathway | \`python-pptx\` or PptxGenJS native shapes | Object-level PowerPoint editable | PowerPoint reopens and shapes remain objects |
| Journal diagram/publisher figure | SVG or TikZ | SVG/TikZ editable in vector/code tools; not necessarily native PPTX shapes | Valid SVG/XML, correct labels, source notes |
| Numerical experimental plot | Matplotlib/PGFPlots from verified arrays | Source/code editable; embedded plot itself may not be per-point editable | Units, data, uncertainty and scientific tests |
| Exploratory object illustration | Generative image | Usually raster and scientifically unreliable for arrows/labels | Check manually; redraw all scientific semantics in vector |
| Model-driven interactive diagram | D3/Canvas/HTML | Source-code editable with parameters | Recompute physical model and compare numerics |

## Fully reproducible minimal example

\`\`\`bash
python -m pip install python-pptx
python examples/pptx_builder.py --out build/infographic_examples.pptx
\`\`\`

\`pptx_builder.py\`:
1. creates a pure-white 13.333 × 7.5 inch presentation;
2. draws original editable shapes (system enclosures and directional arrows);
3. places source attribution **on each scientific slide**;
4. attempts to set detail in editable speaker notes;
5. reopens the output and checks three slides are present and contain no picture objects;
6. reports a **technical** pass, never physical validation.

### Why the diagrams are designed that way

- **Slide 3** full P and full T_e ownership: enclosures mean membership, not causality. Blue transfer arrow and green charging-load-effect arrow refer to different physical quantities. The existence of a two-way operating effect does not imply heat-conditioned two-way causality.
- **Slide 4** extreme heat: one external forcing, two independent downstream thermal lanes. No thermal cross-system arrow.
- **Slide 5** two candidate directions: status words are separate from arrow style; grid-side AC input is a required P-facing evidence gate after charger derating.

## Safe workflow for modifying the real 16-slide deck

1. **Load the existing deck, do not recreate it from memory.** If no existing deck is available, report the missing file.
2. Compare slide count, titles, source text and notes against the input file.
3. Preserve original slide order and identify zero-based indexes of slides to replace/augment.
4. Make native shapes for new scientifically meaningful objects, labels, boundaries and arrows; keep the full canonical T_e definition in the appropriate scope view.
5. Retain *unmodified slides* exactly or prove text/shape/source equality after save. If your library cannot replace content without altering slide theme/notes, choose a compatible preservation method or log the limitation.
6. Retain detailed speaker notes and match external claims to same-slide short APA citations.
7. Reopen the presentation, check slide count, content, and notes integrity. Inspect shape types: a single bitmap on a slide is not a substitute for native-editable diagram objects.
8. Render PPTX to 16:9 images/PDF and inspect every changed slide at full slide size and reduced thumbnail. Look for font fallback, overlaps, clipping, source note readability, arrowheads, false connections, inaccurate enclosures.
9. Test source/claim mapping, quote/frozen objectives unchanged, and compare original vs final unchanged slide contents.
10. Store a versioned QA report, blockers, and source script.

**Caution about minimal example:** The included \`pptx_builder.py\` starts a new three-slide demonstration. It is not a reliable generic patch-in-place implementation for arbitrary templates. Do not misstate its capabilities.

## How to write a complete source-aware figure in code

Declare before coding:

\`\`\`python
claim = {
    "proposition": "A shared extreme-heat disturbance may influence two thermal states independently",
    "epistemic_status": "THESIS-DEFINED CONCEPTUAL DISTINCTION",
    "external_basis": ["IEEE C57.91-2025", "Krama et al. (2026)"],
    "internal_scope": "CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md",
    "inference_prohibited": "shared heat proves thermal interdependency",
}
\`\`\`

Use the above record to choose a two-lane layout, exact labels, and separate citations. For models that actually quantify a relation, replace the conceptual record with a traceable equation and data contract before plotting it.

## Figure acceptance decision

Release only when: physical membership PASS, each arrow recorded and supported/status-labeled, citation adjacent and verified, output editable to requested extent, no clipping, readability/contrast PASS, and rendered proof inspected.

**Scientific and design references:**  
- Jambor & Bornhäuser (2024), https://doi.org/10.1371/journal.pcbi.1011789.  
- Rougier, Droettboom, & Bourne (2014), https://doi.org/10.1371/journal.pcbi.1003833.  
- Oberkampf & Trucano (2002), https://doi.org/10.1016/S0376-0421(02)00005-2.
