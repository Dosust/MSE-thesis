# Spatiotemporal Propagation Requirement V1

**Status:** FROZEN DESIGN REQUIREMENT  
**Date:** 2026-09-16  
**Applies to:** Power–Transportation cascade, recovery, viability, and intervention experiments  
**Framework impact:** strengthens Stages 1–6 without changing the frozen seven-stage architecture  

## 1. Scientific requirement

For the physical Power–Transportation core, resilience shall not be represented only as aggregate performance evolving in time. Whenever a modeled mechanism depends on geographic location or propagation through the infrastructure network, the model shall preserve both **time** and **location**.

```math
\boxed{\textbf{Every modeled Power--Transportation cascade must preserve both time and location.}}
```

The corresponding principle is

```math
\boxed{
\text{resilience evolution}
=
\text{when failure/recovery occurs}
+
\text{where disruption/recovery propagates}.
}
```

This requirement is motivated by Tong et al. (2025), who identify joint temporal–geographic evolution of interdependent-infrastructure performance as an important research need and note that cascading performance losses can propagate across geographic areas. This source establishes the research need; it does **not** prescribe the mathematical formulation adopted here.

**Evidence source:** Tong, W., Li, H. X., Nasirzadeh, F., Yao, F., & Ji, Y. (2025). *Resilience of interdependent infrastructure networks: Review and future directions*. *International Journal of Critical Infrastructure Protection, 51*, 100793. https://doi.org/10.1016/j.ijcip.2025.100793

## 2. Preferred mathematical representation

A geographically embedded multilayer graph is the default representation:

```math
\boxed{
\mathcal G=(\mathcal V,\mathcal E,X),
\qquad
X=\{x_i\}_{i\in\mathcal V},
\qquad
x_i\in\mathbb R^2
}
```

with component-level dynamic state

```math
\boxed{
Y_i(t),
\qquad
i\in\mathcal V.
}
```

Equivalently, where a continuum-style notation is useful,

```math
Y=Y(x,t).
```

The graph representation is preferred for the thesis because substations, charging stations, traffic-control devices, road links, restoration resources, and other relevant components are naturally represented as spatially embedded network objects.

## 3. Spatiotemporal evaluation of interdependencies

The frozen canonical dependency object remains unchanged. Spatial location is introduced through the source and receiver component locations supplied by the graph embedding.

For an edge or interface `e=(s_e,r_e)`, the operational evaluation of the dependency is therefore written as

```math
\boxed{
\mathfrak d_e
\equiv
\mathfrak d_e\!\left(
 x_{s_e},x_{r_e},t,Y,m
\right)
}
```

as shorthand for evaluating the canonical dependency mechanism under the spatial locations of its source and receiver, the current time, system state, and operating mode.

This notation does **not** replace the canonical tuple definition of `\mathfrak d_e`; it adds the spatiotemporal arguments required for execution.

The model must therefore be able to identify:

- where the dependency originates;
- where its effect is received;
- when it activates;
- any propagation or response delay;
- the system state and operating mode under which it is active.

## 4. Required causal trace

For every modeled P–T cascade, the executable trace shall preserve the following structure:

```math
\boxed{
\text{disturbance at }(x_0,t_0)
\rightarrow
\text{interface activation}
\rightarrow
\text{spatiotemporal propagation}
\rightarrow
\text{service loss}
\rightarrow
\text{response/recovery}
\rightarrow
\text{intervention location and time}.
}
```

A valid cascade record must remain traceable at least to

```math
\boxed{
\text{source component}
\rightarrow
\text{causal interface}
\rightarrow
\text{receiver component}
\rightarrow
\text{activation time}
\rightarrow
\text{consequence}
}
```

and, where propagation continues, to subsequent downstream components and times.

## 5. Mandatory execution gates

A spatiotemporal cascade experiment is admissible only if the following gates pass.

