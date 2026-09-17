# Sustainability Case/Data Feasibility Audit — v1.0

**Status:** CURRENT PRE-H4/H5 DATA-GATE AUDIT  
**Effective date:** 2026-09-18  
**Metric authority:** `SUSTAINABILITY_METRIC_CARDS_V1.md`  
**Admission authority:** `SUSTAINABILITY_DIMENSION_ADMISSION_AND_ACCOUNTING_STANDARD_V1.md`  
**Case authority:** `../../project/AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V2.md`  
**Case QC authority:** `../../project/AUSTIN_DATA_QC_AND_GATE_PROTOCOL_V1.md`  
**Candidate case:** `AUS-P5U-2018-V1`

---

## 1. Purpose

This audit tests whether the dimensions retained after the literature/evidence audit can actually be computed and defended for the current Austin coupled Power--Transportation candidate case.

It explicitly separates:

```math
\boxed{
\text{source exists}
\neq
\text{source is temporally/spatially compatible}
\neq
\text{data are materialized and pass QC}
\neq
\text{metric is confirmatory-ready}.
}
```

The audit is performed **before** H4/H5 results and is therefore allowed to narrow or exclude candidate dimensions without outcome-driven selection.

---

## 2. Upstream case constraint

The active case authority currently classifies `AUS-P5U-2018-V1` as:

```text
CANDIDATE CASE ONLY — NOT YET ADMISSIBLE
```

with current gates:

```text
G0 = PASS
G1 = OPEN
G2 = OPEN
G3 = SOURCE QUALIFIED / MATERIALIZATION + TOPOLOGY OPEN
G4 = SOURCE QUALIFIED / 2018 SPATIAL OVERLAP OPEN
G5 = SOURCE QUALIFIED / SEMISYNTHETIC MAPPING OPEN
G6 = OPEN
G7 = SOURCE QUALIFIED / INTERSECTION OPEN
G8 = OPEN
FINAL = NOT YET PASS
```

Therefore no sustainability/resource dimension can be classified `IN` for confirmatory H4/H5 **solely because an external data source exists**. Upstream case admissibility is a common prerequisite.

```math
\boxed{
G_{AUS}=0\text{ or OPEN}
\Rightarrow
G_{H4/H5,\,data}=\text{OPEN}.
}
```

This is not a negative thesis result. It is a data/admissibility state.

---

## 3. Feasibility criteria

For each metric card, this audit asks five case-specific questions in addition to the general nine admission gates:

1. **Vintage compatibility:** is a 2018 or defensibly normalized data source available?
2. **Spatial compatibility:** can the source be assigned to the frozen Austin/P5U support without false precision?
3. **Activity compatibility:** does the coupled model produce the physical activity required by the metric?
4. **Comparator compatibility:** can the same calculation be applied to `a_ref` and all `a_k` under matched scenarios?
5. **Independent adequacy route:** can calculation and uncertainty be checked without using H4/H5 outcomes to tune the metric?

Case feasibility is recorded as `PASS-SOURCE`, `OPEN-QC`, `BLOCKED`, or `OUT-SCOPE`. `PASS-SOURCE` is intentionally weaker than confirmatory `PASS`.

---

# 4. E1 direct intervention/recovery cost feasibility

## Available source routes

### Road/civil interventions

TxDOT maintains an official 2018 archive containing average bid-price data. This provides a temporally aligned candidate unit-cost source for applicable road/civil quantities.

### Power/DER interventions

NREL's 2018 Annual Technology Baseline provides 2018 cost definitions and technology-cost evidence for applicable power-generation technologies. Technology-specific storage, charging infrastructure, hardening and distribution-equipment costs may require additional authoritative sources depending on the final intervention set.

### Quantity data

Unit costs alone are insufficient. The quantities `q_m^{a_k}` must be generated from a frozen intervention design or observed engineering scope. The final intervention set `A` is not yet frozen.

## Feasibility judgment

