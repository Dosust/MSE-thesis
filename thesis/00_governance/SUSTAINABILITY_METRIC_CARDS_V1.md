# Sustainability Metric Qualification Cards — v1.0

**Status:** CURRENT PRE-H4/H5 QUALIFICATION RECORD  
**Effective date:** 2026-09-18  
**Governing standard:** `SUSTAINABILITY_DIMENSION_ADMISSION_AND_ACCOUNTING_STANDARD_V1.md`  
**Live register:** `SUSTAINABILITY_DIMENSION_REGISTER_V1.md`  
**Case authority:** `../../project/AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V2.md`  
**Experiment authority:** `MODEL_EXPERIMENT_VALIDATION_MATRIX.md`  
**Scientific scope:** RQ6/SO6/H4 and RQ7/SO7/H5

---

## 1. Purpose

These metric cards operationalize the Sustainability-Dimension Admission Matrix for the dimensions that survived the evidence audit far enough to require case/data qualification. A metric card is not permission to execute a confirmatory test. It is a reproducible specification of what the quantity would mean, how it would be calculated, what data are required, what can invalidate it, and which open gates prevent confirmatory use.

The controlling rule is:

```math
\boxed{
\text{metric definition}
\neq
\text{data availability}
\neq
\text{confirmatory admission}
\neq
\text{observed result}.
}
```

For a persistent intervention `a_k`, Stage 6 retains the typed consequence object

```math
\boxed{
\mathcal C(a_k)
=
\left(
\Delta\mathfrak R^{a_k},
\mathbf r^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k},
\mathcal F^{a_k},
\mathbf U^{a_k}
\right).
}
```

No metric below may enter `\mathbf r` or `\mathbf J_{\rm sus}` until all applicable admission gates pass under the frozen case and intervention set.

---

# MC-E1 — Direct intervention / recovery cost

**Dimension ID:** `E1`  
**Name:** Direct intervention or recovery cost  
**Primary role:** `RES` — economic/resource consequence  
**RQ/SO/H mapping:** RQ6/SO6/H4; input to RQ7/SO7/H5  
**Evidence status:** `E-PT-Q`, `E-ADJ-Q`  
**Current admission:** `CONDITIONAL`

## Scientific mechanism

A candidate intervention requires physical assets, installation, labor, mobilization, operation or recovery activities whose quantities and unit prices determine direct expenditure. The mechanism is

```math
\boxed{
a_k
\rightarrow
\mathbf q^{a_k}
\rightarrow
C_{\rm direct}^{a_k}.
}
```

For a declared set of cost items `m`, a generic event/planning calculation is

```math
\boxed{
C_{\rm direct}^{a_k}
=
\sum_m q_m^{a_k}c_m^{(y,g)}
+
C_{\rm install}^{a_k}
+
C_{\rm mobilize}^{a_k}
+
C_{\rm op}^{a_k},
}
```

where `q_m` is an intervention quantity and `c_m^(y,g)` is a unit cost referenced to declared price year `y` and geography `g`. Terms are included only when applicable; the equation is not permission to invent missing items.

## Units

Declared currency in a declared price year, provisionally `USD_2018` for the Austin 2018 case unless the final intervention evidence requires another basis and a transparent conversion is frozen.

## Preferred interpretation

Lower cost is preferable conditional on comparable resilience effectiveness and feasibility. Cost is **not** equivalent to economic sustainability.

## Comparator

```math
\Delta C^{a_k}=C_{\rm direct}^{a_k}-C_{\rm direct}^{a_{ref}}.
```

The same cost components and price basis must be applied to every candidate action.

## Accounting boundary

Candidate boundary: intervention-specific direct capital/installation/recovery/operating expenditures within the declared Stage-6/7 intervention horizon. Monetized service losses, macroeconomic effects, health damages and social welfare are excluded unless separately activated under another metric.

## Data route

- TxDOT 2018 average bid-price data are an official candidate source for applicable road/civil work items.
- NREL 2018 Annual Technology Baseline is an authoritative candidate source for applicable electric-generation technology capital/operating cost concepts.
- Technology-specific charging/storage costs require intervention-specific authoritative or peer-reviewed sources; a current cost estimator cannot silently substitute for a 2018 cost without declared temporal normalization.
- Actual quantities must come from the frozen intervention design/model, not from generic literature averages.

## Uncertainty and sensitivity

Propagate uncertainty in unit price, installed quantity, mobilization/installation scope, and temporal normalization. If source ranges exist, preserve them. Do not invent a probability distribution solely to enable Monte Carlo analysis.

