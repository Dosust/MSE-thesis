# Road vs Rail Scope-Gate Decision V1

**Status:** WORKING-FROZEN SCOPE DECISION  
**Date:** 2026-10-06  
**Purpose:** Resolve the open transport-mode decision using the five canonical scope gates rather than intuition.

## 1. Candidates

### Candidate A — Battery-electric road transportation

System class:

```text
Road transport
→ battery-electric road vehicles
→ grid-connected EV charging
```

Core reciprocal electrification mechanism:

```text
P → T:
electric power availability
→ charging capability
→ vehicle energy state / availability
→ mobility service

T → P:
vehicle arrivals + SOC + trip demand
→ charging demand
→ distribution-network loading
```

V2G is not required for this reciprocal interdependency.

### Candidate B — Electric rail transportation

System class:

```text
Rail transport
→ electric traction
→ traction power supply / overhead contact system
```

Core mechanism:

```text
P → T:
traction electrical supply
→ train traction capability
→ rail service

T → P:
train traction demand / regenerative energy
→ traction-network / upstream electrical loading
```

## 2. Decision rule

The five canonical gates are applied with equal decision weight:

1. RQ relevance
2. service relevance
3. physical measurability
4. data/model feasibility
5. Master's tractability

Scoring scale:

- 5 = direct, strong, well-supported
- 4 = strong with one material limitation
- 3 = feasible but significant limitation
- 2 = weak / indirect
- 1 = unsupported for active thesis scope

The score is **decision support**, not a scientific result.

## 3. Evidence matrix

| Gate | Battery-electric road transport | Electric rail | Evidence-based interpretation |
|---|---:|---:|---|
| RQ relevance | 5 | 5 | Both provide direct electricity-based P–T dependence and time-varying operation. |
| Service relevance | 4 | 5 | Rail has immediately interpretable train/passenger delay and cancellation metrics. Road mobility service is strong but must be bounded to a population such as fleet, depot, or charging corridor. |
| Physical measurability | 5 | 5 | Road: ambient/rectifier temperature, offered/delivered charger power, SOC and charging duration have field evidence. Rail: contact-wire current/temperature and catenary thermal states have experimental and validated models. |
| Data/model feasibility | 5 | 3 | Road has public charging-session and travel datasets plus standard distribution test systems. Rail has strong operational open data, but traction electrical/thermal datasets are less accessible and some published railway thermal studies report confidential case data. |
| Master's tractability | 5 | 3 | Road can be bounded to one feeder–EVCS–fleet/corridor mechanism. A rigorous rail study rapidly expands to traction network, train timetable/control, catenary thermal state, restoration and service operations. |
| **Total** | **24/25** | **21/25** | Both pass scientifically; road is currently stronger for a bounded MSE thesis. |

## 4. Road evidence

### Temperature-aware coupled-network modeling already exists

Li & Chang (2024) model:

```text
ambient temperature
→ EV energy use
→ SOC / charging demand
→ EVCS load
→ distribution network
```

Therefore temperature-sensitive road-EV coupling is not itself novel.

### Extreme-heat EVCS resilience control already exists

Bai et al. (2025) study distribution-network resilience under extreme heat using EVCS coordination and V2G. Their extreme-heat representation primarily constrains main-grid supply and increases load demand; EVCS actions are based on schedulable power boundaries and DRL control.

This is important because:

```text
extreme-heat EVCS control exists
```

but it does not establish a charger thermal-state model such as:

```text
T_amb(t)
→ T_rectifier(t)
→ P_EVSE^max(t)
→ charging delay / vehicle availability
→ mobility service
```

### Direct charger thermal evidence exists

Field measurements in a hot-climate fast-charging study show:
- thermally induced charger derating;
- strong relation between rectifier temperature and offered power;
- longer charging duration under peak summer conditions;
- distinction between charger-limited and battery-limited operation.

This provides a measurable physical mechanism for the thesis.

### Dynamic CPTN resilience already exists

