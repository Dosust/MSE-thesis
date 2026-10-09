# Deck3 Mechanism-Centered Scientific Figure Standard — V1

**Status:** Active Deck3 design and traceability standard. **Scope:** slide writing; scientific image and infographic generation; physical-system diagrams; mathematical drawings; editable PPTX shapes, assembly, animation, accessibility, source records and release QA. **Authority:** subordinate to the current thesis scientific authority, the primary Deck3 global-update contract, the Deck3 AI-image standard and the exact 13-token 8-bit sRGB palette. Inspired by an IEEE Transactions on Smart Grid figure **provided by the user** (May 2024, p.3116) as *design analysis*; not a reusable source for assumptions, parameters, thermal laws, copied graphics, or a validated P–T_e coupling.

## 1. Nonnegotiable design proposition

**A scientific figure must show how relevant components, interfaces, quantities, mechanisms, measurements and outcomes relate. A colorful box taxonomy is not a mechanism model.**

A figure should let a reader answer **what component**, **which boundary**, **what variable or information**, **from where to where**, **according to which relation**, **under what assumptions/evidence**, **with what observable service consequence**. Not every slide needs every layer: figure content is chosen by slide purpose. Simplicity serves interpretability and never justifies removing essential scientific qualifiers.

## 2. Scientific layers — keep separate

| Layer | Show when relevant | Do not confuse with |
|---|---|---|
| 0. External conditions | Ambient/heat forcing, scenario and source conditions | An internal state or an established cross-sector effect |
| 1. Complete physical system | Distinct **P** and complete **T_e** components and membership | Simulation subsystem or small active model |
| 2. Interfaces and exchanges | Actual **AC electrical** connection, charging load, admissible thermal mechanism and ports | Reciprocal energy flow or validated thermal causality |
| 3. Physical state and constitutive behavior | Thermal, electrical/operational states; (x(t)), parameter meaning and units | Capability, reliability, or measurement itself |
| 4. Functional/operating constraints | Conditional limits, actual AC/DC transfer, control inputs and operational laws | Delivered electricity/mobility service |
| 5. Observation and estimation | Sensors, observations, uncertainty, identification, parameter provenance and estimators | Physical mechanism, model validation |
| 6. Control and optimization | Controllers, decision inputs, objectives/constraints and feedback to equipment | A governing physical law |
| 7. Mathematical model and simulation | States, equations, solver, domain, verification and VVUQ gates | Empirically validated equipment |
| 8. Service / outcome | Electricity/mobility requirement, delivery and timing, service-level consequence | Automatic environmental/economic/social benefit |
| 9. Post-model assessment | Reporting, cost, sustainability effects and intervention comparisons | Physical system interior or observed physical causality |

Declare whether the **dashed boundary** denotes a physical network, simulation scope, controller, dataset, assessment stage, experiment or active-model subset. Never draw a simulation boundary and let the reader infer it is a physical ownership boundary. Use an **unambiguous legend** if multiple stroke types/boundaries appear.

## 3. Arrow and symbol contract

An engineering arrow is a directed scientific assertion, **not decoration**. Every important arrow requires an adjacent short label (or a keyed legend tied to the arrow ID). Record in a sidecar manifest:
- Unique arrow ID, unique source/target object IDs and explicit direction;
- Type: `physical_flow`, `state_influence`, `constraint_effect`, `control_signal`, `observation`, `data_for_identification`, `model_calculation`, `optimization_decision`, `reporting`, or `sequence`;
- **What crosses / is affected:** quantity name, symbol and units *if defined*, or explicit `OPEN` if unknown (never invent units);
- physical interface or computational/organizational handoff, appropriate boundary;
- governing law/operator or `OPEN`, validity assumptions, evidence and explicit scientific status;
- `P_TO_TE`, `TE_TO_P` or `NONE` for scoped cross-system direction.

For a **candidate cross-system thermal effect**, mark `OPEN` or `CANDIDATE` and visually distinguish it from measured transfer. Qualify P→T_e and T_e→P **independently**. In the T_e→P direction, require a **grid-side AC** evidence gate; DC charging output, a charging-load connection or shared heat exposure alone does not establish directional thermal causality. V2G is not assumed.

Do not use a double-headed arrow merely for aesthetic symmetry: create two independently registered directed assertions. Feedback is a meaningful closed loop with specified signal/state. Curved Bézier connectors, arrowhead angle and route avoidance improve readability but **do not imply physical nonlinearity**.

## 4. Five-layer presenter-controlled explanation

For mechanisms where staged presentation improves comprehension, prefer these *semantic reveal stages* inside existing figure bounds:
1. **Physical boundaries and equipment** (what is real; what belongs where).
2. **Interfaces with carried/affected quantities** (ports, arrows, units or OPEN tags).
3. **Forcing and physical states** (time-dependence, distinct heat pathways).
4. **Observation, identification, estimation, control and feedback** (separate symbols and relationships).
5. **Evidence/verification/validation and service consequence** (candidate vs qualified; no fabricated outcomes).

This is a learning framework, **not a universal demand for five clicks**. Keep all approved native PPTX text, citations and notes visible throughout; use `Appear` + presenter `On Click`, persistent elements, and progressive-slide fallback only as needed. Animation shape IDs correspond to manifest arrow/object IDs. Reveal an arrow with its label, endpoints and evidence qualification; never reveal an unexplained causal-looking line as an interim frame. No animation implies causation.

## 5. Diagram design, color and projection rules

