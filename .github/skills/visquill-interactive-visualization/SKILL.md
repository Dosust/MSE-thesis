---
name: visquill-interactive-visualization
description: Evaluate, prototype, build, and audit VisQuill GDK TypeScript/SVG interactive scientific geometry for engineering diagrams, state-time exploration, physically qualified interfaces, conditional responses, and traceable model-result viewers. Use only when interaction/reactive geometry materially improves a declared scientific communication goal, or when the user explicitly asks for VisQuill. For ordinary static thesis figures, scientific plots, or slides, route to existing skills and skip VisQuill.
metadata:
  version: "1.0.0"
---

# VisQuill Interactive Scientific Visualization

## Role and activation
This is a **conditional tool-specific companion**, NOT a change to the frozen MSE thesis science and NOT a blanket replacement for existing figure skills. Activate when user explicitly requests VisQuill or when an approved scientific visualization genuinely requires a browser-based viewer with linked geometry, reactive constraints, model-driven interaction, or movable handles. Ask before creating a complex web application if the user asked only for static artwork.

A mere reference to VisQuill in a literature discussion does not mandate using it. Do not imply that adding this skill installs the npm package, creates a live website, or permanently enables a tool in every ChatGPT session.

## Mandatory authority and companion skills
Read, in this order:
1. `AI_RESEARCH_INSTRUCTIONS.md`
2. `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`
3. `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`
4. `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md` for research figures and captions
5. task-relevant frozen title, thermal scope, Electrified Transportation composition, state-time definitions, resilience, sustainability and mathematical frameworks.
6. `../engineering-framework-design/SKILL.md` for components, boundaries and interface grammar;
7. `../scientific-diagram-design/SKILL.md` for evidence, arrow semantics, diagram quality;
8. `../mathematical-visualization-design/SKILL.md` for model-to-encoding and state-time animation.
9. `../scientific-infographic-design/SKILL.md` only when the output is a presentation infographic.

These govern **scientific meaning**. This VisQuill skill governs **interactive implementation**, not scientific claims.

## Tool-choice gate — required before building
Use `references/TOOL_FIT_DECISION.md`:
- Ordinary time-series, uncertainty bands, residual charts or quantitative publication figures → Python/Matplotlib, not VisQuill by default.
- Static system boundaries, one-page methodology views and PPTX thesis slides → editorial vector SVG/PPTX skill; VisQuill generally unnecessary.
- Interactive 2D network/interface layout with geometry automatically adapting to input, time scrubber tied to a validated trajectory, or explicitly defined geometric constraints → consider VisQuill GDK.
- Geography-only data exploration with conventional lenses → consider VisQuill Lens separately only if mapping is central and its stated input types meet the task.
- Numerical solver, calibration, uncertainty computation, causal identification or physical validation → **not VisQuill**.

Before proceeding: state scientific question, viewer audience, what interactions explain that a static figure cannot, source of scientific data, output medium, lifecycle/maintenance costs, and license status. If cost outweighs scientific value for the Spring 2027 thesis, use simpler tools.

## Scientific contract
1. Write a scientific figure contract first: view purpose, full system scope, chosen **bounded case**, modeled objects, forcing, physical states, capabilities, coupling, outputs and units, event/threshold source, evidence status and citations, visual mapping, allowed interactions and artifact format.
2. **State ≠ capability ≠ service.** External extreme heat is forcing. Shared heat or electrical charging is not automatically a qualified thermal interdependency. Keep Power System and the full canonical Electrified Transportation System distinct; EVSE belongs to Electrified Transportation but does not define the full system. A bounded case cannot redefine canonical system composition.
3. VisQuill receives **approved arrays/results from an external physics solver**; its geometry is a visualization of the data. No arbitrary motion, temperature-color mapping, reclassified service metric, or visually assumed P↔T_e coupling without explicit scientific provenance.
4. For each directional cross-system relation, record source, receiver, physical mechanism, condition, evidence and validation status. Draw two arrows only if both directions qualify. **CANDIDATE / OPEN** labels are text status, never encoded only through dashed arrows.
5. Use canonical arrow grammar: solid → physical flow, causal ⇒ state effect, dashed ⇢ control/intervention, dotted feedback measurement, reverse arrow only with separate independent qualification. Use clear oversized arrowheads.
6. Required service `Q_P` and `Q_T` must be independently defined and dimensionally meaningful. Do not confuse charging power with actual mobility-service outcome.
7. If data are mock/demo, visibly label **SYNTHETIC EXAMPLE — NOT A VALIDATED THESIS RESULT**. A library animation or simulation is not model validation.
8. Preserve visible adjacent source citations and provenance near scientific relationships; interactive tooltip sources do not replace static figure caption/citation requirements.

