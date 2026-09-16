# Canonical Spatiotemporal Propagation Requirement v1

![Authority](https://img.shields.io/badge/authority-CANONICAL-0969DA)
![Status](https://img.shields.io/badge/status-FROZEN-1A7F37)
![Scope](https://img.shields.io/badge/scope-P--T%20cascade%20dynamics-0969DA)

**Effective date:** 2026-09-16  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Scope:** Mandatory spatial-temporal realization requirement for modeled Power–Transportation disruption, cascading failure, recovery and intervention analysis.  
**Framework effect:** Supplements Stages 1–3 and downstream evaluation; does **not** change the frozen seven-stage sequence or the canonical dependency primitive.  
**Change control:** Any relaxation or structural change requires explicit versioning, Git history and re-audit of dependent models, experiments and figures.

---

## 1. Scientific decision

The thesis adopts the following mandatory modeling rule:

```math
\boxed{
\textbf{Every modeled Power--Transportation cascade must preserve both time and location whenever the physical mechanism is spatially dependent.}
}
```

Accordingly, resilience evolution is not represented only as aggregate performance through time. The model must preserve the joint evolution of:

```math
\boxed{
\text{when failure/recovery occurs}
+
\text{where disruption propagates}.
}
```

This requirement is motivated by recent review evidence identifying temporal–geospatial performance evolution as an important unresolved direction in interdependent-infrastructure resilience research.

---

## 2. Evidence basis and claim boundary

Primary evidence anchor:

> Tong, W., Li, H. X., Nasirzadeh, F., Yao, F., & Ji, Y. (2025). *Resilience of interdependent infrastructure networks: Review and future directions*. International Journal of Critical Infrastructure Protection, 51, 100793. https://doi.org/10.1016/j.ijcip.2025.100793

Tong et al. identify two relevant limitations in the reviewed literature:

1. many studies observe infrastructure performance only at selected time points rather than representing continuous or time-step evolution;
2. interdependent infrastructure performance evolves not only temporally but geographically, because cascading failures can propagate across different locations.

The paper recommends combined temporal–geospatial analysis as a future research direction.

**Claim boundary:** Tong et al. support the need for temporal–geospatial analysis; they do **not** provide or validate the specific mathematical formulation adopted below. The thesis formulation therefore remains a proposed engineering realization subject to verification and validation.

---

## 3. Spatially embedded System-of-Systems representation

For the physical Power–Transportation network, use a geographically embedded graph

```math
\boxed{
\mathcal G=(\mathcal V,\mathcal E,X),
\qquad
X=\{x_i\}_{i\in\mathcal V},
\qquad
x_i\in\mathbb R^2
}
```

where each physically located component `i` has geographic position `x_i` or an equivalent validated spatial reference.

The preferred network-state representation is

```math
\boxed{
Y_i(t),
\qquad
i\in\mathcal V,
\qquad
x_i\in\mathbb R^2.
}
```

The shorthand field representation

```math
Y=Y(x,t)
```

may be used when useful, but it does **not** imply that the thesis requires a continuous spatial field or partial differential equation model.

---

## 4. Compatibility with the canonical dependency contract

The canonical Stage-2 dependency object remains unchanged:

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e).
```

No new primitive field is introduced.

Spatial information is attached through the already canonical source and receiver interface locations

```math
p_e^s,
\qquad
p_e^r,
```

and through node/entity spatial metadata. Thus, when needed for exposition, a dependency may be evaluated as

```math
\boxed{
\mathfrak d_e
=
\mathfrak d_e(x_s,x_r,t,Y,m)
}
```

without redefining the primitive dependency contract.

The required interpretation is:

```text
x_s = spatial location of the source interface/entity;
x_r = spatial location of the receiver interface/entity;
t   = event/evolution time;
Y   = coupled system state;
m   = operating mode.
```

Delay remains distinct from spatial separation. A propagation delay may depend on distance or route state, but

```math
\boxed{
\text{distance}
\neq
\text{causal delay}
\neq
\text{characteristic timescale}.
}
```

---

## 5. Mandatory causal trace

For any spatially dependent cascade mechanism, the model must preserve the following trace:

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
\text{recovery}
\rightarrow
\text{intervention location/time}.
}
```

The corresponding engineering questions are:

```text
Where does the disruption originate?
Through which interfaces does it propagate?
How fast does it propagate?
Which locations and services are affected?
Where does recovery begin and how does it spread?
Where and when should intervention occur?
```

A model that reports only a system-wide aggregate loss while discarding physically relevant propagation location or timing does not satisfy this requirement.

---

## 6. Stage integration

### Stage 1 — Multilayer Structure

Every physically represented Power or Transportation component used in propagation analysis must have a declared spatial reference sufficient to establish adjacency, interface location, routing or geographic exposure where these are physically relevant.

### Stage 2 — Causal Mechanisms

Every retained spatially dependent dependency must identify its source and receiver interface locations and its causal transmission mechanism. Common geographic co-exposure alone does not establish a directed dependency.

### Stage 3 — Coupled Hybrid Multiscale Dynamics

Stage 3 must evolve accepted mechanisms jointly in time and network space whenever propagation depends on geographic location, route, distance, topology or changing accessibility.

A compact representation is

```math
\boxed{
\mathbb I(x,t,Y,m)
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Y(x,t).
}
```

### Stages 4–7

Observation, control, viability, intervention and sustainability evaluation must retain spatial resolution whenever spatial aggregation would change the engineering conclusion.

---

## 7. Scope control

This requirement does **not** impose spatial partial differential equations as a universal modeling method.

The default implementation for the Power–Transportation demonstrator is a spatially embedded multilayer graph with dynamic states on nodes, links and interfaces:

```math
\boxed{
\text{spatial graph}
+
\text{hybrid dynamics}
+
\text{time-varying interdependencies}.
}
```

A continuous spatial field, PDE, cellular model or other spatial formalism is introduced only when the physical mechanism and evidence require it.

---

## 8. Minimum data/provenance requirements

For each spatially dependent modeled component or interface, record as applicable:

```text
component/interface identifier;
infrastructure layer;
validated geographic reference;
coordinate reference system or map convention;
source and receiver identifiers;
physical route/topological connection;
activation time/event time;
causal delay where applicable;
state and service variables;
data source and provenance;
spatial uncertainty/resolution;
temporal resolution;
validation status.
```

Geographic precision must not exceed the precision supported by the source data.

---

## 9. Verification requirements

A spatiotemporal implementation must pass, where applicable:

1. **spatial identity check** — node/interface coordinates and network membership are internally consistent;
2. **topology check** — impossible propagation paths cannot be activated;
3. **time-ordering check** — receiver effects cannot precede physically causal source events;
4. **delay check** — declared causal delay is distinguishable from event time and numerical timestep;
5. **route/access check** — transportation accessibility changes affect restoration/logistics only through declared mechanisms;
6. **aggregation check** — spatial aggregation is tested to determine whether it changes cascade or intervention conclusions;
7. **resolution sensitivity** — conclusions are not artifacts of an arbitrary temporal or geographic discretization;
8. **reproducibility check** — spatial and temporal inputs, transformations and outputs are traceable.

---

## 10. Validation and falsification

The requirement does not assume that adding spatial detail automatically improves prediction.

Where data permit, the thesis must compare a spatially resolved formulation against an appropriate less-resolved comparator and test whether the additional resolution materially improves at least one preregistered quantity such as:

```text
cascade timing;
propagation path;
service-loss localization;
recovery sequencing;
interface criticality;
intervention location/timing;
predictive error on held-out observations.
```

If spatial resolution provides no material value for a declared mechanism or experiment, the simpler representation remains admissible for that specific task, provided the justification is documented.

---

## 11. Canonical research implication

The thesis shall therefore ask not only

> **How much performance is lost?**

but also

> **Where does disruption originate, through which interfaces does it propagate, how fast does it spread, and where and when should intervention occur?**

The resulting causal spine is

```math
\boxed{
\text{interdependency}
\rightarrow
\text{spatiotemporal cascade propagation}
\rightarrow
\text{resilience/viability consequence}
\rightarrow
\text{intervention location and timing}.
}
```

---

## 12. Canonical statement

> **Interdependency, cascading failure, recovery and intervention shall be represented spatiotemporally whenever their physical mechanisms depend on location or propagation through the infrastructure network. Spatial resolution shall be sufficient to preserve causal engineering conclusions but shall not exceed the resolution justified by the governing physics, available evidence and validation data.**

**Status:** FROZEN CANONICAL MODELING REQUIREMENT v1.0.
