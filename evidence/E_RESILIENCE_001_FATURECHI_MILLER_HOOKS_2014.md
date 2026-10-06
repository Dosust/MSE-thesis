# E-RESILIENCE-001 — Faturechi & Miller-Hooks (2014)

**Status:** ADMITTED EXTERNAL EVIDENCE  
**Date admitted:** 2026-10-06  
**Primary use:** scientific foundation for pre-event improvement, adaptation/flexibility, recovery/restoration, disruption profiles, and decision optimization under uncertainty

## Source

Reza Faturechi & Elise Miller-Hooks (2014), "A Mathematical Framework for Quantifying and Optimizing Protective Actions for Civil Infrastructure Systems," *Computer-Aided Civil and Infrastructure Engineering*, 29, 572–589. DOI: 10.1111/mice.12027.

## 1. What the paper establishes

The paper develops an Infrastructure Protection Framework (IPF) that organizes:
- coping capacity;
- preparedness;
- robustness;
- flexibility/adaptability;
- recovery capability;
- resilience.

It explicitly distinguishes:
- innate system capability;
- pre-event actions;
- postevent adaptive/response actions;
- recovery actions;
- resilience as a broader concept incorporating multiple facets.

## 2. Strong mapping to the thesis-defined cycle

The thesis uses:

```text
IMPROVE → ADAPT → RESTORE
```

This paper provides a strong literature basis for that sequence, but not under those exact words.

### IMPROVE — literature mapping

Closest established concepts:
- preparedness;
- robustness enhancement;
- expansion;
- retrofit;
- resource availability.

These are pre-event actions that can improve system capacity, resistance, readiness, or the effectiveness/speed of later response.

Therefore:

```text
THESIS: IMPROVE
≈ literature: preparedness + robustness-enhancing pre-event action
```

### ADAPT — literature mapping

Closest established concept:
- flexibility / adaptability;
- postevent adaptive response.

The paper defines flexibility as the capability of the system to adapt to disruption using available resources and response actions.

Therefore:

```text
THESIS: ADAPT
≈ literature: flexibility / adaptive response
```

### RESTORE — literature mapping

Closest established concept:
- recovery capability;
- postevent response actions that restore lost capacity/performance.

Therefore:

```text
THESIS: RESTORE
≈ literature: recovery capability / restoration
```

## 3. Critical scientific refinement

Do **not** claim:

```text
Resilience = Improve + Adapt + Restore
```

as a universal literature definition.

More defensible:

```text
For this thesis, resilience is operationalized through
Improve → Adapt → Restore,
where these phases are grounded respectively in established
preparedness/robustness, flexibility/adaptability, and recovery concepts.
```

This preserves the thesis-defined structure while grounding it in conventional resilience literature.

## 4. Service trajectory / disruption profile

The paper represents infrastructure performance as a time-dependent disruption profile:

```text
pre-event
→ disruption
→ minimum performance
→ recovery
→ desired recovered state
```

This is directly compatible with our service-centered thesis if system performance is represented as:

```text
Q(t) = [Q_P(t), Q_T(t)]
```

or a defined service function.

The paper distinguishes:
- point performance measures;
- period performance measures based on areas under performance curves.

This provides a strong basis for:
- service deficit;
- minimum service;
- recovery time;
- area-under-curve resilience metrics.

## 5. Optimization under uncertainty

The paper formulates a two-stage stochastic optimization problem:
- first-stage: pre-event preparedness decisions;
- second-stage: postevent recourse/response decisions after disruption realization.

This is directly relevant to the thesis distinction between:
- proactive improvement;
- adaptive response;
- restoration under realized conditions.

However, adopting the full stochastic optimization framework is optional and must pass Master's-scope gates.

## 6. Relevance to thesis presentation

| Slide | Use |
|---|---|
| 1 | Infrastructure disruption and resilience motivation |
| 2 | Established resilience concepts and action timing |
| 3 | Scope language for pre-event vs postevent actions |
| 5 | Service/performance trajectory and recovery profile |
| 6 | Mathematical basis for time-dependent service metrics |
| 7 | Controlled intervention/optimization under uncertainty |
| 8 | Strong foundation for Improve → Adapt → Restore |

## 7. Important distinctions from the paper

The paper itself distinguishes:
- reliability from resilience;
- robustness from flexibility;
- preparedness from recovery;
- pre-event from postevent action;
- system performance level from disruption probability/risk.

This strongly supports our thesis rule:

```text
reliability ≠ resilience
preparedness ≠ recovery
robustness ≠ adaptability
```

## 8. Boundaries

The paper is general civil-infrastructure mathematics with a transportation example.

It does **not** establish:
- extreme-heat physics;
- Power–Transportation electrification coupling;
- transport-electrification technology;
- heat-dependent state equations;
- our exact service variables;
- our exact intervention.

It should therefore ground the **resilience/action architecture**, not the physical mechanism layer.

## 9. Freeze impact

Strengthens and nearly resolves the conceptual basis for:

```text
IMPROVE → ADAPT → RESTORE
```

Recommended status:
- thesis action sequence: **WORKING-FROZEN**
- terminology mapping to literature: **SUPPORTED**
- universal resilience definition claim: **REJECTED**

## 10. Presentation-ready wording

> In this thesis, resilience is operationalized through three engineering phases: Improve, Adapt, and Restore. These correspond to established resilience concepts of pre-event preparedness and robustness enhancement, adaptive flexibility during disruption, and postevent recovery.

