# Phase 1C — Verification Execution Matrix v1

![Status](https://img.shields.io/badge/status-G_V%20NOT%20CLOSED-D73A49)
![Phase](https://img.shields.io/badge/phase-1C-0969DA)

**Initialized:** 2026-09-12  
**Execution update:** 2026-09-12  
**Authority:** `PHASE1_VERIFICATION_TEST_MATRIX_V1.md` + `PHASE1_VERIFICATION_EXECUTION_RESULTS_V1.md` + `PHASE1_CANONICAL_EXECUTION_IDENTITY_V1.md` + `PHASE1_DATA_PROVENANCE_REGISTER_V1.md`  
**Purpose:** aggregate the detailed preregistered verification tests into nine noncompensable execution gates without weakening any original test.

---

## 0. Gate logic

```math
G_V
=
\prod_{k=1}^{9}G_{Vk},
\qquad
G_{Vk}\in\{0,1\}.
```

A gate maps to `1` only when all mandatory tests assigned to it have executed and passed. `FAIL`, `PARTIAL`, `BLOCKED`, and `NOT_EXECUTED` all prevent closure.

```math
\boxed{G_V=1\iff \forall k,\;G_{Vk}=1.}
```

No averaging or compensatory score is allowed.

Execution vocabulary:

```text
PASS         executed and acceptance condition satisfied
FAIL         executed and acceptance condition violated
PARTIAL      some subordinate evidence passes but gate is not complete
BLOCKED      prerequisite unavailable
NOT_EXECUTED deliberately withheld pending upstream gates
```

---

# 1. Current gate matrix

| Gate | Question | Executed state | Binary closure |
|---|---|---|---:|
| `G_V1` | Are equations/algorithms implemented as specified? | `PARTIAL` — 22 host + 22 OCI verification fixtures pass; power benchmark passes; full traffic convergence test fails | 0 |
| `G_V2` | Are units/dimensions/source schemas consistent? | `PARTIAL-PASS` — MATPOWER and Sioux Falls ingestion/conversion tests pass; ACN path unavailable | 0 |
| `G_V3` | Are conservation/balance relations respected? | `PARTIAL` — radial power balance passes; full accepted-solution traffic conservation is not admitted because V-T02 convergence fails first | 0 |
| `G_V4` | Do limiting cases behave correctly? | `PARTIAL-PASS` — synthetic dependency/guard/closure limits pass; complete ACN-dependent limits unavailable | 0 |
| `G_V5` | Are numerical solutions convergent/stable? | **`FAIL`** — Sioux Falls full OD `RG=4.215612504228978e-06 > 1e-6` at frozen `5000` iterations | **0** |
| `G_V6` | Are outputs invariant to irrelevant implementation choices? | `PARTIAL` — deterministic host/OCI fixture evidence exists; full benchmark deterministic-report stage is blocked by V-T02 | 0 |
| `G_V7` | Do known-answer synthetic cases recover expected answers? | `PASS within frozen implemented fixture domain` — 22 host + 22 OCI fixtures pass | 1 |
| `G_V8` | Are parameter/sensitivity perturbations physically coherent? | `NOT_EXECUTED` — withheld pending solver/data verification closure | 0 |
| `G_V9` | Can the complete experiment be reproduced from immutable `R*`? | `BLOCKED_EXTERNAL_CREDENTIAL` — ACN `H_D` unresolved | 0 |

Therefore

```math
\boxed{G_V=0\quad\text{for closure}.}
```

This `0` means **the complete verification gate is not satisfied**. It is not a statement that H1/H2 are false.

---

# 2. Environment/provenance facts feeding the matrix

```text
G_ENV               = 1
canonical env run   = 34700099915
H_code              = a11914a1e7d015d75209e32c84a2459114ba7f17
H_lock              = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env               = sha256:02dcd331815e060c6f9601c9de7cfc9b9d6aa5e487bae08c6c81520b0245a716
host fixtures       = 22 passed
OCI fixtures        = 22 passed
```

Public benchmark raw identities:

```text
case33bw.m        SHA256 b40831eeb444669ae876e2996f0dda9f05cd83e81b314b8dfca51e4890cca95d
SiouxFalls_net    SHA256 ace99b24cec69c273ff0cf3d6d074110177f0cc0ae24b0c7a9f4f4cb5e27635c
SiouxFalls_trips  SHA256 56f9566857f3f66730fd5c4232258d7ee3ac2931a476526331afd062f4958de7
```

Complete data gate:

```math
\boxed{G_D=0}
```

because ACN raw acquisition, processed trajectory and chronological split hashes are not yet available.

---

# 3. Public benchmark execution

Four immutable benchmark integration tests were run.

Passed:

```text
V-D01 / case33bw source schema and conversion
power benchmark radial balance + positive-load sign
V-D02/V-D03 / Sioux Falls source schema and OD total
```

Failed:

```text
V-T02 / full Sioux Falls user-equilibrium convergence
```

Observed after the CFW restart-state implementation correction:

```math
RG_{obs}=4.215612504228978\times10^{-6},
\qquad
RG_{max}=10^{-6}.
```

Thus

```math
RG_{obs}>RG_{max}.
```

The threshold and frozen `5000`-iteration ceiling were not changed after observing the result.

---

# 4. Reproducible failure evidence

The failed benchmark state is retained as an artifact rather than discarded:

```text
preserved workflow run = 34700331684
job                   = 103570834519
workflow head         = df263eb254431fca3897e460b7d9483a29393414
underlying exec code  = a11914a1e7d015d75209e32c84a2459114ba7f17
result                = 3 passed, 1 failed
artifact ID           = 10300236909
artifact digest       = sha256:a688992b67de054f94dd5c7a7f13587285f36fc9c904c684ead11c1490302904
execution UTC         = 2026-09-12T14:48:48Z
```

The workflow records benchmark raw hashes, byte counts, pytest output and execution identity even on failure.

---

# 5. ACN gate

```text
workflow run ID      = 34698786730
state                = BLOCKED_EXTERNAL_CREDENTIAL
missing prerequisite = repository Actions secret ACN_API_TOKEN
API request          = not executed
raw ACN SHA256       = unresolved
```

No replacement data source was introduced.

---

# 6. Noncompensability

The environment and synthetic fixtures cannot compensate for failure of numerical convergence or missing complete data identity:

```math
G_{ENV}=1
\not\Rightarrow
G_V=1.
```

Likewise

```math
G_{V7}=1
\quad\text{but}\quad
G_{V5}=0
\Rightarrow
G_V=0.
```

---

# 7. Validation unlock condition

Validation becomes admissible only when

```math
\boxed{G_D=1\land G_V=1.}
```

At present:

```math
G_{ENV}=1,
\qquad
G_D=0,
\qquad
G_V=0.
```

Therefore

```text
calibration/holdout validation = BLOCKED
H1 confirmatory execution      = BLOCKED
H2 confirmatory execution      = BLOCKED
Stage-5 viability/resilience   = BLOCKED
```

---

# 8. Reopening rule

A failed or blocked gate may be reevaluated only after version-controlled evidence addresses its cause. Existing PASS evidence may be reused only where the relevant code/data dependency has not changed.

Permitted next work:

```text
1. diagnose/correct the traffic solver while preserving the frozen Beckmann problem,
   RG threshold, OD matrix, BPR parameters and max_iter criterion;
2. configure ACN_API_TOKEN externally;
3. execute and hash the frozen ACN request/processing chain;
4. rerun every mandatory verification test affected by those changes.
```

No acceptance criterion may be weakened merely because its first execution failed.
