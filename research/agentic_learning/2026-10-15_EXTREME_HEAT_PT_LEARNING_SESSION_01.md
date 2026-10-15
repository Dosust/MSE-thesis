# Agentic Learning — Session 01: Electrothermal Power–EVSE–Transport Coupling

**Date:** 2026-10-15  
**Status:** COMPLETED AS EXPLORATORY LESSON / NO EMPIRICAL VALIDATION  
**Authority:** See `project/AUTONOMOUS_EXECUTION_PROTOCOL_V1.md`; see adjacent evidence ledger.

## Competence target
Read a real source equation with its operational boundary, distinguish [E] source evidence from [D] mathematical consequence and [P] proposed extension, and select physically admissible coupling complexity.

## Lesson A — Paper-based equations, do not invent source numbers
**Balogun et al., EV-EcoSim, Section II-F, Eq. (16)**: [E] `P_grid = P_ev/eta_evse`.
- `P_grid`: electrical input demand to EVSE; `P_ev`: stated EV charging delivered power; `eta_evse`: conversion efficiency; under this simplified positive-power convention `0<eta_evse<=1`.
- [D] with an idealized loss-only EVSE and no auxiliary/storage dynamics: `P_loss = P_grid-P_ev = P_ev*(1/eta_evse-1)`.
- [D] check `eta_evse=1 => P_loss=0`; with efficiency less than one and non-negative output `P_loss >= 0`.
- **Not implied:** time-varying losses, active cooling, reverse V2G flows, transformer heating and grid service losses follow automatically from Eq. (16). They require independent mechanisms.

**Balogun, Section II-D, Eqs. (13)–(14)**: [E] `theta_o(t)` and `theta_h(t)` are dynamic thermal states driven by ambient `theta_a(t)`, normalized load `K(t)`, and fitted/rated thermal parameters. Retain original equation numbers, units and cooling-mode assumptions in later FTEE. The paper uses Euler time-stepping; numerical step-convergence is not equivalent to equipment validation.

**Balogun, Section II-A**: [E] 2-RC battery ECM with Eq. (1); *battery temperature is fixed at 23°C and internal thermal states are omitted*. No paper-grounded `dot(T_battery)` may be attributed to this source.

## Lesson B — What counts as an actual directional interface?

[P] For a charger at grid bus `i` servicing EVs at mobility facility `j`:
- **P→T**: available electricity/charger power constraint changes charging energy served; subsequent impact on trips or accessibility must be modeled and evidenced separately.
- **T→P**: EV charging arrival/profile changes electrical load; V2G is conditional on hardware/permissions; repair access uses transport routing.
- **Common forcing:** a heatwave independently affects distribution assets and EV energy demand. This is *not by itself* proof that either directly caused the other's failure.

[P] Candidate research chain, requiring each arrow's evidence and testing:
`ambient temperature -> transformer/charger thermal state -> allowable charging capacity -> actual energy delivered -> EV availability -> mobility service`.
Observe the distinction between *equipment functioning* and *delivered critical services*.

## Lesson C — Two coupling schemes and a hypothesis you can falsify
- `M0` independently simulated power, EVSE and road/mobility response, with identical external disturbances.
- `M1` static/algebraic coupling through justified power/charging limits.
- `M2` dynamic coupling with additional *identified* electrothermal interface state(s) and delayed/temperature-dependent response.

**Important:** the framework must explicitly state whether `M1` is sufficient. Lack of identifiable timescales or data should keep `M2` experimental, not mandatory.

Potential falsification tests [P], not empirical findings:
1. Nested limit: as interface coupling is removed, `M2` approaches the disconnected baseline in comparable state/output coordinates.
2. Thermodynamic sign/units and power balance closure across the correct AC/DC boundary.
3. Comparison of equal scenarios and equal control opportunities across M0/M1/M2; assess held-out predictions with error calibration.
4. Thermal state identification/observability; do not add an unobservable state without explicit defensible prior/constraints.
5. Perturbation sensitivity: peak-ambient input versus loading input, keeping all else matched.
6. Step-size/solver and event-order tests; real-time deadline tests if operational control is claimed.
7. Compare independent evidence of mobility service after EVSE curtailment; absent evidence restrict conclusions to charging power delivered.

## Exercise 01 (model verification, hypothetical values only)

Given [A] positive EVSE output `P_ev=50 kW`, [A] one-way efficiency `eta_evse=0.90` under Eq. (16), calculate `P_grid`, `P_loss`, and check whether a negative heat loss would be physically consistent. These values are deliberately *not sourced empirical parameters*.

[D] From Eq. (16): `P_grid=50/0.9=55.555... kW`; `P_loss=5.555... kW`. The non-negative loss and `eta=1` limit pass. Unit: kW; integrated energy kWh requires a specified duration.

## Exercise 02 (critical reasoning)

A hot day causes an increased demand on the feeder and also worsens an EV fleet's range. Does this prove `P->T` interdependency? **No.** The same hazard may cause parallel outcomes. To establish direction, identify feeder/charger supply impact and its mediated change in actual charging/EV trip service; distinguish association, common exposure, and mechanism.

## Mastery check

1. Which exact EV-EcoSim source equations represent *transformer* thermal dynamics? Answer: (13) and (14), Section II-D.
2. Which directly represents EVSE active-power boundary? Answer: (16), Section II-F.
3. Does source include battery internal temperature dynamics? Answer: no; Section II-A explicitly excludes them.
4. Can a HELICS connection itself establish causality? Answer: no; it provides runtime communication/co-simulation.
5. Is a safe-operation set automatically a viability kernel? Answer: no; viable trajectories require specified state dynamics, controls, disturbances and horizon.
6. May this lesson's illustrative numbers be used as fitted case parameters? Answer: no.

## Current scientific disposition

- [E] Primary equations/limitations for EV-EcoSim: **PASS (limited extraction)**.
- [D] Simple loss relation: **PASS (algebra + limit under stated assumptions)**.
- [P] Detailed battery+EVSE+transport dynamic interface model: **DEFERRED_DEPENDENCY** until governing mechanism/evidence and parameter identification.
- [P] Real-time controller performance: **BLOCKED_EVIDENCE** until latency, sensors and out-of-sample test.
- [H] Reliability gain of dynamically coupled over simpler models: **UNTESTED**.
- Thesis hypothesis status and existing Austin case: **UNCHANGED**.

## Immediate next learning session
FTEE-read Swift et al. IEEE transformer I and field verification II; compare against EV-EcoSim (13)-(14), audit units, ambient cooling-mode, numerical stability, and identifiable parameters. Then link to EVSE power through explicit evidence, not by correlation. Stop if primary equations or source assumptions are inaccessible; preserve blockers.
