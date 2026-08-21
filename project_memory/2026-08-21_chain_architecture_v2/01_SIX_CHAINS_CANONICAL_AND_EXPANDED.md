# Six Chains — Canonical Compact Form and Expanded Layer Decomposition

This file corrects an issue in v1: the compact chain wording used in the conversation and the later expanded layer decomposition are **both useful**, but they are not identical. Future chats should preserve the compact ontology and treat the expanded layers as a finer decomposition rather than silently replacing the original chain.

# A. Canonical compact six-chain wording

## Chain I — Physical-system chain

```text
Physics
→ Structure
→ Interfaces
→ Dynamics
```

Question: **What is the system and how does it evolve?**

## Chain II — Observation / inference chain

```text
Observe
→ Identify
→ Estimate
→ Predict
```

Question: **What can be known from data and how uncertain is that knowledge?**

## Chain III — Disturbance / failure chain

```text
Hazard
→ Failure
→ Service Loss
→ Consequences
```

Question: **What happens when the system is stressed?**

## Chain IV — Resilience / viability chain

```text
Admissibility
→ Viability
→ Resilience
→ Recovery
→ Control
```

Question: **Can the system remain acceptable or recover, and what interventions make that possible?**

## Chain V — Engineering-action chain

```text
Design
→ Operate
→ Maintain
→ Restore
→ Plan
→ Adapt
```

Question: **What can engineers change over the system lifecycle?**

## Chain VI — Evaluation / decision chain

```text
Evaluate
→ Trade off
→ Decide
→ Implement
→ Learn
```

Question: **Which feasible action should be chosen and how is the decision revised after implementation?**

---

# B. Expanded layer decomposition

The expanded decomposition adds scientifically distinct intermediate layers without changing the six-chain ontology.

## Chain I — Expanded

```text
physical laws
→ constitutive relations
→ structure/topology
→ interdependencies
→ interface mechanisms
→ states/flows
→ continuous dynamics
→ hybrid modes
→ cascades
```

### I.1 Physical laws
Generic conservation/balance template:

```text
∂q/∂t + div(J_q) = s_q
```

Sector-specific equations must be used for power, water/drainage, transport and solid waste.

### I.2 Structure
Single-sector graph:

```text
G_s=(V_s,E_s)
```

Coupled multilayer system:

```text
G={G_P,G_W,G_T,G_SW,I}
```

### I.3 Interdependency
A dependence statement such as `P → W` says one subsystem affects another, but does not yet specify the physical mechanism.

### I.4 Interface mechanism
The interface is the mechanism implementing the dependency. Candidate state/parameter representation:

```text
I_ij : (X_i,X_j,Z_ij,eta;theta_ij) → exchange/constraint/capacity/failure relation
```

Frozen conceptual rule:

```text
connection != interdependency != interface mechanism
```

### I.5 State / flow

```text
X=[X_P,X_W,X_T,X_SW]^T
```

Each sector state may be high dimensional.

### I.6 Dynamics

```text
X_dot=F(X,Z,m,u,eta;theta)
epsilon Z_dot=G(X,Z,m,eta;theta)
```

### I.7 Hybrid mode / cascade

```text
m+ = Phi(X,Z,m,eta)
```

A failure may alter topology/parameters and create redistribution or cross-sector propagation.

**Output of Chain I:** a defensible forward dynamical model.

---

## Chain II — Expanded

```text
observe
→ sensing/sampling
→ observability
→ identify structure/parameters
→ estimate hidden state
→ assimilate data
→ quantify uncertainty
→ predict
```

### II.1 Observation

```text
Y=H(X,Z;theta)+epsilon_Y
```

Usually `Y != X`.

### II.2 Observability
Ask whether hidden states can be reconstructed from the chosen measurements and model.

### II.3 Identification
Estimate unknown interface/model structure or parameters.

### II.4 Identifiability
Ask whether different parameter values can produce indistinguishable observations.

### II.5 State estimation

```text
p(X_t | Y_0:t)
```

### II.6 Bayesian/UQ layer

```text
p(theta|Y) ∝ p(Y|theta)p(theta)
```

### II.7 Prediction

```text
p(X_future | Y_history, hazard scenario)
```

**Output of Chain II:** estimated states/interfaces/parameters + uncertainty + forecast.

---

## Chain III — Expanded

```text
climate forcing
→ realized hazard
→ exposure
→ vulnerability/fragility
→ damage
→ failure/mode switch
→ cascade
→ functionality loss
→ service loss
→ consequence
→ risk
```

### III.1 Forcing versus hazard

```text
xi(t) → eta(t)
```

For the demonstrator, rainfall forcing and local inundation are distinct objects.

