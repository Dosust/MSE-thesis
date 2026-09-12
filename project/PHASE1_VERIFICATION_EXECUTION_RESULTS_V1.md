# Phase 1C — Verification Execution Results v1

![Status](https://img.shields.io/badge/status-VERIFICATION%20EXECUTED%20NOT%20CLOSED-D73A49)
![Phase](https://img.shields.io/badge/phase-1C-0969DA)

**Executed:** 2026-09-12  
**Purpose:** record what was actually run under the frozen Phase-1 verification design, including failures, corrections, unresolved blockers, and the exact boundary of permissible claims.  
**Authority:** `PHASE1_VERIFICATION_TEST_MATRIX_V1.md`, `PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md`, `PHASE1_DATA_PROVENANCE_REGISTER_V1.md`, `PHASE1_CANONICAL_EXECUTION_IDENTITY_V1.md`.  
**Rule:** a verification failure is preserved as evidence; thresholds are not weakened after results are observed.

---

# 0. Method

```math
\boxed{
\text{LEARN}\rightarrow\text{VERIFY}\rightarrow\text{FORMULATE}\rightarrow\text{DERIVE}
\rightarrow\text{TEST}\rightarrow\text{VALIDATE}\rightarrow\text{SYNTHESIZE}\rightarrow\text{ADVANCE}
}
```

For this execution stage the operational chain is

```math
\boxed{
\text{frozen inputs}
\rightarrow
\text{immutable environment}
\rightarrow
\text{unit/limit tests}
\rightarrow
\text{benchmark reproduction}
\rightarrow
\text{numerical convergence}
\rightarrow
G_V.
}
```

No calibration, validation, H1/H2 or Stage-5 viability analysis is admitted unless the mandatory verification gate closes.

---

# 1. Canonical computational environment `[E]`

Canonical environment run:

```text
workflow            = Phase 1 environment lock and verification smoke
run ID              = 34700099915
job ID              = 103570219520
executable code SHA = a11914a1e7d015d75209e32c84a2459114ba7f17
conclusion          = SUCCESS
Python              = 3.11.16
H_lock              = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env               = sha256:02dcd331815e060c6f9601c9de7cfc9b9d6aa5e487bae08c6c81520b0245a716
Docker image ID     = sha256:feab21248dbf3694ab8a4247c1bc416e08780f013041fd0b9a2fca56431c1b6b
OCI tar SHA256      = 230918f8be9e8a7b13ad8a2a40a300c47f44c048b3e96ba465ce7101aa159942
```

Executed evidence:

```text
hash-locked install                  PASS
required imports                     PASS
SALib Morris/Sobol smoke             PASS
ACN Portal frozen-upstream tests     PASS
Phase-1 fixtures on host             22 passed
Phase-1 fixtures in OCI              22 passed
container build/export               PASS
credential hygiene                   PASS
```

Therefore

```math
\boxed{G_{ENV}=1.}
```

Boundary: `G_ENV=1` establishes executable environment consistency only.

---

# 2. Immutable public benchmark acquisition `[E]`

The benchmark workflow acquired the exact frozen upstream objects and verified each against its preregistered Git blob identity before local hashing.

```text
case33bw.m
  upstream blob = 97e510bee25c543de0453959672fe86b40a999c8
  SHA256        = b40831eeb444669ae876e2996f0dda9f05cd83e81b314b8dfca51e4890cca95d
  bytes         = 4866

SiouxFalls_net.tntp
  upstream blob = 66d0eca4ddcfb82f861bea040060deab7a741b2f
  SHA256        = ace99b24cec69c273ff0cf3d6d074110177f0cc0ae24b0c7a9f4f4cb5e27635c
  bytes         = 3136

SiouxFalls_trips.tntp
  upstream blob = db70eda57738877811e9ac07c25a567973d3b6a0
  SHA256        = 56f9566857f3f66730fd5c4232258d7ee3ac2931a476526331afd062f4958de7
  bytes         = 10859
```

Thus public power/transport raw provenance is closed. ACN provenance is not.

---

# 3. Benchmark tests actually executed `[E]`

The immutable integration suite contains four tests:

1. `test_case33bw_source_schema_and_conversion`
2. `test_case33bw_full_radial_solution_balance_and_positive_load_sign`
3. `test_sioux_falls_source_schema_and_od_total`
4. `test_sioux_falls_full_user_equilibrium_conservation_and_closure_limit`

The first three passed on the immutable benchmark objects.

Therefore the following claims are supported inside the declared benchmark domain:

```text
MATPOWER source schema and unit conversion        PASS
33-bus radial power solution/balance              PASS
positive added load produces expected voltage/current direction PASS
Sioux Falls source schema                         PASS
Sioux Falls OD total = 360600                     PASS
Sioux Falls BPR alpha=0.15, beta=4               PASS
```

The fourth test failed at its preregistered convergence criterion and therefore its later conservation/closure assertions were not admitted as executed PASS evidence.

---

# 4. Transportation-solver failure history

## 4.1 First full immutable benchmark run

```text
workflow run ID = 34699942787
head SHA        = 8ef087f637858e836bda58bef3cece98e10d15d4
result          = 3 passed, 1 failed
failed object   = Sioux Falls full user equilibrium
RG observed     = 0.1696116807192524
criterion       = RG <= 1e-6 by max_iter=5000
verdict         = FAIL
```

This failure was interpreted as an implementation-verification failure, not as evidence against H1/H2.

## 4.2 Diagnosis `[E/D]`

The implementation was compared against the conjugate-direction Frank-Wolfe recurrence described by Mitradjieva & Lindberg (Transportation Science, 2013, DOI `10.1287/trsc.1120.0409`) and an independent public implementation in `UchidaMizuki/TrafficAssign.jl`.

That reference implementation explicitly forms the residual previous direction after line search as

```math
\bar d=(1-\tau_{k-1})d_{k-1}^{CFW}
```

and restarts with an ordinary Frank-Wolfe direction when the prior line step is effectively at the end of the feasible segment.

The Phase-1 Python implementation had not encoded that restart state explicitly. This was corrected without altering:

```text
Sioux Falls data;
BPR cost law;
Beckmann objective;
relative-gap definition;
preregistered gap threshold;
preregistered max iterations;
H1/H2 outcome definitions.
```

Correction commit:

```text
a11914a1e7d015d75209e32c84a2459114ba7f17
```

## 4.3 Rerun after implementation correction

```text
workflow run ID = 34700099913
code SHA        = a11914a1e7d015d75209e32c84a2459114ba7f17
result          = 3 passed, 1 failed
RG observed     = 4.215612504228978e-06
criterion       = RG <= 1e-6
max_iter        = 5000
verdict         = FAIL
```

The correction improved the residual gap by approximately four orders of magnitude, but the frozen criterion was still not met.

Formally,

```math
4.215612504228978\times10^{-6}>10^{-6}.
```

Therefore the test remains FAIL. The improvement is not converted into a PASS by post-hoc threshold relaxation.

---

# 5. Failure-evidence preservation `[D/P]`

The benchmark workflow was then strengthened so that execution identity and evidence artifacts are uploaded even when a mandatory verification test fails.

Workflow-change commit:

```text
df263eb254431fca3897e460b7d9483a29393414
```

Preserved-evidence run:

```text
workflow run ID = 34700331684
job ID          = 103570834519
workflow head   = df263eb254431fca3897e460b7d9483a29393414
executable code = unchanged from a11914a1e7d015d75209e32c84a2459114ba7f17
result          = 3 passed, 1 failed
RG observed     = 4.215612504228978e-06
artifact ID     = 10300236909
artifact digest = sha256:a688992b67de054f94dd5c7a7f13587285f36fc9c904c684ead11c1490302904
executed UTC    = 2026-09-12T14:48:48Z
```

The artifact contains the raw benchmark hashes/byte counts, pytest failure record and execution identity. This converts the failed test into retained reproducibility evidence rather than ephemeral CI output.

---

# 6. ACN execution result `[E/U]`

The frozen authenticated ACN workflow was executed separately:

```text
workflow run ID = 34698786730
head SHA        = c509d7de85627dda9f99023aa8acb5b24737cc9d
lock install    = PASS
credential gate = FAIL because ACN_API_TOKEN is absent
API acquisition = SKIPPED
raw ACN hash    = UNRESOLVED
```

This is classified as

```text
BLOCKED_EXTERNAL_CREDENTIAL
```

rather than data/model failure. No ACN observation was opened, inspected, altered or substituted.

Thus

```math
\boxed{G_D=0}
```

for the complete Phase-1 data gate because `G_ACNraw`, `G_ACNproc` and the chronological split are not closed.

---

# 7. Verification-gate assessment

The nine-gate summary is intentionally noncompensable.

| Gate | State | Evidence |
|---|---|---|
| `G_V1` equations/algorithms implemented as specified | `PARTIAL` | 22/22 frozen fixtures pass; power benchmark passes; full traffic solver criterion fails |
| `G_V2` units/dimensions | `PARTIAL-PASS` | frozen unit/schema conversion fixtures pass for implemented public benchmark components; ACN path unavailable |
| `G_V3` conservation/balance | `PARTIAL` | power balance passes; traffic accepted-solution conservation is downstream of failed convergence assertion |
| `G_V4` limiting cases | `PARTIAL-PASS` | synthetic dependency/limit fixtures pass; complete data-dependent limits not yet executable |
| `G_V5` numerical convergence/stability | **`FAIL`** | Sioux Falls `RG=4.215612504228978e-06 > 1e-6` at 5000 iterations |
| `G_V6` irrelevant implementation invariance | `PARTIAL` | deterministic fixture/environment evidence exists; full benchmark report step blocked by failed preceding test |
| `G_V7` synthetic known-answer recovery | `PASS within implemented fixture domain` | 22 host + 22 OCI verification fixtures pass |
| `G_V8` sensitivity/parameter coherence | `NOT EXECUTED` | not authorized before numerical verification/data closure |
| `G_V9` full reproducibility from complete `R*` | `BLOCKED` | ACN `H_D` unresolved |

Define the closure gate conservatively as

```math
G_V=1
\iff
\forall k\in\{1,\ldots,9\},\;G_{Vk}=1.
```

At present,

```math
\boxed{G_V=0.}
```

Here `0` means **verification closure is false**. It does not mean the scientific hypotheses have been falsified.

---

# 8. Why validation and H1/H2 were not run

The evidence hierarchy requires

```math
G_{ENV}=1
\land
G_D=1
\land
G_V=1
```

before calibration/holdout validation can become admissible.

Currently

```math
G_{ENV}=1,
\qquad
G_D=0,
\qquad
G_V=0.
```

Therefore

```math
\boxed{
G_{VAL}=0_{\text{BLOCKED}},
\qquad
G_{H1}=0_{\text{BLOCKED}},
\qquad
G_{H2}=0_{\text{BLOCKED}}.
}
```

No validation data were opened for result-driven tuning and no confirmatory H1/H2 result was produced.

---

# 9. Exact next allowed technical work

Two independent blockers remain.

## Blocker A — transportation convergence

Allowed:

```text
inspect the CFW numerical recurrence;
compare against an independent implementation/reference solution;
add diagnostic traces that do not change the frozen acceptance criterion;
correct a demonstrable implementation defect under version control;
rerun the entire verification suite after each correction.
```

Not allowed merely to manufacture a PASS:

```text
weaken RG tolerance after observing the result;
increase max_iter only because 5000 did not pass;
remove difficult OD pairs;
change BPR parameters;
replace Sioux Falls;
redefine the relative-gap metric post hoc.
```

If a different solver is introduced, it must solve the same frozen Beckmann/user-equilibrium problem and be treated as a versioned implementation amendment with independent cross-check evidence.

## Blocker B — ACN credential

The user must configure the authorized token externally as repository Actions secret:

```text
ACN_API_TOKEN
```

The token must never be committed or pasted into chat. After the secret exists, rerun the already-frozen acquisition workflow; accept `G_ACNraw=1` only if it records the raw SHA-256, byte count, record count, manifest hash, retrieval time and credential-hygiene PASS.

---

# 10. Current scientifically permissible conclusion

```math
\boxed{
\text{reproducible environment closed}
\land
\text{public benchmark provenance closed}
\land
\text{power benchmark verification passes}
\land
\text{transport numerical convergence does not yet pass}
\land
\text{ACN data gate remains credential-blocked}.
}
```

The correct scientific action is therefore to remain inside verification. Validation, H1/H2 and resilience/viability experiments remain blocked.
