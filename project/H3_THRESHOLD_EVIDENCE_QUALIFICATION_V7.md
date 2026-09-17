# H3 Threshold Evidence Qualification v7.0

**Status:** ACTIVE EVIDENCE QUALIFICATION  
**Date:** 2026-09-17  
**Protocol:** EGMIV–TSP  
**Thesis destination:** Chapter 3 → Stage 5 → RQ5/H3 → Chapter 4 H3 experiment  
**Structural authority:** `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Prior qualification records:** `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V1.md` through `V6.md`  
**Page-control authority:** `../thesis/00_governance/THESIS_PAGE_BUDGET_160_V1.md`

> This version preserves all prior H3 service/recovery/failure-set and `T_V` qualifications and advances the registry through the recovery deadline / horizon `T_R`. It does not alter the frozen semantics of `K(t)`, `G_rec(t)`, `F(t)`, or `T_V`.

---

## 1. Qualification order and current state

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

| Object | Definition/provenance | Universal numerical value | Case-specific numerical value | Confirmatory admission |
|---|---|---|---|---|
| `s_P^{min}` | SUPPORTED | REJECTED | OPEN | BLOCKED |
| `s_T^{min}` | SUPPORTED | REJECTED | OPEN | BLOCKED |
| `s_{P,rec}` | SUPPORTED | REJECTED | OPEN | BLOCKED |
| `s_{T,rec}` | SUPPORTED | REJECTED | OPEN | BLOCKED |
| `F` | SUPPORTED AS PROVENANCE-CONSTRAINED AVOID-SET CONSTRUCTION | NO UNIVERSAL SET/THRESHOLD | OPEN | BLOCKED |
| `T_V` | SUPPORTED AS PROVENANCE-CONSTRAINED FINITE MAINTAINABILITY HORIZON | REJECTED | OPEN | BLOCKED |
| `T_R` | **SUPPORTED AS A PROVENANCE-CONSTRAINED RECOVERY DEADLINE** | **REJECTED** | **OPEN** | **BLOCKED** |

---

# 2. Object Q7 — `T_R` recovery deadline / horizon

## 2.1 Thesis role

The frozen Stage-5 reach–avoid recovery object is

```math
\boxed{
\mathcal R_{\beta,T_R}(t)
=
\left\{
y:
\exists\pi\in\Pi_{\rm adm}
\text{ such that }
\Pr^{\pi}
\left[
\tau_{G_{\rm rec}}\le t+T_R,
Y_s\notin F(s)\ \forall s\in[t,\tau_{G_{\rm rec}})
\mid\mathcal I_t
\right]
\ge\beta
\right\}.
}
```

with first-entry time

```math
\tau_{G_{\rm rec}}
=
\inf\{s\ge t:Y_s\in G_{\rm rec}(s)\}.
```

`T_R` therefore answers one question only:

> **By what deadline must a degraded trajectory enter the declared recovery target `G_rec` while avoiding the hard-failure set `F`?**

It is a recovery requirement. It is not the observed recovery time, the dwell duration, the viability horizon, the hazard duration, or a numerical simulation setting.

---

## 2.2 Targeted evidence-search boundary

The search was restricted to sources needed to answer four questions:

1. What is an authoritative recovery-time objective for lifeline infrastructure?
2. Can recovery deadlines differ across users, services, components, and criticality classes?
3. Is there one universal recovery time that can be transferred to coupled Power–Transportation systems?
4. How must `T_R` be separated from realized recovery time, `T_V`, hazard duration, simulation duration, service threshold, and dwell time?

Sources were restricted to authoritative NIST/FEMA/FHWA recovery guidance and the already-frozen stochastic reach–avoid formulation. Broad resilience browsing and solver selection were excluded under EGMIV–TSP.

---

## 2.3 Qualified evidence

### E1 — NIST explicitly defines a recovery-time objective as a planned restoration duration

NIST SP 1310 defines a recovery time objective as the planned duration for restoring a component or system to a defined operational or functional level for a specified hazard/event level. At system level, the service recovery objective concerns the duration by which services are restored to users through the network. NIST also states that recovery time objectives may differ for users of different criticality and may require coordination and synchronization across subsystems (Davis et al., 2024).

**Evidence use:** directly supports the thesis interpretation of `T_R` as a deadline to achieve a declared recovery state, rather than as an observed outcome or arbitrary analysis window.

### E2 — Recovery objectives are specified by service need, user criticality, and consequence

NIST states that lifeline recovery objectives must be defined in terms of when basic services are needed by customers with different levels of importance, and that target service-recovery times depend on consequences of interruption, conditions, services provided, and users/uses of those services (Davis et al., 2024).

**Evidence use:** supports case-/service-/criticality-specific `T_R` and rejects one universal recovery deadline.

### E3 — Recovery targets are planning inputs, not post hoc fitted outcomes

NIST SP 1310 treats system-level performance and recovery-time objectives as inputs to both asset and organizational-action frameworks; component- and group-level objectives are then developed to meet the system-level target. The framework also states that changes to recovery objectives require transparent communication with authorities and service users (Davis et al., 2024).

**Evidence use:** supports fixing the recovery deadline before confirmatory H3 execution and prohibits selecting `T_R` after viewing model outcomes.

### E4 — FEMA stabilization targets are incident- and stakeholder-specific

FEMA's Community Lifelines construct requires stabilization targets to be developed collaboratively with relevant stakeholders, incorporated into deliberate planning, and adjusted during an incident according to impacts, operational priorities, and objectives. FEMA also distinguishes stabilization from longer-term permanent recovery (Federal Emergency Management Agency [FEMA], 2023, 2025).

**Evidence use:** supports incident- and context-specific recovery objectives and reinforces that a stabilization deadline is not automatically equivalent to complete permanent restoration.

### E5 — Transportation recovery time can be criticality dependent

FHWA resilience guidance distinguishes functional recovery time from full recovery and presents recovery-time evaluation scales whose meaning depends on the importance of the transportation asset. The numerical categories in such evaluation tools are context-specific scoring criteria, not universal recovery deadlines for this thesis (Federal Highway Administration [FHWA], 2024).

**Evidence use:** supports criticality-sensitive transportation recovery deadlines while explicitly rejecting direct import of FHWA example time bands as universal H3 values.

---

## 2.4 Source-qualification gate

For source `q`, apply

```math
G_S^{(q)}
=
G_I\land G_R\land G_C\land G_Q\land G_M\land G_V.
```

| Source | Identity | Relevance | Claim support | Authority/quality | Metadata | Validity-domain treatment | Admission |
|---|---|---|---|---|---|---|---|
| Davis et al. (2024), NIST SP 1310 | PASS | PASS | PASS | PASS — NIST technical framework | PASS | Earthquake/lifeline domain; admitted for recovery-time-objective semantics and criticality logic, not universal numeric transfer | **ADMIT WITH SCOPE LIMIT** |
| Davis et al. (2024), WCEE/NIST | PASS | PASS | PASS | PASS — NIST-authored functional-recovery paper | PASS | Earthquake/lifeline domain; admitted for user/consequence dependence | **ADMIT WITH SCOPE LIMIT** |
| FEMA Community Lifelines Toolkit 2.1 (2023) | PASS | PASS | PASS | PASS — federal emergency-management doctrine/toolkit | PASS | Incident stabilization; admitted for stakeholder/incident-specific target logic | **ADMIT** |
| FEMA Response and Recovery FIOP (2025) | PASS | PASS | PASS | PASS — federal response doctrine | PASS | Incident response/recovery; admitted for target-based end-state logic | **ADMIT** |
| FHWA transportation resilience guidance (2024) | PASS | PASS | PASS | PASS — federal highway technical guidance | PASS | Transportation/highway domain; admitted for criticality-sensitive functional-recovery timing, not universal thresholds | **ADMIT WITH SCOPE LIMIT** |

### Search-result boundary

No admitted source establishes one universal recovery deadline such as

```math
T_R=8\ \mathrm{h},
24\ \mathrm{h},
72\ \mathrm{h},
7\ \mathrm{d},
30\ \mathrm{d},
\text{or another fixed value}
```

for all coupled Power–Transportation systems, hazards, service classes, criticality levels, spatial scales, and recovery objectives.

Therefore a universal numerical `T_R` is **rejected**.

---

## 2.5 Canonical thesis definition

Let `t_R^0` denote the declared recovery-clock origin. This must be explicitly defined by the case, for example a hazard-impact epoch, declared disruption time, or another authority-consistent reference event.

Let

```math
T_{\rm rec}^{\pi}(\omega)
=
\tau_{G_{\rm rec}}(\omega;\pi)-t_R^0
```

be the realized first-entry recovery time for scenario `ω` and policy `π`, provided the trajectory avoids `F` before entry.

Then

```math
\boxed{
T_R
=\text{case-qualified maximum admissible recovery duration from }t_R^0\text{ to entry into }G_{\rm rec}.
}
```

Successful recovery by the deadline is therefore

```math
\boxed{
T_{\rm rec}^{\pi}(\omega)\le T_R
}
```

with

```math
Y_s\notin F(s),
\qquad
s\in[t_R^0,\tau_{G_{\rm rec}}).
```

This yields the explicit distinction

```math
\boxed{T_R\neq T_{\rm rec}.}
```

`T_R` is the requirement/deadline; `T_rec` is the realized outcome.

---

## 2.6 Time-origin rule

A numerical recovery duration is scientifically incomplete without its time origin.

Therefore every candidate `T_R` record must include

```text
clock origin;
event defining time zero;
time-zone / timestamp convention where field data are used;
relationship between disturbance onset, impact, detection, and recovery initiation.
```

The thesis must not silently switch between

```math
\text{time from hazard onset},
\quad
\text{time from peak impact},
\quad
\text{time from service loss},
\quad
\text{time from operator detection},
\quad
\text{time from hazard cessation}.
```

If multiple clocks are operationally relevant, preserve them explicitly rather than forcing them into one undocumented origin.

---

## 2.7 Provenance hierarchy for a numerical `T_R`

A numerical recovery deadline may be admitted only through the following hierarchy.

### Tier R-A — direct authority-defined service recovery objective

An operator, regulator, emergency authority, facility owner, transportation agency, or equivalent case authority explicitly specifies that the relevant service/function must be restored to the defined target within duration `T_req`.

```math
\boxed{T_R=T_{req}}
```

may be admitted when the service target and time origin match the H3 definition.

### Tier R-B — qualified functional-recovery objective

A recovery framework or plan defines a recovery category/time objective for the same service class, criticality class, hazard/scenario, and spatial support. The target may be admitted only after transferability review.

### Tier R-C — evidence-bounded explicit thesis assumption

If no direct case authority exists, a recovery horizon may be declared as an explicit `[A]` assumption only when bounded by case-specific restoration evidence, outage history, repair/resource evidence, or an independently justified scenario family. Sensitivity analysis is then mandatory.

### Rejected route

A deadline selected only because it is common in the literature, makes computation convenient, matches the simulation run length, or improves H3 results is not admissible as evidence-supported `T_R`.

---

## 2.8 Multiple sector/service deadlines in a coupled system

Power and transportation may have different recovery-time objectives:

```math
T_{R,P}^{(i)},
\qquad
T_{R,T}^{(w)},
\qquad
T_{R,PT}^{(q)}\ \text{if a genuine coupled objective exists}.
```

NIST explicitly permits recovery-time objectives to differ by customer/user criticality and notes the need to coordinate and synchronize subsystem recovery objectives (Davis et al., 2024).

Therefore the thesis must not average sectoral deadlines.

The preferred representation is a time-indexed target schedule or deadline family. If a single outer solver horizon is required, define

```math
\boxed{
T_R^{\rm solver}
=
\max_j T_{R,j}^{\rm req}
}
```

only while preserving every earlier deadline as an explicit intermediate constraint/target. This is a thesis-derived implementation rule `[D]`, not a universal recovery formula.

A later power deadline cannot erase an earlier transportation emergency-access deadline, and vice versa.

---

## 2.9 Mandatory separation from other time and service quantities

### Recovery service level

```math
\boxed{s_{P,\rm rec},\ s_{T,\rm rec}\neq T_R.}
```

The service thresholds answer **how much service** constitutes recovery. `T_R` answers **by when** that recovery state must be reached.

### Viability horizon

```math
\boxed{T_V\neq T_R\ \text{in general}.}
```

`T_V` is a maintainability horizon for remaining inside `K`; `T_R` is a deadline for reaching `G_rec` from a degraded state while avoiding `F`.

### Hazard duration

```math
\boxed{T_H\neq T_R\ \text{in general}.}
```

Recovery may begin before a hazard ends, continue after the forcing has ceased, or depend on resource mobilization after impact. Equality requires explicit case evidence.

### Simulation duration

```math
\boxed{T_{sim}\neq T_R.}
```

For direct simulation of the complete recovery window, the numerical run must cover the recovery deadline from the selected time origin, but the run length itself does not define the engineering deadline.

### Observation interval

```math
\boxed{\Delta t_{obs}\neq T_R.}
```

Sampling/aggregation resolution does not define a recovery objective.

### Dwell time

```math
\boxed{\tau_{\rm dwell}\neq T_R.}
```

The default frozen H3 semantics use `T_R` as the deadline for first admissible entry into `G_rec`. If the selected authority requires sustained recovery, the independent dwell condition remains

```math
Y_s\in G_{\rm rec}(s)
\quad
\forall s\in[\tau_G,\tau_G+\tau_{\rm dwell}].
```

If the authority explicitly requires the dwell interval to be completed by the recovery deadline, then the stronger case-specific condition is

```math
\boxed{
\tau_G+\tau_{\rm dwell}\le t_R^0+T_R.
}
```

This stronger condition is activated only by case evidence; it is not the default definition.

---

## 2.10 What must not be used directly as `T_R`

The following are rejected unless independently justified by the selected case:

1. the observed recovery time from the same confirmatory event;
2. the simulation duration;
3. the observation interval;
4. the hazard duration by default;
5. `T_V` merely for notational convenience;
6. `τ_dwell`;
7. full physical repair time when the declared target is functional service recovery;
8. 8 h, 24 h, 72 h, or other categories copied from FHWA/NIST examples without validity-domain matching;
9. a mean historical restoration time used as a hard deadline without an authority/decision rationale;
10. a deadline tuned after viewing H3 outcomes.

---

## 2.11 Uncertainty and preregistration rule

Before confirmatory H3 execution, the final `T_R` record must include

```text
value and units;
clock origin t_R^0;
recovery target G_rec to which the deadline applies;
service/user/criticality class;
source authority;
hazard/scenario domain;
spatial support;
uncertainty or admissible range;
relationship to T_V, T_H, T_sim, Δt_obs, and τ_dwell;
status = evidence-supported or explicit assumption.
```

If evidence supports a range

```math
T_R\in[T_R^{-},T_R^{+}],
```

then the confirmatory design must either preregister a primary value and sensitivity analysis or propagate the horizon uncertainty explicitly. No post-result tuning is allowed.

The probability model for recovery-time variability is **not** implied by the deadline. A stochastic distribution for repair/recovery time requires the independent probability-admissibility gate in `H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md`.

---

## 2.12 EGMIV epistemic status

```text
[E] Recovery-time objectives are planned durations to restore a defined operational/functional level.
[E] Recovery-time objectives may differ by user/customer criticality and can require coordination across subsystems.
[E] Functional-recovery targets are planning/design inputs and should be tied to service needs and consequences.
[E] FEMA stabilization objectives are incident- and stakeholder-specific rather than universal recovery times.
[D] H3 maps an authority-defined recovery-time objective to the deadline T_R in the reach–avoid condition.
[D] T_R is distinct from realized recovery time T_rec.
[D] A single outer solver horizon may be the maximum of multiple qualified deadlines only if all earlier service-specific deadlines remain explicit constraints.
[A] The final case-specific numerical T_R values and time origins are not yet selected.
[U] The numerical T_R, uncertainty range, and any coupled P–T deadline remain open.
```

---

## 2.13 Qualification decision

```math
\boxed{
\begin{aligned}
\text{definition/provenance of }T_R &: \textbf{SUPPORTED},\\
\text{recovery-deadline role in H3} &: \textbf{SUPPORTED},\\
\text{universal numerical }T_R &: \textbf{REJECTED},\\
\text{case-specific numerical }T_R &: \textbf{OPEN},\\
T_R=T_{\rm rec}\text{ universally} &: \textbf{REJECTED},\\
T_R=T_V\text{ universally} &: \textbf{REJECTED},\\
T_R=T_H\text{ universally} &: \textbf{REJECTED},\\
\text{confirmatory-code admission} &: \textbf{BLOCKED UNTIL CASE EVIDENCE IS FROZEN}.
\end{aligned}
}
```

Hence

```math
\boxed{
\operatorname{Status}(T_R)
=
\mathbf{STRUCTURALLY\ QUALIFIED,\ NUMERICALLY\ OPEN}.
}
```

---

# 3. Completion state of the H3 service/state/time qualification sequence

All seven required objects now have qualified semantics/provenance rules:

```math
\boxed{
\underbrace{s_P^{\min}}_{\checkmark}
\rightarrow
\underbrace{s_T^{\min}}_{\checkmark}
\rightarrow
\underbrace{s_{P,\rm rec}}_{\checkmark}
\rightarrow
\underbrace{s_{T,\rm rec}}_{\checkmark}
\rightarrow
\underbrace{F}_{\checkmark}
\rightarrow
\underbrace{T_V}_{\checkmark}
\rightarrow
\underbrace{T_R}_{\checkmark}.
}
```

This is **structural/evidentiary qualification**, not numerical closure. The final case-specific values/criteria remain open and cannot enter confirmatory code until their authorities, uncertainty, validity domains, and time/spatial supports are frozen.

The next admissible task is therefore:

```math
\boxed{
\text{case-specific H3 registry closure}
\rightarrow
\text{uncertainty qualification}
\rightarrow
\Pi_{\rm adm}
\rightarrow
\mathcal C_{H3}
\rightarrow
\text{solver selection and verification}.
}
```

Because the current case/data authority has not yet been frozen, uncertainty qualification must begin by identifying the selected case evidence for the seven qualified objects rather than inventing distributions around placeholder values.

---

# References — APA 7

Davis, C. A., Herseth, A., Johnson, K., & Hortacsu, A. (2024). Functional recovery of lifeline infrastructure system services. *Proceedings of the 18th World Conference on Earthquake Engineering*. National Institute of Standards and Technology. https://www.nist.gov/publications/functional-recovery-lifeline-infrastructure-system-services

Davis, C. A., Johnson, L. A., Kiremidjian, A., Kwasinski, A., O’Rourke, T. D., Stanley, E., Yu, K., Zareian, F., Johnson, K. J., & Hortacsu, A. (2024). *Initial framework to design lifeline infrastructure for post-earthquake functional recovery: Volume 1* (NIST SP 1310). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.1310

Federal Emergency Management Agency. (2023). *Community lifelines implementation toolkit* (Version 2.1). https://www.fema.gov/sites/default/files/documents/fema_lifelines-toolkit-v2.1_2023.pdf

Federal Emergency Management Agency. (2025). *Response and recovery federal interagency operational plan*. https://www.fema.gov/sites/default/files/documents/fema_rd_response-recovery-fiop-npb-042025.pdf

Federal Highway Administration. (2024). *Improving transportation infrastructure resilience: Guidelines for assessing current practices and prioritizing candidate projects*. U.S. Department of Transportation.

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458

