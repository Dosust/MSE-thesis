# Phase 1C — Canonical Execution Identity v1

![Status](https://img.shields.io/badge/status-STRENGTHENED%20ENVIRONMENT%20IDENTITY%20FROZEN-1A7F37)
![Phase](https://img.shields.io/badge/phase-1C-0969DA)

**Frozen:** 2026-09-12  
**Superseding environment-evidence run:** GitHub Actions `34698765300`  
**Authority:** `PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md` + committed hash-lock + successful strengthened environment workflow  
**Boundary:** computational reproducibility/environment verification only; not full model verification, empirical validation, or H1/H2 evidence.

---

## 0. Governing method

```math
\boxed{
\text{LEARN}\rightarrow\text{VERIFY}\rightarrow\text{FORMULATE}\rightarrow\text{DERIVE}
\rightarrow\text{TEST}\rightarrow\text{VALIDATE}\rightarrow\text{SYNTHESIZE}\rightarrow\text{ADVANCE}
}
```

```math
\boxed{
\text{GENERAL EVIDENCE}\rightarrow\text{SCOPE MATCH}\rightarrow\text{THESIS APPLICATION}
\rightarrow\text{WHY}\rightarrow\text{CRITICAL TEST}
}
```

The earlier successful run `34697585840` remains provenance evidence, but run `34698765300` is authoritative because it adds the previously missing SALib and frozen-upstream ACN Portal execution checks without weakening any previous gate.

---

# 1. Canonical successful run `[E]`

```text
workflow            = Phase 1 environment lock and verification smoke
workflow path       = .github/workflows/phase1-environment-lock.yml
run ID              = 34698765300
run number          = 3
head/code SHA       = b8d47d6baa9e0cde51c5dd4d0e41be92e0445d7a
status/conclusion   = completed / success
started UTC         = 2026-09-12T14:15:40Z
completed UTC       = 2026-09-12T14:18:03Z
artifact ID         = 10299955441
artifact digest     = sha256:2d138f3423e108725893b810260ce1aba17b7a67febb8054b0d28961e318dc7d
```

---

# 2. Frozen execution identity

```math
\mathcal R_0
=
(H_{code},H_{lock},H_{env},H_D,ID_{run},t_{run}).
```

```text
H_code = b8d47d6baa9e0cde51c5dd4d0e41be92e0445d7a
H_lock = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env  = sha256:88a673b827ebaaade2556338e38203b87268a6819c9ea017fcf848829bafd0e3
H_D    = PENDING_ACN_AUTHENTICATED_ACQUISITION
ID_run = 34698765300
t_run  = 2026-09-12T14:15:40Z
```

Auxiliary evidence:

```text
OCI archive SHA-256 = 7001ee62793dfbc604d6c09df8a6957993a2cd1846852bdcf929e8d0e0af94e9
```

The exact resolved dependency lockfile is now permanently committed in the thesis repository as `project/requirements-phase1-v1.lock.txt`; a one-time resolver workflow reproduced the expected lock hash and committed it at `9322a451cba1118c27b6d821c4b718fd4a05ad20`.

---

# 3. Runtime identity `[E]`

```text
Python                  = 3.11.16 (GCC 13.3.0)
runtime platform        = Linux x86_64 / Ubuntu 24.04 runner family
float width             = 64 bit
NumPy float64 width     = 64 bit
PYTHONHASHSEED          = 0
OMP_NUM_THREADS         = 1
OPENBLAS_NUM_THREADS    = 1
MKL_NUM_THREADS         = 1
NUMEXPR_NUM_THREADS     = 1
```

Deterministic sub-seed evidence:

```text
scenario-A        = 17146681787701098982
scenario-A repeat = 17146681787701098982
scenario-B        = 15573457804683794101
```

---

# 4. Dependency identity `[E]`

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

The complete hash-locked file, not this descriptive subset, is authoritative.

---

# 5. Strengthened environment evidence `[E]`

The run executed and passed:

```text
canonical hash-lock verification/install  = PASS
package import smoke                       = PASS
SALib Morris smoke                         = PASS
SALib Sobol smoke                          = PASS
ACN Portal frozen-upstream test suite      = 95 passed, 1 deprecation warning
Phase-1 verification fixture suite (host) = 20 passed
Phase-1 verification fixture suite (OCI)  = 20 passed
legacy architecture fixture                = PASS
OCI linux/amd64 build/export               = PASS
credential-hygiene scan                    = PASS
```

Frozen upstream ACN Portal source used for the package-behavior check:

```text
repository = zach401/acnportal
commit     = 14e723b11339e56ca3afd2bf4969f9e4bc8c2623
package    = acnportal 0.3.3
```

The single upstream deprecation warning concerns `pkg_resources`; it did not cause test failure and is retained as software-technical evidence rather than suppressed.

---

# 6. Environment gate

Define

```math
G_{ENV}
=
G_{lock}G_{install}G_{import}G_{SALib}G_{ACNlib}G_{fixture}G_{container}G_{identity}G_{secret}.
```

All terms were executed successfully in canonical run `34698765300`; therefore

```math
\boxed{G_{ENV}=1.}
```

Scope of this conclusion:

> the declared Phase-1 computational environment is internally executable under its frozen dependency identity, including the required uncertainty-analysis APIs and the frozen ACN Portal package test suite.

This does **not** imply that the empirical ACN dataset has been acquired or that the full infrastructure model has been verified.

---

# 7. Data gate remains open `[U]`

The authenticated ACN acquisition workflow subsequently executed under the canonical lock but stopped at its deliberate credential-presence gate because repository secret `ACN_API_TOKEN` is absent.

Therefore

```text
H_D = PENDING_ACN_AUTHENTICATED_ACQUISITION
```

and

```math
\mathcal R^*=(H_{code},H_{lock},H_{env},H_D)
```

is still incomplete.

---

# 8. Scientific boundary

```math
\boxed{
G_{ENV}=1
\not\Rightarrow
G_D=1
\not\Rightarrow
G_V=1
\not\Rightarrow
V_{empirical}=1
\not\Rightarrow
(H_1,H_2)\text{ supported}.
}
```

Allowed claim:

> The Phase-1 software environment, dependency resolution, required package behaviors, deterministic fixtures, and canonical container execution have passed their bounded reproducibility gate.

Not yet allowed:

```text
full model verification;
ACN data validity;
calibration/holdout validation;
H1/H2 conclusions;
resilience/viability conclusions.
```

---

# 9. Next hard gate

```math
\boxed{
\text{configure ACN_API_TOKEN externally}
\rightarrow
\text{rerun frozen acquisition}
\rightarrow
H_D
\rightarrow
\mathcal R^*
\rightarrow
\text{ACN-dependent/full verification}.
}
```
