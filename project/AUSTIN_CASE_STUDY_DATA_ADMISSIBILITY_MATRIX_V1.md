# Austin Case-Study + Data Admissibility Matrix v1

**Date:** 2026-09-18  
**Protocol:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation  
**Authority preserved:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md` + `CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Purpose:** determine whether an Austin Power–Transportation case can replace/extend the current demonstrator without changing RQ0, RQ1–RQ7, SO1–SO7, or H1–H5.  
**Current decision:** **CANDIDATE CASE ONLY — NOT YET FROZEN**.

> This package does not treat source availability as proof of case admissibility. Final case PASS requires feature-level geographic overlap, data-quality checks, and evidence-supported P↔T mechanisms in one exact Austin SMART-DS subregion.

---

## 1. Candidate case identity

```math
\boxed{
\mathcal C_{AUS}^{cand}
=
\left(
\text{SMART-DS v1.0},
2018,
\text{AUS},
P5U,
\Omega_{AUS},
\mathcal G_T,
\eta_F,
\mathbb I_{PT}
\right)
}
```

**Candidate ID:** `AUS-P5U-2018-V1`  
**Power dataset:** SMART-DS v1.0 / 2018 / AUS / P5U / `base_timeseries`  
**Candidate subregion:** `P5U`  
**Selection status:** **PROVISIONAL** — selected for data-admissibility testing because SMART-DS documentation places P5U in the central urban Austin group and recent published Austin-grid work treats P1U–P5U as urban regions. No hypothesis outcome has been inspected or used in this selection.  
**Freeze condition:** P5U becomes final only if all mandatory spatial/data/interdependency gates below pass. Otherwise the deterministic fallback is to evaluate the remaining AUS urban subregions under the same gate logic, without inspecting H1–H5 outcomes.

### Non-cherry-picking rule

The final Austin subregion is selected only from pre-result data admissibility:

```math
G_r
=
G_P
\land G_T
\land G_{traffic}
\land G_{haz}
\land G_{P\to T}
\land G_{T\to P}
\land G_{QC}.
```

A region cannot be selected because it produces a larger cascade, stronger effect size, better viability score, or more favorable hypothesis result.

---

## 2. Austin source matrix

