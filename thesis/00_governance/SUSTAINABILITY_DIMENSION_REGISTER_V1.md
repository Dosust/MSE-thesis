# Sustainability-Dimension Register — v1.0

**Status:** LIVE PRE-ADMISSION REGISTER / NOT YET H4-H5 FROZEN  
**Effective date:** 2026-09-18  
**Governing standard:** `SUSTAINABILITY_DIMENSION_ADMISSION_AND_ACCOUNTING_STANDARD_V1.md`  
**Scientific authority:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Evidence basis:** formal Section-1.5 evidence audit + audited P--T corpus + verified standards/close precedents  
**Change rule:** update only with a dated evidence/data/boundary rationale; after H4/H5 freeze use a formal amendment.

---

## 1. Purpose

This register is the live control table for every quantity proposed as a resilience, resource-efficiency, feasibility, sustainability or transformation variable in Stages 6--7.

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

- `IN` = confirmatory-ready only after all gates pass;
- `CONDITIONAL` = scientifically defensible candidate but one or more execution gates remain open;
- `ROLE-ONLY` = required thesis variable but not part of `\mathbf J_{sus}`;
- `OUT` = excluded from core quantitative thesis scope;
- `CONTEXT` = discussion/limitation relevance only.

No current `CONDITIONAL` dimension becomes confirmatory simply by appearing in this register.

---

## 3. Evidence codes

- `E-PT-Q`: direct coupled P--T quantitative precedent;
- `E-PT-C`: direct coupled P--T contextual/implicit precedent;
- `E-ADJ-Q`: adjacent quantitative transferable precedent;
- `E-STD`: recognized standard/framework;
- `E-CON`: conceptual support;
- `E-0`: no admissible support located in bounded audit.

---

## 4. Master admission matrix — current state

| ID | Candidate quantity | Primary role | Evidence | M | Q | X | D | U | B | K | V | S | Current status | Main reason / open gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `R1` | electricity service / served load / critical-load service | `R-SVC` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | core Stage-5 resilience/service quantity; must not be relabeled as sustainability |
| `R2` | mobility service / unmet trips / travel performance | `R-SVC` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | core transport-service quantity |
| `R3` | aggregate service accessibility | `R-SVC` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | belongs to `K_svc`/resilience unless a distinct distributional construct is defined |
| `R4` | recovery time / restoration time | `R-SVC` | E-PT-Q, E-ADJ-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | resilience/reachability output, not sustainability by itself |
| `E1` | direct intervention/recovery cost | `RES` / economic consequence | E-PT-Q, E-ADJ-Q | P | P | P | C | P | C | P | C | P | **CONDITIONAL** | currency year, included cost components, data source and uncertainty not yet frozen |
| `E2` | budget/capital ceiling | `FEAS` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | feasibility constraint, not outcome |
| `E3` | monetized outage/service-loss cost | `RES` / economic consequence | E-PT-Q | P | P | C | C | P | C | P | C | P | **CONDITIONAL** | high double-counting risk with resilience/service loss and direct cost; valuation method not frozen |
| `RES1` | crew/person-hours | `RES` | E-PT-Q | P | P | P | C | P | C | P | C | P | **CONDITIONAL** | intervention set/resource model must determine relevance and data |
| `RES2` | mobile emergency-resource quantity/capacity | `FEAS` or `RES` | E-PT-Q | P | P | P | C | P | C | P | C | P | **CONDITIONAL** | primary role must be frozen per H4 experiment; candidate intervention set not frozen |
| `RES3` | operational electricity/fuel energy used by intervention/recovery | `RES` | E-PT-Q | P | P | P | C | P | C | P | C | P | **CONDITIONAL** | energy boundary and comparable activity data across interventions not yet frozen |
| `SUS1` | GHG / carbon consequence (`kg` or `t CO2e`) | `SUS` | E-PT-Q, E-ADJ-Q, E-STD | P | P | P | C | P | C | P | C | P | **CONDITIONAL** | emission factors, partial/lifecycle boundary, geography/year and uncertainty not yet frozen |
| `SUS2` | distributional accessibility / equity consequence | `SUS` | E-PT-C, E-CON | P | P | P | C | C | C | P | C | C | **CONDITIONAL** | requires population/group definition, spatial data, metric validity and scope decision; must remain distinct from aggregate service accessibility |
| `SUS3` | material quantity used by persistent intervention | `RES` | E-ADJ-Q, E-STD | P | P | P | C | P | C | P | C | C | **CONDITIONAL** | bill-of-materials/quantity data and intervention scope not yet available |
| `SUS4` | embodied/material GHG consequence | `SUS` | E-ADJ-Q, E-STD | P | P | P | C | P | C | P | C | C | **CONDITIONAL** | depends on `SUS3`, factor/source choice and partial/lifecycle carbon boundary |
| `T1` | renewable-generation capacity/share | `TRANS` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | intervention/technology descriptor; evaluate consequences separately |
| `T2` | storage capacity | `TRANS` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | transformation descriptor/feasibility variable |
| `T3` | charging-station addition/relocation/capacity | `TRANS` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | persistent P--T transformation candidate, not sustainability outcome |
| `T4` | line/road hardening or added redundancy | `TRANS` | E-PT-Q | — | — | — | — | — | — | — | — | — | **ROLE-ONLY** | transformation candidate; consequences determine sustainability relevance |
| `LCA1` | full multi-category life-cycle assessment | `SUS` framework | E-ADJ-Q, E-STD | P | P | P | F | P | C | P | C | F | **OUT** | would require inventory/impact methodology beyond current core MSE scope; may be activated only by formal scope amendment |
| `ENV1` | water-use consequence | `SUS` | E-STD | C | C | P | F | P | F | C | F | F | **OUT** | no current direct P--T mechanism/data route in bounded thesis case |
| `ENV2` | biodiversity/ecosystem consequence | `SUS` | E-STD | C | C | P | F | C | F | C | F | F | **OUT** | outside current P--T model and would require separate ecological assessment |
| `ENV3` | local air-pollutant consequence (`NOx`, `PM`, etc.) | `SUS` | E-CON | C | C | P | F | P | F | C | F | C | **CONTEXT** | potentially relevant but no current emissions/dispersion or health-damage model |
| `SOC1` | public-health consequence | `SUS` | E-CON | C | C | P | F | C | F | C | F | F | **OUT** | requires exposure/health-response model beyond present scope |
| `SOC2` | broad social sustainability index | `SUS` | E-CON | F | C | F | F | F | F | F | F | F | **OUT** | construct not operationalized; prohibited as generic score |
| `ECO1` | jobs/local economic development/macroeconomic benefit | `SUS`/economic | E-CON | C | C | P | F | C | F | C | F | F | **OUT** | requires economic model outside current engineering scope |

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

