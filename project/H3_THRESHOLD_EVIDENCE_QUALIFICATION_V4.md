# H3 Threshold Evidence Qualification v4.0

**Status:** ACTIVE EVIDENCE QUALIFICATION  
**Date:** 2026-09-16  
**Protocol:** EGMIV–TSP  
**Thesis destination:** Chapter 3 → Stage 5 → RQ5/H3 → Chapter 4 H3 experiment  
**Structural authority:** `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Prior qualification records:** `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V1.md`, `V2.md`, `V3.md`  
**Page-control authority:** `../thesis/00_governance/THESIS_PAGE_BUDGET_160_V1.md`

> This version preserves the prior qualification of `s_P^{min}`, `s_T^{min}`, and `s_{P,rec}` and advances the registry through `s_{T,rec}`. It does not alter the frozen semantics of `K(t)`, `G_rec(t)`, `F(t)`, `T_V`, or `T_R`.

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
| `s_{T,rec}` | **SUPPORTED** | **REJECTED** | **OPEN** | **BLOCKED** |
| `F` | OPEN | n/a | OPEN | BLOCKED |
| `T_V` | OPEN | REJECTED by structure | OPEN | BLOCKED |
| `T_R` | OPEN | REJECTED by structure | OPEN | BLOCKED |

---

# 2. Object Q4 — `s_{T,rec}`

## 2.1 Thesis role

The frozen recovery target satisfies

```math
\boxed{G_{\rm rec}(t)\subseteq K(t).}
```

Its transportation-service component may be written

```math
S_T(Y,t)\ge s_{T,\rm rec}(t).
```

The qualification question is:

> What evidence can define a sufficiently recovered transportation-service target without assuming that recovery universally means 100% of pre-event mobility, exact restoration of the pre-event network state, or reopening every transportation component?

This is distinct from `s_T^{min}`:

- `s_T^{min}` defines the minimum mobility service required for acceptable operation in `K_svc`;
- `s_{T,rec}` defines the stricter or otherwise explicitly declared transportation-service milestone required for membership in `G_rec`.

Because `G_rec ⊆ K`, when both are scalar thresholds on the same `S_T` metric and support,

```math
\boxed{s_{T,\rm rec}(t)\ge s_T^{\min}(t).}
```

---

## 2.2 Targeted evidence-search boundary

The search was restricted to authoritative FEMA, NIST, and FHWA sources directly addressing:

1. transportation-system functional recovery;
2. post-event transportation service/functionality;
3. functional versus full recovery;
4. local/state recovery-goal setting; and
5. whether a universal recovered-service fraction exists.

Broad transportation-resilience browsing, generic network metrics, and unrelated algorithm selection were excluded under EGMIV–TSP.

---

## 2.3 Qualified evidence

### E1 — NIST transportation functional-recovery semantics

NIST defines functional recovery for lifeline infrastructure as a post-event state in which the system is maintained or restored to safely and adequately support its basic intended functions. The transportation-specific NIST workshop report explicitly treats functional recovery as a targeted performance state distinct from full functionality and states that the workshop was not intended to set universal functional-recovery goals or recovery times for transportation systems (Beyzaei et al., 2023).

**Evidence use:** supports a distinct transportation recovery target and rejects an assumption that recovered service must automatically equal full pre-event service.

### E2 — Transportation recovery objectives must reflect user needs and regional context

The NIST transportation workshop reports that state DOTs have authority to set performance/recovery goals and that user needs and regional context should drive transportation functional-recovery objectives and metrics. Participants emphasized adaptable frameworks rather than one fixed national numerical target because transportation systems, users, hazards, ownership, and regional functions differ materially (Beyzaei et al., 2023).

**Evidence use:** supports case-specific `s_{T,rec}` provenance and rejects a universal completed-trip percentage.

### E3 — Functional recovery can be below full pre-event functionality

The NIST-FEMA functional-recovery work states that functional recovery is a stepping stone toward full functionality and that the desired functional-recovery target for a building or lifeline system may be less than full pre-event functionality (Abrahams et al., 2021).

**Evidence use:** directly rejects the universal rule `s_{T,rec}=1`.

### E4 — FHWA distinguishes functional recovery from full recovery

FHWA's 2024 transportation-infrastructure resilience guidance distinguishes functional recovery from full recovery. It describes functional recovery as safe network usage with restoration sufficient to support a significant measure of pre-event functionality, while full recovery restores pre-event safety and functionality. FHWA also identifies functional-recovery time and full-recovery time as separate post-event measures (Kourkoulis et al., 2024).

**Evidence use:** provides transportation-specific support for using a recovery milestone below full restoration when the engineering objective is functional service recovery.

### E5 — FEMA permits modified and alternative transportation service before full service resumes

FEMA's Community Lifelines Toolkit provides a transportation example in which modified mass-transit schedules and microtransit are used as roads become passable, while full service is expected later. FEMA's ESF #1 also directs agencies to identify temporary alternative transportation solutions when primary routes or systems are unavailable or overwhelmed (Federal Emergency Management Agency [FEMA], 2016, 2023).

**Evidence use:** supports the thesis distinction between restored critical mobility and complete restoration of the original network/service pattern.

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
| Beyzaei et al. (2023), NIST SP 1295 | PASS | PASS | PASS | PASS — NIST transportation functional-recovery report | PASS | Earthquake-focused; admitted for transportation functional-recovery semantics and target-setting logic | **ADMIT** |
| Abrahams et al. (2021), NIST SP 1269 | PASS | PASS | PASS | PASS — NIST/FEMA federal report | PASS | Built-environment/lifeline functional recovery; admitted for functional-vs-full distinction | **ADMIT** |
| Kourkoulis et al. (2024), FHWA-HIF-24-042 | PASS | PASS | PASS | PASS — FHWA technical report | PASS | Highway-network resilience; admitted for transportation functional-vs-full recovery distinction | **ADMIT** |
| FEMA (2023), Community Lifelines Toolkit 2.1 | PASS | PASS | PASS | PASS — federal emergency-management doctrine/toolkit | PASS | Disaster-response stabilization; admitted for modified-service recovery semantics | **ADMIT** |
| FEMA (2016), ESF #1 Transportation Annex | PASS | PASS | PASS | PASS — National Response Framework annex | PASS | Emergency transportation operations; admitted for temporary-alternative-service semantics | **ADMIT** |

### Search result boundary

No admitted source establishes a universal transportation recovery requirement such as

```math
s_{T,\rm rec}=0.80,
0.90,
0.95,
\text{or }1.00
```

across transportation modes, user groups, hazards, spatial scales, service classes, and recovery objectives.

Therefore a universal numerical `s_{T,rec}` is **rejected**.

---

## 2.5 Mathematical translation into the frozen transportation service metric

Recall the frozen interval service metric

```math
S_{T,m}
=
\min\left[
1,
\frac{\sum_w\omega_w N_{w,m}^{comp}}
{\sum_w\omega_w\widehat N_{w,m}^{req}}
\right].
```

Let

```math
N_{w,m}^{rec}
```

be the **case-authority-defined completed-trip/service target** for OD/service class `w` that must be achieved during interval `I_m` for the selected transportation recovery milestone to count as attained.

When that target is expressed on the same OD set, population/service class, temporal interval, spatial support, and weighting convention as `S_T`, define

```math
\boxed{
s_{T,\rm rec,m}
=
\frac{\sum_w\omega_w N_{w,m}^{rec}}
{\sum_w\omega_w\widehat N_{w,m}^{req}}.
}
```

with

```math
\boxed{
s_{T,m}^{\min}\le s_{T,\rm rec,m}\le1.}
```

The upper bound follows from the normalized service convention; it does **not** require `s_{T,rec}=1`.

This ratio is a thesis-derived mapping `[D]`. The external sources justify the recovery semantics and provenance rule, not the numerical fraction.

---

## 2.6 Non-substitutability guard for critical mobility

An aggregate recovered-service fraction can conceal failure of indispensable emergency or critical OD/service classes. Therefore, for non-substitutable recovery classes,

```math
\boxed{
N_{w,m}^{comp}\ge N_{w,m}^{rec},
\qquad
w\in\mathcal W_{\rm rec,hard}.
}
```

The transportation component of the recovery set should therefore be represented as

```math
\boxed{
G_{\rm rec}^{T}(t)
=
\left\{Y\in K(t):S_T(Y,t)\ge s_{T,\rm rec}(t)\right\}
\cap
\bigcap_{w\in\mathcal W_{\rm rec,hard}}
\left\{Y:N_w^{comp}\ge N_w^{rec}\right\}
\cap
\bigcap_q\left\{Y:g_q^{rec}(Y,t)\le0\right\}.
}
```

The optional native recovery constraints `g_q^{rec}` preserve authoritative requirements that are not naturally expressible as completed-trip fractions, such as:

- safe route availability;
- maximum access time to a critical facility;
- emergency-corridor operability;
- minimum transit headway/service frequency;
- another case-authority transportation requirement.

These constraints must remain in native units unless a validated transformation to `S_T` exists.

---

## 2.7 Functional recovery is not full physical restoration

The admitted NIST/FHWA evidence distinguishes restored function from complete physical restoration. Therefore H3 must not require

```math
\mathcal G_T(t)=\mathcal G_T(t_0)
```

or complete repair/reopening of every transportation component in order to declare functional recovery.

A post-event configuration may be different from the pre-event configuration while still delivering the required mobility service through rerouting, temporary capacity, modified transit service, or alternative modes.

Conversely,

```math
\text{component repaired/open}
\not\Rightarrow
\text{required mobility service recovered}.
```

Service recovery must be demonstrated through the declared `S_T`/native recovery requirements.

---

## 2.8 Persistent recovery and dwell condition

Temporary or modified service may stabilize a transportation lifeline before full service returns (FEMA, 2023). A one-step threshold crossing may therefore be insufficient when the engineering definition requires sustained recovery.

The frozen H3 dwell semantics remain admissible:

```math
\boxed{
Y_s\in G_{\rm rec}(s)
\quad
\forall s\in[\tau_G,\tau_G+\tau_{\rm dwell}].
}
```

The numerical dwell duration is **OPEN** and must be case-supported. No FEMA/NIST/FHWA source is used here to fabricate a universal dwell time.

---

## 2.9 Distinguish service level from recovery deadline

`S_T` and `s_{T,rec}` answer **how much transportation service must be restored**.

`T_R` answers **by when the recovery target must be reached**.

Therefore

```math
\boxed{
s_{T,\rm rec}\neq T_R.}
```

A source that specifies a recovery time but not a service level cannot by itself freeze `s_{T,rec}`. Likewise, a service target without a deadline cannot freeze `T_R`.

---

## 2.10 What must not be used directly as `s_{T,rec}`

The following are rejected as direct substitutes unless a validated transformation to the frozen service metric exists:

1. `S_T=1` merely because full recovery is a conceptual endpoint;
2. exact pre-event network-state equality;
3. percentage of roads/bridges reopened;
4. LOS category;
5. travel time or delay alone;
6. average speed alone;
7. component-repair percentage;
8. time to recovery itself;
9. arbitrary percentages selected from simulation studies.

These may remain independent recovery constraints or diagnostics when relevant, but they are not automatically equivalent to the completed/requested weighted-trip service fraction.

---

## 2.11 Units, scales, aggregation, and uncertainty

| Field | Qualified specification |
|---|---|
| Mathematical object | `s_{T,rec}(t)` or interval form `s_{T,rec,m}` |
| Physical meaning | minimum transportation-service level required to declare the selected recovery milestone achieved |
| Native requirement units | trips, persons, vehicles, transit runs/headway, route availability, travel time, or another authority-native mobility-service target |
| Thesis threshold units | dimensionless fraction `[0,1]` only after validated mapping to `S_T` |
| Structural relation | `s_{T,rec} ≥ s_T^{min}` when both use the same normalized service metric |
| Spatial scale | OD/service class/corridor first; system aggregation only after deterministic mapping and weighting |
| Temporal scale | case-specific recovery milestone interval; distinct from `T_R` |
| Aggregation | weighted completed trips relative to reconstructed requested trips when using `S_T` |
| Persistence | optional dwell condition when transient crossing is insufficient; numerical value OPEN |
| Uncertainty | OD-demand reconstruction, completed-trip observation, penetration/expansion, weighting, service-target uncertainty, temporal/spatial aggregation, and criticality classification |
| Validity domain | selected transportation system/mode, user/service class, hazard, operating state, spatial support, and recovery objective |

No probability distribution for `s_{T,rec}` is frozen. Any later probabilistic representation must be supported by case evidence.

---

## 2.12 EGMIV epistemic status

```text
[E] Transportation functional recovery is a distinct performance state from full recovery/full functionality.
[E] Transportation recovery objectives and metrics should reflect user needs, regional context, system type, and stakeholder/community requirements.
[E] Functional recovery can be achieved before complete physical/network restoration and may use modified or alternative service arrangements.
[E] Federal guidance reviewed here does not prescribe one universal transportation recovery fraction.
[D] A matched-support case-authority completed-trip target can be mapped into the frozen S_T metric as s_{T,rec}.
[D] G_rec ⊆ K implies s_{T,rec} ≥ s_T^{min} when both are scalar thresholds on the same service metric/support.
[D] Native recovery constraints not equivalent to completed-trip fraction should remain separate constraints in G_rec.
[A] The final case-specific N_{w,m}^{rec} targets and native recovery constraints are not yet selected.
[U] The numerical value of s_{T,rec} and any dwell duration remain open.
```

---

## 2.13 Qualification decision

```math
\boxed{
\begin{aligned}
\text{definition/provenance of }s_{T,\rm rec} &: \textbf{SUPPORTED},\\
\text{universal numerical value} &: \textbf{REJECTED},\\
\text{universal requirement }s_{T,\rm rec}=1 &: \textbf{REJECTED},\\
\text{case-specific numerical value} &: \textbf{OPEN},\\
\text{confirmatory-code admission} &: \textbf{BLOCKED UNTIL CASE EVIDENCE IS FROZEN}.
\end{aligned}
}
```

The scientifically admissible result is a provenance-constrained transportation recovery target that preserves critical mobility and native authority requirements without equating functional recovery to full physical restoration.

---

# 3. Next admissible object

```math
\boxed{F}
```

The next targeted qualification must define the Stage-5 hard-failure/avoid set from explicit safety, irreversibility, emergency-service, or non-recoverability criteria while preserving

```math
D(t)=K(t)^c\setminus F(t)\neq\varnothing
```

for degraded-but-recoverable states.

---

# References — APA 7

Abrahams, L., Van Pay, L., Sattar, S., Johnson, K., & McCabe, S. (2021). *NIST-FEMA post-earthquake functional recovery workshop report* (NIST SP 1269). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.1269

Beyzaei, C. Z., Johnson, K. J., Nikolaou, S., Sattar, S., Dukes, J., & Saadat, Y. (2023). *NIST transportation systems and functional recovery workshop report* (NIST SP 1295). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.1295

Federal Emergency Management Agency. (2016). *Emergency Support Function #1—Transportation Annex*. U.S. Department of Homeland Security.

Federal Emergency Management Agency. (2023). *Community Lifelines Toolkit* (Version 2.1). U.S. Department of Homeland Security.

Kourkoulis, R., Gelagoti, F., Chedid, M., Antoniou, M., Alvertos, A. E., Nikolaou, S., & Hung, C. J. (2024). *Improving transportation infrastructure resilience through post-event damage inspection (PDI) and post-event engineering investigation (PEI)* (FHWA-HIF-24-042). Federal Highway Administration.

