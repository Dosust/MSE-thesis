# MSE Thesis Quantitative Reporting Standard

**Standard:** `APA-JARS-QUANT-ADAPTED-V1.0 / Sustainable Engineering profile`  
**Applies to:** thesis chapters containing mathematical models, numerical experiments, case-study calculations, simulations, calibration/validation, sensitivity analysis, and quantitative infrastructure-resilience evidence.

This profile adapts JARS–Quant principles to sustainable engineering. It does not replace ASU thesis requirements, engineering codes/standards, PRISMA for systematic-review stages, or discipline-specific validation requirements.

## Required evidence chain

`research question -> physical/system boundary -> governing equations -> data/parameter provenance -> initial/boundary conditions -> numerical method -> verification -> validation -> scenario experiment -> uncertainty/sensitivity -> resilience/viability result -> bounded engineering interpretation`.

## Introduction

State the infrastructure problem, coupled-system mechanism, literature gap, research question, quantitative contribution, and system boundary. Distinguish what is theoretically derived, numerically simulated, empirically observed, and externally sourced.

## Methods

Every quantitative thesis chapter must report:

- system components and interfaces;
- spatial and temporal boundary;
- governing conservation/constitutive/dynamic equations;
- all variables, symbols, units, and sign conventions;
- initial and boundary conditions;
- parameter values and provenance;
- data sources and preprocessing;
- assumptions and simplifications;
- numerical solver/algorithm and version;
- discretization/time step where relevant;
- tolerances and stopping criteria;
- calibration method if used;
- verification tests (e.g., conservation, manufactured/simple cases, limiting behavior);
- validation evidence against observations, literature benchmarks, or independent data where available;
- uncertainty model and parameter distributions/ranges;
- scenario/hazard definitions;
- sensitivity-analysis method;
- reproducibility environment, seeds, configuration, and hashes.

## Physical and numerical integrity gates

A quantitative engineering result cannot receive `REPORTING_STANDARD_PASS` unless applicable checks confirm:

- dimensional/unit consistency;
- conservation/mass-energy-flow consistency where governing physics requires it;
- feasible state/control bounds;
- numerical convergence/stability at the reported resolution;
- reproducible parameter mapping;
- no silent solver failures;
- explicit handling of infeasible scenarios;
- clear separation of calibration data from validation evidence when possible;
- uncertainty propagated to decision-relevant outputs rather than reported only on inputs.

## Results order

1. analyzed system/case and parameter realization;
2. verification and numerical diagnostics;
3. validation/calibration evidence;
4. primary model outputs;
5. interface/coupling effects;
6. viability/resilience/service-continuity measures;
7. uncertainty intervals/distributions;
8. sensitivity and failure modes;
9. scenario comparisons;
10. exploratory extensions.

Report magnitudes with units. For simulation ensembles, report central tendency plus appropriate ranges/quantiles/intervals. For threshold results, report uncertainty in the threshold and the conditions under which it is valid.

## Figures and tables

Final quantitative figures must be generated from controlling model outputs whenever possible. Captions must state system/scenario, units, parameterization, and whether results are observed, calibrated, or simulated. Preserve native vector graphics for equations/network/system diagrams and high-resolution exports for publication. Do not visually imply empirical validation when a figure contains simulation only.

## Discussion

The Discussion must distinguish:

- mathematical implication;
- physical interpretation;
- case-specific engineering implication;
- evidence-supported generalization;
- unresolved model-form and parameter uncertainty.

Never infer field effectiveness solely from simulation. State which interfaces, hazards, scales, or sectors fall outside the modeled boundary.

## Systematic-review integration

Literature-review chapters should use the governing review protocol/PRISMA workflow. JARS–Quant becomes controlling when the thesis reports new quantitative analyses, model fitting, simulations, experiments, or statistical synthesis. Evidence extracted from literature must retain source anchors and provenance.

## Reproducibility release package

Before a thesis result is treated as frozen, archive:

- governing-equation/model specification;
- parameter/data manifest and provenance;
- solver and environment specification;
- configuration/scenario files;
- executed code/notebooks;
- verification and validation reports;
- uncertainty/sensitivity outputs;
- native figure code and exports;
- final numerical tables;
- hashes and report-producing commit/tag.

The canonical cross-project standard is maintained in `Dossiya-SE/Dossiya-SE/docs/APA_JARS_QUANT_ADAPTED_REPORTING_STANDARD.md`.
