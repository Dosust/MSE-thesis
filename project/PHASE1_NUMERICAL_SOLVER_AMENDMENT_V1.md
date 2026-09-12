# Phase 1C — Numerical Solver Amendment v1

![Status](https://img.shields.io/badge/status-VERIFICATION--STAGE%20AMENDMENT-D29922)
![Scope](https://img.shields.io/badge/scope-TRANSPORT%20NUMERICS%20ONLY-0969DA)

**Date:** 2026-09-12  
**Trigger:** executed verification failure `V-T02` on immutable Sioux Falls benchmark  
**Does not alter:** benchmark, BPR equations, OD matrix, UE objective, relative-gap definition, `RG <= 1e-6` threshold, `N_it <= 5000` cap, P/T/I/O dependency mechanisms, H1/H2, calibration/validation split, or confirmatory outcomes.  
**Status of confirmatory results when amended:** none inspected; validation and H1/H2 remained blocked.

---

## 1. Governing method

```math
\boxed{
\text{LEARN}\to\text{VERIFY}\to\text{FORMULATE}\to\text{DERIVE}
\to\text{TEST}\to\text{VALIDATE}\to\text{SYNTHESIZE}\to\text{ADVANCE}
}
```

Claim tags:

```text
[E] executed/external evidence;
[D] deduction;
[P] thesis implementation decision;
[A] assumption;
[U] unresolved.
```

No failed verification test is deleted or weakened because its result is inconvenient.

---

# 2. Executed failure that triggered the amendment `[E]`

Immutable benchmark run:

```text
workflow = Phase 1 immutable benchmark verification
run ID   = 34699245970
code SHA = 57f647c55655091ed6ef50c1eb2cc2f584e294d0
```

The source identities passed before the solver was executed:

```text
MATPOWER case33bw Git blob = 97e510bee25c543de0453959672fe86b40a999c8
Sioux Falls network blob   = 66d0eca4ddcfb82f861bea040060deab7a741b2f
Sioux Falls OD blob        = db70eda57738877811e9ac07c25a567973d3b6a0
```

Classical link-based Frank-Wolfe result:

```math
RG_{5000}=2.6051341708681704\times10^{-5}.
```

Frozen criterion:

```math
RG\le10^{-6},
\qquad
N_{it,T}\le5000.
```

Therefore:

```math
\boxed{V\text{-}T02_{\mathrm{pure\ FW}}=\mathrm{FAIL}.}
```

This failure remains permanently in the audit trail.

---

# 3. Separate non-scientific test defect `[D]`

The same run also compared

```text
0.041999999999999996 == 0.042
```

using exact binary floating-point equality for bus-24 per-unit load.

However the already-preregistered `V-D01` rule is floating agreement to absolute tolerance `<= 1e-12`. Thus this failure is a **test implementation defect**, not a change in physical data or acceptance criterion.

Correction permitted:

```math
|P_{24}^{parsed}-0.042|\le10^{-12}.
```

No tolerance is being relaxed; the test is being brought into conformance with the frozen rule.

---

# 4. General numerical evidence `[E]`

The classical Frank-Wolfe method for traffic assignment can exhibit slow/stiff convergence near equilibrium. Mitradjieva and Lindberg developed conjugate-direction Frank-Wolfe (CFW) and bi-conjugate Frank-Wolfe (BFW) methods for the same linearly constrained convex traffic-assignment problem and reported favorable convergence relative to pure FW; they also establish global convergence for CFW.

Citation:

> Mitradjieva, M., & Lindberg, P. O. (2013). *The Stiff Is Moving—Conjugate Direction Frank-Wolfe Methods with Applications to Traffic Assignment*. Transportation Science, 47(2), 280–293. https://doi.org/10.1287/trsc.1120.0409

AequilibraE, an established open transportation-modeling implementation, likewise exposes traditional FW, CFW and BFW as alternative equilibration algorithms for traffic assignment. This is implementation precedent, not validation of our code.

---

# 5. Scope match `[D]`

Our transportation problem remains the same separable Beckmann/Wardrop user-equilibrium problem:

```math
\min_x
\quad
\sum_{a\in\mathcal A}
\int_0^{x_a}t_a(w)\,dw
```

subject to the same feasible network-flow set, with

```math
t_a(x_a)
=
t_a^0
\left[
1+\alpha_a\left(\frac{x_a}{c_a}\right)^{\beta_a}
\right].
```

The amendment changes only the feasible descent direction used to solve this same optimization problem.

Therefore it does **not** change:

```text
network;
OD demand;
BPR parameters;
physical meaning of travel time;
crew route definition;
closure mechanism;
relative-gap definition;
convergence tolerance;
maximum iteration budget.
```

---

# 6. Thesis implementation decision `[P]`

The canonical Phase-1 transport equilibrium solver is amended from **pure Frank-Wolfe** to **Conjugate Frank-Wolfe (CFW)** for benchmark/full execution.

Pure FW remains implemented and retained as a diagnostic/reference solver.

Let

```text
x_k = current feasible link-flow vector;
y_k = current all-or-nothing Frank-Wolfe point;
s_{k-1} = previous CFW point of sight;
H_k = diagonal Hessian of the separable Beckmann objective at x_k.
```

For the first update, use the ordinary FW point:

```math
s_k=y_k.
```

Thereafter define

```math
\lambda_k
=
\frac{
(s_{k-1}-x_k)^T H_k (y_k-x_k)
}{
(s_{k-1}-x_k)^T H_k (y_k-s_{k-1})
},
```

with feasibility-preserving clipping

```math
\lambda_k\in[0,0.99999].
```

Then

```math
s_k
=
\lambda_k s_{k-1}
+
(1-\lambda_k)y_k,
```

and the next iterate is obtained by the same exact one-dimensional Beckmann line search along

```math
s_k-x_k.
```

This construction follows the conjugate-direction FW logic used in the cited literature and established transportation software; the thesis implementation is independently tested.

---

# 7. Acceptance criteria remain unchanged `[P]`

```math
\boxed{
RG\le10^{-6}
\quad\text{within}\quad
N_{it,T}\le5000.
}
```

No post-failure threshold change is allowed.

Additional amendment-specific verification requirements:

```text
1. CFW must reproduce analytical/simple-network known-answer tests;
2. every CFW iterate must remain feasible;
3. node-flow conservation must satisfy the original tolerance;
4. final relative gap must satisfy the original tolerance;
5. deterministic repeated execution must produce the same report hash;
6. pure FW failure remains archived rather than overwritten.
```

---

# 8. Why this is scientifically admissible

This amendment occurs during **verification**, before validation data are opened and before H1/H2 comparisons are executed.

The revised logic is:

```math
\boxed{
\text{solver verification failure}
\rightarrow
\text{audited numerical-method repair}
\rightarrow
\text{rerun same frozen tests}
}
```

not

```math
\text{unfavorable scientific result}
\rightarrow
\text{change model until hypothesis passes}.
```

The amendment cannot change any confirmatory scientific conclusion because no confirmatory results have yet been admitted.

---

# 9. Falsification rule

If CFW also fails

```math
RG\le10^{-6}
```

within 5000 iterations on the immutable Sioux Falls benchmark, `V-T02` remains `FAIL` and Phase-1 validation remains blocked. The tolerance or iteration budget will not be weakened inside v1.
