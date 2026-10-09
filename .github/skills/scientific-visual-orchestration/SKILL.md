---
name: scientific-visual-orchestration
description: Route scientific visual requests to the correct existing specialist without collapsing its authority. For Deck3, preserve the frozen thesis science, v1.6 palette, three stages, exact editable text, citations, 75% meaningful-figure contract, and honest QA status.
license: MIT
metadata:
  version: "1.0.0"
  deck3_compatibility: ">=1.6.0,<2.0.0"
---

# Scientific Visual Orchestration — additive cross-skill contract

This is a **router**, not another rendering engine, scientific source, or replacement for existing `SKILL.md` files. Use when a request combines Deck3 presentation production with infographics, formal diagrams, frameworks, mathematical figures, charts, shader lessons, animations, or browser interactions. For a straightforward standalone task, invoke the single relevant specialist directly; do not load every skill indiscriminately.

**Binding source:** [routing contract](references/ROUTING_CONTRACT.json); [acceptance gates](references/ACCEPTANCE_MATRIX.md); [Chapter 10 transfer](references/CHAPTER_10_TRANSFER.md). The authoritative 13-token color source for thesis-authored graphics is [Deck3 sRGB palette](../deck3/references/DECK3_SRGB_PALETTE.json). Never clone or hand-maintain that palette in this router.

## Nonnegotiable scientific and editorial precedence

1. `AI_RESEARCH_INSTRUCTIONS.md`, `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`, `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md` and thesis citation standard.
2. Exact frozen thesis title, complete Power P and full Electrified Transportation T_e composition, heat-conditioned admitted physical scope, state-time distinctions, objective language, evidence statuses and approval requirements.
3. Engineering-framework-design: **physical/functional semantics and system boundary**.
4. Scientific-diagram-design: **element/arrow grammar**; mathematical-visualization-design: **mapping, equations and animation-time semantics**.
5. Scientific-infographic-design: **figure family, audience-facing composition and adjacent scientific citations**.
6. Deck3: **stage routing, 16:9 editable presentation text, approved stage manifests, 75% meaningful geometry on eligible slides, source-preserving assembly and release QA**.
7. Optional implementation specialists (advanced PowerPoint, VisQuill, procedural mathematical art): **methods only**, never upgraded authority over (1)–(6).

When there is a conflict, higher authority wins. Do not resolve missing scientific evidence through visual effects, auto-generated parameters, fabricated plots, full-system redefinition, copied source graphics or unsupported bidirectional arrows.

## Task-aware routing

Classify the task *before* calling a specialist. Use [ROUTING_CONTRACT.json](references/ROUTING_CONTRACT.json), which has exactly one primary specialist per task family and explicit conditional helpers. The specialist is responsible for its substantive output; Deck3 assembles it only when a deck deliverable is requested. Do not duplicate specialist methods in Deck3.

- **Deck production:** Deck3 `text`, `figures`, `assemble`, `all`, `slide N` remain exactly as specified. Deck3 owns editable source wording, frozen digests, notes/citations, stage separation and slide lifecycle.
- **Physical framework or mechanism:** engineering-framework-design -> scientific-diagram-design -> optional mathematical-visualization-design -> infographic only if audience-level compression is needed -> Deck3 on presentation request.
- **One explanatory diagram:** scientific-diagram-design; optionally infographic for layout, never for physical proof.
- **Numerical state-time chart, PDE/vector field or exact mathematical figure:** mathematical-visualization-design; require governing equation, domains/units, reference computation, appropriate captions and tests.
- **Standalone infographic:** scientific-infographic-design. A semantic framework or quantitative plot still delegates its actual scientific correctness to its specialist.
- **Native PowerPoint animation / editable objects:** advanced_powerpoint *under Deck3* when supported by the installed version and separately verified in PowerPoint; do not promise that `python-pptx` has untested animation capabilities.
- **Interactive geometry:** VisQuill only after its tool-fit/license/performance gate; a static SVG is normally enough.
- **Procedural shader study:** procedural-mathematical-art only for an explanatory geometry or educational exercise; not a physical model, measured hazard, case-specific response law or stochastic calibration. The science specialist always supplies valid model outputs first.

## The visual semantics rule

```text
Science/evidence -> accepted mathematical or semantic object
                 -> verified computation/typed relations
                 -> figure family and deterministic rendering
                 -> readability, accessibility, provenance checks
                 -> optional Deck3 assembly and release audit
```

**Animation** displays a specified state or mapping as a function of physical time or explicitly labeled display time. **Diagram** encodes typed relations; arrows must be justified. **Mind map** encodes conceptual hierarchy, never causality. **Chart** encodes measured/theoretical quantities with units and provenance. **Mathematical figure** encodes a named set, map, projection or invariant. Selecting a family is not license to insert otherwise unsupported visual data.

## Deck3 v1.7 nonregression fence

This router is **additive**. It must not change Deck3 v1.6 geometry acceptance (meaningful 75% target / 70–80% acceptable band, with approved scientific exceptions), the three-stage contract, slide-specific frozen objectives, editable native text/notes/citations, citation proximity, Stage-1 blank figure region, Stage-2 independent artwork, Stage-3 lossless assembly, or the 13 registered colors. It must not claim a 75% layout **implemented** by the legacy Deck3 CLI (still documented as unresolved). Gold is valid only as exact ASU Gold `#FFC627` for small **nonessential institutional accents**; never essential marks on white. No other yellow/gold design colors. Photography preserves authentic colors.

## Artifact and release contract

Each output declares: primary skill and helpers, source authority, model/data evidence status, frozen content hash or concept inventory, figure family, equation/edge register where relevant, units and time semantics, generated source and command, approved palette tokens, alt text, caption/citation, known limitations, independent QA results and any blockers.

Distinguish `SPECIFIED`, `BUILT`, `FILE_VERIFIED`, `RENDER_INSPECTED`, `POWERPOINT_PLAYBACK_VERIFIED`, `SCIENTIFICALLY_EVIDENCED` and `PHYSICALLY_VALIDATED`. Do not promote between these from code-unit tests or a saved file alone. Never imply a PPTX/render/animation is fully certified when real application/device checks were not performed.

## Change governance

For each skill upgrade: create a scoped PR, record existing authorities, modify the smallest compatible section, add explicit regression assertions for v1.6 invariants, run all available tests, compare generated slide text/notes/citations and render inspected variants, and disclose any inaccessible Actions or PowerPoint GUI gates. Skills remain individually versioned: this router does not automatically upgrade other skills. 
