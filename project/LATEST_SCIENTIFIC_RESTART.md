# Latest Scientific Restart Pointer

**Updated:** 2026-09-17  
**Purpose:** single live pointer to the latest immutable checkpoint, thesis-only operating protocol, document controls, H3 demonstrator, data-materialization state, boundary freeze, and immediate next admissible task.

## Read first

1. `SCIENTIFIC_CHECKPOINT_2026-09-16_MODEL_FAMILY_V1.md`
2. `AUTONOMOUS_EXECUTION_STATUS.md`
3. `EGMIV_TSP_THESIS_OPERATING_PROTOCOL_V1.md`
4. `STAGE_MODEL_FAMILY_SELECTION_GATE_V1.md`
5. `CANONICAL_7_STAGE_FRAMEWORK_V2.md`
6. `CANONICAL_RQ_SO_HYPOTHESES_V2.md`
7. `RESEARCH_REASONING_PROTOCOL.md`
8. `../thesis/00_governance/THESIS_MASTER_OUTLINE.md`
9. `../thesis/00_governance/THESIS_PAGE_BUDGET_160_V1.md`
10. `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`
11. `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V7.md`
12. `H3_DEMONSTRATOR_FREEZE_V1.md`
13. `H3_HOUSTON_DATA_MATERIALIZATION_QA_V1.md`
14. `H3_HOUSTON_BOUNDARY_FREEZE_V1.md`
15. `H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md`
16. `H3_PREREGISTRATION_V1.md`
17. `H3_ALGORITHM_SELECTION_AND_VERIFICATION_V1.md`
18. `../methods/h3/fetch_houston_boundary.py`

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

Online research must be targeted to a declared thesis evidence deficit and stop when the object is qualified or its evidence boundary is documented. External scientific claims require adjacent verified APA 7 author–date citations.

## Document-control rule

```math
\boxed{P_{\rm total}=160\ \text{pages}.}
```

This is an internal scope-control target, not an ASU page-count requirement.

```math
\boxed{\text{Remove repetition, not science}.}
```

## Current scientific endpoint

```math
\boxed{
\text{Framework/RQ/H closed}
\rightarrow
\text{EGMIV--TSP active}
\rightarrow
\text{H3 service/state/time semantics structurally qualified}
\rightarrow
\mathcal C_{H3}^{HOU}\text{ demonstrator frozen}
\rightarrow
\text{P/T/signal/flood source families qualified}
\rightarrow
\boxed{D_{\Omega}\text{ source + domain semantics frozen}}.
}
```

The seven H3 threshold/state/time objects remain structurally qualified but case-specific numeric realizations remain open:

```math
\{s_P^{\min},s_T^{\min},s_{P,rec},s_{T,rec},F,T_V,T_R\}.
```

## Frozen H3 demonstrator

```math
\boxed{
\mathcal C_{H3}^{HOU}
=
\text{Houston Flood-Stress Coupled Power–Transportation Demonstrator}.
}
```

```text
Case type: geographically grounded semisynthetic mechanism-validation demonstrator.
Power: Texas combined T&D / SMART-DS Houston subset.
Transport: H-GAC roadway/model/traffic Houston subset.
P→T: traffic-signal electricity dependency.
T→P: repair-crew accessibility/travel-time dependency.
Hazard: USGS/FEMA Hurricane Harvey flood-depth/inundation stress field.
Primary claim type: mechanism/decision-value, not historical 2017 reconstruction.
```

The common flood field is not treated as a P↔T causal dependency. Actual utility feeder-to-signal/facility connections are not claimed; cross-layer mappings are reproducible demonstrator constructions and must be validated/sensitivity-tested.

## Data-materialization state

`H3_HOUSTON_DATA_MATERIALIZATION_QA_V1.md` qualifies the source families and freezes the QA protocol.

```text
D_P: Texas combined T&D / SMART-DS v0.9 public OEDI data;
D_T: H-GAC 2025 roadway/model/link/traffic source family;
D_S: City of Houston Traffic Signal GIS layer;
D_F: USGS/FEMA Harvey flood-depth/inundation data;
D_Omega: City of Houston city-limit source and semantics now frozen.
```

