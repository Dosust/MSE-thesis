# Sustainability Outcome Specification v1.0

**Date:** 2026-09-16  
**Status:** PREREGISTERED WORKING SPECIFICATION; NUMERICAL THRESHOLDS/DATA FITS NOT FROZEN  
**Parent:** `RESILIENCE_SUSTAINABILITY_CAUSAL_TRANSLATION_MATRIX_V1.md`

## 1. Purpose

Specify the smallest defensible sustainability outcome set that can be causally connected to validated Power–Transportation interdependency mechanisms. This file defines quantities, units, temporal semantics, data requirements and validation gates. It does not claim that any numerical sustainability improvement has been demonstrated.

The retained core is

```math
\boxed{
\mathbf J_{\rm sus}^{core}
=
[J_{access},J_{energy},J_{carbon}]^\top.
}
```

## 2. Two-horizon rule

Resilience and sustainability are evaluated at different but connected horizons.

```math
\boxed{T_R=\text{event/cascade/recovery horizon}}
```

and

```math
\boxed{T_L=\text{longer sustainability accounting horizon}.}
```

No event-scale result is automatically labeled a long-term sustainability result.

For each outcome `J_j`, distinguish:

```math
J_j^{event}(\omega)=\text{scenario/event-conditioned consequence over }T_R,
```

from

```math
J_j^{long}=\text{long-horizon consequence over }T_L.
```

If event probabilities/rates are independently justified, a long-horizon expectation may use them. If not, retain a scenario vector/set and do not invent probabilities:

```math
\boxed{
\mathcal J_j^{scenario}
=\{J_j(\omega):\omega\in\Omega\}.
}
```

## 3. Accessibility outcome `J_access`

### 3.1 Primary operational form

Let `q_od^req(t)` be requested OD demand and `q_od^cmp(t)` completed OD service for OD pair `od`, with policy/evidence-based weights `w_od>=0`.

Define normalized mobility accessibility/service

```math
\boxed{
A_{OD}(t)
=
\frac{\sum_{od} w_{od}q_{od}^{cmp}(t)}
{\sum_{od} w_{od}q_{od}^{req}(t)}
}
```

when the denominator is positive and its counterfactual/requested-demand estimator is validated.

The event accessibility deficit is

```math
\boxed{
J_{access}^{event}
=
\int_0^{T_R}
[A_{OD}^{ref}(t)-A_{OD}(t)]_+\,dt.
}
```

If `A_OD` is dimensionless, `J_access^event` has units of time (e.g. service-deficit hours). With population/flow weights retained in physical units, the result can be expressed as person-hours or trip-hours.

### 3.2 Essential-service accessibility variant

Where destinations `f` represent essential services and travel-time thresholds have independent provenance, define

```math
A_{ES}(t)
=
\frac{\sum_g w_g\sum_f \nu_f\,\mathbf 1[T_{gf}(t)\le\tau_f]}
{\sum_g w_g\sum_f \nu_f}.
```

No `tau_f` may be invented for convenience. If defensible thresholds are unavailable, use continuous travel-time or generalized-cost accessibility instead of a thresholded form.

### 3.3 Required data

```text
requested/counterfactual OD demand;
completed OD/trips;
road/link travel times or speeds;
charging-station functionality/availability when EV accessibility is tested;
origin/destination or essential-service geography;
weights only if independently justified.
```

### 3.4 Evidence anchors

- Wang et al. (2021), DOI `10.1111/mice.12736` — charging-station failures change electrified-road-network performance.
- Essus & Rachunok (2024), *Electric vehicles limit equitable access to essential services during blackouts* — direct blackout → EV mobility/accessibility pathway.
- Govina, Boakye & Okte (2026), DOI `10.1111/risa.70310` — accessibility metrics grounded in travel time/distance and access to critical facilities.

### 3.5 Gate

`J_access` is admissible as a core outcome only after requested-demand reconstruction and spatial support are validated. Current TLC completed-trip data alone are insufficient to establish `q_od^req`.

---

## 4. Operational energy outcome `J_energy`

Energy must be defined as a physical accounting quantity, not a generic sustainability score.

### 4.1 Charging/grid energy

For EV/grid exchange power `P_EV(t)` with charging positive and V2G export negative,

```math
\boxed{
E_{EV}
=
\int_0^{T_L}P_{EV}(t)\,dt
}
```

with units `MWh`.

If generation dispatch is represented by sources `g`,

```math
E_g=\int_0^{T_L}P_g(t)\,dt.
```

### 4.2 Renewable curtailment/integration

If available renewable power is `P_RE^avail(t)` and used renewable power is `P_RE^use(t)`,

```math
\boxed{
E_{curt}
=
\int_0^{T_L}
[P_{RE}^{avail}(t)-P_{RE}^{use}(t)]_+dt.
}
```

This is preferable to a vague `renewable integration score` because it has units and conservation meaning.

### 4.3 Intervention comparison

For transformation `a_k`,

```math
\Delta E_k=E(\mathfrak M_k)-E(\mathfrak M_0),
```

and similarly for `E_curt`.

### 4.4 Required data/model

```text
EV charging/discharging power profiles;
network load profiles;
generation/renewable availability if generation mix is modeled;
losses if included;
storage charging/discharging if included;
consistent time resolution and energy-conservation checks.
```

### 4.5 Evidence anchors