## Verification

- dimensional check: quantity × unit price = currency;
- independent recomputation of itemized totals;
- identical item taxonomy across interventions;
- zero-change limiting case: if `a_k=a_ref`, `Delta C=0` within numerical tolerance.

## Validation / benchmark

Cross-check unit costs against at least one independent authoritative/peer-reviewed source where feasible. Large disagreement must be retained as uncertainty or resolved before confirmatory use.

## Double-counting control

`C_direct` excludes monetized electricity-service loss, mobility-service loss, recovery-time damage and any quantity already represented in the resilience response unless H4 explicitly activates a separate welfare-cost analysis.

## Open gates

`D`: intervention set and item quantities not frozen; `B`: exact included cost components/price year not frozen; `V`: uncertainty model and cross-source adequacy not frozen.

## Promotion condition

`CONDITIONAL -> IN` only before H4 results are inspected and only after the Austin case is admissible, `A` and `a_ref` are frozen, the itemized cost boundary is frozen, source/provenance is complete, and VVUQ passes.

---

# MC-E3 — Monetized outage / service-loss cost

**Dimension ID:** `E3`  
**Name:** Monetized outage or service-loss cost  
**Primary role:** potential `RES` / economic consequence  
**RQ/SO/H mapping:** potentially RQ6/H4; not required for H5  
**Evidence status:** `E-PT-Q`  
**Current recommendation:** `OUT` of the primary confirmatory vector; optional sensitivity only by preregistered amendment.

## Scientific mechanism

Service loss can be monetized only through a separately justified valuation function:

```math
C_{loss}
=
\mathcal V_P(L_P,t)
+
\mathcal V_T(L_T,t),
```

where `L_P` and `L_T` are already resilience/service losses. Because the same physical losses are core H1–H5 outputs, monetization creates a substantial double-counting and preference-assumption risk.

## Exclusion rationale

The primary thesis can evaluate resilience in physical/service units and direct intervention cost separately. A monetized service-loss objective is not necessary to answer RQ6/H4 or RQ7/H5 and would require defensible value-of-lost-load / value-of-time / welfare assumptions. It is therefore excluded from the primary confirmatory vector unless a later, pre-result amendment demonstrates decision necessity and valid Austin-specific valuation evidence.

---

# MC-RES1 — Crew / person-hours

**Dimension ID:** `RES1`  
**Name:** Repair/recovery labor effort  
**Primary role:** `RES`  
**RQ/SO/H mapping:** RQ6/SO6/H4 when repair-resource interventions are active; H5 input  
**Evidence status:** `E-PT-Q`  
**Current admission:** `CONDITIONAL`

## Scientific mechanism

Transportation accessibility, dispatch timing and repair task duration determine labor effort and resource occupancy:

```math
\boxed{
H_{crew}^{a_k}
=
\sum_r n_r\,T_r^{a_k},
}
```

where `n_r` is the number of personnel assigned to repair task/team `r` and `T_r` is the declared task-duration/occupancy time. Travel time and on-site repair time remain distinct:

```math
T_i^{restore}
=
T_i^{dispatch}
+T_i^{travel}
+T_i^{onsite}.
```

## Units

person-hours; optionally crew-hours if crew composition is fixed and separately reported.

## Accounting boundary

Only labor directly assigned to modeled recovery tasks within the scenario horizon. Administrative labor, supply-chain labor and embodied labor are excluded unless explicitly activated.

## Data route

The Austin QC protocol currently states that repair duration, travel time and crew parameters cannot be inferred from geometry/metadata alone. Qualified task-duration and staffing evidence must therefore come from local/official records or peer-reviewed/benchmark evidence with a declared transferability domain. Generic FEMA defaults may be used only as sensitivity evidence unless independently shown adequate for the case.

## Uncertainty

Task duration, crew availability, traffic delay and parallel-work assumptions are candidate sensitivity variables. Correlation among repair tasks must not be ignored when resource sharing is modeled.

## Double-counting control

Labor cost may be derived from labor hours, but H4 must not treat both labor cost and labor hours as independent sustainability information without explaining the different decision meaning.

## Open gates

`D`: no qualified Austin repair-duration/staffing data frozen; `B`: task classes/horizon open; `V`: transferability/validation open; relevance depends on final intervention set.

## Promotion condition

Only if repair-resource interventions remain in `A` and a defensible task/staffing data route is frozen before outcomes are inspected.

---

# MC-RES2 — Mobile emergency-resource quantity / capacity

