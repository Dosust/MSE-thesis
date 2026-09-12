# Phase 1C — Verification Execution Results v1

![Status](https://img.shields.io/badge/status-PUBLIC%20P%2FT%20VERIFICATION%20PASS-1A7F37)
![Phase](https://img.shields.io/badge/phase-1C-0969DA)

**Executed/updated:** 2026-09-12  
**Purpose:** record what was actually run under the frozen Phase-1 verification design, including failure history, audited numerical repair, current PASS evidence, unresolved ACN blocker, and the exact boundary of permissible claims.  
**Authority:** `PHASE1_VERIFICATION_TEST_MATRIX_V1.md`, `PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md`, `PHASE1_CANONICAL_EXECUTION_IDENTITY_V1.md`, `PHASE1_NUMERICAL_SOLVER_AMENDMENT_V1.md`.  
**Rule:** verification failures remain in the audit trail; acceptance thresholds are not weakened after results are observed.

---

# 0. Method

```math
\boxed{
\text{LEARN}\rightarrow\text{VERIFY}\rightarrow\text{FORMULATE}\rightarrow\text{DERIVE}
\rightarrow\text{TEST}\rightarrow\text{VALIDATE}\rightarrow\text{SYNTHESIZE}\rightarrow\text{ADVANCE}
}
```

Operational chain:

```math
\boxed{
\text{frozen inputs}\rightarrow\text{immutable environment}\rightarrow
\text{unit/limit tests}\rightarrow\text{benchmark reproduction}\rightarrow
\text{numerical convergence}\rightarrow G_V.
}
```

No calibration, validation, H1/H2 or Stage-5 viability analysis is admitted unless the mandatory verification gate closes.

---

# 1. Canonical computational environment `[E]`

Latest successful environment execution on the exact BFW benchmark head:

```text
workflow run ID   = 34700750356
job ID            = 103571958645
code SHA          = d6d97c7353f6d5694dba73ab840ae3a2548dd593
conclusion        = SUCCESS
Python            = 3.11.16
H_lock            = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env             = sha256:ee7469b8ec78c8bf9988fd1c33a7b85de6a49a636ade3337981c56944def50af
Docker image ID   = sha256:9790b75c9857d473f60402a2b79192e085d559f7caa8369df8ec078f83d7b657
OCI tar SHA256    = c13061011790320ef987578b91edb462cf7cff5c18b2fc4cb4c767060726d80c
```

Executed environment evidence:

```text
hash-locked install                  PASS
required imports                     PASS
SALib Morris/Sobol smoke             PASS
ACN Portal frozen-upstream tests     95 passed, 1 warning
Phase-1 fixtures on host             22 passed
Phase-1 fixtures in OCI              22 passed
legacy architecture fixture          5 passed
OCI linux/amd64 build/export         PASS
credential hygiene                   PASS
```

Therefore

```math
\boxed{G_{ENV}=1.}
```

Boundary: `G_ENV=1` establishes executable environment consistency only.

---

# 2. Immutable public benchmark acquisition `[E]`

Canonical benchmark run `34700750330` verified upstream Git blob identities before hashing local materializations.

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

Public power/transport raw provenance is closed. ACN provenance is not.

---

# 3. Canonical immutable benchmark execution `[E]`

```text
workflow             = Phase 1 immutable benchmark verification
run ID               = 34700750330
job ID               = 103571958582
head/code SHA        = d6d97c7353f6d5694dba73ab840ae3a2548dd593
started UTC          = 2026-09-12T14:56:53Z
completed UTC        = 2026-09-12T14:57:36Z
workflow conclusion  = SUCCESS
benchmark tests      = 4 passed in 3.79 s
Phase-1 fixtures     = 22 passed in 0.08 s
artifact ID          = 10300177541
artifact ZIP SHA256  = 3a87c5ec991e2addf7dde8d0ba896ce0d507a8aecfccba4b44b4c8ff4ef0c73f
report SHA256        = 4f2b27af34459c7b4022813a58ed93c457eb2430cea660f88f5f5877b81f6a35
```

The report was generated twice and required byte-for-byte equality before acceptance.

---

# 4. Power benchmark results `[E]`

```text
active branches                      = 32
base kV                              = 12.66
base MVA                             = 10.0
solver iterations                    = 11
max balance residual                 = 3.0808688933348094e-14
minimum voltage                      = 0.9130904793611044 pu
bus-24 base voltage                  = 0.9726811009691813 pu
bus-24 voltage after +0.1 MW         = 0.9714126540936994 pu
branch 23-24 base current            = 0.09581473734223377 pu
branch 23-24 current after +0.1 MW   = 0.10532607030491578 pu
```

Thus the frozen positive-load sign test passes:

```math
\Delta P_{24}>0
\Rightarrow
|V_{24}|\downarrow,
\quad
|I_{23,24}|\uparrow.
```

---

# 5. Transportation convergence history and final result `[E]`

Earlier executions correctly remained FAIL:

```text
initial full immutable RG = 0.1696116807192524
corrected CFW RG          = 4.215612504228978e-06
frozen criterion          = RG <= 1e-6 by max_iter=5000
```

A versioned BFW numerical amendment was then introduced while preserving the frozen mathematical problem and acceptance criterion. See `PHASE1_NUMERICAL_SOLVER_AMENDMENT_V1.md`.

Canonical BFW result:

```text
solver                        = biconjugate-frank-wolfe
iterations                    = 645
relative gap                  = 9.33748496131895e-07
max node balance residual     = 6.184563972055912e-11
scaled node balance residual  = 1.715075976720996e-16
```

Therefore

```math
\boxed{V\text{-}T02=\mathrm{PASS}}
```

because

```math
9.33748496131895\times10^{-7}<10^{-6}
\quad\land\quad
645<5000.
```

The threshold and iteration cap were not relaxed.

---

# 6. Transportation access-limit result `[E]`

At the accepted equilibrium link costs:

```text
crew base cost   = 25.92894954231427
crew closed cost = 27.61418250234074
```

The frozen closure removes `(9,10)` and `(10,9)`, producing

```math
T_{crew}^{closed}>T_{crew}^{base}.
```

The reopen test returns the original shortest-path cost/path in the same fixed-cost state. Therefore the declared road-access limit behavior passes inside this benchmark configuration.

---

# 7. ACN execution state `[E/U]`

The frozen authenticated ACN workflow previously reached its deliberate credential gate and stopped because repository secret `ACN_API_TOKEN` was absent.

```text
workflow run ID = 34698786730
credential gate = BLOCKED_EXTERNAL_CREDENTIAL
API acquisition = SKIPPED
raw ACN hash    = UNRESOLVED
```

No ACN observation was opened, substituted, altered, or used for tuning.

Thus the complete Phase-1 data gate remains open:

```math
\boxed{G_D=0.}
```

---

# 8. Nine-gate verification assessment

The nine-gate summary is noncompensable.

| Gate | Current state | Evidence |
|---|---|---|
| `G_V1` equations/algorithms implemented as specified | `PARTIAL-PASS` | 22/22 frozen fixtures + public P/T benchmark suite pass; ACN/coupled data path pending |
| `G_V2` units/dimensions | `PARTIAL-PASS` | power and transport schema/unit conversions pass; ACN path pending |
| `G_V3` conservation/balance | `PUBLIC P/T PASS` | power residual `3.08e-14`; traffic scaled node residual `1.72e-16` |
| `G_V4` limiting cases | `PARTIAL-PASS` | synthetic dependency limits and road-closure/reopen checks pass; ACN-dependent limits pending |
| `G_V5` numerical convergence/stability | `PUBLIC P/T PASS` | BFW `RG=9.337e-7` in 645 iterations; power solver converges in 11 iterations |
| `G_V6` irrelevant implementation invariance | `PARTIAL-PASS` | report generated twice byte-identically; broader ACN/full-model invariance pending |
| `G_V7` synthetic known-answer recovery | `PASS within implemented fixture domain` | 22 host + 22 OCI fixtures pass |
| `G_V8` sensitivity/parameter coherence | `NOT FULLY EXECUTED` | UQ library smoke passes; scientific parameter-coherence tests wait for full data/model closure |
| `G_V9` full reproducibility from complete `R*` | `BLOCKED` | ACN `H_D` unresolved |

Define

```math
G_V=1
\iff
\forall k\in\{1,\ldots,9\},\;G_{Vk}=1.
```

The prior transport-convergence failure is now closed, but because ACN-dependent/full-coupled gates remain unresolved,

```math
\boxed{G_V=0\;\text{(closure false, not scientific falsification)}.}
```

---

# 9. Why validation and H1/H2 remain blocked

The evidence hierarchy requires

```math
G_{ENV}=1\land G_D=1\land G_V=1
```

before calibration/holdout validation is admissible.

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
G_{VAL}=\mathrm{BLOCKED},
\qquad
G_{H1}=\mathrm{BLOCKED},
\qquad
G_{H2}=\mathrm{BLOCKED}.
}
```

No confirmatory hypothesis result has been produced.

---

# 10. Exact next allowed work

The previous transportation numerical blocker is closed. The active hard path is now:

```math
\boxed{
\text{configure ACN_API_TOKEN externally}
\rightarrow
\text{execute frozen ACN acquisition}
\rightarrow
\text{freeze raw/processed/split hashes}
\rightarrow
\text{execute remaining ACN-dependent/full coupled verification}
\rightarrow
G_V.
}
```

The token must never be committed or pasted into chat. If the credential is unavailable, the scientifically correct state is `BLOCKED_EXTERNAL_CREDENTIAL`; no substitute dataset is authorized inside v1.