- Nature Energy (2022), DOI `10.1038/s41560-022-01105-7` — charging location/control changes peak net demand, storage need, renewable excess and emissions.
- NREL managed-charging synthesis — managed charging can support variable-renewable integration, reliability and lower system costs/emissions.
- Yang, Abdin & Puchinger (2024), DOI `10.1016/j.trc.2024.104726` — coupled vehicle-grid scheduling with renewable integration.

### 4.6 Gate

Current H1 M0/M1/M2 service models do not by themselves establish a complete generation/renewable accounting architecture. `J_energy` is therefore `CONDITIONAL_CORE` until the power-side energy balance and required data are frozen and verified.

---

## 5. Operational carbon outcome `J_carbon`

Operational and embodied carbon must remain separate.

### 5.1 Dispatch-resolved operational carbon

If generator outputs `P_g(t)` and generator-specific emission intensities `e_g(t)` are available,

```math
\boxed{
J_{carbon}^{op}
=
\sum_g\int_0^{T_L}e_g(t)P_g(t)\,dt.
}
```

Units: `kgCO2e` or `tCO2e`.

### 5.2 Grid-factor operational carbon

If only a defensible time-varying grid emissions factor `e_grid(t)` is available,

```math
\boxed{
J_{carbon}^{op}
=
\int_0^{T_L}e_{grid}(t)P_{grid}^{net}(t)\,dt.
}
```

The study must state whether `e_grid` is average, marginal or consequential; these are not interchangeable.

### 5.3 Embodied/lifecycle carbon

For structural interventions,

```math
J_{carbon}^{life}
=J_{carbon}^{emb}+J_{carbon}^{op}+J_{carbon}^{maint}+J_{carbon}^{EOL}
```

is permitted only if intervention-specific lifecycle inventories/EPDs or equivalent data are available. Otherwise thesis conclusions are restricted to operational carbon.

### 5.4 Evidence anchors

- Nature Energy (2022), DOI `10.1038/s41560-022-01105-7` — charging control/infrastructure influence generation-level emissions.
- Applied Energy (2024), DOI `10.1016/j.apenergy.2024.123618` — prospective life-cycle assessment of V2G environmental effects.
- NREL managed-charging synthesis — managed charging is associated with emissions reduction and renewable-integration value across prior studies.

### 5.5 Gate

No carbon conclusion is admissible until the emissions accounting convention, power balance, source data and temporal resolution are frozen before intervention-result inspection.

---

## 6. Cost and equity treatment

### 6.1 Cost

Initially treat cost primarily as a feasibility/budget quantity:

```math
\boxed{C(a_k)\le B}
```

for matched-budget intervention comparisons.

A lifecycle economic objective may be added later as

```math
J_{cost}=C_{capex}+C_{opex}+C_{repair}+C_{disruption},
```

with NPV treatment only after discount rate and accounting boundary have independent provenance.

### 6.2 Equity

Equity is not a scalar by default. It requires a protected/declared grouping and a service burden. A candidate form is

```math
\Delta A_g=A_g-A_{ref}
```

or a Gini/Theil/subgroup-gap statistic over accessibility/service burden. It becomes active only after demographic/spatial data and grouping rules are predeclared.

## 7. Resilience-to-sustainability translation is intervention-mediated

The admissible Stage-6 map is

```math
\boxed{
\Delta\mathbf J_{\rm sus}^{core}
=
\Phi_{RS}(\mathbf R,\mathbf a,\mathfrak M,\omega,T_L)
}
```

not

```math
\mathbf J_{\rm sus}=f(\text{one resilience score}).
```

For each intervention `a_k`, execute

```math
\mathfrak M_k
\rightarrow Y_k(t)
\rightarrow \mathbf R_k
\rightarrow \mathbf J_{{\rm sus},k}^{core}.
```

Matched comparison requires identical hazard/scenario, initial condition, accounting horizon and declared budget/resource envelope.

## 8. Multiobjective decision rule

Do not create arbitrary weights. Retain the objective vector

```math
\mathbf J_k
=
[J_{risk/resilience,k},J_{access,k},J_{energy,k},J_{carbon,k}]
```

with cost/resource feasibility constraints as appropriate.

Define dominance consistently so that all objectives have declared improvement directions, and compute

```math
\boxed{
\mathcal P^*
=
\{a\in\mathcal A^{feas}:\nexists a'\in\mathcal A^{feas}\text{ that dominates }a\}.
}
```

Weights may be introduced only when stakeholder/policy evidence justifies them.

## 9. Verification and validation requirements

Before `J_access`, `J_energy`, or `J_carbon` can support a thesis conclusion:

```text
quantity definition frozen;
units checked;
accounting boundary frozen;
time horizon frozen;
input data provenance recorded;
missingness/uncertainty characterized;
conservation/dimensional checks passed;
independent validation or benchmark route defined;
intervention values not used to tune thresholds or accounting conventions.
```

## 10. Current scientific state

```math
\boxed{
J_{access}:\ \text{CORE STRUCTURE PASS / DATA GATE OPEN}
}
```

```math
\boxed{
J_{energy}:\ \text{CONDITIONAL CORE / POWER-ACCOUNTING MODEL REQUIRED}
}
```

```math
\boxed{
J_{carbon}:\ \text{CONDITIONAL CORE / EMISSIONS MODEL + DATA REQUIRED}
}
```

No numerical sustainability outcome is yet claimed.
