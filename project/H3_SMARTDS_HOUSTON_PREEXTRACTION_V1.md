# H3 SMART-DS Houston Pre-Extraction Protocol v1.0

**Status:** PREPARED / NOT YET EXECUTED  
**Date:** 2026-09-17  
**Protocol:** EGMIV–TSP  
**Case:** `H3-HOU-FLOOD-V1`  
**Thesis destination:** Chapter 4 — H3 power-layer realization and provenance

> This file prepares the next power-data step without violating the unresolved Houston-boundary materialization gate. It authorizes source-structure discovery and code preparation, but prohibits final Houston substation/circuit selection until `G_{\Omega,QA}=1`.

---

## 1. Scientific destination

The power-layer target is

```math
\boxed{
\mathcal G_P^{HOU}
=(\mathcal V_P^{HOU},\mathcal E_P^{HOU})
}
```

with only SMART-DS/Texas components whose documented geographic support intersects the frozen Houston full-service domain, plus the minimum electrical boundary components required for network closure.

This step supplies the physical power state space required later by H3; it does not define H3 thresholds, viability, or recovery by itself.

---

## 2. Qualified source facts

Texas A&M's combined T&D repository describes the case as a **synthetic/fictitious transmission–distribution network on the geographic footprint of Texas**. The official distribution source is OEDI SMART-DS v0.9, containing OpenDSS network data, time-series load profiles, and geographic coordinates. The repository gives the public S3 root

```text
s3://oedi-data-lake/SMART-DS/v0.9/
```

and provides an example Full_Texas path of the form

```text
SMART-DS/v0.9/2016/Full_Texas/P1U/scenarios/base_timeseries/opendss/p1uhs0_1247/
```

as an **example access path**, not as a frozen Houston substation or thesis year.

The SMART-DS user guide states that OpenDSS datasets are hierarchically organized by sub-region, substation and feeder and that `Buscoords.dss` stores the longitude and latitude of network nodes. `Master.dss` is the network entry point and component-specific files describe lines, transformers, loads, controls, PV/storage and other equipment.

### Evidence boundary

The following are therefore supported:

```math
\boxed{G_{P,source}=1}
```

for the dataset family and geographic-coordinate mechanism.

The following are **not yet supported**:

```text
exact SMART-DS year used by H3;
exact Full_Texas subregions intersecting Houston;
exact Houston substation IDs;
exact Houston feeder/circuit IDs;
N_P, M_P;
Houston load denominator;
OpenDSS convergence status;
minimum external electrical boundary set.
```

---

## 3. Gating rule

The final geographic inventory is conditional on the boundary gate:

```math
\boxed{
G_{\Omega,QA}=1
\Rightarrow
\text{Houston SMART-DS geographic selection may execute}.
}
```

If

```math
G_{\Omega,QA}=0,
```

then source-structure discovery may proceed, but no substation may be labelled a final Houston H3 asset.

This prevents use of published map extents, hand-drawn boxes, or approximate city coordinates as a substitute for the frozen `Omega_core` geometry.

---

## 4. Deterministic inventory implementation

Executable utility:

```text
methods/h3/inventory_smartds_houston.py
```

Two modes are frozen.

### Mode A — source-structure discovery

```bash
python methods/h3/inventory_smartds_houston.py \
  --root data/H3-HOU-FLOOD-V1 \
  --discover
```

This lists the public SMART-DS v0.9 year/dataset hierarchy and records which years expose `Full_Texas`. It does **not** perform Houston selection and is admissible while the boundary is blocked.

### Mode B — Houston geographic candidate inventory

```bash
python methods/h3/inventory_smartds_houston.py \
  --root data/H3-HOU-FLOOD-V1 \
  --year <qualified_year> \
  --scenario base_timeseries
```

Mode B hard-requires:

```text
qa/boundary/houston_boundary_qa.json with status=PASS;
processed/boundary/houston_core_full_service.geojson;
valid/nonempty Omega_core geometry.
```

The inventory recursively locates `Buscoords.dss` under each Full_Texas substation, freezes those coordinate files and SHA-256 values, parses documented longitude/latitude rows, and marks a substation as a **candidate** only if at least one documented bus coordinate lies in `Omega_core`.

```math
\boxed{
I_s
=
\mathbf 1\left\{
\exists v\in\mathcal V_s:
\operatorname{coord}(v)\in\Omega_{core}
\right\}.
}
```

`I_s=1` means **candidate Houston substation**, not final retained power subsystem.

---

## 5. Final-selection rule after candidate inventory

Candidate substations must then undergo electrical-closure QA.

Let

```math
\mathcal S_{core}=\{s:I_s=1\}.
```

The final retained power graph is

```math
\boxed{
\mathcal G_P^{HOU}
=
\operatorname{closure}_{elec}(\mathcal S_{core})
}
```

where `closure_elec` adds only the minimum documented upstream/downstream elements needed for valid OpenDSS/network boundary conditions.

Every retained exterior element must be tagged:

```text
is_boundary_connector = 1
in_service_denominator = 0
boundary_reason = documented
```

unless a later service requirement explicitly changes that rule.

No exterior component may be retained merely to improve graph connectivity, viability, or H3 performance.

---

## 6. Mandatory outputs

After Mode B and electrical closure, freeze:

```text
SMART-DS version/year/scenario;
all selected S3 object keys;
raw byte sizes and SHA-256;
subregion/substation/feeder IDs;
Buscoords coordinate counts and invalid-coordinate counts;
inside-core bus counts;
candidate and rejected substation IDs;
boundary connector IDs and reasons;
OpenDSS compile/convergence result;
N_P and M_P;
served-load denominator provenance;
all exclusions and failures.
```

The first inventory output is candidate-only and cannot be used as the confirmatory H3 graph until OpenDSS and network QA pass.

---

## 7. Current gate state

```math
\boxed{
G_{P,source}=1,
\qquad
G_{P,prep}=1,
\qquad
G_{P,inventory}=0,
\qquad
G_{P,QA}=0.
}
```

The second Houston-boundary execution retry also failed before any usable workflow steps ran. Therefore `G_{\Omega,bytes}=G_{\Omega,QA}=0` remains unchanged.

The correct next executable transition remains:

```math
\boxed{
G_{\Omega,QA}=1
\rightarrow
\text{SMART-DS structure/year qualification}
\rightarrow
\text{Houston candidate inventory}
\rightarrow
\text{electrical closure + OpenDSS QA}.
}
```

---

## References

Mateo, C., Postigo, F., Elgindy, T., Birchfield, A., Duenas, P., Palmintier, B., Panossian, N., Gomez, T., de Cuadra, F., Overbye, T., Safdarian, F., & Wallison, D. (2024). Building and validating a large-scale combined transmission & distribution synthetic electricity system of Texas. *International Journal of Electrical Power & Energy Systems, 159*.

Texas A&M University Electric Grid Test Case Repository. (n.d.). *Texas Combined Transmission-Distribution Test Case*. https://electricgrids.engr.tamu.edu/texas7k-td/

Open Energy Data Initiative / NREL. (2021). *SMART-DS User Guide*. https://oedi-data-lake.s3.amazonaws.com/SMART-DS/v1.0/User_Guide/Readme.pdf
