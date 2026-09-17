# Sustainability-Dimension Register — v1.0

**Status:** FROZEN PRE-H4/H5 STATUS REGISTER / DATA-GATED  
**Effective date:** 2026-09-18  
**Governing standard:** `SUSTAINABILITY_DIMENSION_ADMISSION_AND_ACCOUNTING_STANDARD_V1.md`  
**Scientific authority:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Evidence basis:** formal Section-1.5 evidence audit + audited P--T corpus + verified standards/close precedents  
**Metric qualification:** `SUSTAINABILITY_METRIC_CARDS_V1.md`  
**Case/data audit:** `SUSTAINABILITY_CASE_DATA_FEASIBILITY_AUDIT_V1.md`  
**Current status freeze:** `SUSTAINABILITY_ADMISSION_FREEZE_V1.md`  
**Change rule:** update only with a dated evidence/data/boundary rationale; promotion to confirmatory `IN` requires a pre-result versioned admission re-audit.

---

## 1. Purpose

This register is the control table for every quantity proposed as a resilience, resource-efficiency, feasibility, sustainability or transformation variable in Stages 6--7.

It answers:

```math
\boxed{
\text{What is the quantity?}
\rightarrow
\text{What role does it play?}
\rightarrow
\text{Does it pass admission?}
\rightarrow
\text{What remains unresolved?}
}
```

The register does **not** define sustainability by checklist accumulation. Its purpose is to prevent unsupported, duplicated or unmeasurable dimensions from entering H4/H5.

---

## 2. Gate notation

The nine gates are:

- `M` mechanism;
- `Q` RQ/H decision relevance;
- `X` construct validity / non-duplication;
- `D` data/provenance;
- `U` units/metric specification;
- `B` accounting boundary;
- `K` comparator/counterfactual;
- `V` VVUQ/validation route;
- `S` MSE-scope feasibility.

States:

- `P` = PASS;
- `C` = CONDITIONAL/open prerequisite;
- `F` = FAIL for current thesis scope;
- `—` = not evaluated as a sustainability dimension because its primary role is already fixed elsewhere.

Admission states:

- `IN` = confirmatory-ready only after all applicable gates pass;
- `CONDITIONAL` = scientifically defensible candidate but one or more execution gates remain open;
- `ROLE-ONLY` = required thesis variable but not part of `\mathbf J_{sus}`;
- `OUT` = excluded from core quantitative thesis scope;
- `CONTEXT` = discussion/limitation relevance only.

At the present freeze, the confirmatory `IN` set is empty because the Austin candidate case has not passed G0--G8 and the Stage-6 intervention set is not frozen. This is a prerequisite/data state, not a scientific null result.

---

## 3. Evidence codes

- `E-PT-Q`: direct coupled P--T quantitative precedent;
- `E-PT-C`: direct coupled P--T contextual/implicit precedent;
- `E-ADJ-Q`: adjacent quantitative transferable precedent;
- `E-STD`: recognized standard/framework;
- `E-CON`: conceptual support;
- `E-0`: no admissible support located in bounded audit.

---

## 4. Master admission matrix — frozen current state

