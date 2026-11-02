---
name: thesis-system-identification
description: Evidence-controlled system identification and inverse problems for the active extreme-heat Power System–Electrified Transportation thermal-interdependency thesis; follow the orchestrator and repository canonical governance.
---

# System identification and inverse problems

**Prerequisite:** Load `.github/skills/power-ev-thermal-research/SKILL.md` and its current authority/gates before using this module.

## Trigger and objective
Activate when fitting transformer/battery/EVSE thermal parameters from measured data or evaluating predictive horizon performance.

## Steps
1. Define parameter vector, sensor observation function, sampling, noise/loss model, excitation and prior bounds with physical meaning/provenance; distinguish merely effective coefficients from identified heat capacities/resistances.
2. Conduct structural identifiability analysis, parameter scaling, sensitivity-rank and practical-identifiability checks. Report optimizers, convergence, covariance/conditioning/CI, boundaries hit and parameter correlation.
3. Use session/vehicle/site/time-level separation to prevent leakage. Validation selects model; test reports generalization. Never tune using held-out test observations.
4. Verify that `future measured ambient/current/BMS signals` create a conditional **hindcast**, not an operational forecast; report unknown future inputs transparently.
5. Compare every thermal output to persistence and simpler uncoupled equations. Track sensor extrema, not a fictional mean-pack channel. Treat unmeasured battery cooling power as an identifiability blocker.
6. Quantify domain shifts such as SINTEF ambient -19.58 to +25.97 °C versus an extreme-heat use case; restrict claims to qualified exposure range unless separate evidence permits transfer.

## Outputs and gate
`parameter_register.csv`, identifiability diagnostics, train/val/test manifest and sensitivity plots. A numerical minimizer success ≠ identifiable physics. Fitting at a parameter bound, baseline failure, or missing input semantics blocks physical qualification.

### ECE6378 / RPG Lab overlay (S6)
Practice L8–9 and L14–18: baseline regression, scaling, PCA only on training, differentiable forward model/gradient checks, stable optimization, regularization, uncertainty and sensitivity-rank identifiability. L24–25 time-series models are tentative. Before any neural correction, independently establish which heat-balance coefficients are identifiable and whether validation outperforms persistence on both required thermal channels. Declare conditional hindcast if future observed forcing is used. Record instrument uncertainty, fit bounds and domain shift; `M2` residual coefficients are not proven physical heat fluxes.
