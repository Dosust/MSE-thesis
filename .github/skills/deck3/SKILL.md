---
name: deck3
description: Orchestrate a rigorous three-stage scientific PowerPoint workflow with a dominant scientific infographic occupying approximately 75 percent (acceptable 70–80 percent) of the usable content region on every eligible figure-bearing slide, while preserving accurate scientific claims, editable approved text, citations, exact frozen objectives, notes, and physical system boundaries. Activate for Deck3 text, figures, assemble, all, or one-slide commands.
license: MIT
metadata:
  version: "1.2.0"
  short_name: "Deck3"
---

# Deck3 — Scientific Thesis Slide Production

**Short invocation:** `Deck3` (case-insensitive in conversational requests).  
**One-command aliases:** `Deck3 text`, `Deck3 figures`, `Deck3 assemble`, `Deck3 all`.

This is a **dispatcher and end-to-end production skill**. It calls existing authoritative skills; it does not replace the repository's engineering physics, scientific evidence, or mathematical visual semantics.

## 0. The invocation contract

| Say this | Stage | Deliverable | No changes to |
|---|---|---|---|
| **Deck3 text** | **1** | A fully editable 16:9 text-only PPTX with a **genuinely empty, dominant figure region targeting 75% of usable content area** on eligible visual slides; approved copy, notes and citations | Frozen scientific text and objectives |
| **Deck3 figures** | **2** | Separate, scientifically qualified **image-free-of-slide-text** illustration assets designed for the dominant 75% region, with readability/provenance QA | Stage-1 PPTX text, master layout |
| **Deck3 figures slide 6** | **2 / selective** | Only Slide 6 standalone infographic; preserve all other illustrations unchanged | All other files |
| **Deck3 assemble** | **3** | Insert admitted assets into Stage-1 dominant regions **without distortion**; validate rendered occupancy and readability; preserve all approved text, citations and notes | Source figures and approved copy |
| **Deck3 all** | **1 → 2 → 3** | Text deck → scientific figures → final assembled PPTX + QA + previews | Entire frozen governance |

Other accepted commands: `Deck3 1`, `Deck3 2`, `Deck3 3`, `Deck3 slide 9`, `Deck3 QA`. A request naming one stage must **not** silently execute unrelated stages or revise frozen data.

If the user has already supplied approved text or completed stage artifacts, **reuse them** rather than making up a new outline. Do not automatically overwrite an accepted figure, approved baseline, or previous final deck. Establish all input/output paths from actual user-provided files or successful tool creation; never infer sandbox paths from filenames.

## 1. Binding source-of-truth order

1. `AI_RESEARCH_INSTRUCTIONS.md`
2. `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`
3. `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`
4. `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md`
5. Active frozen title, system-composition, thermal scope, state-time, resilience, sustainability and objectives documents.
6. `.github/skills/engineering-framework-design/SKILL.md`
7. `.github/skills/scientific-diagram-design/SKILL.md`
8. `.github/skills/scientific-infographic-design/SKILL.md` and reference library/storyboard.
9. `.github/skills/mathematical-visualization-design/SKILL.md` when equations, data, trajectories or code-generated plots appear.

**Absolute:** scientific citations adjacent to supported claims **on the slide** and beside evidence-bearing figure claims (APA author–date); internal frozen definitions attributed to canonical files. No arbitrary DOI, parameters, temperatures, thermal curves, or validated bidirectionality. Scope is Power P + *full* Electrified Transportation T_e, heat-conditioned directional mechanisms only; EVSE is a component of T_e, not a third infrastructure. A reduced active model never silently redefines T_e.

## 1A. AUDIENCE COPY RULE — 2026-10-09

**The presentation should display scientific content, not the names of fields in the authoring template.** On all title/outline/content/reference slides, never render the literal metadata headings `MAIN MESSAGE`, `THREE KEY POINTS`, `MAIN IDEA`, or `3 BULLETS`. Keep the actual `message` text and meaningful `bullets` visible, editable, sourced and unchanged unless a separate copy revision is explicitly authorized. The manifest may continue to use one message plus three points as invisible authoring structure; the audience must not see that structure's generic labels. Real semantic headings such as `General Objective`, `Specific Objectives`, `System Boundary` and `References` are allowed.

