# Austin Case-Study + Data Admissibility Matrix v2

**Date:** 2026-09-18  
**Protocol:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation  
**Authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md` + `CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Supersedes for active execution:** `AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V1.md`  
**Reason for version:** exact annual TxDOT 2018 roadway inventory was identified after v1; current City road layers are therefore demoted to sensitivity evidence.  
**Decision:** **CANDIDATE CASE ONLY — NOT YET ADMISSIBLE**.

## 1. Frozen candidate

```math
\mathcal C_{AUS}^{cand}
=
(\text{SMART-DS v1.0},2018,\text{AUS},P5U,\Omega,\mathcal G_T,\eta_F,\mathbb I_{PT}).
```

Candidate ID: `AUS-P5U-2018-V1`.

P5U remains provisional until every mandatory G0–G8 gate passes. Subregion selection is based only on pre-result admissibility; H1–H5 outcomes may not be inspected for case selection.

## 2. Active source matrix

| Object | Source | Year / vintage | Spatial resolution / CRS | Temporal resolution | Variable / unit | RQ / hypothesis | Calibration / validation role | Uncertainty / limitation | Evidence level | Gate |
|---|---|---|---|---|---|---|---|---|---|---|
| Study boundary — primary | City of Austin `City_of_Austin_full_purpose_boundary/FeatureServer/0` | last known edit 2019-04-04; closest frozen municipal support currently qualified | polygon; source EPSG:3857; output WGS84 | snapshot | jurisdiction polygon | RQ1 / all | support only | 2019 administrative boundary, not utility service boundary and not exact 2018 snapshot | municipal GIS | **SOURCE PASS / overlap OPEN** |
| Study boundary — sensitivity | City `BOUNDARIES_jurisdictions`, `JURISDICTION_TYPE='FULL'` | current | polygon; EPSG:2277 | snapshot | jurisdiction polygon | RQ1 | boundary sensitivity | current state can differ from 2018/2019 | municipal GIS | **SENSITIVITY ONLY** |
| Austin Energy service area | Austin Energy / City `UTILITIESCOMMUNICATION_austin_energy_service_area` | current | polygon; EPSG:2277 | snapshot | service-area support | RQ1–RQ2 | cross-check only | no feeder topology; cannot identify actual supply to synthetic buses/signals | E3 boundary evidence only | **SOURCE PASS / cross-check OPEN** |
| Power topology + loads | NREL/OEDI SMART-DS `v1.0/2018/AUS/P5U` | **2018** | OpenDSS topology + bus coordinates | load profiles 15 min | buses, lines, transformers, P/Q, voltage | RQ1–RQ3; H1/H3 upstream | development; validation role frozen later | synthetic network, not Austin Energy topology | benchmark source | **SOURCE PASS / raw + geographic QA OPEN** |
| Road topology — **primary** | **TxDOT Roadway Inventory 2018**, `TxDOT_Roadway_Inventory_2018/FeatureServer/0` | **2018 annual inventory** | statewide polyline; EPSG:4269; clip to P5U support | annual inventory snapshot | road geometry + inventory attributes | RQ1–RQ3; H1/H3 | structural model | topology cleaning/snap/direction semantics still require QA; geometry alone does not give travel time | official annual TxDOT inventory | **SOURCE PASS / materialization + clip + topology QA OPEN** |
| Road topology — sensitivity | City Comprehensive Transportation Network (CTN), layer 22 | live; created 2017–2018, updated regularly | polyline; EPSG:2277 | current service | roadway classification, lane/speed/one-way fields | RQ1–RQ3 | topology/attribute sensitivity | **not a frozen 2018 snapshot** | City official classification source | **SENSITIVITY ONLY** |
| Road topology — sensitivity | City `TRANSPORTATION_street_segment` | current | polyline; EPSG:2277 | current | street-centerline attributes | RQ1–RQ3 | geometry sensitivity | current state; routing semantics require QA | City GIS | **SENSITIVITY ONLY** |
| Traffic observations — radar | City `Radar Traffic Counts` (`i626-g7ub`) + sensor locations | 2017-12-16–2021-09-09; restrict confirmatory candidate data to frozen 2018 window | detector/lane point + observations | 15 min | count veh/15 min, speed, occupancy | RQ3/H1 | chronological/event-block development vs held-out candidate | nonuniform/discontinued coverage; no random-row split | City data | **SOURCE PASS / 2018 sensor overlap OPEN** |
| Traffic observations — camera | City `Camera Traffic Counts` (`sh59-i6y9`) + detector locations | historical | detector/intersection | 15 min | count, movement, speed | RQ3/H1 | secondary candidate | GRIDSMART retired; automated counts not fully validated; speed uncertainty | City data | **SOURCE PASS / overlap OPEN** |
| Traffic signals | City `TRANSPORTATION_signals2` | current | point; EPSG:2277 | snapshot | location/type/status | RQ2–RQ4; P→T | semisynthetic mapping object | no published actual supplying feeder or backup-power state | E3 asset location; mapping remains model construct | **SOURCE PASS / mapping OPEN** |
| Flood exposure | City/FEMA-derived FEMA Floodplain | current product | polygon; EPSG:2277 | static | flood-zone class | RQ2–RQ5 | hazard exposure/scenario support | floodplain ≠ event-time flood depth | City/FEMA-derived | **SOURCE PASS / intersection OPEN** |
| EV chargers | Austin Energy; AFDC candidate cross-check | current | points | snapshot | station/port | context/optional extension | not primary H1/H3 | historical 2018 charger state unresolved | public authoritative sources | **OPTIONAL** |
| Repair access | **Derived**: primary 2018 road graph + damaged synthetic power components + declared crew origin + hazard-dependent passability | scenario-specific | graph path | dynamic when traffic/passability model qualified | route feasibility, distance, later travel time | RQ2–RQ5; T→P | model output | travel time/passability/crew data cannot be invented | thesis-derived | **NOT YET COMPUTABLE** |