| Requirement | State | Reason |
|---|---|---|
| 2018 price evidence exists | **PASS-SOURCE** | TxDOT 2018 + NREL 2018 provide candidate routes for some intervention classes |
| all intervention classes covered | **OPEN-QC** | `A` not frozen; charging/storage/hardening sources depend on chosen actions |
| quantities available | **OPEN-QC** | intervention designs not frozen |
| common price year/boundary | **OPEN-QC** | must be frozen after `A` but before H4 execution |
| uncertainty/validation | **OPEN-QC** | cross-source ranges not yet constructed |

**Metric state:** `CONDITIONAL`.

The cost metric is **in thesis scope** but cannot be confirmatory `IN` yet.

---

# 5. RES3 operational energy feasibility

## Available source routes

SMART-DS `v1.0/2018/AUS/P5U` provides 15-minute power/load time-series candidate data and OpenDSS topology after G1 materialization/QC. Coupled intervention simulations can produce charging, storage and other electrical power trajectories. This supplies a direct calculation route:

```math
E_{el}=\sum_t P(t)\Delta t.
```

## Limitations

- The current case is not yet admissible.
- Intervention-specific power trajectories do not exist until `A` is frozen and rerun through the verified model.
- Road-vehicle fuel energy is not inferable from geometry or distance alone; a qualified vehicle/fuel consumption model would be required.
- Operational/event energy does not include embodied/lifecycle energy.

## Feasibility judgment

| Requirement | State | Reason |
|---|---|---|
| electrical activity-data route | **PASS-SOURCE** | SMART-DS/model power trajectories are appropriate once G1 passes |
| temporal integration | **PASS-SOURCE** | 15-minute source/model resolution supports energy integration |
| intervention attribution | **OPEN-QC** | intervention set and baseline not frozen |
| fuel-energy route | **BLOCKED** for confirmatory use | no qualified case vehicle/fuel model frozen |
| VVUQ | **OPEN-QC** | efficiency/dispatch/model uncertainty not frozen |

**Metric state:** `CONDITIONAL`.

Primary feasible scope is **operational electrical energy**. Fuel energy remains excluded unless separately qualified before H4.

---

# 6. SUS1 carbon/GHG feasibility

## Regional electricity factor

EPA eGRID2018 is temporally aligned with the 2018 Austin candidate. For the ERCOT (`ERCT`) subregion the eGRID2018 summary table reports:

```text
Total-output CO2e:      936.1 lb CO2e/MWh
Non-baseload CO2e:    1266.5 lb CO2e/MWh
Grid gross loss:         4.87%
```

This establishes a **regional factor route**, not an Austin Energy utility-specific carbon-intensity observation.

## Fuel factors

EPA's GHG Emission Factors Hub retains an archived 2018 edition that can support declared fuel combustion activity if a fuel-using intervention is later activated.

## Critical accounting choice

The thesis must freeze which question is being answered:

```math
\boxed{
\text{regional attributional operational footprint}
\neq
\text{marginal/avoided project GHG effect}.
}
```

The ERCT total-output rate is a defensible candidate for a regional-average attributional sensitivity/footprint calculation. The non-baseload rate may be used only under a justified consequential/sensitivity interpretation; it is not automatically the true marginal response to a specific Austin intervention. Austin Energy portfolio accounting would require vintage-matched utility evidence and an explicit procurement/accounting rule.

## Feasibility judgment

| Requirement | State | Reason |
|---|---|---|
| 2018 regional electricity factor | **PASS-SOURCE** | EPA eGRID2018 ERCT available |
| 2018 fuel factors | **PASS-SOURCE** | archived EPA factor hub available if needed |
| activity data | **OPEN-QC** | depends on RES3 and intervention model |
| attributional/consequential convention | **OPEN-QC** | must be frozen pre-result |
| Austin-utility-specific factor | **OPEN-QC / not required by default** | regional eGRID is not utility-specific |
| uncertainty/sensitivity | **OPEN-QC** | factor-choice and activity uncertainty not yet propagated |