Ma et al. (2026) already develop:
- PDN restoration;
- dynamic traffic and energy assignment;
- V2G-supported restoration;
- resilient pricing;
- endogenous traffic–power coupling.

Therefore restoration and dynamic road CPTN coupling are not novelty claims.

## 5. Rail evidence

### Strong direct electrical dependence

Bellè et al. (2022) model interdependent railway, traction-power and external-power networks and show cascading effects across the coupled systems.

A separate Great Britain rail resilience study shows that failure of critical traction-power assets can produce large train disruptions and passenger-delay consequences.

### Strong thermal physics

Fu et al. (2022) develop and experimentally validate an electro-thermal contact-wire model:

```math
m C_p \frac{dT}{dt}
=
q_j + q_s - q_r - q_c
```

This directly represents:
- Joule heating;
- solar heat absorption;
- radiative loss;
- convective loss.

Mahairi et al. (2024) further develop thermal models for DC railway conductors and traction-network hosting capacity in multi-train environments.

### Heat-related service evidence

Observed railway heat incidents include:
- track buckling;
- overhead-line sag;
- electrical equipment failures;
- service disruption and delays.

### Resilience saturation

A 2026 Applied Energy railway study already integrates:
- risk-aware planning;
- emergency energy management;
- adaptive train control;
- black start;
- full restoration;
- energy-security and transportation-service objectives.

This architecture is already very close to:

```text
Improve → Adapt → Restore
```

although it is not specifically an extreme-heat physical-state study.

## 6. Novelty-risk comparison

### Road branch

Already covered:
- ambient-temperature EV demand;
- CPTN charging-load prediction;
- extreme-heat EVCS resilience control;
- dynamic CPTN restoration.

Candidate unresolved handoff:

```text
charger / interface thermal state
→ time-varying charging capability
→ mobility + electricity service
→ engineering action effectiveness
```

### Rail branch

Already covered:
- interdependent railway–power vulnerability;
- contact-wire electro-thermal physics;
- thermal hosting capacity;
- railway service resilience;
- planning + adaptation + restoration.

Candidate unresolved handoff:

```text
extreme-heat thermal state
→ traction capability
→ rail service resilience
```

but this sits closer to several already-developed rail models and requires more specialized data.

## 7. Working decision

### Selected transport mode

```text
Road transport
→ battery-electric road transportation
```

### Selected dependency architecture

```text
battery-mediated electric mobility
through grid-connected EV charging
```

### Status

**WORKING-FROZEN**

This selection is for the active thesis workstream and presentation development. It does not yet freeze the exact charging-site context.

## 8. What is still open

The following are **not** resolved by this decision:

- public DC fast charging vs fleet/depot charging;
- wired vs wireless charging;
- exact EVSE component thermal state;
- exact feeder/grid state;
- exact mobility service metric;
- exact electricity service metric;
- adaptation control;
- restoration definition;
- whether V2G is excluded or used only as a comparator.

## 9. Why road is selected

The reason is **not** that road has a stronger electrical dependency than rail.

Rail actually provides a stronger immediate traction dependency.

Road is selected because it provides the stronger overall combination of:

```text
direct electrification coupling
+ measurable heat-dependent physical states
+ accessible data
+ controllable Master's scope
+ remaining physics-to-service handoff
```

This distinction must be preserved.

## 10. Reopen conditions

Reopen this decision only if:

1. full-text evidence shows the candidate road physics-to-service handoff is already comprehensively resolved;
2. required charger/transport data prove inaccessible;
3. the selected road model cannot be reduced to a Master's-scale experiment;
4. supervisor/chair/committee instruction changes the scope;
5. a rail dataset/model opportunity materially changes feasibility.

## 11. Next decision

Apply the same scope-gate method to:

```text
public DC fast charging
vs.
fleet/depot charging
```

Then freeze:
- exact charging context;
- physical state variables;
- Q_P(t);
- Q_T(t).
