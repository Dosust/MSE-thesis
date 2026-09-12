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
PHASE1_NUMERICAL_SOLVER_AMENDMENT_V1.md
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
| P1-2 data identity | `PARTIAL / G_D=0` | MATPOWER + Sioux Falls are raw-hashed and provenance-closed; ACN remains credential-blocked |
| P1-3 parameter register | `CLOSED / FROZEN` | parameter classes, values/ranges and calibration permissions frozen |
| P1-4 software environment | `CLOSED / G_ENV=1` | exact BFW code SHA, hash-lock, linux/amd64 OCI identity and smoke evidence frozen |
| P1-5 verification design | `CLOSED / PREREGISTERED` | mandatory verification suite frozen before confirmatory execution |
| P1-6 H1/H2 decision rules | `CLOSED / PREREGISTERED` | effect metrics, thresholds, model contrasts and falsification logic frozen |
| P1-7 executable implementation | `IMPLEMENTED / VERIFICATION-ONLY` | executable code SHA `d6d97c7353f6d5694dba73ab840ae3a2548dd593` |
| P1-8 public P/T mathematical verification | **`PASS`** | power balance/sign checks + Sioux Falls BFW convergence/conservation/closure pass |
| P1-8 complete mathematical verification | **`NOT CLOSED; G_V=0`** | ACN-dependent/full-coupled verification and complete `R*` remain unresolved |
| P1-9 calibration/holdout validation | `BLOCKED` | requires `G_D=1` and complete `G_V=1` |
| P1-10 H1/H2 confirmatory execution | `BLOCKED` | requires verified + sufficiently validated model |
| Stage-5 viability/resilience | `BLOCKED` | requires Phase-1 closure |

---

## 3. Closed reproducibility evidence

Canonical environment run on the successful BFW executable head:

```text
run ID              = 34700750356
job ID              = 103571958645
H_code              = d6d97c7353f6d5694dba73ab840ae3a2548dd593
H_lock              = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env               = sha256:ee7469b8ec78c8bf9988fd1c33a7b85de6a49a636ade3337981c56944def50af
Docker image ID     = sha256:9790b75c9857d473f60402a2b79192e085d559f7caa8369df8ec078f83d7b657
OCI archive SHA256  = c13061011790320ef987578b91edb462cf7cff5c18b2fc4cb4c767060726d80c
Phase-1 host tests  = 22 passed
Phase-1 OCI tests   = 22 passed
ACN upstream tests  = 95 passed, 1 warning
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

ACN execution remains deliberately blocked at the external credential boundary:

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

This `0` means complete data provenance is not closed; it is not evidence against ACN data quality or against H1/H2.

---

## 5. Verification result — preserved failure history and current PASS

Earlier immutable Sioux Falls executions failed the frozen numerical threshold and remain part of the audit trail:

```text
run 34699942787
RG = 0.1696116807192524
criterion = RG <= 1e-6 by max_iter=5000
verdict = FAIL

