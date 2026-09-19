# Stage 3 Hybrid-Domain Clarification — v2.1

**Date:** 2026-09-19  
**Status:** CANONICAL CLARIFICATION — DESIGN/PROTOCOL ONLY  
**Parent authority:** `project/stage3/STAGE3_SCIENTIFIC_CONSTITUTION_V2.md`  
**Scientific effect:** mathematical closure/notation clarification only; no case parameter, model result, H1 result, or empirical claim is changed.

## 1. Purpose

The Stage-3 v2 constitution already admits continuous/quasi-continuous dynamics, algebraic constraints, hybrid resets, mode transitions, topology transitions, QSTS, network flow, and co-simulation. This clarification makes the **flow domain** and **jump domain** explicit without changing that scientific meaning.

The seven-stage architecture is not reopened.

## 2. Canonical hybrid-domain abstraction

For discrete mode (m), define

~~~math
\boxed{
\mathscr H_3
=
(
C_m,
D_m,
F_m,
A_m,
J_m,
\mathcal G,
\Theta,
\mathbb I^{active}
).
}
~~~

Here:

- (C_m): flow/admissibility domain for continuous or quasi-continuous evolution in mode (m);
- (D_m): jump/event domain in which a declared discrete transition is enabled;
- (F_m): native + coupled differential/continuous evolution operator;
- (A_m): algebraic/network constraint operator;
- (J_m): reset/mode/topology transition operator;
- (mathcal G): current physical topology;
- (Theta): model/physical parameter object;
- (mathbb I^{active}subseteqmathbb I_3^{ready}): currently active Stage2→3-ready dependencies.

The active Stage-3 physical truth remains

~~~math
\boxed{
Y^{phys}=(x_P,x_T,z_{PT}).
}
~~~

No Stage-4 observation, belief, organization, or policy state is inserted into (Y^{phys}).

## 3. Flow semantics

For ((x,z_a)in C_m),

~~~math
\boxed{
\dot x
=
F_{\mathcal G}^{m}
\left(
x,z_a,u^{exo},\eta;
\Theta,
\Xi_{\mathbb I^{active}}
\right),
}
~~~

subject to

~~~math
\boxed{
0=
A_{\mathcal G}^{m}
\left(
x,z_a,u^{exo},\eta;\Theta
\right).
}
~~~

(A_m) is an integration-level alias for the algebraic operator denoted (G_{\mathcal G}^{m}) in the parent Stage-3 constitution. The alias is used only to avoid collision with scientific gate notation (G_k).

The abstract form does not force every subsystem into one equation class. ODE, DAE, QSTS, network-flow, CTM/DTA, microscopic/mesoscopic and qualified co-simulation realizations remain admissible when selected prospectively by the Stage-3 model-family protocol.

## 4. Jump semantics

When a declared event (e) is enabled and the state lies in (D_m),

~~~math
\boxed{
(x^+,m^+,\mathcal G^+)
=
J_e
(
x^-,z_a^-,m^-,\mathcal G^-,\eta
).
}
~~~

This compact operator is equivalent to the parent constitution's separate reset, mode-update, and topology-update maps.

A jump may not be triggered by an unqualified causal relation or by a result-driven rule.

## 5. Timing firewall

The following quantities are permanently distinct:

~~~math
\boxed{
\tau_e^{phys}
\neq
t_{event}
\neq
h_{solver}
\neq
h_{comm}
\neq
T_{horizon}.
}
~~~

Interpretation:

- (	au_e^{phys}): physical/mechanism characteristic time where scientifically meaningful;
- (t_{event}): event time;
- (h_{solver}): numerical integration/solution step;
- (h_{comm}): co-simulation communication step;
- (T_{horizon}): experiment horizon.

A physical causal delay remains governed by the Stage-2 dependency semantics and must not be replaced by solver or communication timing.

## 6. Multiple timescales

~~~math
\boxed{
\tau_P\neq\tau_T
\not\Rightarrow
\text{multirate algorithm is mandatory}.
}
~~~

Timescale separation is evidence relevant to numerical-method selection. A multirate method is used only if required by stability, accuracy, computational efficiency, and convergence evidence for the selected realization.

## 7. Verification obligations

Before a Stage-3 realization may claim implementation verification, check as applicable:

1. flow-domain admissibility;
2. algebraic consistency;
3. jump-domain/guard correctness;
4. reset/mode/topology update correctness;
5. conservation and network balance;
6. units and sign conventions;
7. event ordering;
8. timestep refinement;
9. communication-step sensitivity for co-simulation;
10. limiting/uncoupled cases;
11. reproducibility.

## 8. Claim boundary

~~~math
\boxed{
\text{hybrid-domain closure}
\neq
\text{case validation}
\neq
\text{H1 support}.
}
~~~

This clarification is authoritative only for Stage-3 hybrid-domain representation. All other Stage-3 v2 semantics remain unchanged.
