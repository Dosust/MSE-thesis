# Original Figure Reference → Practical Design Decision Guide

**Purpose:** Translate verified *published visual-design precedents* into explicit figure decisions for a power–electrified transportation thesis. This is **a design-method reference**, not a source of engineering thermal laws or case data.

**Primary references:** Jambor & Bornhäuser (2024), *PLOS Computational Biology*, https://doi.org/10.1371/journal.pcbi.1011789 ; Rougier, Droettboom, & Bourne (2014), *PLOS Computational Biology*, https://doi.org/10.1371/journal.pcbi.1003833 ; Jambor (2025), *Nature Cell Biology*, https://doi.org/10.1038/s41556-025-01684-z ; Oliverio & Wright (2025), *FEBS Letters*, https://doi.org/10.1002/1873-3468.70163 .

## Reference 1: Jambor & Bornhäuser Fig 5 — Match layout to relationship
Original: https://doi.org/10.1371/journal.pcbi.1011789.g005

**Meaning:** Linear, circular, parallel and nested arrangements have different reading implications.

**Use when:** selecting an infographic before drawing arrows, especially Slides 2, 4, 7, 8, 9, 10, 12.

**Worked selection:**
- Slide 4 question: "Does the same ambient heat condition create thermal responses in two systems?" → **parallel lanes**.
- Slide 9 question: "What belongs to each system, and what subset is actively modeled?" → **two disjoint enclosures** for P and T_e; smaller active-model outline within the appropriate system(s).
- Slide 10 question: "What must be completed before model evaluation?" → **linear method gates**.
- Slide 12 question: "Which assessment outcomes are distinct?" → **forked branches** after a shared service-consequence object.

**Wrong:** displaying P and T_e as overlapping circles because they are related; circular sequence for an analysis that has no scientific cycle.

**Success check:** swap one layout for another. If scientific meaning changes, the selected topology is informative.

## Reference 2: Jambor & Bornhäuser Fig 6 — Arrow purpose is context dependent
Original: https://doi.org/10.1371/journal.pcbi.1011789.g006

**Use when:** any figure has arrows beyond a single transfer mechanism.

**Worked example:**
- Slide 3 P → T_e label: "**Electricity supply**" (physically transferred real/electrical power).
- Slide 3 T_e → P label: "**Charging-load influence**" (an effect on grid loading, **not** electrical V2G export unless supported).
- Slide 4 external heat → P and heat → T_e: "**Heat forcing**".
- Slide 5 P thermal constraint → charging effect: "**CANDIDATE; operational limit and charging response to qualify**".
- Slide 10 Evidence → Qualification: **method-workflow progress, not a thermal transfer**. Put "Method workflow" in legend.

**Wrong:** use the same double-arrow to mean electrical energy, thermal feedback, supervisory command, and research sequence. **Never define dashed as uncertainty** when the existing engineering skill assigns dashed to control.

**Success check:** every arrow has source, destination, typed meaning, quantity/verb, proof/status and adjacent domain citation where externally supported.

## Reference 3: Rougier et al. Fig 3 — One message, medium-specific rendering
Original: https://doi.org/10.1371/journal.pcbi.1003833.g003

**Use when:** a thesis figure has too many annotations for projection.

**Worked example:** For a paper, a detailed transformer thermal diagram may show equations, parameters, symbols and assumptions. For Slide 4, retain exactly the supported relationship **external forcing → admitted physical thermal state → capability**, make the equipment label prominent, place derivation in speaker notes, and keep the source note on the slide.

