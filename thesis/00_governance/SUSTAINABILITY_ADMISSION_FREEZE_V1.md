# Sustainability-Dimension Admission Freeze — v1.0

**Status:** FROZEN PRE-H4/H5 SCOPE AND ADMISSION STATE  
**Freeze date:** 2026-09-18  
**Governing standard:** `SUSTAINABILITY_DIMENSION_ADMISSION_AND_ACCOUNTING_STANDARD_V1.md`  
**Metric qualification:** `SUSTAINABILITY_METRIC_CARDS_V1.md`  
**Case/data audit:** `SUSTAINABILITY_CASE_DATA_FEASIBILITY_AUDIT_V1.md`  
**Provenance register:** `SUSTAINABILITY_DIMENSION_REGISTER_V1.md`  
**Case:** `AUS-P5U-2018-V1` — candidate only, not yet admissible  
**RQ/H scope:** RQ6/SO6/H4 and RQ7/SO7/H5

---

## 1. Purpose and meaning of this freeze

This artifact closes the sequence

```math
\boxed{
\text{metric-card qualification}
\rightarrow
\text{case/data feasibility}
\rightarrow
\text{IN / CONDITIONAL / OUT freeze}.
}
```

The freeze prevents outcome-driven metric selection. It records the state **before** H4/H5 execution. It does not state that every retained dimension is already computable.

Two different decisions are recorded:

1. **thesis-scope status** — whether the object belongs in the planned Stage-6/7 analysis at all;
2. **confirmatory-admission status** — whether it has passed all nine gates and may enter confirmatory H4/H5 now.

These statuses must not be conflated.

```math
\boxed{
\text{IN-SCOPE}
\not\Rightarrow
\text{confirmatory IN}.
}
```

The governing admission definition remains non-compensatory: confirmatory `IN` requires all applicable `M,Q,X,D,U,B,K,V,S` gates to pass.

---

## 2. Common upstream blocker

The Austin case authority currently states:

```text
AUS-P5U-2018-V1 = CANDIDATE CASE ONLY — NOT YET ADMISSIBLE
```

with `G1–G8` not all passed. The final intervention set `A` and reference intervention `a_ref` are also not frozen.

Therefore:

```math
\boxed{
\text{Confirmatory IN set at this freeze}=\varnothing.
}
```

This is the scientifically correct current state. It is not evidence that the retained dimensions have zero value or that H4/H5 are unsupported; H4/H5 are **NOT YET AUTHORIZED**.

---

## 3. Final current status matrix

