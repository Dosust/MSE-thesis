# H3 Threshold Evidence Qualification v2.0

**Status:** ACTIVE EVIDENCE QUALIFICATION  
**Date:** 2026-09-16  
**Protocol:** EGMIV–TSP  
**Thesis destination:** Chapter 3 → Stage 5 → RQ5/H3 → Chapter 4 H3 experiment  
**Structural authority:** `H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Prior qualification record:** `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V1.md`  
**Page-control authority:** `../thesis/00_governance/THESIS_PAGE_BUDGET_160_V1.md`

> This version preserves the v1 qualification of `s_P^{min}` and advances the registry through `s_T^{min}`. It does not change the frozen semantics of `K(t)`, `G_rec(t)`, `F(t)`, `T_V`, or `T_R`.

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
| `s_T^{min}` | **SUPPORTED** | **REJECTED** | **OPEN** | **BLOCKED** |
| `s_{P,rec}` | OPEN | OPEN | OPEN | BLOCKED |
| `s_{T,rec}` | OPEN | OPEN | OPEN | BLOCKED |
| `F` | OPEN | n/a | OPEN | BLOCKED |
| `T_V` | OPEN | REJECTED by structure | OPEN | BLOCKED |
| `T_R` | OPEN | REJECTED by structure | OPEN | BLOCKED |

---

# 2. Object Q1 — `s_P^{min}` — inherited result

The complete v1 evidence record remains authoritative in `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V1.md`.

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

No numerical value is imported from simulations, REopt examples, reliability indices, voltage/frequency limits, or arbitrary resilience percentages.

---

# 3. Object Q2 — `s_T^{min}`

## 3.1 Thesis role

The frozen transportation service observable is

```math
0\le S_T(Y,t)\le1,
```

with interval realization

```math
\boxed{
S_{T,m}
=
\min\left[
1,
\frac{\sum_w\omega_w N_{w,m}^{comp}}
{\sum_w\omega_w\widehat N_{w,m}^{req}}
\right].
}
```

The H3 service-admissibility condition permits

```math
S_T(Y,t)\ge s_T^{\min}(t).
```

The qualification question is therefore:

> What authoritative transportation evidence can define a minimum acceptable mobility-service level during disruption without converting LOS, travel time, delay, route status, or another native transport metric into an unsupported universal completed-trip fraction?

---

## 3.2 Targeted evidence-search boundary

The search was limited to authoritative U.S. Department of Transportation / Federal Highway Administration and FEMA sources addressing:

1. multimodal transportation performance and complete person trips;
2. objective-driven performance targets;
3. minimum/critical transportation service during disruptions;
4. emergency transportation lifeline stabilization; and
5. whether a universal transportation performance threshold exists.

Broad literature collection, unrelated resilience indices, and method shopping were excluded under EGMIV–TSP.

---

## 3.3 Qualified evidence

### E1 — FHWA multimodal system performance research

Sinclair and Schaefer's FHWA-sponsored multimodal performance study reports that its literature review found no universal multimodal transportation system performance measure or approach. The study develops a complete-person-trip perspective and treats completed person trips as transportation-system outputs; its proposed Multimodal System Productivity measure uses completed person trips relative to network travel time. The report also emphasizes that complete trip information is necessary for traveler-centered multimodal performance assessment (Sinclair & Schaefer, 2019).

**Evidence use:** directly supports the thesis choice to retain completed-trip service as a legitimate transportation performance object while rejecting any claim that a universal multimodal service threshold already exists.

### E2 — FHWA objectives-driven performance planning

FHWA guidance states that transportation performance measures are tied to specific operations objectives and should be developed according to the needs and resources of the agency. The same guidance lists person throughput as a valid performance family and shows that targets are objective-specific rather than universal constants (Grant et al., 2010).

**Evidence use:** supports deriving `s_T^{min}` from a declared agency/emergency mobility objective and its native target rather than choosing a generic percentage.

### E3 — USDOT/FHWA minimum-LOS boundary

The U.S. Department of Transportation states explicitly that FHWA does not have regulations or policies requiring specific minimum automobile Level of Service values. It also notes that traditional automobile-only LOS can be too narrow for broader transportation performance management goals (U.S. Department of Transportation [USDOT], 2017).

**Evidence use:** rejects LOS A–F or a particular LOS class as a federal universal substitute for `s_T^{min}`. LOS may remain a separate native constraint only when required by the selected case authority.

### E4 — FEMA Community Lifelines transportation semantics

FEMA defines transportation as a Community Lifeline and uses an objectives-based response construct focused on rapid stabilization of lifeline services. The Community Lifelines Toolkit transportation example shows route clearance to critical facilities, modified mass-transit schedules as roads become passable, and temporary/micro-transit alternatives before full service resumes (Federal Emergency Management Agency [FEMA], 2023).

**Evidence use:** supports two important Stage-5 semantics: (i) critical mobility is function/route specific, and (ii) acceptable or stabilized emergency service need not equal full pre-event transportation service. The FEMA example does not provide a universal completed-trip percentage and therefore cannot numerically freeze `s_T^{min}`.

### E5 — FEMA ESF #1 transportation continuity

The FEMA Emergency Support Function #1 Transportation Annex states that emergency transportation decisions must sustain transportation services, meet societal needs, support movement of emergency relief personnel and commodities, and identify temporary alternative transportation solutions when primary systems are damaged, unavailable, or overwhelmed (Federal Emergency Management Agency [FEMA], 2016).

**Evidence use:** supports defining critical mobility/service requirements from emergency functions and required movements rather than from a universal network-wide percentage.

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
| Sinclair & Schaefer (2019), FHWA-HOP-18-085 | PASS | PASS | PASS | PASS — FHWA technical report | PASS | National multimodal measurement research; admitted for measure semantics and non-universality, not a numeric threshold | **ADMIT** |
| Grant et al. (2010), FHWA-HOP-10-026 | PASS | PASS | PASS | PASS — FHWA guidebook | PASS | Agency/region objective-driven planning; admitted for target-selection principle | **ADMIT** |
| USDOT (2017), LOS case studies | PASS | PASS | PASS | PASS — official USDOT policy page | PASS | Automobile LOS only; admitted to reject universal LOS substitution | **ADMIT WITH SCOPE LIMIT** |
| FEMA (2023), Community Lifelines Toolkit 2.1 | PASS | PASS | PASS | PASS — federal emergency-management doctrine/toolkit | PASS | Disaster-response lifeline stabilization; admitted for critical/modified service semantics | **ADMIT** |
| FEMA (2016), ESF #1 Transportation Annex | PASS | PASS | PASS | PASS — National Response Framework annex | PASS | Emergency transportation management; admitted for critical-function/service continuity principle | **ADMIT** |

### Search result boundary

No admitted source establishes a universal value such as

```math
s_T^{\min}=0.50,
0.75,
0.80,
0.90,
0.95,
\text{or }1.00
```

for the fraction of requested weighted OD trips that must be completed across all transportation systems, hazards, service classes, spatial scales, or time windows.

Therefore a universal numerical `s_T^{min}` is **rejected**.

---

## 3.5 Mathematical translation into the frozen service metric

Let

```math
N_{w,m}^{min}
```

be the **documented minimum number of completed trips required** for OD/service class `w` during interval `I_m`, obtained from the selected transportation/emergency authority or derived through a validated transformation from an authoritative native requirement.

When the requirement is expressed on the same OD set, temporal interval, population/service class, and weighting convention as `S_T`, define

```math
\boxed{
s_{T,m}^{\min}
=
\frac{\sum_w\omega_w N_{w,m}^{min}}
{\sum_w\omega_w\widehat N_{w,m}^{req}}
}
```

subject to

```math
0\le N_{w,m}^{min}\le\widehat N_{w,m}^{req}.
```

Then

```math
S_{T,m}\ge s_{T,m}^{\min}
```

means that the weighted number of completed trips meets or exceeds the documented minimum mobility requirement over the declared support.

This ratio is a **thesis-derived mapping `[D]`**, not a value copied from FHWA or FEMA.

### Case of a native percentage requirement

If a qualified case authority directly specifies that at least `q_w` of a defined requested critical-trip class must be completed over interval `I_m`, then

```math
N_{w,m}^{min}=q_w\widehat N_{w,m}^{req}
```

may be admitted, with uncertainty and validity domain preserved.

### Case of a different native metric

If the authoritative requirement is instead stated as:

- maximum travel time or delay;
- minimum corridor throughput;
- route passability/access status;
- evacuation completion deadline;
- transit headway or schedule reliability;
- minimum emergency-access speed;
- Level of Service;

it is **not** automatically converted into `s_T^{min}`.

It may enter `K_svc`, `K_phys`, or `K_op` as its own native constraint, or be mapped into `s_T^{min}` only through a validated transformation with uncertainty propagation.

---

## 3.6 Non-substitutability guard for critical OD/service classes

An aggregate trip-completion ratio can hide failure of an indispensable route or OD class. Completing many discretionary trips must not compensate mathematically for failure to move emergency responders, patients, evacuation populations, repair crews, or other declared critical users.

Therefore, for a set of non-substitutable critical OD/service classes `\mathcal W_{hard}`, impose

```math
\boxed{
N_{w,m}^{comp}\ge N_{w,m}^{min},
\qquad
w\in\mathcal W_{hard}.
}
```

The power and transportation service constraints are then structurally parallel:

```math
\boxed{
K_{svc}^{P}:
S_P\ge s_P^{min}
\ \land\
E_i^{srv}\ge E_i^{req}\ \forall i\in\mathcal C_{hard},
}
```

```math
\boxed{
K_{svc}^{T}:
S_T\ge s_T^{min}
\ \land\
N_w^{comp}\ge N_w^{min}\ \forall w\in\mathcal W_{hard}.
}
```

This prevents aggregate-service compensation from violating critical-function requirements.

---

## 3.7 What must not be used directly as `s_T^{min}`

The following are rejected as direct numerical substitutes unless a validated mapping to the frozen completed/requested weighted OD-trip metric is established:

1. Level of Service A–F;
2. volume-to-capacity ratio;
3. posted or observed speed;
4. travel-time index or planning-time index;
5. travel delay;
6. percentage of roads open;
7. pavement/bridge condition ratings;
8. route-clearance status;
9. transit on-time performance;
10. evacuation time/deadline;
11. an arbitrary percentage used in a published resilience simulation.

These may remain valid engineering quantities, but metric validity does not imply metric interchangeability.

---

## 3.8 Units, scales, aggregation, and uncertainty

| Field | Qualified specification |
|---|---|
| Mathematical object | `s_T^{min}(t)` or interval form `s_{T,m}^{min}` |
| Physical meaning | minimum acceptable transportation-service fraction implied by documented critical-trip/mobility requirements |
| Native requirement units | completed persons/trips per interval, persons/hour, vehicles/hour, travel time, route status, or other authority-native quantity |
| Thesis threshold units | dimensionless fraction `[0,1]` only after validated mapping to `S_T` |
| Spatial scale | OD pair/service class/corridor first; network aggregation only after deterministic mapping |
| Temporal scale | authority-native emergency/service window; mapped to the H3 validation/decision interval without false upsampling |
| Aggregation | weighted completed critical trips relative to counterfactual requested trips on matched spatial/temporal support |
| Uncertainty | OD-demand reconstruction, trip-completion observation, probe/penetration/expansion error, weighting/classification, time alignment, spatial coverage, and requirement uncertainty |
| Validity domain | selected transportation system, user/service classes, hazard/event, spatial support, operating regime, and declared time window |

No probability distribution for `s_T^{min}` is frozen here. Any future distribution must come from case evidence or a defensible uncertainty model.

---

## 3.9 EGMIV epistemic status

```text
[E] FHWA found no universal multimodal transportation-system performance measure/approach in the reviewed literature.
[E] FHWA treats completed person trips as a legitimate multimodal system output and develops person-trip-based performance measures.
[E] FHWA guidance ties transportation performance measures and targets to declared operations objectives and agency needs.
[E] USDOT states that FHWA has no regulation or policy requiring a specific minimum automobile LOS value.
[E] FEMA treats transportation as a critical lifeline and recognizes modified/alternative service before full service is restored.
[E] FEMA ESF #1 emphasizes sustaining transportation services and temporary alternatives during disruptions.
[D] A documented minimum critical-trip requirement can be normalized to the frozen S_T metric only when spatial, temporal, population, and weighting supports are compatible.
[D] Non-substitutable critical OD/service classes require native constraints in addition to the aggregate S_T threshold.
[A] The final case authority, critical OD classes, and required completed-trip quantities remain to be selected.
[U] The numerical value of s_T^{min} remains open.
```

---

## 3.10 Qualification decision

```math
\boxed{
\begin{aligned}
\text{definition/provenance of }s_T^{\min} &: \textbf{SUPPORTED},\\
\text{universal numerical value} &: \textbf{REJECTED},\\
\text{case-specific numerical value} &: \textbf{OPEN},\\
\text{confirmatory-code admission} &: \textbf{BLOCKED UNTIL CASE EVIDENCE IS FROZEN}.
\end{aligned}
}
```

The scientifically valid result is a provenance-constrained rule for deriving `s_T^{min}` from a case-specific transportation/emergency mobility requirement. No universal percentage is invented.

---

## 3.11 Service-requirement gate status for `s_T^{min}`

```text
Authority class identified:                 PASS in principle; final case authority OPEN
Native quantity family identified:          PASS (critical completed trips / throughput / other native mobility requirement)
Context requirement identified:             PASS; final case context OPEN
Target semantics identified:                PASS
Direct mapping to frozen S_T:                CONDITIONAL on matched OD/time/population/weighting support
Tolerance/materiality band:                 OPEN / not required merely to define K_svc
Temporal mapping rule:                      PASS; numerical interval OPEN
Spatial mapping rule:                       PASS; final critical OD/service classes OPEN
Provenance requirement:                     PASS
Pre-confirmatory numerical freeze:          NOT PASSED
```

Therefore `s_T^{min}` is structurally qualified but not numerically frozen.

---

# 4. Consequence for the H3 acceptable set

At this stage the service component of the acceptable set can be written structurally as

```math
\boxed{
K_{svc}(t)
=
K_{svc}^{P}(t)
\cap
K_{svc}^{T}(t),
}
```

with

```math
K_{svc}^{P}(t)
=
\left\{
Y:
S_P(Y,t)\ge s_P^{min}(t),
\ E_i^{srv}(t)\ge E_i^{req}(t)\ \forall i\in\mathcal C_{hard}
\right\},
```

and

```math
K_{svc}^{T}(t)
=
\left\{
Y:
S_T(Y,t)\ge s_T^{min}(t),
\ N_w^{comp}(t)\ge N_w^{min}(t)\ \forall w\in\mathcal W_{hard}
\right\}.
```

The structure is admissible; the case-specific threshold values are not yet admissible for confirmatory execution.

---

# 5. Next admissible object

```math
\boxed{s_{P,\rm rec}}
```

The next targeted qualification must determine what constitutes **sufficiently recovered power service** and whether recovery should be expressed as return to the minimum acceptable set, a stricter critical-load target, a pre-event service level, or another documented operator/service requirement. It must not assume that recovery equals `S_P=1`.

---

# References — APA 7

Federal Emergency Management Agency. (2016). *Emergency Support Function #1—Transportation Annex*. U.S. Department of Homeland Security. https://www.fema.gov/sites/default/files/2020-07/fema_ESF_1_Transportation.pdf

Federal Emergency Management Agency. (2023). *Community Lifelines Implementation Toolkit* (Version 2.1). U.S. Department of Homeland Security. https://www.fema.gov/sites/default/files/documents/fema_lifelines-toolkit-v2.1_2023.pdf

Grant, M., Bauer, J., Plaskon, T., & Mason, J. (2010). *Advancing metropolitan planning for operations: An objectives-driven, performance-based approach—A guidebook* (FHWA-HOP-10-026). Federal Highway Administration. https://ops.fhwa.dot.gov/publications/fhwahop10026/

Sinclair, C., & Schaefer, R. (2019). *Multimodal system performance measures research and application: Innovation and research plan* (FHWA-HOP-18-085). Federal Highway Administration. https://ops.fhwa.dot.gov/publications/fhwahop18085/

U.S. Department of Transportation. (2017). *Level of service case studies: Evolving use of level of service metrics in transportation analysis*. https://www.transportation.gov/office-policy/transportation-policy/level-service-case-studies

