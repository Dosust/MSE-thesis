## 3.1 Canonical State-Time Definitions

The thesis uses *state* and *time* in a precise dynamical-systems sense controlled by `project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`.

### State

> **State in this thesis refers to the minimum set of evolving physical, operational, energy, or degradation variables required to characterize the current modeled condition of the Power System and Electrified Transportation System and to determine their subsequent evolution under extreme-heat forcing. Thermal states are primary; non-thermal states are included only when required to represent the thermal interdependency or its consequences.**

A generic state representation is

```math
\dot X(t)=F\!\left(X(t),H(t),u(t);\theta\right).
```

The thesis distinguishes the full physical state space from the active reduced model state:

```text
full physical state space
≠
active reduced thesis state vector
```

Candidate state classes include:

```text
fast thermal physical states
+ operational / energy states
+ slow degradation / health states
```

For example:

```math
X_P^{th}(t)
=
\begin{bmatrix}
\theta_{TO}(t)\\
\theta_{HS}(t)
\end{bmatrix},
```

while

```math
SOC(t)
```

is an energy state rather than a thermal state.

Aging may also be a legitimate state:

```math
A_{tr}(t),
```

but it enters the active state vector only if its evolution over the declared analysis horizon materially changes the thermal interdependency, capability, transition timing, propagation timing, service trajectory, recovery trajectory, or bounded downstream assessment.

### Forcing, capability, coupling, and service are distinct

Extreme heat is treated as external forcing:

```math
H(t)=T_a(t),
qquad
H(t)\neq X_P^{th}(t).
```

A thermally conditioned capability is generally derived from state:

```math
P_{available}(t)
=
\mathcal C_P\!\left(X_P^{th}(t)\right).
```

Electricity and mobility services are outputs:

```math
Q_P(t),\qquad Q_T(t).
```

A cross-system coupling quantity `Z_{PT}^{th}(t)` is not automatically a state. It is an interface state only if the adopted physics gives it independent dynamic memory; otherwise it is treated as an algebraic exchange/constraint object.

Therefore:

```text
external forcing
≠ state
≠ capability
≠ service
```

and:

```text
coupling quantity
≠ state unless independent dynamics require it
```

### Time

> **Time in this thesis is the independent variable through which those states evolve and through which critical thermal transitions, interdependency propagation, service consequences, and—where explicitly modeled—recovery and degradation are ordered and quantified.**

Thermal inertia makes the problem inherently dynamic:

```math
C_{th}\frac{dT}{dt}
=
\dot Q_{gen}
-
\dot Q_{out}.
```

Hence a change in extreme-heat forcing does not generally produce an instantaneous final internal state.

### Distinct temporal quantities

The thesis distinguishes:

```text
heat-event onset / exposure duration
≠ critical thermal transition time
≠ interdependency propagation delay
≠ service-disruption onset
≠ operational departure deadline
≠ recovery time
≠ degradation / aging horizon
```

For a declared boundary

```math
g_i(X_i(t),H(t),t)\le 0,
```

critical transition time is

```math
\tau_i^C
=
\inf\left\{
t:
g_i(X_i(t),H(t),t)=0
\right\}.
```

For a qualified source transition `i` and receiver response `j`,

```math
\delta_{ij}^{th}
=
t_j^{response}
-
\tau_i^C.
```

A service consequence may occur later when

```math
Q_k(t)<Q_k^{req}(t).
```

### State-time thesis logic

The canonical traceability chain is

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

The exact model may contain feedback; this chain is a semantic and evidential traceability rule rather than a universal feed-forward equation.

### State-admission rule

A candidate state is activated only if:

1. it is a legitimate state under the adopted physical or operational model;
2. its current value is needed to predict subsequent evolution;
3. it participates in a qualified thermal mechanism;
4. it materially affects a capability, transition, propagation delay, service trajectory, recovery trajectory, or bounded downstream assessment over the declared horizon; and
5. it can be sufficiently observed, estimated, calibrated, or otherwise supported for the intended claim.

This is the operational form of **minimum sufficient physics**.
