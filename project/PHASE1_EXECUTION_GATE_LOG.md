# Phase 1 — Execution Gate Log

**Date:** 2026-09-12  
**Purpose:** auditable state of the transition from preregistered experiment design to executable verification/validation.  
**Rule:** status reflects completed evidence, not intended work.

---

## 1. Authority chain

```text
CANONICAL_DEPENDENCY_CONTRACT_V1.md
PHASE1_EMPIRICAL_VALIDATION_PROTOCOL.md
PHASE1_EXPERIMENT_SPECIFICATION_V1.md
PHASE1_GENERAL_TO_THESIS_EVIDENCE_MAP.md
PHASE1_DATA_MANIFEST_V1.md
PHASE1_PARAMETER_REGISTER_V1.md
PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md
PHASE1_VERIFICATION_TEST_MATRIX_V1.md
PHASE1_CONFIRMATORY_H1_H2_MATRIX_V1.md
PHASE1_ACN_ACQUISITION_BLOCKER_V1.md
```

---

## 2. Current phase state

| Gate | State | Meaning |
|---|---|---|
| P1-0 canonical contract | `CLOSED` | dependency object frozen as `(C_e,Sigma_e,Pi_e)` |
| P1-1 experiment specification | `CLOSED / PREREGISTERED` | benchmarks, equations, mappings and model variants frozen |
| P1-2 data identity | `CLOSED WITH BLOCKER` | benchmark identities fixed; ACN raw/processed hashes pending authenticated acquisition |
| P1-3 parameter register | `CLOSED / FROZEN` | parameter classes, values/ranges and calibration permissions frozen |
| P1-4 software target | `CLOSED WITH BUILD BLOCKERS` | target Python/container/direct pins frozen; OCI digest + resolved lockfile pending |
| P1-5 verification design | `CLOSED / PREREGISTERED` | mandatory verification suite frozen before code execution |
| P1-6 H1/H2 decision rules | `CLOSED / PREREGISTERED` | effect metrics, thresholds, model contrasts and falsification logic frozen |
| P1-7 executable implementation | `NOT STARTED` | no code SHA yet |
| P1-8 mathematical verification | `BLOCKED` | requires executable code + complete environment/data hashes |
| P1-9 calibration/holdout validation | `BLOCKED` | requires `G_V=1` |
| P1-10 H1/H2 confirmatory execution | `BLOCKED` | requires verification + component validation |
| Stage-5 viability/resilience | `BLOCKED` | requires Phase-1 closure |

---

## 3. Blocking conditions

Confirmatory execution is prohibited until all are satisfied:

```text
B1  full immutable OCI digest recorded;
B2  resolved hash-locked dependency file created and SHA-256 recorded;
B3  ACN authenticated raw extraction completed for frozen site/window;
B4  ACN raw SHA-256 recorded;
B5  processed ACN trajectory + split/calibration artifacts generated and hashed;
B6  executable model committed and CODE_SHA recorded;
B7  frozen environment smoke gate passes;
B8  all mandatory verification tests pass, giving G_V = 1.
```

No blocker may be bypassed by changing the benchmark/data source or weakening a preregistered test after inspecting results.

---

## 4. Immediate next allowed work

The next scientific operation is **implementation preparation**, in this order:

```math
\boxed{
\text{build frozen container}
\rightarrow
\text{resolve/hash dependencies}
\rightarrow
\text{authenticated ACN acquisition}
\rightarrow
\text{hash raw/processed data}
\rightarrow
\text{implement unit-tested model}
\rightarrow
\text{commit CODE\_SHA}
\rightarrow
\text{run verification matrix}.
}
```

The first executable runs are verification runs only. They are not H1/H2 tests.

---

## 5. Scientific interpretation rule

```text
verification failure       != hypothesis falsification;
data-acquisition failure   != hypothesis falsification;
software incompatibility   != hypothesis falsification;
validation failure         != numerical-verification failure.
```

Only a verified and sufficiently validated model may generate a confirmatory H1/H2 result.

---

## 6. Current overall state

```text
PHASE 1B METHODOLOGY: FROZEN
EXECUTION: NOT AUTHORIZED YET
PRIMARY REASON: reproducibility/data/code blockers remain explicit and unresolved
```

This status is intentional and scientifically preferable to generating early coupled results from an incompletely locked environment.
