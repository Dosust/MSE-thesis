# H3 Threshold Evidence Qualification v3.0

**Status:** ACTIVE EVIDENCE QUALIFICATION  
**Date:** 2026-09-16  
**Protocol:** EGMIV–TSP  
**Thesis destination:** Chapter 3 → Stage 5 → RQ3/H3 → Chapter 4 H3 experiment  
**Structural authority:** `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Prior qualification records:** `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V1.md`, `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V2.md`  
**Page-control authority:** `../thesis/00_governance/THESIS_PAGE_BUDGET_160_V1.md`

> This version preserves the prior qualification of `s_P^{min}` and `s_T^{min}` and advances the registry through `s_{P,rec}`. It does not alter the frozen semantics of `K(t)`, `G_rec(t)`, `F(t)`, `T_V`, or `T_R`.

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

Current status:

| Object | Definition/provenance | Universal numerical value | Case-specific numerical value | Confirmatory admission |
|---|---|---|---|---|
| `s_P^{min}` | SUPPORTED | REJECTED | OPEN | BLOCKED |
| `s_T^{min}` | SUPPORTED | REJECTED | OPEN | BLOCKED |
| `s_{P,rec}` | **SUPPORTED** | **REJECTED** | **OPEN** | **BLOCKED** |
| `s_{T,rec}` | OPEN | OPEN | OPEN | BLOCKED |
| `F` | OPEN | n/a | OPEN | BLOCKED |
| `T_V` | OPEN | REJECTED by structure | OPEN | BLOCKED |
| `T_R` | OPEN | REJECTED by structure | OPEN | BLOCKED |

---

# 2. Inherited results — `s_P^{min}` and `s_T^{min}`

The complete evidence records remain in v1 and v2. Their current qualified status is:

```math
\boxed{
\begin{aligned}
\text{definition/provenance} &: \textbf{SUPPORTED},\\
\text{universal numerical value} &: \textbf{REJECTED},\\
\text{case-specific numerical value} &: \textbf{OPEN},\\
\text{confirmatory-code admission} &: \textbf{BLOCKED UNTIL CASE EVIDENCE IS FROZEN}.
\end{aligned}
}
```

No numerical value may be imported from a simulation, generic benchmark, or unrelated reliability/performance metric.

---

# 3. Object Q3 — `s_{P,rec}`

## 3.1 Thesis role

The frozen H3 recovery target satisfies

```math
\boxed{G_{\rm rec}(t)\subseteq K(t).}
```

Its power-service component may be written

```math
S_P(Y,t)\ge s_{P,\rm rec}(t).
```

The qualification question is therefore:

> What evidence can define a sufficiently recovered electrical-service target without assuming that recovery universally means `S_P=1`, exact return to the pre-event state, or complete restoration of every noncritical load?

This is distinct from `s_P^{min}`:

- `s_P^{min}` defines the minimum service required for acceptable operation in `K_svc`;
- `s_{P,rec}` defines the stricter or otherwise explicitly declared service milestone that makes a state admissible as a recovery target in `G_rec`.

Because `G_rec ⊆ K`, the same-metric scalar thresholds must satisfy

```math
\boxed{s_{P,\rm rec}(t)\ge s_P^{\min}(t)}
```

whenever both constraints are evaluated on the same service metric and support.

---

## 3.2 Targeted evidence-search boundary

The search was restricted to sources directly addressing one or more of the following:

1. power-system post-event recovery/restoration;
2. infrastructure performance targets during recovery;
3. critical-load restoration;
4. energy-lifeline stabilization/re-establishment; and
5. whether full or pre-event restoration is universally required to declare recovery.

Sources were restricted to peer-reviewed infrastructure-resilience research and authoritative DOE/NREL/FEMA materials. Method shopping and broad resilience-literature collection were excluded under EGMIV–TSP.

---

## 3.3 Qualified evidence

### E1 — Infrastructure resilience performance targets are not universally equivalent to full pre-event restoration

Poulin and Kane's critical review of 273 infrastructure-resilience publications shows that recovery curves depend on the selected performance measure, normalization reference, scenario, and stakeholder goal. They explicitly note that full restoration may not be possible and that endogenous performance targets may be appropriate when full recovery is infeasible; performance targets and thresholds require stakeholder engagement and validation (Poulin & Kane, 2021).

**Evidence use:** supports rejecting `s_{P,rec}=1` as a universal rule and supports a case-/scenario-/stakeholder-specific recovery target.

### E2 — Energy-resilience metrics and recovery criteria are context specific

NREL states that no single energy-resilience metric applies broadly; appropriate metrics depend on goals, event context, hazard, scale, and perspective. NREL lists load not served, critical services without power, and time to recovery among valid performance-based resilience measures (Anderson et al., 2019).

**Evidence use:** supports defining the power recovery target from the selected engineering objective and critical-service context rather than from an arbitrary universal fraction.

### E3 — Critical-load restoration is a prioritized service-restoration problem

Zhang et al. formulate distribution-system critical-load restoration as a sequential restoration problem in which critical loads carry priority weights and the objective is to restore those loads rapidly and reliably under network and generation constraints (Zhang et al., 2021).

**Evidence use:** supports representing recovery through priority-weighted restoration of critical electrical service. This source does **not** provide a universal numerical `s_{P,rec}` and is admitted for restoration semantics/model structure only.

### E4 — FEMA distinguishes stabilization from complete permanent restoration

FEMA's Community Lifelines doctrine states that stabilization occurs when basic lifeline services are provided either through rapid re-establishment or contingency solutions. Stabilization may rely on temporary measures; for the energy lifeline, temporary generators at critical facilities are an explicit example. Re-establishment is a longer-term condition in which normal lifeline service providers are again available through emergency repairs or other means (Federal Emergency Management Agency [FEMA], 2023).

**Evidence use:** establishes that a meaningful emergency-service recovery milestone may be below complete pre-event restoration and may be defined by restored critical functions. It also motivates distinguishing transient threshold crossing from sustained recovery.

### E5 — Power-system resilience lacks a universally accepted recovery/evaluation metric

Yao, Liu, and Jain identify the lack of universally accepted power-system resilience metrics/evaluation methods and distinguish post-event resilience evaluation from pre-event estimation (Yao et al., 2022).

**Evidence use:** reinforces rejection of a universal numerical recovery fraction independent of case and metric definition.

---

## 3.4 Source-qualification gate

For source `q`, apply

```math
G_S^{(q)}
=
G_I\land G_R\land G_C\land G_Q\land G_M\land G_V.
```

| Source | Identity | Relevance | Claim support | Authority/quality | Metadata | Validity-domain treatment | Admission |
|---|---|---|---|---|---|---|---|
| Poulin & Kane (2021) | PASS | PASS | PASS | PASS — peer-reviewed critical review | PASS | Cross-infrastructure; admitted for target/recovery semantics, not a power-specific numerical value | **ADMIT** |
| Anderson et al. (2019) | PASS | PASS | PASS | PASS — NREL technical guidance | PASS | Energy resilience; context dependence explicit | **ADMIT** |
| Zhang et al. (2021) | PASS | PASS | PASS | PASS — peer-reviewed IEEE/NREL paper | PASS | Distribution critical-load restoration; admitted for prioritized-restoration semantics only | **ADMIT WITH SCOPE LIMIT** |
| FEMA (2023) Community Lifelines Toolkit 2.1 | PASS | PASS | PASS | PASS — federal emergency-management doctrine/toolkit | PASS | Emergency lifeline stabilization/re-establishment; admitted for recovery-milestone semantics | **ADMIT** |
| Yao et al. (2022) | PASS | PASS | PASS | PASS — NREL/IEEE review framework | PASS | Power-system resilience evaluation; admitted for non-universality/evaluation structure | **ADMIT** |

### Search result boundary

No admitted source establishes a universal requirement such as

```math
s_{P,\rm rec}=0.80,
0.90,
0.95,
\text{or }1.00
```

for every power system, critical-service class, hazard, spatial scale, and recovery objective.

Therefore a universal numerical `s_{P,rec}` is **rejected**.

---

## 3.5 Mathematical translation into the frozen service metric

For validation/recovery interval `I_m`, recall the frozen service metric

```math
S_{P,m}
=
\frac{\sum_i\omega_i E_{i,m}^{srv}}
{\sum_i\omega_i\widehat E_{i,m}^{d}}.
```

Let

```math
E_{i,m}^{rec}
```

be the **case-authority-defined electrical service target** for entity/service class `i` that must be restored for the system to count as sufficiently recovered during interval `I_m`.

When this target is defined on the same spatial, temporal, demand, and weighting support as `S_P`, define

```math
\boxed{
s_{P,\rm rec,m}
=
\frac{\sum_i\omega_i E_{i,m}^{rec}}
{\sum_i\omega_i\widehat E_{i,m}^{d}}.
}
```

with the structural consistency condition

```math
\boxed{
s_{P,m}^{\min}\le s_{P,\rm rec,m}\le1.}
```

The upper bound `1` follows from the normalized service convention; it does **not** assert that the case-specific recovery target must equal `1`.

### Recovery-set contribution

The power-service component of the recovery target becomes

```math
G_{\rm rec}^{P}(t)
=
\left\{
Y\in K(t):
S_P(Y,t)\ge s_{P,\rm rec}(t),
\ \text{plus required native critical-load constraints}
\right\}.
```

---

## 3.6 Non-substitutability and critical-function recovery guard

An aggregate recovery fraction must not allow excess restoration of noncritical loads to compensate for failure to recover an indispensable critical function.

For non-substitutable critical entities, require

```math
\boxed{
E_{i,m}^{srv}\ge E_{i,m}^{rec},
\qquad i\in\mathcal C_{\rm rec,hard}.
}
```

Therefore the recovery target should generally be represented as an intersection:

```math
\boxed{
G_{\rm rec}^{P}(t)
=
\left\{Y\in K(t):S_P\ge s_{P,\rm rec}\right\}
\cap
\bigcap_{i\in\mathcal C_{\rm rec,hard}}
\left\{Y:E_i^{srv}\ge E_i^{rec}\right\}.
}
```

This is a thesis-derived formulation `[D]` that preserves the authority-native critical-load requirements rather than collapsing them into one scalar.

---

## 3.7 Stabilization is not automatically persistent recovery

FEMA distinguishes temporary contingency stabilization from longer-term re-establishment of lifeline services (FEMA, 2023). A trajectory that touches the recovery target for one numerical time step may therefore be inadequate evidence of sustained recovery.

The already-frozen H3 specification permits a dwell condition:

```math
\boxed{
Y_s\in G_{\rm rec}(s)
\quad
\forall s\in[\tau_G,\tau_G+\tau_{\rm dwell}].
}
```

For `s_{P,rec}`, this means that when the engineering case requires persistent recovery, the recovery threshold must be maintained for a case-supported dwell interval. The numerical value of `\tau_{\rm dwell}` remains **OPEN**; FEMA's doctrine supports the semantic distinction, not a universal duration.

---

## 3.8 What must not be used directly as `s_{P,rec}`

The following are rejected as direct substitutes unless a validated mapping to the frozen service metric exists:

1. `S_P=1` merely because many idealized resilience curves return to nominal performance;
2. exact pre-event state equality `Y(t)=Y(t_0)`;
3. voltage/frequency limits, which belong in `K_phys`;
4. SAIDI/SAIFI or customer interruption counts;
5. time to recovery, which is a temporal metric rather than the recovery service level;
6. arbitrary percentages from published simulations;
7. the fraction of network components physically repaired if service restoration is not demonstrated.

A power system can meet an authority-defined recovery service target while remaining in a different physical configuration from the pre-event state. Conversely, repaired infrastructure does not by itself prove that the required service has been restored.

---

## 3.9 Units, scales, aggregation, and uncertainty

| Field | Qualified specification |
|---|---|
| Mathematical object | `s_{P,rec}(t)` or interval form `s_{P,rec,m}` |
| Physical meaning | minimum power-service level required to declare the selected recovery milestone achieved |
| Native requirement units | kW, kWh, critical-load profile, critical-service availability, or another authority-native electrical-service target |
| Thesis units | dimensionless fraction `[0,1]` after validated mapping to `S_P` |
| Structural relation | `s_{P,rec} ≥ s_P^{min}` when both use the same normalized service metric |
| Spatial scale | critical load/facility/entity first; aggregation only after deterministic mapping and weighting |
| Temporal scale | case-specific recovery interval/milestone; distinct from `T_R` |
| Aggregation | must match the service observable; interval energy when observations are interval-energy data |
| Persistence | optional dwell condition when transient crossing is insufficient; numerical dwell time OPEN |
| Uncertainty | recovery-target uncertainty + meter/model error + demand-baseline error + temporal/spatial aggregation + criticality classification |
| Validity domain | selected case, hazard, critical-service class, operating mode, spatial support, and declared recovery objective |

No probability distribution for `s_{P,rec}` is frozen. If the recovery target is uncertain, its uncertainty representation must be supported by case evidence rather than imposed for solver convenience.

---

## 3.10 EGMIV epistemic status

```text
[E] Power/infrastructure resilience recovery targets and metrics are context- and stakeholder-dependent rather than universally fixed.
[E] Full restoration may be infeasible in some resilience analyses; performance targets can therefore differ from nominal/pre-event performance.
[E] Critical-load restoration is a recognized power-system restoration objective and may prioritize loads by criticality.
[E] Emergency lifeline stabilization can be achieved through temporary or partial service solutions before complete permanent restoration.
[D] For the frozen normalized S_P metric, an authority-defined recovered-energy/service target can be mapped to s_{P,rec} by a matched-support ratio.
[D] G_rec ⊆ K implies s_{P,rec} ≥ s_P^{min} when both are scalar thresholds on the same S_P metric.
[A] The final case-specific E_{i,m}^{rec} profile/value is not yet selected.
[U] The numerical value of s_{P,rec} and any dwell duration remain open.
```

---

## 3.11 Qualification decision

```math
\boxed{
\begin{aligned}
\text{definition/provenance of }s_{P,\rm rec} &: \textbf{SUPPORTED},\\
\text{universal numerical value} &: \textbf{REJECTED},\\
\text{case-specific numerical value} &: \textbf{OPEN},\\
\text{universal requirement }s_{P,\rm rec}=1 &: \textbf{REJECTED},\\
\text{confirmatory-code admission} &: \textbf{BLOCKED UNTIL CASE EVIDENCE IS FROZEN}.
\end{aligned}
}
```

The scientifically admissible result is therefore a provenance-constrained recovery-target rule, not a guessed percentage and not an automatic return-to-one assumption.

---

# 4. Next admissible object

```math
\boxed{s_{T,\rm rec}}
```

The next targeted qualification must determine what counts as sufficiently recovered transportation service, preserving the distinction between restored critical mobility and full pre-event mobility and without converting travel time, LOS, route availability, or other native transportation metrics into a completed-trip recovery fraction unless a validated mapping exists.

---

# References — APA 7

Anderson, K., Hotchkiss, E., & Murphy, C. (2019). *Valuing resilience in electricity systems* (NREL/FS-7A40-74673; revised 2022). National Renewable Energy Laboratory. https://www.nrel.gov/docs/fy19osti/74673.pdf

Federal Emergency Management Agency. (2023). *Community lifelines implementation toolkit* (Version 2.1). U.S. Department of Homeland Security. https://www.fema.gov/sites/default/files/documents/fema_lifelines-toolkit-v2.1_2023.pdf

Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926

Yao, Y., Liu, W., & Jain, R. (2022). *Power system resilience evaluation framework and metric review: Preprint* (NREL/CP-5D00-80817). Presented at the IEEE PES Innovative Smart Grid Technologies Conference (ISGT NA). https://www.nrel.gov/docs/fy22osti/80817.pdf

Zhang, X., Eseye, A., Reynolds, M., Knueven, B., & Jones, W. (2021). Restoring critical loads in resilient distribution systems using a curriculum learned controller. Paper presented at the 2021 IEEE Power & Energy Society General Meeting (PESGM). https://doi.org/10.1109/PESGM46819.2021.9637834
