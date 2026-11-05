# KIT electrical topology: evidence audit for 110 kV, 20 kV and 400 V EV observations

**Audit date:** 2026-11-05
**Dataset:** https://doi.org/10.5281/zenodo.22826984
**Prior local acquisition and timing audit:** [KIT_OLTC_22826984_ACQUISITION_AUDIT.md](KIT_OLTC_22826984_ACQUISITION_AUDIT.md)
**Decision:** Physical 110/20/0.4 kV hierarchy CONFIRMED at KIT Campus North infrastructure level; exact PMU04_TK1 to PMU01_J01 to EV_SH.J.6 physical route NOT VERIFIED.

## 1. Frozen scope

The current thesis investigates **thermal** Power ↔ Electrified Transportation interdependencies under extreme heat. Electrical connectivity is supporting evidence only, and not itself proof of an extreme-heat mechanism. This file is subject to the [title V3](../../../project/CANONICAL_THESIS_TITLE_V3.md), [thermal scope V4](../../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md), [SO1–SO3](../../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md) and [evidence rule](../../../project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md).

## 2. Verified external sources

### E1. Original KIT Zenodo record (Dorn and co-creators, 2026)

**Primary source:** https://zenodo.org/records/22826984; DOI 10.5281/zenodo.22826984.

The creators identify the original source as KIT Campus North energy infrastructure. They describe 100 ms synchronized 110 kV, 20 kV and 400 V voltage/current measurements, including EV charging, solar PV and heat-pump loads. The recorded anomaly is a real on-load tap changer (OLTC) regulation problem; the source describes approximately 30-second recurrent downstream voltage steps and increased contact resistance/corrosion of the resistor-type tap selector mechanism.

The specific selected original files are:
- **110 kV:** oltc_fail_110kV_PMU04_TK1_100ms.parquet.
- **20 kV:** oltc_fail_20kV_PMU01_J01_100ms.parquet.
- **400 V EV:** oltc_fail_400V_EV_SH.J.6_100ms.parquet.

The online dataset description does **not** provide an asset-level electrical adjacency map proving that the two named PMUs and the EV point lie along one direct supply path. It does not list actual feeder/switchgear, the EV station's parent MV/LV transformer, or operational switch configurations.

### E2. Mehlmann and co-authors (2023), real campus architecture

**Peer-reviewed primary reference:** Mehlmann et al. (2023), The Kopernikus ENSURE Co-Demonstration Platform, IEEE Open Journal of Power Electronics. DOI https://doi.org/10.1109/OJPEL.2023.3332515. Full paper https://publications.rwth-aachen.de/record/974106/files/974106.pdf, **Section III-D and Figure 4**.

The described KIT Campus North distribution grid:
- has **three** 110/20 kV supply transformers totaling **87 MVA**;
- feeds **two 20 kV busbars**;
- has **seven open rings** with **42 MV/LV stations**;
- has a detailed PowerFactory campus grid model with around **1,800 buses**, **1,000 switches/breakers**, **500 lines**, and **122 transformers** from 20 kV to lower voltage levels, predominantly 400 V (also 10 and 6 kV);
- the paper's Figure 4 is a **reduced RSCAD representation** of that network, with simplifications. Model component numbers are not a verified 2026 physical asset census.

**Interpretation:** the campus-level electric hierarchy 110 kV → 110/20 kV transformers → 20 kV ring network → MV/LV transformers → 400 V loads is supported. However, several possible parent transformers, switches and feeder paths exist; the paper does not map the 2026 original time-series sensor identifiers to the network.

### E3. Kühnapfel and Hagenmeyer (2025), independent documentation

**Source:** Kühnapfel, U., & Hagenmeyer, V. (2025), On the Art of Electric Power System Modelling and Simulation for Integrated Transmission-Distribution Analysis, in *Modelling the Energy Transition: Cultures, Visions, Narratives*. Edited volume DOI https://doi.org/10.1007/978-3-031-69031-0; source https://publikationen.bibliothek.kit.edu/1000183007/162085181, campus model around pages 124–125.