**Dimension ID:** `RES2`  
**Name:** Mobile emergency-resource availability/capacity  
**Primary role:** default `FEAS`; may become `RES` only in a declared efficiency test  
**RQ/SO/H mapping:** RQ4/RQ6/RQ7 depending intervention  
**Evidence status:** `E-PT-Q`  
**Current status:** `ROLE-ONLY` by default; `CONDITIONAL` only if promoted to an H4 efficiency denominator.

## Scientific mechanism

Mobile resources constrain feasible actions and can alter service recovery. Candidate quantities include vehicle count, power rating, stored energy, operating hours or travelled distance.

```math
\mathcal U_t
=
\mathcal U(\widehat Y_t,z_I,z_O;R_{mobile}).
```

The resource amount is not a sustainability consequence by itself.

## Role rule

Unless H4 specifically asks how much resilience benefit is obtained per mobile-resource unit, `RES2` remains a feasibility/control variable and does not enter `J_sus`.

## Data route

Values must be derived from the frozen intervention/resource scenario, not selected post hoc to maximize resilience. If a real fleet is claimed, official fleet data are required; otherwise the quantity must be labeled a benchmark/scenario design variable.

---

# MC-RES3 — Operational energy

**Dimension ID:** `RES3`  
**Name:** Operational/recovery energy attributable to an intervention  
**Primary role:** `RES`  
**RQ/SO/H mapping:** RQ6/SO6/H4; H5 input  
**Evidence status:** `E-PT-Q`  
**Current admission:** `CONDITIONAL`

## Scientific mechanism

An intervention can change electricity charging/discharging, storage losses, mobile-resource operation and other energy-consuming processes. For electrical energy represented by model power trajectories:

```math
\boxed{
E_{el}^{a_k}
=
\sum_{t\in\mathcal T}
P_{int}^{a_k}(t)\Delta t.
}
```

For net additional intervention energy relative to a reference:

```math
\boxed{
\Delta E_{el}^{a_k}
=
E_{el}^{a_k}-E_{el}^{a_{ref}}.
}
```

Fuel energy, if activated, must be calculated separately from measured/modeled fuel quantity and an authoritative heating-value convention; it must not be inferred from road distance without a qualified vehicle/fuel model.

## Units

kWh/MWh for electricity; MJ/GJ or physical fuel units plus conversion basis for fuel. Keep electricity and fuel disaggregated before any aggregation.

## Accounting boundary

Candidate primary scope: **operational/event energy during the declared disruption/recovery horizon**. Embodied/lifecycle energy is excluded from `RES3`.

## Data route

- SMART-DS candidate power data provide 15-minute electrical P/Q/load trajectories for the 2018 synthetic Austin benchmark after G1 passes.
- Intervention-specific EV/storage/charger power profiles must come from the coupled simulation.
- Traffic/fuel energy requires a separate validated consumption model and is not presently qualified.

## Uncertainty

Power/charging profile uncertainty, storage efficiency, intervention dispatch and scenario duration. If fuel is activated, vehicle consumption and congestion dependence become additional uncertainties.

## Verification

Energy balance, sign convention, storage round-trip losses, timestep integration and unit conversion must pass. The identical-trajectory limit must yield `Delta E=0`.

## Validation

Electrical load/operation must remain within validated model/domain ranges. Energy is not considered validated merely because numerical integration succeeds.

## Double-counting control

Energy and GHG may both be retained only if their distinct decision roles are explicit; GHG derived from energy is statistically dependent on this metric.

## Open gates

Austin G1/case admissibility, final intervention set, exact energy boundary and VVUQ.

---

# MC-SUS1 — Carbon / greenhouse-gas consequence

**Dimension ID:** `SUS1`  
**Name:** Operational or explicitly partial intervention greenhouse-gas consequence  
**Primary role:** `SUS`  
**RQ/SO/H mapping:** RQ6/SO6/H4; RQ7/SO7/H5  
**Evidence status:** `E-PT-Q`, `E-ADJ-Q`, `E-STD`  
**Current admission:** `CONDITIONAL`

## Scientific mechanism

Energy/fuel activity attributable to an intervention is mapped to GHG emissions through declared factors:

```math
\boxed{
J_{GHG}^{a_k}
=
\sum_s A_s^{a_k}EF_s,
}
```

where `A_s` is a traceable activity quantity and `EF_s` is a factor with declared source, geography, year and gas/GWP basis.

For a matched intervention comparison:

```math
\boxed{
\Delta J_{GHG}^{a_k}
=
J_{GHG}^{a_k}-J_{GHG}^{a_{ref}}.
}
```

## Units

