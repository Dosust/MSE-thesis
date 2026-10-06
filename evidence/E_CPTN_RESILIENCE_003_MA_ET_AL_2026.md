# E-CPTN-RESILIENCE-003 — Ma et al. (2026)

**Status:** ADMITTED — STRONG RESILIENCE / RESTORATION COMPARATOR  
**Date reviewed:** 2026-10-06  
**Source type:** Peer-reviewed Applied Energy article, full text supplied by user  
**Primary use:** CPTN resilience, PDN restoration, dynamic traffic-and-energy assignment, pricing coordination, V2G flexibility, restoration metrics, comparator architecture

## Source

Cheng Ma, Canqi Yao, Haochen Hua, Shunbo Lei (2026),  
"Resilient pricing-driven coordination of coupled power and transportation networks: A learning-augmented mixed-integer reformulation approach,"  
*Applied Energy* 420, 128158.  
DOI: 10.1016/j.apenergy.2026.128158.

## 1. What the paper establishes

The paper develops a resilient pricing-driven bilevel coordination framework for coupled power and transportation networks (CPTNs).

Upper level:
- PDN restoration;
- microgrid formation;
- load pickup;
- resilient V2G pricing.

Lower level:
- transportation-network dynamic traffic and energy assignment (DTEA);
- EV routing;
- charging/discharging power;
- traffic-energy co-optimization.

The two levels are coupled through price signals and spatio-temporal V2G availability.

## 2. Bidirectional CPTN mechanism

The paper explicitly states:

```text
PDN disruption
→ EV charging disruption
→ altered EV traffic assignment
```

and:

```text
TN conditions / EV traffic-energy decisions
→ spatio-temporal V2G availability
→ PDN restoration capability
```

This is a genuine reciprocal operational interdependency.

Important distinction for this thesis:

```text
bidirectional interdependency
≠
bidirectional electrical power flow
```

because the reverse direction here is enabled through V2G and traffic-energy decisions, not by interdependency language alone.

## 3. Restoration formulation

The paper explicitly optimizes restoration performance.

Power-side outcomes include:
- weighted restored load;
- restored nodes;
- restoration steps;
- microgrid formation;
- V2G contribution.

The P33-T12 case restores all loads by time step t4 in the reported scenario.

The larger P123-T24 case restores all loads within seven steps in the reported scenario.

## 4. Dynamic coupling

The DTEA model co-optimizes:
- EV traffic flow;
- EV charging/discharging power;
- aggregate energy state;
- queuing;
- path decisions.

The paper emphasizes that traffic flows and charging/discharging power are continuous decision variables and are co-optimized, creating endogenous nonlinear flow-power coupling.

This makes the paper a strong dynamic-coupling comparator.

## 5. Learning-augmented reformulation

A neural-network surrogate is trained on simulation-generated data and embedded into a mixed-integer formulation to approximate nonlinear energy-flow terms.

The NN is not used as a black-box controller; it is used to learn nonlinear constraints and is then encoded inside the optimization.

The paper compares:
- fixed C&D power baseline;
- McCormick linearization;
- constraint-learning linearization.

It reports lower approximation error and stronger V2G utilization for the proposed formulation.

## 6. Critical boundary for our thesis

This paper does **not** model:
- ambient temperature forcing;
- extreme-heat physics;
- component thermal states;
- heat-dependent charging capability;
- heat-dependent PDN equipment capability;
- electricity and mobility serviceability under heat;
- pre-event thermal improvement actions.

A text search of the full paper returns no temperature/heat model; "thermal" appears only in references.

Therefore this paper is a **resilience/restoration comparator**, not a heat-physics comparator.

## 7. What it blocks as novelty

Do not claim novelty for:

```text
dynamic CPTN resilience coordination
PDN restoration + TN traffic dynamics
V2G-supported restoration
bilevel CPTN resilient pricing
joint traffic and energy assignment
learning-augmented mixed-integer reformulation
```

## 8. What remains open

The thesis may still investigate:

```text
extreme heat
→ physical thermal/electrical state
→ capability degradation
→ qualified P–T electrification coupling
→ electricity + mobility service trajectory
→ Improve / Adapt / Restore action effectiveness
```

This is not yet a final novelty claim.

## 9. Strong methodological lesson

The paper gives a good benchmark for:

```text
dynamic coupling
+ restoration trajectory
+ controlled method comparison
+ explicit decision variables
+ computational validation
```

It should be treated as one of the closest **resilience-operation comparators** for the road-EV CPTN branch.

## 10. Presentation use

- Slide 2: evidence that dynamic CPTN resilience and restoration are already well developed.
- Slide 3: example of genuine reciprocal operational coupling.
- Slide 6: comparator for dynamic traffic-energy equations and optimization architecture.
- Slide 7: strong precedent for restoration trajectories, method comparison, and computational validation.
- Slide 8: shows that restoration is already well developed; our contribution cannot simply be "restore coupled P–T systems."

## 11. Freeze impact

**REJECT as novelty**
- dynamic CPTN restoration;
- V2G-supported restoration;
- resilient pricing coordination;
- joint traffic-energy assignment.

**KEEP OPEN**
- extreme-heat physical-state representation;
- heat-dependent serviceability;
- improvement before disruption;
- heat-state-aware adaptation;
- heat-driven recovery/restoration trajectory;
- exact road-vs-rail scope.
