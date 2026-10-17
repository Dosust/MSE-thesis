# Research synthesis release — 2026-10-17

This is a **draft, evidence-bounded** mathematical synthesis of the three obtained original focal studies (Gong 2015; Kunlasing 2022; Krama 2026), adjoining foundation sources, and a new proposed Power–Electrified Transportation electrothermal hybrid model under extreme heat.

## Artifacts

1. [THREE_PAPER_SOURCE_BY_SOURCE_COMPARATIVE_MATRIX.csv](THREE_PAPER_SOURCE_BY_SOURCE_COMPARATIVE_MATRIX.csv) — 14 source-located mechanism/measurement/equation/validation records for three focal papers.
2. [FOUNDATIONAL_PRIOR_ART_AND_THIRTY_SOURCE_ACCESS.md](FOUNDATIONAL_PRIOR_ART_AND_THIRTY_SOURCE_ACCESS.md) — source-version hierarchy, prior transformer thermal models, 2025 IEEE loading-guide status, 2018 IEC guide scope, remaining access blockers and falsifiable novelty claims.
3. [COUPLED_ELECTROTHERMAL_HYBRID_MODEL_V0.md](COUPLED_ELECTROTHERMAL_HYBRID_MODEL_V0.md) — proposed derived P thermal two-node energy balances + EVSE effective thermal balance + electrical power/constraint interface, hybrid states/modes, measurement operator, conservation, solvability/identifiability, service reachability.
4. [VVUQ_IDENTIFIABILITY_AND_DATA_GATES.md](VVUQ_IDENTIFIABILITY_AND_DATA_GATES.md) — dimension, energy and solver verification; actual-observable calibration; temporal/hardware/joint-interface independent validation; consent/time-synchronization and robust service requirements.
5. [SYNTHETIC_ELECTROTHERMAL_SANITY_V0.py](SYNTHETIC_ELECTROTHERMAL_SANITY_V0.py) — standalone Python 3 synthetic sanity tests for energy balances, AC/DC loss, numerical refinement and temperature-dependent offer power. **Not calibrated, not a field scenario, not a standards implementation, and not a multi-site cross-infrastructure validation.** It intentionally has no battery capacity/SoC termination and therefore 2-hour delivered DC energy is an unconstrained port-energy integral, **not** an EV journey or battery storage claim.

### Executable check

`python3 SYNTHETIC_ELECTROTHERMAL_SANITY_V0.py`

The same locally inspected code passed its included unit/sanity checks; reported synthetic 2h output was 100.0 kWh at 25°C and 64.3074 kWh at 50°C, entirely determined by **arbitrary illustrative parameters** and intentionally omitted BMS limits. **Do not use numbers as empirical prediction or physical capability.**

### Scientific status

- **Stage 2 three-paper comparative matrix:** COMPLETE, source-bounded.
- **Stage 3 remaining priority 30:** INCOMPLETE; 6 original publisher PDFs, 1 author accepted manuscript and 1 indexed publisher article among 30; 22 priority originals still unverified. Susa 2005 original article and complete normative IEEE/IEC standards unverified.
- **Stage 4 proposed mathematics:** v0 DERIVED under listed assumptions; not fitted, proved to be formally viable, experimentally validated, or frozen.
- **Stage 5 VVUQ:** preregistered protocol/logic complete; no new raw training data or joint experiment.
- Gong and Kunlasing original ASU PDFs are secured within the conversation, not redistributed through GitHub. Krama original PDF previously verified, raw 1/5-min measurements unreceived. Corresponding-author email request reported sent by user; not independently verified.

### Existing upstream/source audits
- ../gong_original_ieee_2026_10_17/GONG_2015_ORIGINAL_IEEE_EVIDENCE_AUDIT.md
- ../kunlasing_original_ieee_2026_10_17/KUNLASING_2022_ORIGINAL_IEEE_PHYSICS_CONTROL_VALIDATION_AUDIT.md
- ../krama_original_pdf_2026_10_16/KRAMA_ORIGINAL_PDF_PHYSICS_MATHEMATICS_VALIDATION.md

**Research integrity gate:** Existing prior art covers transformer heat dynamics, thermal control of charging, and charger heat derating independently. A new coupling equation is a **hypothesis** until original physical source/control/receiver measurements are synchronized and physically attributed. No global novelty claim is made.

### Mathematical continuation — reduced-model proof v0.1 (2026-10-17)

- [REDUCED_COUPLING_EQUILIBRIUM_AND_STABILITY_V01.md](REDUCED_COUPLING_EQUILIBRIUM_AND_STABILITY_V01.md) establishes, under restrictive constant-ambient, constant-efficiency, instantaneous monotone-cap assumptions: (1) uniqueness of an electrothermal operating equilibrium by scalar fixed-point monotonicity; (2) local exponential stability away from nonsmooth guard ties by negative Jacobian trace and positive determinant; (3) a conditional local tradeoff in which EVSE derating can reduce instantaneous transformer copper losses while decreasing charging service. These are **newly derived mathematical propositions** under stated assumptions, **not** evidence of causal site validation or global novelty.
- [VERIFY_REDUCED_STABILITY_V01.py](VERIFY_REDUCED_STABILITY_V01.py) is a *synthetic only*, standalone numerical check for three idealized regimes (charger-limited, transformer-limited and unrestricted), operating point root, Jacobian finite differences and AC/DC energy accounting. Toy thresholds are **NOT** real device safety ratings. A separate local expanded verifier was executed successfully; the committed compact verifier should be run in GitHub CI before marking computational verification complete.
- Strong scientific restriction: local stability of this 2-state toy **does not imply** global stability, safety, compliance, charging-service viability, realistic battery acceptance, or validity of the 3-state transformer oil/winding + charger model under delays, hysteresis, loss nonlinearity, harmonics and network power-flow effects.

