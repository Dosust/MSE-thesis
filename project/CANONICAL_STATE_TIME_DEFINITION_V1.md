# Canonical State-Time Definition V1

**Status:** CANONICAL — FROZEN THESIS STATE-TIME INTERPRETATION AUTHORITY  
**Effective date:** 2026-10-08  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Scope authorities:** `CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md` + `CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`

## 1. Canonical meaning of state

> **State in this thesis refers to the minimum set of evolving physical or operational variables required to characterize the current condition of the Power System and Electrified Transportation System and to determine their subsequent evolution under extreme-heat forcing. The primary states of interest are thermal states; non-thermal states are included only where required to represent the thermal interdependency or its service consequence.**

Simple interpretation:

```text
State = what condition is the modeled system in?
```

A state variable is a variable whose current value, together with the inputs and model parameters, is required to determine the subsequent evolution of the adopted model.

Generic representation:

```math
\dot X(t)=F(X(t),H(t),u(t);\theta),
```

where:

- (X(t)) = modeled system state;
- (H(t)) = external forcing, including extreme heat;
- (u(t)) = control or operating action;
- (	heta) = model parameters.

This definition does **not** imply that every physically meaningful quantity is an active thesis state.

## 2. Primary state structure

The primary active state class is thermal:

```math
X_{th}(t)=
\begin{bmatrix}
X_{P,th}(t)\\
X_{T_e,th}(t)
\end{bmatrix}.
```

Candidate Power-system thermal states may include transformer top-oil and winding hottest-spot temperatures:

```math
X_{P,th}(t)
=
\begin{bmatrix}
\theta_{TO}(t)\\
\theta_{HS}(t)
\end{bmatrix},
```

subject to evidence, parameterization, and model admission.

Candidate Electrified Transportation thermal states may include an EVSE internal/rectifier temperature and, only where necessary, battery temperature:

```math
T_{EVSE}(t), \qquad T_B(t).
```

These examples are **candidate state variables, not a frozen exact active state set**. The exact active states remain OPEN until the application case, mechanisms, parameters, and model-validity evidence are frozen.

## 3. Not everything is a state

### 3.1 External forcing is not system state

Ambient/extreme-heat forcing may be represented as:

```math
H(t)=T_a(t).
```

Preserve:

```text
external heat forcing ≠ system thermal state
```

The forcing changes system states; it is not itself a Power- or Electrified-Transportation-system state.

### 3.2 Capability is not state

A capability may be a function of state:

```math
P_{available}(t)=\mathcal C_P(X_{P,th}(t)).
```

Preserve:

```text
State ≠ Capability
```

State describes physical/operational condition. Capability describes what the system or component can currently do.

### 3.3 Service is not state

Electricity and mobility services are system/service outputs:

```math
Q_P(t)=\text{electricity-service trajectory},
```

```math
Q_T(t)=\text{mobility-service trajectory}.
```

Preserve:

```text
State ≠ Capability ≠ Service
```

### 3.4 SOC is an operational/energy state, not a thermal state

```math
SOC(t)
```

is an evolving energy/operational state where it is required by the model.

Preserve:

```text
SOC ≠ thermal state
```

If a broader Electrified Transportation state vector is required:

```math
X_{T_e}(t)=
\begin{bmatrix}
X_{T_e,th}(t)\\
X_{T_e,en}(t)
\end{bmatrix},
\qquad
X_{T_e,en}(t)=SOC(t).
```

## 4. State-admission rule

A physically meaningful quantity is admitted as an **active thesis state** only when its evolution is required to predict the adopted model trajectory and materially affects at least one of:

- the qualified thermal-interdependency mechanism;
- a thermal capability boundary or critical transition;
- an electricity- or mobility-service trajectory;
- a validation result;
- an engineering conclusion.

Therefore:

```text
physical quantity ≠ state variable ≠ active thesis state
```

The governing principle remains **minimum sufficient physics**.

## 5. Canonical meaning of time

> **Time in this thesis represents the temporal evolution of those states and the timing of critical thermal transitions, interdependency propagation, service degradation, and, where modeled, service recovery.**

Simple interpretation:

