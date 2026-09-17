# Austin Road-Vintage Protocol v1

**Status:** PRE-DATA FREEZE — source hierarchy fixed; spatial overlap and topology remain unexecuted.

## Scientific question

Which roadway source is temporally and semantically admissible for the 2018 SMART-DS Austin case without silently treating a current road layer as 2018 truth?

## Frozen source hierarchy

### Primary — exact annual vintage

**TxDOT Roadway Inventory 2018**

- Feature service: `https://services.arcgis.com/KTcxiTD9dsQw4r7Z/ArcGIS/rest/services/TxDOT_Roadway_Inventory_2018/FeatureServer/0`
- Geometry: polyline.
- Inventory year: 2018.
- Source family: TxDOT Geospatial Roadway Inventory Database (GRID).
- Role: primary 2018 transport-topology evidence for the Austin case after P5U spatial clipping and topology QA.
- The statewide service is queried only inside the frozen SMART-DS P5U acquisition envelope and is materialized through ID-first pagination.

### Sensitivity 1 — City semantic cross-check

**City of Austin Comprehensive Transportation Network (CTN)**

- Layer: `https://maps.austintexas.gov/arcgis/rest/services/Shared/Transportation_1/MapServer/22`
- Created by City transportation staff between 2017 and 2018.
- Official City source for roadway classifications and defining characteristics.
- The live service is updated regularly; therefore it is **not** an archival 2018 snapshot.
- Role: current semantic/topological sensitivity cross-check only.

### Sensitivity 2 — current City centerline

**City of Austin Street Centerline**

- Existing repository source retained unchanged.
- Role: current-geometry sensitivity/QC only.
- It must not be described as 2018 roadway truth.

## Frozen admissibility rule

The road gate may pass only if all of the following hold:

1. the TxDOT 2018 source materializes with complete ID-first pagination and immutable hashes;
2. the clipped primary layer contains usable polyline features intersecting the candidate P5U support;
3. topology QA passes after explicit geometric cleaning/snap rules;
4. repair-access targets are reachable under the declared structural routing model;
5. differences against CTN/current City centerline are quantified as sensitivity, not silently reconciled;
6. no travel time is inferred from distance alone; travel-time dynamics require a separately qualified traffic model;
7. no road layer is selected after inspecting H1–H5 outcomes.

## Prohibitions

- Do not call the live CTN layer a frozen 2018 road network.
- Do not substitute a current City centerline for the TxDOT 2018 inventory without a versioned scientific decision.
- Do not interpret spatial coincidence as a causal P↔T dependency.
- Do not fabricate speed, capacity, travel time, passability, or repair-delay values from geometry alone.
- Do not treat successful download as topology or case admissibility.

## Decision state

```text
TxDOT 2018 source qualification: PASS
Raw materialization: OPEN
P5U overlap: OPEN
Topology QA: OPEN
Repair-access routing: OPEN
Current-source sensitivity: OPEN
Final road admissibility: NOT YET PASS
```

## Evidence anchors

- TxDOT Roadway Inventory annual-data page: https://www.txdot.gov/data-maps/roadway-inventory.html
- TxDOT 2018 feature service: https://services.arcgis.com/KTcxiTD9dsQw4r7Z/ArcGIS/rest/services/TxDOT_Roadway_Inventory_2018/FeatureServer/0
- City CTN layer: https://maps.austintexas.gov/arcgis/rest/services/Shared/Transportation_1/MapServer/22
