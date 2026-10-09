---
name: scientific-infographic-design
description: Convert scientific claims, presentations, chapter introductions, research problems, literature comparisons, and evidence-grounded engineering content into original, accessible, editable infographics. Select the correct visual family, declare system and model boundaries, register meaningful arrows and evidence status, keep adjacent scientific citations, and run scientific, visual, accessibility, and PowerPoint QA. Use for science-presentation infographic redesign, graphical abstracts, mechanism figures, comparison matrices, research workflows, and cited thesis slides; defer formal framework semantics to engineering-framework-design and diagram grammar to scientific-diagram-design.
license: MIT
metadata:
  version: "2.1.0"
---

> **Presentation orchestration shortcut:** For a three-stage PPTX task use `Deck3 text`, `Deck3 figures`, `Deck3 assemble`, or `Deck3 all` via `../deck3/SKILL.md`. This scientific-infographic skill remains authoritative for **scientific figure meaning, scene registers and figure QA**, while Deck3 manages stage dispatch, reserved blank spaces and lossless assembly. A standalone infographic is not a screenshot of the entire PowerPoint slide.

# Scientific Infographic Design — Evidence-First Presentation Agent

## 0. Mission, precedence, and activation

Turn a supported **scientific message** into an original explanatory figure that can be understood at presentation size *without claiming more than the evidence proves*. This is not a decorative slide-template generator.

Use for scientific infographics and presentation/graphical-abstract figures. For formal systems-engineering framework specification, **load and obey** `.github/skills/engineering-framework-design/SKILL.md`. For element/relationship semantics and exact mathematical figures, **load and obey** `.github/skills/scientific-diagram-design/SKILL.md` and, when needed, `.github/skills/mathematical-visualization-design/SKILL.md`. This skill governs **visual compression and communication**, not the truth of a physical mechanism.

For this repository, always read in order:
1. `AI_RESEARCH_INSTRUCTIONS.md`;
2. `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`;
3. `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`;
4. `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md`;
5. relevant frozen scientific scope/system/definition/objective files.

Never change the thesis title, frozen objective wording, full Electrified Transportation System composition, or extreme-heat thermal-only scope when simplifying graphics. A model subset is not the full system definition.

## 0A. Dominant figure scale on Deck3 slides — current user rule

When this infographic skill is used for an **eligible Deck3 figure-bearing slide**, the standalone scientific figure must be designed for approximately **75% of the usable below-title content region** (70–80% acceptance band with verified readability and truthful layout). See `../deck3/SKILL.md` §2A for the exact denominator, meaningful-content occupancy, exemptions and rejection rules.

- Compose for the **actual final PPTX slot aspect ratio**, not arbitrary landscape proportions; keep the artwork scientifically minimal but make core mechanisms, labels, equations and large directional arrows **readable at presentation size**.
- Figures remain **standalone assets** and must **not** absorb/replace the editable slide title, approved main message, exactly three native slide points or visible scientific source credits merely because the graphic is larger.
- Strict white canvas and white box interiors. Restrained color only for semantic arrows, borders, headings, line series and small accents. Do not use colored/gray fills, decorative gradients or shadows.
- Occupancy is not a pretext to invent extra states, causal arrows, temperature limits, output curves, literature evidence or decorative icons. Shared forcing is not interdependency; an unqualified candidate must never appear validated.
- A figure failing scientific integrity or projection legibility **fails regardless of spatial share**. White filler margins or image-container dimensions alone cannot be counted as meaningfully occupied infographic area.
- Text-intensive frozen objectives require a valid text-only/companion layout when 75% occupancy would destroy legibility; do not paraphrase exact objective wording as a figure.
- **Implementation note:** legacy `deck3.py` slots do not yet meet this rule; do not claim assembled occupancy validation until geometry and tests have been updated or independently verified.

## 1. Peer-reviewed design evidence

