# Deck3 Presentation Variant Router V1 — Explicit 10 / 8 / 13 / 14 Slide Authority

**Effective:** 2026-10-13. **Routing instruction only**; does not rewrite other user-approved text, citations, source decks or scientific authority.

## Mandatory decision before `Deck3 all`, `Deck3 text`, `Deck3 figures` or `Deck3 assemble`

Resolve `deck_variant` from the **current explicit user request** and its actual source text/manifest, not historical defaults or inferred filenames. Do not mix slide numbers, sources or image placement across variants.

| Variant ID | Authorized source/context | Count and visual placement |
|---|---|---|
| `mse_progress_10_2026_10_13` | User explicitly approved exactly **10 slides** in conversation on 2026-10-13 (titles and content descriptions below) | 10 slides total, including Slide 2 Outline and Slide 10 Thank You; image placement **only where visual is justified**, and each requested image is a standalone asset |
| `deck3_3min_8` | `thesis/presentations/deck3/DECK3_3MIN_8SLIDES_CANONICAL_TEXT_V1.md` if accessible and still approved for an explicitly requested 3-minute version | 8 slides; follow that master and its figure-bearing slides |
| `chapter1_13` | Actual approved 13-slide Chapter 1 text/manifest when explicitly selected | 13 slides; media routing based on its own approved content |
| `chapter1_14` | `.github/skills/deck3/references/CHAPTER1_14_SLIDE_WORKING_REVISION_2026-10-10.md` plus the authentic full approved 14-slide text source | 14 slides; 10 distinct figures for Slides 3–12; others text-led |

**Critical:** The previously referenced `thesis/presentations/deck3/DECK3_PRESENTATION_MASTER_ROUTER_V1.md` was not found on `main` at this review. This new file is the explicit routing authority. Existing instructions that say “active 8” or “current 13” apply **only if that exact variant is selected**. If a manuscript, agreed 10-slide text or underlying frozen title is unavailable, keep content **OPEN** rather than invent slide copy.

## Exact 10-slide user-authorized title and purpose mapping

| ID | Title (user approved) | Approved content boundary | Recommended figure media (not forced art) |
|---|---|---|---|
| 1 | Title | Exact frozen research title; presenter, ASU, verified supervisor details | Restrained original physical equipment image **optional**; all typography and logos external/native; never generate ASU logo |
| 2 | Outline | Presentation structure and key topics | **Native editable outline**; no standalone artwork necessary |
| 3 | Research Background | Extreme heat, Power infrastructure, electrified transportation and thermal exposure | Standalone physical-environment *two-system* heat forcing illustration, **not** heat-wave decoration |
| 4 | Research Problem, Gap & Objectives | Scientific problem, unresolved interfaces, exact GO/SO1–SO3 | **Native editable evidence-to-gap and objective diagram**; no AI text cards |
| 5 | Physical System Architecture | Eight working P1–P4 and T1–T4 research components, physically justified typed interfaces | **IEC-inspired single-line P1/P2/T1/T2 + separate SoS/thermal/control relationships**, all source-checked; no fake installed P3 or reverse power |
| 6 | Research Methodology | Evidence → mechanisms → electrical/thermal modeling → qualification/verification | Native editable research process; clearly separate solver verification and independent field validation |
| 7 | Work Completed | Literature screening, component/evidence qualification, reproducible modeling work | Native editable evidence-status table/timeline with **actually supported milestones** |
| 8 | Preliminary Results | Real verified outputs and appropriately qualified plots | **Matplotlib/other numerical plot from admitted source CSV or model output**; do not use AI-generated curves or illustrative scatter as data |
| 9 | Remaining Work & Research Plan | Open I2/I3 evidence gates and **October 2026–April 2027** work timeline | Native editable month-based schedule with future/conditional tasks clearly distinguished |
| 10 | Thank You | Closing and questions | Minimal closing, no new result or invented installation; original equipment illustration optional |

No more than 10 slides are added automatically. **Slide 2 Outline and Slide 10 Thank You are included**, not extras. **Do not force 10 equipment images into all 10 slides.** When user asks “one image for each slide,” interpret as 10 separate scientific-purpose assets, but ask/review whether outline, results, and timetable are better delivered as separately editable native graphics; never fulfill with one contact sheet or a 10-panel collage. An inserted graph created from actual data can be a scientifically valid independent illustration.

## Production/QA requirements for the 10-slide branch

- The user's text above is a **title/purpose summary**, not a complete final verbatim source for every bullet, supervisor identity, citations or numerical figure. Freeze exact text only after it is inspected/approved. No invented equations, charts, measured results, or institutional details.
- Stage 1: authentic approved text/citations native editable; outline/thank-you first-class slide types (do not force “3 bullets” or source_note on them if the approved source differs).
- Stage 2: generate only admissible illustrations for appropriate slides, **independently inspect and export** each genuine asset. Source/publication/physical/rights and diagram-family selection governed by `DECK3_PROFESSIONAL_ENGINEERING_VISUAL_REFERENCES_V1.md`.
- Stage 3: preserve 10-slide exact ordering, original notes and citations, no text–image overlaps. 75% meaningful figure-area target applies only where figure scientifically warranted and geometry can be verified, never to outline/results tables or thank-you by default.
- Animation: presenter on-click reveals only for declared scientific relationships; physical-time data-model animations separate and labeled. Actual playback `NOT_RUN` until executed.
- **Current runtime caveat:** `examples/deck3.py` has a legacy strict three-bullet manifest and limited `kind` list. **A 10-slide routing policy does not make legacy runtime support this variant automatically.** Use an authorized source manifest adapted with tested runtime code; do not silently manufacture missing slide copy or claim a compiled 10-slide PPTX.

## Status

`ROUTED_FOR_PRODUCTION_NOT_YET_RENDERED`: explicit 10-slide variant recorded. No individual image or finished deck becomes validated through adding this file. All formerly generated AI-only images remain provisional until each is re-reviewed against the relevant scientific/visual authority.