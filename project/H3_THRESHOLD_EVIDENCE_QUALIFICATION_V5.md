# H3 Threshold Evidence Qualification v5.0

**Status:** ACTIVE EVIDENCE QUALIFICATION  
**Date:** 2026-09-16  
**Protocol:** EGMIV–TSP  
**Thesis destination:** Chapter 3 → Stage 5 → RQ5/H3 → Chapter 4 H3 experiment  
**Structural authority:** `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Prior qualification records:** `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V1.md` through `V4.md`  
**Page-control authority:** `../thesis/00_governance/THESIS_PAGE_BUDGET_160_V1.md`

> This version preserves the prior qualification of `s_P^{min}`, `s_T^{min}`, `s_{P,rec}`, and `s_{T,rec}` and advances the registry through the hard-failure / avoid set `F(t)`. It does not alter the frozen semantics of `K(t)`, `G_rec(t)`, `T_V`, or `T_R`.

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
| `F` | **SUPPORTED AS A PROVENANCE-CONSTRAINED AVOID-SET CONSTRUCTION** | **NO UNIVERSAL SET/THRESHOLD** | **OPEN** | **BLOCKED** |
| `T_V` | OPEN | REJECTED by structure | OPEN | BLOCKED |
| `T_R` | OPEN | REJECTED by structure | OPEN | BLOCKED |

---

# 2. Object Q5 — `F(t)` hard-failure / avoid set

## 2.1 Thesis role

The frozen H3 semantics require three distinct state classes:

```math
\boxed{
K(t)=\text{acceptable operation},
}
```

```math
\boxed{
F(t)=\text{hard/unacceptable states that the recovery trajectory must avoid},
}
```

and

```math
\boxed{
D(t)=K(t)^c\setminus F(t).
}
```

`D(t)` is the degraded recovery-eligible region used to represent states that are outside acceptable operation but are not declared forbidden. Membership in `D` alone does **not** prove that recovery is dynamically achievable; actual recoverability is determined later by the reach–avoid computation.

The qualification question is:

> Which states are scientifically defensible members of `F(t)` without collapsing every unacceptable service state into hard failure and thereby eliminating degraded recovery?

---

## 2.2 Targeted evidence-search boundary

The search was restricted to sources needed to answer exactly four questions:

1. What does reach–avoid theory require an avoid/unsafe set to represent?
2. Which power-system states are explicitly treated by authoritative reliability standards as conditions to prevent or mitigate?
3. Which transportation functions are explicitly treated by federal emergency doctrine as life-safety/critical access requirements?
4. Does any authoritative source justify `F=K^c` or one universal numerical hard-failure threshold for a coupled Power–Transportation system?

Sources were restricted to peer-reviewed stochastic reach–avoid literature and current/authoritative NERC and FEMA materials. Broad resilience browsing and algorithm selection were excluded under EGMIV–TSP.

---

## 2.3 Qualified evidence

### E1 — Reach–avoid theory requires a distinct unsafe/avoid set

Summers and Lygeros formulate finite-horizon stochastic reach–avoid as the probability of reaching a target set while avoiding an unsafe set before the target is hit. The target and unsafe sets are distinct mathematical objects supplied by the problem specification rather than being inferred from one another (Summers & Lygeros, 2010).

Abate, Prandini, Lygeros, and Sastry similarly characterize probabilistic safety with respect to a declared safe region of state space and compute policies that maximize the probability of remaining in that region (Abate et al., 2008).

Vinod and Oishi formulate stochastic reachability over time-varying state constraints and explicitly treat safety/performance constraints as problem-defined sets under bounded control authority (Vinod & Oishi, 2021).

**Evidence use:** supports keeping `F` separate from `K^c` and defining it from explicit safety/forbidden-state requirements before the reach–avoid solver is selected.

### E2 — Power-system instability, uncontrolled separation, and cascading are authoritative unacceptable outcomes

NERC Reliability Standard TOP-001-6 states that its purpose is to prevent instability, uncontrolled separation, or cascading outages that adversely affect Interconnection reliability and requires prompt action to prevent or mitigate such occurrences (North American Electric Reliability Corporation [NERC], 2021/2025).

Current NERC reliability terminology defines System Operating Limits from configuration-specific operating criteria including facility ratings, transient stability, voltage stability, and system voltage limits. This means the relevant hard boundary is not one universal numeric value; it depends on the actual system configuration and prescribed reliability criteria (NERC, 2025).

**Evidence use:** supports admitting case-applicable instability, uncontrolled separation, cascading, and technically justified protection/safety limits as candidate power-side hard-failure criteria. It does **not** justify classifying every minor service shortfall or every recoverable operating-limit excursion as `F`.

### E3 — Power-system limits can have emergency margins; therefore not every violation of nominal operation is automatically hard failure

NERC operating-limit methodology distinguishes normal and emergency ratings/voltage limits and allows system adjustments within specified emergency durations in some operating conditions. This distinction demonstrates that degraded or emergency operation can exist between normal acceptability and catastrophic outcomes, depending on the applicable methodology and system conditions (NERC, FAC-011 methodology).

**Evidence use:** directly supports preserving a nonempty degraded region instead of defining `F=K^c`.

### E4 — Critical transportation is function-specific and includes life-safety access

FEMA's Response and Recovery Federal Interagency Operational Plan defines critical transportation as transportation infrastructure access and accessible transportation services required for response priorities, including evacuation and delivery of vital personnel, equipment, and services. It identifies establishment of physical access through appropriate corridors and movement of lifesaving and life-sustaining resources as critical transportation tasks (Federal Emergency Management Agency [FEMA], 2025).

**Evidence use:** supports admitting case-authority-defined loss of mandatory life-safety/critical access as a candidate transportation hard-failure criterion when the selected H3 specification declares that loss forbidden even transiently.

### E5 — A transportation component outage is not automatically system hard failure

FEMA's Community Lifelines Toolkit provides transportation examples in which ordinary bus service is unavailable while modified mass-transit schedules and microtransit are used as roads become passable. Thus local component/service loss can coexist with alternative or degraded service before full recovery (FEMA, 2023).

**Evidence use:** rejects the rule `component failed ⇒ Y∈F` and supports placing many outage states in `D=K^c\setminus F` when critical life-safety constraints remain satisfiable.

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
| Summers & Lygeros (2010) | PASS | PASS | PASS | PASS — peer-reviewed Automatica | PASS | General stochastic hybrid reach–avoid theory; admitted for unsafe-set semantics | **ADMIT** |
| Abate et al. (2008) | PASS | PASS | PASS | PASS — peer-reviewed Automatica | PASS | General stochastic safety/reachability; admitted for declared safe-region semantics | **ADMIT** |
| Vinod & Oishi (2021) | PASS | PASS | PASS | PASS — peer-reviewed Automatica | PASS | Stochastic target-tube reachability; admitted for constrained-set semantics | **ADMIT** |
| NERC TOP-001-6 / Glossary | PASS | PASS | PASS | PASS — mandatory reliability standard + official terminology | PASS | Bulk Electric System; admitted for power-side candidate hard-state semantics, not universal case thresholds | **ADMIT WITH DOMAIN LIMIT** |
| FEMA Response and Recovery FIOP (2025) | PASS | PASS | PASS | PASS — federal response doctrine | PASS | Disaster-response critical transportation; admitted for life-safety/critical-access semantics | **ADMIT** |
| FEMA Community Lifelines Toolkit 2.1 (2023) | PASS | PASS | PASS | PASS — federal emergency-management toolkit | PASS | Emergency lifeline stabilization; admitted to show local outage/degradation need not equal system hard failure | **ADMIT** |

### Search result boundary

No admitted source establishes a universal coupled-infrastructure hard-failure set or a universal scalar threshold of the form

```math
S_P<c_P
\quad\text{or}\quad
S_T<c_T
```

that is valid across all Power–Transportation systems, hazards, operating modes, critical-service classes, spatial scales, and time horizons.

Therefore the **semantics and provenance rule for `F` are supported, but the case-specific criteria remain open**.

---

## 2.5 Canonical thesis construction of `F(t)`

Let `R_F` be the set of case-qualified hard-failure criteria. Each criterion is represented as

```math
h_r(Y,t;\kappa_r)>0,
\qquad r\in R_F,
```

where `\kappa_r` is a sourced, case-specific threshold/parameter set with units, authority, uncertainty, and validity domain.

Define

```math
\boxed{
F(t)
=
\bigcup_{r\in R_F}
\left\{Y:h_r(Y,t;\kappa_r)>0\right\}.
}
```

An equivalent logical form is

```math
\boxed{
Y\in F(t)
\iff
\exists r\in R_F:\ h_r(Y,t;\kappa_r)>0.
}
```

This is a thesis-derived set construction `[D]`; the evidence sources justify the classes of admissible hard-failure criteria and their case-specific provenance, not the final numerical thresholds.

---

## 2.6 Candidate criterion classes

The final case may use only criteria that pass evidence qualification. Candidate classes are:

### A. Power hard-safety/reliability criteria

```math
F_P^{hard}(t)
=
F_{P,\rm instability}
\cup
F_{P,\rm uncontrolled\ separation}
\cup
F_{P,\rm cascading}
\cup
F_{P,\rm protection/safety}.
```

Possible case-specific realizations include:

- instability prohibited by the applicable reliability methodology;
- uncontrolled separation prohibited by the applicable reliability methodology;
- cascading prohibited by the applicable reliability methodology;
- violation of a technically justified emergency/protection limit that the selected authority treats as non-admissible for the recovery trajectory;
- case-specific emergency critical-load floor, but only if the authority requires that it never be crossed.

A normal operating-limit violation is **not automatically** admitted to `F`; emergency ratings, corrective-action time, protection design, and the case authority must be examined first.

### B. Transportation hard-safety/critical-access criteria

```math
F_T^{hard}(t)
=
F_{T,\rm unsafe\ use}
\cup
F_{T,\rm mandatory\ access}
\cup
F_{T,\rm life\ safety}.
```

Possible case-specific realizations include:

- a transportation state in which the recovery policy would require use of an authority-closed/unsafe facility or route;
- loss of a mandatory critical access function when the selected emergency authority explicitly requires continuous access;
- failure of a case-defined evacuation/lifesaving movement requirement that is declared non-negotiable during the recovery interval.

A road closure, bus outage, bridge outage, low speed, congestion, or reduced trip completion is **not automatically** a system-level hard failure because rerouting, temporary capacity, or alternative modes may preserve admissible critical mobility.

### C. Coupled P–T hard-failure criteria

A coupled criterion may be included only when the case evidence establishes a genuinely joint forbidden condition that cannot be represented correctly as separate power and transportation constraints:

```math
F_{PT}^{hard}(t)
=
\bigcup_{q\in R_{PT}^{hard}}
\{Y:h_q^{PT}(Y,t)>0\}.
```

Examples may include a documented coupled state in which power loss and transport inaccessibility jointly eliminate an indispensable emergency function. No such criterion is frozen until a selected case provides evidence and a measurable definition.

The final avoid set is therefore

```math
\boxed{
F(t)
=
F_P^{hard}(t)
\cup
F_T^{hard}(t)
\cup
F_{PT}^{hard}(t),
}
```

with empty terms permitted if a criterion class is not supported by the selected case.

---

## 2.7 Mandatory distinction from degraded operation

The thesis must preserve

```math
\boxed{F(t)\subsetneq K(t)^c}
```

for the intended H3 demonstrator whenever degraded recovery is part of the research question.

Then

```math
\boxed{
D(t)=K(t)^c\setminus F(t)
}
```

contains states that violate one or more acceptable-operation requirements but have not crossed a declared hard-failure boundary.

Examples that may belong in `D` rather than `F`, depending on case evidence, include:

- partial load shedding while critical safety constraints remain satisfied;
- reduced transportation trip completion with safe critical routes still available;
- temporary operation inside an authority-permitted emergency rating/time band;
- local road/transit component outages with viable detours/alternative modes;
- service below `s_P^{min}` or `s_T^{min}` when the shortfall is recoverable and not prohibited even transiently.

This distinction is essential because setting

```math
F(t)=K(t)^c
```

would make every degraded state forbidden and would destroy the thesis's intended post-degradation reach–avoid recovery problem.

---

## 2.8 Non-circularity rule

Do **not** define

```math
F(t)
=
\{Y:\text{the reachability solver later says recovery is impossible}\}.
```

That would use the output of the H3 reachability problem to define one of its own inputs.

Instead:

```math
\boxed{
\text{authority/evidence-defined forbidden states}
\rightarrow F
\rightarrow
\text{reach–avoid computation}
\rightarrow
\text{states from which }G_{rec}\text{ is reachable while avoiding }F.
}
```

Thus `F` is a **specification input**, while dynamic non-recoverability is a **reachability result**.

---

## 2.9 What must not be used directly as `F`

The following constructions are rejected unless independently justified by the selected case:

1. `F=K^c`;
2. `F=G_rec^c`;
3. all states with `S_P<s_P^{min}`;
4. all states with `S_T<s_T^{min}`;
5. every component outage;
6. every SOL/operating-limit excursion without examining emergency margins and corrective-action allowances;
7. all states from which a preliminary solver happens not to recover;
8. zero service as the only possible hard-failure definition;
9. an arbitrary weighted composite failure score;
10. an AI/ML anomaly label with no validated mapping to an authority-defined unsafe state.

---

## 2.10 Logical consistency tests required before numerical freeze

The final case-specific `F` must pass:

```math
\boxed{K(t)\cap F(t)=\varnothing,}
```

and, for the intended degraded-recovery H3 domain,

```math
\boxed{D(t)=K(t)^c\setminus F(t)\neq\varnothing.}
```

Additionally,

```math
\boxed{G_{rec}(t)\cap F(t)=\varnothing}
```

follows from `G_rec(t)⊆K(t)` and `K(t)∩F(t)=∅` and must be checked numerically after discretization/implementation.

The case set should include test states from each intended class:

```text
acceptable / viable candidate;
acceptable but possibly nonviable candidate;
degraded recovery-eligible candidate;
hard-failure / avoid candidate.
```

If any intended class is empty under the final parameterization, report that fact rather than moving thresholds after viewing results.

---

## 2.11 Units, scales, uncertainty, and validity domain

`F` has no single physical unit because it is a union of heterogeneous hard constraints. Each criterion must therefore preserve its native units.

| Field | Qualified specification |
|---|---|
| Mathematical object | `F(t)` |
| Meaning | case-defined unsafe/forbidden state set that reach–avoid recovery trajectories may not enter |
| Units | criterion-specific; no scalar universal unit |
| Power candidate quantities | MW/Mvar/A/Hz/V, stability/protection states, load-loss quantities, topology/mode indicators, or another authority-native safety quantity |
| Transportation candidate quantities | route/facility safety status, critical-access connectivity, evacuation/lifesaving movement quantities, or another authority-native requirement |
| Spatial scale | component/corridor/OD/facility/system depending criterion; mapping to the H3 state must be explicit |
| Temporal scale | criterion-specific; some may be instantaneous while emergency limits may have allowed duration |
| Aggregation | no cross-criterion averaging unless independently justified; the default combination is logical union |
| Uncertainty | measurement/state-estimation error, threshold uncertainty, topology/status uncertainty, model-class uncertainty, temporal alignment, and authority interpretation |
| Validity domain | selected infrastructure, operating configuration, hazard/mode, critical-service class, spatial support, and recovery interval |

No probability distribution over `F` boundaries is frozen in this step. Boundary uncertainty is passed to the subsequent H3 uncertainty-qualification gate.

---

## 2.12 EGMIV epistemic status

```text
[E] Reach–avoid theory distinguishes a target set from an unsafe/avoid set and requires the trajectory to avoid the unsafe set until target attainment.
[E] NERC reliability standards explicitly seek to prevent/mitigate instability, uncontrolled separation, and cascading outages that adversely affect Interconnection reliability.
[E] Power-system operating boundaries are configuration- and criterion-specific, and emergency operating allowances can exist; therefore nominal-limit violation is not universally synonymous with hard failure.
[E] FEMA critical-transportation doctrine identifies physical access, evacuation, and movement of lifesaving/life-sustaining resources as critical transportation functions.
[E] FEMA examples show that individual transportation services/components can be unavailable while alternative or modified service remains possible.
[D] `F(t)=⋃_r{Y:h_r(Y,t;κ_r)>0}` is the thesis set construction for qualified hard criteria.
[D] `F⊂K^c` and `D=K^c\F` preserve degraded recovery-eligible states when the H3 problem requires post-degradation recovery.
[D] Membership in `D` does not prove actual reachability to `G_rec`; reachability is tested later.
[A] The final case-specific criterion list `R_F` and numerical `κ_r` values are not yet selected.
[U] Numerical hard-failure boundaries and their uncertainty remain open.
```

---

## 2.13 Qualification decision

```math
\boxed{
\begin{aligned}
\text{definition/provenance of }F &: \textbf{SUPPORTED},\\
\text{universal hard-failure set} &: \textbf{REJECTED},\\
F=K^c &: \textbf{REJECTED},\\
\text{case-specific criterion set }R_F &: \textbf{OPEN},\\
\text{case-specific thresholds }\kappa_r &: \textbf{OPEN},\\
\text{confirmatory-code admission} &: \textbf{BLOCKED UNTIL CASE EVIDENCE IS FROZEN}.
\end{aligned}
}
```

The scientifically admissible result is therefore a **provenance-constrained union of authority-defined unsafe states**, not a generic complement of acceptable operation and not an arbitrary service threshold.

---

# 3. Next admissible object

```math
\boxed{T_V}
```

The next targeted qualification must determine the maintainability/viability horizon from a defensible engineering decision/service interval without assuming a universal horizon and without conflating simulation duration, observation interval, hazard duration, or recovery deadline.

After `T_V`, qualify `T_R`.

---

# References — APA 7

Abate, A., Prandini, M., Lygeros, J., & Sastry, S. (2008). Probabilistic reachability and safety for controlled discrete time stochastic hybrid systems. *Automatica, 44*(11), 2724–2734. https://doi.org/10.1016/j.automatica.2008.03.027

Federal Emergency Management Agency. (2023). *Community lifelines toolkit* (Version 2.1). https://www.fema.gov/sites/default/files/documents/fema_lifelines-toolkit-v2.1_2023.pdf

Federal Emergency Management Agency. (2025). *Response and recovery federal interagency operational plan*. https://www.fema.gov/sites/default/files/documents/fema_rd_response-recovery-fiop-npb-042025.pdf

North American Electric Reliability Corporation. (2025). *Glossary of terms used in NERC reliability standards*. https://www.nerc.com/globalassets/standards/reliability-standards/glossary_of_terms_111225.pdf

North American Electric Reliability Corporation. (2021/2025). *TOP-001-6: Transmission operations*. https://www.nerc.com/standards/reliability-standards/top/top-001-6

Summers, S., & Lygeros, J. (2010). Verification of discrete time stochastic hybrid systems: A stochastic reach-avoid decision problem. *Automatica, 46*(12), 1951–1961. https://doi.org/10.1016/j.automatica.2010.08.006

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458