| ID | Candidate quantity | Primary role | Evidence | M | Q | X | D | U | B | K | V | S | Current status | Main reason / open gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `R1` | electricity service / served load / critical-load service | `R-SVC` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | core Stage-5 resilience/service quantity; must not be relabeled as sustainability |
| `R2` | mobility service / unmet trips / travel performance | `R-SVC` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | core transport-service quantity |
| `R3` | aggregate service accessibility | `R-SVC` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | belongs to `K_svc`/resilience; distinct from distributional accessibility |
| `R4` | recovery time / restoration time | `R-SVC` | E-PT-Q, E-ADJ-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | resilience/reachability output, not sustainability by itself |
| `E1` | direct intervention/recovery cost | `RES` / economic consequence | E-PT-Q, E-ADJ-Q | P | P | P | C | P | C | P | C | P | **CONDITIONAL** | official 2018 cost-data routes exist, but intervention quantities, boundary and VVUQ are not frozen |
| `E2` | budget/capital ceiling | `FEAS` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | feasibility constraint, not outcome |
| `E3` | monetized outage/service-loss cost | potential `RES` | E-PT-Q | P | P | F | C | P | C | P | C | P | **OUT** | high duplication/preferences risk because physical service loss is already a primary resilience object; not required to answer H4/H5 |
| `RES1` | crew/person-hours | `RES` | E-PT-Q | P | P | P | C | P | C | P | C | P | **CONDITIONAL** | retain only if repair-resource interventions remain; Austin task-duration/staffing evidence not frozen |
| `RES2` | mobile emergency-resource quantity/capacity | `FEAS` default | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | control/feasibility variable; promote to `RES` only through a preregistered efficiency contrast |
| `RES3` | operational electricity/fuel energy used by intervention/recovery | `RES` | E-PT-Q | P | P | P | C | P | C | P | C | P | **CONDITIONAL** | electrical-energy route is strong; fuel-energy model remains unqualified; intervention boundary/case open |
| `SUS1` | GHG / carbon consequence (`kg` or `t CO2e`) | `SUS` | E-PT-Q, E-ADJ-Q, E-STD | P | P | P | C | P | C | P | C | P | **CONDITIONAL** | EPA eGRID2018 route exists; activity data, factor convention, boundary and VVUQ remain open |
| `SUS2` | distributional accessibility / equity consequence | `SUS` | E-PT-C, E-CON | P | P | P | C | C | C | P | C | C | **CONDITIONAL** | 2018 ACS route exists, but group/opportunity definition, overlap, metric validity and scope remain open |
| `SUS3` | material quantity used by persistent intervention | `RES` | E-ADJ-Q, E-STD | P | P | P | F | P | C | P | C | F | **OUT** | no frozen bill of materials and not justified within current confirmatory MSE core |
| `SUS4` | embodied/material GHG consequence | `SUS` | E-ADJ-Q, E-STD | P | P | P | F | P | C | P | C | F | **OUT** | depends on material inventory and adds lifecycle-accounting scope not currently justified |
| `T1` | renewable-generation capacity/share | `TRANS` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | intervention/technology descriptor; evaluate consequences separately |
| `T2` | storage capacity | `TRANS` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | transformation descriptor/feasibility variable |
| `T3` | charging-station addition/relocation/capacity | `TRANS` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | persistent P--T transformation candidate, not sustainability outcome |
| `T4` | line/road hardening or added redundancy | `TRANS` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | transformation candidate; consequences determine sustainability relevance |
| `LCA1` | full multi-category life-cycle assessment | `SUS` framework | E-ADJ-Q, E-STD | P | P | P | F | P | C | P | C | F | **OUT** | separate inventory/impact methodology beyond current core MSE scope |
| `ENV1` | water-use consequence | `SUS` | E-STD | C | C | P | F | P | F | C | F | F | **OUT** | no current direct P--T mechanism/data route in bounded thesis case |
| `ENV2` | biodiversity/ecosystem consequence | `SUS` | E-STD | C | C | P | F | C | F | C | F | F | **OUT** | outside current P--T model and requires separate ecological assessment |
| `ENV3` | local air-pollutant consequence (`NOx`, `PM`, etc.) | `CTX` | E-CON | C | C | P | F | P | F | C | F | C | **CONTEXT** | potentially relevant but no current emissions/dispersion or health-damage model |
| `SOC1` | public-health consequence | `SUS` | E-CON | C | C | P | F | C | F | C | F | F | **OUT** | requires exposure/health-response model beyond present scope |
| `SOC2` | broad social sustainability index | `SUS` | E-CON | F | C | F | F | F | F | F | F | F | **OUT** | construct not operationalized; generic score prohibited |
| `ECO1` | jobs/local economic development/macroeconomic benefit | economic/social | E-CON | C | C | P | F | C | F | C | F | F | **OUT** | requires a separate economic model |

---

## 5. Current scientific interpretation by family

### 5.1 Resilience/service family