Design method is grounded in:
- **Jambor & Bornhäuser (2024)**, *Ten simple rules for designing graphical abstracts*, https://doi.org/10.1371/journal.pcbi.1011789 — Figs 1 (sketch → draft → final), 5 (purposeful layouts), 6 (arrow ambiguity), and 2 (consistent pictograms).
- **Rougier, Droettboom, & Bourne (2014)**, *Ten Simple Rules for Better Figures*, https://doi.org/10.1371/journal.pcbi.1003833 — Figs 3 (paper vs oral presentation), 6 (misleading scales), 7 (clutter vs small multiples).
- **Kosslyn et al. (2012)**, https://doi.org/10.3389/fpsyg.2012.00230 — perceptual/cognitive presentation flaws.
- **Wong (2011)**, *Color blindness*, https://doi.org/10.1038/nmeth.1618; *Avoiding color*, https://doi.org/10.1038/nmeth.1642 — redundancy beyond hue.
- **Fujii (2026)**, *How to design effective scientific figures*, https://doi.org/10.1038/s41562-026-02466-9, Fig 1 — message, audience, chart form, iteration; figure visible on publisher page, full article may be subscription only.
- **W3C WCAG 2.2**, https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html — required graphical objects at least 3:1 contrast.
- **Microsoft PowerPoint accessibility**, https://support.microsoft.com/en-us/accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities — reading order, alt text, titles, contrast.

Consult `references/FIGURE_REFERENCE_LIBRARY.md` for selected original figure links and **what can be learned**, not what should be copied. Do not confuse these visual-design sources with scientific evidence for domain-specific physics.

## 2. Required figure contract — before drawing

For **each** infographic prepare:

```yaml
slide_number:
slide_title:
audience:
one_main_message:
one_question_figure_answers:
figure_family:
internal_scope_authority:
physical_systems_and_boundaries:
elements_and_semantic_types:
directional_relationships:
  - source:
    target:
    transfer_or_mechanism:
    arrow_semantic_class:
    evidence_status: # ESTABLISHED / THESIS-DEFINED / CANDIDATE / OPEN
    adjacent_citation:
state_and_time_meaning:
service_consequences:
prohibited_visual_implications:
visual_layout:
visible_source_note:
speaker_note_detail:
output_format:
accessibility_and_QA:
```

If evidence for a claimed directional dependency is OPEN, either show it explicitly as a **candidate** with its gate or omit it. A decorative arrow is prohibited.

## 3. Scientific figure family selection

| Actual question | Figure family | Never confuse with |
|---|---|---|
| What belongs to the system? | **separate enclosing boundaries / architecture view** | operational/service boundary condition |
| What external factor acts on the equipment? | **parallel forcing → state → capability lanes** | proven cross-system coupling |
| How might a source influence a receiver? | **directional, source→constraint→interface→receiver mechanism lane** | association or shared exposure |
| Which mechanisms have evidence? | **source-by-claim / qualification matrix** | unjustified all-or-none novelty claim |
| What remains to be studied? | **established→documented limitation→bounded handoff→proposed test** | “nobody has done this” |
| Which objective leads to what output? | **objective-to-output traceability** | boxes whose links are arbitrary |
| What happens with state and time? | **state-time timeline/trajectory with admitted thresholds** | invented measured/simulated data |
| How does research advance? | **evidence/qualification/model/VVUQ workflow with gates** | physical causal flow |
| What outcome is delivered? | **physical state → capability → service → service-based resilience** | state = service |
| How compare response consequences? | **side-by-side cases / two-pathway assessment** | automatically beneficial sustainability |
| How explain many series? | **small multiples / aligned comparison** | rainbow/3D/clutter charts |

Prefer **one principal figure family per slide**. Avoid turning a formal architecture into an infographic with untraceable arrows.

## 4. Arrow grammar and evidence status must be orthogonal

**Never silently redefine a line style that the active framework/diagram skill already assigns a semantic meaning.** Default repository grammar:

- solid direction: physical or information transfer;
- heavy direction: justified cause/effect propagation;
- dashed: control/intervention;
- dotted return: observation/feedback;
- thin non-directional line: membership/association;
- bidirectional: only where the two separate directions are individually justified.
- If the graphic is solely a *method workflow*, declare a distinct methodological-process grammar/legend; do not imply a physical conservation flow.

**Evidence status is a separate textual attribute, never encoded by dash style alone:**
`ESTABLISHED`, `THESIS-DEFINED`, `CANDIDATE — qualification required`, `OPEN — source verification required`.

