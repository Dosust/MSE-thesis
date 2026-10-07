# Canonical State-Time Definitions V1

**Status:** CANONICAL — FROZEN THESIS DEFINITION  
**Effective date:** 2026-10-08  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Applies to:** all active thesis scope, conceptual and mathematical frameworks, literature review, methodology, results, figures, and interpretation using the terms *state*, *state-time*, *transition time*, *propagation delay*, *service disruption time*, *recovery time*, or *aging/degradation state*.  
**Higher scope authorities:** `CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md` + `CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`

## 1. Canonical meaning of state

In this thesis:

> **A state variable is an evolving physical, operational, energy, or degradation variable whose current value is required, together with the model inputs and parameters, to determine the subsequent evolution of the modeled system.**

A general representation is

```math
\dot X(t)=F\!\left(X(t),H(t),u(t);\theta\right),
```

where:
- `X(t)` is the modeled state;
- `H(t)` is external forcing, including extreme heat;
- `u(t)` is a control or operating action when present;
- `\theta` contains model parameters.

The state answers:

```text
What condition is the modeled system in now, in the sense required to predict what happens next?
```

This definition is stricter than “any quantity that changes with time.”

## 2. Full physical state space versus active reduced model state

A real component or infrastructure system may possess many legitimate states. The thesis does not model all of them.

Distinguish:

```text
full physical state space
≠
active reduced thesis state vector
```

A physically legitimate state enters the **active model state vector** only when its evolution is required to represent or materially predict at least one of:
- a thermally conditioned capability or constraint;
- activation or evolution of a qualified thermal interdependency;
- a critical transition time;
- an interdependency propagation delay;
- an electricity-service trajectory;
- a mobility-service trajectory;
- a declared recovery trajectory;
- a bounded downstream resilience or sustainability consequence that depends on that state.

This is the formal state-admission expression of the thesis rule of **minimum sufficient physics**.

## 3. State classes used in this thesis

### 3.1 Fast thermal physical states

These describe temperature-related physical condition over the operational thermal horizon.

Candidate examples, subject to final case qualification, include:

```math
X_P^{th}(t)
=
\begin{bmatrix}
\theta_{TO}(t)\\
\theta_{HS}(t)
\end{bmatrix},
```

for transformer top-oil and winding hottest-spot temperatures, and potentially

```math
X_{T_e}^{th}(t)
=
\begin{bmatrix}
T_{EVSE}(t)\\
T_B(t)
\end{bmatrix}
```

where EVSE or battery temperature is admitted only if it is needed by the selected thermal mechanism.

### 3.2 Operational / energy states

A variable may be a valid system state without being a thermal state.

For example,

```math
SOC(t)
```

is an evolving vehicle energy state.

Therefore:

```text
SOC is a state
SOC is not a thermal state
```

A broader Electrified Transportation state representation may be written as

```math
X_{T_e}(t)
=
\begin{bmatrix}
X_{T_e}^{th}(t)\\
X_{T_e}^{en}(t)
\end{bmatrix},
\qquad
X_{T_e}^{en}(t)=SOC(t),
```

when SOC is required to translate thermal charging capability into mobility consequence.

### 3.3 Slow degradation / health states

Aging and degradation can be legitimate state variables.

For transformer insulation, a generic degradation state may be written as

```math
A_{tr}(t)
```

or represented through a justified health variable such as accumulated loss of life or another evidence-supported insulation-condition quantity.

The important distinction is:

```text
aging/degradation can be a state
≠
aging/degradation must be an active state in this thesis
```

A slow degradation state is activated only if its evolution over the selected heat-event and analysis horizon materially changes the modeled thermal interdependency, capability, timing, service trajectory, recovery trajectory, or bounded downstream assessment.

Thus:

```text
fast thermal state
≠
operational / energy state
≠
slow degradation / health state
≠
service
```

## 4. What is not treated as a state under the active thesis convention

### 4.1 External heat forcing

Extreme heat is treated as exogenous forcing:

```math
H(t)=T_a(t)
```

or, where spatial variation is required,

```math
H(x,t).
```

Therefore:

```math
H(t)\neq X_P^{th}(t).
```

External forcing acts on the system state. It is not itself an internal Power- or Electrified-Transportation state under the active modeling convention.

