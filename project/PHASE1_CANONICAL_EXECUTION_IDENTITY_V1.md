# Phase 1C — Canonical Execution Identity v1

![Status](https://img.shields.io/badge/status-ENVIRONMENT%20IDENTITY%20CLOSED-1A7F37)
![Phase](https://img.shields.io/badge/phase-1C-0969DA)

**Frozen/updated:** 2026-09-12  
**Canonical environment run:** GitHub Actions `34700099915`  
**Executable code SHA:** `a11914a1e7d015d75209e32c84a2459114ba7f17`  
**Authority:** `PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md` + committed hash-lock + successful canonical environment workflow  
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

This revision supersedes the earlier environment identity at code SHA `b8d47d6baa9e0cde51c5dd4d0e41be92e0445d7a` because the transportation verification implementation was subsequently corrected and committed at `a11914a1e7d015d75209e32c84a2459114ba7f17`. The new environment run verifies the exact corrected executable state.

---

# 1. Canonical successful environment run `[E]`

```text
workflow            = Phase 1 environment lock and verification smoke
run ID              = 34700099915
job ID              = 103570219520
head/code SHA       = a11914a1e7d015d75209e32c84a2459114ba7f17
status/conclusion   = completed / success
runner              = Ubuntu 24.04 / linux-amd64
Python              = CPython 3.11.16
artifact ID         = 10300396362
artifact name       = phase1-environment-lock-a11914a1e7d015d75209e32c84a2459114ba7f17
artifact digest     = sha256:0b65f641b875b35e52db015c8c7c3520f31b562f65c664628a3716da4a795f35
```

Artifact retention is workflow-controlled. The hashes below, not artifact availability, are the enduring execution identities.

---

# 2. Frozen execution identity

```math
\mathcal R_0
=
(H_{code},H_{lock},H_{env},H_D,ID_{run},t_{run}).
```

```text
H_code = a11914a1e7d015d75209e32c84a2459114ba7f17
H_lock = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env  = sha256:02dcd331815e060c6f9601c9de7cfc9b9d6aa5e487bae08c6c81520b0245a716
H_D    = PENDING_ACN_AUTHENTICATED_ACQUISITION
ID_run = 34700099915
t_run  = 2026-09-12T14:43Z canonical workflow execution window
```

Additional immutable environment evidence:

```text
Docker image ID       = sha256:feab21248dbf3694ab8a4247c1bc416e08780f013041fd0b9a2fca56431c1b6b
OCI archive SHA-256   = 230918f8be9e8a7b13ad8a2a40a300c47f44c048b3e96ba465ce7101aa159942
OCI descriptor digest= sha256:02dcd331815e060c6f9601c9de7cfc9b9d6aa5e487bae08c6c81520b0245a716
```

The exact resolved dependency lockfile remains `project/requirements-phase1-v1.lock.txt`; its SHA-256 is `H_lock` above.

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

The complete hash-locked dependency file, not this descriptive subset, is authoritative.

---

# 4. Executed environment evidence `[E]`

Canonical run `34700099915` passed every declared environment step, including:

```text
canonical hash-lock verification/install  = PASS
package import smoke                       = PASS
SALib Morris smoke                         = PASS
SALib Sobol smoke                          = PASS
ACN Portal frozen-upstream test suite      = PASS
Phase-1 verification fixtures (host)       = 22 passed
Phase-1 verification fixtures (OCI)        = 22 passed
legacy architecture fixture                = PASS
OCI linux/amd64 build/export               = PASS
credential-hygiene scan                    = PASS
```

Frozen upstream ACN Portal source used for package-behavior evidence:

```text
repository = zach401/acnportal
commit     = 14e723b11339e56ca3afd2bf4969f9e4bc8c2623
package    = acnportal 0.3.3
```

---

# 5. Environment gate

Define

```math
G_{ENV}
=
G_{lock}G_{install}G_{import}G_{SALib}G_{ACNlib}G_{fixture}G_{container}G_{identity}G_{secret}.
```

All terms were executed successfully in canonical run `34700099915`; therefore

```math
\boxed{G_{ENV}=1.}
```

Allowed claim:

> The declared Phase-1 computational environment for code SHA `a11914a...` is internally executable under the frozen dependency identity, required package APIs, verification fixtures, and canonical linux/amd64 container.

This claim does **not** establish correctness of the full coupled infrastructure model.

---

# 6. Public benchmark materialization `[E]`

The immutable benchmark workflow independently materialized the locked upstream objects and verified their Git blob identities. Their local SHA-256 identities are:

```text
MATPOWER case33bw.m
  SHA256 = b40831eeb444669ae876e2996f0dda9f05cd83e81b314b8dfca51e4890cca95d
  bytes  = 4866

SiouxFalls_net.tntp
  SHA256 = ace99b24cec69c273ff0cf3d6d074110177f0cc0ae24b0c7a9f4f4cb5e27635c
  bytes  = 3136

SiouxFalls_trips.tntp
  SHA256 = 56f9566857f3f66730fd5c4232258d7ee3ac2931a476526331afd062f4958de7
  bytes  = 10859
```

These hashes close the local materialization identity for the public power/transport benchmark objects. They do not close the ACN data gate.

---

# 7. ACN data gate remains open `[U]`

The authenticated ACN workflow previously reached its deliberate credential-presence gate and stopped because repository secret `ACN_API_TOKEN` is absent. No ACN record was requested or transformed.

Therefore

```text
H_D = PENDING_ACN_AUTHENTICATED_ACQUISITION
```

and the complete experiment identity

```math
\mathcal R^*=(H_{code},H_{lock},H_{env},H_D)
```

is not yet closed.

---

# 8. Verification status is separate from environment status

A successful environment does not compensate for a failed numerical verification test. In particular, the immutable Sioux Falls full user-equilibrium verification on the corrected code reached

```math
RG=4.215612504228978\times10^{-6}
```

after the maximum preregistered `5000` iterations, while the frozen acceptance criterion is

```math
RG\le10^{-6}.
```

Therefore the transportation convergence test remains **FAIL** and full `G_V` is not closed.

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
full model verification;
ACN data validity;
calibration/holdout validation;
H1/H2 conclusions;
resilience/viability conclusions.
```

---

# 10. Next hard gates

```math
\boxed{
\begin{array}{c}
\text{resolve the remaining transportation convergence defect without weakening the frozen test}\\
+\\
\text{configure ACN_API_TOKEN externally and materialize/hash the frozen ACN request}
\end{array}
\rightarrow
G_V\text{ re-execution}.
}
```

No validation or H1/H2 execution is authorized until all mandatory verification tests applicable to the confirmatory model pass.
