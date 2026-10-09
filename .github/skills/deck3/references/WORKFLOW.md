# Deck3 — Three-stage scientific slide workflow

**One short name:** **Deck3**.  
Accepted chat inputs:
- `Deck3 text` / `Deck3 1`
- `Deck3 figures` / `Deck3 2`
- `Deck3 figures slide 6`
- `Deck3 assemble` / `Deck3 3`
- `Deck3 all`
- `Deck3 QA`

The assistant must use the user's actual approved deck/text/source files, not infer paths. This is an execution guide, not permission to invent literature, equipment limits, thermal coupling laws, or case results.

## Dominant scientific-figure layout — current user rule

For every **eligible figure-bearing slide**, the standalone scientific figure targets **75% of usable slide content area**, with an accepted **70–80%** range only after scientific/readability QA. The usable region is explicitly defined below the title/message header, above the citations/footer and inside slide margins. Meaningful artwork must visually occupy the region; a large blank PNG containing a small figure does not satisfy the rule. Title, outline, references and approved text-only/long-objectives exceptions do not require a figure.

- **Stage 1:** reserve an actually empty dominant region before text approval; retain exact native wording, three bullets where specified, citations and notes. Where content cannot fit the remaining 20–30%, stop for approval to split/re-layout. Do not shrink frozen objectives.
- **Stage 2:** design the infographic for the dominant slot aspect ratio and projection-scale legibility; no whole-slide screenshots, redundant slide title/three bullets, invented results, colored panel interiors or unqualified thermal arrows.
- **Stage 3:** preserve the Stage-1 source, contain-fit without distortion, compute achieved visible graphic/usable area, inspect each rendered slide, and block final release on illegible labels, overlap or evidence failure.
- **Current runtime limitation:** `examples/deck3.py` still has **legacy fixed small figure slots**. Merely adding this rule to the skill/manifest does **not** implement or verify new layout geometry. Update and test the authoring/assembly code or use a separately verified compliant slide layout **before claiming 75% QA PASS**. The earlier 16-slide Stage-1 deck and 10-of-11 provisional assembly are not retroactively compliant.

This is a **layout priority**, not permission to displace real scientific content, misrepresent measurements, falsify figure area with padding or violate the canonical source/citation requirements.

## Stage 1 — The exact text-only deck with deliberate whitespace

Inputs:
1. Actual approved slide content (or an approved source PowerPoint and extracted faithful manifest).
2. Frozen General Objective and SO1–SO3, exact canonical scope.
3. Verified author–date claims/citations and reference slides.
4. Slide-to-image selection and the active storyboards.

Output: 16:9 PowerPoint with native **Times New Roman** slide text (title, main message, three points, citation/footer, notes). Figures occupy empty reserved right-side areas, not boxes marked `INFOGRAPHIC PLACEHOLDER`. Outline, title, references need not include any figure. Long frozen objectives may use `layout=long_objectives`, with text extending in the full approved width.

Native helper:
```bash
python examples/deck3.py text \
  --manifest manifest.json --out output/stage1_text.pptx
```

**Critical:** do not overwrite a user-approved text source without explicit request; if no manifest exists, extract/write it **from actual source**, not an invented replacement. Make a visually readable review preview with the slide renderer.

## Stage 2 — Independently generated and checked illustrations

Inputs: frozen text/individual slide brief, system and citation authorities; optional existing approved images.

For each designated slide:
1. Ask which single scientific question the image answers.
2. Register all physical objects, member systems, interface variables and arrows (direction and **meaning**).
3. Choose scientific diagram family: architecture / external forcing / candidate mechanism / evidence-gap mind map / RQ traceability / frozen-objective outcomes / full system vs reduced model / VVUQ workflow / physical-to-service outcomes / two-pathway sustainability / chapter roadmap.
4. Draw only the **standalone illustration**. No slide title, three bullets or presenter-only callouts in the image.
5. Cite scientific evidence with exact verified author–date where needed; preserve a longer provenance record externally.
6. Inspect pixel-level readability at *the final inserted image size*. Prefer original vectors and Times New Roman label declarations.
7. Save `Slide_NN_*.png` plus corresponding SVG/source when available, and a source/arrow/QA register.
8. Do not overwrite previously approved assets unless specifically asked.

