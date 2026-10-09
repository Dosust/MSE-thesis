# Deck3 — Advanced PowerPoint Methods and Micro-Skills

**Status:** proposed integration guide; current repo SKILL.md and canonical palette take precedence. Source references are collected in `OFFICIAL_SOURCE_REGISTRY.md`.

## A. Capability selection matrix

| No. | Implementation technique | Example audience task | Native individual edit? | Presenter click? | Verified boundary |
|---:|---|---|---|---|---|
| 01 | PowerPoint text/shapes/format controls | Scientific titles, system enclosures | Yes | Yes | PowerPoint desktop |
| 02 | Straight or elbow connectors | P→T_e electrical interface and physical topology | Yes | Yes, if animated | Connection point attachment matters |
| 03 | Curved connectors | Long-distance interfaces around enclosures | Yes | Yes | Curve is not a nonlinear equation |
| 04 | Freeform/edit-point Bézier shape | Feedback loop with explicit relation | Yes | Yes | Anchor/attachment behavior differs from connector |
| 05 | Merge Shapes | Custom instrument/physics symbols | Yes | Yes | Semantic geometry and original asset licensing |
| 06 | SVG imported graphics | Circuit/vehicle/transformer line art | Scalable; separate part editing conditional | Whole SVG by default | Convert-to-Shape only where supported |
| 07 | Native Office Math | Thermal ODE/matrix/equation | Yes | Usually as math object | Round-trip supported LaTeX subset only |
| 08 | Static vector figures (SVG/PDF) | Publication geometry / evidence mapping | SVG may remain whole | Whole graphic | Does not equal independently editable labels |
| 09 | Native charts | State-time trajectory and thresholds | Yes, chart data editable | Often effect options | Only source-grounded/synthetic explicitly tagged |
| 10 | Python-generated SVG plots | Numerically accurate curves, uncertainty | Source editable, PPT component mostly atomic | Atomic unless separated | Preserve script/data; no invented case result |
| 11 | SmartArt | Simple chapter hierarchy | Yes within SmartArt | By level/one-by-one | Do not substitute for scientific mechanism |
| 12 | PowerPoint Animations pane | Evidence-gated appearances | Yes | On Click | Actual slideshow acceptance required |
| 13 | Interactive trigger on shape | Click one equipment object to explain it | Yes | Object click | Some platform/edition differences |
| 14 | Morph with `!!name` matching | Transition model/scope across slides | Yes | Slide transition | Separate slides; 1:1 stable match |
| 15 | Custom motion path | Object following a declared conceptual route | Yes | On Click | Movement does not establish real thermal dynamics |
| 16 | 3D models | Real equipment spatial orientation | Model component edit limited | Interactive/animation | Version and file compatibility; true geometry needed |
| 17 | Cameo | Live presenter on recorded defense slide | Yes | N/A | Not relevant to most scientific diagrams |
| 18 | Hyperlinks/Zoom | Nonlinear presentation navigation | Yes | Click navigation | Not a substitute for explanatory arrows |
| 19 | Native chart/shape animations via Aspose | Programmatic effect sequence | Yes | Yes | License + native PowerPoint playback |
| 20 | OOXML low-level timing | Unsupported custom effect arrangement | Yes | Yes if valid | XML references, testing, viewer differences |
| 21 | PowerPoint COM/VBA | Template batch transforms on Windows | Yes | Yes | Windows desktop + macro security |
| 22 | PptxGenJS | Slide masters/JS diagrams/charts | Yes | Not assumed | Project wiki lists animations unimplemented |
| 23 | Python-pptx | Source-grounded PPTX layout + shapes | Yes | Not via high-level animation API | Pair with tested animation backend |
| 24 | Progressive click-through fallback | Sequential five-stage evidence mechanism | Yes | One slide change per click | More slides; matching page numbering plan |
| 25 | Export PPTX/PDF/SVG/PNG/video | Accessible distribution and revision | Source varies | Depends on output | Exported PDF / images do not play PPTX animation |

## B. When to use each animation family

### Entrance / `Appear` (default)
Show one previously hidden scientific object group. Use after it is semantically introduced. Preserve prior content. Most chapter-introduction diagrams should use this.

### `Fade` (exception)
Same semantic behavior with subtle appearance duration. Use when momentary opacity change does not suggest partial physical reliability. User default is `Appear`.

### Emphasis (narrow use)
Highlight one already visible object when comparing two model states. Do not turn state into a fake warning simply by changing color. Color-coded evidence stays in named labels.

### Motion path (rare)
Move a marker/equipment object if the pathway itself represents a clearly declared object movement (e.g. vehicle mobility) and path/temporal mapping is real or explicitly hypothetical. A moving arrowhead along P→T_e is ordinarily misleading; prefer appearance of a static arrow.

### Morph (narrow use)
Different views across **successive slides**: full system membership → bounded active model, without implying physically evolving temperature. Use matched semantic IDs; key plot axes and explanatory text remain stable. Chart Morph typically cross-fades; do not rely on quantitative interpolation.

### SmartArt build (only organization)
Use for chapter progression, academic workflow or hierarchy. Not appropriate when every node/arrow has physical direction or quantified state semantics.

### 3D rotation (optional)
Use only when physical geometry matters and model is from documented reference. Never interpret a generic rotatable transformer/EVSE model as exact case equipment.

## C. The object-property stack

Every scientific object should have independently specified:
1. Content: physical entity / physical state / operating constraint / service / controller / observer / evidence gate / objective.
2. Relation: direction, mechanism, source/target, timing meaning and evidence status.
3. Rendering: shape or SVG source, bounding box, approved palette token, stroke, label, no colored fill.
4. Editability: `native`, `svg_atomic`, `raster`, `3D`, `chart`, `math_native`.
5. Animation: `static`, `OnClick`, `WithPrevious`, `Morph` (if separate slides).
6. Verification: what was checked vs still awaiting Microsoft PowerPoint GUI.

## D. Recommended Deck3 core pipeline

1. Frozen baseline + scientific source audit.
2. Decide diagram family and exact audience question.
3. Define complete system membership and active model subset.
4. Register objects, directions, sources, status and units.
5. Build native scientific shapes and vector assets.
6. Run mathematical/citation/color/geometry QA.
7. Create reveal groups and separate animation backend only for approved slides.
8. Build stable fallback (cumulative slides).
9. Render *all* cumulative states and compare source text/notes and visual content.
10. Test native desktop PowerPoint click/remote and accessibility; release statuses honestly.

## E. Comparative tool recommendations

**Core open workflow:** `python-pptx` + vector SVG authoring + deterministic geometry tests + user-side desktop PowerPoint QA. Keeps editable science and low operational complexity.

**Higher animation automation:** same source graphics + Aspose.Slides timeline effect backend with licensing/interop QA. Use only when actual version/API proof is available.

**Microsoft-focused interactive workflow:** native PowerPoint GUI for advanced interactive animations, Morph, Merge Shapes and meaningful clickable triggers, then export full PPTX plus fallback.

**Research numerical plots:** Python/Numpy/Matplotlib SVG + raw data/code if approved, not a handmade freeform line pretending to be a physical solution.

**JS alternative:** PptxGenJS for layout/data-driven charts; combine with PowerPoint UI or verified separate animation layer. Do not claim its routine slide generation automatically enables the PowerPoint animation pane.