```text
Time = when and how state changes and consequences propagate.
```

The thesis is dynamic rather than snapshot-based:

```math
X(t_0)\rightarrow X(t_1)\rightarrow X(t_2)\rightarrow\cdots
```

Thermal inertia is central. A generic thermal balance may be written:

```math
C_{th}\frac{dT}{dt}
=
\dot Q_{gen}
-
\dot Q_{out}.
```

Hence the same instantaneous external forcing need not imply the same instantaneous system state because the current state carries thermal history.

Preserve:

```text
same forcing ≠ same instantaneous state
```

## 6. Distinct temporal quantities

### 6.1 Exposure time

```math
t_{exposure}
```

is the duration over which the defined extreme-heat forcing acts.

### 6.2 Critical thermal transition time

```math
\tau_i^C
=
\inf\left\{
t:
g_i(X_i(t))=0
\right\}.
```

It identifies the first time a declared state/capability boundary is reached.

### 6.3 Thermal-interdependency propagation delay

If the source-system transition occurs at (	au_i^C) and a consequential receiver-system response is identified at (t_j^{response}), then:

```math
\delta_{ij}^{th}
=
t_j^{response}-\tau_i^C.
```

This quantity is admitted only when the source transition, receiver response, and causal/coupling relation are operationally defined and identifiable.

### 6.4 Service-consequence time

A service consequence may occur after the underlying thermal transition and capability change.

Preserve:

```text
thermal transition time ≠ service-consequence time
```

### 6.5 Recovery time

```math
t_R
```

is used only if recovery is explicitly represented and required service is operationally defined.

Preserve:

```text
transition time ≠ propagation delay ≠ service-consequence time ≠ recovery time
```

## 7. State and time together

State tells **what condition the modeled system is in**.

Time tells **how that condition evolves, when critical transitions occur, and when consequences propagate to the coupled system and service layer**.

Canonical short interpretation:

```text
State + Time = dynamic physical evolution and the timing of coupled service consequences.
```

The governing chain is:

```text
Extreme Heat
→ Thermal State Evolution
→ Thermal Capability / Constraint
→ Qualified Thermal Interdependency
→ State-Time Consequence
→ Electricity / Mobility Service Consequence
```

A compact mathematical representation is:

```math
H(t)
\rightarrow
X_{th}(t)
\rightarrow
C(t)
\rightarrow
Z_{PT}^{th}(t)
\rightarrow
\{\tau^C,\delta^{th},Q_P(t),Q_T(t)\}.
```

## 8. Scale interpretation

The thesis may distinguish state variables by physical scale where useful:

### Micro

Material/device-scale physical states, for example semiconductor junction temperature or cell-level temperature.

### Meso

Component/subsystem states, for example transformer top-oil/hottest-spot temperature, EVSE internal temperature, or battery-pack temperature.

### Macro

The model generally transitions from physical state to capability, system operation, and service rather than treating service itself as a physical state.

Preserve:

```text
micro/meso physical state → macro capability/service consequence through time
```

Micro-scale detail is admitted only when it materially changes the thermal-interdependency or service result.

## 9. Permanent distinctions

```text
external forcing ≠ system state
physical quantity ≠ state variable ≠ active thesis state
thermal state ≠ operational/energy state
state ≠ capability ≠ service
transition time ≠ propagation delay ≠ service-consequence time ≠ recovery time
thermal exposure ≠ thermal interdependency
common heat exposure ≠ directional dependency
```

## 10. What remains OPEN

This authority freezes the **meaning of state and time**, not the final model contents.

The following remain OPEN until independently qualified:

- exact active Power-system state variables;
- exact active Electrified Transportation state variables;
- whether battery temperature is required;
- exact capability laws and thresholds;
- exact service definitions (Q_P(t)) and (Q_T(t));
- exact event horizon and sampling resolution;
- exact critical-transition and propagation-identification procedures;
- recovery-time use, unless recovery is explicitly modeled.

## 11. Reopen conditions

This authority may be changed only through an explicit versioned amendment authorized by the user, supervisor/chair/committee direction, contradictory evidence or infeasibility, or a higher ASU/SSEBE requirement.
