# H3 Houston Traffic-Signal Source and Materialization v1.0

**Status:** SOURCE QUALIFIED / RAW MATERIALIZATION OPEN  
**Date:** 2026-09-17  
**Protocol:** EGMIV–TSP  
**Case:** `H3-HOU-FLOOD-V1`  
**Thesis destination:** Chapter 4 — H3 P→T interface realization and provenance

> This file qualifies the City of Houston traffic-signal GIS source required by the frozen P→T mechanism. It does not claim that signal features have already been downloaded, clipped to `Omega_core`, or mapped to SMART-DS assets.

---

## 1. Scientific destination

The signal layer supplies the transport-side interface objects for

```math
\boxed{
\text{power availability}
\rightarrow
\text{traffic-signal operation}
\rightarrow
\text{transport performance}.
}
```

For each signal `j`, the demonstrator retains the frozen structural form

```math
\boxed{
a_j^{sig}(t)
=\phi_j\left(S_{P,\mu(j)}(t),b_j(t)\right),
}
```

where `mu(j)` is the reproducible synthetic power mapping and `b_j` is a separately qualified backup-power state. This dataset supplies signal locations only; it does **not** observe the actual utility feeder serving each signal.

---

## 2. Qualified authoritative source

Primary source:

```text
City of Houston Public Works
TDO/Traffic_Management_gx
ArcGIS MapServer
Traffic Signal — layer 26
https://geogimsms.houstontx.gov/arcgis/rest/services/TDO/Traffic_Management_gx/MapServer/26
```

The City-hosted service identifies `Traffic Signal` as layer 26 under the Traffic Management map service. The parent service reports:

```text
Copyright: City of Houston Public Works;
Spatial reference: 102740 / EPSG:2278;
Supported query formats: JSON, GeoJSON, PBF;
MaxRecordCount: 2000.
```

The source is therefore admissible for location-level P→T interface construction:

```math
\boxed{G_{S,source}=1.}
```

No claim is made yet about the current number of signal records, field completeness, null geometry, duplicate locations, or Houston-core coverage.

---

## 3. Why the maintenance-request layer is not the primary signal inventory

A separate City-hosted `Traffic Signals Maintain - Open` layer exists, but it represents open maintenance/service-request records rather than the canonical inventory of traffic-signal assets. It is therefore not used as the primary H3 signal-location source.

The H3 source contract requires an asset/location layer, not a maintenance-case layer.

---

## 4. Raw materialization contract

Executable utility:

```text
methods/h3/materialize_houston_traffic_signals.py
```

The utility must:

```text
1. retrieve and freeze layer metadata;
2. determine the server-declared object-ID field rather than assuming one;
3. query the full signal feature set with pagination;
4. request WGS84 output for reproducible spatial QA while preserving metadata/native CRS provenance;
5. preserve every raw page unchanged;
6. compute SHA-256 and byte size for metadata and every page;
7. combine pages only as a processed derivative;
8. verify point geometry, unique object IDs, finite coordinates and page completeness;
9. record feature count and missing/null geometry count;
10. never silently drop duplicate IDs or malformed features.
```

Because the service advertises a 2,000-record maximum, pagination is mandatory unless a byte-level query proves that the total is below the limit.

---

## 5. Boundary and Houston-core rule

Raw City signal acquisition is independent of `G_Omega_QA`; therefore the complete source layer may be frozen before the Houston boundary materialization succeeds.

Final H3 signal selection is not independent:

```math
\boxed{
G_{\Omega,QA}=1
\Rightarrow
\mathcal S_{sig}^{HOU}
=\{j:x_j\in\Omega_{core}\}
\text{ may be constructed}.
}
```

No feature may be declared an H3 Houston signal solely from the map-service extent, a hand-drawn bounding box, or a city-name field.

Signals outside `Omega_core` may be retained only as explicit boundary/context objects if required for transportation-network continuity; they are not automatically included in the primary interface denominator.

---

## 6. Signal-to-road association