## Implementation workflow
Follow `references/IMPLEMENTATION.md`:
**Decision gate** → **source/data schema** → **minimal design** → **standalone TypeScript implementation** → **geometry/interaction tests** → **scientific acceptance tests** → **static export/fallback** → **license/citation audit**.

### Official installation
- New independent demo (in a separate project folder): `npm create visquill@latest`.
- Existing TypeScript web project: `npm install @visquill/visquill-gdk`.
- Use the installed package's TypeScript definitions plus the matching official API guide/docs rather than inventing method names.
- Initial verified vendor API entry points: `VisQuill.create(container, "prefix-")`; `graphic.canvas`; `canvas.handles.disk`; `canvas.visuals.circle`; `Reactive.do`; `Circles.circleAt`; `graphic.dispose()`.
- Consult `examples/reactive_geometry_demo.ts` for **an illustrative browser module**, not a solver or validated thermal viewer.
- Do not install dependencies into the thesis repository root without an explicit approved implementation task.

## Visual specification
Use only the exact 13 authored sRGB tokens in `.github/skills/deck3/references/DECK3_SRGB_PALETTE.json` for every styled element; no additional shades. Canvas, SVG background and every panel interior pure white `#FFFFFF`; text primarily black `#000000`. Thin semantic color accents: Power blue, Electrified Transportation green, heat red. Never unapproved purple/gold (exact ASU Maroon #8C1D40 and ASU Gold #FFC627 explicitly excepted), colored fills, decorative gradients, shadows or irrelevant motion. Large readable labels and directional arrows. Never use color as the sole status signal. Include accessible legend/labels, keyboard/alternative usage when appropriate, no surprise hidden controls.

## Publishing, license and dependency policy
Use `references/LICENSE_AND_SOURCES.md`. **The VisQuill GDK is vendor-licensed, not an MIT package**. Official 2026 pricing/terms permit non-commercial educational/research use with the required visible "Made with VisQuill" attribution. The separate VisQuill Lab and example projects are MIT licensed; preserve attribution/legal requirements. Do not remove vendor attribution from outputs. Recheck the actual current terms and version on the day of deployment, especially for public demos, commercial use, or redistribution. No copied vendor bundle, compiled package, or third-party assets are committed in this skill.

## Acceptance gates
- **Scientific:** scope/boundaries, traceable data/equations, status labels, no invented physical relation, citations/units, matched scenario boundaries.
- **Functional:** controls change documented model inputs or select **precomputed** valid results; labels, trajectories and geometry remain synchronized; no interactions silently change science; null/missing data handled.
- **Technical:** TypeScript typecheck, browser smoke test, cleanup (`dispose`), performance/accessibility, relative paths and stable version pinning.
- **Reproducible:** working code + data schema + README + version + visible provenance + tested static SVG/PNG fallback when actually implemented.
- **Academic:** static figures remain intelligible independently of viewer; editable presentation assets not silently replaced by browser-only artifacts.
- **Status:** distinguish **NOT RUN / DEMO ONLY / VERIFIED / VALIDATED**. A skill file passing structural tests is NOT proof that the VisQuill runtime was executed.

## Invocation examples
- "Use VisQuill to create an interactive interface diagram from my approved Power–Transportation coupling register."
- "Check if this time-scrubbed thermal-state figure needs VisQuill or a static SVG."
- "Build a VisQuill browser prototype using **synthetic, visibly labeled demonstration data**; do not treat it as validated."
- "Use VisQuill to explore validated model output while preserving source units, boundaries and no assumed bidirectional arrows."