Current general source gate:

```math
\boxed{
G_{source,P}=G_{source,T}=G_{source,S}=G_{source,F}=1.
}
```

## Houston boundary freeze

`H3_HOUSTON_BOUNDARY_FREEZE_V1.md` closes the source/semantic deficit for `D_Omega`.

Primary authoritative source:

```text
City of Houston / MyCity Houston
HoustonMap/Administrative_Boundary/MapServer/0
Layer: Houston City Limit
```

The City layer distinguishes `SERVICE_TY=FULL` and `SERVICE_TY=LIMITED`. Because limited-purpose annexations do not carry the same general-purpose municipal service regime, the H3 spatial support is now explicitly separated:

```math
\boxed{
\Omega_{legal}=\operatorname{dissolve}(FULL\cup LIMITED),
}
```

```math
\boxed{
\Omega_{core}=\operatorname{dissolve}(FULL),
\qquad
\Omega_{HOU}:=\Omega_{core},
}
```

```math
\boxed{
\Omega_{limited}=\operatorname{dissolve}(LIMITED).
}
```

`Omega_core` is the primary H3 service-analysis/clipping domain. `Omega_limited` remains a separate contextual/sensitivity domain. Exterior electrical/road nodes may be retained only when needed for network closure and are excluded from service denominators unless independently justified.

A deterministic acquisition/checksum utility is now committed:

```text
methods/h3/fetch_houston_boundary.py
```

It is designed to download the untouched ArcGIS JSON in native spatial reference, compute SHA-256, validate polygon/schema requirements, enumerate `SERVICE_TY` counts, and create a manifest. It intentionally does not reproject, dissolve, repair, or alter raw geometry.

Current boundary gate:

```math
\boxed{
G_{\Omega,source}=1,
\qquad
G_{\Omega,bytes}=0,
\qquad
G_{\Omega,QA}=0.
}
```

The present execution container cannot resolve the City of Houston host through direct external DNS. Browser research exposes authoritative metadata but not a local raw geometry payload. Therefore no byte size, SHA-256, raw feature count, FULL/LIMITED feature count, polygon area, multipart count, invalid-geometry rate, or final clipped geometry is claimed.

This is a data-access/materialization blocker, not H3 falsification.

## Gate state

```math
\boxed{
G_{case}=1,
\quad
G_{source}=1,
\quad
G_{\Omega,source}=1,
\quad
G_{bytes}=0,
\quad
G_{QA}=0,
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

## Immediate next task

```math
\boxed{
D_{\Omega}\text{ raw bytes}
\rightarrow
\text{SHA256 + native CRS + geometry QA}
\rightarrow
G_{\Omega,QA}=1.
}
```

Exact restart order:

```text
1. run methods/h3/fetch_houston_boundary.py in a network-enabled environment;
2. freeze raw byte size, SHA-256, access timestamp, source query and native CRS;
3. verify polygon geometry, SERVICE_TY classes and null/invalid geometry rate;
4. construct Omega_legal, Omega_core and Omega_limited only as processed derivatives;
5. cross-check geometry/attributes against the secondary City-hosted COH City Limits layer;
6. freeze boundary feature counts, areas and multipart-component counts;
7. only then enumerate SMART-DS geographic metadata and materialize D_P for Houston;
8. then materialize D_T, D_S and D_F;
9. run network/interface QA;
10. populate the case-specific numerical H3 registry and advance uncertainty qualification.
```

Do not fabricate geometry from published extents or renderer metadata. Do not replace the City source with an arbitrary third-party polygon merely because it is easier to download.

## Hard prohibition

Do not redesign the framework, browse without a declared thesis evidence need, collect papers without extraction purpose, replace the frozen Houston demonstrator casually, claim the synthetic power network is the actual Houston grid, treat the Harvey stress test as a historical reconstruction, merge FULL and LIMITED service regimes into one H3 service denominator without explicit change control, invent numerical thresholds/probabilities/horizons, infer P↔T causality from common flood exposure, choose a solver before dimensions/uncertainty close, or run confirmatory H3 until all required gates equal 1.
