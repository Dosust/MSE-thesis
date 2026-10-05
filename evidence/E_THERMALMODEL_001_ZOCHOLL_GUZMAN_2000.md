# E-THERMALMODEL-001 — Zocholl & Guzman (2000)

**Status:** ADMITTED EXTERNAL EVIDENCE  
**Date admitted:** 2026-10-05  
**Primary use:** thermal-state memory, time evolution, protection, and distinction between static current limits and state-aware thermal models

## Source
Stanley E. Zocholl and Armando Guzman, "Thermal Models in Power System Protection," Schweitzer Engineering Laboratories, presented at the 54th Annual Georgia Tech Protective Relaying Conference, 2000; originally presented at the 26th Annual Western Protective Relay Conference, 1999.

## What the source supports

The paper explains that thermal protection based only on overcurrent coordination cannot fully represent thermal history, while differential-equation-based thermal models can track temperature state through time.

Core mechanism:

```text
electrical loading
→ heat generation
→ thermal state with memory
→ temperature limit / protection action
```

For overhead lines, the thermal balance includes:
- conductor losses;
- convection;
- radiation;
- solar gain;
- conductor heat capacity.

## Thesis relevance

This source strengthens the distinction:

```text
instantaneous electrical quantity
≠ thermal state
```

and:

```text
static limit
≠ time-dependent thermal history
```

That is important if the thesis claims that physical state and time matter for service/resilience.

It also supports using a state-evolution model only when the relevant thermal memory changes the engineering conclusion.

## Improvement connection

The paper supports the logic:

```text
simplified protection representation
→ state-aware thermal model
→ more accurate thermal-state tracking
→ improved protection / operational decision
```

Therefore, "improvement first" can be grounded in better physical-state representation rather than simply adding mathematical complexity.

## Boundary

The paper is a protection/thermal-model tutorial. It does not establish:
- coupled Power-Transportation resilience;
- transport service;
- the thesis adaptation strategy;
- restoration dynamics.

## Presentation mapping

- Slide 4: state + time + thermal memory.
- Slide 6: state equations / thermal model structure.
- Slide 7: model adequacy and protection/decision consequence.
- Slide 8: improvement through state-aware physical modeling.

## Freeze impact

Strengthens:
- state and time as physically meaningful;
- thermal history where justified;
- improvement through better model adequacy.

Does not freeze:
- exact thermal state vector;
- exact power component;
- transport mode;
- intervention.