**Use the 2026-10-09 comparative audit before the next Chapter 1 design pass:** `references/CHAPTER1_COMPARATIVE_DESIGN_LESSONS_2026-10-09.md`. Preserve strong ASU typography/evidence, restrained scientific figures, clear bidirectional-evidence gates, and ensure figures actually occupy the current §2A dominant visual target. Do not claim a legacy small-image layout satisfies 75%.

## 2. The slide architecture (text versus illustration)

- **Slide text stays in native PowerPoint text shapes:** title, **one unlabeled scientific statement**, **exactly three concise supporting points with no visible metaheading** on substantive slides, in-text source/footer, slide number, and detailed notes. An approved frozen objective requiring long text remains **verbatim**, not abbreviated to force layout.
- **Standalone figure asset:** a scientific mechanism, boundary, research comparison, or method figure inserted into a **dominant dedicated region**. It is not a screenshot or mockup of the whole slide, and it must not repeat the slide title, main message, or three points.
- **Reserved visual space:** pure white, truly blank; no gray rectangle, text saying `PLACEHOLDER`, decorative dashed outline, or filler symbol in the delivered text stage.
- **Graphics belong only where they improve comprehension.** Title, outline and references may remain text-only. For active 16-slide Chapter 1, designated figure slots default to Slides **3–13**; Slide 2 has no compulsory figure.
- **Typography:** Times New Roman on editable slide text; use Times New Roman wherever figure text is generated deterministically (SVG/TikZ). If unavailable, preserve the declared name and disclose visual font substitution.
- **Visual:** white canvas/boxes only; black readable text, restrained semantic color on borders/large arrows/small accents. No gold unless explicitly requested, no panel fills, glows, gradients, shadows, gray/colored cards, or ornament.
- **Arrow and status register:** each scientific arrow states source, target, physical transfer/cause/control, citation and `ESTABLISHED`/`THESIS-DEFINED`/`CANDIDATE`/`OPEN`. The drawn line style denotes **relationship**, never unverified status. Never add user-facing badges like `CANDIDATE—not case-qualified` if the user asked to omit presenter-only warnings; retain the qualifying semantics in QA/notes and never imply validation in the visual.
- **Responsive figure fitting:** retain source aspect ratio, contain/center inside the dominant reserved slot, never distort or crop essential evidence to hit an arbitrary quota. Prefer a source figure with the correct final aspect ratio and minimal internal blank margins. High-resolution PNG for reliable PPTX rendering; retain SVG/editable source when available.

## 2A. MANDATORY 75% SCIENTIFIC FIGURE DOMINANCE — 2026-10-09

**User-directed layout contract.** For each eligible **figure-bearing** content slide, a meaningful scientific infographic/diagram/chart/framework must be the dominant communication object, targeting **75% of usable slide content area** (default acceptance band **70–80%**). This overrides the legacy small right-side illustration convention but **does not** override exact frozen research wording, evidence truthfulness, citation visibility or source readability.

### Define the denominator correctly

- **Usable content region (U):** the slide rectangle within agreed horizontal margins **below the native slide title/main-message header and above the citation/footer strip**. Define and save its numeric [x, y, width, height] in the manifest or QA report. The title, slide number, outer margins, fixed header and reference-footer areas are **excluded**.
- **Actual visual region (V):** the rectangular visible bounds of the **meaningful infographic** as placed on the slide, clipped to U. A mostly white graphic with a tiny object at its center must **not** receive full-area credit; measure/visually inspect its **effective occupied graphic content**, not just a blank PNG canvas.
- **Coverage:** visual_share = area(V ∩ U)/area(U); aim for **0.75** and accept **0.70–0.80** only if physical readability, citation preservation and text accuracy pass. Record actual achieved fraction, not only reserved slot fraction.
- **Text budget:** supporting main-message text, native editable bullets, captions and other content use the remaining approximately **20–30%**. The visual dominates; **scientific relationships, evidence, service meanings and necessary numerical labels may reside inside the figure** without copying the whole slide's native text.
- **Exceptions:** title, outline, reference slides, and explicitly text-only slides have no 75% requirement. Dense exact-wording objectives or evidence tables may require a separate text-only companion or approved slide split rather than illegible content or an inaccurate figure. Record reason, approved layout and figure occupancy. **No fabricated filler or forced large decorative image solely to meet 75%.**

### Conflict resolution: scientific truth > forced geometry

