---
name: thesis-thermal-physics
description: Evidence-controlled thermal physics for the active extreme-heat Power System–Electrified Transportation thermal-interdependency thesis; follow the orchestrator and repository canonical governance.
---

# Thermal physics

**Prerequisite:** Load `.github/skills/power-ev-thermal-research/SKILL.md` and its current authority/gates before using this module.

## Trigger and objective
Activate for transformer top-oil/winding hot-spot, EVSE rectifier/cooling/derating and battery thermal-state mechanisms under extreme heat.

## Steps
1. Write energy-control volume, state/sensor location, heat sources, thermal capacitance, ambient exchange, convection/cooling, equipment limits, initial conditions and correct units for each physical component.
2. Candidate generic balance `C_th dT/dt = Q_loss - Q_cooling - (T-T_a)/R_th` is **only a schematic T1 starting point**; it is not an admitted transformer, charger or battery law until component interpretation and primary evidence support every term.
3. Transformer: inspect loading/current harmonic contributions, resistive/stray losses, time constants, oil-to-winding coupling and relevant exact manufacturer/IEC/IEEE limits. Do not treat generic top-oil predictions as verified transformer derating.
4. EVSE: verify actual sensor locations, fan/coolant actuation, rectifier loss, thermal derating algorithm and measured input/output power; do not invent a 50-kW charger manufacturer curve.
5. Battery: distinguish `BMSminPackTemperature`, `BMSmaxPackTemperature`, and inaccessible mean/core temperatures; verify cooling power versus an ambiguous BMS diagnostic proxy and check current polarity.
6. Verify limiting cases (no electrical load, equal ambient/device temperature, constant inputs, cooling failure), conservation, nonnegative dissipation and domain of validity.

## Outputs and gate
`equation_register.csv`, mechanism diagrams, physical-state dictionary, thermal parameters/uncertainty. Block any heat flux, threshold or thermal capacity lacking equipment-appropriate evidence. External ambient forcing ≠ internal state; thermal state ≠ capability ≠ service.

### ECE6378 / RPG Lab overlay (S4)
Use L2–4, L10–11 to connect observed electrical loading and documented equipment loss laws to component heat balances. Distinguish (a) electrical line/transformer *thermal loading ratings* used in DistFlow/OPF and (b) actual oil/winding/EVSE/BMS thermal state observations. The course page does not independently supply transformer/EVSE thermal ODEs, cooling laws, sensor calibrations or derating curves; source these elsewhere before admission. Enforce state→capability→service, not electrical current limit→assumed temperature.
