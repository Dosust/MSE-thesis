# Deck3 Professional Engineering Visual References and Science-to-Graphic Routing V1

**Effective:** 2026-10-13. **Status:** ACTIVE PRODUCTION REFERENCE / SOURCE-REVIEW STANDARD; subordinate to canonical thesis evidence, approved deck wording, original equipment documents, and the Deck3 exact 13-token palette. **Scope:** Deck3 all, text, individual scientific illustrations, system/engineering diagrams, mathematical figures, numerical charts, PowerPoint assembly, and genuine physical-time animation.

## 0. Why this exists: avoid generic AI visuals
Earlier 10-image drafts repeated transformer/car/desert scenes, overhead lines in place of the actual TU Wien 20Cable feeder, invented displays/curves/temperature-like imagery, extra cabinets, decorative suns/heat waves, and whole-slide panels where the user wanted **standalone insertable figures**. Those images remain **PROVISIONAL / NOT SCIENTIFICALLY APPROVED**. Reject similar generations; do not redesign the same scenes with a different prompt. A scientific diagram must be *drawn from an admitted mechanism and topology*, not inferred from the subject's keywords.

**Rules:** one slide/figure → one defensible scientific question → minimum physically meaningful elements → independently typed and evidenced relationships. Decide the *diagram family* BEFORE the medium or image generator. No stock-style montage when exact symbols, topology, data, equations or controls must be rendered with editable geometry.

## 1. Verified external authorities and their exact roles

| Reference | Directly verified authoritative page | What it permits | What it does NOT establish |
|---|---|---|---|
| **IEC 60617 graphical symbols** | https://webstore.iec.ch/en/publication/2723 | Primary electrotechnical symbol database; authoritative categories include conductors, energy conversion, switchgear and protection. Symbol identity/design must be checked in the actual licensed database or another rights-compliant original reference. | The public catalog is **not** a free, inspectable catalog of every individual symbol; never falsely assert a custom icon is IEC-60617-compliant or reproduce restricted symbol artwork without rights. |
| **OMG SysML v2 specification** | https://www.omg.org/spec/SysML/2.0 | Formal concepts for systems structure, ports, connections, requirements, behaviors, quantities and traceability. Use genuine syntax/semantics only if checked against the normative specification. | A generic nested-box cartoon is **not** automatically a SysML-compliant model; no need to pretend to use formal SysML when drawing a simpler, explicitly typed SoS view. |
| **INCOSE Systems Engineering Handbook** | https://www.incose.org/resources-publications/technical-publications/se-handbook/ | Systems-engineering process/viewpoint/lifecycle guidance, interface management and system-level framing. | This webpage is a handbook description; do not claim to have examined or quote inaccessible book chapters or specific proprietary figures. |
| **IEEE PES Test Feeders** | https://sites.ieee.org/pes-testfeeders/ | Source-finding lead for recognized feeder benchmarks, their individual topologies, and published model files. | **Source page may be robots-blocked.** Without the original target feeder file, its topology and numerical values remain unverified; no transfer into the TU Wien 20Cable network. |
| **EPRI OpenDSS workflow** | https://opendss.epri.com/Workflow.html | Specific professional figure families: one-line/circuit plots, voltage profile along feeder, equipment P/V/I views, exported numerical results. | Screenshots/output from other feeders are not evidence for the user's TU Wien case. |
| **IEEE Author Center: graphics** | https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/ and https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/ | Vector-first graphics, sufficient original resolution, line-pattern/marker accessibility beyond colors. | Journal raster dpi/column-width requirements do not automatically become PowerPoint projection sizes; these are distinct outputs. |
| **Nature Research Figure Guide** | https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/ | Accurate tick marks, labeled axes/units, accessibility, legible annotations; reject unnecessary background grid, clutter, shadows and made-up graphics. | Nature's published-figure font sizes/format constraints are not automatically applicable to ASU presentation slides. |
| **ASU official presentations guide** | https://brandguide.asu.edu/execution-guidelines/presentations | ASU recommends 16:9 presentation format; official branded templates are available under ASU access restrictions. | Does not authorize AI-drawn ASU logos, invented ASU identity, approval of user's custom template, or replace the user's Times New Roman requirement. |
| **Manim Community** | https://docs.manim.community/en/stable/tutorials/building_blocks.html | Reproducible animated mathematical objects, scenes and transformations. | Rendering a mathematical-looking curve does not validate its equation, parameter, source data, or physical time interpretation. |

**Access record:** The publicly reachable pages above were checked for their stated purpose on 2026-10-13; this is **not** a symbol-by-symbol inspection, review of every source figure, verified licensing clearance, or endorsement by these organizations. Retain individual figure URL/version/rights/access state for any actual selected exemplar. Do not copy figures or licensed artworks.