`R1`--`R4` are central thesis outputs but **not sustainability dimensions**. They define what the system is trying to maintain/recover.

```math
\boxed{
\mathfrak R
\neq
\mathbf J_{sus}.
}
```

The H4/H5 analysis begins only after resilience outcomes are available.

### 5.2 Economic/resource family

The current core candidates are direct cost (`E1`) and operational energy (`RES3`). Crew-hours (`RES1`) remain conditional on the final intervention family. `E3` monetized service loss is excluded from the primary confirmatory vector to avoid duplicating physical service-loss outcomes and importing unneeded valuation assumptions.

The preferred representation is:

```math
\boxed{
\mathbf r(a)
\subseteq
\left(C_{direct},E_{op},H_{crew}\right),
}
```

where the subset is frozen only after metric-specific gates pass.

### 5.3 Environmental sustainability family

`SUS1` carbon/GHG has the strongest direct P--T sustainability precedent and an identified 2018 Austin-regional data route through EPA eGRID. It remains `CONDITIONAL` because direct precedent and source existence do not substitute for case admissibility, activity data, a declared attributional/consequential convention, accounting boundary and VVUQ.

`SUS4` embodied/material GHG is excluded from the current core. It may be reactivated only through a pre-result amendment if the final intervention set contains decision-material physical construction and a defensible bill-of-materials/factor route.

### 5.4 Social/distributional family

`SUS2` distributional accessibility/equity remains a conditional extension. The U.S. Census 2018 ACS provides a plausible demographic data route, but the construct must remain distinct from aggregate mobility service and requires group/population geography, an opportunity/service definition, spatial overlap, uncertainty and decision relevance.

Broad social-sustainability indices are excluded.

### 5.5 Transformation descriptors

`T1`--`T4` describe **what is changed**, not whether the change is sustainable.

For each candidate transformation:

```math
\boxed{
a_k
\rightarrow
\mathcal C(a_k)
}
```

must be evaluated before any sustainability label is assigned.

---

## 6. Frozen pre-H4/H5 consequence architecture

The typed architecture is:

```math
\boxed{
\mathcal C(a_k)
=
\left(
\Delta\mathfrak R^{a_k},
\mathbf r^{a_k},
\Delta\mathbf J_{sus}^{a_k},
\mathcal F^{a_k},
\mathbf U^{a_k}
\right).
}
```

The planned core resource vector is narrowed to:

```math
\boxed{
\mathbf r_{core}^{a_k}
\subseteq
\left(
C_{direct}^{a_k},
E_{op}^{a_k}
\right),
}
```

with `H_crew` as a conditional extension.

The planned core sustainability vector is narrowed to:

```math
\boxed{
\mathbf J_{sus,core}^{a_k}
\subseteq
\left(
CO_{2e}^{a_k}
\right),
}
```

with distributional accessibility/equity as a conditional extension.

The subset notation is mandatory because no conditional dimension is confirmatory `IN` yet.

Cost and energy may appear in the joint engineering decision even when they are not semantically typed as `SUS`; H5 does not require relabeling every decision criterion as sustainability.

---

## 7. Accounting choices — qualified but not confirmatory-frozen

### Cost

- report in a declared currency and price year;
- separate direct investment/recovery cost from monetized service loss;
- preferred vintage target is 2018 for the Austin 2018 case where credible 2018 sources exist;
- use present value only if a multi-year planning horizon is activated;
- freeze any discount/escalation method before confirmatory H4/H5.

### Energy

- primary feasible scope is operational electrical energy during the declared event/recovery horizon;
- retain physical energy units;
- distinguish electricity from fuel energy;
- include storage losses if material to the intervention comparison;
- do not assume operational energy represents lifecycle energy;
- fuel energy remains conditional on a qualified consumption model.

### Carbon/GHG

- primary candidate scope is operational/event or explicitly partial intervention carbon rather than full LCA;
- EPA eGRID2018 provides a regional ERCOT factor route but not an Austin Energy utility-specific factor;
- freeze average/attributional versus marginal/consequential interpretation before confirmatory execution;
- use `CO2e` with declared gas/GWP basis where relevant;
- distinguish calculated footprint from avoided/project-emission claims;
- full lifecycle terminology remains prohibited unless explicitly activated under the applicable ISO framework.

