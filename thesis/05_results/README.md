# Chapter 5 — Results

**Writing/inference authority:** [`../00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`](../00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md)  
**Experiment authority:** [`../00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md`](../00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md)

## Purpose

Report outputs from frozen confirmatory or explicitly declared exploratory analyses without interpretation inflation.

## Required one-to-one structure

```math
\boxed{\text{Chapter-IV experiment}\longleftrightarrow\text{Chapter-V result}}
```

Recommended sections:

1. H1 results — dynamic causal coupling;
2. H2 results — information and organization;
3. H3 results — viability/reachability incremental information;
4. H4 results — intervention performance and sustainability consequences;
5. H5 results — joint engineering decision;
6. supporting interface-criticality results, if separately declared;
7. conditional adaptive-transformation results, if scientifically activated;
8. cross-hypothesis robustness and sensitivity.

## Result reporting object

For every principal result report:

```math
\boxed{
\text{experiment/result ID}
\rightarrow
\text{estimate}
\rightarrow
\text{uncertainty}
\rightarrow
\text{threshold/decision rule}
\rightarrow
\text{test outcome}
\rightarrow
\text{validity domain}.
}
```

Where applicable also report sample/scenario support, effect size or practical engineering magnitude, missingness, sensitivity and protocol deviations.

## Theory-to-result link

When Chapter III or IV creates a theoretical expectation, explicitly compare it with the numerical/empirical observation:

```math
\boxed{
\text{theoretical/physical expectation}
\overset{\text{declared experiment}}{\longleftrightarrow}
\text{observed result}.
}
```

Agreement is evidence within the tested domain; disagreement must be retained and investigated rather than hidden.

## Reporting rules

- retain null and negative findings;
- report uncertainty with point estimates;
- separate statistical/model discrimination from engineering materiality;
- disclose protocol deviations/amendments;
- separate confirmatory and exploratory results;
- do not use causal language beyond what the design supports;
- do not infer probability from unweighted scenario frequencies without a justified probability model;
- preserve raw-to-result provenance;
- do not rename an intervention “efficient” or “sustainable” unless the preregistered operational definition is satisfied;
- do not treat supporting interface diagnostics as primary H4/H5 results unless separately promoted and tested.

## Current state

H1 confirmatory result sections remain blocked until row-level data retrieval/qualification and subsequent preregistered execution are authorized and completed. Other hypothesis sections remain blocked by their respective preregistration/evidence gates.

## Exit gate

Chapter V passes only when every confirmatory result maps to a frozen Chapter-IV method, uncertainty and validity are reported, null/negative outcomes remain visible, and exploratory outputs are clearly labeled.

See [`../00_governance/THESIS_COMPLETION_GATES.md`](../00_governance/THESIS_COMPLETION_GATES.md).