### 4.2 Capability

A thermally conditioned capability is an output or algebraic/constraint quantity derived from state unless the adopted component model provides independent dynamics requiring it to be augmented as a state.

Example:

```math
P_{available}(t)
=
\mathcal C_P\!\left(X_P^{th}(t)\right).
```

Therefore, by default:

```text
state ≠ capability
```

### 4.3 Service

Electricity and mobility services are performance/service outputs:

```math
Q_P(t),\qquad Q_T(t).
```

Therefore:

```text
state ≠ capability ≠ service
```

### 4.4 Coupling / interface object

A cross-system quantity such as

```math
Z_{PT}^{th}(t)
```

is not automatically a state.

It is treated as:
- an **algebraic coupling/exchange/constraint object** when it is determined instantaneously from states, inputs, and operating conditions; or
- an **interface state** only if the chosen physics gives it independent dynamic memory and its current value is required to predict future evolution.

This prevents the notation from turning every exchanged quantity into a state by definition.

## 5. Canonical meaning of time

In this thesis:

> **Time is the independent variable through which state evolution, thermal accumulation and inertia, critical transitions, cross-system propagation, service consequences, and—where explicitly modeled—recovery and degradation are ordered and quantified.**

The operational question is not only:

```text
What state is reached?
```

but:

```text
When is it reached?
How long does it persist?
When does it change capability?
How long before the consequence appears in the coupled system?
When does a service consequence appear?
If modeled, when is required service restored?
```

## 6. Why thermal behavior is inherently state-time

A generic lumped thermal balance is

```math
C_{th}\frac{dT}{dt}
=
\dot Q_{gen}
-
\dot Q_{out}.
```

Because of thermal storage/inertia, a change in forcing does not generally produce an instantaneous final state.

Therefore:

```text
same instantaneous forcing
≠
same instantaneous internal state
```

unless the initial state and relevant history are also equivalent under the adopted model.

The current state carries the information from prior evolution needed by the state model.

## 7. Distinct temporal quantities

The thesis must not use one generic “time to failure” quantity.

### 7.1 Heat-event onset and exposure duration

```math
t_0
```

denotes the declared heat-event/model onset, and

```math
t_{exposure}
```

denotes the duration of the relevant heat exposure.

### 7.2 Thermal / capability transition time

For a declared physical or operational boundary

```math
g_i(X_i(t),H(t),t)\le 0,
```

define

```math
\tau_i^C
=
\inf\left\{
t:
g_i(X_i(t),H(t),t)=0
\right\}.
```

It answers:

```text
When does the modeled component/system first enter the declared capability-limiting or critical condition?
```

A temperature crossing is not automatically a critical transition unless the boundary has physical or operational meaning and evidence.

### 7.3 Thermal-interdependency propagation delay

For a qualified source transition `i` and consequential receiver response `j`,

```math
\delta_{ij}^{th}
=
t_j^{response}
-
\tau_i^C.
```

It answers:

```text
How long after the qualified source transition does the declared consequential response appear in the coupled system?
```

Propagation delay requires an explicitly qualified directional mechanism. It is not graph distance and is not inferred from correlation alone.

### 7.4 Service-consequence / service-disruption onset

Let

```math
t_Q
```

denote the time at which a declared electricity or mobility service requirement first becomes unsatisfied, where applicable.

For example,

```math
Q_k(t)<Q_k^{req}(t).
```

Thus:

```text
critical thermal transition time
≠
service-disruption onset time
```

### 7.5 Operational deadline

For fleet/depot applications, a vehicle departure deadline may be denoted

```math
t_d.
```

A thermal/capability limitation becomes a mobility consequence only if it prevents the declared mobility requirement from being met by the relevant deadline or service window.

### 7.6 Recovery time

If recovery is explicitly modeled,

```math
t_R
```

is the time required to restore the declared service requirement.

Recovery time is not activated merely because the thesis title contains resilience.

### 7.7 Degradation / aging horizon

A slow degradation process has its own relevant horizon,

```math
t_{deg},
```

which may be much longer than the event-scale thermal response.

Therefore:

```text
thermal-response timescale
≠
operational/departure timescale
≠
service-disruption timescale
≠
recovery timescale
≠
aging/degradation timescale
```

