# Austin Case-Study + Data Admissibility Matrix v3

**Date:** 2026-09-18  
**Protocol:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation  
**Authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md` + `CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Supersedes for active execution:** `AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V2.md`  
**Reason for version:** temporal provenance is now explicit for current signal GIS, retrospective traffic-sensor metadata, and static floodplain evidence.  
**Decision:** **CANDIDATE CASE ONLY — NOT YET ADMISSIBLE**.

## 1. Frozen candidate

```math
\mathcal C_{AUS}^{cand}
=
(\text{SMART-DS v1.0},2018,\text{AUS},P5U,\Omega,\mathcal G_T,\eta_F,\mathbb I_{PT}).
```

Candidate ID: `AUS-P5U-2018-V1`.

P5U remains provisional until every mandatory G0–G8 gate passes. Case/subregion selection may not use H1–H5 outcomes.

## 2. Active source matrix

| Object | Source | Temporal role | Spatial / temporal resolution | Scientific role | Main limitation | Gate |
|---|---|---|---|---|---|---|
| Study boundary — primary | City of Austin Full Purpose boundary, 2019-era FeatureServer | **near-period support** | polygon | geographic support | not exact 2018 and not utility boundary | source PASS / overlap OPEN |
| Study boundary — sensitivity | current City jurisdiction layer | **CURRENT_SENSITIVITY** | polygon | boundary sensitivity | current state differs from 2018/2019 | sensitivity only |
| Austin Energy service area | Austin Energy / City FeatureServer | **CURRENT_CROSSCHECK** | polygon | service-area cross-check | no feeder topology | source PASS / cross-check OPEN |
| Power topology + loads | NREL/OEDI SMART-DS `v1.0/2018/AUS/P5U` | **EXACT_2018_BENCHMARK** | OpenDSS + bus coordinates; 15-min loads | primary synthetic power benchmark | synthetic, not Austin Energy topology | source PASS / raw + geographic QA OPEN |
| Road topology — primary | TxDOT Roadway Inventory 2018 | **EXACT_2018_ANNUAL_INVENTORY** | polyline; EPSG:4269 | primary structural transport topology | topology cleaning/direction/travel dynamics still require QA | source PASS / materialization + topology OPEN |
| Road — sensitivity | Austin CTN | **CURRENT_SENSITIVITY** | live polyline; EPSG:2277 | semantic/topological cross-check | created 2017–2018 but updated regularly; not frozen 2018 | sensitivity only |
| Road — sensitivity | Austin current street centerline | **CURRENT_SENSITIVITY** | polyline | geometry cross-check | current state | sensitivity only |
| Radar traffic observations | City Radar Traffic Counts | **HISTORICAL_2018_OBSERVATION** when restricted to 2018 | 15 min | traffic calibration/validation candidate | correlated rows; incomplete/nonuniform detector coverage | source PASS / 2018 extraction OPEN |
| Radar sensor locations | City Travel Sensors | **RETROSPECTIVE_LOCATION_METADATA** | points / device metadata | KITS-ID spatial join for 2018 observations | later metadata; stationarity/history not automatically verified | source PASS / 2018 join OPEN |
| Traffic signals — raw | City `TRANSPORTATION_signals2` | **CURRENT_NONVERSIONED_SOURCE** | point; daily updated live service | source for retrospective filtering | not a historical snapshot | source PASS |
| Traffic signals — derived | filter raw signals by non-null `TURN_ON_DATE <= 2018-12-31` | **RETROSPECTIVE_2018_SUBSET** | point | semisynthetic P→T mapping candidate | survivor subset; removed post-2018 signals may be absent | extraction OPEN |
| Floodplain | City/FEMA Floodplain | **STATIC_SCENARIO_SUPPORT** | polygon | spatial susceptibility / synthetic flood-scenario support | not event-time depth or hydrograph; not automatically 2018 geometry | source PASS / intersection OPEN |
| Repair access | thesis-derived from qualified 2018 road graph + damaged synthetic power assets + declared crew origin | scenario-dependent | graph path | T→P mechanism | travel time/passability require separate evidence | NOT YET COMPUTABLE |

## 3. Temporal evidence contract

The active temporal semantics are controlled by `AUSTIN_TEMPORAL_EVIDENCE_PROTOCOL_V1.md`.

```math
G_{time}=G_{sig}G_{traffic}G_{flood}.
```

### Signal gate

```math
\mathcal S_{sig}^{2018*}
=
\{s:\operatorname{TURN\_ON\_DATE}(s)\neq\varnothing,
\operatorname{TURN\_ON\_DATE}(s)\le2018\text{-}12\text{-}31\}.
```

