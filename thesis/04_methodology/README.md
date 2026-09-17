# Chapter 4 — Methodology and Experimental Design

**RQ–SO–H authority:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Experiment authority:** `../00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md`  
**Writing/inference authority:** `../00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`

## Purpose

Convert hypotheses into preregistered, reproducible experiments with explicit baselines, held constants, treatments, data qualification, verification, validation, uncertainty, practical significance and falsification.

## Core structure

1. EGMIV research method
2. evidence-search and qualification
3. data provenance and row-level qualification
4. minimal sufficient experimental realization
5. H1 — dynamic causal interdependency experiment
6. H2 — information/organization/feasible-control experiment
7. H3 — viability/reachability incremental-information experiment
8. H4 — intervention effectiveness/efficiency/sustainability-consequence experiment
9. H5 — joint resilience–sustainability decision experiment
10. supporting interface-criticality analysis, if activated
11. optional adaptive/sequential transformation extension, if separately activated
12. verification
13. validation
14. uncertainty quantification and sensitivity
15. decision/falsification rules
16. computational reproducibility

## Experiment object

```math
\boxed{
\mathcal T_i=
(H_i,M_i,B_i,\Omega_i,D_i,\theta_i,X_i,T_i,Z_i,\delta_i,\mathcal F_i,V_i,U_i)
}
```

where `X_i` records held-constant conditions and `T_i` records the treatment/change. Calibration, verification and validation roles of `D_i` must be declared separately.

## Confirmatory design rule

Before execution, each primary hypothesis must have:

- comparator/baseline;
- held constants;
- treatment/change;
- primary response vector;
- practical/engineering significance criterion;
- uncertainty treatment;
- scenario/domain;
- data role and provenance;
- verification/validation protocol;
- falsification/non-support condition.

A failed prerequisite gate produces `NOT TESTED`, not hypothesis falsification.

## H1 current gate

Current project authority indicates M0/M1/M2 implementations and confirmatory design are advanced/frozen as applicable, but raw row-level event retrieval/qualification remains blocking. No H1 calibration or confirmatory run is authorized until the predeclared data gates pass.

## H3–H5 prerequisite rule

H3 requires frozen service/acceptability/recovery sets, horizons, uncertainty semantics, probability levels where justified, primary Skill metric and `delta_3`.

H4 requires a declared intervention set, resilience-effectiveness criterion, efficiency definition/resource denominator, sustainability accounting boundaries, consequence-distance rule and `delta_4`.

H5 requires the same candidate actions and uncertainty domain across resilience-only and joint evaluation, plus a frozen set/regret metric and `delta_5`.

Interface-ranking superiority and adaptive-pathway superiority are not silently substituted for H4/H5.

## Prohibited practices

- tuning confirmatory thresholds after observing relevant results;
- validating only the preferred model;
- treating assumed parameters as measured data;
- using training/calibration evidence as held-out validation evidence;
- changing held-out events because model performance is poor;
- suppressing null/negative results;
- introducing post hoc primary metrics without labeling the analysis exploratory;
- assigning probability distributions without defensible evidentiary support.

## Exit gate

See `../00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md` and `../00_governance/THESIS_COMPLETION_GATES.md`. Confirmatory execution is authorized only after all hypothesis-specific prerequisite gates pass.