**Metric state:** `CONDITIONAL`.

Carbon/GHG is the strongest environmental-sustainability candidate, but it remains blocked from confirmatory `IN` until case, activity and factor-boundary gates pass.

---

# 7. RES1 crew/person-hours feasibility

The case QC protocol requires a declared crew origin, route feasibility and separation of dispatch, travel and on-site repair time. It explicitly prohibits inventing repair duration, travel time or crew parameters from metadata/geometry.

Generic FEMA material documents possible restoration-analysis assumptions and staffing defaults, but such values do not establish Austin-specific calibration. They can be used, at most, as benchmark/sensitivity evidence unless transferability is defended.

## Feasibility judgment

| Requirement | State | Reason |
|---|---|---|
| road-access mechanism | **PASS-SOURCE** | T->P repair-access mechanism is part of case design |
| crew route | **OPEN-QC** | G6 is open |
| task durations | **BLOCKED** for empirical claim | no qualified Austin task-duration source frozen |
| crew size/availability | **OPEN-QC** | requires official/local or qualified benchmark evidence |
| resource-efficiency role | **OPEN-QC** | only relevant if repair actions remain in `A` |

**Metric state:** `CONDITIONAL`.

It may remain a scenario/feasibility variable even if it never becomes a primary H4 response.

---

# 8. RES2 mobile emergency-resource feasibility

Direct P--T literature provides strong methodological precedent for EVs, mobile storage, emergency vehicles and repair resources. For this thesis, however, resource count/capacity is primarily a control/feasibility descriptor until a particular intervention family is frozen.

## Feasibility judgment

| Requirement | State | Reason |
|---|---|---|
| mechanism/evidence | **PASS-SOURCE** | direct P--T precedent |
| candidate fleet/resource definition | **OPEN-QC** | `A` not frozen |
| real Austin fleet evidence | **OPEN-QC** | not required for benchmark scenario, but required for empirical fleet claim |
| efficiency-denominator role | **OPEN-QC** | must be declared before H4 |

**Current state:** `ROLE-ONLY (FEAS)`; if promoted to a resource-efficiency response, status becomes `CONDITIONAL` until the above gates pass.

---

# 9. SUS2 distributional accessibility/equity feasibility

## Population/demographic data route

The U.S. Census Bureau's 2018 ACS 5-year estimates provide demographic, social, economic and housing variables down to census tract and block-group geography. Thus a vintage-compatible demographic data route exists.

## Remaining model requirements

A distributional-accessibility metric additionally requires:

- a frozen group/population definition;
- spatial overlay with the final P5U/transport support;
- a declared opportunity/service set;
- a travel-cost/accessibility function;
- treatment of people/trips crossing the analysis boundary;
- ACS margins of error / small-area uncertainty;
- a decision question showing that distributional information is not merely decorative.

Aggregate travel time or unmet trips are already resilience/service variables and cannot be rebranded as equity.

## Feasibility judgment

| Requirement | State | Reason |
|---|---|---|
| 2018 demographic data | **PASS-SOURCE** | ACS 5-year tract/block-group data available |
| final spatial overlap | **OPEN-QC** | Austin G2/G3 and P5U support not frozen |
| opportunity/service definition | **OPEN-QC** | not frozen |
| distributional metric validity | **OPEN-QC** | metric family not frozen |
| scope burden | **OPEN-QC** | must remain bounded enough for MSE |

**Metric state:** `CONDITIONAL`.

This dimension must not enter the primary H4/H5 vector unless the pre-result spatial/data feasibility check passes.

---

# 10. SUS3 materials and SUS4 embodied carbon feasibility

No final material-intensive intervention set or bill of materials is currently frozen. Direct coupled P--T resilience evidence is weaker for material inventories and embodied-carbon accounting than for operational cost/energy/carbon. A defensible embodied-carbon analysis would require intervention-specific quantities and qualified factors/EPDs plus an explicit partial lifecycle boundary.