Existing source code in this repo:
- `../scientific-infographic-design/examples/figures.py` — three example SVG scenes;
- `../scientific-infographic-design/examples/pptx_builder.py` — independently editable three-slide PPTX prototype;
- `../scientific-infographic-design/references/CHAPTER1_FIGURE_STORYBOARD.md` — 16-slide routing;
- `../scientific-infographic-design/examples/WORKED_FIGURE_RECIPES.md` — semantics and evidence gates.

Audit actual delivered PNG files:
```bash
python examples/deck3.py figures \
  --manifest manifest.json --figures approved_figures/ \
  --report output/figure_asset_report.json
```
Or only one:
```bash
python examples/deck3.py figures \
  --manifest manifest.json --figures approved_figures/ --slide 6
```

**Limit:** This CLI validates PNG presence, pixel readability minimum, hash/provenance identity and mapping. It does NOT generate scientific content automatically. The agent must actually create/check assets before Stage 3.

## Stage 3 — Lossless integration into original slide structure

```bash
python examples/deck3.py assemble \
  --manifest manifest.json \
  --text-pptx output/stage1_text.pptx \
  --figures approved_figures/ \
  --out output/final.pptx \
  --qa output/composition_qa.json
```

Guaranteed by the implementation, subject to tests:
- exactly one PNG on each requested slide, zero elsewhere;
- correct image-to-slide mapping from manifest;
- *contain fit* preserves image aspect ratio; no forced stretching;
- all original native editable textboxes still present, **exact slide text strings** unchanged;
- source speaker notes unchanged;
- speaker notes are not visible disclaimer banners inside illustrations;
- PowerPoint can be reopened as an intact ZIP archive;
- figure SHA-256 hash recorded.

Must be verified separately by actual render/inspection:
- projection-size readability of objective wording and citations;
- image does not cover text on irregular/custom layouts;
- title/reference slides remained clean;
- scientific arrows are correct, data provenance is defensible;
- line styles have stable engineering meaning;
- no label clipping, font substitution, low contrast or semantic ambiguity.

## All stages from one request

```bash
python examples/deck3.py all \
  --manifest manifest.json \
  --figures approved_figures/ \
  --output-dir output/
```

`all` first generates text-only PPTX, then audits all figure files, then assembles. **When figures are missing, it intentionally stops after Stage 1** and identifies the missing slide/image; the design agent must create the independently verified assets before re-running it. The workflow does not silently substitute placeholder pictures.

For a conversational `Deck3 all` request, the assistant actively designs figure assets one by one (using the available image-generation/vector tools), rather than waiting for the user to supply them if inputs and tool capabilities permit.

## Three scientific invariants and prohibited visual shortcuts

1. **Full Electrified Transportation System** includes road EV, RESS, propulsion and auxiliary electrical systems, vehicle power-supply circuit, EVSE, physical charge connection and necessary communication/control; the selected active thermal-model subset is not the whole system.
2. **Shared external heat** affects both P and T_e independently unless cross-system causality is qualified; a double-headed arrow does not establish bidirectional thermal physics.
3. **Service-level analysis** distinguishes physical state, functional capability, service, resilience and separately bounded sustainability. A thermal state or reliability metric is not automatically a mobility service outcome.

No numerical plots without admitted equations/data. No gold, colored panels or gray interior backgrounds. Use white/black with restrained border/line accents and clear arrows. Evidence status can remain in notes when presenter-only status badges are deliberately removed, but the diagram must not falsely claim validation.

## Expected acceptance format

```text
Deck3 stage: text | figures | assemble | all
Input authority: <repo paths and actual deck path>
Accepted science: <what the evidence supports>
Figure slots: slide numbers
Scientific blockers: OPEN if not verified
Files: existing, verified paths
QA: source text unchanged? notes unchanged? citations adjacent?
Visual review: preview inspected? labels/clipping?
Release: PASS / BLOCKED / PROVISIONAL
```

**Reusable scope:** Chapter 1 is one example; these steps apply to thesis defense decks, conference posters converted to slide presentations, future chapters, and other scientific talks when their own manifests and scientific authorities are supplied.
