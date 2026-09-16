# Latest Scientific Restart Pointer

**Updated:** 2026-09-17  
**Purpose:** live pointer to the latest H3 scientific endpoint and immediate admissible task.

## Read first

1. `SCIENTIFIC_CHECKPOINT_2026-09-16_MODEL_FAMILY_V1.md`
2. `EGMIV_TSP_THESIS_OPERATING_PROTOCOL_V1.md`
3. `CANONICAL_7_STAGE_FRAMEWORK_V2.md`
4. `CANONICAL_RQ_SO_HYPOTHESES_V2.md`
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
15. `H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md`
16. `H3_PREREGISTRATION_V1.md`
17. `H3_ALGORITHM_SELECTION_AND_VERIFICATION_V1.md`
18. `../methods/h3/materialize_houston_boundary.py`
19. `../methods/h3/inventory_smartds_houston.py`
20. `../methods/h3/materialize_smartds_houston_power.py`
21. `../methods/h3/qa_smartds_power_layer.py`
22. `../methods/h3/materialize_hgac_transport.py`
23. `../config/h3_houston_power_source_v1.json`
24. `../config/h3_houston_transport_source_v1.json`

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
\text{Framework/RQ/H closed}
\rightarrow
\mathcal C_{H3}^{HOU}\text{ frozen}
\rightarrow
D_{\Omega}\text{ source/semantics frozen}
\rightarrow
\text{boundary execution externally blocked}
\rightarrow
Y_P^{H3}=2016\text{ qualified}
\rightarrow
\text{SMART-DS materialization/OpenDSS QA prepared}
\rightarrow
\boxed{Y_T^{H3}=2023\text{ H-GAC transport source/base year qualified + raw acquisition prepared}}.
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

Primary claim type: geographically grounded semisynthetic mechanism/decision-value experiment, **not** historical reconstruction of Houston's actual 2017 grid, road state, outage chronology or restoration chronology.

Primary service domain:

```math
\boxed{
\Omega_{HOU}:=\Omega_{core}
=\operatorname{dissolve}(SERVICE\_TY=FULL).
}
```

`Omega_limited` remains a separate sensitivity/context domain. Exterior electrical/road elements may be retained only when physically required for model/network closure and are excluded from service denominators unless independently justified.

## Boundary gate

The City of Houston source and FULL/LIMITED semantics are frozen, but two GitHub-hosted execution attempts ended before usable runner steps were executed. No raw boundary artifact was produced.

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

## SMART-DS power branch

Frozen primary power source:

```text
SMART-DS version: v0.9
Year:             2016
Dataset:          Full_Texas
Scenario:         base_timeseries
```

```math
\boxed{Y_P^{H3}=2016.}
```

Prepared sequence:

```math
G_{\Omega,QA}=1
\rightarrow
\text{Houston candidate substations}
\rightarrow
\text{candidate raw materialization}
\rightarrow
\text{OpenDSS compile/solve QA}
\rightarrow
N_P,M_P.
```

Current power gate:

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

No Houston power asset IDs, graph dimensions, service denominator or convergence result are claimed yet.

## H-GAC transportation branch

Primary source family:

```text
Houston-Galveston Area Council (H-GAC)
2025 Transportation Conformity
C.4 Roadway Network Files
C.3 Link Listing and Capacity Staging
C.1 Travel Model Validation
```

The H-GAC conformity modeling system identifies the Travel Demand Model base year as 2023 and forecast years as 2026, 2030, 2040 and 2045. The primary H3 transport vintage is therefore frozen as

```math
\boxed{Y_T^{H3}=2023.}
```

This is a reproducibility/current-base-model choice for the semisynthetic demonstrator, not a claim that the 2023 network is historical Houston during Harvey.

H-GAC regional context (not Houston graph dimensions):

```text
8-county model region;
Cube Voyager environment;
four-step demand modeling;
5,263 TAZs total;
5,217 internal TAZs;
46 external zones/stations.
```

Prepared raw acquisition utility:

```text
methods/h3/materialize_hgac_transport.py
```

It preserves C.1/C.3/C.4 source bytes, records resolved URL/HTTP metadata/byte size/SHA-256, rejects HTML/error payloads, safely inventories ZIP archives, and preserves extracted members in `interim/` rather than modifying `raw/`.

Regional raw acquisition does not require Houston boundary QA. Final Houston link/node selection does.

The transport simulation and service graphs are kept distinct:

```math
\boxed{
\mathcal G_{T,sim}^{HOU}
\supseteq
\mathcal G_{T,svc}^{HOU}.
}
```

External/centroid/boundary connectors may be required for route continuity but are not automatically admitted to the `S_T` service denominator.

Current transport gate:

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

No C.4 archive contents, CRS, network fields, Houston link IDs, `N_T`, `M_T`, OD matrix or service denominator are claimed yet.

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

Because the Houston boundary gate blocks final geographic selection but not independent raw source acquisition, the next admissible task is:

```math
\boxed{
\text{materialize H-GAC C.1/C.3/C.4 raw bytes}
\rightarrow
\text{SHA256 + archive inventory}
\rightarrow
\text{freeze actual file/field semantics}.
}
```

Execute when a network-enabled runtime can reach H-GAC:

```bash
python methods/h3/materialize_hgac_transport.py \
  --root data/H3-HOU-FLOOD-V1 \
  --source all
```

In parallel, a successful network-enabled Houston boundary run remains required before any final Houston P/T geographic selection.

After `G_Omega_QA=1` and raw P/T materialization:

```text
1. complete SMART-DS Houston candidate inventory and OpenDSS QA;
2. inspect H-GAC C.4/C.3 field semantics and construct the Houston roadway graph;
3. materialize City traffic signals;
4. materialize Harvey flood raster/polygon;
5. construct and QA P→T and T→P mappings;
6. report actual P/T/interface dimensions;
7. populate the seven-object H3 case registry;
8. qualify uncertainty;
9. only then select/verify the H3 solver.
```

## Hard prohibition

Do not construct Houston geometry from published extents; do not substitute third-party P/T data solely for convenience; do not infer actual CenterPoint topology from SMART-DS; do not treat H-GAC regional TAZ counts as Houston network counts; do not infer C.4 field semantics before raw inspection; do not treat traffic counts as `S_T` without an evidence-matched mapping; do not invent network dimensions or thresholds; and do not execute confirmatory H3 until every required gate closes.
