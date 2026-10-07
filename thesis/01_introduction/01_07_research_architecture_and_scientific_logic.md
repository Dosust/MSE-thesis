## 1.7 Research Architecture and Scientific Logic

**State-time authority:** `project/CANONICAL_STATE_TIME_DEFINITION_V1.md`

The active research architecture is deliberately short:

```text
1. Identify and qualify thermal states and directional thermal mechanisms
→
2. Model thermal interdependency evolution through state and time
→
3. Quantify transition timing, propagation timing, and service consequences
```

The architecture follows the frozen objectives.

### Canonical state-time semantics

State is the minimum set of evolving physical or operational variables required to determine the adopted model trajectory. Thermal states are primary; non-thermal operational states enter only where required by the thermal interdependency or service consequence.

Time represents state evolution and the timing of critical transitions, interdependency propagation, service consequences, and recovery where modeled.

```text
external forcing ≠ system state
state ≠ capability ≠ service
thermal state ≠ operational/energy state
transition time ≠ propagation delay ≠ service-consequence time ≠ recovery time
```

Exact active states remain open until qualified under minimum-sufficient physics.

### Step 1 — Thermal mechanism qualification

Define the thermally sensitive physical states, temperature-dependent capabilities, thresholds, and directional Power–Electrified Transportation mechanisms required by the study.

Output:

```text
qualified thermal mechanism set
+ thermally active state set
+ validity conditions
```

### Step 2 — Physics-based state-time model

Represent the evolution of the thermally active Power states, Electrified-Transportation states, and cross-system coupling quantities using minimum sufficient physics.

Structural form:

```math
X^{th}(t)=
\begin{bmatrix}
X_P^{th}(t)\\
Z_{PT}^{th}(t)\\
X_{T_e}^{th}(t)
\end{bmatrix}.
```

### Step 3 — Consequence quantification

Determine, where physically identifiable:

```math
\tau_i^C,
\qquad
\delta_{ij}^{th},
\qquad
Q_P(t),
\qquad
Q_T(t).
```

The final scientific chain is:

```text
Extreme Heat
→ Thermal State Evolution
→ Thermal Capability / Constraint
→ Qualified Thermal Interdependency
→ State-Time Consequence
→ Electricity / Mobility Service Consequence
```

Broader seven-stage, viability, organization, sustainability, and engineering-decision architectures are historical or supporting methods and are not the active thesis research architecture.
