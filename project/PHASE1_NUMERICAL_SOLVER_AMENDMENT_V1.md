# Phase 1C — Numerical Solver Amendment v1

![Status](https://img.shields.io/badge/status-BFW%20VERIFICATION%20PASS-1A7F37)
![Scope](https://img.shields.io/badge/scope-TRANSPORT%20NUMERICS%20ONLY-0969DA)

**Date:** 2026-09-12  
**Trigger:** executed verification failure `V-T02` on the immutable Sioux Falls benchmark.  
**Final numerical amendment:** Biconjugate Frank–Wolfe (BFW).  
**Does not alter:** benchmark, BPR equations, OD matrix, Beckmann/UE objective, relative-gap definition, `RG <= 1e-6` threshold, `N_it <= 5000` cap, P/T/I/O dependency mechanisms, H1/H2, calibration/validation split, or confirmatory outcomes.  
**Boundary:** numerical verification only; no empirical validation or H1/H2 conclusion is implied.

---

## 1. Governing method

```math
\boxed{
\text{LEARN}\to\text{VERIFY}\to\text{FORMULATE}\to\text{DERIVE}
\to\text{TEST}\to\text{VALIDATE}\to\text{SYNTHESIZE}\to\text{ADVANCE}
}
```

Evidence discipline:

```math
\boxed{
\text{GENERAL EVIDENCE}\to\text{SCOPE MATCH}\to\text{THESIS APPLICATION}
\to\text{WHY}\to\text{CRITICAL TEST}
}
```

Claim tags: `[E]` executed/external evidence, `[D]` deduction, `[P]` thesis implementation decision, `[A]` assumption, `[U]` unresolved.

---

# 2. Frozen scientific problem `[P]`

The transportation problem remains the same separable Beckmann/Wardrop user-equilibrium problem

```math
\min_x\;\sum_{a\in\mathcal A}\int_0^{x_a}t_a(w)\,dw
```

with frozen Sioux Falls network/OD data and BPR link costs

```math
t_a(x_a)=t_a^0\left[1+0.15\left(\frac{x_a}{c_a}\right)^4\right].
```

The preregistered numerical acceptance condition remains

```math
\boxed{RG\le10^{-6},\qquad N_{it,T}\le5000.}
```

No threshold, iteration cap, OD record, BPR parameter, objective, or relative-gap definition was changed after observing the failed result.

---

# 3. Failure history preserved `[E]`

Pure/earlier conjugate implementations did not satisfy the frozen criterion:

```text
initial immutable run      = 34699942787
initial RG                 = 0.1696116807192524
verdict                    = FAIL

corrected CFW code SHA     = a11914a1e7d015d75209e32c84a2459114ba7f17
corrected CFW run          = 34700099913
corrected CFW RG           = 4.215612504228978e-06
verdict                    = FAIL
```

Because

```math
4.215612504228978\times10^{-6}>10^{-6},
```

the CFW result was not reclassified as PASS. These failures remain part of the audit trail.

---

# 4. General evidence and scope match `[E/D]`

Mitradjieva and Lindberg developed conjugate-direction and biconjugate Frank–Wolfe methods for the same class of linearly constrained convex traffic-assignment problems. The methodological implication relevant here is narrow: an accelerated feasible search direction may be changed while retaining the underlying Beckmann problem, all-or-nothing shortest-path oracle, and line search.

Reference:

> Mitradjieva, M., & Lindberg, P. O. (2013). *The Stiff Is Moving—Conjugate Direction Frank-Wolfe Methods with Applications to Traffic Assignment*. Transportation Science, 47(2), 280–293. DOI: `10.1287/trsc.1120.0409`.

An independent implementation was inspected in:

```text
repository = UchidaMizuki/TrafficAssign.jl
file       = src/algorithm-frank_wolfe.jl
commit     = f4d7dbb679c219f4816d510618f472226488ad43
```

This external code is a recurrence/reference anchor only. It is not evidence that the thesis Python implementation is correct. Our implementation must pass its own frozen verification tests.

Scope match:

```text
general method              -> separable convex static traffic assignment
our application             -> Sioux Falls separable BPR Beckmann UE
mathematical invariant      -> same feasible-flow set and same objective
implementation-only change  -> accelerated feasible search direction
```

---

# 5. Thesis implementation amendment `[P/D]`

The BFW solver is isolated in:

```text
phase1_exec/transport_bfw.py
```

The canonical benchmark test and report call this implementation while retaining exactly the same acceptance assertions.

Successful canonical executable head:

```text
d6d97c7353f6d5694dba73ab840ae3a2548dd593
```

The amendment retains:

```text
same immutable Sioux Falls network;
same immutable OD matrix;
same BPR alpha=0.15, beta=4;
same Beckmann objective;
same all-or-nothing oracle;
same exact one-dimensional Beckmann line search;
same relative-gap implementation;
same RG <= 1e-6 criterion;
same max_iter = 5000.
```

Therefore the amendment is a verification-stage numerical repair, not a change to the research hypothesis or physical/engineering model.

---

# 6. Critical test result `[E]`

Canonical benchmark workflow:

```text
workflow       = Phase 1 immutable benchmark verification
run ID         = 34700750330
job ID         = 103571958582
head/code SHA  = d6d97c7353f6d5694dba73ab840ae3a2548dd593
started UTC    = 2026-09-12T14:56:53Z
completed UTC  = 2026-09-12T14:57:36Z
conclusion     = SUCCESS
```

The immutable benchmark integration suite reported:

```text
4 passed in 3.79 s
```

The transport report was:

```text
solver                        = biconjugate-frank-wolfe
iterations                    = 645
relative gap                  = 9.33748496131895e-07
max node balance residual     = 6.184563972055912e-11
scaled node balance residual  = 1.715075976720996e-16
```

Thus

```math
9.33748496131895\times10^{-7}<10^{-6}
\quad\land\quad
645<5000,
```

so the previously failed numerical convergence test now passes without changing its preregistered criterion.

---

# 7. Access-limit and physical-direction checks `[E]`

With equilibrium link costs held fixed, the road-closure verification produced

```text
crew base cost   = 25.92894954231427
crew closed cost = 27.61418250234074
```

hence

```math
T_{crew}^{closed}>T_{crew}^{base}.
```

The same canonical report also preserved the power-side sign test:

```text
bus-24 voltage, base          = 0.9726811009691813 pu
bus-24 voltage, +0.1 MW       = 0.9714126540936994 pu
branch 23-24 current, base    = 0.09581473734223377 pu
branch 23-24 current, +0.1 MW = 0.10532607030491578 pu
power balance residual max    = 3.0808688933348094e-14
```

The added real load therefore lowered local voltage and increased branch current as required by the frozen sign check.

---

# 8. Deterministic reproducibility `[E]`

The canonical workflow generated the benchmark report twice and required byte-for-byte equality before accepting the run.

```text
benchmark report SHA-256 = 4f2b27af34459c7b4022813a58ed93c457eb2430cea660f88f5f5877b81f6a35
artifact ID              = 10300177541
artifact ZIP SHA-256     = 3a87c5ec991e2addf7dde8d0ba896ce0d507a8aecfccba4b44b4c8ff4ef0c73f
```

The public raw data hashes remained unchanged:

```text
case33bw.m            = b40831eeb444669ae876e2996f0dda9f05cd83e81b314b8dfca51e4890cca95d
SiouxFalls_net.tntp   = ace99b24cec69c273ff0cf3d6d074110177f0cc0ae24b0c7a9f4f4cb5e27635c
SiouxFalls_trips.tntp = 56f9566857f3f66730fd5c4232258d7ee3ac2931a476526331afd062f4958de7
```

Therefore the transport PASS is attributable to the versioned numerical implementation amendment, not to changed benchmark inputs.

---

# 9. Allowed and prohibited conclusions

Allowed:

```math
\boxed{
\text{BFW satisfies the preregistered Sioux Falls numerical-convergence criterion on the frozen benchmark.}
}
```

Not established:

```text
empirical validity of the transportation model;
validity of ACN observations;
validity of the complete coupled P-T-I-O model;
identifiability of all Phase-1 parameters;
H1/H2 support;
resilience/viability conclusions.
```

---

# 10. Gate consequence

```text
public power benchmark verification      PASS
public transport convergence             PASS
public transport conservation            PASS
public road-closure limit                PASS
deterministic benchmark report           PASS
ACN raw/provenance gate                  BLOCKED_EXTERNAL_CREDENTIAL
complete Phase-1 verification gate       NOT YET CLOSED
```

The active hard blocker is now authenticated ACN materialization and hashing, followed by execution of the remaining ACN-dependent/full-coupled verification tests. Validation and H1/H2 remain unauthorized until the complete noncompensable verification gate closes.