## 2. Scientific view-selection matrix (not one generic illustration family)

| Scientific task | Correct primary view | Semantic tests | Correct renderer |
|---|---|---|---|
| **Electrical connectivity** | Recognizable IEC-inspired **single-line** network with actual buses/branches/AC ports, or exact original feeder topology | Topology, voltage level, direction, phases, equipment/port labels, side-load branches and symbol provenance; never use overhead poles as if TU Wien 20Cable had them | Original vector SVG/native PPTX; real network data plot only if admitted |
| **Systems membership/SoS** | Separate Power and full Electrified Transportation constituent boundaries, parts, typed interfaces and selected active-model subset | Physical-system boundary ≠ simulation boundary ≠ control volume; four selected T components do not exhaust all physical T_e equipment; enforce port semantics | Native PPTX/SVG; SysML-like only if labeled **conceptual**, unless normative notation actually checked |
| **Physical thermal mechanism** | Heat/energy balance, qualified thermal RC equivalent, or equipment cutaway WITH source-qualified hardware | External ambient forcing separately from thermal state and losses; heat W versus T °C/K; avoid imaginary radiant coupling or undocumented fans | Vector schematic; relevant equipment-only original art optional |
| **State-time mathematical behavior** | Actual ODE/DAE state trajectory or formally declared event-time schematic | Derived from admitted law and initial/boundary conditions; labels/units; distinguish simulation from measured series; events censored if not observed | Python/Matplotlib/Manim with stored data+solver manifest |
| **Research/evidence gap** | Native editable evidence-to-question relation, not a charger/transformer montage | Distinguish published AC measurements, predicted offered DC, raw missing synchronous CPC50 measurements, I2/H1 OPEN and I3/H2 OPEN | Native editable PPTX relationships/tables, citations external to image |
| **Methodology** | Provenance/qualification gates and sequence (research-process arrows, NOT physical flow) | Source → observation → physics → model → tests → conditional conclusion; separate verification and empirical validation | Native editable PPTX flow |
| **Work completed** | Source-status/verified-results matrix, no stock tick marks | Report performed work with appropriate proof and limitations; do not give synthetic tests the status of field validation | Native editable PPTX evidence ledger |
| **Preliminary results** | Measured/model-derived graph from **actual** admitted data/CSV and reproducible script | Axis units, explicit series provenance, time window, data/model assumptions, uncertainty, noninvented points; never AI-drawn pseudo-data | Python/Matplotlib + editable slide caption/legend |
| **Project plan** | Month-based Gantt/timeline without fabricated completion | Separate completed/ongoing/planned, dates, dependency gates and contingent data access | Native PPTX vector/text |
| **Title / Closing** | Optional single restrained original physical equipment image, or text-only | Exact approved title/identity from source; no generated logos, invented thesis titles or scenic heat decoration | Equipment-only original SVG/illustration |

## 3. TU Wien–Qatar–Najar–Bærug admissibility gates

- TU Wien **20Cable**: a **radial low-voltage MAIN CABLE FEEDER WITH CUSTOMER BRANCHES**. Use exact workbook for original 10 main 100 m segments and 20 customer 10 m branches; a simplified circuit must be marked *schematic subset*. Overhead transmission poles are NOT the verified TU Wien case.
- P1 transformer, P2 cable feeder, P3 transformer protection/load-management hardware, P4 transformer cooling; T1 DC EV charger, T2 battery, T3 EVSE cooling, T4 vehicle HVAC are the user-approved current **working investigation roster**. Do not automatically draw all as separately installed free-standing hardware or separate ODE states.
- I1: *ordinary Power → EVSE grid-side AC supply*, NOT proof of temperature-mediated interdependency. I5: EVSE DC delivery to vehicle battery (actual offered/delivered/accepted boundaries differ). No V2G/reverse AC energy arrow without exact device authority.
- External extreme heat acts on P and T_e independently; shared forcing alone is **not cross-system propagation**.
- I2/H1: candidate T1/T3 thermal operating condition → *actual* grid-side AC P,Q/current change → P2/P1 loading/losses → conditional P1 temperature dynamics; Qatar's reported derating/AC measurements do not establish complete matched TU Wien transformer field response or independently identified law.
- I3/H2: candidate P1 temperature → installed P3 sensing/control law → actual charger restriction. No installed controller trace/operation admitted; **OPEN**. Do not depict verified power interruption solely from hot equipment.
- Najar 160 kVA ONAN parameters support **conditional surrogate**, not measured TU Wien thermal constants. Bærug measured 40 MVA dataset is independent model-evaluation evidence, **not transferable** P1 parameters. Do not insert machine-generated curves into preliminary results.
- Each selected external example is *design-language reference only* until its actual source object, data version, rights and physical relation pass qualification.

