# H3 SMART-DS Year Qualification v1.0

**Status:** PRIMARY POWER-NETWORK VINTAGE QUALIFIED / HOUSTON GEOGRAPHIC INVENTORY STILL BLOCKED  
**Date:** 2026-09-17  
**Protocol:** EGMIV–TSP  
**Case:** `H3-HOU-FLOOD-V1`  
**Thesis destination:** Chapter 4 — H3 power-layer realization and provenance  
**Upstream authority:** `H3_DEMONSTRATOR_FREEZE_V1.md`, `H3_SMARTDS_HOUSTON_PREEXTRACTION_V1.md`

---

## 1. Scientific question

The immediate source-selection question is:

```math
\boxed{
\text{Which SMART-DS v0.9 network vintage can be frozen for the primary Houston H3 power layer without inventing a historical reconstruction claim?}
}
```

The H3 demonstrator is semisynthetic and mechanism-validation oriented. Therefore the selected SMART-DS year is a **synthetic network vintage**, not a claim that the distribution topology reproduces the actual Houston grid in the Hurricane Harvey year.

---

## 2. Evidence retrieved

### 2.1 SMART-DS v0.9 year roots

The official OEDI S3 viewer for `SMART-DS/v0.9/` exposes three top-level year roots:

```text
2016/
2017/
2018/
```

This establishes the existence of those year namespaces in v0.9. It does **not** by itself establish that every year contains a `Full_Texas` realization suitable for the thesis.

### 2.2 Directly documented `Full_Texas` path

The official Texas A&M **Texas Combined Transmission–Distribution Test Case** page explicitly provides the following example retrieval path:

```text
s3://oedi-data-lake/SMART-DS/v0.9/2016/Full_Texas/P1U/scenarios/base_timeseries/opendss/p1uhs0_1247/
```

The same official page states that the distribution data contain OpenDSS network data, time-series load profiles, and geographic coordinates, and describes the Texas case as a synthetic/fictitious network on the geographic footprint of Texas.

Therefore the existence of a `2016/Full_Texas` realization with the required data family is directly supported by an authoritative source.

### 2.3 Dataset validation literature

Mateo et al. (2024) describe the combined synthetic Texas T&D system as publicly available, geolocated in Texas, synthetic rather than utility-confidential, and validated to reproduce characteristics found in actual networks. The paper reports a system exceeding 15,000 feeders and 46 million electrical nodes, establishing that the source family is large enough to require geographically selective extraction rather than whole-state materialization.

Reference:

Mateo, C., Postigo, F., Elgindy, T., Birchfield, A. B., Dueñas, P., Palmintier, B., Panossian, N., Gómez, T., de Cuadra, F., Overbye, T. J., Safdarian, F., & Wallison, D. (2024). Building and validating a large-scale combined transmission & distribution synthetic electricity system of Texas. *International Journal of Electrical Power & Energy Systems, 159*, 110037. https://doi.org/10.1016/j.ijepes.2024.110037

---

## 3. Qualification decision

The primary H3 power-network vintage is frozen as:

```math
\boxed{
Y_P^{H3}=2016
}
```

with source path family:

```text
SMART-DS/v0.9/2016/Full_Texas/
```

and primary scenario family:

```text
base_timeseries
```

### Why 2016 is admissible

The choice is based on **direct authoritative source traceability**, not on a claim that 2016 is physically closer to Hurricane Harvey than 2017 or 2018.

The decision rule is:

```math
\boxed{
\text{directly documented Full_Texas realization}
+\text{OpenDSS}
+\text{time series}
+\text{geographic coordinates}
+\text{public reproducibility}
\Rightarrow
Y_P^{H3}=2016.
}
```

This is a reproducibility decision for a semisynthetic experiment.

---

## 4. Explicit non-claims

The following are **not** claimed:

```text
2016 SMART-DS is the real Houston 2016 grid;
2016 SMART-DS is the real Houston 2017 Harvey grid;
2016 topology reproduces CenterPoint Energy topology;
2016 is the only year containing Full_Texas;
2017 or 2018 are scientifically inferior;
network vintage and hazard year must match in this demonstrator.
```

The hazard remains the observed Harvey flood field used as a spatial stress field. The power network remains synthetic. Their combination is intentionally semisynthetic.

---

## 5. Why 2017/2018 are not frozen now

The official OEDI root verifies that 2017 and 2018 namespaces exist. However, the currently retrieved authoritative evidence does not directly verify a `2017/Full_Texas` or `2018/Full_Texas` path with the same clarity as the Texas A&M 2016 example.

Therefore:

```math
\boxed{
2017,2018:\ \text{AVAILABLE YEAR ROOTS, Full_Texas QUALIFICATION OPEN}
}
```

They are not rejected. They simply do not supersede the directly supported 2016 realization under the current evidence gate.

Any later switch requires explicit change control and must show a material scientific advantage for H3 rather than calendar matching alone.

---

## 6. Interaction with the Houston boundary gate

Year qualification does **not** close geographic selection.

```math
\boxed{
G_{P,year}=1
}
```

but

```math
\boxed{
G_{\Omega,QA}=0
\Rightarrow
G_{P,inventory}=0.
}
```

The final Houston candidate inventory remains prohibited until the authoritative `Omega_core` geometry has passed byte-level and geometry QA.

After `G_{\Omega,QA}=1`, execute:

```bash
python methods/h3/inventory_smartds_houston.py \
  --root data/H3-HOU-FLOOD-V1 \
  --year 2016 \
  --scenario base_timeseries
```

---

## 7. Gate state after this qualification

```math
\boxed{
G_{P,source}=1,
\qquad
G_{P,year}=1,
\qquad
G_{P,prep}=1,
\qquad
G_{P,inventory}=0,
\qquad
G_{P,QA}=0.
}
```

No Houston substation IDs, feeder IDs, node/edge counts, load denominator, OpenDSS convergence result, or electrical closure set are claimed yet.

---

## 8. Immediate next admissible task

Because the primary year is now qualified, the remaining prerequisite is entirely spatial/execution based:

```math
\boxed{
G_{\Omega,QA}=1
\rightarrow
\text{2016 Full_Texas Houston candidate inventory}
\rightarrow
\text{minimum electrical closure}
\rightarrow
\text{OpenDSS compile/power-flow QA}.
}
```

If boundary execution remains blocked, the only admissible parallel work is preparation/verification that does not label any SMART-DS asset as a Houston asset.

---

## Authoritative sources

Open Energy Data Initiative. (n.d.). *AWS S3 Explorer — SMART-DS v0.9*. https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=SMART-DS/v0.9/

Texas A&M University. (n.d.). *Texas Combined Transmission–Distribution Test Case*. https://electricgrids.engr.tamu.edu/texas7k-td/

Mateo, C., Postigo, F., Elgindy, T., Birchfield, A. B., Dueñas, P., Palmintier, B., Panossian, N., Gómez, T., de Cuadra, F., Overbye, T. J., Safdarian, F., & Wallison, D. (2024). Building and validating a large-scale combined transmission & distribution synthetic electricity system of Texas. *International Journal of Electrical Power & Energy Systems, 159*, 110037. https://doi.org/10.1016/j.ijepes.2024.110037