**Wrong:** deleting the word \`candidate\`, a critical boundary, or a source note to achieve visual simplicity. Simplicity can never strengthen an external scientific claim.

**Success check:** compare all modeled variables, physical directions and status labels before/after reduction. No changed or invented science.

## Reference 4: Rougier et al. Fig 7 — Many views versus one occluded view
Original: https://doi.org/10.1371/journal.pcbi.1003833.g007

**Use when:** comparing baseline, extreme heat and engineering response **once real comparable data and defined service metrics exist**.

**Worked example:**
- top: Power service \(Q_P(t)\) for three admitted cases;
- bottom: mobility service \(Q_T(t)\) for the **same** experiment horizon;
- within each panel, comparisons use aligned units and reference requirements.
- if the units differ between services, do not share a y-axis; preserve comparable time.

**Wrong:** put temperature, SOC, charging current, and mobility performance on one unlabelled multi-axis chart or invent aesthetically pleasing heat curves.

**Success check:** sources, axis units, scenario definitions, uncertainty, and case comparability are shown.

## Reference 5: Jambor & Bornhäuser Fig 1 — Sketch → draft → final
Original: https://doi.org/10.1371/journal.pcbi.1011789.g001

**Use when:** launching any new high-impact infographic, especially the first architecture/thermal/mechanism prototypes.

**Worked example:**
1. "System boundary, not proven dependency" is the one-sentence message.
2. Element register identifies P, full T_e, electrical interface, optional candidate dependency.
3. Wireframe shows only two white enclosures and explicitly labeled exchanges.
4. Editable SVG/PPTX and citations are produced.
5. Semantic tests and screenshots are inspected before slide release.

**Wrong:** send a generative model an aesthetic prompt and then decide the physics from the resulting image.

**Success check:** an independent reader can map visible objects back to the element/relation register.

## Reference 6: Rougier et al. Fig 6 — Prevent misleading quantitative encoding
Original: https://doi.org/10.1371/journal.pcbi.1003833.g006

**Use when:** adding any perceived magnitude, value, risk, delay, color intensity, line length or area.

**Worked example:** Do not scale a transformer rectangle proportional to assumed "criticality" without a registered metric and rule. A crossing of an admitted service threshold must be drawn with the real threshold and exact crossing calculation, not approximate eyeballing.

**Wrong:** an impressive-looking thicker red line means "strong coupling" without an operational definition; a toy plot looks like field data.

**Success check:** each quantitative graphical encoding is a documented function of a verified/specified quantity, or the whole figure is marked **CONCEPTUAL / NOT TO SCALE**.

## Reference 7: Jambor & Bornhäuser Fig 2 — Consistent icon style
Original: https://doi.org/10.1371/journal.pcbi.1011789.g002

**Use when:** schematic physical equipment icons help explain system membership.

**Worked example:** One vector-line icon family, consistent strokes, black text, blue border P, green border T_e, no decorative vehicle art. Preserve the complete system inventory in the technical source note if the main slide labels are compressed.

**Wrong:** mismatched AI photorealistic transformer beside emoji-style EV and clip-art cloud. **License warning:** original Fig 2 includes third-party icon attributions; do not copy such icons without checking specific licenses.

## References beyond the original top six

### Jambor (2025), Figures 1–3: Figure QA checklist
Publisher: https://doi.org/10.1038/s41556-025-01684-z

**Use:** final review checklist for message clarity, accessibility, and feedback iteration. **Do not** copy copyrighted publisher figure assets unless licensed.

### Oliverio & Wright (2025), Figures 1–2: Layout and reading direction
Publisher: https://doi.org/10.1002/1873-3468.70163

**Use:** top-to-bottom/left-to-right hierarchy, with clarity on whether arrows express reading guidance rather than physical mechanisms. In this repository, use position/numbering for reading order and reserve **scientific arrows for real declared relations**.

### Wong (2011): Redundant visual encoding, beyond color alone
Sources: https://doi.org/10.1038/nmeth.1618 and https://doi.org/10.1038/nmeth.1642

**Use:** show Power/Transportation via labels and enclosures in addition to distinct border colors; evidence status appears in words. Check in grayscale.

## Figures and licenses are not interchangeable

The PLOS articles include open-access licensing information; individual third-party icon/figure assets can carry additional rights. Original author-created Fig 1 drawings in Jambor & Bornhäuser are specifically described as CC0 in their caption. Publisher-hosted Nature figures and commercial templates are **view-and-learn only** unless explicit reuse rights are confirmed. Original editable thesis shapes are safest.

## Scientific-domain citations must be separate

Examples of evidence sources for the *thesis's physics* (not design):
- Qian et al. (2015), DOI: https://doi.org/10.1016/j.ijepes.2014.09.040 — EV charging and transformer thermal-aging conditions.
- Visakh & Selvan (2023), DOI: https://doi.org/10.1016/j.segan.2023.101096 — relevant transformer/EV charging/service-disruption prior art.
- Krama et al. (2026), DOI: https://doi.org/10.1016/j.ecmx.2026.101960 — one equipment- and climate-specific charging thermal study.
- IEEE C57.91-2025 — transformer thermal-loading guide; edition/clause-level claims must be checked.

Each cited scientific statement needs **adjacent accurate in-text citations**. None of these citations validates an entire bidirectional thesis mechanism automatically.
