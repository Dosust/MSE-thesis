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
14. `H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md`
15. `H3_PREREGISTRATION_V1.md`
16. `H3_ALGORITHM_SELECTION_AND_VERIFICATION_V1.md`
17. `../methods/h3/materialize_houston_boundary.py`
18. `../methods/h3/inventory_smartds_houston.py`
19. `../methods/h3/materialize_smartds_houston_power.py`
20. `../methods/h3/qa_smartds_power_layer.py`
21. `../config/h3_houston_power_source_v1.json`

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
\boxed{\text{SMART-DS materialization + electrical/OpenDSS QA machinery prepared}}.
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

Primary claim type: geographically grounded semisynthetic mechanism/decision-value experiment, **not** historical reconstruction of Houston's actual 2017 grid, outage chronology or restoration chronology.

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

## SMART-DS power source

Frozen primary power source:

```text
SMART-DS version: v0.9
Year:             2016
Dataset:          Full_Texas
Scenario:         base_timeseries
Prefix family:    SMART-DS/v0.9/2016/Full_Texas/
```

```math
\boxed{Y_P^{H3}=2016.}
```

This is a reproducibility/source-traceability choice for the semisynthetic demonstrator, not a claim that the synthetic 2016 network is historical Houston.

Candidate selection remains:

```math
\boxed{
I_s
=
\mathbf 1\{\exists v\in\mathcal V_s:\operatorname{coord}(v)\in\Omega_{core}\}.
}
```

A candidate substation is not yet a final H3 power subsystem.

## Prepared power realization pipeline

### 1. Houston geographic candidate inventory

```text
methods/h3/inventory_smartds_houston.py
```

Hard-requires `G_Omega_QA=1` for final Houston selection.

### 2. Candidate raw materialization

```text
methods/h3/materialize_smartds_houston_power.py
```

It freezes source object keys, byte sizes, ETags/last-modified metadata, preserved relative paths and SHA-256 identities for the complete source-provided candidate-substation OpenDSS packages.

### 3. Electrical closure and OpenDSS QA

Scientific protocol:

```text
project/H3_SMARTDS_ELECTRICAL_CLOSURE_AND_OPENDSS_QA_V1.md
```

Executable QA:

```text
methods/h3/qa_smartds_power_layer.py
```

The simulation graph and service domain are explicitly separated:

```math
\boxed{
\mathcal G_{P,sim}^{HOU}
\supseteq
\mathcal G_{P,svc}^{HOU}.
}
```

The station-level closure rule preserves complete source-provided OpenDSS packages and adds only documented external dependencies needed for `Master.dss` resolution. Exterior support elements are not automatically included in Houston service accounting.

Baseline QA reports/validates:

```text
Master.dss resolution;
OpenDSS compile;
baseline solve convergence;
nonempty buses and PD elements;
finite voltage outputs where available;
bus/node/circuit-element/PD-element counts;
line/transformer/load counts;
isolated branches/loads and loop counts where supported;
OpenDSSDirect and engine versions.
```

Voltage extrema are diagnostic only; no arbitrary voltage threshold is introduced by this QA step.

Simulation-layer dimensions are frozen only after successful execution:

```math
\boxed{
N_P^{sim}=\sum_s N_{bus,s},
\qquad
M_P^{sim}=\sum_s N_{PD,s}.
}
```

They do **not** yet define the `S_P` service denominator.

## Current power gate

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

Overall:

```math
\boxed{
G_{case}=1,
\quad
G_{source}=1,
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

H3 confirmatory execution remains **NOT AUTHORIZED**.

## Immediate next executable transition

```math
\boxed{
\text{successful Houston-boundary materialization}
\rightarrow
G_{\Omega,QA}=1
\rightarrow
\text{2016 Houston candidate inventory}
\rightarrow
\text{candidate raw materialization}
\rightarrow
\text{electrical closure + OpenDSS QA}.
}
```

Exact commands after the boundary gate closes:

```bash
python methods/h3/inventory_smartds_houston.py \
  --root data/H3-HOU-FLOOD-V1 \
  --year 2016 \
  --scenario base_timeseries

python methods/h3/materialize_smartds_houston_power.py \
  --root data/H3-HOU-FLOOD-V1 \
  --year 2016 \
  --scenario base_timeseries

python methods/h3/qa_smartds_power_layer.py \
  --root data/H3-HOU-FLOOD-V1 \
  --year 2016 \
  --scenario base_timeseries
```

If the boundary runner remains externally blocked, only scientifically independent preparation may continue. Do not label any SMART-DS substation as Houston until `G_Omega_QA=1`.

After `G_P_QA=1`, proceed to H-GAC transportation materialization, City traffic-signal materialization, Harvey flood materialization, P↔T interface QA, case-specific H3 registry closure, uncertainty qualification, then H3 solver verification.

## Hard prohibition

Do not construct Houston geometry from published extents; do not substitute a third-party boundary for convenience; do not infer actual CenterPoint topology from SMART-DS; do not silently repair OpenDSS source models; do not introduce arbitrary voltage/service thresholds; do not invent network dimensions; and do not execute confirmatory H3 until every required gate closes.