`E1`, `E3`, `RES1`--`RES3` are potentially critical because interventions with comparable resilience may consume different amounts of money, energy, time, labor or mobile capacity.

The preferred representation is not to call all of these sustainability. Instead:

```math
\boxed{
\mathbf r(a)
=
(r_C,r_E,r_L,r_M,\ldots)
}
```

with only the relevant admitted components activated.

### 5.3 Environmental sustainability family

`SUS1` carbon/GHG currently has the strongest direct P--T sustainability precedent. It remains `CONDITIONAL` because direct precedent does not substitute for a declared accounting boundary and case-specific emission-factor/data validation.

`SUS4` embodied/material GHG is scientifically defensible but currently weaker for the direct P--T case and requires material inventory data.

### 5.4 Social/distributional family

`SUS2` distributional accessibility/equity is retained as a serious candidate rather than silently included. It must satisfy a distinct construct from aggregate mobility service and requires group/population geography, an accessibility/equity metric and validation.

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

## 6. Preliminary Stage-6 consequence structure

No dimension is yet finally frozen, but the current admissible architecture is:

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
\right)
}
```

with the **candidate** resource vector

```math
\mathbf r^{a_k}
\subseteq
\left(
C_{direct},
E_{op},
H_{crew},
R_{mobile},
M_{material}
\right),
```

and the **candidate** sustainability vector

```math
\mathbf J_{sus}^{a_k}
\subseteq
\left(
CO_{2e},
A_{dist},
CO_{2e}^{emb}
\right).
```

The subset notation is deliberate: the final vector is not frozen until all gates for each component pass.

Cost and energy may still appear in the overall engineering decision vector even when they are not typed as `SUS`; H5 is a joint engineering decision, not a requirement to relabel every decision criterion as sustainability.

---

## 7. Current default accounting choices — not yet frozen

These are **working defaults**, not confirmatory specifications.

### Cost

- report in a declared currency and price year;
- separate direct investment/recovery cost from monetized service loss;
- use present value only if a multi-year planning horizon is activated;
- freeze discount rate before confirmatory H4/H5.

### Energy

- retain physical energy units;
- distinguish electricity from fuel energy;
- include storage losses if material to the intervention comparison;
- do not assume operational energy represents lifecycle energy.

### Carbon/GHG

- first candidate scope: operational/event or explicitly partial intervention carbon rather than full LCA;
- use `CO2e` with declared gases/GWP basis where relevant;
- freeze emission-factor source, geography and year;
- distinguish observed/calculated emissions from avoided-emissions/project claims;
- if lifecycle/partial carbon footprint is activated, follow the applicable ISO framework and record exact standard version.

### Distributional accessibility

- keep aggregate network accessibility in Stage-5 service/resilience;
- use a separate group/geographic distributional metric only if population/zone data and decision relevance are established;
- do not infer equity from aggregate travel-time improvement.

---

## 8. Metric-card activation queue

Before final H4/H5 freeze, create complete metric cards in this order:

1. `E1` direct intervention/recovery cost;
2. `RES3` operational energy;
3. `SUS1` carbon/GHG;
4. `RES1` crew/person-hours if repair-resource interventions remain in the candidate set;
5. `RES2` mobile emergency-resource quantity/capacity if used as efficiency rather than only feasibility;
6. `SUS2` distributional accessibility/equity only after a data-feasibility audit;
7. `SUS3/SUS4` material quantity/embodied carbon only if persistent physical interventions require meaningful material accounting.

The queue is based on current direct evidence and likely decision relevance, not on a claim that lower-ranked dimensions are unimportant.

---

## 9. H4 register requirements

Before H4 confirmatory execution, this register must identify:

- final intervention set `\mathcal A`;
- role of every metric;
- final admitted `\mathbf r` and `\mathbf J_{sus}`;
- baseline `a_ref`;
- accounting boundary for each component;
- common scenario ensemble;
- practical/materiality criterion;
- uncertainty propagation;
- non-support/falsification rule.

If a candidate dimension fails a prerequisite after the freeze process, its status becomes `NOT TESTED`; it is not assigned a zero consequence.

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

A thesis chapter must not introduce a new sustainability dimension without first registering it here.

---

## 12. Current next gate

The matrix structure is now established. The next required work is **metric-card qualification**, beginning with `E1`, `RES3`, and `SUS1`, followed by the case/intervention data-feasibility audit.

Only after these checks should the register be converted from pre-admission to a final `IN / CONDITIONAL / OUT` freeze for Section 1.6 and H4/H5 preregistration.