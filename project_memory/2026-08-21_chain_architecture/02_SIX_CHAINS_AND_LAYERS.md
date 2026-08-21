# Six Scientific Chains and Their Layers

## Why six chains

The project no longer treats all research activities as one linear sequence. The six chains separate different classes of questions about the same infrastructure system.

A **chain** is a family of scientific transformations/questions. A **layer** is a distinct stage inside that family. Cross-cutting tools such as optimization, UQ, machine learning, numerical analysis and statistics should not be confused with physical stages.

---

# Chain I — Physical System

**Question:** What is the system and what governs it?

```text
physical laws → structure → interdependencies → interfaces → states/flows → dynamics → cascades
```

### I.1 Physical laws
Generic balance template:

```text
∂q/∂t + div(J_q) = s_q
```

Sector-specific forms can represent energy balance, hydraulic/mass balance, transport flow conservation and waste/material accumulation.

### I.2 Structure
Single-sector graph: `G_s=(V_s,E_s)`.

Multilayer system:

```text
G = {G_P,G_W,G_T,G_SW,I}
```

Coupling operator:

```text
A(t) = block matrix with diagonal intra-sector blocks and off-diagonal cross-sector blocks
```

### I.3 Interdependency
Statement that one sector/state influences another.

Example: `P → W` because pumping requires electricity.

### I.4 Interface
The actual mechanism implementing the interdependency, e.g.

```text
I_ij : (X_i,X_j,Z_ij,eta) → cross-sector exchange / constraint
```

Important distinction:

```text
connection ≠ interdependency ≠ interface mechanism
```

### I.5 State / flows

```text
X=[X_P,X_W,X_T,X_SW]^T
```

Each sector state may itself be high-dimensional.

### I.6 Dynamics

```text
M(X) X_dot = F(X,Z,m,u,eta;theta)
epsilon Z_dot = G(X,Z,m,eta;theta)
```

### I.7 Cascades
Local component/interface changes can modify topology/flows, generate redistribution and cause cross-sector failures.

**Chain-I output:** a physically meaningful forward model `F_dyn`.

---

# Chain II — Observation, Inference and Prediction

**Question:** What do we know about the system and how certain are we?

```text
observe → observability → identify → estimate → assimilate → UQ → predict
```

### II.1 Observation

```text
Y(t)=H(X(t),Z(t);theta)+epsilon_Y(t)
```

Usually `Y != X` because the full state is not observed.

### II.2 Observability
Ask whether the hidden state can be reconstructed from available measurements under the declared model.

### II.3 Identification
Estimate unknown interface/model parameters or structure.

```text
theta_hat = argmin_theta [data misfit + regularization]
```

### II.4 Identifiability
Ask whether different parameters can generate indistinguishable observations.

```text
G(theta1)=G(theta2) => theta1=theta2 ?
```

### II.5 State estimation / data assimilation

```text
p(X_t | Y_0:t)
```

### II.6 UQ
Posterior or confidence representation, e.g.

```text
p(theta|Y) ∝ p(Y|theta)p(theta)
```

### II.7 Prediction

```text
p(X_future | Y_history, future hazard scenario)
```

**Chain-II output:** estimated states/interfaces/parameters + uncertainty + forecast.

---

# Chain III — Hazard, Failure and Consequence

**Question:** How does disturbance become physical damage, service loss and societal consequence?

```text
hazard → exposure → vulnerability → damage → failure → cascade → functionality loss → service loss → consequence → risk
```

### III.1 Forcing versus realized hazard

```text
xi(t) → eta(t)
```

Example: rainfall forcing `xi` becomes local inundation/flood stress `eta` through environmental and infrastructure conditions.

### III.2 Exposure

```text
eta_i = eta(x_i,t)
```

### III.3 Vulnerability / fragility
A representative lognormal fragility family:

```text
P(D_i >= d_s | IM) = Phi((ln IM - ln mu_i,ds)/beta_i,ds)
```

### III.4 Failure / hybrid transition

```text
m_i(t-) → m_i(t+)
A(t-) → A(t+)
```

### III.5 Cascading disruption

```text
local damage → redistribution → cross-sector failure
```

### III.6 Service mapping

```text
S(t)=Psi(X(t),m(t),Z(t))
```

### III.7 Service deficit / consequence

```text
D_i(t)=[S_i^req-S_i(t)]_+
L=∫ Σ_i w_i D_i(t) dt
```

**Chain-III output:** damage/failure/service-loss/consequence trajectories.

---

# Chain IV — Resilience, Viability, Recovery and Control

**Question:** Can the system remain acceptable, and if disrupted can it recover?

```text
state → admissibility → viability → reachability → service continuity → recoverability → recovery → control
```

### IV.1 Admissibility

```text
K_R=K_phys ∩ K_service ∩ K_sus ∩ K_eq
```