corrected CFW code SHA = a11914a1e7d015d75209e32c84a2459114ba7f17
run 34700099913
RG = 4.215612504228978e-06
criterion = RG <= 1e-6 by max_iter=5000
verdict = FAIL
```

A versioned Biconjugate Frank-Wolfe numerical amendment was then implemented for the same frozen Beckmann problem. The benchmark, BPR parameters, OD matrix, gap definition, tolerance and iteration cap were not changed.

Canonical successful public benchmark run:

```text
run ID              = 34700750330
job ID              = 103571958582
code SHA            = d6d97c7353f6d5694dba73ab840ae3a2548dd593
benchmark tests     = 4 passed in 3.79 s
Phase-1 fixtures    = 22 passed in 0.08 s
report SHA256       = 4f2b27af34459c7b4022813a58ed93c457eb2430cea660f88f5f5877b81f6a35
artifact ID         = 10300177541
artifact ZIP SHA256 = 3a87c5ec991e2addf7dde8d0ba896ce0d507a8aecfccba4b44b4c8ff4ef0c73f
```

Power verification:

```text
max balance residual = 3.0808688933348094e-14
bus24 voltage base   = 0.9726811009691813 pu
bus24 voltage +0.1MW = 0.9714126540936994 pu
I23-24 base          = 0.09581473734223377 pu
I23-24 +0.1MW        = 0.10532607030491578 pu
```

Transportation verification:

```text
solver                       = biconjugate-frank-wolfe
iterations                   = 645
relative gap                 = 9.33748496131895e-07
scaled node-balance residual = 1.715075976720996e-16
crew base cost               = 25.92894954231427
crew closed cost             = 27.61418250234074
```

Hence the previously active transportation convergence blocker is closed because

```math
9.33748496131895\times10^{-7}<10^{-6}
\quad\land\quad
645<5000.
```

The preregistered tolerance was not weakened and `max_iter` was not increased.

---

## 6. Complete verification-gate assessment

Public P/T verification now passes, but full Phase-1 verification remains noncompensable and includes ACN/full-coupled requirements.

```text
G_V1 equations/algorithms          PARTIAL-PASS
G_V2 units/dimensions              PARTIAL-PASS
G_V3 conservation/balance          PUBLIC P/T PASS
G_V4 limiting cases                PARTIAL-PASS
G_V5 numerical convergence         PUBLIC P/T PASS
G_V6 implementation invariance     PARTIAL-PASS
G_V7 synthetic known answers       PASS in implemented fixture domain
G_V8 parameter/sensitivity coherence NOT FULLY EXECUTED
G_V9 complete R* reproducibility   BLOCKED by unresolved ACN H_D
```

Define

```math
G_V=1\iff\forall k\in\{1,\ldots,9\},\;G_{Vk}=1.
```

Therefore

```math
\boxed{G_V=0\text{ (complete closure false).}}
```

This no longer reflects a public transportation convergence failure. It reflects unresolved ACN-dependent/full-coupled verification.

---

## 7. Active blocking conditions

The earlier environment and transportation-solver blockers are closed. The active hard path is now:

```text
B1  configure an authorized GitHub Actions repository secret named ACN_API_TOKEN;

B2  rerun the already-frozen authenticated ACN workflow without changing site,
    date window, timeseries flag, client version or QC rules;

B3  record raw ACN SHA-256, byte count, record count, manifest/page hashes,
    retrieval timestamp and credential-hygiene PASS;

B4  execute deterministic ACN processing/QC and freeze processed + chronological
    calibration/validation split hashes;

B5  execute all remaining ACN-dependent/full-coupled mandatory verification tests;

B6  obtain complete G_V=1 before opening validation/H1/H2.
```

No blocker may be bypassed by substituting another charging dataset, modifying the frozen ACN window, removing inconvenient records after outcome inspection, or weakening a preregistered criterion.

---

## 8. Exact user-side unblock operation

The only external action required from the user is:

```text
GitHub repository
-> Settings
-> Secrets and variables
-> Actions
-> New repository secret
-> Name: ACN_API_TOKEN
-> Value: the user's authorized Caltech ACN API token
```

The token must **never** be pasted into chat or committed to the repository.

After the secret exists, rerun workflow `Phase 1 authenticated ACN acquisition` and preserve the resulting immutable evidence.

---

## 9. Current scientific interpretation

```math
\boxed{
G_{ENV}=1,
\qquad
G_D=0,
\qquad
G_V=0,
\qquad
G_{VAL}=\mathrm{BLOCKED},
\qquad
G_{H1}=G_{H2}=\mathrm{BLOCKED}.
}
```

Important distinctions:

```text
verification failure       != hypothesis falsification;
data-acquisition blocker   != hypothesis falsification;
public benchmark PASS      != full coupled-model validation;
G_ENV=1                    != G_V=1.
```

---

## 10. Current overall state

```text
PHASE 1B/1C METHODOLOGY: FROZEN
REPRODUCIBLE ENVIRONMENT: CLOSED
PUBLIC P/T DATA PROVENANCE: CLOSED
PUBLIC P/T BENCHMARK VERIFICATION: PASS
TRANSPORT CONVERGENCE BLOCKER: CLOSED
ACN DATA GATE: BLOCKED_EXTERNAL_CREDENTIAL
COMPLETE G_V: NOT CLOSED
VALIDATION: NOT AUTHORIZED
H1/H2: NOT AUTHORIZED
STAGE-5 VIABILITY/RESILIENCE: NOT AUTHORIZED
```

The scientifically correct stopping point is now the external ACN credential/data-provenance boundary, followed by the remaining ACN-dependent/full-coupled verification tests.
