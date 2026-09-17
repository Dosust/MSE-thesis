# Chapter 4 — Methodology and Experimental Design

**Experiment authority:** [`../00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md`](../00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md)  
**Writing/inference authority:** [`../00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`](../00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md)

## Purpose

Convert research questions, developmental obligations and H1–H5 into reproducible methods with explicit baselines, treatments, held conditions, data roles, validation, uncertainty and falsification.

## Core structure

1. EGMIV research method;
2. evidence-search and qualification;
3. data provenance and row-level qualification;
4. minimal sufficient experimental realization;
5. H1 — dynamic causal interdependency experiment;
6. H2 — information and organization experiment;
7. H3 — viability–reachability incremental-information experiment;
8. H4 — intervention performance and sustainability-consequence experiment;
9. H5 — joint resilience–sustainability decision experiment;
10. supporting interface-criticality analysis, if activated;
11. conditional adaptive-transformation extension, if activated;
12. verification;
13. validation;
14. uncertainty quantification and sensitivity;
15. statistical/decision rules and falsification;
16. computational reproducibility.

## Confirmatory experiment object

```math
\boxed{
\mathcal T_i=
(H_i,M_i,B_i,\Omega_i,D_i,\theta_i,Z_i,\delta_i,\mathcal F_i,V_i,U_i,C_i,X_i,R_i)
}
```

with:

- `C_i`: held/matched conditions;
- `X_i`: the treatment/representation/intervention/decision difference actually changed;
- `R_i`: data/evidence role (development, calibration, training, validation, held-out test).

## Experimental-writing requirement

For every hypothesis state explicitly:

```math
\boxed{
\text{What is held fixed?}
\quad+
\text{What is changed?}
\quad+
\text{What is measured?}
\quad+
\text{What would fail to support the hypothesis?}
}
```

This must be written before confirmatory execution.

## H1 current gate

Current project authority records M0/M1/M2 implementation and verification as advanced/frozen as applicable and the H1 confirmatory design as frozen. Raw row-level event retrieval/qualification remains blocking. No calibration or confirmatory H1 run is authorized until the predeclared data gates pass.

## H2 gate

H2 requires the nested `P+T`, `P+T+I`, `P+T+I+O` comparison under matched physical states/disturbances, with information and organizational effects separated. Empirical/domain/metric/threshold and validation specifications remain open until frozen in the experiment matrix/hypothesis authority.

## H3 gate

H3 must compare conventional performance/recovery information against the declared viability–reachability resilience object. `K`, `G_rec`, `F`, `T_V`, `T_R`, uncertainty semantics, admissible policy class, solver, primary skill/decision metric, `delta_3` and data domain must be fixed/qualified before confirmatory execution.

Interface criticality is supporting unless separately preregistered.

## H4 gate

H4 must preserve:

```math
\boxed{
\text{intervention}
\rightarrow
\text{resilience outcome}
\rightarrow
\text{effectiveness}
\rightarrow
\text{efficiency}
\rightarrow
\text{sustainability consequences}.
}
```

The intervention set, target-attainment rule, resource vector, sustainability vector, accounting boundaries, consequence-distance/materiality metric and `delta_4` must be preregistered before confirmatory analysis.

## H5 gate

H5 retains the canonical comparison

```math
\boxed{\mathcal A_R^{\star}\ \text{vs}\ \mathcal A_{R,S}^{\star}}
```

with the v2.1 requirement that effectiveness and efficiency be explicit inputs to the joint decision construction. Candidate actions, feasibility constraints, uncertainty ensemble, set/regret metric and `delta_5` must be frozen before confirmatory execution.

## Verification and validation

```math
\boxed{\text{verification}\neq\text{validation}.}
```

Verification addresses implementation/mathematical correctness. Validation addresses adequacy for intended real-system use.

No preferred model is validated alone where a rival-model claim is made.

## Prohibited practices

- tuning confirmatory thresholds after observing target results;
- changing the held-out split because model performance is poor;
- validating only the preferred model;
- treating assumed parameters as measured data;
- using calibration/training evidence as held-out validation evidence;
- reporting unweighted scenario frequency as probability without a justified probability model;
- suppressing null/negative results;
- retroactively redefining effectiveness, efficiency or sustainability to favor an intervention;
- converting an exploratory analysis into confirmatory language after seeing outcomes.

## Exit gate

Chapter IV passes only when applicable baselines, treatments, held conditions, data roles, domains, metrics, thresholds, parameter provenance, V&V, UQ and falsification rules are fixed and auditable.

See [`../00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md`](../00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md) and [`../00_governance/THESIS_COMPLETION_GATES.md`](../00_governance/THESIS_COMPLETION_GATES.md).
