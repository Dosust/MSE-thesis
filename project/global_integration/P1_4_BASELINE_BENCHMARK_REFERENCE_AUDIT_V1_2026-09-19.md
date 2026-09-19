# P1.4 Baseline / Benchmark / Reference Audit v1 — 2026-09-19

**Status:** EXECUTED — PASS  
**Scope:** GLOBAL_BASELINE_BENCHMARK_REFERENCE_REGISTRY_V1.md  
**Empirical effect:** NONE

## 1. Result

~~~math
\boxed{
G_{P1.4}^{design}=PASS
}
~~~

~~~text
38 PASS
0 FAIL
~~~

## 2. Audit objective

Verify that the thesis-wide registry prevents category leakage among:
- baseline;
- comparator;
- benchmark problem;
- verification fixture;
- reference solution;
- reference calculation;
- validation evidence/reference;
- synthetic truth;
- empirical ground truth;
- oracle;
- external practice/factor reference;
- requirement threshold;
- qualified case;
- treatment;
- evidence-source reference;
- auxiliary counterfactual model.

## 3. Checks

| ID | Check | Result |
|---|---|---|
| P14-01 | baseline/benchmark/reference/validation/ground-truth firewall present | PASS |
| P14-02 | synthetic truth separated from empirical ground truth | PASS |
| P14-03 | baseline ontology/subtypes defined | PASS |
| P14-04 | benchmark and verification fixture classes defined | PASS |
| P14-05 | reference solution separated from reference calculation | PASS |
| P14-06 | validation evidence/reference class defined | PASS |
| P14-07 | ground-truth policy conservative | PASS |
| P14-08 | oracle separated from validation | PASS |
| P14-09 | external practice/factor reference class defined | PASS |
| P14-10 | requirement threshold separated from reference/benchmark | PASS |
| P14-11 | qualified final case separated from benchmark class | PASS |
| P14-12 | counterfactual reconstruction model typed separately | PASS |
| P14-13 | Stage-1 fixture claim ceiling protected | PASS |
| P14-14 | Stage-2 mechanism evidence not mislabeled validation | PASS |
| P14-15 | H1 primary baseline is M1 | PASS |
| P14-16 | H1 M0 remains secondary uncoupled comparator | PASS |
| P14-17 | Stage-3 coupled benchmark truth typed synthetic | PASS |
| P14-18 | Stage-3 terminal B3 case typed QUALIFIED_CASE | PASS |
| P14-19 | model-generated OD prohibited as independent H1b truth | PASS |
| P14-20 | H2 N0 baseline typed correctly | PASS |
| P14-21 | Stage-4 validation not overstated | PASS |
| P14-22 | H3 R_curve typed information baseline | PASS |
| P14-23 | Stage-5 numerical reference solution separated | PASS |
| P14-24 | Stage-5 benchmark agreement cannot become validation | PASS |
| P14-25 | Stage-6 a0 typed intervention counterfactual baseline | PASS |
| P14-26 | Stage-6 a_BAU remains conditional | PASS |
| P14-27 | Stage-6 standards/factors not validation by default | PASS |
| P14-28 | H5 resilience-only arm typed decision baseline | PASS |
| P14-29 | Stage-7 terminal B7,3 typed QUALIFIED_CASE | PASS |
| P14-30 | Stage-7 upstream claim-ceiling inheritance preserved | PASS |
| P14-31 | calibration and validation roles separated | PASS |
| P14-32 | benchmark reproduction cannot imply validation | PASS |
| P14-33 | numerical reference solution cannot imply real-system evidence | PASS |
| P14-34 | unnamed reference prohibited for future confirmatory work | PASS |
| P14-35 | H1–H5 baseline map complete | PASS |
| P14-36 | Stage-6 v1/v2 benchmark supersession respected | PASS |
| P14-37 | no model-generated truth promoted to empirical ground truth | PASS |
| P14-38 | P1.4 design gate defined | PASS |

## 4. Key scientific resolutions

### R1 — reference is no longer a single class

The registry requires explicit subtype. For example:

~~~text
REFERENCE_SOLUTION
REFERENCE_CALCULATION
VALIDATION_REFERENCE
EVIDENCE_SOURCE_REFERENCE
EXTERNAL_PRACTICE/FACTOR_REFERENCE
~~~

These have different epistemic meanings and claim ceilings.

### R2 — Bk,3 is not globally treated as a benchmark

Where Stage-3/5/6/7 protocols use a ladder ending in a qualified thesis case, the ladder label is retained but the global class is:

~~~text
QUALIFIED_CASE
~~~

This prevents a final empirical/realistic case from inheriting synthetic benchmark semantics.

### R3 — baseline-demand models are auxiliary reconstruction models

Counterfactual demand models used to reconstruct requested demand during disruption are classified:

~~~text
AUXILIARY_COUNTERFACTUAL_MODEL
~~~

not experimental baseline and not truth.

### R4 — benchmark truth is not empirical truth

Controlled synthetic truth supports verification/synthetic validation only.

### R5 — validation evidence requires independence and intended-use relevance

A higher-fidelity model, held-out dataset, empirical observation or reconstructed service target must retain uncertainty and declared validation domain.

None is automatically called ground truth.

## 5. Current classification state

~~~text
P1.4 registry ontology = CLOSED
H1–H5 baselines = TYPED
Stage-3/5/6/7 benchmark ladders = TYPED
Stage-4 validation references = DEFERRED
empirical ground-truth assignments = NONE BY DEFAULT
future unnamed reference = PROHIBITED
~~~

## 6. Closure

~~~math
\boxed{
P1.4=PASS
}
~~~

Next:

~~~math
\boxed{
P1.5=\text{GLOBAL FINAL-CASE SCHEMA}
}
~~~

The final-case schema must now use the P1.4 classes explicitly for every data/reference/benchmark field.