### Distributional accessibility

- keep aggregate network accessibility in Stage-5 service/resilience;
- use a separate group/geographic distributional metric only if population/zone data and decision relevance are established;
- the 2018 ACS is a candidate demographic source, not a frozen accessibility metric;
- do not infer equity from aggregate travel-time improvement.

---

## 8. Metric-card qualification — COMPLETED FOR CURRENT SCOPE

The required cards are now maintained in `SUSTAINABILITY_METRIC_CARDS_V1.md` for:

1. `E1` direct intervention/recovery cost;
2. `E3` monetized service-loss cost exclusion decision;
3. `RES1` crew/person-hours;
4. `RES2` mobile emergency-resource role;
5. `RES3` operational energy;
6. `SUS1` carbon/GHG;
7. `SUS2` distributional accessibility/equity;
8. `SUS3` material quantity exclusion/activation rule;
9. `SUS4` embodied carbon exclusion/activation rule.

The case/data feasibility audit is `SUSTAINABILITY_CASE_DATA_FEASIBILITY_AUDIT_V1.md` and the current freeze decision is `SUSTAINABILITY_ADMISSION_FREEZE_V1.md`.

---

## 9. H4 register requirements

Before H4 confirmatory execution, this register must additionally identify:

- an admissible final case;
- final intervention set `\mathcal A`;
- role of every active metric;
- final admitted `\mathbf r` and `\mathbf J_{sus}`;
- baseline `a_ref`;
- accounting boundary for each component;
- common scenario ensemble;
- practical/materiality criterion;
- uncertainty propagation;
- non-support/falsification rule.

If a candidate dimension fails a prerequisite after the freeze process, its experiment state becomes `NOT TESTED`; it is not assigned a zero consequence.

---

## 10. H5 register requirements

H5 must use the same candidate actions and scenario ensemble for both decision formulations.

Baseline:

```math
\boxed{
\mathcal A_R^{\star}
}
```

Joint evaluation:

```math
\boxed{
\mathcal A_{R,S}^{\star}
}
```

The default decision representation is vector-valued/nondominated. Any weighted scalarization requires a separate weight/utility justification and sensitivity analysis.

The register must document whether the joint decision differs because of:

- resource use;
- direct cost;
- carbon/GHG;
- distributional accessibility if admitted;
- feasibility;
- uncertainty/regret.

This preserves interpretability of *why* the decision changes.

---

## 11. Chapter synchronization

The register must be consulted and synchronized when drafting or revising:

- Section 1.5 Sustainable Engineering Significance;
- Section 1.6 Scope, Boundaries and Assumptions;
- Chapter 2.21 resilience--sustainability literature synthesis;
- Chapter 3 Stage 6 consequence definitions;
- Chapter 3 Stage 7 decision definitions;
- Chapter 4 H4/H5 experiments;
- Chapter 5 H4/H5 results tables;
- Chapter 6 trade-off/burden-shifting discussion;
- Chapter 7 RQ6/RQ7 conclusions.

A thesis chapter must not introduce a new sustainability dimension without first registering and qualifying it here.

---

## 12. Current next gate

Metric qualification, case/data feasibility analysis and the current `IN / CONDITIONAL / OUT` freeze are complete.

The next admissibility sequence is now:

```math
\boxed{
G_{AUS}=PASS
\rightarrow
\mathcal A,a_{ref}\text{ frozen}
\rightarrow
\text{metric-specific data materialization/QC}
\rightarrow
\text{boundary + VVUQ freeze}
\rightarrow
\text{pre-result promotion audit}
\rightarrow
\text{CONDITIONAL}\to\text{IN where justified}.
}
```

No H4/H5 confirmatory execution is authorized before that sequence closes. Section 1.5 may now be written from the evidence and scope significance; Section 1.6 must state the current quantitative boundary and the conditional nature of metrics not yet promoted to `IN`.