# Latest Scientific Restart Pointer

> **Current question authority (2026-09-17):** [CANONICAL_RQ_SO_HYPOTHESES_V3.md](CANONICAL_RQ_SO_HYPOTHESES_V3.md). RQ0 is overarching; RQ1–RQ7 correspond to SO1–SO7. H1–H5 retain their identifiers. RQ1/SO1 and RQ2/SO2 supply developmental evidence to H1; RQ3/SO3 → H1; RQ4/SO4 → H2; RQ5/SO5 → H3; RQ6/SO6 → H4; RQ7/SO7 → H5, with H4 intervention-performance inputs.


**Updated:** 2026-09-17  
**Purpose:** live pointer to the latest H3 scientific endpoint and immediate admissible task.

## Read first

1. `SCIENTIFIC_CHECKPOINT_2026-09-16_MODEL_FAMILY_V1.md`
2. `EGMIV_TSP_THESIS_OPERATING_PROTOCOL_V1.md`
3. `CANONICAL_7_STAGE_FRAMEWORK_V2.md`
4. `CANONICAL_RQ_SO_HYPOTHESES_V3.md`
5. `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`
6. `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V7.md`
7. `H3_DEMONSTRATOR_FREEZE_V1.md`
8. `H3_HOUSTON_DATA_MATERIALIZATION_QA_V1.md`
9. `H3_HOUSTON_BOUNDARY_FREEZE_V1.md`
10. `H3_HOUSTON_BOUNDARY_EXECUTION_ATTEMPT_2026-09-17_V2.md`
11. `H3_SMARTDS_HOUSTON_PREEXTRACTION_V1.md`
12. `H3_SMARTDS_YEAR_QUALIFICATION_V1.md`
13. `H3_SMARTDS_ELECTRICAL_CLOSURE_AND_OPENDSS_QA_V1.md`
14. `H3_HGAC_TRANSPORT_SOURCE_AND_BASEYEAR_QUALIFICATION_V1.md`
15. `H3_HOUSTON_TRAFFIC_SIGNAL_SOURCE_AND_MATERIALIZATION_V1.md`
16. `H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md`
17. `H3_PREREGISTRATION_V1.md`
18. `H3_ALGORITHM_SELECTION_AND_VERIFICATION_V1.md`
19. `../methods/h3/materialize_houston_boundary.py`
20. `../methods/h3/inventory_smartds_houston.py`
21. `../methods/h3/materialize_smartds_houston_power.py`
22. `../methods/h3/qa_smartds_power_layer.py`
23. `../methods/h3/materialize_hgac_transport.py`
24. `../methods/h3/materialize_houston_traffic_signals.py`
25. `../config/h3_houston_power_source_v1.json`
26. `../config/h3_houston_transport_source_v1.json`
27. `../config/h3_houston_signal_source_v1.json`

## Thesis-only execution rule

```math
\boxed{
\text{Prompt}
\rightarrow
\text{Thesis destination}
\rightarrow
\text{Scientific question}
\rightarrow
\text{Evidence}
\rightarrow
\text{Mathematics}
\rightarrow
\text{Test}
\rightarrow
\text{Citation}
\rightarrow
\text{Thesis-ready output}.
}
```

```math
\boxed{\text{No thesis purpose}\Rightarrow\text{No research action}.}
```

Blocked execution may be bypassed only by scientifically independent preparation. Missing raw evidence must never be replaced by fabricated geometry, counts, thresholds, interfaces or model outputs.

## Current scientific endpoint

```math
\boxed{
\mathcal C_{H3}^{HOU}\text{ frozen}
\rightarrow
D_{\Omega}\text{ source/semantics frozen but byte QA blocked}
\rightarrow
Y_P^{H3}=2016\text{ SMART-DS qualified}
\rightarrow
Y_T^{H3}=2023\text{ H-GAC qualified}
\rightarrow
\boxed{D_S\text{ City traffic-signal source qualified + materializer prepared}}.
}
```

## Frozen H3 demonstrator

```math
\boxed{
\mathcal C_{H3}^{HOU}
=
\text{Houston Flood-Stress Coupled Power–Transportation Demonstrator}.
}
```

Primary claim type remains a geographically grounded **semisynthetic mechanism/decision-value experiment**, not reconstruction of Houston's actual 2017 grid, road state, outage chronology or restoration chronology.

Primary spatial support:

```math
\boxed{
\Omega_{HOU}:=\Omega_{core}=\operatorname{dissolve}(SERVICE\_TY=FULL).
}
```

`Omega_limited` remains separate. Exterior P/T elements may be retained only when required for physical/network closure and are excluded from service denominators unless independently justified.

## Boundary gate

City source and FULL/LIMITED semantics are frozen, but successful raw-byte/geometry execution remains unavailable:

```math
\boxed{
G_{\Omega,source}=1,
\qquad
G_{\Omega,bytes}=0,
\qquad
G_{\Omega,QA}=0.
}
```

Boundary byte/geometry QA is **NOT TESTED**, not scientifically failed.

## Power branch