### III.2 Exposure

```text
eta_i=eta(x_i,t)
```

### III.3 Vulnerability / fragility
A representative lognormal family is:

```text
P(D_i >= d_s | IM)=Phi((ln IM-ln mu_i,ds)/beta_i,ds)
```

This is a generic family, not a universal infrastructure equation. Final models need sector/hazard-specific evidence.

### III.4 Failure
Representable as a hybrid transition/topology change.

### III.5 Service mapping

```text
S(t)=Psi(X(t),m(t),Z(t))
```

### III.6 Service deficit / consequence

```text
D_i(t)=[S_i^req-S_i(t)]_+
L=∫ sum_i w_i D_i(t) dt
```

**Output of Chain III:** hazard-to-service-loss/consequence trajectory.

---

## Chain IV — Expanded

```text
admissibility
→ viability
→ reachability
→ resilience performance
→ recoverability
→ capture/recovery geometry
→ recovery time
→ control feasibility
```

### IV.1 Admissibility

```text
K_R=K_phys ∩ K_service ∩ K_sus ∩ K_eq
```

### IV.2 Viability

```text
V_R={x0 in K_R : exists admissible u(.) keeping the trajectory in K_R}
```

### IV.3 Reachability
Representative HJ/HJI family:

```text
∂_t V + H(x,∇V)=0
```

The exact sign/min-max convention depends on the declared reachability game.

### IV.4 Classical resilience performance
A representative normalized loss/recovery metric family can be written as:

```text
R = 1 - [∫(Q0-Q(t))dt]/[Q0(tf-t0)]
```

This is not the same object as a viability kernel.

### IV.5 Recovery / capture

```text
C_R={x0 : exists admissible u(.), finite T, X(T) in V_R}
```

### IV.6 Recovery time

```text
tau_R(x0)=inf{T : exists admissible u(.), X(T) in V_R}
```

### IV.7 Control
First ask whether an admissible viability/recovery control exists. Optimization may follow.

**Output of Chain IV:** `V_R`, `∂V_R`, `C_R`, `tau_R`, admissible control sets.

---

## Chain V — Expanded

```text
requirements
→ design
→ deploy
→ operate
→ monitor
→ maintain
→ restore
→ retrofit
→ plan
→ adapt
→ circularize where relevant
```

Design variables:

```text
d={topology,capacity,redundancy,storage,interface hardening,...}
```

Design dependence:

```text
d → F_d → V_R(d), C_R(d)
```

Operation acts on the built design through `u(t)`.

Monitoring feeds Chain II.

Maintenance changes deterioration/failure dynamics.

Restoration is a constrained recovery scheduling/resource allocation problem.

Adaptation changes design/operation under nonstationary hazards.

**Output of Chain V:** operational interventions, repair schedules, designs and adaptation pathways.

---

## Chain VI — Expanded

```text
needs/performance goals
→ alternatives
→ evaluation
→ sustainability/equity constraints
→ tradeoffs
→ decision under uncertainty
→ implementation
→ learning/revision
```

A multi-criteria evaluation vector may include:

```text
J=[economic cost, carbon/resource use, service loss, inequity, recovery time, risk,...]
```

Sustainability can be a hard constraint rather than merely a weight.

Equity can be represented by explicitly justified group/service constraints, not a generic label.

Multiobjective optimization may return a Pareto set rather than one universal optimum.

Implementation introduces institutions, budgets, jurisdiction and governance.

Learning sends new data back to Chain II.

**Output of Chain VI:** evaluated alternatives, decision set, chosen action and learning loop.

---

# C. How the six chains interact

A useful structural view is:

```text
I Physical system
→ III Hazard/failure/consequence
→ IV Viability/recovery/control
→ V Engineering action
→ VI Decision
```

while:

```text
II Observation/inference ↔ I, III, IV, V
```

and:

```text
VI → IV
```

because sustainability/equity/service requirements help define the admissible set `K_R`.

## One core object per chain

| Chain | Core object | Meaning |
|---|---|---|
| I | `F` / coupled dynamic operator | what governs the system |
| II | `p(X,theta,Z|D)` | what is known |
| III | `eta,m,S,L` | what happens under stress |
| IV | `V_R,C_R` | what can survive/recover |
| V | `u,d` | what engineers can change |
| VI | `J`, Pareto/decision set | what is selected |

# D. Present thesis position

The strongest current MSE spine is:

```text
Chain I + Chain II + Chain IV
```

with Chain III supplying physically meaningful disturbances/failures, Chain V supplying engineering intervention, and Chain VI supplying sustainability/equity/decision constraints.

This is a scope statement, not a claim that the other chains are unimportant.