### IV.2 Viability

```text
V_R={x0 in K_R : exists u(.) keeping X(t) in K_R}
```

### IV.3 Reachability
Controlled reachable sets answer which states can be reached under admissible controls/disturbances.

Representative HJ/HJI family:

```text
∂_t V + H(x,∇V)=0
```

with min/max order depending on the target/disturbance convention.

### IV.4 Classical resilience-performance metrics
A generic performance-loss form:

```text
R = 1 - [∫(Q0-Q(t))dt] / [Q0(tf-t0)]
```

This answers a different question from viability. Performance metrics summarize loss/recovery curves; viability tests state-space feasibility.

### IV.5 Recovery/capture

```text
C_R={x0 : exists u(.), finite T, X(T) in V_R}
```

### IV.6 Recovery time

```text
tau_R(x0)=inf{T : exists u(.), X(T) in V_R}
```

### IV.7 Control
First ask whether a viable/recovery control exists; optimization can follow.

**Chain-IV output:** `V_R`, `∂V_R`, `C_R`, `tau_R`, viable/recovery control sets.

---

# Chain V — Engineering Lifecycle / Action

**Question:** What can engineers physically change over the lifecycle?

```text
requirements → design → deploy → operate → monitor → maintain → restore → retrofit → adapt → circularize
```

### V.1 Design

```text
d={topology,capacity,redundancy,storage,interface hardening,...}
```

```text
d → F_d → V_R(d), C_R(d)
```

### V.2 Operation
Fast decision/control on the existing design:

```text
u(t)=pi(X(t))
```

### V.3 Monitoring
Feeds Chain II with observations and supports state/interface estimation.

### V.4 Maintenance
Changes deterioration/failure dynamics and future risk.

### V.5 Restoration
Post-disaster scheduling/resource-allocation problem under physical and resource constraints.

### V.6 Retrofit / adaptation
Long-horizon design changes under changing hazard distributions/nonstationarity.

### V.7 Circularity
May constrain material/resource choices and lifecycle recovery/reuse, but is not the mathematical center of the present MSE.

**Chain-V output:** operations, repair schedules, designs and adaptation pathways.

---

# Chain VI — Sustainability, Evaluation and Decision

**Question:** Which technically feasible option should society choose?

```text
needs → alternatives → evaluate → trade off → decide → implement → learn → revise
```

### VI.1 Evaluation vector

```text
J(d,u)=[economic cost, carbon, service loss, inequity, recovery time, risk,...]
```

### VI.2 Sustainability
Can be a hard constraint, not just another weight:

```text
carbon(d) <= threshold
resource use(d) <= threshold
```

### VI.3 Equity
Can be represented by group-specific service floors or other explicitly justified measures:

```text
S_g(t) >= S_g^min for all declared groups g
```

### VI.4 Tradeoffs
Multiobjective optimization may produce a Pareto set rather than one universal optimum.

### VI.5 Decision under uncertainty
Possible forms include expected utility, CVaR, robust/minimax or other declared risk criteria.

### VI.6 Implementation
Adds institutional, budget, jurisdictional and governance constraints not derivable from physics alone.

### VI.7 Learning
Post-implementation observations feed Chain II again.

**Chain-VI output:** evaluated alternatives, Pareto/decision set, selected action and learning loop.

---

# Interaction among chains

The most useful conceptual coupling is:

```text
I Physical System → III Hazard/Failure → IV Viability/Recovery → V Engineering Action → VI Decision
```

while

```text
II Information/Inference ↔ I, III, IV, V
```

and

```text
VI → IV
```

because societal sustainability/equity requirements help define the admissible set `K_R`.

## One core object per chain

| Chain | Core object | Meaning |
|---|---|---|
| I | `F` / dynamic operator | what governs the system |
| II | `p(X,theta,Z | D)` | what is known |
| III | `eta,m,S,L` | what happens under stress |
| IV | `V_R,C_R` | what can survive/recover |
| V | `u,d` | what engineers can change |
| VI | `J,Pareto,a*` | what is chosen |

## Current mathematical effort priority

The current discussion ranked mathematical emphasis approximately as:

- Chain I physical-system/coupled dynamics: highest mathematical-physics priority;
- Chain IV viability/recovery/control: highest theorem/geometry opportunity;
- Chain II inverse problems/UQ: essential for identification reliability;
- Chain III hazard/failure: provides forcing and hybrid transitions;
- Chain V design/restoration: strong applied-math/optimization layer;
- Chain VI sustainability/equity/decision: essential to meaning/admissibility but should not dominate the mathematical core.

The strongest research spine is therefore `Chain I + Chain II + Chain IV`, with Chain III supplying disturbances, Chain V supplying engineering action, and Chain VI defining admissibility/value constraints.