```text
SMART-DS v0.9 / 2016 / Full_Texas / base_timeseries
```

```math
\boxed{
G_{P,source}=1,
\quad
G_{P,year}=1,
\quad
G_{P,prep}=1,
\quad
G_{P,inventory}=0,
\quad
G_{P,raw}=0,
\quad
G_{P,QA}=0.
}
```

Prepared chain:

```math
G_{\Omega,QA}=1
\rightarrow
\text{Houston candidate substations}
\rightarrow
\text{raw SMART-DS freeze}
\rightarrow
\text{OpenDSS compile/solve QA}
\rightarrow
N_P,M_P.
```

No Houston power asset IDs, graph dimensions, service denominator or convergence result are claimed yet.

## Transportation branch

```text
H-GAC 2025 Transportation Conformity
Model base year: 2023
Primary network: C.4 Roadway Network Files
Support: C.3 Link Listing and Capacity Staging; C.1 Travel Model Validation
```

```math
\boxed{
G_{T,source}=1,
\quad
G_{T,year}=1,
\quad
G_{T,prep}=1,
\quad
G_{T,raw}=0,
\quad
G_{T,inventory}=0,
\quad
G_{T,QA}=0.
}
```

Prepared raw acquisition:

```text
methods/h3/materialize_hgac_transport.py
```

Raw regional acquisition may occur before `G_Omega_QA=1`; final Houston link/node selection may not.

## Traffic-signal / P→T interface branch

Primary source:

```text
City of Houston Public Works
TDO/Traffic_Management_gx
Traffic Signal — MapServer layer 26
https://geogimsms.houstontx.gov/arcgis/rest/services/TDO/Traffic_Management_gx/MapServer/26
```

The parent service identifies layer 26 as `Traffic Signal`, reports City of Houston Public Works copyright, spatial reference 102740 / EPSG:2278, query support for JSON/GeoJSON/PBF, and `MaxRecordCount=2000`.

The frozen mechanism remains

```math
\boxed{
\text{power availability}
\rightarrow
\text{traffic-signal operation}
\rightarrow
\text{transport performance}.
}
```

Signal locations do **not** reveal actual CenterPoint feeder assignments or feature-level backup-power states.

Prepared materializer:

```text
methods/h3/materialize_houston_traffic_signals.py
```

It freezes layer metadata and count query, paginates the complete feature set, preserves every raw GeoJSON page, records byte sizes/SHA-256, verifies unique object IDs and point coordinates, and writes a processed WGS84 derivative. It does not clip to `Omega_core` or perform P/T mappings.

Current signal gate:

```math
\boxed{
G_{S,source}=1,
\quad
G_{S,prep}=1,
\quad
G_{S,raw}=0,
\quad
G_{S,core}=0,
\quad
G_{S,roadmap}=0,
\quad
G_{S,powermap}=0,
\quad
G_{S,QA}=0.
}
```

After boundary closure:

```math
\mathcal S_{sig}^{HOU}
=
\{j:x_j\in\Omega_{core}\}.
```

Then freeze signal-to-road and signal-to-synthetic-power mappings before inspecting H3 outcomes. Mapping proximity is a demonstrator construction, not an observed utility service assignment.

## Current overall gate state

```math
\boxed{
G_{case}=1,
\quad
G_{source}=1,
\quad
G_{\Omega,QA}=0,
\quad
G_{P,prep}=1,
\quad
G_{T,prep}=1,
\quad
G_{S,prep}=1,
\quad
G_K=0,
\quad
G_U=0,
\quad
G_{\Pi}=0,
\quad
G_{alg}=0.
}
```

H3 confirmatory execution remains **NOT AUTHORIZED**.

## Immediate next admissible task

The next independent source required by the frozen demonstrator is the observed Harvey flood field:

```math
\boxed{
D_F\text{ source qualification + materialization preparation}
\rightarrow
\text{depth/inundation provenance}
\rightarrow
\text{raw hash/CRS/raster-polygon QA}.
}
```

This can be prepared without changing the still-open P/T/signal geographic-selection gates.

When network-enabled execution becomes available, the pending raw tasks are:

```text
1. Houston boundary bytes + geometry QA;
2. H-GAC C.1/C.3/C.4 raw bytes + archive inventory;
3. City traffic-signal raw pages + signal QA;
4. 2016 SMART-DS Houston candidate inventory/materialization after boundary QA.
```

After `G_Omega_QA=1` and all raw layers are frozen:

```text
1. construct Houston power and road graphs;
2. select Houston-core signals;
3. overlay Harvey hazard;
4. construct/QA P→T and T→P mappings;
5. report actual P/T/signal/interface dimensions;
6. populate the seven-object H3 case registry;
7. qualify uncertainty;
8. only then select/verify the H3 solver.
```

## Hard prohibition

Do not invent geometry, counts, backup-power states, actual signal feeders, network dimensions, hazard probabilities, thresholds or mapping coverage; do not use maintenance requests as the canonical signal inventory; and do not execute confirmatory H3 until every required gate closes.

