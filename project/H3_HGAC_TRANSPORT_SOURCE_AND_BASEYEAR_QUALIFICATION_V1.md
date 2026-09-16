# H3 H-GAC Transportation Source and Base-Year Qualification v1.0

**Status:** SOURCE + BASE YEAR QUALIFIED / RAW BYTES + HOUSTON CLIP OPEN  
**Date:** 2026-09-17  
**Protocol:** EGMIV–TSP  
**Case:** `H3-HOU-FLOOD-V1`  
**Thesis destination:** Chapter 4 — H3 transportation-layer realization and provenance

> This file advances the transportation branch independently while the Houston boundary and SMART-DS execution gates remain blocked. It freezes the H-GAC source family and transport-model base year but does not claim that roadway files have been downloaded, parsed, clipped, or transformed into the final H3 graph.

---

## 1. Scientific destination

The transportation layer must eventually produce

```math
\boxed{
\mathcal G_{T,sim}^{HOU}
=(\mathcal V_T^{HOU},\mathcal E_T^{HOU})
}
```

and a separately audited service-demand/accounting domain compatible with the frozen transportation service definition `S_T`.

The transport graph is required for:

```text
transport service degradation;
flood-driven road impairment;
P→T signal-operation effects;
T→P repair-crew travel/accessibility;
reachability and recovery calculations.
```

---

## 2. Qualified H-GAC source family

Primary authoritative source:

```text
Houston-Galveston Area Council (H-GAC)
2025 Transportation Conformity
https://www.h-gac.com/transportation-conformity/2025
```

The current H-GAC conformity package explicitly publishes:

```text
Appendix C.1 — Travel Model Validation;
Appendix C.2 — Links, Miles, Centerline, and Lane Miles Summaries;
Appendix C.3 — Link Listing and Capacity Staging;
Appendix C.4 — Roadway Network Files.
```

The primary raw objects required for H3 transport realization are:

```text
C.4 Roadway Network Files                      -> primary network source;
C.3 Link Listing and Capacity Staging          -> link/capacity semantics and cross-check;
C.1 Travel Model Validation                    -> model-validation provenance/support.
```

The H-GAC traffic-data program separately documents regional traffic-volume counts, vehicle-speed data, and vehicle-classification data used to improve demand estimates and support travel-demand modeling. These data remain calibration/validation support, not an automatic substitute for the modeled OD/service requirement.

```math
\boxed{G_{T,source}=1.}
```

---

## 3. Transport model semantics

The 2025 conformity report states that the H-GAC Travel Demand Model:

```text
covers Brazoria, Chambers, Fort Bend, Galveston, Harris, Liberty, Montgomery, and Waller counties;
is executed in the Cube Voyager environment;
uses a four-step process: trip generation, trip distribution, mode choice, roadway assignment;
assigns vehicle trips to the roadway network and produces link-level vehicle-miles traveled;
uses traffic analysis zones as the basic geographic unit.
```

The report identifies:

```text
model base year: 2023;
forecast years: 2026, 2030, 2040, 2045;
TAZs: 5,263 total;
internal TAZs: 5,217;
external zones/stations: 46.
```

These are regional model facts and are not yet Houston H3 graph counts.

---

## 4. Base-year qualification

The primary H3 roadway-network vintage is frozen as

```math
\boxed{Y_T^{H3}=2023.}
```

Rationale:

```text
1. H-GAC explicitly identifies 2023 as the calibrated/current model base year in the 2025 conformity modeling system;
2. H3 requires a reproducible roadway state rather than a forecast scenario chosen for convenience;
3. the thesis demonstrator is semisynthetic and does not claim historical reconstruction of Hurricane Harvey in 2017;
4. selecting 2023 avoids silently using a future 2026/2030/2040/2045 planning network as the baseline physical transport state.
```

Therefore:

```math
\boxed{G_{T,year}=1.}
```

This does **not** assert that the 2023 H-GAC network reproduces Houston's road network during Harvey.

---

## 5. Raw acquisition contract

Executable utility:

```text
methods/h3/materialize_hgac_transport.py
```

Frozen H-GAC download endpoints:

```text
C.1:
https://www.h-gac.com/getmedia/26d3529a-3e1b-4211-83b5-a55515a06589/C1_Travel_Model_Variation

C.3:
https://www.h-gac.com/getmedia/6faf4b9d-d6e7-4c7c-830b-7110663b0e52/C3_Link_Listing_and_Capacity_Staging

C.4:
https://www.h-gac.com/getmedia/e1498b1d-470d-4df9-92bb-2d55b749f524/C4_Roadway-Network-Files
```

The utility must:

```text
preserve returned bytes unchanged;
record final/resolved URL, HTTP metadata, byte count and SHA-256;
reject HTML/error pages as data;
detect ZIP payloads from bytes rather than filename assumptions;
extract ZIPs only into interim/, never over raw/;
prevent path traversal;
record every extracted member's path, byte count, CRC and SHA-256.
```

No source archive member format is frozen until the actual bytes are inspected.

---

## 6. Boundary and clipping rule

Regional source materialization is scientifically independent of the unresolved Houston municipal geometry, so raw H-GAC files may be frozen before `G_Omega_QA=1`.

However, final Houston selection remains gated:

```math
\boxed{
G_{\Omega,QA}=1
\Rightarrow
\text{Houston roadway clipping/selection may execute}.
}
```

No link may be classified as an H3 Houston service/network link from an approximate bounding box, published map extent, or city-name attribute alone.

Exterior links/nodes needed for route/network closure must later be tagged separately from the Houston service-accounting domain.

---

## 7. Simulation graph versus service graph

The transport realization must preserve the same accounting distinction already frozen for power:

```math
\boxed{
\mathcal G_{T,sim}^{HOU}
\supseteq
\mathcal G_{T,svc}^{HOU}.
}
```

`G_T,sim` may contain external connectors, centroid connectors, or boundary links required for route continuity or assignment. These must not automatically enter the Houston `S_T` denominator.

The future QA must distinguish at minimum:

```text
physical roadway links;
centroid/connectors;
external stations/connectors;
directionality;
link length;
capacity;
lanes;
free-flow/travel-time fields when supplied;
functional class when supplied;
OD/TAZ support;
inside-core versus boundary-support role.
```

No field semantics are assumed until the downloaded C.3/C.4 files are inspected.

---

## 8. Current gate state

```math
\boxed{
G_{T,source}=1,
\qquad
G_{T,year}=1,
\qquad
G_{T,prep}=1,
\qquad
G_{T,raw}=0,
\qquad
G_{T,inventory}=0,
\qquad
G_{T,QA}=0.
}
```

The source and year qualification do not close the data/model gate.

---

## 9. Exact next transport sequence

```math
\boxed{
\text{H-GAC C.1/C.3/C.4 raw bytes}
\rightarrow
\text{SHA256 + archive inventory}
\rightarrow
\text{field/file semantics}
\rightarrow
G_{\Omega,QA}=1
\rightarrow
\text{Houston extraction}
\rightarrow
\text{transport topology/service QA}
\rightarrow
N_T,M_T.
}
```

Execution command:

```bash
python methods/h3/materialize_hgac_transport.py \
  --root data/H3-HOU-FLOOD-V1 \
  --source all
```

If external retrieval remains blocked, retain `G_T_raw=0`; do not invent archive contents, network counts, CRS, link attributes or OD matrices.

---

## 10. Hard prohibitions

Do not:

```text
treat regional TAZ counts as Houston network dimensions;
treat traffic counts as the S_T denominator without an evidence-matched mapping;
use a future forecast network as baseline without change control;
claim the 2023 H-GAC model is the historical 2017 Harvey transport network;
clip from a hand-drawn Houston bounding box;
assume Cube/network archive field meanings before byte-level inspection;
replace H-GAC with OSM solely because it is easier to download;
run H3 transportation dynamics before topology and service QA pass.
```

---

## References

Houston-Galveston Area Council. (2026). *2025 transportation conformity documents and files*. https://www.h-gac.com/transportation-conformity/2025

Houston-Galveston Area Council. (2026). *2025 transportation conformity report*. https://www.h-gac.com/getmedia/a6adb026-1fec-49bd-b297-52f899ccd2cd/2025_Transportation_Conformity_Report_final-rev2

Houston-Galveston Area Council. (n.d.). *Traffic data*. https://www.h-gac.com/traffic-data
