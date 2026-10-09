---
name: deck3
description: Orchestrate a rigorous three-stage thesis PowerPoint workflow from source-grounded text to standalone scientific infographics to assembled, audited presentation. Activate for Deck3 text, Deck3 figures, Deck3 assemble, Deck3 all, or a single-slide request such as Deck3 figures slide 6. Preserve the exact approved text, adjacent scientific citations, frozen objectives, notes, and complete system scope.
license: MIT
metadata:
  version: "1.0.0"
  short_name: "Deck3"
---

# Deck3 — Scientific Thesis Slide Production

**Short invocation:** `Deck3` (case-insensitive in conversational requests).  
**One-command aliases:** `Deck3 text`, `Deck3 figures`, `Deck3 assemble`, `Deck3 all`.

This is a **dispatcher and end-to-end production skill**. It calls existing authoritative skills; it does not replace the repository's engineering physics, scientific evidence, or mathematical visual semantics.

## 0. The invocation contract

| Say this | Stage | Deliverable | No changes to |
|---|---|---|---|
| **Deck3 text** | **1** | A fully editable text-only 16:9 PPTX with an **actually empty** infographic region wherever an illustration is needed; approved slide copy, notes, citations | Frozen scientific text and objectives |
| **Deck3 figures** | **2** | A separate, scientifically qualified illustration for every designated slide (PNG and, where appropriate, editable SVG), contact sheet and figure-source/arrow registry | Stage-1 PPTX text, master layout |
| **Deck3 figures slide 6** | **2 / selective** | Only Slide 6 standalone infographic; preserve all other illustrations unchanged | All other files |
| **Deck3 assemble** | **3** | Place admitted figure assets into Stage-1 blank regions **without stretching** or changing approved text, citations or speaker notes; render/QA final PPTX | Source figures and approved copy |
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

## 2. The slide architecture (text versus illustration)

- **Slide text stays in native PowerPoint text shapes:** title, **one main message**, **exactly three concise points** on substantive slides, in-text source/footer, slide number, and detailed notes. An approved frozen objective requiring long text remains **verbatim**, not abbreviated to force layout.
- **Standalone figure asset:** a scientific mechanism, boundary, research comparison, or method figure inserted into an empty region **beside** text. It is not a screenshot or mockup of the entire slide, and it must not repeat the slide title, main message, or three points.
- **Reserved visual space:** pure white, truly blank; no gray rectangle, text saying `PLACEHOLDER`, decorative dashed outline, or filler symbol in the delivered text stage.
- **Graphics belong only where they improve comprehension.** Title, outline and references may remain text-only. For active 16-slide Chapter 1, designated figure slots default to Slides **3–13**; Slide 2 has no compulsory figure.
- **Typography:** Times New Roman on editable slide text; use Times New Roman wherever figure text is generated deterministically (SVG/TikZ). If unavailable, preserve the declared name and disclose visual font substitution.
- **Visual:** white canvas/boxes only; black readable text, restrained semantic color on borders/large arrows/small accents. No gold unless explicitly requested, no panel fills, glows, gradients, shadows, gray/colored cards, or ornament.
- **Arrow and status register:** each scientific arrow states source, target, physical transfer/cause/control, citation and `ESTABLISHED`/`THESIS-DEFINED`/`CANDIDATE`/`OPEN`. The drawn line style denotes **relationship**, never unverified status. Never add user-facing badges like `CANDIDATE—not case-qualified` if the user asked to omit presenter-only warnings; retain the qualifying semantics in QA/notes and never imply validation in the visual.
- **Responsive figure fitting:** retain source pixel ratio, letterbox/center inside the reserved slot, never distort for the sake of filling space. High-resolution PNG for reliable PPTX rendering and independently delivered SVG for scalable source.

## 3. Stage 1 — Text / blank visual spaces

**Command:** `Deck3 text`.

1. Read actual approved source content or a manifest of slides; separate `title`, `outline`, `content`, `references`.
2. Verify every externally supported claim has an adjacent verified citation. Full bibliography on final slides and internal canonical authority where applicable.
3. Use one main message + **three** concise points for each substantive slide; preserve any frozen GO/SO1–SO3 exact text, even if its bullets are necessarily longer.
4. Build 16:9 editable PowerPoint with **no pictures or decorative diagrams**. Leave the right-side reserved figure region actually empty wherever `figure.file` is specified.
5. Speaker notes carry full evidence qualification and verbal explanation; they do not replace same-slide references.
6. For Chapter 1, the default is 16 slides, with 11 figures on Slides 3–13; generalize according to the provided manifest rather than hard-coding future slide counts.
7. Reopen and render slides. Reject clipping, overlap, low contrast, absent citations, and changed frozen wording. Record baseline text and notes digests.

