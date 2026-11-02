---
name: thesis-mathematical-modeling
description: Evidence-controlled applied mathematical modeling for the active extreme-heat Power System–Electrified Transportation thermal-interdependency thesis; follow the orchestrator and repository canonical governance.
---

# Applied mathematical modeling

**Prerequisite:** Load `.github/skills/power-ev-thermal-research/SKILL.md` and its current authority/gates before using this module.

## Trigger and objective
Activate for state-time dynamics, ODE/DAE/hybrid models, thermal-conditioned electrical interfaces, operating constraints and directional dependency hypotheses.

## Steps
1. Define a minimum sufficient thermal/operational state `x`, external forcing `T_a`, controls `u`, parameters `theta`, observations `y` and explicit port variables with dimensions and domain.
2. Admit each equation as `E1` fundamental, `E2` standard, `E3` literature or `E4/T1` thesis-derived, with governing source, stated assumptions, derivation and scope; if absent mark OPEN.
3. Build `dot(x_P)=f_P(x_P,z_PT,T_a,u_P;theta_P)` and `dot(x_Te)=f_Te(x_Te,z_PT,T_a,u_Te;theta_Te)` only as provisional structural candidates until constitutive terms are justified. Formulate P→T_e and T_e→P thermal mechanisms **separately**.
4. Preserve causality, energy flow, algebraic constraints, coupling delays, switching/derating conditions, thermal initial and physical boundary conditions. Ensure state-time response is observable for selected sensors.
5. Show dimension checks and analytical/numerical limits: disconnected systems, constant loading, no heat forcing, saturation/derating, charge prohibited, and zero thermal coupling.
6. State exactly which conclusions follow from mathematics alone and which require empirical validation. A numerical model fitting one component is not an independently validated coupled network.

## Outputs and gate
`equation_register.csv`, state and port dictionary, dimensional-check report, coupling removal/ablation tests. PASS requires an admitted derivation and verified numerical implementation; field-validation status remains independent.

### ECE6378 / RPG Lab overlay (S5)
Use L10–11 for audited algebraic electrical power-flow constraints and L19–23 (tentative) for graph-aware / constrained optimization ideas. Pair the resulting electrical algebraic system with *separately admitted* thermal ODEs in an ODE/DAE/hybrid candidate, with dimensional checks, coupling removal and event handling. ML-embedded OPF/SCUC feasibility is a **method** transfer and must not be adopted as a transformer derating constitutive law. Use the `M0/M1/M2` comparator proposal and exact-feasibility checks in `references/PHYSICS_CONSTRAINED_ML_VVUQ.md`.