| ID | Quantity | Primary role | Thesis-scope status | Confirmatory status | Freeze decision / reason |
|---|---|---|---|---|---|
| `R1` | electricity service / served critical load | `R-SVC` | **IN-SCOPE** | **ROLE-ONLY** | core resilience/service object; not sustainability |
| `R2` | mobility service / unmet trips / travel performance | `R-SVC` | **IN-SCOPE** | **ROLE-ONLY** | core transport-service object |
| `R3` | aggregate accessibility | `R-SVC` | **IN-SCOPE** | **ROLE-ONLY** | Stage-5 service quantity; cannot be duplicated as sustainability |
| `R4` | recovery/restoration time | `R-SVC` | **IN-SCOPE** | **ROLE-ONLY** | viability/reachability/resilience output |
| `E1` | direct intervention/recovery cost | `RES` | **IN-SCOPE** | **CONDITIONAL** | strong direct evidence and official cost-data routes; intervention quantities/boundary/VVUQ open |
| `E2` | budget/capital ceiling | `FEAS` | **IN-SCOPE** | **ROLE-ONLY** | feasibility constraint, not outcome |
| `E3` | monetized outage/service-loss cost | potential `RES` | **OUT-SCOPE primary** | **OUT** | duplicates core service-loss information and requires additional valuation assumptions; optional sensitivity only by amendment |
| `RES1` | crew/person-hours | `RES` | **CONDITIONAL-SCOPE** | **CONDITIONAL** | retain only if repair-resource interventions remain; Austin task-duration/staffing evidence not frozen |
| `RES2` | mobile emergency-resource count/capacity | `FEAS` default | **IN-SCOPE if intervention uses it** | **ROLE-ONLY** | control/feasibility descriptor; promote to `RES` only by preregistered efficiency test |
| `RES3` | operational electrical energy | `RES` | **IN-SCOPE** | **CONDITIONAL** | direct model calculation route exists; case/intervention/boundary/VVUQ open |
| `RES3-F` | fuel energy | `RES` | **CONDITIONAL-SCOPE** | **CONDITIONAL** | no qualified case fuel-consumption model yet; exclude unless activated pre-result |
| `SUS1` | operational/partial carbon/GHG | `SUS` | **IN-SCOPE** | **CONDITIONAL** | strongest direct environmental precedent; eGRID2018 route exists; activity/factor convention/boundary open |
| `SUS2` | distributional accessibility/equity | `SUS` | **CONDITIONAL-SCOPE** | **CONDITIONAL** | 2018 ACS route exists but construct, groups, opportunity set, overlap and scope remain open |
| `SUS3` | material quantity | `RES` | **OUT-SCOPE core** | **OUT** | no frozen bill of materials; reactivate only if final structural interventions make it decision-material |
| `SUS4` | embodied/material GHG | `SUS` | **OUT-SCOPE core** | **OUT** | depends on material inventory and adds lifecycle-accounting scope not currently justified |
| `T1` | renewable-generation capacity/share | `TRANS` | **IN-SCOPE as candidate transformation** | **ROLE-ONLY** | describes what is changed, not sustainability by itself |
| `T2` | storage capacity | `TRANS` | **IN-SCOPE as candidate transformation** | **ROLE-ONLY** | transformation descriptor |
| `T3` | charger addition/relocation/capacity | `TRANS` | **IN-SCOPE as candidate transformation** | **ROLE-ONLY** | transformation descriptor |
| `T4` | line/road hardening or redundancy | `TRANS` | **IN-SCOPE as candidate transformation** | **ROLE-ONLY** | transformation descriptor |
| `LCA1` | full multi-category life-cycle assessment | `SUS` framework | **OUT-SCOPE** | **OUT** | separate inventory/impact-analysis program; not needed for current RQ6/RQ7 |
| `ENV1` | water-use consequence | `SUS` | **OUT-SCOPE** | **OUT** | no current P--T mechanism/data route in bounded case |
| `ENV2` | biodiversity/ecosystem consequence | `SUS` | **OUT-SCOPE** | **OUT** | would require separate ecological assessment |
| `ENV3` | local air pollutants | `CTX` | **CONTEXT ONLY** | **CONTEXT** | potentially relevant but no current emissions/dispersion consequence model |
| `SOC1` | public-health consequence | `SUS` | **OUT-SCOPE** | **OUT** | exposure/health-response model outside MSE core |
| `SOC2` | broad social-sustainability index | `SUS` | **OUT-SCOPE** | **OUT** | construct not operationalized; generic index prohibited |
| `ECO1` | jobs/local macroeconomic development | economic/social | **OUT-SCOPE** | **OUT** | requires separate economic model |

---

## 4. Frozen Stage-6/7 architecture after qualification

The consequence object remains

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

The **planned core resource vector** is now narrowed to

```math
\boxed{
\mathbf r^{a_k}_{core}
\subseteq
\left(
C_{direct}^{a_k},
E_{op}^{a_k}
\right),
}
```

with crew-hours activated only when the final intervention family requires repair labor:

```math
H_{crew}^{a_k}\quad\text{conditional extension}.
```

The **planned core sustainability vector** is narrowed to

```math
\boxed{
\mathbf J_{\rm sus,core}^{a_k}
\subseteq
\left(
CO_{2e}^{a_k}
\right),
}
```

with distributional accessibility/equity retained as a conditional extension:

```math
A_{dist}^{a_k}\quad\text{conditional extension}.
```

The subset notation is mandatory until metric-specific gates pass.

This means the thesis will **not** attempt to manufacture a large sustainability vector merely to appear comprehensive. A small, auditable vector is scientifically preferable to a broad but weakly supported one.

