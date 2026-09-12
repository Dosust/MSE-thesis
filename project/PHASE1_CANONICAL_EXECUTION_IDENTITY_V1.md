# Phase 1C — Canonical Execution Identity v1

![Status](https://img.shields.io/badge/status-ENVIRONMENT%20%2B%20PUBLIC%20P%2FT%20CLOSED-1A7F37)
![Phase](https://img.shields.io/badge/phase-1C-0969DA)

**Updated:** 2026-09-12  
**Canonical BFW benchmark run:** GitHub Actions `34700750330`  
**Canonical environment run:** GitHub Actions `34700750356`  
**Executable code SHA:** `d6d97c7353f6d5694dba73ab840ae3a2548dd593`  
**Boundary:** computational reproducibility plus public power/transport verification only; ACN-dependent full verification, empirical validation and H1/H2 remain blocked.

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

---

# 1. Canonical execution pair `[E]`

## 1.1 Environment identity

```text
workflow          = Phase 1 environment lock and verification smoke
run ID            = 34700750356
job ID            = 103571958645
head/code SHA     = d6d97c7353f6d5694dba73ab840ae3a2548dd593
conclusion        = SUCCESS
runner image      = Ubuntu 24.04.5 LTS / ubuntu-24.04 image 20260907.300.1
Python            = CPython 3.11.16
```

## 1.2 Public benchmark verification identity

```text
workflow          = Phase 1 immutable benchmark verification
run ID            = 34700750330
job ID            = 103571958582
head/code SHA     = d6d97c7353f6d5694dba73ab840ae3a2548dd593
conclusion        = SUCCESS
executed UTC      = 2026-09-12T14:57:33Z
artifact ID       = 10300177541
artifact digest   = sha256:3a87c5ec991e2addf7dde8d0ba896ce0d507a8aecfccba4b44b4c8ff4ef0c73f
```

---

# 2. Frozen execution identity

For the current executable state,

```math
\mathcal R_0=(H_{code},H_{lock},H_{env},H_D,ID_{run},t_{run}).
```

```text
H_code = d6d97c7353f6d5694dba73ab840ae3a2548dd593
H_lock = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env  = sha256:ee7469b8ec78c8bf9988fd1c33a7b85de6a49a636ade3337981c56944def50af
H_D    = PENDING_ACN_AUTHENTICATED_ACQUISITION
ID_run = 34700750330
T_run  = 2026-09-12T14:57:33Z benchmark report identity
```

Additional environment identities:

```text
Docker image ID      = sha256:9790b75c9857d473f60402a2b79192e085d559f7caa8369df8ec078f83d7b657
OCI descriptor       = sha256:ee7469b8ec78c8bf9988fd1c33a7b85de6a49a636ade3337981c56944def50af
OCI archive SHA-256  = c13061011790320ef987578b91edb462cf7cff5c18b2fc4cb4c767060726d80c
```

Because `H_D` for ACN is unresolved, the complete experiment identity

```math
\mathcal R^*=(H_{code},H_{lock},H_{env},H_D)
```

is not yet closed.

---

# 3. Runtime and dependency identity `[E]`

```text
Python                  = 3.11.16
architecture            = linux/amd64
float width             = 64 bit
PYTHONHASHSEED          = 0
OMP_NUM_THREADS         = 1
OPENBLAS_NUM_THREADS    = 1
MKL_NUM_THREADS         = 1
NUMEXPR_NUM_THREADS     = 1
```

Direct scientific/runtime package pins include:

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

The complete hash-locked dependency file `project/requirements-phase1-v1.lock.txt` is authoritative.

---

# 4. Environment closure `[E]`

Environment run `34700750356` passed:

```text
hash-lock verification/install       PASS
required imports                     PASS
SALib Morris/Sobol smoke             PASS
ACN Portal upstream suite            95 passed, 1 warning
Phase-1 host fixtures                22 passed
Phase-1 OCI fixtures                 22 passed
legacy architecture fixtures         5 passed
OCI build/export                     PASS
credential-hygiene scan              PASS
```

Therefore

```math
\boxed{G_{ENV}=1.}
```

This establishes environment executability only.

---

# 5. Public benchmark materialization `[E]`

```text
MATPOWER case33bw.m
  upstream commit = 2e0ef79a6c4526858ee923491d92781ad4507fb7
  Git blob        = 97e510bee25c543de0453959672fe86b40a999c8
  SHA256          = b40831eeb444669ae876e2996f0dda9f05cd83e81b314b8dfca51e4890cca95d
  bytes           = 4866

SiouxFalls_net.tntp
  upstream commit = d1639b4ef218c17928ba573e806ddf8ba5e7ae6d
  Git blob        = 66d0eca4ddcfb82f861bea040060deab7a741b2f
  SHA256          = ace99b24cec69c273ff0cf3d6d074110177f0cc0ae24b0c7a9f4f4cb5e27635c
  bytes           = 3136

SiouxFalls_trips.tntp
  upstream commit = d1639b4ef218c17928ba573e806ddf8ba5e7ae6d
  Git blob        = db70eda57738877811e9ac07c25a567973d3b6a0
  SHA256          = 56f9566857f3f66730fd5c4232258d7ee3ac2931a476526331afd062f4958de7
  bytes           = 10859
```

These close local public P/T data identity only.

---

# 6. Public benchmark verification identity `[E]`

Canonical report:

```text
report SHA256 = 4f2b27af34459c7b4022813a58ed93c457eb2430cea660f88f5f5877b81f6a35
```

Power:

```text
max balance residual = 3.0808688933348094e-14
solver iterations    = 11
```

Transportation:

```text
solver                = biconjugate-frank-wolfe
iterations            = 645
relative gap          = 9.33748496131895e-07
scaled node residual  = 1.715075976720996e-16
```

The frozen transport criterion was

```math
RG\le10^{-6},\qquad N_{it}\le5000,
```

therefore the public transport convergence blocker is closed.

---

# 7. ACN data gate remains open `[U]`

The authenticated ACN workflow previously stopped at the credential-presence gate because GitHub Actions secret `ACN_API_TOKEN` was absent. No ACN record was requested or transformed.

```text
H_D = PENDING_ACN_AUTHENTICATED_ACQUISITION
```

The token must be configured externally as a repository secret and must never be committed or pasted into chat.

---

# 8. Verification status is distinct from public benchmark success

The public P/T benchmark now passes its implemented numerical and conservation checks, but the complete Phase-1 verification gate includes ACN-dependent/full-coupled requirements. Therefore

```math
\boxed{
G_{ENV}=1,
\qquad
G_D=0,
\qquad
G_V=0\text{ (closure not yet complete)}.
}
```

`G_V=0` here means only that the noncompensable complete verification closure condition is false; it is not evidence against H1 or H2.

---

# 9. Scientific boundary

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

Not yet allowed:

```text
calibration/holdout validation;
H1/H2 conclusions;
full coupled-model validity claims;
Stage-5 resilience/viability conclusions.
```

---

# 10. Next hard gate

```math
\boxed{
\text{ACN_API_TOKEN configured externally}
\rightarrow
\text{frozen ACN acquisition}
\rightarrow
\text{raw/processed/split hashes}
\rightarrow
\text{remaining full verification}
\rightarrow G_V.
}
```

No substitute ACN dataset or weakened verification criterion is authorized inside Phase-1 v1.
