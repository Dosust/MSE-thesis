# Chapter 1 Deck3 v1.8.1 — 13-slide source and ten AI-image audit
**Date:** 2026-10-09
**Assessment:** `STAGE1_SOURCE_VERIFIED` / `STAGE2_AI_DRAFTS_NOT_APPROVED` / `FINAL_ASSEMBLY_BLOCKED`.
**Source artifact:** local `Deck3_Chapter1_13Slides_STAGE1_TEXT_ONLY_v18.pptx` (not committed to GitHub).
**Governance:** `DECK3_MEDIA_ROUTING_AND_FAIL_CLOSED_IMAGE_QA_V1.md`, `DECK3_NO_EXPLANATORY_PANELS_IN_IMAGES_V1.md`, `DECK3_MECHANISM_TRACEABILITY_STANDARD_V1.md`, `CANONICAL_THESIS_TITLE_V2.md`, `CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`.

## Independently inspected Stage 1
- Opened 13-slide editable PPTX with `python-pptx`; **zero pictures**; slide 1 contains exact title **Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience**.
- Exact frozen General Objective and SO1, SO2, SO3 all found verbatim as editable slide content (Slide 8).
- No visible literal `MAIN MESSAGE` or `THREE KEY POINTS` strings in native slide content.
- Native slide explicit RGB XML source scan found **zero values outside** the exact 13-color authored registry. This checks explicit authored slide colors, not scientific content or raster images.
- Previous Chapter 1 working count **13** (Slides 14–16 references omitted at user request). The separately quoted **eight-slide correction** cannot be validated or adopted without that actual file or an instruction replacing the existing source.

## Ten AI figures — per-slide production repair

| Slide | Defect | Correct implementation |
|---|---|---|
| 3. Engineering Background | Repeated equipment names inside big white cards; physical scene/energy ports not visualized | Original vector-like transformer/grid + EVSE/EV equipment scene; independently editable AC supply and charging-load arrows |
| 4. Extreme-Heat Context | Conceptually sound parallel heat paths but two text-box stacks, not equipment/thermal response | Distinct P and T_e physical thermal responses to *external* forcing; native labels |
| 5. Research Problem | Candidate directions are usefully separated, but long evidence-gate bands baked into pixels | Native PowerPoint per-direction mechanism objects and separate evidence gates, with grid-side AC T_e→P |
| 6. Bounded Gap | AI-baked table and source attributions; citations not independently reviewed | Native editable evidence matrix with adjacent checked citations |
| 7. Research Questions | Giant RQ/SO text cards, double-headed arrows are ambiguous | Native editable alignment only; no physics claims from those connectors |
| 9. System Boundary | Full T_e membership cards, one unlabeled supply arrow, explanatory bottom band | Original physical-system boundary/equipment illustration plus native active-model subset label and named interface |
| 10. Research Approach | Five big method-text boxes, two evidence summary brackets baked into PNG | Native step/gate workflow, optional presenter click-build; verification and validation remain separate |
| 11. Expected Contributions | Long explanatory output panels and an extra bottom note | Native editable SO→expected-output mapping; none represented as validated |
| 12. Resilience/Sustainability | Two large text-heavy dashed assessment panels; ambiguous arrows to resilience | Native state→capability→transfer→service diagram, two distinct bounded assessment pathways; native supporting statements |
| 13. Thesis Organization | Simple sequence flattened as AI art, colored border variants cannot be source certified | Native editable 6-chapter roadmap; arrows denote sequence, not physical causality |

**All ten** were available as 1672×941 raster PNGs; **none** had a corresponding same-stem SVG source or `*.trace.json` at the audited top-level asset location. The absence of SVG does not automatically mean a poor picture, but it does mean **the diagram's independent PowerPoint object editability and exact source-color compliance cannot be certified**. None should be inserted into an allegedly approved scientific deck without new review.

## Workflow correction saved

The new `DECK3_MEDIA_ROUTING_AND_FAIL_CLOSED_IMAGE_QA_V1.md` chooses media from the slide's scientific job. The main Deck3 is **v1.8.1** with synchronized workflow/AI-image/scientific infographic/diagram/advanced PPTX/writing governance. Runtime `deck3.py` no longer labels PNG integrity checks as `PASS stage 2`; each record reports `NOT_REVIEWED_NO_EXPLANATORY_PANEL_GATE`, `native_individual_object_editability: false`, `ready_for_certified_assembly: false`. Four unit tests were added in `test_media_routing_and_provisional_image_gate.py`; remote execution remains NOT VERIFIED.

## Correct next procedure

1. Do not replace the 13-slide Stage 1 source with an unseen eight-slide draft.
2. Convert the research/argument/material into **native editable PPTX**; do not ask AI to produce textual worksheets and citation panels.
3. Generate only scientifically justified physical equipment scenes, retaining exact sources/vector layers, short on-scene labels and no explanatory panels.
4. For each cross-system link, record physically meaningful objects and directed arrow type/source/quantity/receiver/interface; independent evidence and `grid-side AC` for T_e→P.
5. Recheck exact author–date claims against original sources, meaningful object area rather than image boundary, 13-color palette, white interiors, citation/notes preservation and projected text legibility.
6. Independently test native animation object IDs/reveal sequence in desktop PowerPoint before calling the results animated/certified.

**Important:** Updating a design skill is not the same as regenerating affected images. The ten prior PNGs are retained as exploratory assets; they have not been overwritten or fully reconstructed. No false scientific empirical validation, verified novelty, or PowerPoint desktop playback is claimed.
