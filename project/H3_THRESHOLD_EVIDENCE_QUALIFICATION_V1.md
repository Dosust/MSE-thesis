# H3 Threshold Evidence Qualification v1.0

**Status:** ACTIVE EVIDENCE QUALIFICATION  
**Date:** 2026-09-16  
**Protocol:** EGMIV–TSP  
**Thesis destination:** Chapter 3 → Stage 5 → RQ3/H3 → Chapter 4 H3 experiment  
**Structural authority:** `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Page-control authority:** `../thesis/00_governance/THESIS_PAGE_BUDGET_160_V1.md`

> This file qualifies numerical/provenance evidence for the open H3 state-set registry. It does not change the frozen semantics of `K(t)`, `G_rec(t)`, `F(t)`, `T_V`, or `T_R`.

---

## 1. Qualification order

```math
\boxed{
s_P^{\min}
\rightarrow
s_T^{\min}
\rightarrow
s_{P,\rm rec}
\rightarrow
s_{T,\rm rec}
\rightarrow
F
\rightarrow
T_V
\rightarrow
T_R.
}
```

Current completed object in this version: `s_P^{min}`.

---

# 2. Object Q1 — `s_P^{min}`

## 2.1 Thesis role

The frozen H3 service map is

```math
0\le S_P(Y,t)\le1,
```

with observed/validated realization based on weighted served electrical energy relative to counterfactual requested energy. The H3 service-admissibility condition permits

```math
S_P(Y,t)\ge s_P^{\min}(t).
```

The qualification question is therefore:

> What evidence can define the minimum acceptable electrical service level without inventing a universal resilience threshold?

---

## 2.2 Targeted evidence search question

```text
For a power-system resilience application, what authoritative engineering evidence defines
minimum electricity service during disruption, and does that evidence justify a universal
numerical service fraction or require a case-/mission-specific critical-load requirement?
```

Search was intentionally limited to authoritative U.S. Department of Energy / national-laboratory sources directly addressing critical load, resilience metrics, and emergency energy requirements. Broad exploratory literature collection was excluded under EGMIV–TSP.

---

## 2.3 Qualified evidence

### E1 — DOE/FEMP energy-security guidance

The U.S. Department of Energy Federal Energy Management Program requires critical facilities to be identified from the site's mission/function and directs facility managers to estimate the energy level required to support critical loads. Its energy-security plan template specifically asks for the **quantified minimum amount of energy required to meet critical loads in an emergency**, with electricity expressed in kW where appropriate (U.S. Department of Energy, Federal Energy Management Program [FEMP], 2006).

**Evidence use:** supports a mission-/facility-specific minimum-energy requirement as the correct engineering source object for `s_P^{min}`. It does **not** supply a universal fraction.

### E2 — DOE/PNNL Technical Resilience Navigator practice

The Technical Resilience Navigator pilot at Pacific Northwest National Laboratory determined critical-load energy requirements using mission/site-owner interviews, audits, metered data, modeled loads, nameplate information, and engineering verification. The resource explicitly notes that critical-load requirements may be directly provided by mission owners or approximated and then checked against real data (Pacific Northwest National Laboratory [PNNL], 2021).

**Evidence use:** supports case-specific identification plus verification/validation of the minimum critical-load requirement and supports retaining uncertainty where only ranges or reconstructed values exist.

### E3 — NREL resilience-metric guidance

Anderson, Hotchkiss, and Murphy state that no single resilience definition or metric applies broadly; the appropriate metric depends on goals, event context, hazards, scale, and perspective. Their performance-based examples include load not served, critical services without power, and time to recovery (Anderson et al., 2019).

**Evidence use:** rejects a universal numerical `s_P^{min}` chosen independently of case, service class, hazard, and decision context.

### E4 — REopt critical-load semantics

NREL's REopt resilience workflow defines critical load as the load that must be met during the specified grid outage. The tool allows users to define the critical load as a percentage or upload a profile and uses example percentages such as 50%, 75%, and 100% for sensitivity exploration; those percentages are user inputs/examples, not engineering standards (National Renewable Energy Laboratory [NREL], n.d.).

**Evidence use:** supports representing a critical-load requirement as a site-specific fraction/profile while explicitly rejecting REopt example percentages as normative threshold values.

---

## 2.4 Source-qualification gate

For source `q`, apply

```math
G_S^{(q)}
=
G_I\land G_R\land G_C\land G_Q\land G_M\land G_V.
```

| Source | Identity | Direct relevance | Supports claimed proposition | Authority/quality | Metadata | Validity-domain treatment | Admission |
|---|---|---|---|---|---|---|---|
| DOE/FEMP (2006) | PASS | PASS | PASS | PASS — official DOE/FEMP guidance | PASS | Federal-facility context; admitted for threshold *principle*, not a universal value | **ADMIT** |
| PNNL (2021) TRN | PASS | PASS | PASS | PASS — DOE national-laboratory resilience practice | PASS | Site/campus critical loads; admitted for case-specific identification and verification | **ADMIT** |
| Anderson et al. (2019) | PASS | PASS | PASS | PASS — NREL technical fact sheet | PASS | General energy-resilience metric selection; context dependence explicit | **ADMIT** |
| NREL REopt tutorial | PASS | PASS | PASS with limitation | PASS — national-laboratory tool documentation | PASS | Percent examples are illustrative, not requirements | **ADMIT FOR SEMANTICS ONLY** |

No source found in this targeted qualification supplies a defensible universal percentage such as 50%, 75%, 80%, 90%, 95%, or 100% of *total ordinary demand* as the general minimum acceptable power-service threshold for this thesis.

---

## 2.5 Mathematical translation into the frozen H1/H3 service metric

For validation interval `I_m`, the frozen power-service metric is

```math
S_{P,m}
=
\frac{\sum_i\omega_i E_{i,m}^{srv}}
{\sum_i\omega_i\widehat E_{i,m}^{d}}.
```

Let

```math
E_{i,m}^{req}
```

be the documented minimum electrical energy required during `I_m` to sustain the selected critical function(s), obtained from the case authority and qualified under the evidence procedure above.

When the engineering requirement is expressible in the same aggregation and weighting convention as `S_P`, define the candidate threshold

```math
\boxed{
s_{P,m}^{\min}
=
\frac{\sum_i\omega_i E_{i,m}^{req}}
{\sum_i\omega_i\widehat E_{i,m}^{d}}.
}
```

with

```math
0\le E_{i,m}^{req}\le \widehat E_{i,m}^{d}
```

for each included service entity under the chosen convention.

Then

```math
S_{P,m}\ge s_{P,m}^{\min}
```

has an engineering interpretation tied to a documented minimum critical-service requirement rather than an arbitrary resilience percentage.

### Non-substitutability guard

Aggregate service alone can hide failure of an individually indispensable critical load. Therefore, when a critical entity/function is non-substitutable, add the native requirement

```math
\boxed{
E_{i,m}^{srv}\ge E_{i,m}^{req},
\qquad i\in\mathcal C_{hard},
}
```

inside `K_svc`; do not allow excess service to noncritical loads to compensate for loss of a mandatory critical function.

This is consistent with the frozen H3 rule that `K_svc` may contain more specific critical-load requirements in addition to the scalar service-fraction constraint.

---

## 2.6 What must not be used as `s_P^{min}`

The following are rejected as direct substitutes for the service threshold unless a validated transformation to the frozen service metric is established:

1. voltage limits;
2. frequency limits;
3. SAIDI/SAIFI or other reliability indices;
4. value of lost load;
5. total outage duration;
6. arbitrary REopt example percentages;
7. a percentage selected because it is common in a published simulation.

Voltage/frequency and other physical operating limits belong in `K_phys`; outage duration or restoration deadlines belong in the relevant temporal/recovery objects; materially different metrics remain separate compliance criteria unless a validated mapping exists.

---

## 2.7 Units, scales, aggregation, and uncertainty

| Field | Qualified specification |
|---|---|
| Mathematical object | `s_P^{min}(t)` or interval form `s_{P,m}^{min}` |
| Physical meaning | minimum acceptable electrical-service fraction implied by documented critical-function energy requirements |
| Native requirement units | kW, kWh, or time-indexed load profile, depending on authority/source |
| Thesis threshold units | dimensionless fraction `[0,1]` after validated normalization to the frozen `S_P` metric |
| Spatial scale | critical load/facility/entity first; system aggregation only after deterministic mapping and weighting |
| Temporal scale | native requirement window; converted to the common validation/decision interval without false upsampling |
| Aggregation | interval energy preferred when field data are interval energy; instantaneous kW only if the requirement and model use instantaneous power consistently |
| Uncertainty | mission-owner range, meter/model error, demand-baseline error, temporal aggregation, and classification uncertainty must be retained and propagated |
| Validity domain | the selected case, critical-service class, hazard/operating regime, spatial support, and declared time window |

No probability distribution for `s_P^{min}` is frozen at this stage. If requirement uncertainty is represented probabilistically later, its distribution must be justified from case evidence rather than assumed for computational convenience.

---

## 2.8 EGMIV epistemic status

```text
[E] Minimum emergency energy for critical loads should be defined from the site's critical functions/mission and quantified in native engineering units.
[E] Critical-load requirements can require multiple site-specific data sources and engineering verification.
[E] Resilience metric/target choice is context dependent; no universal resilience service fraction is established by the qualified sources.
[D] Mapping a documented minimum critical-energy requirement into the frozen normalized S_P metric yields the ratio formulation above when numerator/denominator supports are consistent.
[A] The final case-specific E_req profile/value remains unspecified until the case authority/data source is selected.
[U] The numerical value of s_P^{min} remains open.
```

---

## 2.9 Qualification decision

```math
\boxed{
\begin{aligned}
\text{definition/provenance of }s_P^{\min} &: \textbf{SUPPORTED},\\
\text{universal numerical value} &: \textbf{REJECTED},\\
\text{case-specific numerical value} &: \textbf{OPEN},\\
\text{confirmatory-code admission} &: \textbf{BLOCKED UNTIL CASE EVIDENCE IS FROZEN}.
\end{aligned}
}
```

The correct scientific result is therefore **not** a guessed percentage. The defensible result is a provenance-constrained rule for deriving `s_P^{min}` from a documented critical-load requirement in the selected case.

---

## 2.10 R1–R8 service-requirement gate status for `s_P^{min}`

The upstream service-requirement architecture requires authority, native quantity, context, target, tolerance where needed, temporal/spatial compatibility, provenance, and pre-confirmatory freeze. At this point:

```text
Authority class identified:                 PASS in principle; final case authority OPEN
Native quantity identified:                 PASS (critical kW/kWh/profile → normalized S_P)
Context requirement identified:             PASS; final case context OPEN
Target semantics identified:                PASS
Tolerance/materiality band:                 OPEN / not required merely to define K_svc
Temporal mapping rule:                      PASS; numerical interval OPEN
Spatial mapping rule:                       PASS; final entities OPEN
Provenance requirement:                     PASS
Pre-confirmatory numerical freeze:          NOT PASSED
```

Therefore `s_P^{min}` is structurally qualified but not numerically frozen.

---

# 3. Next admissible object

```math
\boxed{s_T^{\min}}
```

The next targeted search must identify authoritative transportation/emergency-mobility service requirements that can be mapped to the frozen completed/requested weighted OD-trip service metric without converting unrelated transportation performance measures into an unsupported service fraction.

---

# References — APA 7

Anderson, K., Hotchkiss, E., & Murphy, C. (2019). *Valuing resilience in electricity systems* (NREL/FS-7A40-74673). National Renewable Energy Laboratory. https://www.nrel.gov/docs/fy19osti/74673.pdf

National Renewable Energy Laboratory. (n.d.). *REopt Lite tutorial: Resilience inputs (text version).* https://www.nlr.gov/reopt/curriculum/videos/reopt-lite-tutorial-module-4-text

Pacific Northwest National Laboratory. (2021). *Calculating energy and water loads for resilience planning* (PNNL-SA-165444). U.S. Department of Energy, Federal Energy Management Program. https://www.energy.gov/sites/default/files/2022-04/trn-calculating-energy-water-loads.pdf

U.S. Department of Energy, Federal Energy Management Program. (2006). *Performing energy security assessments: A how-to guide for federal facility managers.* Oak Ridge National Laboratory. https://www1.eere.energy.gov/femp/pdfs/energy_security_guide.pdf