## 4. Required per-slide original exemplar audit

Before designing each eligible **standalone** asset, record in machine-readable figure brief or research ledger:

1. `deck_variant`, exact `slide_id`, approved one-line message, actual slide body/citation source, and slot dimensions.
2. `diagram_family` from Section 2, whether illustration is scientifically necessary, and why an imported image versus native PowerPoint is chosen.
3. External `authority_url` and `examined_object` (actual figure/equipment/manual/symbol page rather than merely paper title). `access_depth`: `CATALOG_ONLY`, `PAGE_READ`, `FIGURE_INSPECTED`, or `SOURCE_DATA_AUDITED`.
4. `design_takeaway` learned (layout/alignment/symbol conventions) **not copied artwork**; `rights`: `ORIGINAL`, `PERMISSION_VERIFIED`, `OPEN`, with no reuse of source pixels without rights.
5. Typed nodes, ports, directed edges and quantities; arrow evidence status and claim-level citations. Distinguish physical, external forcing, control, measurement, methodological sequence and conditional hypothesis.
6. Choose deterministic SVG/native PPTX when technical symbols/topology/labels/axes are needed; AI image generation only for authorized realistic *equipment-only* art where appearance materially helps.
7. Record QA `PASS`/`FAIL`/`BLOCKED`/`NOT_RUN` for **scientific mechanism**, original artwork/right clearance, edited geometry, exact authored palette/white surfaces, text/citation editability, rendered readability, and actual PowerPoint/GIF playback separately.

**Mandatory rule:** No claim of “professionally researched,” “IEC-compliant,” “peer-reviewed reference-matched,” or “publication-ready” unless the relevant object/standard, source depth, and actual QA were inspected and logged.

## 5. Human-quality design and anti-AI acceptance

Reject if repeated stock transformer/car/sun scenery, generic desert skyline dominating content, floating heat symbols presented as physics, impossible power/control arrows, fabricated transformer fan/control/cooling installation, arbitrary values/temperature contours, unreadable mini-plots, entire slide screenshots presented as insertable figures, text panels built into equipment art, unjustified multi-colored boxes, gradients or shadows. **Use discipline-specific views**, deliberate whitespace, consistent scale and line widths, high-contrast fonts and minimal labels. A figure is not improved by adding unrelated engineering objects.

Graphics may retain realistic natural plant/equipment colors; authored diagrams remain **exactly** within `DECK3_SRGB_PALETTE.json` (13 approved tokens) on white canvas/panels, institutional gold strictly nonessential. The slide title/notes/equations/source attributions must be native editable Times New Roman PPTX elements where applicable.

## 6. Numerical and animation contracts

- Source-data charts: actual arrays, units, missingness and temporal alignment; save plotting script, input file/version/hash, output image, and source-to-series map. No illustrative curve in a preliminary-results figure unless unmistakably labeled “schematic / not data.”
- Thermal model trajectories: explicitly specified equipment/model, input units, initial conditions, parameter provenance, step alignment at discontinuities and convergence/uncertainty where relevant; solver accuracy ≠ physical validation.
- Animation must distinguish **presentation time** `s` from physical time `t`; component sequential **reveals** are not evidence of power propagation. Scientific-time video frames map to admitted measured/simulated `x(t)` and save time map/units; unmeasured cross-coupling never animated as observed.
- A GIF/MP4 is not natively editable internally in PPTX; provide SVG, original source, native overlays and static frame as separate deliverables. Check actual PowerPoint playback before claiming it passed; otherwise `NOT_RUN`.
- Prefer vector PDF/SVG/PPTX originals and validated export; IEEE journal format/dpi specifications apply **only when preparing IEEE journal submission**, not automatically to projected ASU slides.

## 7. Execution and authority placement

Called by `Deck3 all`, `Deck3 figures`, `Deck3 QA`, research-expert, scientific-diagram, scientific-infographic, mathematical-visualization, engineering-framework, advanced PowerPoint and optional interactive view. Mandatory order: frozen science → approved presentation variant → one figure brief → primary physical/data source → external visual exemplar inspection/rights → semantic diagram family → original creation → traceability/QA → genuine rendering/playback → eligible assembly.

**This standard is a cross-skill routing and evidence reference, NOT an amendment to frozen objectives, component IDs, thermal equations, slide titles or empirical status.** Existing image files receive no retroactive approval.