**Output:** `*_stage1_text.pptx` + slide manifest + render preview.

## 4. Stage 2 — Standalone figure-by-figure science

**Command:** `Deck3 figures` or `Deck3 figures slide N`.

For each figure: (1) read the slide message/three points and active scientific authority; (2) choose one mechanism/question; (3) build an object and arrow register; (4) choose figure family (architecture, independent forcing lanes, candidate mechanism pathways, evidence-gap mind map, system/model boundary, VVUQ gates, services and bounded sustainability, chapter sequence); (5) generate **only the image asset**, not the complete slide; (6) visually inspect and verify source claims and math; (7) save original PNG/SVG and figure metadata.

**Scientific figure gate:** shared extreme heat alone ≠ proven two-way thermal coupling; candidate T_e→P chain needs grid-side **AC input** evidence; full T_e != active reduced subset; state != function/capability != service/resilience; sustainability requires separately qualified direct and intervention pathways. Never show fake numerical observations.

Do not add presentation-only disclaimers, extra presenter notes, or `CANDIDATE / OPEN` banners into the illustration when these have been expressly excluded from the visible design. Such statuses remain explicit in the manifest / scientific review and figure citation documentation.

**Output:** one source-named `Slide_NN_*.png` per intended slide, optional same-base SVG, per-figure QA record and source files. Existing approved figure assets must not be silently replaced.

**Important automation boundary:** The included Python helper does **not generate domain-correct scientific illustrations out of thin air**; the agent must actually draw/produce them, via original vector code or the appropriate image-generation tool, and verify each before Stage 3. If assets are missing, `Deck3 all` stops with an actionable missing-file report, not substituted clip art.

## 5. Stage 3 — Compose, verify, export

**Command:** `Deck3 assemble`.

1. Reopen Stage-1 PPTX and manifest.
2. For each designated slide, require the **exact file** listed in the manifest; do not guess a file path.
3. Verify SVG/PNG integrity, image dimensions and graphic provenance. Prefer PNG insertion in PowerPoint and keep SVG original separately.
4. Place each image in the specified region with **contain** fitting, centered, without distortion and without rewriting original textbox runs or notes.
5. Preserve citation/footer, frozen objectives, slide order and reference slides.
6. Assert exact Stage-1 vs final slide text and notes equality, expected picture count per slide, PPTX archive integrity, no images on forbidden slides, correct white interiors, and unchanged source figure hashes.
7. Render *every* slide and inspect at full and thumbnail scale. Programmatic geometric tests alone are not sufficient to assert there is no text overlap or scientific misinterpretation.
8. Deliver final PPTX, contact sheet/preview, Stage-1 PPTX if requested, and archived independent source graphics.

**Output:** `*_final.pptx` and QA JSON; a high-resolution preview is mandatory for presentation review.

## 6. Runnable orchestrator and manifest contract

- `examples/deck3.py`: generic and deterministic **Stage 1 / Stage 2 asset audit / Stage 3 / all** utility; no internet or fabricated domain data.
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

Only `kind=content` with `figure` reserves a figure. A long frozen objective can specify `"layout":"long_objectives"`. The generator may reject text that cannot fit safely and require adding a slide or a text-only layout; **never silently truncate frozen research content**.

## 7. Hard-stop gates, release checklist, and user-facing response

**Stop / fail:** missing source deck when asked to preserve it; missing graphic; evidence/claim mismatch; altered frozen text; changed full T_e system definition; fake numeric heat plots; wrong arrow/status meaning; any misplaced/cropped arrow or text; unresolved clipped-slide rendering.

**PASS checks:**
- file open/save/reopen; original notes and exact text preserved through assembly;
- correct independent figure for each designated slide;
- no image becomes a full-slide screenshot when the intent is supporting illustration;
- source aspect ratio unchanged; no box clipping;
- exact citation-to-claim mapping verified manually and by source registry;
- white panels, Times New Roman style, readable projection size;
- every designed scientific relation passes diagram and evidence gates.

**User response:** provide exact links to verified newly created files; record passes and limitations honestly. Do not say a physical model is validated because image generation, PPTX integrity checks, or numerical code tests passed.

## 8. Version

1.0.0 — 2026-10-09. Introduced single short-name three-stage reusable slide workflow. Older scientific-design skills remain authoritative; this skill only orchestrates artifacts and QA.
