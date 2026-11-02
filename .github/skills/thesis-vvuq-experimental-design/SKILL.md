---
name: thesis-vvuq-experimental-design
description: Evidence-controlled vvuq and experimental design for the active extreme-heat Power System–Electrified Transportation thermal-interdependency thesis; follow the orchestrator and repository canonical governance.
---

# VVUQ and experimental design

**Prerequisite:** Load `.github/skills/power-ev-thermal-research/SKILL.md` and its current authority/gates before using this module.

## Trigger and objective
Activate to design falsifiable tests, separate correlation from directional causality, audit simulation truth claims and independently validate components or any physically connected system.

## Steps
1. Predeclare hypothesis, measured response, physical perturbation, confounders, negative controls, comparator and endpoint before examining test labels; preserve exact source and split manifests.
2. **Verification:** source code tests, units, integration convergence and tolerance, conservation, physical constraints, consistent algebraic signs and event handling.
3. **Validation:** independently held-out, real measured observations from the correct site/equipment/domain, compared to matched persistence and competing reduced-model baselines; report MAE/RMSE/bias and intervals/coverage with sample sizes, not cherry-picked score.
4. **UQ:** sensor/calibration noise, missing data, parameter uncertainty, operating-input variability and structural model uncertainty; uncertainty intervals must be calibrated to the target horizon/domain, not extrapolated by assertion.
5. **Causal evidence:** time ordering, physical topology, availability of confounder observations, restriction logs and interventions. Do not infer heat transfer/direction from coincident thermal trends or from a power-flow equation alone.
6. Separate `SIMULATION_VERIFIED`, `COMPONENT_CONDITIONAL_VALIDATED`, `CONNECTED_ELECTRICAL_VALIDATED`, `CONNECTED_THERMAL_FIELD_VALIDATED`. Each status requires its own evidentiary gate; lacking field data yields `BLOCKED_EVIDENCE` rather than simulated validation.

## Outputs and gate
`validation_register.csv`, executed numerical test logs, failure/ablation tables, uncertainty calibration, threats-to-validity and falsifiable direction-specific conclusion. For coupled field validation require documented connected transformer/EVSE, synchronized direct thermal and electrical observations plus independent held-out tests.

### ECE6378 / RPG Lab overlay (S7)
Use L14 as **minimum evaluation standard**; L9/12–13/16–18 for comparators and L19/21/23–27 (tentative) only after sample adequacy. Pre-register equal horizons/input information, time/site/session-held-out partitions, train-only feature selection/PCA, matched persistence/physics/statistical/hybrid models, MAE/RMSE/bias, calibration, physical feasibility, solver gap, timing and OOD heat exposure. Physically constrained ML must be verified for *actual* hard constraints, not only low penalty. Populate `ml_experiment_register.csv`, run `check_ml_experiments.py`, and retain prior G6/G7 block states until real independent thermal field evidence qualifies them.