## Feasibility judgment

| Requirement | SUS3 material quantity | SUS4 embodied GHG |
|---|---|---|
| direct case quantity data | **BLOCKED** | depends on SUS3 |
| factor/data route | **OPEN-QC** | **OPEN-QC** |
| boundary | **OPEN-QC** | **OPEN-QC** |
| MSE scope | **FAIL for current core** | **FAIL for current core** |

**Metric states:** `OUT` of the current confirmatory core. Reactivation requires a dated pre-result amendment and a final intervention set whose material burden is both material to the engineering decision and quantifiable.

Full multi-category LCA remains `OUT`.

---

## 11. Cross-metric data dependency graph

The audit reveals the following dependencies:

```math
\boxed{
G_{AUS}
\rightarrow
\mathcal A,a_{ref}
\rightarrow
\text{intervention trajectories/quantities}
\rightarrow
\begin{cases}
C_{direct}\\
E_{op}\\
H_{crew}\\
R_{mobile}
\end{cases}
\rightarrow
\begin{cases}
CO_{2e}\\
A_{dist}
\end{cases}
\rightarrow
H4/H5.
}
```

In particular:

```math
\boxed{
RES3\;E_{op}
\rightarrow
SUS1\;CO_{2e}
}
```

so carbon cannot become confirmatory-ready before its underlying activity data do.

---

## 12. Data-feasibility decision

At the current scientific state:

- **high-feasibility but still data-gated:** direct cost, operational electricity energy, operational/partial carbon;
- **conditional on intervention family:** crew-hours and mobile resources;
- **conditional on additional spatial/social construct work:** distributional accessibility/equity;
- **not justified within current confirmatory MSE core:** materials, embodied carbon and full LCA.

No candidate sustainability/resource response is yet `IN` because the frozen Austin candidate has not passed its common case-admissibility gates and the H4 intervention set is not yet frozen.

```math
\boxed{
\text{no current IN}
\neq
\text{no usable sustainability dimensions}.
}
```

It means the surviving dimensions are scientifically admissible **in principle** but not yet confirmatory-ready.

---

## 13. Required promotion sequence

A `CONDITIONAL` dimension can become `IN` only through this pre-result sequence:

```math
\boxed{
G_{AUS}=PASS
\rightarrow
\mathcal A,a_{ref}\text{ frozen}
\rightarrow
\text{metric-specific data materialized + QC}
\rightarrow
\text{boundary frozen}
\rightarrow
\text{VVUQ frozen}
\rightarrow
\text{admission re-audit}
\rightarrow
IN.
}
```

Changing a metric, factor convention, boundary, comparator or primary status after H4/H5 outcomes are observed requires a formal amendment and may convert the affected analysis to exploratory.

---

## 14. External data authorities verified for this audit

1. U.S. EPA, Historical eGRID Data, including eGRID2018: https://www.epa.gov/egrid/historical-egrid-data
2. U.S. EPA, eGRID2018 Summary Tables: https://www.epa.gov/sites/production/files/2020-01/documents/egrid2018_summary_tables.pdf
3. U.S. EPA, GHG Emission Factors Hub, including archived 2018 edition: https://www.epa.gov/climateleadership/ghg-emission-factors-hub
4. U.S. Census Bureau, 2018 ACS 5-Year Data: https://www.census.gov/data/developers/data-sets/acs-5year/2018.html
5. TxDOT, official 2018 average-bid-price archive: https://ftp.txdot.gov/pub/txdot-info/trf/hsip/2018/
6. NREL, 2018 Annual Technology Baseline: https://atb-archive.nrel.gov/electricity/2018/

Source existence is evidence of feasibility, not proof of case-level adequacy. Every source actually used in H4/H5 must be materialized or otherwise immutably identified, versioned, and included in the provenance/QC record.
