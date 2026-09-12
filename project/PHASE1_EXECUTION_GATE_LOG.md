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
PHASE1_CANONICAL_EXECUTION_IDENTITY_V1.md
PHASE1_DATA_PROVENANCE_REGISTER_V1.md
PHASE1_VERIFICATION_TEST_MATRIX_V1.md
PHASE1_VERIFICATION_EXECUTION_RESULTS_V1.md
PHASE1_CONFIRMATORY_H1_H2_MATRIX_V1.md
PHASE1_ACN_ACQUISITION_BLOCKER_V1.md
```

---

## 2. Current phase state

| Gate | State | Meaning |
|---|---|---|
| P1-0 canonical contract | `CLOSED` | dependency object frozen as `(C_e,Sigma_e,Pi_e)` |
| P1-1 experiment specification | `CLOSED / PREREGISTERED` | benchmarks, equations, mappings and model variants frozen |
| P1-2 data identity | `PARTIAL / G_D=0` | MATPOWER + Sioux Falls are locally RAW_HASHED; ACN remains credential-blocked |
| P1-3 parameter register | `CLOSED / FROZEN` | parameter classes, values/ranges and calibration permissions frozen |
| P1-4 software environment | `CLOSED / G_ENV=1` | hash-lock, exact code SHA, linux/amd64 OCI identity and smoke evidence frozen |
| P1-5 verification design | `CLOSED / PREREGISTERED` | mandatory verification suite frozen before confirmatory execution |
| P1-6 H1/H2 decision rules | `CLOSED / PREREGISTERED` | effect metrics, thresholds, model contrasts and falsification logic frozen |
| P1-7 executable implementation | `IMPLEMENTED / VERIFICATION-ONLY` | executable code SHA `a11914a1e7d015d75209e32c84a2459114ba7f17` |
| P1-8 mathematical verification | **`EXECUTED / NOT CLOSED; G_V=0`** | power/public schema tests pass; Sioux Falls convergence fails; ACN-dependent tests blocked |
| P1-9 calibration/holdout validation | `BLOCKED` | requires `G_D=1` and `G_V=1` |
| P1-10 H1/H2 confirmatory execution | `BLOCKED` | requires verified + sufficiently validated model |
| Stage-5 viability/resilience | `BLOCKED` | requires Phase-1 closure |

---

## 3. Closed reproducibility evidence

Canonical environment run:

```text
run ID              = 34700099915
job ID              = 103570219520
H_code              = a11914a1e7d015d75209e32c84a2459114ba7f17
H_lock              = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env               = sha256:02dcd331815e060c6f9601c9de7cfc9b9d6aa5e487bae08c6c81520b0245a716
Phase-1 host tests  = 22 passed
Phase-1 OCI tests   = 22 passed
G_ENV               = 1
```

This closes the computational environment gate only.

---

## 4. Data gate

Public benchmark materialization identities are closed:

```text
case33bw.m SHA256          = b40831eeb444669ae876e2996f0dda9f05cd83e81b314b8dfca51e4890cca95d
SiouxFalls_net SHA256      = ace99b24cec69c273ff0cf3d6d074110177f0cc0ae24b0c7a9f4f4cb5e27635c
SiouxFalls_trips SHA256    = 56f9566857f3f66730fd5c4232258d7ee3ac2931a476526331afd062f4958de7
```

ACN execution:

```text
workflow run ID = 34698786730
credential gate = BLOCKED_EXTERNAL_CREDENTIAL
ACN_API_TOKEN   = absent from repository Actions secrets at execution
raw acquisition = skipped before API request
H_D             = unresolved
```

Therefore

```math
\boxed{G_D=0.}
```

---

## 5. Verification result

The immutable public benchmark workflow was executed repeatedly under the frozen threshold.

Initial full run:

```text
run ID 34699942787
Sioux Falls RG = 0.1696116807192524
criterion      = RG <= 1e-6 by max_iter=5000
verdict        = FAIL
```

After correcting the CFW restart-state implementation:

```text
correction commit = a11914a1e7d015d75209e32c84a2459114ba7f17
run ID            = 34700099913
result            = 3 passed, 1 failed
Sioux Falls RG    = 4.215612504228978e-06
criterion         = RG <= 1e-6 by max_iter=5000
verdict           = FAIL
```

Failure-evidence retention was then hardened. The same executable was rerun through workflow head `df263eb254431fca3897e460b7d9483a29393414`:

```text
run ID          = 34700331684
result          = 3 passed, 1 failed
artifact ID     = 10300236909
artifact digest = sha256:a688992b67de054f94dd5c7a7f13587285f36fc9c904c684ead11c1490302904
```

The preregistered threshold was not weakened and `max_iter` was not increased in response to the failed result.

Therefore

```math
\boxed{G_V=0.}
```

Here `0` means the noncompensable verification closure condition is false; it is not an H1/H2 result.

---

## 6. Remaining blocking conditions

The earlier environment/code blockers are closed. The active blockers are now:

```text
B1  resolve the Sioux Falls user-equilibrium numerical convergence defect
    without weakening RG <= 1e-6 or changing the frozen benchmark problem;

B2  configure authorized GitHub Actions secret ACN_API_TOKEN externally;

B3  rerun the frozen ACN workflow and record raw SHA-256, byte/record counts,
    retrieval manifest and processed/split hashes;

B4  rerun all mandatory verification tests after B1-B3 and obtain G_V=1.
```

No blocker may be bypassed by changing the benchmark/data source, removing difficult observations, opening validation data for tuning, or weakening a preregistered acceptance criterion after observing results.

---

## 7. Current allowed work

```math
\boxed{
\text{traffic-solver verification/correction}
\;\parallel\;
\text{external ACN credential configuration}
\rightarrow
\text{ACN materialization/hash}
\rightarrow
\text{complete verification rerun}.
}
```

The traffic-solver branch may add diagnostics, cross-check an independent implementation, or correct a demonstrable implementation error. Any solver change must remain mathematically equivalent to the frozen Beckmann/user-equilibrium problem and must be version-controlled.

---

## 8. Scientific interpretation rule

```text
verification failure       != hypothesis falsification;
data-acquisition failure   != hypothesis falsification;
software incompatibility   != hypothesis falsification;
validation failure         != numerical-verification failure.
```

The correct current logic is

```math
\boxed{
G_{ENV}=1,
\qquad
G_D=0,
\qquad
G_V=0,
\qquad
G_{VAL}=\text{BLOCKED},
\qquad
G_{H1}=G_{H2}=\text{BLOCKED}.
}
```

---

## 9. Current overall state

```text
PHASE 1B/1C METHODOLOGY: FROZEN
REPRODUCIBLE ENVIRONMENT: CLOSED
PUBLIC P/T DATA PROVENANCE: CLOSED
ACN DATA GATE: BLOCKED_EXTERNAL_CREDENTIAL
FULL VERIFICATION: EXECUTED BUT NOT CLOSED
VALIDATION: NOT AUTHORIZED
H1/H2: NOT AUTHORIZED
STAGE-5 VIABILITY/RESILIENCE: NOT AUTHORIZED
```

This is the correct scientific stopping point until the two explicit verification/data blockers are resolved.
