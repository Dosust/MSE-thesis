# E-INTERDEP-002 — Ganguly & Mukherjee (2022)

**Status:** ADMITTED WITH CAUTION — PREPRINT EVIDENCE  
**Date admitted:** 2026-10-06  
**Source type:** arXiv preprint (v1, 13 Dec 2022), not treated as peer-reviewed evidence unless publication status is independently verified  
**Primary use:** interdependent-infrastructure modeling taxonomy; intra- vs inter-infrastructure failure separation; time-dependent vulnerability; redundancy; incomplete-information modeling  
**Do not use as:** direct physics-based evidence for extreme-heat Power–Transportation dynamics

## Source

Prasangsha Ganguly & Sayanti Mukherjee,  
"IIVA: A Simulation Based Generalized Framework for Interdependent Infrastructure Vulnerability Assessment," arXiv:2212.06894v1 (2022).

## 1. What the paper contributes

The paper proposes a generalized simulation-based framework for infrastructure vulnerability under incomplete information. It combines:

- dynamic fault trees (DFT);
- continuous-time / time-dependent Bayesian-network reliability modeling;
- network-of-networks representation;
- physical, logical, and geographical interdependencies;
- scenario-based simulation;
- intra-infrastructure cascading failure;
- inter-infrastructure induced failure;
- comprehensive vulnerability as combined failure probability.

Its high-level structure is:

```text
intra-infrastructure failure
+
inter-infrastructure failure
→ comprehensive vulnerability
```

## 2. Strong conceptual distinction for the thesis

The paper separates:

```text
intra-infrastructure propagation
≠
inter-infrastructure propagation
```

This is directly useful for the Power–Transportation thesis.

For our framework:

```text
Power internal dynamics/failures
+
Transportation internal dynamics/failures
+
qualified P–T coupling
→ coupled service consequence
```

The thesis should not attribute all degradation to interdependency when some loss arises from within-system physics.

## 3. Interdependency qualification

The paper considers physical, logical, geographical, and functional forms of interdependency.

Important detail from Algorithm 2:
an interdependency edge is first considered only if:
- a node may require a service from another infrastructure node; or
- its state may be affected by that other node.

Spatial distance is then used to modulate interdependency-edge strength.

This supports a stronger rule for our thesis:

```text
functional/service requirement first
→ spatial relation may modify exposure/strength
```

not:

```text
co-location alone → dependency
```

Therefore the paper is compatible with our rule:

```text
co-location ≠ dependency
```

provided the service/state-reliance condition is enforced first.

## 4. Time and state relevance

The framework estimates failure probability as a function of time and explicitly propagates failure probabilities over repeated iterations.

This supports:

```text
interdependency consequence = time-dependent
```

and reinforces the need to distinguish:
- static topology;
- dynamic state;
- time-dependent failure/service consequence.

However, this is probabilistic failure evolution, not a physical heat-transfer or power-flow state model.

## 5. Redundancy and improvement

The paper reports that vulnerability decreases as redundancy increases in its modeled systems.

This supports the **IMPROVE** phase conceptually:

```text
diagnose structural vulnerability
→ identify redundancy deficiency
→ allocate improvement resources
→ reduce failure vulnerability
```

But its numerical redundancy findings are model/case dependent and should not be transferred directly to our P–T system.

## 6. Information and organizational support

The paper argues that isolated infrastructure management can underestimate system vulnerability and that collaboration/information sharing among interdependent infrastructure managers can improve awareness of comprehensive vulnerability.

This provides useful evidence for retaining Information (I) and Organization (O) as **support domains**, not as the physical P–T core.

## 7. Modeling taxonomy

The paper summarizes six broad infrastructure-modeling categories:
1. aggregate supply-demand;
2. dynamic simulation;
3. agent-based;
4. physics-based;
5. population mobility;
6. Leontief input-output.

The authors classify their own approach as hybrid/simulation-based rather than physics-based.

This is important positioning for our thesis:

```text
hybrid probabilistic vulnerability model
≠
physics-based mathematical engineering model
```

Our thesis may borrow structural ideas from such frameworks while deriving physical state equations from the relevant engineering physics.

## 8. Important limitations for thesis use

The paper:
- uses synthetic/hypothetical data for several networks;
- uses heuristic interdependency construction under incomplete information;
- assumes independence between intra- and inter-infrastructure failure probabilities when combining them;
- uses user-defined thresholds and relative-importance matrices;
- does not model extreme heat;
- does not model P–T electrification physics;
- does not define electricity/mobility service trajectories;
- does not validate our Improve–Adapt–Restore cycle.

These assumptions must not be transferred without independent justification.

## 9. Presentation mapping

| Slide | Use |
|---|---|
| 2 — Established knowledge | Existing interdependent-infrastructure vulnerability models already handle multiple dependency types and time-dependent failure propagation |
| 3 — Scope | Strong distinction between intra-system and inter-system mechanisms; functional reliance must precede spatial weighting |
| 4 — Mechanism | Useful structural logic for propagation, but not physical heat equations |
| 5 — Performance | Vulnerability probability is not the same as serviceability or resilience |
| 7 — Test/validation | Scenario analysis and sensitivity to redundancy/interdependency parameters |
| 8 — Improvement | Redundancy and information-sharing can be candidate improvement levers, subject to P–T-specific testing |

## 10. Freeze impact

Strengthens:
- intra-system vs inter-system separation;
- time-dependent interdependency consequences;
- functional dependency before proximity weighting;
- Information and Organization as supporting domains;
- redundancy as an improvement candidate.

Still OPEN:
- final P–T transport mode;
- exact electrification mechanism;
- physical state equations;
- exact service metrics;
- adaptation strategy;
- restoration strategy.

## 11. Presentation-ready sentence

> Existing hybrid vulnerability frameworks can represent intra- and inter-infrastructure failure propagation under incomplete information, but they do not replace the physics-based state equations needed to determine how extreme heat changes Power–Transportation capability and service.

