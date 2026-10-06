# E-CPTN-TEMP-001 — Li & Chang (2024)

**Status:** ADMITTED — CLOSEST OPEN-ACCESS TEMPERATURE-AWARE ROAD-EV CPTN COMPARATOR  
**Date reviewed:** 2026-10-06  
**Source type:** Peer-reviewed, open-access journal article  
**Primary use:** novelty-boundary control; temperature → EV energy consumption → SOC/charging demand → distribution-network load; controlled comparator design

## Source

Benxin Li & Xuanming Chang (2024),  
"EV Charging Station Load Prediction in Coupled Urban Transportation and Distribution Networks,"  
*Energy Engineering*, 121(10), 3001–3018.  
DOI: 10.32604/ee.2024.051332.

## 1. Why this paper is close to the thesis

This study already contains all of the following in one coupled road-EV / distribution-network model:

- dynamic urban transportation network;
- EV routing;
- ambient-temperature effect;
- EV power consumption;
- SOC / charging-demand consequence;
- charging-station load aggregation;
- transportation–distribution coupling through charging stations;
- dynamic charging-price intervention;
- security-constrained distribution-network thresholds.

Therefore, the thesis must **not** claim that linking ambient temperature to EV charging demand in a coupled P–T network is new.

## 2. System architecture

The authors treat EVs simultaneously as:
- transportation agents in the road network; and
- mobile electric loads in the distribution network.

The coupling node is the EV charging station.

For charging station k connected to distribution node n(k):

```math
P_{n(k),t}^{ch}=\sum_i P_{i,t}^{n}
```

Thus:

```text
transport movement / SOC / charging decision
→ station charging load
→ distribution-network loading
```

## 3. Temperature mechanism actually modeled

The temperature effect is on **vehicle energy consumption**, mainly through heating/cooling auxiliary demand.

The paper defines power consumption per kilometre at ambient temperature T_p as:

```math
F_{T_p}=K_{T_p}+E
```

with a piecewise heating/cooling contribution K_Tp triggered outside temperature thresholds.

Interpretation:

```text
ambient temperature
→ HVAC energy use
→ energy consumption per kilometre
→ battery depletion / charging demand
→ station load
```

This is a **demand-side temperature mechanism**.

## 4. What it does not model

The paper does not establish a dynamic physical chain of:

```text
ambient heat
→ charger / cable / transformer / line component temperature
→ heat-dependent electrical capability
→ service degradation
```

Its temperature mechanism is not a multi-physics component thermal-state model.

Important distinction:

```text
temperature-sensitive EV energy demand
≠
heat-dependent infrastructure capability
```

## 5. Controlled cases

The paper compares four cases:

- Case 1: no ambient-temperature or speed influence;
- Case 2: temperature effect only;
- Case 3: speed effect only;
- Case 4: temperature + speed.

Reported total regional charging energy over 24 h:

- Case 1: 27.2 MWh;
- Case 2: 28.87 MWh;
- Case 3: 29.39 MWh;
- Case 4: 31.49 MWh.

The authors attribute the temperature-only increase to air-conditioning energy use.

## 6. Intervention

The paper develops dynamic charging pricing based on:
- predicted charging demand;
- station maximum thresholds;
- security-constrained distribution-network feasibility.

This means **operational intervention in a temperature-aware CPTN already exists**.

Therefore, generic claims such as:

```text
"we introduce temperature-aware control of EV charging"
```

are not defensible novelty claims.

## 7. Service / resilience boundary

The main outcomes are:
- charging-load prediction;
- charging efficiency;
- charging-price guidance;
- distribution-network secure operation.

The study does **not** directly operationalize:
- electricity service trajectory Q_P(t);
- mobility service trajectory Q_T(t);
- service deficit;
- minimum service;
- recovery time;
- Improve → Adapt → Restore resilience cycle;
- extreme-heat recovery.

This is a possible remaining handoff, but it is **not yet a confirmed research gap**.

## 8. Validation boundary

The paper validates:
- travel-time prediction against a BPR reference;
- charging-load consequences using four simulation cases.

This is model/case validation, not direct validation of heat-dependent physical component temperatures or resilience recovery.

## 9. Thesis consequence

### Rejected novelty claims

```text
ambient temperature → EV power use → charging demand is new
temperature-aware CPTN charging-load prediction is new
temperature-aware charging intervention is new
```

### Candidate remaining distinction

```text
temperature-sensitive demand representation
vs.
explicit heat-dependent physical state/capability representation
propagated to electricity + mobility service trajectories
and resilience actions
```

This distinction must be tested against the rest of the closest literature before being promoted to a research gap.

## 10. Slide mapping

- Slide 2: strongest evidence that temperature-aware road-EV CPTN modeling already exists.
- Slide 4: use to distinguish demand-side temperature effect from infrastructure thermal-state effect.
- Slide 6: useful comparator architecture.
- Slide 7: precedent for controlled cases and operational intervention.

## 11. Freeze impact

**FREEZE / REJECT:**
- novelty claim based only on ambient-temperature effects in EV energy consumption;
- novelty claim based only on temperature-aware charging-load prediction;
- novelty claim based only on dynamic charging pricing.

**KEEP OPEN:**
- whether explicit heat-dependent component states materially change coupled service trajectories;
- exact road-vs-rail choice;
- exact service metrics;
- final comparator architecture.