---

## 5. H4 implication

H4 remains:

```math
\boxed{
a_k
\rightarrow
\left(
\Delta\mathfrak R^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k}
\right),
}
```

with resource-efficiency quantities reported separately through `r(a_k)`.

At current freeze, the intended comparison is therefore conceptually:

```math
\boxed{
\left(
\Delta\mathfrak R^{a_k},
\Delta C_{direct}^{a_k},
\Delta E_{op}^{a_k},
\Delta CO_{2e}^{a_k}
\right)
}
```

plus `H_crew` and/or `A_dist` only if their conditional gates pass **before** confirmatory outcomes are inspected.

No materiality threshold `delta_4` is selected by this freeze.

---

## 6. H5 implication

The baseline decision remains

```math
\mathcal A_R^{\star},
```

and the joint engineering decision remains

```math
\mathcal A_{R,S}^{\star}.
```

The H5 decision vector may include admitted resource criteria even when they are not semantically labeled `SUS`. Therefore H5 is interpreted as a joint **resilience + resource efficiency + declared sustainability + feasibility + uncertainty** decision, consistent with RQ7/SO7.

The default decision method remains vector-valued/nondominated. No weighted composite sustainability score is frozen.

---

## 7. Mandatory promotion gate

No `CONDITIONAL` dimension can become `IN` unless all of the following occur before confirmatory H4/H5 outcomes:

```math
\boxed{
G_{AUS}=PASS
\land
\mathcal A\text{ frozen}
\land
a_{ref}\text{ frozen}
\land
D_j=PASS
\land
B_j=PASS
\land
V_j=PASS
\land
\text{all other applicable gates}=PASS.
}
```

The promotion decision must be recorded by a dated amendment or a versioned `SUSTAINABILITY_ADMISSION_FREEZE_V2.md`.

If a data source fails after preregistration, the metric becomes `NOT TESTED` for that experiment; it is not assigned zero effect and H4/H5 are not automatically falsified.

---

## 8. Change-control rule

After this freeze:

- adding a new primary sustainability/resource dimension;
- reactivating `E3`, `SUS3`, `SUS4`, `LCA1`, `ENV1`, `ENV2`, `SOC1`, `SOC2` or `ECO1`;
- changing the carbon accounting convention;
- changing a metric from role-only to primary response;
- changing the accessibility/equity construct;
- changing cost/energy boundaries;

requires a dated pre-result amendment stating rationale, evidence, case/data feasibility, affected hypotheses and whether any relevant outcomes had already been observed.

No post-result amendment may be presented as preregistered confirmatory design.

---

## 9. Thesis writing consequences

Section 1.5 may now state that the thesis evaluates resilience together with **resource/economic and environmental consequences**, but must not imply that every sustainability dimension is measured. It may identify direct cost, operational energy and carbon/GHG as the planned core consequence families, while distributional accessibility remains conditional.

Section 1.6 must state explicitly that full LCA, water, biodiversity, public-health, broad social-sustainability and macroeconomic modeling are outside the current quantitative thesis boundary.

Chapter 2 must preserve direct P--T evidence versus adjacent method-transfer evidence.

Chapters 3–4 must not replace the conditional status with numerical formulas/parameters until case/data gates pass.

Chapters 5–7 may report and interpret only metrics that were promoted to `IN` before confirmatory execution; `NOT TESTED` dimensions remain visible as limitations.

---

## 10. Freeze conclusion

```math
\boxed{
\begin{aligned}
\text{Core planned consequence families:}
&\quad C_{direct},\ E_{op},\ CO_{2e};\\
\text{Conditional extensions:}
&\quad H_{crew},\ A_{dist},\ \text{fuel energy};\\
\text{Excluded from core:}
&\quad \text{monetized service loss, materials/embodied GHG, full LCA,}\\
&\quad \text{water, biodiversity, public health, broad social index, macroeconomics}. 
\end{aligned}
}
```

At this freeze, `IN_confirmatory = empty set` because upstream Austin case and intervention/data gates remain open. This is the final scientifically valid status **at the present pre-H4/H5 stage**.
