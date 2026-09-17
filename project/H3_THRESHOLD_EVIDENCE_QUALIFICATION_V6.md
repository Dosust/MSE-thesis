# H3 Threshold Evidence Qualification v6.0

**Status:** ACTIVE EVIDENCE QUALIFICATION  
**Date:** 2026-09-16  
**Protocol:** EGMIV–TSP  
**Thesis destination:** Chapter 3 → Stage 5 → RQ5/H3 → Chapter 4 H3 experiment  
**Structural authority:** `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Prior qualification records:** `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V1.md` through `V5.md`  
**Page-control authority:** `../thesis/00_governance/THESIS_PAGE_BUDGET_160_V1.md`

> This version preserves all prior H3 service/recovery/failure-set qualifications and advances the registry through the viability / maintainability horizon `T_V`. It does not alter the frozen semantics of `K(t)`, `G_rec(t)`, `F(t)`, or `T_R`.

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
| `T_V` | **SUPPORTED AS A PROVENANCE-CONSTRAINED FINITE MAINTAINABILITY HORIZON** | **REJECTED** | **OPEN** | **BLOCKED** |
| `T_R` | OPEN | REJECTED by structure | OPEN | BLOCKED |

---

# 2. Object Q6 — `T_V` viability / maintainability horizon

## 2.1 Thesis role

The frozen Stage-5 probabilistic viability object is

```math
\boxed{
\mathcal V_{\alpha,T_V}(t)
=
\left\{
y\in K(t):
\exists\pi\in\Pi_{\rm adm}
\text{ such that }
\Pr^{\pi}
\left[
Y_\tau\in K(\tau),
\forall\tau\in[t,t+T_V]
\mid\mathcal I_t
\right]
\ge\alpha
\right\}.
}
```

`T_V` therefore answers one question only:

> **For how long must the coupled Power–Transportation system be able to remain within the declared acceptable-operation set `K(τ)` under admissible control and uncertainty?**

It is a physical/service decision horizon, not automatically a numerical simulation setting.

---

## 2.2 Targeted evidence-search boundary

The search was restricted to sources needed to answer four questions:

1. Is a finite horizon an admissible input to stochastic viability analysis?
2. What engineering evidence can legitimately determine the duration for which critical service must be sustained?
3. Is there a universal maintainability duration applicable to coupled Power–Transportation resilience?
4. How must `T_V` be distinguished from simulation duration, observation interval, hazard duration, operational/replanning period, and recovery deadline `T_R`?

Sources were restricted to peer-reviewed stochastic-viability theory and authoritative DOE/NREL/NIST resilience guidance. Broad resilience browsing and solver selection were excluded under EGMIV–TSP.

---

## 2.3 Qualified evidence

### E1 — Finite-horizon stochastic viability is mathematically well defined

Doyen and De Lara formulate uncertain discrete-time dynamics on a declared finite time interval `t=t0,…,T` and define stochastic viability through the probability of satisfying state and control constraints over that horizon. Their dynamic-programming construction treats the terminal time/horizon as part of the problem specification rather than as a universal property of the system (Doyen & De Lara, 2010).

**Evidence use:** supports the finite-horizon H3 viability formulation and the interpretation of `T_V` as an externally declared analysis/service horizon.

### E2 — Critical-load sustainment duration is scenario/site specific, not universal

DOE/FEMP resilience practice uses site-specific resilience planning and tools that evaluate how long a system can sustain a site's critical load during a grid outage. REopt resilience inputs explicitly require a specified outage duration, and REopt outputs test whether the critical load can be sustained for that specified outage period; example durations are scenario inputs rather than universal standards (National Renewable Energy Laboratory [NREL], 2020a, 2020b; U.S. Department of Energy, Federal Energy Management Program [FEMP], n.d.).

**Evidence use:** supports deriving a power-side maintainability horizon from a documented outage/continuity requirement or scenario rather than adopting a generic number of hours or days.

### E3 — The required service time depends on mission/threat/outage consequences

DOE guidance on resilient power planning states that critical-load definitions and backup-power duration should consider the nature of the threat and the potential/expected duration of outages; it also notes that different facilities may have established requirements that differ materially (U.S. Department of Energy [DOE], 2018).

**Evidence use:** supports a case-/mission-/hazard-specific `T_V` and rejects transferring another organization's backup-duration requirement directly into this thesis without a matching validity domain.

### E4 — Lifeline service time objectives depend on users, consequences, and context

NIST states that practical lifeline recovery/service objectives must be defined in terms of when basic services are needed by different users, and that target service-recovery times depend on the consequences of interruption, local conditions, services provided, and user needs (Davis et al., 2024). NIST's functional-recovery program likewise treats recovery priorities and timelines as context-sensitive engineering objectives rather than universal constants (National Institute of Standards and Technology [NIST], n.d.).

**Evidence use:** reinforces that the time basis for Stage-5 service constraints must originate from the selected system/service context rather than arbitrary modeling convenience.

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
| Doyen & De Lara (2010) | PASS | PASS | PASS | PASS — peer-reviewed control theory | PASS | General stochastic viability; admitted for finite-horizon semantics | **ADMIT** |
| NREL REopt resilience tutorials (2020) | PASS | PASS | PASS | PASS — national-laboratory tool documentation | PASS | Site-level critical-load outage analysis; admitted for specified-duration semantics, not a universal value | **ADMIT WITH SCOPE LIMIT** |
| DOE/FEMP resilience planning | PASS | PASS | PASS | PASS — federal resilience guidance | PASS | Facility/site resilience; admitted for mission/site specificity | **ADMIT** |
| DOE (2018) resilient-power guidance | PASS | PASS | PASS | PASS — federal technical guidance | PASS | Federal-facility energy resilience; admitted for threat/outage-duration selection principle | **ADMIT WITH DOMAIN LIMIT** |
| Davis et al. (2024), NIST | PASS | PASS | PASS | PASS — NIST lifeline functional-recovery research | PASS | Earthquake/lifeline recovery; admitted for context-dependent service-time objectives | **ADMIT WITH SCOPE LIMIT** |

### Search-result boundary

No admitted source establishes one universal maintainability duration such as

```math
T_V=12\ \mathrm{h},
24\ \mathrm{h},
72\ \mathrm{h},
7\ \mathrm{d},
14\ \mathrm{d},
\text{or }30\ \mathrm{d}
```

for all coupled Power–Transportation systems, hazards, service classes, spatial scales, and operating contexts.

Therefore a universal numerical `T_V` is **rejected**.

---

## 2.5 Canonical thesis definition

Let

```math
\mathcal R_V
```

be the qualified set of case-specific service-continuity / maintainability requirements relevant to the H3 demonstrator. Each requirement record must identify

```math
r_V
=
(\text{service},\text{population/entity},\text{start condition},\text{duration},\text{authority},\text{hazard/scenario},\text{uncertainty},\text{validity domain}).
```

Then `T_V` is the finite horizon over which the declared viability statement is intended to hold:

```math
\boxed{
T_V
=\text{case-qualified maintainability horizon used in }
\Pr[Y_\tau\in K(\tau),\ \forall\tau\in[t,t+T_V]].
}
```

This is a thesis-defined role `[D]`; the numerical value is not frozen until the case requirement is qualified.

---

## 2.6 Admissible provenance hierarchy for `T_V`

A numerical `T_V` may be admitted only through the following hierarchy:

### Tier V-A — direct authority/service continuity requirement

A regulator, operator, facility owner, emergency authority, or other case authority explicitly requires the relevant service to remain available for duration `T_req`.

```math
\boxed{T_V=T_{req}}
```

may be admitted if the requirement matches the H3 service definition and validity domain.

### Tier V-B — authoritative scenario / outage-duration requirement

The selected case authority defines a credible disruption/outage scenario of duration `T_out` and requires acceptable critical service throughout that period.

```math
\boxed{T_V=T_{out}}
```

may be admitted as a scenario-specific viability horizon.

### Tier V-C — evidence-bounded thesis scenario

If no direct service-duration requirement exists, a horizon may be declared as an explicit thesis scenario assumption only when its range is justified from case-specific outage/hazard/mission evidence and sensitivity analysis is planned.

Status must remain `[A]`, not `[E]`.

### Rejected route

A duration chosen only because it is computationally convenient, common in another paper, or available in software defaults is not admissible as an evidence-supported `T_V`.

---

## 2.7 Mandatory separation from other time quantities

The thesis must preserve the following distinctions.

### Numerical integration step

```math
\boxed{\Delta t_{sim}\neq T_V.}
```

`Δt_sim` controls numerical resolution. It does not state how long acceptable service must be maintained.

### Observation / validation interval

```math
\boxed{\Delta t_{obs}\neq T_V.}
```

`Δt_obs` controls measurement/aggregation resolution. A 5-min or 15-min observation interval does not imply a 5-min or 15-min viability requirement.

### Total simulation duration

```math
\boxed{T_{sim}\neq T_V,\qquad T_{sim}\ge T_V\ \text{for a complete direct simulation of the viability window}.}
```

The simulation may extend beyond the viability horizon for initialization, hazard realization, recovery, sensitivity analysis, or comparison. Equality is optional, not semantic.

### Hazard duration

Let `T_H` denote the duration of the external hazard forcing or selected hazard episode.

```math
\boxed{T_H\neq T_V\ \text{in general}.}
```

A system may need to maintain service beyond the forcing interval because consequences persist after the hazard ceases; alternatively a receding-horizon operational analysis may evaluate a shorter decision window during a longer evolving hazard. Equality requires case justification.

### Operational / replanning period

Let `Δt_plan` denote the interval at which operators reassess and update actions.

```math
\boxed{\Delta t_{plan}\neq T_V.}
```

A receding-horizon implementation may re-evaluate viability every `Δt_plan`, but the look-ahead maintainability requirement remains a separate object.

### Recovery horizon

```math
\boxed{T_V\neq T_R\ \text{in general}.}
```

`T_V` asks how long acceptable operation can be maintained from an acceptable state. `T_R` asks by when a degraded state must reach `G_rec` while avoiding `F`. No universal ordering or equality between them is assumed.

---

## 2.8 Coupled P–T horizon logic

Power and transportation may have different authority-native continuity requirements:

```math
T_{V,P}^{req},
\qquad
T_{V,T}^{req},
\qquad
T_{V,PT}^{req}\ \text{(if a coupled requirement exists)}.
```

The preferred scientific representation is to keep the acceptable set time-varying:

```math
K(\tau)
=
K_P(\tau)\cap K_T(\tau)\cap K_{PT}(\tau)\cap K_{op}(\tau),
```

so each requirement is active over its own documented temporal support.

If a single solver horizon is required, an admissible thesis reduction is

```math
\boxed{
T_V
=
\max\left(
T_{V,P}^{req},
T_{V,T}^{req},
T_{V,PT}^{req}
\right),
}
```

**only if** `K(τ)` correctly encodes which requirements remain active at each time. This is a thesis-derived implementation rule `[D]`, not an externally established universal formula.

If no coupled requirement exists, `T_{V,PT}^{req}` is omitted rather than invented.

---

## 2.9 Receding-horizon viability option

If the final operational problem requires repeated decision updates, define an assessment time sequence

```math
t_k=t_0+k\Delta t_{plan}.
```

At each update,

```math
\mathcal V_{\alpha,T_V}(t_k)
```

is recomputed or re-evaluated using the current information state `\mathcal I_{t_k}`.

This yields

```math
\boxed{
\text{observe/update}
\rightarrow
\mathcal V_{\alpha,T_V}(t_k)
\rightarrow
u_k
\rightarrow
\text{advance to }t_{k+1}.
}
```

where `u_k` is the admissible operational action. A receding implementation does not justify shortening `T_V` arbitrarily; the look-ahead horizon must still be tied to the decision/service requirement or labeled as an explicit model assumption.

---

## 2.10 What must not be used directly as `T_V`

The following are rejected unless independently justified by the selected case:

1. the simulation integration step;
2. the observation interval;
3. the dataset sampling interval;
4. the total simulation run length;
5. the hazard duration merely because it is available;
6. `T_R` merely for notational convenience;
7. a 12-, 24-, 72-hour, 7-day, 14-day, or 30-day value copied from another organization or paper;
8. a REopt tutorial example duration;
9. a software default horizon;
10. a horizon selected after viewing H3 results because it produces a preferred conclusion.

---

## 2.11 Pre-registration and sensitivity rule

Before confirmatory H3 execution, the final `T_V` must be frozen with:

```text
value and units;
start-time convention;
service/decision rationale;
source authority;
hazard/scenario domain;
spatial/service population;
uncertainty or admissible range;
relationship to T_H, T_sim, Δt_obs, Δt_plan, and T_R;
status = evidence-supported or explicit assumption.
```

If the evidence supports a range rather than a point value,

```math
T_V\in[T_V^{-},T_V^{+}],
```

then the confirmatory design must either preregister a primary value plus sensitivity analysis or propagate horizon uncertainty explicitly. The horizon may not be tuned after observing H3 outcomes.

---

## 2.12 Units, scales, aggregation, and uncertainty

| Field | Qualified specification |
|---|---|
| Mathematical object | `T_V` |
| Physical meaning | duration over which acceptable coupled service must be maintainable |
| Units | time (seconds/minutes/hours/days as appropriate to the case) |
| Provenance | authority-defined continuity requirement, authority-defined outage/scenario duration, or explicit evidence-bounded thesis assumption |
| Start convention | must be declared: assessment time, disruption onset, post-detection time, or another case-defined origin |
| Spatial scale | coupled H3 demonstrator domain; underlying requirements may be entity/corridor/system specific |
| Temporal relation | finite horizon for the viability chance constraint; not an observation or numerical resolution |
| Uncertainty | scenario/outage-duration uncertainty, service-duration requirement uncertainty, event timing uncertainty, and model/decision-horizon uncertainty where applicable |
| Validity domain | selected case, hazard, service class, operational mode, spatial support, and decision context |

---

## 2.13 EGMIV epistemic status

```text
[E] Stochastic viability can be formulated on a finite, explicitly declared time horizon.
[E] Critical-load resilience analyses use specified outage durations and evaluate whether critical service can be sustained for those durations.
[E] Resilience/service time objectives are context dependent and can depend on mission, hazard/outage duration, interruption consequences, service type, and users.
[D] T_V is the duration over which the H3 viability event Y_τ∈K(τ) for all τ∈[t,t+T_V] is asserted.
[D] T_V is distinct from Δt_sim, Δt_obs, T_sim, T_H, Δt_plan, and T_R unless a case-specific requirement justifies equality.
[D] If one computational horizon must cover multiple sector-specific continuity requirements, max native duration with time-varying K(τ) is an admissible implementation reduction, not a universal law.
[A] No case-specific P–T maintainability duration has yet been selected.
[U] The numerical value/range of T_V remains open.
```

---

## 2.14 Qualification decision

```math
\boxed{
\begin{aligned}
\text{definition/provenance of }T_V &: \textbf{SUPPORTED},\\
\text{finite-horizon viability role} &: \textbf{SUPPORTED},\\
\text{universal numerical }T_V &: \textbf{REJECTED},\\
\text{case-specific numerical }T_V &: \textbf{OPEN},\\
T_V=T_H\text{ universally} &: \textbf{REJECTED},\\
T_V=T_R\text{ universally} &: \textbf{REJECTED},\\
T_V=T_{sim}\text{ universally} &: \textbf{REJECTED},\\
\text{confirmatory-code admission} &: \textbf{BLOCKED UNTIL CASE EVIDENCE IS FROZEN}.
\end{aligned}
}
```

The scientifically admissible result is a provenance-constrained finite maintainability horizon, not a guessed duration and not a duration inherited from numerical convenience.

---

# 3. Next admissible object

```math
\boxed{T_R}
```

The next targeted qualification must establish the recovery deadline/horizon: by what case-supported time must a degraded state reach `G_rec` while avoiding `F`, and how must that deadline be separated from `T_V`, hazard duration, functional-recovery target times, simulation duration, and any dwell requirement.

---

# References — APA 7

Davis, C. A., Herseth, A., Johnson, K., & Hortacsu, A. (2024). *Functional recovery of lifeline infrastructure system services*. Proceedings of the 18th World Conference on Earthquake Engineering. National Institute of Standards and Technology. https://www.nist.gov/publications/functional-recovery-lifeline-infrastructure-system-services

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008

National Institute of Standards and Technology. (n.d.). *Functional recovery of buildings and lifelines*. https://www.nist.gov/programs-projects/functional-recovery-buildings-and-lifelines

National Renewable Energy Laboratory. (2020a). *REopt Lite tutorial: Resilience inputs* (NREL/TP-7A40-76676). https://www.nrel.gov/docs/fy20osti/76676.pdf

National Renewable Energy Laboratory. (2020b). *REopt Lite tutorial: Resilience outputs* (NREL/TP-7A40-76678). https://www.nrel.gov/docs/fy20osti/76678.pdf

U.S. Department of Energy. (2018). *Small modular reactors: Adding to resilience at federal facilities*. https://www.energy.gov/sites/prod/files/2018/01/f47/Small%20Modular%20Reactors%20-%20Adding%20to%20Resilience%20at%20Federal%20Facilities%20.pdf

U.S. Department of Energy, Federal Energy Management Program. (n.d.). *Distributed energy resources for resilience*. https://www.energy.gov/cmei/femp/distributed-energy-resources-resilience

