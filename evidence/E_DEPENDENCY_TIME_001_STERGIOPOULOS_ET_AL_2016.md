# E-DEPENDENCY-TIME-001 — Stergiopoulos et al. (2016)

**Status:** ADMITTED EXTERNAL EVIDENCE  
**Date admitted:** 2026-10-06  
**Primary use:** definition and qualification of infrastructure dependency; time-dependent cascading effects; distinction between dependency and geographic co-location; proactive mitigation analysis

## Source

George Stergiopoulos, Panayiotis Kotzanikolaou, Marianthi Theocharidou, Georgia Lykou, Dimitris Gritzalis.  
"Time-based critical infrastructure dependency analysis for large-scale and cross-sectoral failures."  
International Journal of Critical Infrastructure Protection 12 (2016) 46–60.  
DOI: 10.1016/j.ijcip.2015.12.002.

## 1. Standardized dependency definition

The paper adopts a one-directional dependency concept:

```text
A dependency is a one-directional reliance of an asset/system/network
on an input, interaction, or other requirement from another source
in order to function properly.
```

This is directly relevant to the thesis qualification rule:

```text
connection ≠ dependency
co-location ≠ dependency
```

A Power → Transportation or Transportation → Power relation must identify:
- direction;
- required input or interaction;
- affected function;
- consequence if the input is degraded or unavailable.

## 2. Dependency types and co-location distinction

The paper distinguishes physical, informational, logical, and geographical dependencies.

Important thesis implication:
- physical proximity can create a **common-cause exposure**;
- proximity alone does not prove a functional dependency.

Thus:

```text
geographical co-location
→ possible common-cause vulnerability
≠ functional interdependency
```

This strongly supports keeping the thesis statement:

```text
co-location ≠ dependency
```

## 3. Time-dependent dependency evolution

The paper extends static dependency analysis by assigning each dependency:
- an impact magnitude;
- a time to maximum impact;
- a growth/evolution pattern;
- a time-dependent impact function.

It considers slow, linear, and rapidly evolving impacts.

General lesson for the thesis:

```text
dependency consequence is not necessarily instantaneous
```

and:

```text
interdependency effect = function of time
```

This is useful for Power–Transportation service analysis under extreme heat, where:
- physical states evolve over time;
- service consequences may lag physical forcing;
- the timing of intervention can matter.

## 4. Cascading vs common-cause failures

The paper distinguishes:
- cascading failure;
- escalating failure;
- common-cause failure.

This is important for the thesis because extreme heat may:
1. directly stress both Power and Transportation components as a common external forcing; and
2. also propagate effects through functional P–T dependencies.

Therefore the framework should not confuse:

```text
common heat exposure
with
cross-system dependency propagation
```

## 5. Proactive improvement relevance

The CIDA framework is designed to:
- identify underestimated dependency-risk paths;
- compare alternative mitigation controls;
- assess reaction-time implications;
- target critical nodes;
- improve resistance and restorative capability.

This strongly supports the thesis **IMPROVE** phase as a proactive decision problem.

Literature mapping:

```text
THESIS: IMPROVE
← proactive identification of critical dependency paths
← mitigation-control comparison
← strengthening critical nodes / reducing dependency risk
```

## 6. Adaptation and restoration relevance

The paper cites resilience-oriented control as the capacity to:
- absorb;
- adapt;
- rapidly recover.

Its own tool can compare mitigation controls with different reaction times and identify locations/times where controls should be implemented.

For the thesis:
- this is conceptual/methodological support for **ADAPT** and **RESTORE**;
- it does not provide the physical control laws for our coupled P–T system.

## 7. Critical boundary for our thesis

The method is primarily:
- graph-based;
- risk-based;
- fuzzy/time-based;
- dependent on organization-level risk assessments and expert input.

It is **not** a physics-based model of:
- heat transfer;
- power flow;
- EV charging;
- transport dynamics;
- coupled physical state evolution.

Therefore:

```text
time-based dependency risk model
≠ physics-based dynamical model
```

This distinction is central to our thesis.

## 8. Strong thesis opportunity

This paper helps expose a precise methodological handoff:

```text
high-level dependency graph
→ identifies who depends on whom and how impacts can propagate in time
```

but our thesis seeks:

```text
physical state equations
→ quantify how extreme heat changes capability
→ propagate those changes through qualified P–T dependencies
→ evaluate electricity and mobility service
→ improve / adapt / restore
```

This is not yet a novelty claim. It is a useful research-positioning distinction.

## 9. Presentation mapping

| Slide | Use |
|---|---|
| 1 | Motivation: cross-sectoral dependencies can propagate failures |
| 2 | Established dependency-analysis methods and time-based cascading analysis |
| 3 | Strong definition of dependency and distinction from co-location |
| 4 | Time-dependent propagation logic; cascading vs common-cause |
| 5 | Service consequence should be distinguished from dependency risk |
| 7 | Reaction time, mitigation-control comparison, scenario analysis |
| 8 | Proactive improvement and targeted mitigation logic |

## 10. Freeze impact

Strengthens:
- dependency must be directional and functional;
- co-location is not dependency;
- time must be explicit;
- common-cause exposure and cascading dependency must be separated.

Still OPEN:
- exact P–T physical coupling law;
- selected transport mode;
- exact state variables;
- service metrics;
- adaptation control;
- restoration action.

