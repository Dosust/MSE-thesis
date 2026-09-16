# Minimal P–T–I–O Mechanism Set v1.0

**Date:** 2026-09-16  
**Status:** FROZEN WORKING MECHANISM SET; PARAMETER CALIBRATION/EMPIRICAL VALIDATION PENDING  
**Purpose:** preserve the minimum causal content required to test the thesis chain `I -> R -> J_sus` without unnecessary model expansion.

## 1. Selection rule

A mechanism is retained only if it is needed for at least one of:

```text
H1 dynamic P–T interdependency;
H2 information/organization effect on feasible response;
H3 viability/structural inadequacy diagnosis;
H4 mechanism-sensitive intervention testing;
H5 resilience-to-sustainability transformation.
```

and if it has a physically interpretable state/control pathway plus an evidence/validation route.

## 2. Frozen minimum set

### M-PT-1 — Power → charging/traction service

```math
P_c(t)\rightarrow\mu_c(t)\rightarrow q_c(t)\rightarrow S_T(t).
```

Role: captures power loss causing charging-service degradation, backlog and mobility loss.

### M-PT-2 — Power → traffic-control service

```math
P_i(t)\rightarrow C_\ell(t)\rightarrow T_{ij}(t)\rightarrow S_T(t).
```

Role: captures signal/control dependency of roadway service. It is not mandatory inside H1-v1 if the frozen H1 comparator excludes it; it is retained thesis-wide for later P–T mechanism coverage.

### M-TP-1 — Transportation → power restoration through crew access

```math
x_T(t)\rightarrow\tau_{crew}(t)\rightarrow\tau_{repair}(t)\rightarrow S_P(t).
```

Role: captures recovery interdependency and is already represented in the H1 dynamic comparator.

### M-TP-2 — Transportation electrification → power loading/flexibility

```math
\lambda_{EV},SOC,u_c\rightarrow P_{EV}(t)\rightarrow x_P(t).
```

Optional reverse flexibility:

```math
SOC,u_{V2G}\rightarrow P_{V2G}(t)\rightarrow x_P(t).
```

Role: provides the principal bridge from P–T coupling to operational energy/carbon consequences. It is introduced only after H1-v1 validation so it does not contaminate the frozen H1 comparison.

### M-I-1 — Information → state belief/decision quality

```math
D_{0:t}\rightarrow b_t(Y)\rightarrow u(t).
```

Role: captures sensing, communication and inference uncertainty; tested through the H2 nested comparison rather than assumed.

### M-O-1 — Organization → feasible response set/timing

```math
z_O(t)\rightarrow\mathcal U(z_I,z_O,t),\tau_{response}.
```

Role: captures crew/resource/authority/coordination limitations through feasible control, not as an abstract organizational score.

## 3. Minimum cross-layer architecture

```math
\boxed{
\mathbb I_{min}
=
\{
M_{PT1},M_{PT2},M_{TP1},M_{TP2},M_{I1},M_{O1}
\}.
}
```

This is the thesis-wide mechanism set. It is not the H1-v1 demonstrator.

## 4. Hypothesis nesting

### H1 subset

```math
\mathbb I_{H1}
=\{M_{PT1},M_{TP1}\}
```

for the already frozen dynamic charging-memory and road-to-repair comparison. Additional mechanisms are excluded from H1-v1 to preserve falsifiability and nestedness.

### H2 extension

```math
\mathbb I_{H2}
=\mathbb I_{H1}\cup\{M_{I1},M_{O1}\}.
```

### H3/H4

Use validated H1/H2 dynamics plus frozen admissibility/viability objects; no new mechanism is added merely to improve results.

### H5/sustainability extension

```math
\mathbb I_{H5}
=\mathbb I_{H2}\cup\{M_{TP2}\}
```

when the energy/carbon accounting model is activated. `M_PT2` may also be activated if accessibility under signal/control loss is part of the final transformation experiment.

## 5. Mechanism admission contract

For each mechanism `M_e`, the following must exist before confirmatory use:

```text
source/receiver and ports;
physical/functional carrier;
state/update equation;
parameters and units;
activation guard;
timescale/delay;
evidence source;
uncertainty representation;
limiting/reduction behavior;
verification test;
validation route;
context of use.
```

## 6. Excluded from the minimal set unless later evidence requires them

```text
AI/GNN controllers;
learned non-Euclidean geometry;
detailed market dynamics;
full endogenous route-choice feedback from charger queues;
large behavioral choice models;
material lifecycle inventories;
additional infrastructure sectors beyond P,T,I,O;
extra resilience indices without a declared decision role.
```

Exclusion is a scope-control decision, not a statement that these mechanisms are scientifically unimportant.

## 7. Scientific purpose mapping

```math
\boxed{
\begin{aligned}
M_{PT1},M_{PT2},M_{TP1}
&\rightarrow\text{disturbance propagation/recovery/accessibility},\\
M_{TP2}
&\rightarrow\text{power loading/flexibility/energy-carbon consequences},\\
M_{I1},M_{O1}
&\rightarrow\text{knowledge and feasible response},\\
\text{validated combination}
&\rightarrow\mathbf R\rightarrow\Phi_{RS}\rightarrow\mathbf J_{sus}^{core}.
\end{aligned}
}
```