For every arrow record source, target, actual mechanism/exchange, direction, arrow class, evidence status, and adjacent source. A two-headed P↔T_e identity symbol denotes the *investigation scope* only if expressly labeled; it must not be presented as proven bidirectional thermal physics.

## 5. Visual grammar and accessibility

- Exact **white #FFFFFF background and white box/panel interiors**. No gray/off-white tints, filled colored cards, gradients, shadows, gold, textures, or invented visual effects.
- Use **black text**. Allow controlled semantic color for borders, headings, large arrows, and small accents only. Thesis profile defaults: blue=Power, green=Electrified Transportation, muted red=external extreme heat; always label components in text.
- No mini arrows. Every arrow must be thick/large enough to be understood at slide scale.
- Consistent typefaces, aligned margins, whitespace, label placement, line widths, and diagram icon family.
- Do not rely on hue to differentiate components/directions/status. Verify grayscale meaning and color-vision accessibility (Wong, 2011).
- Important graphical lines/icons must be distinguishable (WCAG non-text 3:1 criterion); use adequate text contrast and legible projection typography.
- Prefer editable PowerPoint shapes/text and vector SVG export. Native shapes are the default for boundary/arrow/evidence workflows.
- **No invented data trajectories, thresholds, temperature figures, derating curves, plots, equations, validation findings, or numerical service deficits.** Conceptual shapes/axes must say `CONCEPTUAL / NOT MEASURED` if interpretation otherwise ambiguous.
- A caption/source note is part of the scientific figure, not an optional footer.
- For slides, use compact adjacent APA author–date citations to externally supported claims; a final reference list alone **fails**.

## 6. Design pipeline (non-optional)

1. **Read authority and evidence:** establish what the exact literature supports, full-system boundary, active model subset, and OPEN items.
2. **Distill the one-sentence message:** reject “show resilience” / “draw systems” as insufficient.
3. **Select figure family:** choose based on the scientific question and audience, not aesthetics.
4. **Draft a storyboard:** arrange correct objects/lanes/boundaries and register arrows and evidence status.
5. **Prototype a black/white layout:** hierarchy, negative space, arrows; test that grayscale-only still reads correctly.
6. **Add semantic accents and citations:** source metadata verified, exact claim-source match, meaningful arrow labels.
7. **Render editable artifact:** use deterministic geometry whenever feasible; speaker notes carry derivations and extended context.
8. **Run four hard QA gates:** scientific truth, citation/evidence, visual meaning, accessibility/technical integrity. If blocked, explicitly report `BLOCKED / OPEN`.
9. **Render/review at multiple scales:** native 16:9 and thumbnail; inspect clipping, label collision, genuine arrow direction, and reading order; correct before delivery.

Jambor & Bornhäuser (2024) Fig 1 is a precedent for iterating from rough structure to usable figure, NOT permission to trace its artwork. Rougier et al. (2014) Fig 3 specifically motivates simplifying oral-presentation views without changing the underlying scientific message.

## 7. Thesis-specific non-negotiables

The two physical systems are the **Power System P** and the full canonical **Electrified Transportation System T_e**. The latter includes electrically propelled road vehicle, RESS, propulsion/auxiliary electrical systems, vehicle power-supply circuit, EVSE, physical connection, and communication/control needed for power transfer (bidirectional where supported). EVSE is not a third infrastructure. `System Boundary` is not a mathematical `Boundary Condition`.

Extreme heat is an **external forcing**; its separate effects on P and T_e do **not** independently prove thermal interdependency. For each candidate P→T_e and T_e→P direction, show an evidence gate and label admission status. A decreased EVSE DC charging output does not by itself establish the sign, shape, or timing of upstream AC input change; qualified equipment and measured/defensible interface behavior are required. Physical state, thermal capability, electricity/mobility service, resilience, and sustainability are distinct objects. Critical state-transition time, propagation delay, service-consequence time, and recovery time cannot be conflated.

Keep frozen GO and SO1–SO3 **verbatim**. Final RQs/hypotheses, component models, equipment cases, numerical thresholds, validation results, and exact novelty remain OPEN until admitted under the current canonical authorities.

## 8. Chapter 1 figure-routing guide