Reports 3 × 110/20 kV transformers in KIT Campus North rated **2 × 23.5 MVA and 40 MVA**, summing to 87 MVA. This supports the campus supply architecture and underscores that one 110 kV observation alone does **not** establish which of multiple transformers fed the EV point.

## 3. Evidence-to-claim matrix

| Exact research question | Decision | Reason |
|---|---|---|
| Is the KIT Campus North 110 kV supply electrically connected to its 20 kV network? | **CONFIRMED, general network** | E2/E3 describe the three 110/20 kV campus transformers. |
| Does the campus 20 kV network supply 400 V loads? | **CONFIRMED, general network** | E2 documents MV/LV substations and lower-level transformer links. |
| Does E1 place the measured EV charging and the PMUs in the same campus infrastructure study? | **YES, source-reported** | E1 explicitly describes same campus multisite synchronized observations and the EV measurement. |
| Is PMU04_TK1 actually upstream of PMU01_J01 along one named supply transformer? | **OPEN** | Source identity/location and transformer winding/bus mapping not released in E1–E3. |
| Is PMU01_J01 the physical parent feeder of EV_SH.J.6? | **OPEN** | Parent feeder, MV/LV transformer, switching status, node mapping absent. |
| Were those exact connections constant throughout 50-day record? | **OPEN** | 2026 bus-tie and feeder-switch states not supplied. |
| Are all three UTC sample grids identical? | **USER-LOCAL VERIFIED** | 43,200,000 × 3 timestamps, zero grid mismatches, reported by user on Nov. 5. This is not external sensor clock calibration. |
| Does voltage-event coherence prove a direct source-feeder path? | **NO** | Parallel branches may share upstream disturbance; causality/topology not identified solely by a common voltage event. |
| Does KIT include measured ambient/transformer/EVSE temperatures? | **NO in three inspected schemas** | Original Parquet metadata lists electrical signals, no thermal sensors. |
| Are directional thermal causality and mobility service resilience field validated? | **NO** | No thermal restriction or required/delivered mobility service state measurements verified. |

## 4. Candidate campus hierarchy versus *unproven* sensor map

**Verified architectural abstraction, not a wiring map for these particular sensors:**

Public 110 kV supply → multiple 110/20 kV transformers → 20 kV busbars → multiple 20 kV rings → MV/LV transformers → 400 V distribution → EV charging.

**Specific measured pairing remains a hypothesis:**

PMU04_TK1 (110 kV) → ? → PMU01_J01 (20 kV) → ? → EV_SH.J.6 (400 V).

Do not draw a solid or unconditional directed PMU-to-EV connection until source documentation identifies the 2026 parent assets and operating switching arrangements.

## 5. Exact additional metadata required

Contact the original Zenodo record contact persons **Marvin Dorn** and **Sebastian Beichter** or the KIT campus network data custodians. Request non-sensitive/anonymized:

1. Measurement-point-to-bus/transformer map for PMU04_TK1 at 110 kV and PMU01_J01 at 20 kV, including each sensor's physical meter/CT/PT placement.
2. Actual 2026 110/20 kV transformer association, bus-tie settings, and connections relevant to the two PMUs.
3. EV_SH.J.6 point-to-LV feeder and parent 20/0.4 kV MV/LV transformer; parent 20 kV ring and bus, exact meter location relative to charging equipment.
4. Dynamic topology changes/switch statuses, if any, over the source reporting interval (2026-02-04 through 2026-03-26 campus-local dates), and their recorded times.
5. OLTC ID, tap-position/fault-phase annotation semantics and control event timing for attribution, without assuming tap-position telemetry exists.
6. If a full single-line diagram is restricted, an anonymized **edge-list/adjacency table** with the sensor IDs, upstream/downstream transformer/bus nodes and effective switching intervals is sufficient for this gate.
7. Instrument time-reference accuracy and CT/PT sign and voltage conventions to interpret measured correlations.