`G_sig` requires a nonempty retained subset inside final spatial support, reported missing-date rate, retained survivorship-bias warning, and no claim of a complete 2018 inventory.

### Traffic gate

`G_traffic` requires genuine 2018 radar observations, unique/non-null KITS-ID spatial join, retained-road overlap, and a chronological/event-block development/validation split. Random row-level splitting is prohibited.

### Flood gate

`G_flood` requires spatial intersection with retained assets and preserves the label `STATIC_SCENARIO_SUPPORT`. A historical event claim requires separately qualified event-specific intensity/depth/time evidence.

## 4. Data-QC record

Every materialized object must freeze:

```text
source organization; dataset/product; temporal role; vintage/update;
acquisition UTC; raw endpoint; license/access; byte count; SHA-256;
source CRS; analysis CRS; feature/row count; missingness/null geometry;
duplicates; spatial/temporal resolution; variables/units; time zone;
uncertainty/limitations; RQ/H role; development/validation/test role;
processing code + Git commit; PASS/FAIL/BLOCKED state.
```

No `w_ij`, `delta_ij`, `tau_ij`, threshold, probability law, speed, travel time, flood depth, passability, or repair duration may be inferred from metadata or geometry alone.

## 5. Frozen G0–G8 gates

```math
G_{AUS}=\prod_{k=0}^{8}G_k.
```

- **G0 canonical consistency:** RQ0 + RQ1–RQ7 / SO1–SO7 and canonical H1–H5 semantics unchanged.
- **G1 power materialization:** P5U OpenDSS/coordinates hashed, parsed, connected/simulatable.
- **G2 common spatial support:** retained layers have nonempty overlap under explicit CRS transformations.
- **G3 transport topology:** TxDOT 2018 clip nonempty; topology QA passes; current City-road differences quantified as sensitivity.
- **G4 traffic observations:** ≥1 genuine 2018 radar detector family passes temporal/spatial join and chronological/event-block role freeze.
- **G5 P→T mapping:** ≥1 signal from the retrospective 2018 survivor subset maps reproducibly to an eligible synthetic power component; mapping remains semisynthetic.
- **G6 T→P repair access:** ≥1 repairable synthetic power component has qualified structural road access; travel time remains open until traffic/passability dynamics are qualified.
- **G7 flood exposure:** static flood-support layer intersects retained assets; dynamic hazard claims require separate event evidence.
- **G8 QC/provenance:** immutable identity, hashes, counts, CRS, missingness, temporal role, license/access, code/commit and data-role metadata pass.

Current state:

```text
G0 = PASS
G1 = OPEN
G2 = OPEN
G3 = SOURCE QUALIFIED / MATERIALIZATION + TOPOLOGY OPEN
G4 = SOURCE/TEMPORAL SEMANTICS QUALIFIED / 2018 JOIN + OVERLAP OPEN
G5 = SOURCE/TEMPORAL SEMANTICS QUALIFIED / RETROSPECTIVE EXTRACTION + MAPPING OPEN
G6 = OPEN
G7 = SOURCE/TEMPORAL SEMANTICS QUALIFIED / INTERSECTION OPEN
G8 = OPEN
G_time = OPEN
FINAL = NOT YET PASS
```

## 6. Deterministic execution order

```math
\text{P5U raw power}
\rightarrow\text{spatial support}
\rightarrow\text{TxDOT 2018 roads}
\rightarrow\text{road topology QA}
\rightarrow\text{2018 radar extraction+KITS join}
\rightarrow\text{retrospective signal subset}
\rightarrow\text{static flood overlay}
\rightarrow P\to T
\rightarrow T\to P
\rightarrow\text{freeze final case}.
```

If P5U fails any mandatory pre-result gate, remaining Austin SMART-DS urban subregions must be evaluated under the same rules without inspecting H1–H5 outcomes.

## 7. Primary evidence registry

1. NREL/OEDI SMART-DS: https://data.openei.org/submissions/2981
2. TxDOT annual roadway inventory: https://www.txdot.gov/data-maps/roadway-inventory.html
3. TxDOT 2018 roadway service: https://services.arcgis.com/KTcxiTD9dsQw4r7Z/ArcGIS/rest/services/TxDOT_Roadway_Inventory_2018/FeatureServer/0
4. City Radar Traffic Counts: https://data.austintexas.gov/resource/i626-g7ub
5. City Travel Sensors: https://data.austintexas.gov/resource/6yd9-yz29
6. City Traffic/Pedestrian Signals: https://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/TRANSPORTATION_signals2/FeatureServer/0
7. City/FEMA Floodplain: https://maps.austintexas.gov/gis/rest/Shared/Floodplain/MapServer/1

Source existence is never equivalent to final case admissibility.
