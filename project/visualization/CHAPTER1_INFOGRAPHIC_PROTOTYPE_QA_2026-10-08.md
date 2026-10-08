# Chapter 1 Scientific Infographic Prototypes — Semantics and Citation QA (2026-10-08)

**Status:** WORKING PROTOTYPE — awaiting scientific/presentation review; not an authorized change to frozen thesis science.  
**Target:** Slides 3–5 of the 16-slide Chapter 1 cited introduction PowerPoint, retaining the other 13 slides verbatim.  
**Design skill:** `.github/skills/scientific-infographic-design/SKILL.md`, and `references/CHAPTER1_FIGURE_STORYBOARD.md`.  
**Artifact:** An editable PowerPoint was produced as a ChatGPT conversation attachment: `ASU_MSE_Chapter1_Infographic_Prototypes_Slides3-5.pptx`. This file is NOT claimed to have been uploaded to GitHub.

## A. Slide 3 — Two-system architecture

**Message:** The full Power System P and Electrified Transportation System T_e are different physical systems; their electrical interaction is not itself a qualified heat-conditioned dependency.

**Diagram objects:** Two separately enclosed, pure-white physical domains. P contains network, transformer, and operating constraints. T_e explicitly contains vehicle, rechargeable storage, propulsion, auxiliary electrical functions, vehicle power-supply circuit, EVSE, physical connection, and power-transfer controls. These are inventory/membership elements, not a claim that every component has been admitted to a reduced state vector.

**Arrow register:**
- P→T_e: solid blue arrow, labeled **ELECTRICITY** — actual physical electrical supply.
- T_e→P: green arrow, labeled **LOAD EFFECT** — causal influence of charging demand on Power loading, **not V2G reverse power flow**.
- No arrow asserts a thermal mechanism, an outage, cascade, quantified propagation, or a resilience result.

**Source support:** Qian et al. (2015), https://doi.org/10.1016/j.ijepes.2014.09.040 ; Diahovchenko et al. (2023), https://doi.org/10.1016/j.epsr.2023.109455 . Complete T_e membership: `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md` §§1–4A. Extrapolated specific thermal mechanisms remain OPEN.

## B. Slide 4 — Common extreme heat is not thermal coupling

**Message:** External heat can influence P thermal state/capability and T_e thermal state/capability separately. The independent responses do not establish P↔T_e causal heat-conditioned coupling.

**Arrow register:** Two red forcing arrows from the external-heat object to the **two different system boundaries**; within each white-bounded system, one state→capability arrow. There is deliberately **no cross-system thermal arrow**.

**Source support:** IEEE Std C57.91-2025, `https://standards.ieee.org/ieee/C57.91/7163/` (active standard published March 2026; guide applies to mineral-oil-immersed transformer loading with stated domain); Krama et al. (2026), https://doi.org/10.1016/j.ecmx.2026.101960 (field-tested commercial air-cooled DC fast charger; results **not universally transferable** to all EVSE).

**Scope caution:** Example candidate thermal states shown are not frozen model states; thermal capability relations and manufacturer-specific limits remain OPEN for the eventual case.

## C. Slide 5 — Independent candidate mechanism directions

**Message:** The research must qualify the complete P→T_e and T_e→P heat-conditioned pathways individually. Two boxed lanes are clearly labeled **CANDIDATE — not case-qualified**.

- **P→T_e candidate:** heat-conditioned P operating constraint → *applied* charging supply restriction → actual T_e charging capability → mobility-service requirement. The operating policy/constraint enforcement, charged power, and service requirement remain OPEN.
- **T_e→P candidate:** EVSE thermal response/derating → grid-side AC input change **to verify** → actual P electrical loading → transformer thermal response. Service consequences require a **separate** defined electricity-service evaluation. EVSE DC delivered/output power cannot simply be identified with the AC-side current/real/reactive/harmonic load without equipment- and case-specific evidence.

**Source support and limits:** Krama et al. (2026), charger-specific measured thermal behavior and electrical performance; Qian et al. (2015), EV charging/transformer load and aging; Visakh and Selvan (2023), https://doi.org/10.1016/j.segan.2023.101096, EV charging/transformer thermal loading and service-disruption analysis. No single cited source is represented as validating this combined two-way thesis application.

**Causality convention:** Arrow shape denotes the *kind* of candidate relation being investigated; `CANDIDATE` / `OPEN` label is the separate epistemic status. Do not use a dashed control arrow to represent uncertainty.

## D. Verification record

**Automated working checks** after rebuilding the deck:
- 16-slide PowerPoint preserved.
- Slides 3, 4, and 5 replaced using editable native PowerPoint shapes/text/connectors, with **zero embedded bitmap pictures** in each edited slide.
- All other **13 slides had exact unchanged extracted text**.
- New three slides contain visible adjacent in-slide research/source references and retain original, detailed source-content speaker notes.
- Deck was successfully rendered to 16-page PDF for internal visual review and slides 3–5 rasterized at 2001×1125 pixels for inspection.
- Second rendering pass corrected a crowded Slide 4 headline and avoided presenting thermal-state and electricity-service outcomes as an interchangeable box on Slide 5.
- Visual review found pure-white slide and box interiors, directional arrows, readable titles, and no visually apparent clipped graphics on redesigned slides.

**Limitations of this QA:** It is a visual/semantic prototype audit, not a demonstrated empirical validation or automatic proof of PowerPoint accessibility/read-order correctness. The eventual equipment, measured time-aligned data, operating rules, and service requirement definitions remain OPEN. The working figures are not frozen and should not be used to infer validated bidirectional thermal physics.

## E. Next design stage (after review)

Apply the same grammar to Slides 6–13, prioritizing:
1. Slide 6: specific cited prior-art and still-OPEN evidence matrix;
2. Slide 9: frozen full-system vs active-model boundary view;
3. Slide 10: evidence/qualification/model/VVUQ gates;
4. Slide 12: state→capability→service→resilience and separate bounded sustainability paths.

Do not propagate any scientific conclusion, threshold, or validation claim from the presentation graphics alone.
