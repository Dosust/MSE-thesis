# Deck3 Visual Reference Retrieval Protocol V1 (2026-10-10)

**Status:** Mandatory retrieval, qualification and provenance protocol for Deck3 All Forms, Dossiya Research Expert, scientific AI image generation, and animated editable PowerPoint. Implementation specification; does not claim that automatic orchestration or physics verification has been executed.

## Authoritative collection locator (not yet merged)
- Repository: `Dossiya-SE/MSE-thesis`.
- Library branch: `research/deck3-160-visual-reference-samples-20261010` (PR #72, open at protocol creation).
- Data root: `project/deck3_visual_reference_collection/`.
- Required files: `README.md`, `samples_160.csv`, `sources_13.csv`.
- Never assume these files exist on `main` or this protocol's feature branch. Always fetch with the explicit library ref until merged. On later use check PR/branch status; prefer verified merged canonical path, never silently fallback to other source.
- 160 *design briefs*, **not 160 inspected scientific figures**. Exactly 16 entries per slide 3–12 (eight concepts × two modes). Rights are `NOT_CLEARED`; asset verification is `SOURCE_LEAD_NOT_INDIVIDUAL_ASSET_VERIFIED` on initial collection. Do NOT imply permission or approval.

## Deterministic retrieval algorithm
1. Identify active 14-slide user-approved text baseline; request slide number in [3..12] for figure tasks. Slides 1,2,13,14 are infographic-free. Extract one scientific message, active system boundaries, qualified arrow semantics, and required evidence from source text/notes.
2. Fetch all three collection files using explicit GitHub branch. Parse CSV as proper quoted CSV, never split by comma. Check unique `sample_id`; all fields present; exactly 160 records, ten slide groups of 16, eight concepts each with exactly one `NATIVE_SCHEMATIC` and one `HYBRID_SCENE`. If validation fails, report `CATALOG_FAIL`.
3. Filter by exact integer `slide`; obtain all 16. Exclude any candidate that contradicts scientific message. Candidate scoring for conceptual *suitability* only, not scientific approval: physics relevance 0–30; mechanism clarity 0–25; evidence traceability 0–20; slide-message economy 0–10; editability/animation feasibility 0–10; visual clarity 0–5; total 100. Record weighted rationale and conflicts; no invented evidence. Rank stable by score descending then `sample_id` ascending. Optional selected combination must cite every component sample ID.
4. For every selected candidate, resolve `source_id` in `sources_13.csv` and inspect specific originating article, technical source, or individual media asset. Check actual license/permissions and whether direct reproduction is allowed; generic institutional source pages do not establish per-image rights. Status `REFERENCE_ONLY`, `ADAPTED_REDRAWN`, `DIRECT_REUSE_LICENSED`, `INSPIRATION_ONLY`, `BLOCKED_RIGHTS`, or `BLOCKED_SCIENCE`. A citation is not reuse permission. Source-derived physical claims need in-slide author–year citations and article references in final slide; non-article technical/image credits in figure notes/provenance.
5. Dossiya Expert qualifies components and directional mechanisms independently: full P/T_e boundary vs selected transformer–AC EVSE–vehicle subset; 40-record disposition register; heat as common forcing; P→T_e and T_e→P individually conditional; T_e→P actual grid-side AC V/I/P/Q; thermal control volumes/signs, operating/control action, timing, service metric; knowledge gaps `OPEN` or `NOT_RUN`. Reject any source/visual claiming empirically established coupling without appropriate evidence.
6. Emit a **qualified visual brief** (even when verification remains OPEN) containing slide/message; selected sample IDs and modes; source and rights ledger; exact component/port list; each arrow (from,to,type, quantity/units,evidence); heat/energy boundary; foreground image content; native labels/equations/citations; 13-token palette and all-white background; narration/click sequence; exclusions; research unknowns and blocked concepts. For image generation supply this brief, not an image to imitate closely. Render original equipment only; never embed explanatory panel/text literature cards.
7. Stage 3 builds editable native PPTX shapes/ports/arrows/equations/citations and meaningful On Click animations. Preserve exact frozen GO/SO1–SO3 and user-approved 14-slide format, with Slides 3–12 figure-only; terminal Slide 14 journal-article references only. Distinguish animation-target XML verification from actual Microsoft PowerPoint playback.
8. Record exact selected sample IDs, source URL/DOI, original asset reference, license evidence, transformations, trace.json ID(s), rendered QA, native object and animation IDs, reviewer, timestamp, individual gate states. A successful file write is never scientific/rights/playback certification.

## Gates
- `CATALOG`: exact dataset structure, unique IDs and correct source lookup.
- `SOURCE_RIGHTS`: asset-level rights; direct reuse blocked without permission.
- `SCIENTIFIC`: governing laws, P/T_e limits, causal/evidence boundaries.
- `FIGURE`: exact palette, real mechanisms, minimal labels, no decorative fills, visual clarity.
- `PPTX`: native editability, no collisions, slide text fidelity, figures and speaker notes.
- `ANIMATION`: only scientific reveals; actual playback separately checked.
- `RELEASE`: **FAIL_CLOSED** if any essential gate FAIL/OPEN/NOT_RUN; intermediate output may be explicitly labeled provisional.

## Example (Slide 5)
Fetch 16 Slide 5 records; compare both directions, shared forcing and interface representation by the fixed rubric. Select only suitable concepts; show transformer thermal condition → **applicable conditional restriction** → supply/charging feasibility, separately from EVSE thermal state → charging control → **grid-side AC demand** → transformer loss/temperature response. The latter may reduce losses, so no presumed worsening. Stage reveals: physical subset; conditional P→T_e; conditional T_e→P; service impact as open question. Never claim observed numeric propagation without executed validation.

## Cross-skill calls
Deck3 stage 1 and all forms: retrieve/refine storyboard and register.
Dossiya Expert: review and science-gate candidates.
AI Image Generation: receive qualified visual brief; generate original assets; native annotations deferred to PPTX.
Animated PowerPoint: consume selected sample IDs/brief/trace sidecar and validate actual animation targets.
Deck3 QA: inspect all gates and retain attribution.
This protocol augments, not replaces, `DECK3_EXTERNAL_VISUAL_SOURCE_ADAPTATION_STANDARD_V1.md`, `DECK3_MECHANISM_TRACEABILITY_STANDARD_V1.md`, `DECK3_MEDIA_ROUTING_AND_FAIL_CLOSED_IMAGE_QA_V1.md`, exact palette and thesis authorities.
