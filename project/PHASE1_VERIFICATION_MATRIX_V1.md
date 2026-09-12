# Phase 1C — Verification Execution Matrix v1

![Status](https://img.shields.io/badge/status-EXECUTION%20MATRIX%20ACTIVE-0969DA)
![Phase](https://img.shields.io/badge/phase-1C-1A7F37)

**Initialized:** 2026-09-12  
**Authority:** `PHASE1_VERIFICATION_TEST_MATRIX_V1.md` + `PHASE1_CANONICAL_EXECUTION_IDENTITY_V1.md` + `PHASE1_DATA_PROVENANCE_REGISTER_V1.md`  
**Purpose:** collapse the detailed preregistered verification tests into nine noncompensable execution gates without weakening any original test.  
**Rule:** a gate is `PASS` only from executed evidence. `BLOCKED` and `NOT YET EXECUTED` are not failures of the scientific hypothesis, but neither counts as a pass.

---

## 0. Gate logic

Define

```math
G_V
=
\prod_{k=1}^{9}G_{Vk},
\qquad
G_{Vk}\in\{0,1\}.
```

Therefore

```math
\boxed{
G_V=1
\iff
G_{V1}=G_{V2}=\cdots=G_{V9}=1.
}
```

No averaging or compensatory score is allowed. A failed or unresolved critical gate cannot be offset by strong performance elsewhere.

Execution-state vocabulary:

```text
PASS                 executed and acceptance condition satisfied;
FAIL                 executed and acceptance condition violated;
BLOCKED              prerequisite unavailable;
NOT_YET_EXECUTED     executable but evidence not yet generated;
PARTIAL              some subordinate tests pass, full gate not closed.
```

For the multiplicative equation, only `PASS` maps to `1`; all other states keep the gate open and therefore prevent `G_V=1`.

---

# 1. G_V1 — Equations and algorithms implemented as specified

Question:

> Does the code implement the declared constituent equations, coupling operators, guards, event logic and algorithms without hidden substitutions?

Maps to detailed tests including:

```text
V-P01..V-P05
V-T01..V-T06
V-I01..V-I05
V-O01..V-O04
V-C01..V-C06
V-M01
```

Evidence already executed:

```text
- radial power synthetic branch-flow residual fixture: PASS;
- added-load voltage-direction fixture: PASS;
- BPR monotonicity fixture: PASS;
- simple Frank-Wolfe equilibrium fixture: PASS;
- road-closure shortest-path monotonicity fixture: PASS;
- canonical dependency/guard/event unit fixtures: PASS within current 20-test suite.
```

Current state:

```text
G_V1 = PARTIAL
```

Reason: not every detailed benchmark/data-backed test has yet been executed against the frozen real benchmark inputs.

---

# 2. G_V2 — Units, dimensions and schema consistency

Question:

> Do quantities preserve declared dimensions and source schemas across P, T, I and O interfaces?

Required evidence:

```text
- MATPOWER source conversion/schema test;
- Sioux Falls schema/unit test;
- ACN timezone/power/replay schema tests;
- cross-interface unit conversions;
- dimensional audit of restoration times and charging injection.
```

Current state:

```text
G_V2 = PARTIAL / ACN-DEPENDENT PORTION BLOCKED
```

---

# 3. G_V3 — Conservation and balance

Question:

> Do implemented solutions satisfy the constituent physical/network balance laws within preregistered numerical tolerances?

Evidence already executed:

```text
power branch-flow residual synthetic test = PASS (<1e-10 fixture tolerance);
transport node-flow conservation synthetic test = PASS (<1e-10 fixture tolerance).
```

Still required:

```text
full IEEE-33 benchmark residual execution;
full Sioux Falls assignment conservation execution;
ACN energy reconstruction V-D06.
```

Current state:

```text
G_V3 = PARTIAL
```

---

# 4. G_V4 — Mathematical/physical limiting cases

Question:

> When a mechanism is removed or a parameter approaches a declared limit, does the code recover the analytically expected reduced model?

Required limits include

```math
\Phi_e=0,
\qquad
\gamma_e=0,
\qquad
\delta_I=0,
\qquad
P_{ch}=0,
```

plus road reopen/closure and zero organizational-delay limits.

Current evidence:

```text
multiple synthetic coupling/availability/delay/restoration fixtures = PASS within current test suite.
```

Current state:

```text
G_V4 = PARTIAL
```

Full benchmark-backed ablation equivalence remains to be run.

---

# 5. G_V5 — Numerical convergence and stability

Question:

> Are accepted numerical solutions converged and stable under preregistered solver/time-step criteria?

Frozen criteria include:

```math
\epsilon_P\le10^{-8},
\qquad
RG\le10^{-6},
\qquad
\epsilon_{\Delta t}\le10^{-3}.
```

Current evidence:

```text
simple radial solver convergence fixture = PASS;
simple Frank-Wolfe convergence fixture = PASS.
```

Still required:

```text
IEEE-33 benchmark convergence;
Sioux Falls full-OD convergence;
5-min vs 2.5-min designated refinement test after ACN trajectory exists.
```

Current state:

```text
G_V5 = PARTIAL
```

---

# 6. G_V6 — Invariance to irrelevant implementation choices

Question:

> Do results remain unchanged under changes that should not alter the declared mathematics?

Required evidence:

```text
- deterministic ordering independent of hash/container iteration;
- host vs canonical-container fixture agreement;
- configuration ablations modify only declared I/O fields;
- no hidden duplicate charging injection;
- no silent solver-failure deletion.
```

Executed evidence:

```text
20 Phase-1 fixtures passed on host;
20 Phase-1 fixtures passed in canonical linux/amd64 container;
PYTHONHASHSEED/thread policy fixed;
deterministic seed derivation repeated identically.
```

Current state:

```text
G_V6 = PARTIAL
```

Reason: full benchmark/state-vector invariance has not yet been exercised.

---

# 7. G_V7 — Synthetic known-answer recovery

Question:

> Does the implementation recover cases whose correct behavior is known analytically or by construction?

Executed examples:

```text
zero-load radial feeder -> flat 1.0 p.u. voltage and zero current: PASS;
two-path symmetric traffic network -> 5/5 equilibrium split: PASS;
BPR zero-flow -> free-flow time: PASS;
fixed-cost path-set reduction cannot reduce shortest-path cost: PASS;
restoration/additive-event synthetic fixtures: PASS in current suite.
```

Current state:

```text
G_V7 = PASS for the currently declared synthetic known-answer fixture set.
```

Any future addition of a mandatory synthetic fixture reopens this gate until executed.

---

# 8. G_V8 — Physically coherent perturbation/sensitivity behavior

Question:

> Do controlled input perturbations produce changes with the mechanism sign/direction implied by the declared model in its bounded operating domain?

Executed examples:

```text
added positive load in simple radial case lowers receiving voltage: PASS;
BPR travel time increases with nonnegative flow: PASS;
road closure with fixed remaining costs does not reduce shortest-path cost: PASS.
```

Still required:

```text
benchmark-level charging-load sign check;
organizational-delay monotonicity over registered parameter ranges;
information latency/error perturbation checks;
parameter-screening coherence once calibrated ACN objects exist.
```

Current state:

```text
G_V8 = PARTIAL
```

---

# 9. G_V9 — Complete reproducibility from R*

Question:

> Can the complete verification execution be reproduced from the immutable code, dependency, environment and data identities?

Required object:

```math
\mathcal R^*
=
(H_{code},H_{lock},H_{env},H_D).
```

Known identities:

```text
H_lock = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
H_env  = immutable OCI descriptor recorded in PHASE1_CANONICAL_EXECUTION_IDENTITY_V1.md
H_D    = unresolved because ACN credential is absent
```

The ACN acquisition workflow run `34698786730` verified the canonical lock installation but failed at the explicit external-credential presence gate before any download.

Current state:

```text
G_V9 = BLOCKED_EXTERNAL_CREDENTIAL
```

---

# 10. Current gate vector

```math
\mathbf G_V
=
[
P,
P,
P,
P,
P,
P,
1,
P,
B
],
```

where `P=PARTIAL` and `B=BLOCKED` are execution-state symbols rather than numeric successes.

Thus the only valid binary scientific conclusion is

```math
\boxed{G_V\neq1\text{ at present}.}
```

It would be incorrect to report `G_V=0` as a mathematical/model failure because several gates have not yet been fully executable; the precise status is **verification not yet closed**.

---

# 11. Validation unlock condition

Validation is authorized only when

```math
\boxed{
G_{V1}=G_{V2}=\cdots=G_{V9}=1.
}
```

Until then:

```text
calibration beyond preregistered preparation = BLOCKED;
holdout validation = BLOCKED;
H1/H2 confirmatory comparisons = BLOCKED;
Stage-5 viability/resilience claims = BLOCKED.
```

---

# 12. Next execution order

```math
\boxed{
\text{close environment hardening run}
\rightarrow
\text{execute all non-ACN benchmark tests}
\rightarrow
\text{configure ACN secret externally}
\rightarrow
H_D
\rightarrow
\text{execute ACN-dependent tests}
\rightarrow
G_V.
}
```

No hypothesis result is admissible before this sequence closes.