### Three-state mathematical continuation (17 October 2026)

- [THREE_STATE_ELECTROTHERMAL_THEOREMS_V01.md](THREE_STATE_ELECTROTHERMAL_THEOREMS_V01.md) — full-variable/unit/provenance table, power-to-winding and charger heating equations, **3-state** existence/uniqueness proof, exact cubic Routh–Hurwitz proof of local exponential stability under differentiable nonincreasing thermal power caps, ambient sensitivity, inward-pointing safety enclosure, and a constructive sufficient constant-power service/deadline certificate. Also documents non-identifiability, observation mapping, and why delayed/hybrid operation is unproven.
- [VERIFY_THREE_STATE_THEOREMS_V01.py](VERIFY_THREE_STATE_THEOREMS_V01.py) — standalone synthetic Python/numpy verifier. Three active regimes, fixed point, analytical/finite-difference Jacobian, characteristic polynomial, copper/charger energy balance, invariant enclosure, ambient monotonicity, sufficient toy service example, smooth joint-cap random cases and time-step refinement. **GitHub CI execution still needed; independent local equivalent verifier passed.** All test thresholds and results are arbitrary mathematical checks, not verified safety limits.
- [THREE_STATE_EXECUTION_STATUS_2026_10_17.md](THREE_STATE_EXECUTION_STATUS_2026_10_17.md) — 7-stage research-gate status and blocked source/data conditions.

**Claim boundary:** This is a proven conditional *three-effective-temperature* model, **not** proof that existing power/transport field data establish a validated three-state physical interdependency, globally robust viability, current standard compliance, or novel research result relative to all global prior art.

### Mathematical continuation — bounded delay, hysteresis, AC DAE and observations (2026-10-17)

- [DELAYED_HYBRID_DAE_OBSERVABILITY_V01.md](DELAYED_HYBRID_DAE_OBSERVABILITY_V01.md) — full variables/units glossary, lagged functional differential equations, **sufficient** dimensionless delay-independent small-gain bound `kappa=hmax*Lo/r+ell*Lc/s<1` for fixed-mode incremental exponential convergence under finite bounded delays, explicit first-exit proof, separate delayed-scalar instability crossing counterexample, hysteresis no-chattering bound, mode-independent thermal upper enclosure, real/reactive AC power-flow DAE and an illustrative resistive-feeder branch singularity, sampling-aware observation operators, actual source measurement boundaries.
- [VERIFY_DELAY_HYBRID_DAE_OBSERVATION_V01.py](VERIFY_DELAY_HYBRID_DAE_OBSERVATION_V01.py) — standalone synthetic Python/numpy numerical checks for small-gain spectral radius, imaginary-root crossing, relay transitions, resistive feeder voltage limit, structural observable sensor pair and 500 artificial face-invariance cases. An independently constructed local equivalent script passed all six checks; the **exact committed GitHub file is not yet verified by GitHub Actions**.
- **No claim that the complete delayed switched three-state DAE is globally stable, that physical safety limits have been observed, or that combined Power–EVSE thermal response is empirically identified.** A grid DAE fold can invalidate an otherwise regular ODE branch; real operating modes require actual controls/telemetry.


### Research continuation — AC feeder, thermal current coupling, constrained service reachability (17 October 2026)

- [AC_FEEDER_THERMAL_REACHABILITY_V01.md](AC_FEEDER_THERMAL_REACHABILITY_V01.md): full glossary with each symbol's physical meaning and SI unit, independent MATPOWER 8.1 source equation provenance, exact balanced two-bus phasor power-flow derivation and high-voltage branch discriminant, transformer winding-vs-feeder loss distinction, exact held-input three-state heat flow, safety and charging-deadline specifications, general reach-avoid quantifiers vs deliberately restricted two-scenario open-loop exhaustive search, reproducible arbitrary assumptions and validation blockers.
- [VERIFY_AC_FEEDER_REACHABILITY_V01.py](VERIFY_AC_FEEDER_REACHABILITY_V01.py): Numpy/SciPy standalone mathematical checker. The **locally executed prototype** passed eight independent nonlinear complex AC residual comparisons, fold detection, heating and loss accounting, all 4096 six-stage candidate schedules under two toy scenarios, stage-interior temperature maxima and a 25-kWh nameplate infeasibility proof. **The exact GitHub-committed script bytes are present and structurally reviewed; GitHub CI execution remains outstanding.**
- **Synthetic result:** under invented rated/safety/heat/weather/control parameters only, 17 kWh DC-port requirement in 2 h has one feasible common open-loop 20-minute schedule (12,8,8,8,8,8) kW delivering 17.333 kWh. Neither a complete robust viability kernel nor a real transport charging prediction.
- **Independent verification limit:** MATPOWER nodal power-flow identities are published and used for derivation, and an independently coded SciPy power-flow residual crosschecks the analytic two-bus solver, but MATPOWER software was not run, an official IEEE 13-node case was not loaded, and no measured distribution feeder was matched. The next gate is an actual independent IEEE standard feeder benchmark, plus synchronized real power–charger thermal data.

**Evidence boundary:** This work is mathematically/algorithmically source-grounded but is not physically calibrated or experimentally validated for joint transformer–EVSE thermal causality. Do not merge the stacked PR as a completed field resilience demonstration.
