# Phase 1B/1C — Software Environment Lock v1

![Status](https://img.shields.io/badge/status-G_ENV%3D1-1A7F37)
![Phase](https://img.shields.io/badge/phase-1B%2F1C-0969DA)

**Target frozen:** 2026-09-12  
**Execution closure refreshed:** 2026-09-12  
**Purpose:** freeze and verify the computational context in which Phase-1 verification is permitted to run.  
**Boundary:** `G_ENV=1` means the declared environment is reproducibly executable. It does not mean the complete infrastructure model has passed verification, empirical validation, or H1/H2.

---

## 0. Claim discipline

```math
\boxed{
\text{GENERAL EVIDENCE}\rightarrow\text{SCOPE MATCH}\rightarrow\text{THESIS APPLICATION}
\rightarrow\text{WHY}\rightarrow\text{TEST}
}
```

Claim tags: `[E]` external/executed fact, `[P]` preregistered thesis choice, `[D]` derived rationale, `[A]` explicit assumption, `[U]` unresolved.

---

# 1. Reproducibility object

```math
\mathcal R_{run}=(H_D,H_\Theta,H_{env},H_{lock},H_{code},H_{seed},ID_{scenario}).
```

Current canonical executable environment:

```text
H_code = d6d97c7353f6d5694dba73ab840ae3a2548dd593
H_lock = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env  = sha256:ee7469b8ec78c8bf9988fd1c33a7b85de6a49a636ade3337981c56944def50af
H_D    = PENDING_ACN_AUTHENTICATED_ACQUISITION
```

`H_D` remains unresolved because authenticated ACN acquisition has not succeeded.

---

# 2. Canonical runtime `[P/E]`

```text
container family = Docker / OCI
base image       = python:3.11.16-slim-bookworm
base digest      = sha256:528257d48c1da0dcecc2e725d1ae34498d60c965f1241e39cd6a85a8859bdf84
canonical arch   = linux/amd64
Python           = CPython 3.11.16
floating point   = float64 / 64 bit
PYTHONHASHSEED   = 0
OMP threads      = 1
OpenBLAS threads = 1
MKL threads      = 1
NumExpr threads  = 1
```

The authoritative confirmatory architecture is linux/amd64 even when development occurs on another architecture.

---

# 3. Canonical dependency identity

The authoritative resolved dependency lock is

```text
project/requirements-phase1-v1.lock.txt
```

with

```text
LOCKFILE_SHA256 = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
```

Direct scientific/runtime pins include:

```text
numpy==1.26.4
scipy==1.11.4
pandas==2.1.4
networkx==3.2.1
matplotlib==3.8.2
scikit-learn==1.3.2
requests==2.31.0
pytz==2024.1
typing_extensions==4.9.0
acnportal==0.3.3
SALib==1.4.8
pytest==8.2.2
```

The lock is installed with pip `--require-hashes`; package ranges are not used for canonical runs.

---

# 4. Latest executed environment closure `[E]`

```text
workflow          = Phase 1 environment lock and verification smoke
run ID            = 34700750356
job ID            = 103571958645
head/code SHA     = d6d97c7353f6d5694dba73ab840ae3a2548dd593
started UTC       = 2026-09-12T14:56:55Z
completed UTC     = 2026-09-12T14:59:02Z
conclusion        = SUCCESS
runner            = Ubuntu 24.04.5 LTS / linux-amd64
```

Immutable container evidence:

```text
Docker image ID        = sha256:9790b75c9857d473f60402a2b79192e085d559f7caa8369df8ec078f83d7b657
OCI descriptor digest = sha256:ee7469b8ec78c8bf9988fd1c33a7b85de6a49a636ade3337981c56944def50af
OCI archive SHA-256    = c13061011790320ef987578b91edb462cf7cff5c18b2fc4cb4c767060726d80c
artifact ID            = 10300247744
artifact ZIP SHA-256   = a070ff3e3b9b9d62e4fd2957b8f6f97a7618346fff603f4bf27ca1de16817ae7
```

Executed checks:

```text
hash-lock identity/install                 PASS
required package imports                   PASS
SALib Morris + Sobol smoke                 PASS
ACN Portal frozen-upstream unit tests      95 passed, 1 warning
Phase-1 verification fixtures on host      22 passed
Phase-1 verification fixtures in OCI       22 passed
legacy architecture fixture                5 passed
linux/amd64 OCI build/export               PASS
credential hygiene                         PASS
```

The warning in the upstream ACN Portal suite is a deprecation warning concerning `pkg_resources`; no test failed.

---

# 5. Environment gate

Define

```math
G_{ENV}=G_{build}G_{install}G_{import}G_{unit}G_{smoke}G_{lock}G_{container}G_{identity}G_{secret}.
```

Every declared term above passed in run `34700750356`; therefore

```math
\boxed{G_{ENV}=1.}
```

Permitted claim:

> The Phase-1 software environment corresponding to executable code SHA `d6d97c7...` is reconstructible from the frozen hash-lock, passes the declared package/library/fixture smoke suite, and has an immutable linux/amd64 OCI identity.

Prohibited inference:

```math
G_{ENV}=1\not\Rightarrow G_V=1.
```

---

# 6. Public benchmark verification under this environment `[E]`

The exact same executable head `d6d97c7...` passed the immutable public benchmark workflow in run `34700750330`.

```text
benchmark tests             = 4 passed
Phase-1 fixture suite       = 22 passed
power residual max          = 3.0808688933348094e-14
transport solver            = biconjugate-frank-wolfe
transport iterations        = 645
transport relative gap      = 9.33748496131895e-07
transport scaled residual   = 1.715075976720996e-16
benchmark report SHA256     = 4f2b27af34459c7b4022813a58ed93c457eb2430cea660f88f5f5877b81f6a35
```

The public P/T numerical-convergence blocker is therefore closed without changing the frozen criterion.

---

# 7. ACN boundary `[U]`

Current ACN state:

```text
prior ACN workflow run = 34698786730
credential gate        = BLOCKED_EXTERNAL_CREDENTIAL
raw ACN SHA256         = UNRESOLVED
processed hashes       = UNRESOLVED
```

The repository secret must be named:

```text
ACN_API_TOKEN
```

The token must never be committed or pasted into chat.

---

# 8. Canonical scientific boundary

```math
\boxed{
G_{ENV}=1,
\qquad
G_D=0,
\qquad
G_V=0\text{ (complete closure not yet achieved)}.
}
```

Hence validation, H1/H2 and Stage-5 resilience/viability execution remain blocked until ACN provenance and the remaining full verification requirements close.
