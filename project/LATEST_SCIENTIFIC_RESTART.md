# Latest Scientific Restart Pointer

**Updated:** 2026-09-17  
**Purpose:** single live pointer to the latest immutable checkpoint, thesis-only operating protocol, H3 demonstrator, data-materialization state, boundary execution attempt, and immediate next admissible task.

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
15. `H3_HOUSTON_BOUNDARY_EXECUTION_ATTEMPT_2026-09-17_V1.md`
16. `H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md`
17. `H3_PREREGISTRATION_V1.md`
18. `H3_ALGORITHM_SELECTION_AND_VERIFICATION_V1.md`
19. `../methods/h3/fetch_houston_boundary.py`
20. `../methods/h3/materialize_houston_boundary.py`
21. `../.github/workflows/h3-houston-boundary-materialization.yml`

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
D_{\Omega}\text{ source + domain semantics frozen}
\rightarrow
\boxed{\text{boundary materialization execution attempted but externally blocked}}.
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

## Houston boundary semantics

Primary authoritative source:

```text
City of Houston / MyCity Houston
HoustonMap/Administrative_Boundary/MapServer/0
Layer: Houston City Limit
```

The H3 study support remains:

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

`Omega_core` is the primary H3 service-analysis/clipping domain. `Omega_limited` remains a separate contextual/sensitivity domain. Exterior electrical/road nodes may be retained only when required for network closure and are excluded from service denominators unless independently justified.

## Boundary execution attempt

Two executable routes are now committed:

```text
methods/h3/fetch_houston_boundary.py
methods/h3/materialize_houston_boundary.py
.github/workflows/h3-houston-boundary-materialization.yml
```

The materialization runner is designed to preserve the untouched City ArcGIS FeatureSet JSON, compute SHA-256/byte size, verify `SERVICE_TY`, reject null/empty/invalid geometries without silent repair, construct `Omega_core`, `Omega_limited`, and `Omega_legal` only as processed derivatives, calculate areas in EPSG:2278, and cross-check against the independent City-hosted `COH City Limits` layer.

GitHub Actions execution identity:

```text
workflow commit: c72354809e1132779fd7173fbe958dad7ba450e0
workflow run:    35150698128
workflow job:    104977978792
status:          completed
conclusion:      failure
runner_id:       0
steps:           []
```

The job terminated before any step was assigned/executed. The repository's existing `Python package` workflow on the same commit also failed in the same interval. Therefore this is treated as an external execution/runner blocker, not as a boundary-code failure or scientific failure.

No raw geometry artifact or scientific QA result was produced by that run.

## Current gate state

```math
\boxed{
G_{case}=1,
\quad
G_{source}=1,
\quad
G_{\Omega,source}=1,
\quad
G_{\Omega,bytes}=0,
\quad
G_{\Omega,QA}=0,
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

The correct execution status is:

```text
BOUNDARY MATERIALIZATION = NOT EXECUTED
H3 = NOT TESTED
```

H3 confirmatory execution remains **NOT AUTHORIZED**.

## Immediate next task

```math
\boxed{
\text{obtain one successful network-enabled execution of the frozen boundary runner}
\rightarrow
D_{\Omega}\text{ raw bytes}
\rightarrow
\text{SHA256 + CRS + geometry QA}
\rightarrow
G_{\Omega,QA}=1.
}
```

Accepted execution routes:

```text
A. GitHub Actions can assign a runner to the committed workflow; or
B. methods/h3/materialize_houston_boundary.py is executed in another network-enabled environment and its outputs are returned unchanged.
```

Required outputs before continuation:

```text
coh_city_limits_primary_raw.json
coh_city_limits_manifest.json
houston_boundary_qa.json
houston_boundary_summary.txt
houston_core_full_service.geojson
houston_legal_full_plus_limited.geojson
houston_limited_service.geojson (when LIMITED exists)
```

Only after `G_Omega_QA=1` continue in this order:

```text
1. enumerate SMART-DS/Texas geographic metadata;
2. identify Houston-intersecting substations/circuits plus minimum electrical boundary components;
3. materialize and hash the corresponding OpenDSS/time-series/geographic objects;
4. run baseline power-network/OpenDSS QA;
5. then materialize D_T, D_S and D_F;
6. run network/interface QA;
7. populate the case-specific numerical H3 registry;
8. advance uncertainty qualification.
```

Do not fabricate geometry from published extents or renderer metadata. Do not replace the City source with an arbitrary third-party polygon merely because it is easier to download.

## Hard prohibition

Do not redesign the framework, browse without a declared thesis evidence need, collect papers without extraction purpose, replace the frozen Houston demonstrator casually, claim the synthetic power network is the actual Houston grid, treat the Harvey stress test as a historical reconstruction, merge FULL and LIMITED service regimes into one H3 service denominator without explicit change control, invent numerical thresholds/probabilities/horizons, infer P↔T causality from common flood exposure, choose a solver before dimensions/uncertainty close, or run confirmatory H3 until all required gates equal 1.