- Canvas and all box/header/legend interiors **#FFFFFF**; all authored colors **only** exact tokens from `DECK3_SRGB_PALETTE.json`. No gradients/shadows/textural fills. ASU Gold and Bright Turquoise only for small **nonessential** accents; photographs may retain authentic colors with provenance.
- Meaningful arrowheads are large, clear, directional. Prefer fixed anchors, minimal crossovers, deliberate orthogonal/curved routing, and labels **offset from** lines (never overprinted).
- Preserve variable names as defined by the real source and show units or explicit `OPEN`; italic mathematics and native Office Math where appropriate.
- One scientific takeaway; reduce repeated miniature text, unrelated icons, gratuitous symmetry, 3D and ornament. Icons denote actual equipment/measurements/control, not generic decoration.
- The 70–80% figure share is **effective meaningful science**, not a white-padded image rectangle. Measure usable bounds and check projected labels, not only PNG pixel count.
- Prefer separate editable PowerPoint objects/native connectors and SVG source; raster previews are not equivalent to individually editable or independently animatable layers.
- No on-slide template labels such as `MAIN MESSAGE` / `THREE KEY POINTS`. Content and source attribution remain; actual frozen objectives and approved slide text must not be silently revised.

## 6. Mechanism trace sidecar (machine-auditable structural record)

For each scientific diagram asset, put an optional-to-open but **required-for-science-approval** sidecar adjacent to the PNG/SVG: `<stem>.trace.json` (e.g. `Slide_05_Research_Problem.trace.json`).

The sidecar **does not prove scientific validity**. It allows structural checks and records evidence for independent review. Use `examples/mechanism_trace_qa.py` and `examples/mechanism_trace_example.json`.

Required:
- `schema` = `deck3-mechanism-trace-v1`, `figure_id`, `takeaway`, `science_authority`, `evidence_status`, `assumptions` list, `limitations` list;
- `boundaries`: each ID/type/membership/meaning; physical P and full T_e separate when relevant, active model separately typed;
- `objects`: unique IDs, parent boundary, meaning/type, evidence status;
- `arrows`: unique IDs, existing endpoints, semantic `type`, nonblank `label`, `carried_quantity`, `direction`, `interface`, `law_or_operator`, `evidence_status`, `sources` list and `evidence_gate`;
- `review`: independent `physics`, `labels`, `figure`, `citations`, `animation` fields, each `OPEN`/ `PASS`/`FAIL`. PASS is recorded only with actual human and/or validated domain review; the checker does not fill these fields.

Source checking: external scientific `ESTABLISHED` or `QUALIFIED` arrow requires a nonempty evidence citation and an explicit qualifying method/assumptions. The checker verifies presence and consistency, **not** whether those cited studies genuinely support the claim. The `science_authority` is a real source/ref, not autogenerated literature.

Backwards compatibility: an old PNG without sidecar can still be assembled as a **PROVISIONAL** working draft; its QA record must say `TRACE_NOT_REGISTERED` and it cannot be called scientifically traceable/certified. A malformed/inconsistent supplied sidecar **blocks** Stage 2 and Stage 3. Never backfill a historical sidecar with invented physics simply to turn a test green.

## 7. Release gates and scientific authority

All original Deck3 S/W/C/F/A/Q gates still apply. Add **M — mechanism traceability**:
- Objects and declared boundaries match the selected viewpoint; physical vs model distinctions unambiguous.
- Every essential arrow has an ID, semantics, quantity/OPEN, direction and valid endpoints; citations and evidence status are attached.
- Measurement/identification/simulation/assessment phases remain separate, with correct times and units where defined.
- Directional P→T_e / T_e→P candidate thermal mechanisms have independent evidence gates.
- Diagram does not claim validated results from illustrative model construction.
- Tested geometry and native shape/animation fidelity, rendered projected readability and manual source checking are separately reported.

**Allowed output statuses:** `SOURCE_SPECIFIED`, `STRUCTURAL_TRACE_PASS_NOT_PHYSICS_VERIFIED`, `TRACE_NOT_REGISTERED_PROVISIONAL`, `RENDERED_QA_PENDING`, `POWERPOINT_PLAYBACK_PENDING`, `PHYSICALLY_VALIDATED` **only when actual independent empirical evidence warrants it**. A passing code test is *never* a physics conclusion.

## 8. Slide-family adaptation for current Chapter 1

- **Slide 3:** distinguish P and full T_e and name AC supply vs charging-load effect separately.
- **Slide 4:** external heat forces both independently; no false cross-sector thermal arrow.
- **Slide 5:** two *candidate* directions, independent evidence gates; T_e→P must include **grid-side AC** behavior.
- **Slide 6:** literature matrix distinguishes source-covered mechanisms from OPEN case-specific novelty/gaps; citations next to claims.
- **Slide 7:** RQs are working, frozen SOs remain verbatim where shown.
- **Slide 9:** physical, simulation/active-model and external assessment boundaries are not interchangeable.
- **Slide 10:** separate source identification, model formulation, numerical verification, empirical validation, uncertainty and derived service metrics.
- **Slide 11:** proposed outputs are not completed validated results.
- **Slide 12:** thermal state → capability → actual transfer → delivered service; resilience and the two bounded sustainability pathways separate.
- **Slide 13:** sequence arrows mean **chapter order**, never physical causation.

## 9. Real-world limits and attribution

The user-supplied IEEE diagram is used here as a **design inspiration** only. Do not reproduce copyrighted IEEE artwork, lift its topology as an established model for this thesis, or assign its symbol labels as if they are measured quantities in the user's case. Do not infer its paper title, authors, parameter data or empirical validity merely from a screenshot. Any later manuscript citation needs verified bibliographic source and content-specific support.