## 3. Mandatory data-QC record

Every materialized object must freeze:

```text
source organization; dataset/product; vintage/update; acquisition UTC;
raw endpoint; license/access; byte count; SHA-256; source CRS;
analysis CRS; feature/row count; missingness/null geometry; duplicates;
spatial and temporal resolution; variables and units; time zone;
uncertainty/limitations; RQ/H role; development/validation/test role;
processing code + Git commit; PASS/FAIL/BLOCKED state.
```

No `w_ij`, `delta_ij`, `tau_ij`, threshold, probability law, travel time, speed, passability, or repair duration may be inferred from metadata or geometry alone.

## 4. Frozen gates

```math
G_{AUS}=\prod_{k=0}^{8}G_k.
```

- **G0 canonical consistency:** RQ0 + RQ1–RQ7 / SO1–SO7 and H1–H5 semantics unchanged.
- **G1 power materialization:** P5U OpenDSS/coordinates hashed, parsed, connected/simulatable.
- **G2 common spatial support:** retained layers have nonempty overlap and declared CRS transformation.
- **G3 transport topology:** **TxDOT 2018** primary clip is nonempty and topology QA passes; differences against both live City sources are quantified as sensitivity.
- **G4 traffic observations:** at least one 2018-qualified detector family overlaps the retained transport support with chronological/event-block development/held-out roles.
- **G5 P→T:** at least one retained signal is mapped reproducibly to an eligible synthetic power component; mapping is explicitly semisynthetic.
- **G6 T→P:** at least one repairable synthetic power component has a qualified road-access route; travel time remains open until traffic dynamics are qualified.
- **G7 hazard exposure:** flood layer intersects retained power or transport assets; dynamic flood depth/time requires separate evidence/scenario model.
- **G8 QC/provenance:** immutable identity, hashes, counts, CRS, missingness, license/access, code/commit and role metadata pass.

Current state:

```text
G0 = PASS
G1 = OPEN
G2 = OPEN
G3 = SOURCE QUALIFIED (TXDOT 2018) / MATERIALIZATION + TOPOLOGY OPEN
G4 = SOURCE QUALIFIED / 2018 SPATIAL OVERLAP OPEN
G5 = SOURCE QUALIFIED / SEMISYNTHETIC MAPPING OPEN
G6 = OPEN
G7 = SOURCE QUALIFIED / INTERSECTION OPEN
G8 = OPEN
FINAL = NOT YET PASS
```

## 5. Deterministic execution order

```math
\text{P5U raw power}
\rightarrow \text{boundary/service support}
\rightarrow \text{TxDOT 2018 road clip + topology QA}
\rightarrow \text{City road sensitivity}
\rightarrow \text{2018 traffic-sensor overlap}
\rightarrow \text{signals}
\rightarrow \text{flood overlay}
\rightarrow P\to T
\rightarrow T\to P
\rightarrow \text{freeze manifest/subregion}.
```

If P5U fails a mandatory pre-result data gate, evaluate remaining Austin SMART-DS urban subregions under the same definitions without inspecting H1–H5 outcomes.

## 6. Primary evidence registry

1. NREL/OEDI SMART-DS: https://data.openei.org/submissions/2981
2. TxDOT annual roadway inventory: https://www.txdot.gov/data-maps/roadway-inventory.html
3. TxDOT 2018 roadway feature service: https://services.arcgis.com/KTcxiTD9dsQw4r7Z/ArcGIS/rest/services/TxDOT_Roadway_Inventory_2018/FeatureServer/0
4. City CTN layer 22: https://maps.austintexas.gov/arcgis/rest/services/Shared/Transportation_1/MapServer/22
5. City Traffic/Pedestrian Signals: https://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/TRANSPORTATION_signals2/FeatureServer/0
6. City Radar Traffic Counts: https://data.austintexas.gov/resource/i626-g7ub
7. City Camera Traffic Counts: https://data.austintexas.gov/resource/sh59-i6y9
8. City FEMA Floodplain: https://maps.austintexas.gov/gis/rest/Shared/Floodplain/MapServer/1

Source existence is not case admissibility. Final PASS requires executed feature-level evidence for the exact frozen subregion.
