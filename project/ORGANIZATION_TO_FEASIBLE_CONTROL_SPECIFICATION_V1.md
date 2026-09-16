# Organization-to-Feasible-Control Specification v1.0

**Date:** 2026-09-16  
**Status:** WORKING MATHEMATICAL SPECIFICATION — not a novelty claim and not yet empirically validated  
**Stages:** 2 → 4 → 5  
**Authority:** subordinate to `CANONICAL_DEPENDENCY_CONTRACT_V1.md`, `CANONICAL_7_STAGE_FRAMEWORK.md`, and `PHASE1_EMPIRICAL_VALIDATION_PROTOCOL.md`

## 1. Scientific purpose

Replace an undefined scalar “organizational resilience” with interpretable organizational states that modify admissible infrastructure actions, task precedence and response time.

The required causal chain is

```math
\boxed{
\text{rules/authority/resources/coordination}
\rightarrow
z_O
\rightarrow
\mathcal U(z_I,z_O)
\rightarrow
u(t)
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Q(t).
}
```

## 2. Prior-art boundary

The thesis does not claim novelty for logical interdependencies, restoration coordination, repair-crew routing, collaborative recovery planning or rule-mediated infrastructure interaction.

Relevant evidence includes:

- Yu et al. (2025), *Logical interdependencies in infrastructure*, Risk Analysis 45(2), 356–375, DOI `10.1111/risa.16555`: formal/informal rules, actor actions, information and aggregation rules can create logical infrastructure interdependencies.
- Çavdar, He & Qiu (2022), *Repair Crew Routing for Power Distribution Network Restoration*, arXiv:2204.04848: road-network logistics interact with power restoration sequencing.
- Work-crew routing literature integrates road routing with infrastructure restoration scheduling (Transportation Research Part B 118, 2018, DOI `10.1016/j.trb.2018.10.001`).
- Xu, Li & Chen (2024), *Resilience-driven post-disaster restoration of interdependent infrastructure systems under different decision-making environments*, Reliability Engineering & System Safety 241, 109599, DOI `10.1016/j.ress.2023.109599`.

The thesis-specific question is whether organizational constraints can be encoded transparently enough to alter the feasible control set and improve explanation/prediction in a coupled P–T demonstrator.

## 3. Organizational state must be typed

Use a structured organizational state rather than a generic coefficient:

```math
z_O(t)
=
\left(
\mathcal A_O(t),
\mathcal R_O(t),
\mathcal P_O(t),
\mathcal C_O(t)
\right),
```

where

```text
A_O = authorization/decision-right state;
R_O = available human/material/resource capacities;
P_O = task precedence and procedural constraints;
C_O = coordination/communication commitments relevant to action feasibility.
```

The exact implementation may use discrete, hybrid or set-valued states. These objects are not assumed continuous.

## 4. Authorization constraints

Let `J` index candidate operational actions. Define authorization availability

```math
\alpha_j(t)\in\{0,1\}.
```

Then a simple authorization constraint is

```math
\boxed{
|u_j(t)|\le \alpha_j(t)\,\bar u_j.
}
```

When `alpha_j=0`, the corresponding action is unavailable even if physically possible.

`alpha_j` must be connected to an explicit rule, authority state or event logic; it may not be tuned as a free resilience parameter.

## 5. Resource constraints

Let `r_O(t)` be the vector of available organizational resources and `B_u` the resource-consumption matrix for operational actions. Then

```math
\boxed{
B_u u(t)\le r_O(t).
}
```

Examples may include:

```text
repair crews;
service vehicles;
mobile generation/storage;
spare components;
inspection capacity;
control-center personnel;
contractor availability.
```

Units and resource accounting must be explicit.

## 6. Transport-constrained restoration

For restoration action `j`, let

```math
\mathcal R_j(t)
```

be the feasible route set under transportation state `x_T(t)` and current access/authority constraints.

Travel time is

```math
T_{travel,j}(t)
=
\min_{r\in\mathcal R_j(t)}
\sum_{a\in r} t_a(x_T(t)).
```

