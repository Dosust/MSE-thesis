# Austin Data QC and Gate Protocol v1.0

**Case:** `AUS-P5U-2018-V1`  
**Date:** 2026-09-18  
**Protocol:** EGMIV  
**Status:** QA LOGIC FROZEN / RAW EXECUTION BLOCKED BY CURRENT NETWORK ENVIRONMENT

## 1. Purpose

This protocol determines whether the Austin candidate may advance from source qualification to a frozen case. It deliberately separates four claims:

```math
\boxed{
\text{source exists}
\neq
\text{bytes acquired}
\neq
\text{data pass QC}
\neq
\text{case is scientifically admissible}.
}
```

No H1--H5 result may be inspected while choosing the Austin subregion or repairing data-quality defects.

## 2. Raw-data integrity gate

Every acquired object must record:

```text
source URL / dataset identifier;
acquisition UTC;
immutable local path;
byte count;
SHA-256;
feature/row count where applicable;
query/filter parameters;
page-level hashes for paginated services.
```

For ArcGIS layers, acquisition is ID-first and paginated. The merged feature count must equal the unique object-ID count. A server transfer limit or missing page is a hard failure.

## 3. Power gate G1

`G1_power_materialization = PASS` only if:

1. the frozen SMART-DS path is `v1.0/2018/AUS/P5U/base_timeseries`;
2. `Buscoords.dss` is materialized and hashed;
3. coordinates are finite, unique by bus identifier where required by the model, geographically plausible, and non-degenerate;
4. the OpenDSS objects required by the chosen feeder realization are completely inventoried/materialized;
5. model parse/load-flow checks pass before any coupled experiment;
6. no SMART-DS component is described as actual Austin Energy topology.

## 4. Common spatial-support gate G2

Let `Omega_P5U` denote the empirical spatial support of the retained SMART-DS assets, **not** an inferred utility service territory.

`G2_common_spatial_support = PASS` only if the retained power assets have documented overlap with:

- the declared Austin analysis boundary;
- the Austin Energy service-area polygon used as an independent cross-check;
- a routable City road subnetwork;
- at least one retained traffic-signal location.

A bounding-box intersection alone is insufficient for final PASS; feature-level geometry is required.

## 5. Transport topology gate G3

The retained road graph must be nonempty and routable for every OD pair and repair-access path used in the experiment. PASS requires:

```text
all retained road bytes/pages accounted for;
valid geometries or explicitly logged repairs;
node/link construction reproducible;
no missing endpoint coordinates;
all experiment OD endpoints attached to a routable component;
all declared repair origins and repair targets attached to a routable component.
```

No arbitrary global connectivity percentage is imposed; the engineering requirement is path feasibility for every route the experiment actually uses.

## 6. Traffic-observation gate G4

At least one qualified 2018 observation family must spatially overlap the retained road graph. Counts without detector/sensor coordinates do not satisfy this gate.

The primary candidate is the Austin radar series because its documented coverage includes 2018. Camera counts may be secondary evidence subject to their documented limitations.

Calibration/development and held-out roles must be frozen before hypothesis testing.

## 7. P->T mapping gate G5

Each signal used as a P->T interface must have one reproducible synthetic power mapping. Mapping is a demonstrator construct, not an observed utility feeder assignment.

Before confirmatory execution, freeze:

```text
eligible power-asset class;
spatial/service-area mapping operator;
maximum admissible mapping discrepancy or rejection rule;
percentage and identities of retained/rejected signals;
sensitivity to reasonable alternative mapping rules.
```

The rejection criterion must be derived from development spatial geometry / engineering interpretation before H1--H5 outcomes are inspected; it may not be chosen to maximize a hypothesis effect.

## 8. T->P repair-access gate G6

For every damaged power component used in restoration experiments:

```math
\boxed{
T_i^{restore}
=
T_i^{dispatch}
+T_i^{travel}(\mathcal G_T,t)
+T_i^{onsite}.
}
```

PASS requires a declared crew origin, a feasible route to each repair target in the undisturbed reference state, and explicit treatment of road closures/congestion in disturbed states. `T_travel` and `T_onsite` must remain distinct.

## 9. Flood gate G7

The FEMA/City floodplain layer is initially a **spatial exposure classifier**, not an event-time depth field and not a failure probability.

For a primary coupled-flood experiment, PASS requires feature-level intersection with at least one retained power component and at least one retained road component. If this criterion fails, P5U is rejected for the primary coupled-flood case before hypothesis results are inspected.

Fragility/failure probabilities remain separate later gates.

## 10. Provenance/QC gate G8

`G8_qc_provenance = PASS` only if all mandatory files have immutable hashes, all transformations are code-versioned, CRS transformations are declared, missingness is reported, geometry repairs are logged, and every derived crosswalk can be regenerated from frozen source objects.

## 11. Case decision

```math
\boxed{
G_{AUS}
=
\bigwedge_{k=0}^{8}G_k.
}
```

Only if `G_AUS=1` may `final_case_admissibility` become `true`.

If P5U fails a scientific gate, evaluate the remaining Austin SMART-DS urban subregions using the same pre-result gates. A data/software access failure is `BLOCKED/NOT TESTED`, not evidence against H1--H5.

## 12. Evidence basis

Coupled power--transportation studies explicitly model traffic-signal dependence on electric power and repair-crew dependence on road accessibility, supporting the two directional mechanisms retained here (Ge, Du, & Ye, 2019, https://doi.org/10.1007/s40565-019-0524-7; Wei et al., 2019, https://doi.org/10.1007/s40565-019-0516-7). More recent repair-sequencing work retains the same two-way mechanism: power failures delay traffic through signal outages, while transportation delays affect crew arrival (https://doi.org/10.1080/10286608.2025.2602872).

The Austin Energy service-area source is used only as an independent geographic cross-check; it does not disclose actual feeder topology.
