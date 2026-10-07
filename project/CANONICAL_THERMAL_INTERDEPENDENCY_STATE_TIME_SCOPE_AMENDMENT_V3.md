# Canonical Thermal-Interdependency State-Time Scope Amendment V3

**Status:** CANONICAL — FROZEN ACTIVE THESIS SCOPE  
**Effective date:** 2026-10-07  
**Supersedes for active scope:** `CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V2.md`  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**

## 1. Permanent active-scope rule

The thesis is restricted to **thermal interdependencies between the Power System and the Electrified Transportation System and the consequences of those interdependencies through physical state and time**.

The active scientific chain is:

```text
Extreme heat
→ thermal state / temperature-dependent capability
→ qualified thermal P ↔ T_e interdependency
→ state-time evolution
→ critical transition / propagation timing
→ electricity + mobility service consequence
```

No broader interdependency family is active unless it is required as a boundary condition for the thermal mechanism and is explicitly admitted.

## 2. Physical systems

```text
Power System P
↔
Electrified Transportation System T_e
```

The Electrified Transportation System boundary remains controlled by `CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`.

> **In this thesis, the electrified transportation system comprises the electrically propelled road vehicle, its rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, the vehicle power-supply circuit, electric-vehicle supply equipment, the physical charging connection, and the communication and control functions required for electrical power transfer, including bidirectional transfer where supported (ISO 6469; ISO 5474; ISO 15118; IEC 61851; IEC 62196).**

EVSE belongs to `T_e`. Cross-system coupling/interface variables are mathematical objects representing exchange, constraints, or dependency conditions and do not constitute a third physical infrastructure system.

## 3. Definition of thermal interdependency

A directional Power–Electrified Transportation relation is active only when a **temperature or thermal state changes the activation, strength, capacity, timing, or consequence of the cross-system dependency**.

A thermal interdependency therefore requires:

```text
thermal forcing/state
+
qualified directional mechanism
+
source-state or capability change
+
cross-system effect
+
receiver-state or service consequence
+
time
```

Common heat exposure alone is not an interdependency:

```text
common heat exposure ≠ thermal interdependency
```

A structural connection alone is not an interdependency:

```text
connection ≠ dependency
```

## 4. Active directional pathways

### Power → Electrified Transportation

The active pathway is of the form:

```text
Power-system thermal state / temperature-dependent capacity
→ electrical capability available to T_e
→ EVSE charging capability
→ vehicle energy state / availability
→ mobility consequence
```

Only the minimum physical states required to establish and quantify this pathway are modeled.

### Electrified Transportation → Power

The active pathway is of the form:

```text
T_e thermal state / temperature-dependent charging or transfer capability
→ EVSE charging demand or supported reverse transfer
→ electrical demand/exchange at the P–T_e boundary
→ Power-system state/capability consequence
```

Bidirectional transfer is included only where supported by the selected technology, data, and experiment.

## 5. State-time analytical focus

The primary analytical objects are physical state and time.

A structural state container may be written as:

```math
X(t)=
\left[
X_P^{\top}(t),
Z_{PT}^{\top}(t),
X_{T_e}^{\top}(t)
\right]^{\top},
```

with extreme-heat forcing `H(x,t)`.

Only thermally relevant states and exchanged quantities are activated.

Derived quantities may include:

```math
\tau_i^C
=
\text{critical thermal transition time},
```

```math
\delta_{ij}
=
\text{thermal-interdependency propagation delay},
```

```math
Q_P(t),\;Q_T(t)
=
\text{electricity and mobility service trajectories}.
```

## 6. Active outputs

The thesis may quantify:

- thermal state trajectories;
- temperature-dependent capability or derating;
- activation of qualified thermal interdependencies;
- critical transition timing;
- cross-system propagation timing;
- electricity-service consequences;
- mobility-service consequences;
- recovery of those services only where recovery is needed to interpret the thermal consequence.

## 7. Explicitly outside active analytical scope

The active thesis does **not** study as primary research objects:

- generic non-thermal Power–Transportation interdependencies;
- repair-crew accessibility or logistics unless required as a fixed boundary condition;
- broad Information or Organization networks;
- generic institutional or governance interdependencies;
- all-hazard resilience;
- flooding, storms, earthquakes, or other hazards;
- comprehensive sustainability optimization;
- broad economic-development modeling;
- full life-cycle assessment;
- generic multiobjective infrastructure transformation;
- universal intervention optimization;
- non-thermal restoration mechanisms;
- all transportation modes.

These items may appear only as literature context, boundary conditions, limitations, or future work unless a formally versioned scope amendment reopens them.

## 8. Minimum-sufficient-physics rule

The thesis models only the physics required to answer the thermal-interdependency state-time question.

```text
system-scope membership ≠ mandatory detailed model
```

A component or state is activated only if it changes:
- a thermal threshold;
- a directional thermal dependency;
- a transition time;
- a propagation delay;
- an electricity-service prediction; or
- a mobility-service prediction.

## 9. Permanent scientific distinctions

```text
external heat forcing ≠ system thermal state
common heat exposure ≠ thermal interdependency
structural connection ≠ directional dependency
EVSE ∈ T_e
interface variable ≠ third physical system
state ≠ function ≠ service
transition time ≠ propagation delay ≠ recovery time
temperature correlation ≠ causal thermal mechanism
simulation ≠ validation
```

## 10. Governance

This file is the controlling scope authority for all future thesis work unless the user, supervisor, chair, committee, or a formally versioned scope amendment explicitly changes it.

Earlier broad seven-stage, RQ1–RQ7, P–T–I–O, intervention, sustainability, and decision architectures are retained for provenance and reusable methods but do not control the active research scope where they conflict with this amendment.
