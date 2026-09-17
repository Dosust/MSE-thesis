# H3 Demonstrator Freeze v1.0

**Status:** DEMONSTRATOR ARCHITECTURE FROZEN / NUMERICAL REGISTRY OPEN  
**Date:** 2026-09-17  
**Protocol:** EGMIV–TSP  
**Thesis destination:** Chapter 3 → Stage 5 → RQ5/H3 → Chapter 4 H3 experiment  
**Scientific authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`, `CANONICAL_RQ_SO_HYPOTHESES_V3.md`, `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`, `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V7.md`  
**Execution state:** H3 confirmatory execution remains BLOCKED.

> This file freezes one concrete, reproducible H3 demonstrator so that the remaining thresholds, uncertainty models, admissible controls, algorithms, metrics, and data roles can be qualified against one declared system instead of an abstract Power–Transportation problem.

---

## 1. Frozen case identity

```math
\boxed{
\mathcal C_{H3}^{\rm HOU}
=
(\mathcal G_P,\mathcal G_T,\eta_{flood},\mathbb I_{PT},\mathcal O,\mathcal U,\mathcal D)
}
```

**Case ID:** `H3-HOU-FLOOD-V1`  
**Name:** **Houston Flood-Stress Coupled Power–Transportation Demonstrator**  
**Geographic domain:** City of Houston, Texas, with only the boundary connectors needed to preserve electrical and transportation network closure.  
**Case type:** geographically grounded **semisynthetic mechanism-validation demonstrator**.  
**Primary disturbance:** Hurricane Harvey observed flood-inundation / flood-depth field used as a spatial stress field.  
**Primary scientific purpose:** test whether uncertainty-aware viability + reach–avoid information adds decision-relevant information beyond conventional resilience/performance curves for a physically coupled power–road system.

The case is **not** a reconstruction of the real 2017 CenterPoint distribution grid, traffic state, outage chronology, or restoration chronology. The infrastructure layers use reproducible synthetic/current public models, while the Harvey flood field supplies a real observed hazard footprint. All thesis conclusions must therefore be stated as mechanism- and demonstrator-specific unless separately externally validated.

---

## 2. Why this case is admissible

The demonstrator was selected only after checking the evidence needs created by H3.

| Gate | Requirement | Evidence state | Decision |
|---|---|---|---|
| `G_geo` | P and T systems can be represented in one real geographic domain | SMART-DS/Texas7k provides geographically embedded synthetic T&D data; H-GAC provides regional roadway data | PASS |
| `G_Pdata` | open/reproducible power model with network + load/time-series support | Texas combined transmission–distribution / SMART-DS data are public synthetic datasets with geographic coordinates and OpenDSS distribution models | PASS |
| `G_Tdata` | authoritative roadway/traffic data | H-GAC publishes traffic counts, travel-model validation, link listings, and roadway network files | PASS |
| `G_haz` | observed hazard field can affect both networks spatially | USGS/FEMA Harvey release contains flood inundation polygons, depth rasters, boundaries, and high-water marks | PASS |
| `G_PT` | at least one evidence-supported P→T mechanism | power loss can disable traffic signals; FHWA explicitly addresses signal backup power during utility outages | PASS |
| `G_TP` | at least one evidence-supported T→P mechanism | road accessibility affects repair-crew travel and power restoration sequencing in established P–T resilience models | PASS |
| `G_rep` | reproducibility possible without confidential utility topology | synthetic power model + public transport/hazard data | PASS |
| `G_hist` | exact historical-event reconstruction required | NO — deliberately outside the H3 primary claim | NOT REQUIRED |

Therefore

```math
\boxed{G_{case}=1}
```

for a semisynthetic mechanism-validation experiment. This does **not** imply `G_K=1`, `G_U=1`, or authorization of H3 execution.

---

## 3. Power-system realization

### 3.1 Data family

Use the **Texas Combined Transmission–Distribution Test Case / SMART-DS Texas data family** as the power-system source.

The Texas combined case is a synthetic transmission–distribution network on the geographic footprint of Texas. Its distribution component includes OpenDSS network data, load time series, and geographic coordinates, and the transmission–distribution mapping links transmission loads to associated distribution circuits. SMART-DS is intentionally “realistic but not real” and its synthetic distribution networks are generated using geographic constraints and validated statistical/operational characteristics rather than confidential utility topology (NREL/SMART-DS; Texas A&M synthetic-grid project).

### 3.2 Houston extraction rule

The primary electrical domain is defined by the **City of Houston municipal polygon**:

```math
\mathcal V_P^{HOU}
=
\{i\in\mathcal V_P:\operatorname{coord}(i)\in\Omega_{HOU}\}
\cup
\mathcal V_P^{boundary}.
```

`V_P^boundary` contains only adjacent electrical nodes/substations required to preserve network boundary conditions for the retained Houston circuits. Boundary nodes are not treated as Houston service demand unless their loads lie inside the geographic service domain.

No bus or feeder may be manually added because it gives a preferred H3 result.

### 3.3 Power model level

The preferred physical realization is **distribution-level OpenDSS / validated reduced distribution dynamics**, not a transmission-bus proxy for traffic-signal loads.

A reduced model may be used for Stage-5 computation only after verifying that the reduction preserves the quantities entering

```math
S_P,\quad K_{phys},\quad F,\quad G_{rec},\quad \mathbb I_{PT}.
```

### 3.4 Power service observable

Retain the frozen form

```math
S_{P,m}
=
\frac{\sum_i\omega_i E_{i,m}^{srv}}
{\sum_i\omega_i\widehat E_{i,m}^{d}}.
```

For the primary demonstrator, **no unsupported criticality weighting is allowed**. The default is

```math
\omega_i=1
```

unless an authority-backed critical-service classification is mapped to a load/entity. Hospitals, emergency facilities, and traffic-signal loads may additionally enter as native non-substitutable constraints rather than being hidden inside an arbitrary scalar weight.

---

## 4. Transportation realization

### 4.1 Network and traffic source

Use Houston–Galveston Area Council (H-GAC) roadway-network and traffic-model products. H-GAC publishes traffic counts and uses them to support regional travel-demand modeling; its 2025 conformity archive includes travel-model validation, link/capacity files, and roadway network files. H-GAC also completed a 2024 household travel survey and provides linked OD transit survey information that can support demand/OD construction.

### 4.2 Houston extraction rule

```math
\mathcal G_T^{HOU}
=
\operatorname{clip}_{\Omega_{HOU}}(\mathcal G_T^{HGAC})
+\mathcal E_T^{boundary},
```

where `E_T^boundary` contains only external connectors required to represent OD flows entering or leaving the Houston analysis domain.

### 4.3 Traffic-signal layer

Use the City of Houston traffic-signal GIS feature layer for the P→T interface. Signal locations are spatial objects; the actual utility feeder supplying each signal is not public and must **not** be claimed as observed.

Each signal `j` will therefore be associated with the synthetic power network through a reproducible mapping rule

```math
\mu_{P\to T}(j)
=
\operatorname{argmin}_{i\in\mathcal V_P^{eligible}}
d(j,i)
```

or a superior topology/service-area mapping if the SMART-DS feeder geometry permits it. The final mapping rule and maximum admissible mapping distance must be frozen before H3 labels are inspected.

### 4.4 Transportation service observable

Retain the frozen form

```math
S_{T,m}
=
\min\left[
1,
\frac{\sum_w\omega_w N_{w,m}^{comp}}
{\sum_w\omega_w\widehat N_{w,m}^{req}}
\right].
```

Primary OD weights are equal unless a documented emergency/critical-service priority supports different weights. Critical hospital/emergency-access OD classes may be enforced as native constraints.

---

## 5. Hazard realization

### 5.1 Hazard dataset

Use the USGS/FEMA Hurricane Harvey flood-inundation data release for southeastern Texas. The release contains flood-inundation polygons, flood-depth rasters, mapped boundaries, and high-water-mark locations for the August–September 2017 event.

Define the observed spatial hazard field

```math
\eta_F(x)=d_{Harvey}(x),
```

where `d_Harvey(x)` is the qualified flood-depth value or documented inundation state at location `x`.

### 5.2 Primary H3 hazard semantics

The H3 primary demonstrator is **not a full hydrodynamic replay**. The observed Harvey field is used to create the post-impact state / damage exposure at the recovery origin.

```math
\boxed{
t_R^0=\text{declared post-impact damage-assessment epoch}.}
```

Component damage/passability is generated from qualified fragility/passability relationships in a later data/model gate. If those relationships cannot be qualified, the affected component states must be scenario-bounded rather than assigned fabricated probabilities.

### 5.3 Temporal non-equivalence rule

The 2017 Harvey hazard field may be overlaid on a later synthetic/current infrastructure representation only as a **stress-test scenario**:

```math
\boxed{
\text{Harvey hazard footprint}
+\text{current/synthetic network}
\neq
\text{historical Harvey reconstruction}.
}
```

No validation claim may compare modelled 2024/2025 network behavior directly against 2017 observed outages without a separate historical harmonization study.

---

## 6. Frozen bidirectional interdependency mechanisms

The H3 primary demonstrator includes exactly two operational interdependency mechanisms plus one common-cause hazard pathway.

### 6.1 P→T: traffic-signal electricity dependency

For signal `j`, define power-availability state

```math
a_j^{sig}(t)
=
\phi_j\left(S_{P,\mu(j)}(t),b_j(t)\right),
```

where `b_j` represents qualified backup-power state/capability.

Loss of utility power can force traffic signals into outage or backup operation; FHWA traffic-signal guidance explicitly discusses UPS/battery and generator systems used to maintain signal operation during power failures.

The exact mapping

```math
\text{signal-power loss}
\rightarrow
\text{capacity/delay effect}
```

is **OPEN** pending calibration/qualification. It may not be assigned by intuition.

### 6.2 T→P: repair-crew accessibility dependency

Road condition affects the time required for power-repair resources to reach damaged power assets. For damaged power component `i`, use the structural decomposition

```math
\boxed{
T_i^{restore}
=
T_i^{dispatch}
+T_i^{travel}(\mathcal G_T(t))
+T_i^{onsite}.
}
```

Transportation disruption therefore modifies the feasible restoration trajectory of the electrical system. This mechanism is established in interdependent P–T restoration research, including work in which signal outages degrade transportation and road delays affect repair-crew arrival and restoration sequencing.

The numerical repair-time and crew-resource models remain OPEN until qualified.

### 6.3 Common-cause flood pathway

```math
\eta_F
\rightarrow
\{\text{power-component exposure},\text{road-link exposure}\}.
```

This common exposure is **not itself a causal P↔T dependency**. It must remain distinct from the two directional mechanisms above.

---

## 7. Explicit exclusions from primary H3

To preserve identifiability and computational tractability, the following are excluded from the **primary** H3 demonstrator unless later evidence shows they are necessary to test H3:

```text
EV smart charging and V2G;
rail/transit traction-power coupling;
fuel-supply coupling;
mobile energy storage / MEPS;
telecommunication failure as a separate physical network;
full hydrodynamic flood evolution;
full historical Harvey outage reconstruction;
actual CenterPoint distribution topology;
AI/GNN traffic forecasting as a required H3 component.
```

They may be secondary extensions only after the primary H3 experiment closes.

---

## 8. Information and organization support layers

H3 retains the canonical P–T–I–O state semantics, but I/O are supporting layers rather than additional physical systems.

Minimum information objects:

```text
power state/load observations;
road/link state observations;
flood exposure state;
repair-status observations;
traffic-signal power/backup state where available.
```

Minimum organizational objects:

```text
repair-crew availability;
crew depot/start location;
permitted switching/repair actions;
road closure/access rules;
priority rules for critical service if authority-backed.
```

No stochastic organizational model is authorized until the uncertainty gate passes.

---

## 9. Candidate admissible action classes

The demonstrator freezes the **action classes**, not yet the final policy family `Pi_adm`:

```math
u(t)
=
\left(
 u_P^{switch/restore},
 u_T^{route/access},
 u_C^{dispatch/sequence}
\right).
```

Candidate classes are:

1. power isolation/switching/reconfiguration supported by the selected reduced SMART-DS model;
2. road-route selection / accessibility state used for repair travel;
3. repair-crew dispatch and repair sequence.

No action absent from the selected data/model realization may enter `Pi_adm` later merely to improve H3 performance.

---

## 10. Service and recovery objects inherited by the case

The case inherits without semantic change:

```math
K(t)=K_{phys}(t)\cap K_{svc}(t)\cap K_{op}(t),
```

```math
D(t)=K(t)^c\setminus F(t),
```

```math
G_{rec}(t)\subseteq K(t),
```

and

```math
\mathfrak R_T
=
\left(
\mathcal V_{\alpha,T_V},
\mathcal R_{\beta,T_R},
\rho_{\mathcal V},
T_{\mathcal V},
T_{rec},
P_{viable},
P_{recover}
\right).
```

The H3 case freeze does **not** assign numerical values to

```math
\boxed{
\{s_P^{min},s_T^{min},s_{P,rec},s_{T,rec},F,T_V,T_R,\alpha,\beta\}.
}
```

Those values/criteria must now be derived from the selected Houston case evidence or be preregistered as explicit bounded assumptions.

---

## 11. Critical-facility support data

Hospital/emergency-facility locations may be introduced as service-critical spatial anchors using authoritative/open Houston/FEMA/Hazus/HIFLD-style facility data. Houston publishes a hospital feature layer, and FEMA Hazus 6 uses HIFLD Open datasets for hospitals, emergency operations centers, fire stations, police stations, and transportation facilities.

Use of these locations does not imply that the synthetic SMART-DS grid reproduces the actual utility feeder serving a facility. Facility-to-synthetic-load mapping is a demonstrator construct and must be disclosed as such.

---

## 12. Data-vintage rule

The demonstrator intentionally combines datasets of different vintages. Therefore:

```math
\boxed{
\text{data-vintage mismatch}
\Rightarrow
\text{scenario interpretation, not historical reconstruction}.
}
```

The data manifest must record, for every source:

```text
source organization;
dataset/product title;
version/date;
download date;
license/access terms;
original CRS;
local file hash;
processing script/commit;
spatial clip rule;
time aggregation;
missing-data treatment.
```

---

## 13. Data-freeze sequence

The next reproducible implementation step is:

```math
\boxed{
\text{download/materialize}
\rightarrow
\text{hash}
\rightarrow
\text{reproject}
\rightarrow
\text{clip Houston}
\rightarrow
\text{network QA}
\rightarrow
\text{cross-layer mapping QA}
\rightarrow
\text{freeze manifest}.
}
```

Required quantitative QA before case-data freeze:

```text
number of retained P buses/nodes/feeders;
number of retained T nodes/links;
number of mapped traffic signals;
percentage of signals successfully mapped to eligible power nodes;
number of flood-exposed P components;
number/length of flood-exposed road links;
network connectivity before/after clipping;
OD coverage retained after clipping;
critical-facility coverage if used;
coordinate/mapping residuals;
all exclusions and missing records.
```

If the mapped P–T interface coverage is inadequate, the correct status is `CASE DATA GATE FAILED`; do not repair it by manually inventing interfaces.

---

## 14. H3 matched-comparison realization

The existing preregistration remains unchanged:

```math
\boxed{
Q_{conv}(\omega)
\quad\text{vs}\quad
Q_{VRR}(\omega)
=Q_{conv}(\omega)\cup\mathfrak R_T(\omega).
}
```

For each scenario `omega`, both comparators must share:

```text
same Houston networks;
same flood realization/damage state;
same initial state;
same P↔T mechanisms;
same observations;
same control authority;
same future outcome label;
same development/test split.
```

Only the Stage-5 viability/reach–avoid information supplied to the decision/prediction layer may differ.

---

## 15. Case-specific registry state after demonstrator freeze

| Object | Case source now identified? | Numerical/criterion state |
|---|---:|---|
| `s_P^{min}` | Houston power-service / critical-facility context fixed | OPEN |
| `s_T^{min}` | H-GAC mobility / emergency-access context fixed | OPEN |
| `s_{P,rec}` | Houston functional power-recovery context fixed | OPEN |
| `s_{T,rec}` | Houston functional transportation-recovery context fixed | OPEN |
| `F` | power safety + flood/road critical-access domains fixed | OPEN criteria/thresholds |
| `T_V` | Houston service-continuity context fixed | OPEN |
| `T_R` | Houston functional-recovery context fixed | OPEN |
| uncertainty models | source families identified | OPEN |
| `Pi_adm` | action classes identified | OPEN final semantics |
| H3 algorithm | not selected | OPEN |

Therefore:

```math
\boxed{G_{case}=1,\qquad G_K=0,\qquad G_U=0,\qquad G_{Pi}=0,\qquad G_{alg}=0.}
```

---

## 16. Frozen scientific claim boundary

The demonstrator may support claims of the form:

> For a geographically grounded semisynthetic Houston power–road system exposed to an observed Harvey flood-stress field, explicitly modelled P→T signal-power dependence and T→P repair-access dependence alter coupled service/recovery dynamics, and Stage-5 viability/reach–avoid information is or is not incrementally useful relative to conventional resilience-curve information under the preregistered experiment.

It may **not**, without additional validation, support claims that:

```text
the model reconstructs CenterPoint's actual grid;
the model reproduces Houston's actual 2017 outage chronology;
the synthetic feeder supplying a mapped signal/facility is the real feeder;
the H3 result generalizes to all cities/hazards;
Harvey damage probabilities were observed if they were generated from fragility models;
correlation/common flood exposure proves P↔T causal dependence.
```

---

## 17. Immediate next task

```math
\boxed{
\text{HOU data materialization + QA}
\rightarrow
\text{Houston-specific numerical threshold/recovery registry}
\rightarrow
\text{uncertainty qualification}.
}
```

First materialize and freeze the source datasets and their spatial mappings. Then populate, in order:

```math
\boxed{
s_P^{min}
\rightarrow
s_T^{min}
\rightarrow
s_{P,rec}
\rightarrow
s_{T,rec}
\rightarrow
F
\rightarrow
T_V
\rightarrow
T_R.
}
```

No solver selection is authorized before this case/data gate establishes the actual state dimension, interface count, threshold registry, and uncertainty representation.

---

## References — APA 7

Federal Highway Administration. (2023). *Traffic Signal Program Handbook* (FHWA-HOP-23-041). U.S. Department of Transportation. https://ops.fhwa.dot.gov/publications/fhwahop23041/

Houston-Galveston Area Council. (2026). *2025 Transportation Conformity: Documents and files*. https://www.h-gac.com/transportation-conformity/2025

Houston-Galveston Area Council. (n.d.). *Traffic data*. https://www.h-gac.com/home/transportation-planning/traffic-data

National Renewable Energy Laboratory. (n.d.). *SMART-DS: Synthetic Models for Advanced, Realistic Testing: Distribution Systems and Scenarios*. https://www.nrel.gov/grid/smart-ds.html

Pan, S., & Boyles, S. (2026). Optimising repair sequences for interdependent infrastructure resilience: A simulation model of power and transportation networks. *Civil Engineering and Environmental Systems, 43*(1), 26–48. https://doi.org/10.1080/10286608.2025.2602872

Texas A&M University Electric Grid Test Case Repository. (n.d.). *Texas Combined Transmission-Distribution Test Case*. https://electricgrids.engr.tamu.edu/texas7k-td/

U.S. Geological Survey. (2018). *Data used to characterize peak streamflows and flood inundation resulting from Hurricane Harvey of selected areas in southeastern Texas and southwestern Louisiana, August–September 2017*. https://www.usgs.gov/data/data-used-characterize-peak-streamflows-and-flood-inundation-resulting-hurricane-harvey