If

```math
\mathcal R_j(t)=\varnothing,
```

the repair action is temporarily infeasible regardless of electrical need.

This is a concrete `T -> O/control -> P` mechanism and is already part of the Phase-1 organizational dependency fixture.

## 7. Task precedence and response time

Represent response activities as a directed acyclic task graph when their order is constrained:

```math
\mathcal G_O^{task}=(\mathcal N_O,\mathcal E_O).
```

Each task `l` has duration `tau_l` and resource/authorization requirements.

If all tasks are strictly sequential,

```math
\tau_{response}
=
\sum_l \tau_l.
```

If tasks overlap, the correct completion time is the critical-path length:

```math
\boxed{
\tau_{response}
=
\max_{p\in\mathcal P_{task}}
\sum_{l\in p}\tau_l.
}
```

The thesis must not use an arithmetic sum when parallel work is permitted.

## 8. Feasible operational control set

Let `U_phys(Y,t)` denote physically admissible operational controls. The organizationally constrained feasible set is

```math
\boxed{
\mathcal U(Y,z_I,z_O,t)
=
\left\{
u\in\mathcal U_{phys}(Y,t):
A_O\nu\le b_O(z_O),
B_u\nu\le r_O(z_O),
\Gamma_O(\nu,z_O)=1
\right\}.
}
```

Here `Gamma_O` represents discrete authorization, precedence and logical feasibility conditions.

Information state `z_I` may further constrain controls when required observations/communications are unavailable.

## 9. Operational policy

The Stage-4 policy remains

```math
\boxed{
\nu(t)
=
\pi\!\left(
\widehat X(t),z_I(t),z_O(t)
\right),
\qquad
\nu(t)\in\mathcal U(Y,z_I,z_O,t).
}
```

This is operational control of the current regime. It is not the Stage-7 strategic transformation action `a_k`.

## 10. H2 ablation design

Use matched physical equations and scenarios:

```math
\mathscr N_0=P+T,
```

```math
\mathscr N_1=P+T+I,
```

```math
\mathscr N_2=P+T+I+O.
```

Primary incremental contrasts are

```math
\mathscr N_1-\mathscr N_0
```

for information effects and

```math
\boxed{
\mathscr N_2-\mathscr N_1
}
```

for organizational effects.

Candidate intermediate quantities include:

```math
|\mathcal U(t)|,
\qquad
\tau_{response},
\qquad
T_{travel},
\qquad
N_{actions}^{feasible},
```

with downstream outcomes such as service loss and restoration time.

## 11. Evidence and parameter rules

Every organizational quantity used in a confirmatory model must identify:

```text
source rule/event/log;
actor or responsible unit;
operational meaning;
units/state domain;
measurement/inference method;
uncertainty;
validity period/domain;
calibration vs validation role.
```

A generic `organization score`, `coordination coefficient` or `governance resilience factor` is prohibited unless independently defined, measured and validated for the exact use.

## 12. Validation strategy

Evidence may include:

```text
work-order timestamps;
crew dispatch/arrival/repair logs;
road-access records;
resource rosters;
authorization/procedure records;
incident command timelines;
observed restoration trajectories.
```

Minimum tests:

1. reproduce observed task/dispatch timing within declared tolerance;
2. verify that removing an organizational constraint recovers the less-constrained baseline;
3. verify resource conservation/accounting;
4. test predictive value on held-out incidents/scenarios when possible;
5. report unobserved organizational states as inferred/uncertain rather than measured.

## 13. Current status

```text
ORGANIZATIONAL SEMANTICS: SPECIFIED
GENERIC FEASIBLE-CONTROL MAP: SPECIFIED
PHASE-1 D_O FIXTURE: CONSISTENT WITH CANONICAL PROTOCOL
EMPIRICAL ORGANIZATIONAL DATA: NOT YET QUALIFIED
H2 CONFIRMATORY EXECUTION: NOT AUTHORIZED
NOVELTY: NOT CLAIMED
```