1. Preserve the **full official GO/SO1–SO3, approved bullet text, citations and notes exactly**. Never shorten a frozen objective, erase a required source, or hide evidence limitations to gain space.
2. Keep the one-message/three-point requirement when the source deck/manifest specifies it; make *supporting* bullets as concise as permitted **before freezing the Stage-1 source**. Do not silently rewrite or remove already approved text.
3. If the required text cannot fit legibly into the remaining 20–30%, **block or request an approved re-layout, split, or companion text slide**. Do not shrink text to illegibility or overlap it with the figure.
4. Do not stretch, distort, artificially upscale small type, crop scientific arrows, or surround a small diagram with white padding to fake occupancy. Adapt the **source artwork and figure aspect ratio** to the reserved region.
5. Preserve **white (#FFFFFF) full slide and white interiors** for all boxes/panels; no gradients, colored fills, texture, shadows, gold or decorative components. Colors may label headings, meaningful lines, arrow classes and small scientific accents only. Use **large, semantically justified directional arrows**, never ornamental arrows.
6. A large figure that misstates physics, adds an unqualified thermal link, invents data or uses unreadable labels **fails** regardless of measured coverage.

### Required Stage-by-Stage acceptance

**Deck3 text / Stage 1**
- Reserve the 75%-target region **at authoring time**, with true empty white space and no drawn placeholder. Store usable-content bounds, intended visual bounds and target in the manifest/QA.
- Put native title/message and three key points in a readable remaining region **only if they physically fit**. Keep the source/footer visible and the objective wording verbatim.
- **Do not claim an old Stage-1 deck with legacy 35–50% figure boxes satisfies this revised requirement.** A previously accepted deck must be explicitly re-laid out before compliant assembly; preserve the old baseline as an archive.

**Deck3 figures / Stage 2**
- Produce **standalone** source graphics optimized for the final dominant slot; omit slide titles, original three bullets, duplicated message and unrelated decorative text **inside** the artwork.
- Validate scientific object membership, directions, evidence statuses, source claims, equations, typography, labels and arrow readability **at the actual insertion dimensions**, not merely when the PNG is opened fullscreen.
- Check whether the content effectively uses the target area. Redesign oversparse compositions, do not magnify whitespace or introduce extraneous information just to fill a box.

**Deck3 assemble / Stage 3**
- Insert only a figure whose correct science/evidence and source geometry have passed the Stage-2 gate.
- Quantify **actual final effective visual occupancy** as well as saved slot geometry. Preserve original aspect ratio and editable slide text/notes/citations exactly. An existing approved 35%-figure deck is **non-compliant** until re-layout is explicitly authorized.
- Render and visually inspect **every figure-bearing slide** at full-slide and presentation/thumbnail size. Reject clutter, illegible figure labels, scientific misstatements, clipping and overlap, even if area is 75%.
- If a compulsory figure is missing, or a generated figure paraphrases a frozen objective, contains a wrong physical state/variable or falsely asserts causal evidence, **release status is BLOCKED / PROVISIONAL**. Do not label it approved.

### Manifest and implementation compatibility

Every figure-bearing slide should eventually store fields logically equivalent to:

```json
{
  "figure": {
    "file": "Slide_03_physical_interface.png",
    "alt": "Specific scientific mechanism description",
    "layout_role": "primary",
    "target_usable_area_fraction": 0.75,
    "acceptance_fraction_min": 0.70,
    "acceptance_fraction_max": 0.80
  },
  "usable_content_bounds_in": [0.7, 1.9, 12.0, 4.9],
  "figure_slot_bounds_in": [3.75, 1.9, 8.95, 4.9]
}
```

Coordinates shown here are **illustrative only**, not an automatically validated layout; actual ratios must be computed from the chosen bounds and slide content. These are **design/QA metadata**, not a claim that the current `examples/deck3.py` supports the fields.

**Implementation gate:** The current repository `examples/deck3.py` uses a legacy smaller fixed image slot. A documentation update **alone does not upgrade its geometry**. Until the runtime and tests are independently updated, block 75%-compliance claims made by the old CLI and perform/verify custom layout authoring where necessary. Never report a geometry QA PASS solely from file save/reopen or slide-picture count.

## 3. Stage 1 — Text / blank visual spaces

**Command:** `Deck3 text`.

1. Read actual approved source content or a manifest of slides; separate `title`, `outline`, `content`, `references`.
2. Verify every externally supported claim has an adjacent verified citation. Full bibliography on final slides and internal canonical authority where applicable.
3. Use one main statement + **three** concise points for each substantive slide **as invisible manifest/authoring structure**; never draw `MAIN MESSAGE` or `THREE KEY POINTS` text boxes; preserve any frozen GO/SO1–SO3 exact text, even if its bullets are necessarily longer.
4. Build 16:9 editable PowerPoint with **no pictures or decorative diagrams**. For every eligible figure-bearing slide reserve the **75%-target primary visual region** (definition in §2A), truly empty/white. Keep required native wording, slide citations and footer fully readable. If the geometry cannot fit, BLOCK and re-author/split only with approval; do not pretend a legacy small slot meets the new rule.
5. Speaker notes carry full evidence qualification and verbal explanation; they do not replace same-slide references.
6. For Chapter 1, the default is 16 slides, with 11 figures on Slides 3–13; generalize according to the provided manifest rather than hard-coding future slide counts.
7. Reopen and render slides. Reject clipping, overlap, unreadable 25% text rail, low contrast, absent citations, non-compliant figure-slot geometry, or changed frozen wording. Record baseline text/notes digests, usable-region bounds, intended figure fraction and any approved exceptions.

**Output:** `*_stage1_text.pptx` + slide manifest + render preview.

## 4. Stage 2 — Standalone figure-by-figure science

**Command:** `Deck3 figures` or `Deck3 figures slide N`.

For each figure: (1) read slide message/three points, actual figure-slot **size and ratio**, and active scientific authority; (2) choose one mechanism/question; (3) build object and arrow registers; (4) choose figure family (architecture, independent forcing, directional mechanisms, literature evidence, boundaries, VVUQ, service outcomes or chapter sequence); (5) generate **only the standalone image asset**, not a slide screenshot; (6) fit the meaningful content to the **75%-target** final region without internal filler whitespace; (7) visually inspect actual presentation-size labels, physics, citations and dimensions; (8) save source PNG/SVG and figure metadata.

**Scientific figure gate:** shared extreme heat alone ≠ proven two-way thermal coupling; candidate T_e→P chain needs grid-side **AC input** evidence; full T_e != active reduced subset; state != function/capability != service/resilience; sustainability requires separately qualified direct and intervention pathways. Never show fake numerical observations.

Do not add presentation-only disclaimers, extra presenter notes, or `CANDIDATE / OPEN` banners into the illustration when these have been expressly excluded from the visible design. Such statuses remain explicit in the manifest / scientific review and figure citation documentation.

**Output:** one source-named `Slide_NN_*.png` per intended slide, optional same-base SVG, per-figure QA record and source files. Existing approved figure assets must not be silently replaced.

**Important automation boundary:** The included Python helper does **not generate domain-correct scientific illustrations out of thin air**; the agent must actually draw/produce them, via original vector code or the appropriate image-generation tool, and verify each before Stage 3. If assets are missing, `Deck3 all` stops with an actionable missing-file report, not substituted clip art.

## 5. Stage 3 — Compose, verify, export

**Command:** `Deck3 assemble`.

1. Reopen Stage-1 PPTX and manifest.
2. For each designated slide, require the **exact file** listed in the manifest; do not guess a file path.
3. Verify SVG/PNG integrity, image dimensions and graphic provenance. Prefer PNG insertion in PowerPoint and keep SVG original separately.
4. Place each image in the **Stage-1 dominant, 75%-target region** with contain fitting, centered and undistorted, without rewriting original textbox runs or notes. Where source aspect ratio would make actual figure occupancy fall below the accepted band, block and remake/re-layout before accepting.
5. Preserve citation/footer, frozen objectives, slide order and reference slides.
6. Assert exact Stage-1 vs final slide text and notes equality, expected picture count per slide, PPTX archive integrity, no images on forbidden slides, correct white interiors, and unchanged source figure hashes.
7. Render *every* slide and inspect at full and thumbnail/presentation scale. On every eligible slide report the intended vs actual **effective visual occupancy** and whether it lies in the 70–80% band. Programmatic boxes alone cannot prove meaningful graphic coverage, label readability or scientific correctness.
8. Deliver final PPTX, contact sheet/preview, Stage-1 PPTX if requested, and archived independent source graphics.

**Output:** `*_final.pptx` and QA JSON including figure occupancy/bounds and exceptions; a high-resolution preview is mandatory. **Do not claim full Deck3 figure-dominance compliance unless the actual PPTX, not merely this skill text, was tested.**

## 6. Runnable orchestrator and manifest contract

- `examples/deck3.py`: generic and deterministic **Stage 1 / Stage 2 asset audit / Stage 3 / all** utility; **current legacy slot geometry does not implement §2A** until separately revised and tested; no internet or fabricated domain data.
- `examples/deck3_manifest_example.json`: small demonstration schema only; reuse a real approved outline instead of treating sample content as thesis authority.
- `references/WORKFLOW.md`: exact input/output usage examples, common scientific figure failures, checkpoint/revision protocol.
- `tests/test_deck3.py`: deterministic regression checks for editable text, slide structure, image aspect ratio, missing-figure blockers, and unchanged text/notes.

**Running (from the skill directory):**

```bash
python -m pip install python-pptx Pillow
python examples/deck3.py text --manifest examples/deck3_manifest_example.json --out build/example_text.pptx
python examples/deck3.py figures --manifest examples/deck3_manifest_example.json --figures build/figures
python examples/deck3.py assemble --manifest examples/deck3_manifest_example.json --text-pptx build/example_text.pptx --figures build/figures --out build/example_final.pptx
python examples/deck3.py all --manifest examples/deck3_manifest_example.json --figures build/figures --output-dir build
python -m unittest discover -s tests -v
```

Stage `figures` is an **audit of actual independently generated assets**, not an image-generation substitute; use ChatGPT image generation or a scientific vector renderer to create each image before this CLI stage.

### Strict minimal manifest

```json
{
  "deck_name": "Example thesis chapter",
  "slides": [
    {"kind": "title", "title": "A scientific topic", "subtitle": "Chapter introduction", "notes": ""},
    {"kind": "content", "title": "Scientific context", "message": "One defensible scientific message.", "bullets": ["Point one.", "Point two.", "Point three."], "source_note": "Thesis canonical authority / exact verified author-year citation.", "notes": "", "figure": {"file": "Slide_02_context.png", "alt": "Independent scientific figure explaining the topic."}},
    {"kind": "references", "title": "References", "entries": ["Verified full citation or canonical source record"], "notes": ""}
  ]
}
```

Only `kind=content` with `figure` reserves a figure. A long frozen objective can specify `"layout":"long_objectives"`. Under §2A, a dense objectives slide may require a text-only or split-slide exception, **never an inaccurate figure paraphrase of a frozen objective**. The current generator uses legacy slots; **do not assert 75% implementation until code/tests are updated**. The generator may reject text that cannot fit safely; **never silently truncate frozen research content**.

## 7. Hard-stop gates, release checklist, and user-facing response

**Stop / fail:** missing approved source deck; missing/misidentified figure; evidence/claim mismatch; altered frozen text; changed full T_e boundary; fake numerical data; incorrect arrow semantics; cropped text; illegible scaled labels; or **figure-bearing slides missing a measured, documented 70–80% effective visual share without an authorized scientific/layout exception**.

**PASS checks:**
- file open/save/reopen; original notes and exact text preserved through assembly;
- correct independent figure for each designated slide;
- no image becomes a full-slide screenshot when the intent is supporting illustration;
- source aspect ratio unchanged; no box clipping; **dominant figure occupancy measured against U, not assumed from a rectangle**;
- exact citation-to-claim mapping verified manually and by source registry;
- white panels, Times New Roman style, readable projection size;
- every designed scientific relation passes diagram and evidence gates.

**User response:** provide exact links to verified newly created files; record passes and limitations honestly. Do not say a physical model is validated because image generation, PPTX integrity checks, or numerical code tests passed.

## 8. Version

1.2.0 — 2026-10-09. Remove on-slide authoring category labels; preserve actual editable wording. Adds Chapter 1 comparative-design lessons and generator regression gate.\n\n1.1.0 — 2026-10-09. User-directed 75% dominant-scientific-figure rule (70–80% band), denominator/meaningful-occupancy definition, safe frozen-content conflict gates, stage-specific QA and explicit warning that existing Deck3 CLI geometry remains legacy until separately updated and tested.

1.0.0 — 2026-10-09. Introduced single short-name three-stage reusable slide workflow. Older scientific-design skills remain authoritative; this skill only orchestrates artifacts and QA.