**Acceptance gate:** G3 precise measurement path passes only after a traceable primary-source point-to-asset mapping and time-valid switching configuration, not on the basis of correlated time series alone.

## 6. What can be tested with the locally held Parquet files now?

- After the already completed every-row timestamp validation, evaluate matched-event voltage steps and charging-power response only as **supporting electrical evidence**.
- Respect observed variable semantics, phase-vs-line voltage definitions, per-level nominal scaling, and unknown direction/sign conventions.
- Compare suspected OLTC anomaly versus a valid baseline, and other low-voltage heat-pump/PV branches if independently downloaded/qualified.
- Common voltage steps can occur on different electrical branches and are not enough to infer exact feeder/transformer ancestry.
- This OLTC electrical regulation anomaly is **not** itself an extreme-heat thermal mechanism.

## 7. G0–G7 scientific admission update

- **G0:** published source supports real campus operational electrical measurements; exact site/device and instrument details partially OPEN.
- **G1:** three original user-local MD5 PASS, source data not uploaded to GitHub.
- **G2:** schema, stated units and timestamp grid verified; detailed quality and sensor semantics pending.
- **G3, broad:** campus 110/20/0.4 kV physical architecture source-supported.
- **G3, exact:** PMU04_TK1 to PMU01_J01 to EV_SH.J.6 physical ancestry and switch timeline **OPEN**.
- **G4:** 100 ms recorded timestamp grid verified for all 129,600,000 rows; independent clocks unverified; thermal state measurements absent.
- **G5–G7:** coupled thermal model validation, directional thermal dependence and electricity/mobility service consequences **NOT established**.

**Next required evidence:** source-provided 2026 bus–transformer–feeder–EV sensor adjacency and switch-status table. **No repeat of completed downloads, MD5 or timestamp tests.**

## Links

- DOI of dataset: https://doi.org/10.5281/zenodo.22826984
- E2 publication DOI: https://doi.org/10.1109/OJPEL.2023.3332515
- E3 edited book DOI: https://doi.org/10.1007/978-3-031-69031-0
- Original Mac acquisition QA: [KIT audit](KIT_OLTC_22826984_ACQUISITION_AUDIT.md)
- Frozen thesis evidence requirements: [standard](../../../project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md)


## 9. User-approved scope decision: proceed without feeder-specific mapping

**2026-11-05 user direction:** The user considers the documented campus-level shared electrical infrastructure and exact shared 100 ms timestamp grid sufficient for the present **system-level electrical analysis**. The user explicitly declines additional feeder-specific information gathering as a prerequisite for continuing work.

**Operational interpretation:**
- **Proceed now** with same-system, synchronized **cross-voltage electrical event/response** analysis for 110 kV, 20 kV and 400 V EV series. Use measured signal changes, appropriate normalization, and explicit event windows; do not make upstream causality claims beyond what the data justify.
- The published multi-level electrical campus architecture and the user's 129,600,000-row timestamp-grid PASS are sufficient for this **bounded descriptive/comparative analysis**. A detailed 2026 feeder/transformer ID is **not an execution blocker** for this objective.
- Preserve the distinction **shared power system and synchronized observations != verified serial parent-child route**. The exact PMU04_TK1 -> PMU01_J01 -> EV_SH.J.6 feeder and switch mapping remains **UNVERIFIED** and is relevant only if a future claim demands a unique supply path or branch-specific causal transfer.
- Avoid repeatedly requesting the same feeder mapping in this workstream unless the user explicitly pursues branch-specific analysis or a scientific result depends on that mapping.
- KIT still has **no verified ambient/EVSE/transformer temperature or recorded thermal derating fields**. It therefore cannot alone validate SO1–SO3 thermal model/causality/service outcomes; acquire those separately.

**Current progress decision:** proceed with instrument-level power/voltage-quality checks and correlated event analysis; treat exact physical feeder attribution as a *recorded limitation*, not a stoppage criterion. This is a working analysis choice, **not** a change to any canonical thesis authority.