Use `references/CHAPTER1_FIGURE_STORYBOARD.md` as the figure-by-figure plan for the active 16-slide introductory presentation. Source-specific design citations belong with that storyboard; domain physics literature is assessed separately for each scientific claim.

## 9. Failure cases and hard stop

FAIL and revise if any figure:
- shows gray or tinted interior/background without explicit user permission;
- silently narrows full T_e to EVSE alone;
- promotes a proposed thermal interaction to an established mechanism;
- uses dashed arrow to mean uncertainty when that style is already reserved for control;
- adds arrows for decoration or reading order alone;
- puts a method workflow arrow in the physical-causation grammar without explanation;
- has bibliography-only citations without adjacent domain-claim attribution;
- shows measured-looking curves or numerical thresholds with no source;
- merges resilience and sustainability or claims response automatically improves both;
- cannot be edited when the deliverable requires editable diagrams;
- clips any label, equation, source note, or crucial boundary;
- borrows protected figures/artwork without permission and attribution.

## 10. Verification fixtures

**Fixture A — Parallel extreme-heat exposure (Chapter 1 Slide 4):**
`heat [outside] → P thermal state → P capability` and independently `heat [outside] → T_e thermal state → T_e capability`. PASS only if *no thermal P↔T_e coupling is inferred*. Cite a transformer thermal source and a charger-specific heat response source on the respective lanes.

**Fixture B — Directional mechanisms (Slide 5):**
Two lanes, P→T_e and T_e→P, with separately specified source thermal state, thermal constraint, power-transfer interface, receiver response, time consequence, and evidence gate. PASS only if missing data are labeled CANDIDATE or OPEN; no fake two-way feedback loop or inferred AC electrical response.

**Fixture C — System boundary (Slide 9):**
Show full T_e scope, separate P scope, explicit electrical interface, and a smaller **active model subset** drawn as a different enclosing boundary. PASS only if EVSE remains part of T_e and mobility service is an output, not a physical component.


## 10A. Which skill does what? — task router with concrete invocation examples

