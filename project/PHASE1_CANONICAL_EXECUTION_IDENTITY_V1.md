# Phase 1C — Canonical Execution Identity v1

![Status](https://img.shields.io/badge/status-ENVIRONMENT%20IDENTITY%20FROZEN-1A7F37)
![Phase](https://img.shields.io/badge/phase-1C-0969DA)

**Frozen:** 2026-09-12  
**Authority:** `PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md` + GitHub Actions run `34697585840`  
**Purpose:** freeze the exact software/code/environment identity produced by the first successful canonical Phase-1 environment-lock run.  
**Boundary:** this document establishes computational reproducibility evidence only. It does **not** establish full model verification, empirical validation, or support for H1/H2.

---

## 0. Thesis method

```math
\boxed{
\text{LEARN}
\rightarrow
\text{VERIFY}
\rightarrow
\text{FORMULATE}
\rightarrow
\text{DERIVE}
\rightarrow
\text{TEST}
\rightarrow
\text{VALIDATE}
\rightarrow
\text{SYNTHESIZE}
\rightarrow
\text{ADVANCE}
}
```

Evidence translation rule:

```math
\boxed{
\text{GENERAL EVIDENCE}
\rightarrow
\text{SCOPE MATCH}
\rightarrow
\text{THESIS APPLICATION}
\rightarrow
\text{WHY}
\rightarrow
\text{CRITICAL TEST}
}
```

Claim tags:

```text
[E] externally observed execution fact;
[P] preregistered thesis choice;
[D] result derived from frozen evidence;
[A] explicit assumption;
[U] unresolved blocker.
```

---

# 1. Successful canonical environment run `[E]`

GitHub Actions evidence:

```text
workflow name       = Phase 1 environment lock and verification smoke
workflow path       = .github/workflows/phase1-environment-lock.yml
workflow run ID     = 34697585840
workflow run number = 2
event                = push
branch               = main
status               = completed
conclusion           = success
run started UTC      = 2026-09-12T13:51:20Z
run updated UTC      = 2026-09-12T13:53:41Z
head/code SHA        = 59a0a71f7f90221a215e40389c0600e7ef3d52a5
```

Workflow evidence artifact:

```text
artifact ID          = 10299178011
artifact name        = phase1-environment-lock-59a0a71f7f90221a215e40389c0600e7ef3d52a5
artifact SHA-256     = 8bfefce5d766a08f6c4befa019ea7b43deabc46ff2de51da0d54391e1c323d77
artifact created UTC = 2026-09-12T13:53:32Z
```

The artifact is an evidence carrier; its retention policy is finite, so the cryptographic identities extracted below are the canonical permanent thesis record.

---

# 2. Frozen execution identity

The Phase-1 reproducibility identity is

```math
\mathcal R_0
=
\left(
H_{code},
H_{lock},
H_{env},
H_D,
ID_{run},
t_{run}
\right).
```

For v1:

```text
H_code = 59a0a71f7f90221a215e40389c0600e7ef3d52a5
H_lock = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env  = sha256:86fb03316014ff27c9141882f935e52b4a6bf2000ace0b46e2f0df74447b420f
H_D    = PENDING_ACN_AUTHENTICATED_ACQUISITION
ID_run = 34697585840
t_run  = 2026-09-12T13:51:20Z
```

Auxiliary immutable environment evidence:

```text
Docker local image ID = sha256:580030ae5ae2080c6b39ce16b36d78e691d547d0c7947a74e0389fdd72a9a066
OCI archive SHA-256   = 417805be3b4ade3e60e299e7d6d037d869c7060c3aaed38bb0229b98c73a2a0b
```

`H_env` is the OCI manifest descriptor emitted from the canonical `linux/amd64` OCI export. It is used as the environment identity rather than a mutable image tag.

---

# 3. Runtime facts `[E]`

The successful workflow recorded:

```text
Python = 3.11.16 (GCC 13.3.0)
runner OS = Ubuntu 24.04.5 LTS
runner architecture = x86_64
IEEE-754 double width = 64 bit
NumPy float64 width = 64 bit
PYTHONHASHSEED = 0
OMP_NUM_THREADS = 1
OPENBLAS_NUM_THREADS = 1
MKL_NUM_THREADS = 1
NUMEXPR_NUM_THREADS = 1
```

Deterministic seed fixture:

```text
scenario-A        -> 17146681787701098982
scenario-A repeat -> 17146681787701098982
scenario-B        -> 15573457804683794101
```

This satisfies the intended deterministic sub-seed rule for the tested fixtures.

---

# 4. Resolved dependency evidence `[E]`

The successful resolver produced a hash-locked dependency file with

```text
requirements-phase1-v1.lock.txt
SHA-256 = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
```

Selected resolved versions include:

```text
acnportal==0.3.3
SALib==1.4.8
numpy==1.26.4
scipy==1.11.4
pandas==2.1.4
networkx==3.2.1
matplotlib==3.8.2
scikit-learn==1.3.2
requests==2.31.0
pytz==2024.1
pytest==8.2.2
```

The complete generated lockfile is the authority; this list is descriptive only.

---

# 5. Verification-only fixture result `[E]`

The canonical workflow executed the current Phase-1 verification fixture suite both on the GitHub runner and inside the canonical `linux/amd64` container:

```text
host fixture result      = 20 passed
container fixture result = 20 passed
```

These results show that the implemented verification fixtures execute consistently in both contexts.

They do **not** establish that every test in `PHASE1_VERIFICATION_TEST_MATRIX_V1.md` has been executed. In particular, authenticated ACN data checks and the complete nine-gate verification closure remain pending.

---

# 6. Environment gate decomposition

For Phase 1C, define

```math
G_{ENV}
=
G_{build}
G_{install}
G_{import}
G_{fixture}
G_{container}
G_{identity}
G_{secret}.
```

Evidence from run `34697585840` establishes:

| Sub-gate | Result | Evidence |
|---|---:|---|
| `G_build` | 1 | OCI/Docker build step completed |
| `G_install` | 1 | resolved lock/install step completed |
| `G_import` | 1 | direct-package import smoke completed |
| `G_fixture` | 1 | 20 Phase-1 fixtures passed on runner |
| `G_container` | 1 | 20 Phase-1 fixtures passed in linux/amd64 container |
| `G_identity` | 1 | code/lock/OCI identities recorded |
| `G_secret` | 1 | tracked-file literal-token hygiene check passed |

Therefore for this **bounded environment gate**:

```math
\boxed{G_{ENV}=1.}
```

This definition is intentionally narrower than the full model-verification gate `G_V`. Any additional package-specific or model-specific test remains part of verification and cannot be inferred from `G_ENV=1`.

---

# 7. Data hash remains unresolved `[U]`

The environment run did not have an authorized ACN extraction. Therefore

```text
H_D = PENDING_ACN_AUTHENTICATED_ACQUISITION
```

and the fully specified run identity

```math
\mathcal R^*=(H_{code},H_{lock},H_{env},H_D)
```

cannot yet be closed.

This is the next hard gate.

---

# 8. Scientific interpretation

Correct implications:

```math
\boxed{
G_{ENV}=1
\not\Rightarrow
G_V=1
\not\Rightarrow
V_{empirical}=1
\not\Rightarrow
(H_1,H_2)\text{ supported}.
}
```

The present evidence supports only:

> The declared Phase-1 software environment can be reconstructed and can execute the current verification-only fixture suite under an immutable code/lock/environment identity.

It does not support:

```text
- empirical validity of the P–T demonstrator;
- correctness of every declared mathematical mechanism;
- identifiability of all parameters;
- predictive superiority of dynamic coupling;
- resilience/viability conclusions;
- support for H1 or H2.
```

---

# 9. Next allowed operation

```math
\boxed{
\text{ACN authenticated acquisition}
\rightarrow
H_D
\rightarrow
\mathcal R^*
\rightarrow
\text{full verification execution}.
}
```

Until `H_D` is frozen, validation and confirmatory H1/H2 execution remain blocked.