kg CO2e or t CO2e. Report physical activity alongside the converted GHG result.

## Accounting boundary

The default candidate is **operational/event or explicitly partial intervention carbon**, not full LCA. The final card must state whether electricity generation, grid losses, fuels, intervention construction/materials and avoided emissions are included or excluded.

## Austin 2018 factor route

EPA eGRID2018 provides a temporally aligned regional factor for the ERCOT (`ERCT`) subregion. The 2018 summary table reports:

- total-output CO2e rate: `936.1 lb CO2e/MWh`;
- non-baseload CO2e rate: `1266.5 lb CO2e/MWh`;
- grid gross loss: `4.87%`.

These factors are **regional**, not an Austin Energy utility-specific portfolio factor. The total-output factor is a candidate attributional regional factor; the non-baseload factor may be informative for a sensitivity/consequential interpretation but must not automatically be labeled the marginal emissions effect of a specific intervention. Austin Energy-specific procurement/generation accounting would require a qualified vintage-matched utility factor and an explicit attribution rule.

If liquid fuels enter the intervention, EPA's archived 2018 GHG Emission Factors Hub is an authoritative candidate source, subject to exact fuel/process matching.

## Factor-choice rule

The factor convention must be frozen **before** confirmatory results:

```math
\text{attributional footprint}
\neq
\text{marginal/avoided project effect}.
```

A project-level emission-reduction claim requires an explicit counterfactual and appropriate project-accounting logic; it cannot be inferred from an arbitrary average factor.

## Standards boundary

Full LCA terminology is prohibited unless ISO 14040/14044 requirements are explicitly activated. A partial carbon-footprint study must state its boundary and follow the applicable ISO 14067 principles if that terminology is used.

## Uncertainty

Activity data, emission factor, temporal/geographic mismatch, grid-loss treatment, storage losses, and factor-choice sensitivity. Electricity GHG uncertainty is coupled to `RES3` energy uncertainty.

## Verification

- unit conversion and factor application tests;
- sign convention for imports/exports/V2G;
- baseline equality gives `Delta J_GHG=0`;
- no negative 'avoided' emissions without a declared counterfactual.

## Validation / adequacy

Factor provenance and case geography/vintage must be documented. Regional eGRID adequacy is a modeling assumption, not evidence of Austin Energy utility-specific emissions.

## Open gates

Austin case admissibility; final energy activity data; factor convention; inclusion of grid losses; boundary; uncertainty propagation.

---

# MC-SUS2 — Distributional accessibility / equity consequence

**Dimension ID:** `SUS2`  
**Name:** Distributional mobility-access consequence  
**Primary role:** `SUS` if activated; aggregate accessibility remains `R-SVC`  
**RQ/SO/H mapping:** RQ6/H4 and RQ7/H5 only if distributional decision value is demonstrated  
**Evidence status:** `E-PT-C`, `E-CON`; official demographic data route exists  
**Current admission:** `CONDITIONAL`

## Construct boundary

This card is **not** the aggregate transportation service variable already used in Stage 5. It concerns how service/access consequences are distributed across declared geographic or population groups.

```math
\boxed{
A_{aggregate}
\neq
A_{distributional}.
}
```

## Candidate mathematical families

No primary metric is frozen yet. Admissible families include opportunity-based accessibility, relative service-loss burden or group-specific recovery measures. A generic accessibility form is

```math
A_g(t)
=
\sum_{o\in\mathcal O}w_o f(c_{go}(t)),
```

but `O`, `w_o`, impedance function `f`, group definition `g` and travel-cost variable `c` must be independently justified before use. This equation is a candidate family, not the frozen thesis metric.

## Data route

The U.S. Census 2018 ACS 5-year dataset provides demographic and socioeconomic estimates down to census tract and block-group geographies. This gives a vintage-compatible population/group data route for the Austin 2018 case. However, feature-level overlap with the final P5U transport support, the relevant opportunity/destination set, and the specific distributional groups remain unfrozen.

## Units

Depends on the selected construct: opportunities reachable, minutes/hours, service-loss ratio, or a declared dimensionless distribution metric. Any index requires transparent normalization and interpretation.

## Accounting boundary

Freeze population/group definition, spatial unit, transportation opportunity/service set, time horizon, treatment of travelers outside the study boundary, and handling of ACS sampling uncertainty.

## Uncertainty

ACS margins of error where applicable, spatial aggregation/MAUP, network travel-time uncertainty, group definition and accessibility-function choice.

## Double-counting control

If the same travel-time or unmet-trip variable is used in Stage-5 resilience and in this metric, the Stage-6 quantity must represent **distributional heterogeneity**, not a duplicate aggregate average.