| User intent / example request | Primary skill | Companion | Deliverable | Why |
|---|---|---|---|---|
| "Define the power–transport system architecture" | \`engineering-framework-design\` | \`scientific-diagram-design\` | Semantically registered boundary/interface diagram | Physical ownership and interfaces must be correct before visual styling |
| "Design Slide 3 as an infographic" | **this skill** | engineering + scientific diagram | Slide storyboard + editable figure | Simplify a verified architecture for an audience |
| "Show extreme heat and its effects" | scientific diagram + **this skill** | engineering | Two independent thermal lanes | Separates common forcing from cross-system coupling |
| "Explain candidate P→T_e and T_e→P effects" | engineering + scientific diagram | **this skill** | Two explicitly qualified mechanism lanes | The paths need independently justified interfaces |
| "Create mathematical threshold or propagation figure" | \`mathematical-visualization-design\` | scientific diagram + **this skill** | Defined formula/variable semantics + mathematical visual | Geometry/trajectory must arise from a mathematical model or be explicitly schematic |
| "Write rigorous Python generating a research figure" | \`mathematical-visualization-design\` | this skill | Reproducible program, tests, SVG/PPTX | Code is an implementation of a declared model/diagram contract |
| "Create/update my Chapter 1 PowerPoint" | **this skill** | figure and math skills as needed | Editable slide deck, citations, notes, QA | Audience-level figure composition differs from a journal manuscript |
| "Review an image and improve its design" | \`scientific-diagram-design\` | this skill | Semantic QA, change log, revised artwork | Correct symbols, arrows and boundaries before enhancement |
| "Create mathematical animation or interactive state trajectory" | mathematical visualization | scientific diagram | Model-driven animation + units/time controls | Time, motion and colors must encode computed quantities |
| "Construct a literature research-gap matrix" | **this skill** | evidence/citation authorities | Exact prior-art evidence matrix | Avoid unsupported novelty claims and citation laundering |

**Mandatory routing order:** (1) canonical research authority; (2) object/arrow semantics; (3) figure family and audience; (4) deterministic generation; (5) citation and rendering QA. The router can combine skills but must never treat the graphic as evidence.

### Examples of user prompts the agent must handle

**A. Systems infographic**
> Use the frozen P/T_e composition to draw two distinct white-bordered systems. Show \`P→T_e\` electricity supply as an actual electrical exchange and \`T_e→P\` charging-load influence as a different causal quantity. Keep any thermal interactions explicitly unqualified. Add an APA citation and editable-PPTX shapes.

**B. Scientific mechanism**
> Create two separate candidate thermal-interdependency mechanism lanes. For each arrow provide source, receiver, exchanged/conditioned quantity, case admission status and a verification gate. Never use \`↔\` as proof.

**C. Mathematical coding**
> Define a mathematical quantity and admissible input data, write tested Python calculating it, render a labeled SVG, and explicitly distinguish measured results, a synthetic unit test and a schematic illustration. Do not fabricate equipment parameters.

**D. Presentation conversion**
> Preserve the exact frozen General Objective and SO1–SO3. Convert each text-heavy slide to one scientific message with traceable labels, same-slide citations, speaker notes, and editable vectors. Render/check every slide.

## 10B. Precisely how to learn from each ranked figure

The \`FIGURE_REFERENCE_LIBRARY.md\` records **original sources** and not domain evidence. Apply the following six worked interpretation rules (Jambor & Bornhäuser, 2024; Rougier et al., 2014):

| Reference figure | Use **when** | Example for this thesis | Why this figure family works | Never transfer |
|---|---|---|---|---|
| Jambor & Bornhäuser **Fig 5, layout families** | Need to choose linear vs parallel vs nested arrangement | Slide 4 uses **parallel** heat-response lanes; Slide 9 uses separate system boundary with a smaller selected model subset | Topology of communication follows scientific relation | Their biology icons or exact arrangement |
| Jambor & Bornhäuser **Fig 6, arrows** | One graphic contains different types of connection | Slide 3 uses physically labeled electrical transfer and separately labeled loading effect; Slide 5 uses candidate directed mechanism | Prevents arrow meaning from drifting between panels | Source-domain arrows or an arrow style conflicting with engineering skill |
| Rougier et al. **Fig 3, paper vs oral display** | Converting manuscript figure into lecture slide | Keep exact scientific states and directions; simplify secondary labels and move full derivation to speaker notes | Presentation needs different information density | Removing assumptions or citations to make the image look cleaner |
| Rougier et al. **Fig 7, small multiples** | Comparing several cases/time traces | Matched baseline/heat/response services on separate aligned axes, **only after real case data exist** | Improves comparison without plot occlusion | Synthetic numerical service trajectories masquerading as observed results |
| Jambor & Bornhäuser **Fig 1, sketch→draft→final** | Before coding any complex figure | First author registers, then wireframe, then editable PPTX, then screenshots and corrections | Catches semantic problems before styling | Tracing their visual geometry |
| Rougier et al. **Fig 6, misleading encodings** | Showing thresholds, magnitudes, trade-offs, uncertainty | Service comparison must use declared units, scales, baseline and uncertainty where appropriate | Prevents visual inflation of differences | Arbitrary node size for risk/criticality |

Extended source-to-design examples, failure cases, citations and exact article links: \`references/FIGURE_DESIGN_APPLICATION_GUIDE.md\`.

**Reference trust boundary:** a graphical abstract figure teaches *design grammar only*. It is not evidence for a transformer limit, EV charging thermal law, state trajectory, research gap, resilience metric or standard scope.

## 10C. End-to-end recipe for every new scientific slide

**Input contract:** source slide or chapter section; frozen scientific scope and wordings; audience; cited evidence; active vs excluded elements; expected output format.

**Step 1. Claim inventory.** Separate \`EVIDENCE\`, \`CANONICAL INTERNAL\`, \`PROPOSED/T1\`, \`OPEN\`. Attach appropriate source/authority to each. A fact remains OPEN if a DOI exists but does not support the exact assertion.

**Step 2. Figure question.** Write precisely one question, e.g. "Does common heat exposure alone imply coupled thermal interdependency?" Answer: **No** (internal frozen qualification rule).

**Step 3. Formal scene graph (no drawing yet).** Register every physical system, boundary, interface, forcing, state, capability, function, service and optional comparison. Require correct ownership.

**Step 4. Relation register.** Every arrow records \`(source, target, relation kind, exchanged quantity/meaning, direction, evidence status, citation, admission gate)\`.

**Step 5. Pick original figure family.** Use Fig 5's principle: separate comparison vs temporal chain vs containment; not every slide is a left-to-right process.

**Step 6. Write a storyboard/brief.** Create exact approved labels, short title, main claim, legend, citation placements, expected speaker notes, prohibited implications, contrast requirements.

**Step 7. Draw deterministic editable geometry.** Use native shapes and connectors for PPTX; use SVG/TikZ for journal/vector views; data-driven charts only when data provenance exists. If rasterization is unavoidable, retain vector original and explicitly record the loss of editability.

**Step 8. Mathematical verification for all numerical figures.** Check equations, units, time domain, data provenance, assumptions, physical bounds, independent validation status, interpolation definition and plots against underlying array values. A schematic is labeled \`CONCEPTUAL — NOT MEASURED\`.

**Step 9. Source QA.** Validate each same-slide author–date source and reference list entry; internal canonical decisions receive version/path attribution, not irrelevant external literature.

**Step 10. Render QA.** Inspect slide-native size and thumbnail; measure clipping, overlap, readability and directional arrows; ensure white panel interiors and accessible contrast. Re-render changed slide.

**Step 11. Record reproducibility.** Save script, input fixture, source register, figure spec, output artifact, test results, software dependency versions and known limitations.

## 10D. Mathematical coding contract

A scientific graphic generated by code requires a **model contract**:

\`\`\`text
SCIENTIFIC CLAIM / QUESTION
→ CANONICAL OBJECTS + SOURCE AUTHORITY
→ EXACT MATHEMATICAL VARIABLE DEFINITION / UNIT / DOMAIN
→ ADMISSIBLE DATA + DATA PROVENANCE
→ GOVERNING EQUATION OR THESIS-DERIVED FORMULA (T1 IF NEW)
→ ASSUMPTIONS AND INITIAL / BOUNDARY CONDITIONS
→ NUMERICAL IMPLEMENTATION AND ALGORITHM
→ VERIFICATION TESTS (including edge cases)
→ VALIDATION / INDEPENDENT PHYSICAL EVIDENCE (if claimed)
→ VISUAL ENCODING
→ CAPTION + ADJACENT CITATIONS
→ EDITABLE VECTOR / PPTX + RENDER INSPECTION
\`\`\`

Examples of legitimate \`state-time\` metrics (definitions are conditional and case-specific, not frozen equipment limits):

- **First passage to a declared threshold** \(\tau=\inf\{t\ge t_0:g(X(t),t)\le 0\}\); specify existence, event direction, numerical interpolation, units and sampling resolution.
- **Propagation delay** \(\delta_{i\rightarrow j}=\tau_j^{\mathrm{response}}-\tau_i^{\mathrm{source}}\); may be interpreted only when those two events and the causal link are independently defined and the event ordering is compatible.
- **Service gap** \(D_k=\int_{t_0}^{t_1}[Q_k^{\mathrm{req}}(t)-Q_k(t)]_+\,dt\); specify service units, time units, common horizon and reference requirement. Do not equate this integral automatically with resilience.
- **Model object** \(X_{\mathrm{th}}(t)\) means only the admitted thermal-state vector; do not automatically insert interface \(Z(t)\) as a state without dynamics.

Never pass off sample threshold \`0.5\`, arbitrary temperature \`40 °C\`, or time \`2 h\` as a case-specific physical parameter. Examples may use **dimensionless synthetic test arrays** only when labels and captions explicitly identify them as software tests, NOT case physics.

**Implementation examples:**
- \`examples/figures.py\`: runnable deterministic **pure-Python SVG diagram generator** with three Chapter 1 example scenes; does not need external datasets; all labels/citations contained in the script.
- \`examples/mathematical_metrics.py\`: runnable, tested **dimensionless numerical metric functions** with validation/edge-case guards and an explicitly synthetic example; no device-specific thresholds.
- \`examples/pptx_recipe.md\`: how to turn an admitted scene graph into editable PowerPoint shapes and verified slides, with source/notes/read-order checks.
- \`examples/WORKED_FIGURE_RECIPES.md\`: step-by-step from literature claim to figure objects, arrows, caption and hard-stop tests.

## 10E. Code-generator instructions

If the user asks "write the code," return executable code, not only a prompt. Prefer standard-library SVG or a deterministic PowerPoint library according to target. Code must:

1. define a typed/structured **element register** and **arrow register**, including epistemic status separately from line style;
2. prohibit accidental cross-system edges in shared-forcing views;
3. validate inclusion of full technical system membership on the scope slide, even when a limited application is highlighted;
4. preserve data-source and equation provenance alongside the exported visual;
5. use original vector shapes, pure-white canvas and white interiors;
6. keep deterministic coordinates and prevent out-of-canvas labels;
7. not infer measured physical values from schematic positions or line widths;
8. include robust test fixtures: valid input, no crossing, empty array, non-monotonic time, absent event, invalid units/dimensions where applicable;
9. include an execution command and a concise PASS/FAIL report;
10. generate a reader-facing figure caption explaining evidence status, applicability, and sources.

**Renderer decision:**
- Static boundaries and conceptual diagrams → **SVG / PPTX native shapes**.
- Mathematical plots from real arrays → Matplotlib/SVG or vector-native PPTX chart with appropriately qualified values.
- Publication math (exact TeX) → TikZ/PGFPlots when equations/notation require it, with PDF/SVG rendering QA.
- Interactive math → parameter-driven D3/Canvas, but never animate fictional thermal events as established.
- Generative imagery → exploratory only for physical object illustrations; redraw scientific arrows, text, boundaries, equations and evidence labels deterministically, and validate against authoritative registers.

## 10F. Worked-example QA and scoring rubric

**Hard fail regardless of visual beauty:** false thermal bidirectionality, mismatched system boundary, invented numerical data, unqualified physical coupling, wrong arrow meaning, uncited external claim, inaccessible/clipped source label, false measured-looking trajectory, altered frozen objective.

After passing hard gates, evaluate each from **0–4**:
- physical / mathematical semantics;
- claim-to-source fit and adjacent APA attribution;
- logical viewpoint selection;
- arrow and boundary readability;
- low cognitive load without semantic loss;
- accessibility and grayscale robustness;
- editability / reproducibility;
- visual inspection and unit tests.

Only prototypes with **all hard gates PASS** and **no dimension below 3** are eligible for presentation release. Scores are agent evaluation heuristics, not scientifically validated performance measures.

**Three invariant fixtures** (must retain existing Section 10 fixtures):
1. parallel heat paths, zero P↔T_e thermal arrows;
2. separate P→T_e and T_e→P mechanism lanes with evidence gates, including *grid-side AC input* for a claimed EVSE→transformer effect;
3. complete T_e physical composition, external P separately bounded, optional reduced model inside the correct full boundary.

## 10G. Generated outputs and status-report format

Deliver the user:
1. **figure or editable slide/PPTX**, not merely a proposed design, when requested;
2. the scientific message and **figure type**;
3. compact arrow/boundary legend and **in-text citations**;
4. data/evidence status (\`ESTABLISHED\`, \`CANONICAL\`, \`CANDIDATE\`, \`OPEN\`);
5. script/renderer and editability detail where code was used;
6. scientific QA and numerical/technical test summary, showing limitations and blockers honestly.

If no data exist, prefer a plainly labeled **conceptual diagram** over a fake plot. If a required link or paper source cannot be verified, keep \`OPEN\`; use an original scientifically limited diagram only where still admissible.

## 11. Version history

### 2.0.0 — 2026-10-08
Added full task router; figure-by-figure why/when/how examples; coding model contract; deterministic SVG and metrics examples; executable test expectations; PPTX recipe; QA scoring and delivery workflow.


### 1.0.0 — 2026-10-08
Established peer-reviewed figure-reference workflow, figure family routing, presentation-level semantic compression, explicit arrow-vs-evidence orthogonality, mandatory adjacent in-text scientific citations, frozen P–T_e thesis boundary, PowerPoint accessibility checks, and three scientific fixtures.

