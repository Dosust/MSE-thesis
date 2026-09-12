# Phase 1B — Software Environment Lock v1

![Status](https://img.shields.io/badge/status-SOFTWARE%20TARGET%20LOCK%20v1.0-0969DA)
![Phase](https://img.shields.io/badge/phase-1B-1A7F37)

**Frozen:** 2026-09-12  
**Authority:** `PHASE1_EXPERIMENT_SPECIFICATION_V1.md` + `PHASE1_DATA_MANIFEST_V1.md` + `PHASE1_PARAMETER_REGISTER_V1.md`  
**Purpose:** freeze the computational context in which Phase-1 verification, calibration, validation and H1/H2 comparisons are permitted to run.  
**Important status:** the *target* environment is frozen here, but confirmatory execution remains blocked until the resolved dependency lockfile, OCI image digest, ACN raw-data hashes and executable code SHA exist and pass the smoke/verification gates below.

---

## 0. Method

The software decision uses the thesis evidence translation rule:

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
\text{TEST}.
}
```

Claim tags:

```text
[E] external software/standard fact;
[P] preregistered thesis choice;
[D] derived rationale;
[A] explicit assumption;
[U] unresolved item that blocks execution.
```

NASA-STD-7009B treats software/model implementation, verification, validation, uncertainty and acceptance criteria as model-credibility concerns. ASME VVUQ terminology likewise separates verification of the mathematical/computational implementation from validation of the real-world representation. These standards do not prescribe Python or any package version; the package choices below are thesis-specific reproducibility decisions.

---

# 1. Reproducibility object

A Phase-1 run is identified by

```math
\mathcal R_{run}
=
(
H_D,
H_\Theta,
H_{env},
H_{lock},
H_{code},
H_{seed},
ID_{scenario}
),
```

where

```text
H_D       = hashes/immutable identities from PHASE1_DATA_MANIFEST_V1;
H_Theta   = parameter-register version/commit;
H_env     = OCI image digest;
H_lock    = resolved package-lock SHA-256;
H_code    = executable-model Git commit SHA;
H_seed    = seed-manifest SHA-256;
IDscenario= immutable experiment/scenario identifier.
```

Reproducibility requires

```math
\boxed{
\mathcal R_{run}^{(1)}=\mathcal R_{run}^{(2)}
\Rightarrow
Z^{(1)}\approx Z^{(2)}
}
```

under the numerical tolerances declared in `PHASE1_VERIFICATION_TEST_MATRIX_V1.md`.

This is a bounded computational reproducibility claim. It is not a claim that floating-point results are bit-identical across arbitrary hardware/software stacks.

---

# 2. Operating-system and container target

## 2.1 General evidence `[E]`

Containerization does not validate a scientific model, but it provides a practical way to isolate and record operating-system and library dependencies. NASA-STD-7009B requires traceability of model implementation and credibility products; ASME VVUQ 60.1 provides guidance for disciplined computational-software selection.

## 2.2 Thesis application `[P]`

Reference runtime:

```text
container family : Docker/OCI
base image tag   : python:3.11.16-slim-bookworm
architecture     : linux/amd64 for canonical reported runs
OS family        : Debian Bookworm slim
Python           : CPython 3.11.16
```

The canonical reported experiment uses `linux/amd64` even when development occurs on Apple Silicon. Native ARM runs may be used for development/verification comparison but are not the authority for confirmatory numbers unless a versioned amendment establishes cross-architecture equivalence.

### Why Python 3.11 `[D]`

ACN Portal 0.3.3 upstream CI explicitly tested Python 3.8, 3.9, 3.10 and 3.11. The package source itself declares version 0.3.3 and depends on NumPy, pandas, matplotlib, requests, pytz, typing-extensions and scikit-learn. Python 3.11 therefore lies inside the package's demonstrated upstream test matrix rather than relying on an untested newer interpreter.

### OCI digest rule `[U/P]`

The human-readable tag above is frozen now, but tags are mutable references. Before the first verification run, record the **full immutable OCI digest** returned by the registry/pull operation:

```text
python:3.11.16-slim-bookworm@sha256:<FULL_DIGEST>
```

Status until recorded:

```text
OCI_FULL_DIGEST = BLOCKING-PENDING
```

No confirmatory run may rely only on the mutable tag.

---

# 3. Direct package pins

The direct package set is frozen in `requirements-phase1-v1.in`.

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

## 3.1 ACN Portal `[E/D]`

`acnportal==0.3.3` is the frozen ACN-Sim/ACN-Data client version. Upstream commit

```text
14e723b11339e56ca3afd2bf4969f9e4bc8c2623
```

corresponds to the 0.3.3 version bump. The package's `setup.py` lists its direct dependencies but does not impose exact versions.

PyPI source-distribution SHA-256:

```text
a9ae36a7b79463a13684b9c570402e06d4619d1baded5f598bd3c0206e0da809
```

PyPI wheel SHA-256:

```text
3bda7c776a451f53c778fb3b92202ec1ebcb265c92b2116ab8eb20d62114315b
```

For the canonical build, the source distribution is preferred so the artifact hash and upstream source state can be audited explicitly.

## 3.2 SALib `[E/D]`

Use

```text
SALib==1.4.8
```

instead of the newer 1.5.2 in Phase 1 v1.

Reason: SALib 1.5.2 requires NumPy >=2.0, whereas SALib 1.4.8 requires NumPy >=1.20.3 and still contains Morris and Sobol methods required by the preregistered UQ sequence. Keeping SALib 1.4.8 allows a conservative NumPy-1.26 environment closer to the era of ACN Portal 0.3.3, reducing gratuitous compatibility change before scientific verification.

This is a software-risk decision `[P/D]`, not a claim that SALib 1.4.8 is scientifically superior.

SALib 1.4.8 wheel SHA-256:

```text
fef0f0637a97f1adca35a435e41274add6275ea42428f04d3e83deb720cc0234
```

---

# 4. Resolved dependency lock

Direct pins are not sufficient for full reproducibility because packages have transitive dependencies.

Before verification execution, resolve the environment **inside the frozen Python 3.11 container** and generate a hash-locked file, for example:

```text
requirements-phase1-v1.lock.txt
```

using a deterministic resolver (`pip-tools` or equivalent) with package hashes.

Required integrity record:

```math
H_{lock}=SHA256(\text{requirements-phase1-v1.lock.txt}).
```

Status:

```text
RESOLVED_LOCKFILE = BLOCKING-PENDING
LOCKFILE_SHA256    = BLOCKING-PENDING
```

If resolution changes any direct pin, `PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V2.md` is required. Direct pins may not be silently changed.

---

# 5. Numerical implementation choices

## 5.1 Floating point `[P]`

Canonical floating-point type:

```text
IEEE-754 binary64 / NumPy float64
```

No mixed float32/float64 execution is allowed in confirmatory code unless explicitly documented and verified.

## 5.2 Linear-algebra threading `[P]`

For canonical runs:

```text
OMP_NUM_THREADS=1
OPENBLAS_NUM_THREADS=1
MKL_NUM_THREADS=1
NUMEXPR_NUM_THREADS=1
```

Why: stochastic/thread scheduling and reduction order can create avoidable run-to-run floating-point differences. Single-thread numerical kernels trade speed for auditability in the bounded demonstrator.

## 5.3 Python hash determinism `[P]`

```text
PYTHONHASHSEED=0
```

Any code that depends on iteration order of unordered containers is a defect; this setting is an additional reproducibility safeguard, not a substitute for deterministic algorithms.

---

# 6. Random-number governance

The master seed is

```math
s_0=20260912.
```

Use NumPy's explicit generator API:

```text
numpy.random.Generator(numpy.random.PCG64(seed))
```

Never use unseeded global random state in confirmatory execution.

For each stochastic experiment object with immutable identifier `ID_k`, derive the sub-seed from

```math
s_k
=
\operatorname{uint64}
\left(
\operatorname{SHA256}(\text{"20260912|"}||ID_k)_{0:16}
\right).
```

This prevents accidental seed reuse caused by manually incrementing integers.

A generated

```text
PHASE1_SEED_MANIFEST_V1.csv
```

must list every stochastic run ID and derived seed before H1/H2 execution. Its SHA-256 becomes `H_seed`.

---

# 7. Solver ownership

## 7.1 Power model `[P]`

Phase 1 does **not** introduce a second external power-system library merely to solve the 33-bus branch-flow equations.

The canonical implementation will use thesis-owned deterministic Python functions for the declared radial branch-flow/DistFlow equations, with SciPy used only where a generic numerical routine is necessary.

The MATPOWER `case33bw` file remains the immutable **data benchmark**, not the runtime solver.

Why: separating benchmark data from solver implementation allows the verification matrix to test the actual equations used by the thesis and avoids hidden behavior from an additional power-flow software stack.

## 7.2 Transportation model `[P]`

The Sioux Falls user-equilibrium solver is thesis-owned Frank-Wolfe code using:

```text
NumPy/SciPy for numeric operations;
NetworkX for deterministic shortest-path graph operations.
```

No commercial solver is introduced.

## 7.3 Charging model `[E/P]`

ACN-Sim functionality is supplied through `acnportal==0.3.3`. The upstream package test suite must pass in the frozen container before ACN-derived outputs are admitted.

---

# 8. ACN credentials and secret handling

ACN-Data's API requires an access token. The token is a credential and must **never** be committed to Git, manifests, logs, notebooks, or output files.

Canonical injection mechanism:

```text
ACN_API_TOKEN=<secret environment variable>
```

The acquisition script must read the token only from the process environment.

It must log:

```text
API base URL;
site;
query interval;
timeseries flag;
record count;
HTTP/application completion state;
raw output SHA-256;
```

and must **not** log the token.

The token's absence is a legitimate execution blocker; it is not permission to substitute another dataset.

---

# 9. Time and timezone discipline

ACN API datetime fields are stored in UTC/GMT and the site record supplies its timezone. Phase-1 preprocessing must therefore:

```text
1. parse source timestamps as timezone-aware UTC;
2. convert to America/Los_Angeles for the frozen experiment window/day partition;
3. never use naive datetimes in persisted intermediate files;
4. serialize timestamps in ISO-8601 with explicit offset or Z.
```

Simulation time index for ACN aggregation is the 5-minute local-time grid declared in the experiment specification.

---

# 10. Code versioning

The executable code does not yet exist and therefore cannot honestly be assigned a code SHA.

Before any verification run:

```text
CODE_SHA = Git commit containing the exact executable implementation
```

and the working tree must be clean.

Status:

```text
EXECUTABLE_CODE_SHA = BLOCKING-PENDING
```

Uncommitted code may be used for development only; its output cannot enter thesis evidence.

---

# 11. Environment smoke gate

Before scientific verification, the frozen environment itself must pass:

```text
S-E01  build OCI image successfully;
S-E02  install resolved hash-locked dependencies;
S-E03  import every direct package;
S-E04  run upstream acnportal unit tests;
S-E05  run SALib Ishigami smoke example for Morris/Sobol availability;
S-E06  run NumPy/SciPy deterministic arithmetic smoke test twice;
S-E07  confirm float64, timezone and RNG configuration;
S-E08  record pip freeze, Python build string and OS release;
S-E09  compute H_env and H_lock;
S-E10  verify no secret appears in image history/logs/repository.
```

Any failure blocks Phase-1 model verification. Package substitution requires a versioned environment amendment.

---

# 12. Current execution status

```text
TARGET PYTHON/OS           LOCKED
DIRECT PACKAGE PINS        LOCKED
ACNPORTAL VERSION/SOURCE   LOCKED
SALIB VERSION              LOCKED
RNG POLICY                 LOCKED
FLOAT/THREAD POLICY        LOCKED
SECRET POLICY              LOCKED
FULL OCI DIGEST            BLOCKING-PENDING
RESOLVED HASH LOCKFILE     BLOCKING-PENDING
ACN API TOKEN              EXTERNAL-CREDENTIAL REQUIRED
ACN RAW/PROCESSED HASHES   BLOCKING-PENDING
EXECUTABLE CODE SHA        BLOCKING-PENDING
```

Therefore:

```math
\boxed{
\text{Phase-1B specification complete}
\neq
\text{execution authorized}.
}
```

The next allowed operation is environment construction + smoke testing + ACN acquisition, followed by the already-preregistered mathematical verification matrix.

---

# 13. References / evidence anchors

- NASA. (2024). **NASA-STD-7009B — Standard for Models and Simulations**.
- NASA. (2026). **NASA-HDBK-7009B — Implementation Guide for NASA-STD-7009B**.
- ASME. **VVUQ 1-2022 — Verification, Validation, and Uncertainty Quantification Terminology in Computational Modeling and Simulation**.
- ASME. (2025). **VVUQ 60.1 — Considerations and Questionnaire for Selecting Computational Physics Simulation Software**.
- ACN Portal 0.3.3 source, upstream commit `14e723b11339e56ca3afd2bf4969f9e4bc8c2623`.
- ACN Portal `setup.py`, which declares v0.3.3 and its direct package dependencies.
- ACN Portal CI workflow, which tests Python 3.8–3.11.
- PyPI `acnportal==0.3.3` release metadata and distribution hashes.
- PyPI `SALib==1.4.8` release metadata and requirements.
- Python Docker Official Image, `python:3.11.16-slim-bookworm`.