After the H-GAC Houston roadway graph exists, each retained signal must be associated with a physical intersection/node or nearest admissible road junction under a frozen spatial rule.

The association must report at minimum:

```text
signal object ID;
signal coordinate;
road node/intersection ID;
association distance;
association method;
ambiguous-match flag;
unmatched flag.
```

A maximum admissible signal-to-road mapping distance remains **OPEN** until the actual network resolution and mapping residual distribution are observed. It must not be selected after inspecting H3 outcomes.

---

## 7. Signal-to-power association

The actual City signal feeder is not public and must not be inferred as observed truth. The primary demonstrator uses a reproducible synthetic mapping:

```math
\boxed{
\mu_{P\to T}(j)
=\operatorname{argmin}_{i\in\mathcal V_P^{eligible}}d(j,i)
}
```

or a superior feeder/service-area rule if SMART-DS geometry supports it after power QA.

For every mapped signal, freeze:

```text
signal ID;
synthetic power asset/node ID;
mapping method;
distance;
eligibility rule;
uncertainty/sensitivity class.
```

A mapped pair is a **demonstrator interface**, not evidence of the real CenterPoint service assignment.

---

## 8. Backup-power evidence boundary

The City signal GIS layer alone does not establish whether a particular signal has UPS, battery, generator or other backup supply. Therefore

```math
\boxed{
\text{signal location data}
\neq
\text{backup-power state data}.
}
```

`b_j(t)` remains unknown unless a separate authoritative source identifies backup capability. If no feature-level evidence is available, backup behavior must enter through declared scenarios/sensitivity bounds rather than fabricated probabilities.

---

## 9. Required QA quantities

After materialization and after boundary closure, report:

```math
N_S^{raw},\qquad
N_S^{core},\qquad
N_S^{null},\qquad
N_S^{dup},\qquad
r_{road},\qquad
r_{P\to T}.
```

where

```math
r_{road}=\frac{N_{signal\to road}}{N_S^{core}},
\qquad
r_{P\to T}=\frac{N_{signal\to power}}{N_S^{core}}.
```

Also report mapping-distance distributions, unmatched records, duplicate coordinates, invalid coordinates, and exclusions.

No minimum acceptable mapping-rate threshold is assigned in this file. Any such criterion must be preregistered before H3 outcome inspection.

---

## 10. Gate state

```math
\boxed{
G_{S,source}=1,
\qquad
G_{S,prep}=1,
\qquad
G_{S,raw}=0,
\qquad
G_{S,core}=0,
\qquad
G_{S,roadmap}=0,
\qquad
G_{S,powermap}=0,
\qquad
G_{S,QA}=0.
}
```

No signal count or mapping result is claimed until executable materialization succeeds.

---

## 11. Exact next sequence

```math
\boxed{
\text{City signal raw bytes}
\rightarrow
\text{SHA256 + metadata/page QA}
\rightarrow
G_{\Omega,QA}=1
\rightarrow
\text{Houston-core signal selection}
\rightarrow
\text{signal-to-road mapping}
\rightarrow
\text{signal-to-power mapping}
\rightarrow
\text{interface QA}.
}
```

Execution command:

```bash
python methods/h3/materialize_houston_traffic_signals.py \
  --root data/H3-HOU-FLOOD-V1
```

---

## 12. Hard prohibitions

Do not:

```text
claim the actual utility feeder serving any signal;
use the open maintenance-request layer as the canonical signal inventory;
assign backup-power states without source evidence;
clip to Houston before G_Omega_QA=1;
choose a signal-to-road or signal-to-power distance threshold after H3 outcomes are known;
interpret proximity as observed causal service assignment;
invent signal counts, mapping rates or interface coverage.
```

---

## References

City of Houston Public Works. (n.d.). *Traffic Management* [ArcGIS MapServer]. https://geogimsms.houstontx.gov/arcgis/rest/services/TDO/Traffic_Management_gx/MapServer

Federal Highway Administration. (2023). *Traffic Signal Program Handbook* (FHWA-HOP-23-041). https://ops.fhwa.dot.gov/publications/fhwahop23041/
