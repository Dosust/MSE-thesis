# Chapter 5 — Results

**Writing/inference authority:** `../00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`  
**Experiment authority:** `../00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md`

## Purpose

Report outputs from frozen or explicitly exploratory experiments without interpretation inflation.

## Required one-to-one structure

```math
\boxed{\text{Chapter 4 experiment}\longleftrightarrow\text{Chapter 5 result}}
```

Recommended sections:

1. H1 results — dynamic causal coupling;
2. H2 results — information and organization;
3. H3 results — viability/reachability incremental information;
4. H4 results — intervention effectiveness, efficiency and sustainability consequences;
5. H5 results — joint resilience–sustainability engineering decision;
6. supporting interface-criticality results, if activated and qualified;
7. optional adaptive/sequential transformation results, if separately activated;
8. cross-hypothesis robustness and sensitivity.

## Result reporting object

```math
\boxed{
\text{experiment ID}
\rightarrow\text{estimate/output}
\rightarrow\text{uncertainty}
\rightarrow\text{practical/decision threshold}
\rightarrow\text{hypothesis status}
\rightarrow\text{validity domain}.
}
```

## Theory-to-result link

Where a Chapter-3 derivation implies an expected qualitative or quantitative behavior, report the comparison explicitly:

```math
\boxed{
\text{theoretical expectation}
\longleftrightarrow
\text{numerical/empirical observation}.
}
```

Agreement is not automatically validation; disagreement must not be hidden and may reveal model, parameter, numerical or theoretical limitations.

## Reporting rules

- retain null and negative findings;
- report uncertainty with point estimates;
- report effect size/practical significance where applicable, not only statistical significance;
- disclose protocol deviations/amendments;
- separate confirmatory and exploratory results;
- do not use causal language beyond experimental design support;
- preserve raw-to-result provenance;
- do not upgrade a failed prerequisite gate into a scientific negative result;
- do not introduce new primary metrics after results are observed without labeling the analysis exploratory.

## Current state

H1 confirmatory result sections remain blocked until row-level data retrieval/qualification and subsequent preregistered execution are authorized and completed. H2–H5 remain subject to their hypothesis-specific data, metric, accounting-boundary, VVUQ and preregistration gates.

## Exit gate

See `../00_governance/THESIS_COMPLETION_GATES.md`. Every reported result must trace to a declared method, uncertainty statement, decision rule and validation domain.