| Object | Source / authority | Vintage | Spatial resolution / CRS | Temporal resolution | Primary variable(s) / unit | RQ / H role | Calibration / validation role | Known uncertainty / limitation | Evidence state | Current gate |
|---|---|---:|---|---|---|---|---|---|---|---|
| **Study boundary** | City of Austin `BOUNDARIES_jurisdictions` / Full Purpose boundary | current; daily updates | polygon; City GIS; commonly EPSG:2277 | snapshot | jurisdiction polygon | RQ1 / support all | neither; defines analysis support | administrative boundary ≠ utility service boundary | authoritative municipal GIS | **PASS source / spatial clip pending** |
| **Austin Energy service area** | City of Austin / Austin Energy `UTILITIESCOMMUNICATION_austin_energy_service_area` | current; daily updates | polygon | snapshot | electric service-area boundary | RQ1–RQ2 | cross-check only | does not reveal actual feeder topology; SMART-DS is synthetic | authoritative utility boundary; public domain | **PASS source / cross-check pending** |
| **Power topology + loads** | NREL/OEDI SMART-DS v1.0, Austin `AUS`; candidate `2018/P5U` | 2018 | OpenDSS network with geographic coordinates; subregion/substation/feeder hierarchy | load profiles at 15 min | buses, lines, transformers, loads, voltage, P/Q | RQ1–RQ3; H1 upstream; H3 upstream | development/calibration allowed; held-out use defined later | synthetic, not Austin Energy topology; P5U coordinates must be materialized and clipped | NREL/OEDI public synthetic benchmark | **PASS source / exact P5U geographic QA pending** |
| **Road topology** | City of Austin `TRANSPORTATION_street_segment` / Street Centerline | current; continuously maintained | polyline; EPSG:2277 | snapshot | segment ID, road class, speed limit, one-way, length | RQ1–RQ3; H1/H3 | structural model | addressing/network layer; routing connectivity and turn restrictions require QA | City GIS | **PASS source / P5U clip + network QA pending** |
| **Traffic observations — camera** | City of Austin `Camera Traffic Counts` (`sh59-i6y9`) + Travel Detectors | historical | detector/intersection linked to device-location table | **15 min** | volume veh/15 min; direction; movement; speed mph | RQ3/H1; demand calibration/validation candidate | candidate calibration + held-out validation after chronology audit | GRIDSMART devices retired; automated machine-vision counts not fully validated; speed calibration uncertain | City open data | **PASS source / detector-location P5U overlap pending** |
| **Traffic observations — radar** | City of Austin `Radar Traffic Counts` (`i626-g7ub`) + Travel Sensors | 2017-12-16 to 2021-09-09 | lane/detector linked to sensor-location table | **15 min** | volume veh/15 min; speed; occupancy | RQ3/H1; independent traffic-observation candidate | calibration/validation candidate | historical and discontinued; sensor coverage nonuniform | City open data | **PASS source / sensor-location P5U overlap pending** |
| **Traffic signals** | City of Austin `TRANSPORTATION_signals2` | current; daily updates | point; EPSG:2277 | snapshot | signal location/type/status fields | RQ2–RQ4; P→T mechanism | mapping/validation object | signal GIS does not publish actual supplying feeder or backup-power state | City Transportation authoritative asset GIS | **PASS source / P5U count + synthetic-power mapping pending** |
| **Flood exposure** | City of Austin / Watershed Protection FEMA Floodplain + Fully Developed Floodplain | current product; monthly/open service | polygon; EPSG:2277 | static hazard/exposure layer | flood-zone class; effective date | RQ2–RQ5; hazard exposure | scenario definition, not response calibration by itself | floodplain ≠ event-time flood depth; not a historical replay | City/FEMA-derived GIS | **PASS source for exposure / dynamic-hazard semantics pending** |
| **EV chargers** | Austin Energy public charging network / station map; AFDC may provide independent station inventory | current | station/port locations | snapshot + network-use summaries | location, port type/count; charging usage when available | RQ1–RQ2 context; optional P↔T extension | **not primary H1/H3 unless separately preregistered** | public map may require extraction; exact historical 2018 inventory may differ | Austin Energy / DOE-NREL AFDC | **PASS contextual source / not required for primary case** |
| **Repair access** | **Derived**, not a raw dataset: street graph + flood/passability + damaged power-asset locations + crew assumptions | scenario-specific | path on clipped road graph | dynamic | travel time/distance, route feasibility | RQ2–RQ5; T→P mechanism | model output / validation target if observations exist | cannot be computed until road/power/hazard layers are co-registered; crew/depot data may be assumption-bounded | thesis-derived object | **NOT YET COMPUTABLE** |

---

## 3. Data-quality fields that must be frozen for every materialized dataset

Every acquired object must record:

```text
source organization;
product/dataset title;
version or source update time;
acquisition UTC;
raw URL/API endpoint;
license/access terms;
raw byte count;
SHA-256;
original CRS;
final analysis CRS;
feature/row count;
spatial resolution;
temporal resolution;
variable names and units;
missingness/null geometry;
duplicate rate;
coordinate validity;
time-zone handling;
uncertainty/known limitations;
RQ/Hypothesis role;
calibration/development/test role;
processing script + Git commit;
PASS/FAIL/BLOCKED state.
```

No numerical `w_{ij}`, `delta_{ij}`, `tau_{ij}`, threshold, or probability distribution may be inferred from source metadata alone.

---

## 4. Exact Austin admissibility gates

### G0 — canonical thesis consistency

```math
G_0=1
```

iff all Austin artifacts preserve RQ0 + RQ1–RQ7 / SO1–SO7 and H1–H5 semantics. Austin is a case realization, not a new hypothesis architecture.

### G1 — SMART-DS P5U power materialization

PASS only if raw P5U OpenDSS + coordinate objects are materialized, hashed, parse successfully, and contain a connected/simulatable network with explicit geographic coordinates.

### G2 — common spatial support

PASS only if the retained P5U bus/line footprint has nonempty overlap with the declared Austin analysis boundary and all retained non-power layers are transformed to one declared analysis CRS.

### G3 — transport topology

PASS only if the clipped street-centerline graph has a nonempty connected component of sufficient size for OD/repair routing, with topology and one-way/speed attributes audited.

### G4 — traffic observations

PASS only if at least one qualified traffic-observation family has geocoded detectors inside the retained P5U transport footprint and supports a predeclared chronological development/test design.

### G5 — P→T mechanism