| Gate | Requirement |
|---|---|
| **ST1 — Spatial identity** | Each modeled physical component has a valid spatial locator or an explicitly justified non-spatial exception. |
| **ST2 — Temporal identity** | Disturbance, state, observation, control, failure, and recovery events use a declared common time basis. |
| **ST3 — Directional traceability** | Every interdependency used in a cascade identifies source, receiver, mechanism, and direction. |
| **ST4 — Propagation timing** | Propagation, activation, communication, or response delay is represented, estimated, bounded, or explicitly declared negligible. |
| **ST5 — State evolution** | Component or service states can be reconstructed through time rather than only at initial, minimum, and final performance points. |
| **ST6 — Spatial aggregation provenance** | Any city-, network-, or system-level resilience metric remains traceable to the underlying spatial component states. |
| **ST7 — Intervention specificity** | Every tested intervention identifies where it acts, when it acts, and which mechanism or state equation it changes. |
| **ST8 — Uncertainty** | Material uncertainty in timing, location, state observation, and propagation parameters is carried into validation/UQ rather than silently fixed. |

Failure of a required gate blocks a confirmatory spatiotemporal claim; it does not authorize imputation without evidence.

## 6. Relationship to performance curves

Performance curves may remain as conventional aggregate benchmarks, but they shall not substitute for the underlying spatiotemporal state evolution when the physical mechanism is location dependent.

Thus

```math
\boxed{
\text{component states }Y_i(t)
\rightarrow
\text{spatiotemporal propagation}
\rightarrow
\text{aggregate service/performance curve}
}
```

is admissible, whereas using an aggregate performance curve alone to infer where or through which interface a cascade propagated is not.

This preserves direct comparability with conventional resilience assessment while preventing spatial propagation from being erased by aggregation.

## 7. Scope control

This requirement does **not** mandate spatial partial differential equations throughout the thesis.

```math
\boxed{
\text{default spatial representation}
=
\text{geographically embedded graph}
}
```

A continuum/PDE representation is used only where the underlying physics and available data require it.

Additional scope rules:

1. Spatial resolution shall not exceed the resolution supported by data or physics.
2. Geographic co-location or correlation alone shall not be interpreted as causal interdependency.
3. Information and organizational mechanisms are spatially represented only when location materially affects sensing, communication, authority, resources, access, or response.
4. Aggregate metrics remain permitted for reporting, but the causal model must retain the underlying spatial provenance.

## 8. Integration with the frozen seven-stage framework

This requirement strengthens, but does not replace, the existing architecture:

```math
\boxed{
\mathcal S
\rightarrow
\mathbb I(x,t,Y,m)
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Y_i(t)
\rightarrow
\mathbf R
\rightarrow
 a_k(x,t)
\rightarrow
\left(\Delta\mathbf R,\Delta\mathbf J_{\mathrm{sus}}\right).
}
```

- **Stage 1 — Multilayer Structure:** attach defensible spatial locations to relevant physical components.
- **Stage 2 — Causal Mechanisms:** preserve directional source–receiver interfaces and their spatial relation.
- **Stage 3 — Coupled Hybrid Multiscale Dynamics:** evolve component states through time and propagate effects across the embedded graph.
- **Stage 4 — Observation, Organization, Feedback and Control:** represent observation, communication, coordination, access, and response delays where material.
- **Stage 5 — Viability:** compute maintainability from the full system state while retaining the spatial provenance of state degradation and constraint activation.
- **Stage 6 — Resilience-to-Sustainability Transformation Interface:** identify where and when resilience weaknesses motivate intervention.
- **Stage 7 — Sustainable Transformation Pathways:** remains unchanged; spatiotemporal consequences feed pathway evaluation where relevant.

## 9. Governing scientific question

The design requirement is summarized by the following engineering question:

```math
\boxed{
\text{Where does disruption originate, through which interfaces does it propagate,}
\;\text{how fast does it spread, and where and when should intervention occur?}
}
```

This is a **model-design requirement**, not a new numbered thesis research question unless the research-question specification is formally revised.

## 10. Freeze rule

The following are frozen for subsequent model development unless changed through an explicit versioned revision:

```math
\boxed{
\text{P--T cascades with location-dependent mechanisms}
\Rightarrow
\text{spatiotemporal representation is mandatory.}
}
```

```math
\boxed{
\text{Performance curves may benchmark resilience, but may not erase causal spatial provenance.}
}
```

```math
\boxed{
\text{No new PDE requirement is introduced by this specification.}
}
