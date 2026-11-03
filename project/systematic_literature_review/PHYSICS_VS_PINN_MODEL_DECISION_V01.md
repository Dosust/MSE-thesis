# Physics versus PINN/PIML — evidence-based methodological decision v1.0

**Date:** 3 November 2026. **Decision status:** \`PROVISIONAL_PHYSICS_FIRST; COUPLED_FIELD_PINN_NOT_ADMISSIBLE_ON_CURRENT_DATA\`. **NOT final independent model performance verdict.**

## What professor Phelan requested

A thorough prior-study investigation before model choice and **conditional** consideration of physics-informed ML **if experimental evidence is sufficient**; otherwise conventional physics.

## Current evidence of physical and modeling precedent

- IEC 60076-7:2018 supplies mineral-oil transformer loading and operating temperature/thermal-aging physics (applicability and exact site model selection still need confirmation).
- Bragone et al. 2022 DOI 10.1016/j.epsr.2022.108447 already used a field-boundary-informed 1D transformer heat PDE PINN compared with a finite-volume model. The paper's stated conclusion is **PINN did not outperform FVM for the tested data quantity/type**. No foundation for “first transformer thermal PINN” or automatic ML superiority.
- Cao et al. 2026 DOI 10.1016/j.applthermaleng.2026.130776 reports a physics-informed neural Transformer for EV thermal-management energy prediction under extreme ambient conditions, **not** a supplying power transformer.
- Acker et al. 2025/2026 DOI 10.1007/s41104-025-00157-7 calibrate a battery and coolant physics model from actual EV measurements, while evaluating a predictive controller through a validated simulator.
- Field Qatar EVSE thermals (Krama 2026) and field bus transformer electrical measurements (Li 2026) are **different apparatus**; currently available raw data do not demonstrate one synchronized connected extreme-heat thermal control system.

## Recommended admissible sequence

**Gate M0: Define the apparatus and physical model context.** Specify transformer type/cooling, EVSE rectifier/cooling, AC/DC/auxiliary energy boundary, battery capacity and temperature operator, weather, service commitments; mark unknown equipment and control policies OPEN.

**Gate M1: Pure-physics baseline.** Implement first-law energy balance and equipment-appropriate standard thermal ODE/PDE with verified units/parameters/initial states; numerical convergence and energy residual tests; compare to persistence and simple effective parametric model on reproducible chronological splits (with explicit future forcing availability). Identifiability of physical parameters must be tested separately from full rank of statistical regression.

**Gate M2: Qualified data check.** Need actual thermal observations, forcing, sensors, frequency, sensor semantics, suitable heat excitation, calibration/validation partitions and justified external transfer domain. Component-level transformer data allow a component-level benchmark even without connected-site EVSE data.

**Gate M3: Conditional physics-informed learning.** If M2 passes for a specific asset, compare physics baseline against simple gray-box/physics-guided residual and a minimally specified PINN/PIML on *identical* data splits, available inputs and metric horizons. Prespecify RMSE/MAE, out-of-regime temperature, missingness, uncertainty calibration/coverage, physical constraint violations, runtime/complexity and data-efficiency. Keep instrument topology and measurement units explicit.

**Gate M4: Connected model study.** Requires matched, **physically mapped** same-site transformer thermal and EVSE internal thermal/electrical streams, actual restriction/control reason codes and service deadlines. Without these, the linked dynamics can be presented as **conditional physics simulation**, never validated interdependency causality.

## Decision matrix

| Observational evidence | Permissible near-term model | Scientific ceiling |
|---|---|---|
| No adequate component-level thermal records | First-law pure physics/standards with bounded parameters, UQ and numerical verification | Mechanistically constrained *scenario simulation*, not empirical fit |
| Measured SINTEF transformer ambient/loading/top-oil | Reduced transformer physics candidate and matched conventional benchmarks; optional component-level physics-guided learning if independent validation supports | Same-transformer within observed range; max ambient +25.97°C |
| Qualified measured EVSE rectifier/power/ambient series (Qatar raw currently unavailable) | EVSE component physics/gray-box, optional PIML with independent sessions | No link to supplying transformer without site connection |
| Valid vehicle pack temperatures/charge-state series (TUM/KU Leuven after QA) | Vehicle/battery physics and optional residual/PIML | No proven EVSE power-thermal law or transformer feedback |
| Matched site-wide thermal electrical/control/service measurements | Coupled dynamic physics and possibly PINN/PIML if benchmarks justified | Source-defined site, equipment and heat regime only |

## Current decision and blockers

**PROVISIONAL SELECTION = physics-first for the thesis mathematical foundation.** A PINN is an *optional comparative method* only if a specific thermal state, forcings and valid holdouts can be established. The current original records support exploratory SINTEF component modeling and a literature-supported physical structure, **not** a validated extreme-heat coupled PINN.

**Not demonstrated yet:** physics-only independent external thermal validation; matched gray-box vs PINN benchmark; systematic review closure; one-site P↔EVSE measured heat-feedback and real service outcome. Do not claim a final PINN gain or definitive proof that no PINN would work.

**Acceptance gate:** model choice can be upgraded to FINAL only after full evidence review and data-quality/identifiability and matched baseline tests, or recorded defensible no-go ruling with complete assumptions and independent reviewers when available.
