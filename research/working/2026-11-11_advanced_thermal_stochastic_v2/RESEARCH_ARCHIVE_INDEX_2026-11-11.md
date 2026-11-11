# ASU thesis: reproducible research archive, 11 November 2026

**Official title:** Engineering of Power–Electrified Transportation Interdependencies for Resilience.

**Status:** WORKING RESEARCH EVIDENCE. Computations executed by assistant, **not** independently repeated by the researcher or accepted by an advisor. This archive does not change any frozen canonical thesis authority. No same-site heat-mediated Power–Transportation causation, 30 °C-plus empirical validation, or charging-induced transformer aging has been demonstrated.

## Saved packages and SHA-256

| Phase | Package | Files in ZIP | SHA-256 |
|---|---|---:|---|
| 1 | `thesis_research_execution_20261111.zip` | 8 | `4c1c9ba887067d8c0530d473eed6261ddf962a6936e3749c76d24f3c091d9b4a` |
| 2 | `ASU_Thesis_Drive_Only_Research_Execution_2026-11-11.zip` | 21 | `3bf6f45008f4e33c2862b523fbcb7fb323c03b3cc1c8c5d17491da6e511c59a6` |
| 3 | `ASU_Advanced_Physics_Stochastic_Charging_2026-11-11.zip` | 24 | `dc9d8c7eb72c7497349f1d5f3f93c6ce5b4ba8b33da78563061506cdede5fea6` |

Each ZIP integrity check passed. ZIPs contain derived reports, executable Python and results, without raw original measurements. Read `RESEARCH_ARCHIVE_MANIFEST_2026-11-11.json` for per-file hashes, original data identities and recorded scientific boundaries.

## Exact latest-run results, and interpretation

- SINTEF: 8,592 records; 6,012 train and 2,576 chronological held-out contiguous one-hour pairs. Effective one-state model RMSE 0.2165286606 °C versus persistence 0.2516987404 °C. **Model MAE 0.1498538702 °C is worse than persistence 0.1449809092 °C.**
- SINTEF thermal load-order counterfactual: 106 within-installation 24-hour windows, fixed observed ambient and initial state, current samples rearranged with total squared-current exposure unchanged. **Median absolute difference in modeled final temperature 0.3548588306 °C.** Does not demonstrate EV causation.
- SINTEF seasonal effective time constants: Jan–Apr 15.9818 h, May–Aug 8.2944 h, Sep–Dec 13.5708 h. Local normalized one-step sensitivity condition number 2.4247; seasonal shifts do not prove structural non-identifiability.
- SINTEF observed hot-spot channels are below top oil in 84.11% (HV) and 70.94% (LV) of paired samples. **Aging-life estimation blocked**, pending original sensor semantics and aging-law qualification; no verified equipment limit defined.
- EPFL: 1,878 sessions, 1,865 same-day, 221 observed days. Observed sample median daily maximum simultaneous sessions 2, Spearman duration-energy 0.6638. The 16 selected days' offline LP **44.0092% median modeled peak reduction compares to a hypothetical front-loaded comparator**, not measured before/after. Energy-meter reconciliation remains open.
- KU Leuven: 40,873 battery/electrical observations, 12 backward timestamp steps. Pack temperature is not charger/EVSE rectifier temperature.
- STREAM: 419,184 aligned P/Q station-time pairs; power units, asset ratings, transfer mapping unresolved.
- Chronological absolute-residual band: nominal 90%, 95.282% empirical holdout coverage on a 60/20/20 temporal split; not guaranteed calibrated forecast coverage. Numerical ODE integration benchmark verifies solver behavior, not physical model.

## Source and reproduction controls

- Original measured files remain in Google Drive and are **not distributed with these ZIPs**. Six input SHA-256 values and source identifiers are in `ORIGINAL_INPUT_MANIFEST.json` inside the latest ZIP and in the archive manifest.
- Latest ZIP entry point: `REPRODUCE.md`; scripts `run_advanced_experiments.py`, `epfl_reproduce.py`, and `verify_experiment_results.py`, plus requirements, JSON outputs, plots and detailed reports 00 through 08.
- Scripts use absolute `/mnt/data` paths; adapt these to the local environment, install dependencies, and restore the six original source files with exactly matching checksums. The EPFL replay script has its own output directory; do not treat that as evidence of experiment divergence.
- Previous November 11 phases use different scripts/inputs/evaluation definitions. Do not replace their results silently or mix evaluation baselines.

## Scientific gates

| Gate | Status |
|---|---|
| SO1 directional thermally induced Power↔Transportation mechanism | PARTIAL COMPONENT ONLY; real directed thermal link NOT ESTABLISHED |
| SO2 physics-based state-time thermal formulation | PARTIAL: reduced transformer ODE and numerical tests; coupling OPEN |
| SO3 physical critical transitions, propagation and service outcomes | BLOCKED: linked operating limits, control action and service requirements missing |
| Transformer aging-life | BLOCKED: sensor semantics, insulation-specific law, admissible thresholds |
| Harmonic-loss analysis | BLOCKED: qualified harmonic spectra/waveforms missing |
| Thermal-constrained scheduling | BLOCKED: equivalent equipment-specific power/current/thermal capability transfer mapping |
| Extreme-heat validation | BLOCKED: SINTEF ambient maximum 25.97 °C |

## Authorship and authority

Assistant-generated code and results are exploratory working outputs. They are **not** independently researcher-executed or supervisor-approved claims. Preserve original dated evidence, working artifacts and canonical scope documents unchanged. Scientific novelty and system-level causal attribution are unresolved. All future reruns must record source checksums, code version, protocol, metric definitions, sample sizes, uncertainties and negative findings.

Current authority: `project/CANONICAL_THESIS_TITLE_V3.md`, `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`, `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`, and `project/PHYSICS_MATHEMATICS_FIRST_HYPOTHESIS_TESTING_SCOPE_DIRECTIVE_V1.md` in the thesis GitHub repository.
