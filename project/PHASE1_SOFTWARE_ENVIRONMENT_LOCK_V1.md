# Phase 1B/1C — Software Environment Lock v1

![Status](https://img.shields.io/badge/status-G_ENV%3D1-1A7F37)
![Phase](https://img.shields.io/badge/phase-1B%2F1C-0969DA)

**Target frozen:** 2026-09-12  
**Execution closure updated:** 2026-09-12  
**Authority:** `PHASE1_EXPERIMENT_SPECIFICATION_V1.md` + `PHASE1_DATA_MANIFEST_V1.md` + `PHASE1_PARAMETER_REGISTER_V1.md`  
**Purpose:** freeze and then verify the computational context in which Phase-1 verification is permitted to run.  
**Boundary:** `G_ENV=1` means the environment is reproducibly executable; it does not mean the infrastructure model has passed full mathematical verification or empirical validation.

---

## 0. Method and claim discipline

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
\text{TEST}
}
```

Claim tags:

```text
[E] external/software fact
[P] preregistered thesis choice
[D] derived rationale
[A] explicit assumption
[U] unresolved item
```

NASA-STD-7009B and ASME VVUQ practice motivate traceability, implementation verification, validation separation and acceptance criteria. They do not prescribe the package/version choices below; those are Phase-1 reproducibility decisions `[P]`.

---

# 1. Reproducibility object

A Phase-1 run is identified by

```math
\mathcal R_{run}
=
(H_D,H_\Theta,H_{env},H_{lock},H_{code},H_{seed},ID_{scenario}).
```

For the current canonical executable environment:

```text
H_code = a11914a1e7d015d75209e32c84a2459114ba7f17
H_lock = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env  = sha256:02dcd331815e060c6f9601c9de7cfc9b9d6aa5e487bae08c6c81520b0245a716
H_D    = PENDING_ACN_AUTHENTICATED_ACQUISITION
```

`H_D` is intentionally unresolved because ACN authenticated acquisition has not succeeded.

---

# 2. Canonical runtime `[P/E]`

```text
container family = Docker / OCI
base family      = python:3.11.16-slim-bookworm
canonical arch   = linux/amd64
Python           = CPython 3.11.16
floating point   = IEEE-754 float64 for numerical state arrays
PYTHONHASHSEED   = 0
OMP threads      = 1
OpenBLAS threads = 1
MKL threads      = 1
NumExpr threads  = 1
```

The canonical reported run is linux/amd64 even when development occurs on Apple Silicon. Cross-architecture development results are not authoritative confirmatory results unless separately shown equivalent.

### Why Python 3.11 `[D]`

ACN Portal 0.3.3 upstream CI included Python 3.11, so the frozen interpreter remains within the demonstrated upstream test range rather than relying on an untested newer interpreter.

---

# 3. Canonical package identity

Direct scientific/runtime pins:

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

The authoritative dependency identity is the fully resolved hash-locked file:

```text
project/requirements-phase1-v1.lock.txt
```

with

```text
LOCKFILE_SHA256 = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
```

The environment installs this file using pip hash verification; package ranges are not used for canonical runs.

### ACN Portal `[E/D]`

```text
package          = acnportal==0.3.3
upstream commit  = 14e723b11339e56ca3afd2bf4969f9e4bc8c2623
```

Its frozen upstream unit suite is included in the environment gate.

### SALib `[P/D]`

`SALib==1.4.8` is retained because it provides the preregistered Morris/Sobol methods while remaining compatible with the conservative NumPy-1.26 line used alongside ACN Portal 0.3.3. This is a software-risk choice, not a claim of scientific superiority.

---

# 4. Executed environment closure `[E]`

Canonical GitHub Actions run:

```text
workflow          = Phase 1 environment lock and verification smoke
run ID            = 34700099915
job ID            = 103570219520
head/code SHA     = a11914a1e7d015d75209e32c84a2459114ba7f17
conclusion        = SUCCESS
artifact ID       = 10300396362
artifact digest   = sha256:0b65f641b875b35e52db015c8c7c3520f31b562f65c664628a3716da4a795f35
```

Container identities:

```text
Docker image ID        = sha256:feab21248dbf3694ab8a4247c1bc416e08780f013041fd0b9a2fca56431c1b6b
OCI descriptor digest = sha256:02dcd331815e060c6f9601c9de7cfc9b9d6aa5e487bae08c6c81520b0245a716
OCI archive SHA-256    = 230918f8be9e8a7b13ad8a2a40a300c47f44c048b3e96ba465ce7101aa159942
```

Executed checks:

```text
hash-lock identity/install                 PASS
required package imports                   PASS
SALib Morris + Sobol smoke                 PASS
ACN Portal frozen-upstream unit tests      PASS
Phase-1 verification fixtures on host      22 passed
Phase-1 verification fixtures in OCI       22 passed
legacy architecture fixture                PASS
linux/amd64 OCI build/export               PASS
credential hygiene                         PASS
```

---

# 5. Environment gate

Define

```math
G_{ENV}
=
G_{build}
G_{install}
G_{import}
G_{unit}
G_{smoke}
G_{lock}
G_{container}
G_{identity}
G_{secret}.
```

Every term above passed in canonical run `34700099915`; therefore

```math
\boxed{G_{ENV}=1.}
```

Permitted claim:

> The Phase-1 software environment corresponding to executable code SHA `a11914a...` can be reconstructed from the frozen hash-lock, passes the declared package/library/fixture smoke suite, and has an immutable linux/amd64 OCI identity.

Prohibited inference:

```math
G_{ENV}=1\not\Rightarrow G_V=1.
```

---

# 6. Public benchmark identity under the environment

The immutable benchmark workflow independently confirmed the frozen public source objects and calculated local raw hashes:

```text
case33bw.m
SHA256 = b40831eeb444669ae876e2996f0dda9f05cd83e81b314b8dfca51e4890cca95d
bytes  = 4866

SiouxFalls_net.tntp
SHA256 = ace99b24cec69c273ff0cf3d6d074110177f0cc0ae24b0c7a9f4f4cb5e27635c
bytes  = 3136

SiouxFalls_trips.tntp
SHA256 = 56f9566857f3f66730fd5c4232258d7ee3ac2931a476526331afd062f4958de7
bytes  = 10859
```

These are data identities, not model-validation results.

---

# 7. Full verification is currently not closed

The corrected transportation implementation at `H_code=a11914a...` was run against the immutable Sioux Falls benchmark with the preregistered criterion

```math
RG\le10^{-6},\qquad N_{iter}\le5000.
```

Observed result:

```math
RG=4.215612504228978\times10^{-6}>10^{-6}.
```

Therefore

```text
traffic numerical convergence = FAIL
G_V                           = 0 / NOT CLOSED
```

The environment remains PASS; the numerical verification remains FAIL. These conclusions are deliberately separated.

Failure evidence is preserved by benchmark workflow run `34700331684`, artifact ID `10300236909`, artifact digest `sha256:a688992b67de054f94dd5c7a7f13587285f36fc9c904c684ead11c1490302904`.

---

# 8. ACN boundary

The ACN acquisition workflow cannot be completed until an authorized token is configured as GitHub Actions secret `ACN_API_TOKEN`.

Current state:

```text
ACN workflow run = 34698786730
credential gate  = BLOCKED_EXTERNAL_CREDENTIAL
raw ACN SHA256   = UNRESOLVED
processed hashes = UNRESOLVED
```

No token is to be committed or pasted into chat.

---

# 9. Canonical scientific boundary

```math
\boxed{
G_{ENV}=1,
\qquad
G_D=0,
\qquad
G_V=0.
}
```

Hence

```math
\boxed{
\text{validation, H1/H2, and Stage-5 resilience/viability execution remain blocked}.
}
```

The next admissible computational work is restricted to resolving the traffic-solver verification defect under the same frozen mathematical problem and completing authenticated ACN materialization/provenance.