## Open gates

Metric construct, opportunity set, spatial overlay, ACS variable set, validation/interpretation and MSE-scope burden.

## Promotion condition

Promote only if a pre-result feasibility study demonstrates that the distributional metric can materially differentiate candidate interventions and can be computed reproducibly from qualified Austin data without expanding the thesis into a separate equity study.

---

# MC-SUS3 — Material quantity

**Dimension ID:** `SUS3`  
**Name:** Material quantity used by persistent physical interventions  
**Primary role:** `RES`  
**Evidence status:** `E-ADJ-Q`, `E-STD`  
**Current recommendation:** `OUT` of the core confirmatory H4/H5 scope under the present case/intervention state.

## Scientific mechanism

Persistent construction can require material quantities:

```math
M^{a_k}=\sum_m q_m^{a_k}.
```

However, no final intervention set or bill of materials is presently frozen. Generic material assumptions would therefore be sensitivity-only and would not support a confirmatory resource claim.

## Activation rule

`SUS3` may be reactivated only by a dated **pre-result** amendment if the final `A` contains material-intensive structural alternatives and authoritative/engineering quantity takeoffs can be produced for all compared actions.

---

# MC-SUS4 — Embodied / material GHG

**Dimension ID:** `SUS4`  
**Name:** Embodied/material greenhouse-gas consequence  
**Primary role:** `SUS`  
**Evidence status:** `E-ADJ-Q`, `E-STD`  
**Current recommendation:** `OUT` of the core confirmatory H4/H5 scope.

## Scientific mechanism

If material quantities are available,

```math
J_{GHG}^{emb,a_k}
=
\sum_m q_m^{a_k}EF_m.
```

At present `SUS3` lacks a frozen bill of materials; hence an embodied-carbon comparison would require an additional inventory/EPD data program. This is methodologically valid but not currently justified within the MSE core.

## Activation rule

Requires prior activation of `SUS3`, declared cradle-to-gate or other partial boundary, qualified factors/EPDs, and an amendment before H4/H5 results.

---

## 2. Role-only records that do not require sustainability admission

The following quantities remain mandatory in their existing scientific roles but must not enter `J_sus` merely to enlarge the sustainability vector:

| ID | Quantity | Frozen primary role |
|---|---|---|
| `R1` | electricity service / served load | `R-SVC` |
| `R2` | mobility service / unmet trips / travel performance | `R-SVC` |
| `R3` | aggregate accessibility | `R-SVC` |
| `R4` | recovery/restoration time | `R-SVC` |
| `E2` | budget/capital ceiling | `FEAS` |
| `RES2` | mobile-resource capacity/count | `FEAS` unless explicitly promoted to efficiency |
| `T1` | renewable-generation capacity/share | `TRANS` |
| `T2` | storage capacity | `TRANS` |
| `T3` | charging-station addition/relocation/capacity | `TRANS` |
| `T4` | line/road hardening or redundancy | `TRANS` |

---

## 3. Current metric qualification result

The metric definitions are now sufficiently specified to support a case/data feasibility audit. None of the `CONDITIONAL` cards is yet confirmatory-ready because the Austin candidate itself has not passed G0–G8 and the final Stage-6 intervention set has not been frozen.

```math
\boxed{
\text{qualified metric semantics}
\not\Rightarrow
\text{qualified case data}.
}
```

The controlling next artifact is `SUSTAINABILITY_CASE_DATA_FEASIBILITY_AUDIT_V1.md`.

---

## References / data authorities used by these cards

- U.S. EPA. *Historical eGRID Data — eGRID2018*. https://www.epa.gov/egrid/historical-egrid-data
- U.S. EPA. *eGRID2018 Summary Tables*. https://www.epa.gov/sites/production/files/2020-01/documents/egrid2018_summary_tables.pdf
- U.S. EPA. *GHG Emission Factors Hub* (includes archived 2018 factors). https://www.epa.gov/climateleadership/ghg-emission-factors-hub
- U.S. Census Bureau. *2018 ACS 5-Year Data*. https://www.census.gov/data/developers/data-sets/acs-5year/2018.html
- TxDOT. *2018 average bid prices* (official archive). https://ftp.txdot.gov/pub/txdot-info/trf/hsip/2018/
- NREL. *2018 Annual Technology Baseline*. https://atb-archive.nrel.gov/electricity/2018/
- ISO 14040/14044 and ISO 14067 are applicable only if their corresponding lifecycle/carbon-footprint claims are activated.