## 8. Canonical state-time chain

The active physical chain is:

```text
Extreme Heat Forcing
→ State Evolution
→ Thermally Conditioned Capability / Constraint
→ Qualified Thermal Interdependency
→ Receiver-State / Operational Consequence
→ Electricity + Mobility Service Consequence
→ Resilience Interpretation
```

A compact mathematical representation is

```math
H(t)
\rightarrow
X(t)
\rightarrow
C(t)
\rightarrow
Z_{PT}^{th}(t)
\rightarrow
X_{receiver}(t)
\rightarrow
\{Q_P(t),Q_T(t)\}.
```

The exact ordering may contain feedback; the chain is a semantic traceability rule, not a claim that every admitted model is feed-forward.

## 9. Example logic

A candidate Power-to-Transportation sequence is:

```text
ambient extreme heat + electrical loading
→ transformer thermal-state evolution
→ thermal/capability boundary reached at tau_P^C
→ available charging capability changes
→ vehicle energy state evolves differently
→ mobility requirement is missed at or by t_d
→ Q_T < Q_T^req
```

A candidate Transportation-to-Power sequence is:

```text
heat-dependent vehicle/charging requirement
→ charging demand trajectory
→ transformer loading
→ transformer thermal-state evolution
→ capability/service consequence
```

Each arrow requires independent physical and evidential qualification.

## 10. Scale interpretation

The thesis may use state variables at different scales:

```text
Micro:
material/device states
e.g. junction temperature, cell temperature, insulation health

Meso:
component/subsystem states
e.g. transformer top-oil/hot-spot temperature, EVSE temperature, battery temperature

Macro:
system/service behavior
typically represented through capability, operation, and service outputs rather than by relabeling service as a physical state
```

The thesis bridge is:

```text
micro/meso physical state
→ meso capability
→ macro service consequence through time
```

Micro-scale detail is activated only when it materially affects that bridge.

## 11. State-admission test

For every candidate state `x_i(t)`, ask:

1. Is it a legitimate state under the adopted physical/operational model?
2. Is its initial/current value needed to predict subsequent evolution?
3. Does it participate in a qualified thermal mechanism?
4. Does it materially affect a capability, constraint, transition time, propagation delay, service trajectory, recovery trajectory, or bounded downstream assessment over the declared horizon?
5. Can it be observed, estimated, calibrated, or otherwise supported sufficiently for the intended claim?

If the variable is physically real but fails the active-model relevance/evidence test, it remains part of the conceptual physical system but is not activated in the reduced thesis state vector.

## 12. Permanent distinctions

```text
external heat forcing ≠ internal system state
thermal state ≠ operational/energy state
fast state ≠ slow degradation/health state
state ≠ capability
state ≠ service
capability ≠ service
coupling quantity ≠ state unless independent dynamics require it
critical transition time ≠ propagation delay
critical transition time ≠ service-disruption time
propagation delay ≠ recovery time
event-scale thermal response ≠ aging/degradation horizon
system-scope membership ≠ active model state
physical reality ≠ required model fidelity
simulation ≠ validation
```

## 13. Thesis-ready short definitions

> **State in this thesis refers to the minimum set of evolving physical, operational, energy, or degradation variables required to characterize the current modeled condition of the Power System and Electrified Transportation System and to determine their subsequent evolution under extreme-heat forcing. Thermal states are primary; non-thermal states are included only when required to represent the thermal interdependency or its consequences.**

> **Time in this thesis is the independent variable through which those states evolve and through which critical thermal transitions, interdependency propagation, service consequences, and—where explicitly modeled—recovery and degradation are ordered and quantified.**

Short form:

```text
State: What modeled condition is the system in now, such that we can determine what happens next?

Time: When and how does that condition evolve, cross a meaningful boundary, propagate, and affect service?

State + Time: How thermally driven system conditions evolve and generate coupled consequences.
```

## 14. Governance rule

These definitions control future use of *state* and *time* in the active thesis unless superseded by an explicitly versioned definition required by new evidence, supervisor/committee direction, or a higher ASU/SSEBE requirement.

Historical files remain unchanged for provenance where they do not control the active thesis.