PASS only if at least one City traffic signal lies in the retained domain and can be mapped to an eligible synthetic power component under a frozen reproducible mapping rule. The mapping is a semisynthetic construct; it must never be labeled the actual Austin Energy feeder assignment.

### G6 — T→P mechanism

PASS only if at least one retained damaged/repairable power component has a road-access mapping to the clipped street graph so that restoration travel time is a well-defined graph-dependent quantity.

### G7 — hazard exposure

PASS only if the chosen flood layer intersects at least one retained power component or transport link. If dynamic flood depth/time is required, a separate time-varying/event dataset or explicit bounded scenario model must be qualified before confirmatory use.

### G8 — QC / provenance

PASS only if every mandatory dataset has immutable source identity, hash, CRS, row/feature counts, missingness/geometry QA, license, and processing provenance.

### Final case gate

```math
\boxed{
G_{AUS}
=G_0G_1G_2G_3G_4G_5G_6G_7G_8.
}
```

Current state:

```text
G0 canonical consistency                 = PASS
G1 P5U raw power materialization         = OPEN
G2 common spatial support                = OPEN
G3 transport topology                    = SOURCE QUALIFIED / CLIP OPEN
G4 traffic observations                  = SOURCE QUALIFIED / P5U OVERLAP OPEN
G5 P→T signal-power mapping              = SOURCE QUALIFIED / MAPPING OPEN
G6 T→P repair-access mapping             = OPEN
G7 flood exposure                        = SOURCE QUALIFIED / P5U INTERSECTION OPEN
G8 full QC/provenance                    = OPEN

FINAL AUSTIN CASE ADMISSIBILITY           = NOT YET PASS
```

This is intentionally stricter than a source-list exercise. The Austin case must not replace the current frozen demonstrator until `G_AUS=1` or an explicit version-controlled scientific decision accepts a documented semisynthetic limitation.

---

## 5. Frozen deterministic execution order

```math
\boxed{
\begin{aligned}
&\text{materialize P5U power coordinates/topology}\\
&\rightarrow \text{materialize Austin boundary + service area}\\
&\rightarrow \text{clip/QA road graph}\\
&\rightarrow \text{locate traffic detectors}\\
&\rightarrow \text{locate signals}\\
&\rightarrow \text{overlay flood layer}\\
&\rightarrow \text{build P→T mapping}\\
&\rightarrow \text{build T→P repair-access mapping}\\
&\rightarrow \text{freeze data manifest and exact subregion}.
\end{aligned}
}
```

If P5U fails a mandatory gate for objective data-coverage reasons, evaluate the remaining Austin SMART-DS urban regions using the same frozen gate definitions. Do not inspect H1–H5 performance before subregion selection.

---

## 6. Source registry used for v1 qualification

1. National Renewable Energy Laboratory / OEDI — *SMART-DS Synthetic Electrical Network Data OpenDSS Models for SFO, GSO, and AUS*: https://data.openei.org/submissions/2981
2. SMART-DS v1.0 user guide: https://oedi-data-lake.s3.amazonaws.com/SMART-DS/v1.0/User_Guide/Readme.pdf
3. City of Austin — Street Centerline: https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/TRANSPORTATION_street_segment/FeatureServer/0
4. City of Austin — Camera Traffic Counts API: https://dev.socrata.com/foundry/data.austintexas.gov/sh59-i6y9
5. City of Austin — Radar Traffic Counts API: https://dev.socrata.com/foundry/data.austintexas.gov/i626-g7ub
6. City of Austin — Traffic and Pedestrian Signals: https://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/TRANSPORTATION_signals2/FeatureServer
7. City of Austin — Austin Energy service area: https://data.austintexas.gov/Locations-and-Maps/Austin-Energy-Service-Area/i2t2-i3uy/about
8. City of Austin — FEMA Floodplain: https://maps.austintexas.gov/gis/rest/Shared/Floodplain/MapServer/1
9. City of Austin — Full Purpose boundary: https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/City_of_Austin_WFL1/FeatureServer/0
10. Austin Energy — EV charging network: https://austinenergy.com/green-power/plug-in-austin/EVerything-Charging
11. DOE/NREL AFDC — charging network data methods/download: https://afdc.energy.gov/stations/charging-networks

### Evidence interpretation

The sources establish that the required Austin data families exist and are publicly queryable. They do **not** by themselves prove that all features intersect P5U, that an actual traffic signal is supplied by a particular synthetic feeder, or that a floodplain polygon implies a time-varying flood depth. Those claims remain gated.
