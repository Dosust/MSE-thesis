# EGMIV H1 — M2 Dynamic Causal Coupling v1.0

**Method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method  
**Hypothesis:** H1  
**Role:** dynamic causal comparator against verified M0 and M1  
**Parameter status:** `BENCHMARK_TEST_HARNESS_ONLY`

M2 preserves the verified M0 power/traffic solvers and the M1 same-step coupling maps, then adds only the dynamic states required to test whether temporal causal coupling contains information that static coupling cannot represent.

Core added states:

```math
X_k^{M_2}=\left[x_P(k),x_T(k),q_c(k),d_j(k),r_j(k)\right],
```

where `q_c` is charger backlog, `d_j` is repair-crew path progress, and `r_j` is power-component repair progress.

Dynamic charging:

```math
q_c(k+1)=\max\{0,q_c(k)+\Delta t[\lambda_c(k)-\mu_c(k)]\}.
```

Requested charging power includes current arrivals plus backlog demand, while requested EV electricity remains in the power-service denominator even when unserved.

Dynamic recovery uses state-dependent crew travel over CTM cells and monotone repair progress. A blocked road gives zero crew speed; restoration becomes visible to the power solver only on the next step after repair completion.

Mandatory nesting rules:

```math
M_2\rightarrow M_1
\quad\text{when charger memory is suppressed and dynamic repair is disabled},
```

and dynamic repair travel reduces to the M1 static free-flow delay under unobstructed free-flow traffic.

Verification status:

```text
29 passed, 0 failed
```

This includes the retained M1 regression suite plus 16 M2-specific gates. See `reports/M2_VERIFICATION.md`.

## Interpretation boundary

This M2 version is intentionally minimal and nested. Charger queues affect mobility service through FCFS current-arrival fulfillment while the underlying CTM state remains identical to M1. This isolates **interface memory** from route-choice or traffic-rerouting effects. Those richer feedbacks remain deferred until evidence and H1 validation require them.

Repair jobs use fixed road paths and one crew equivalent per job. This verifies dynamic access delay and restoration causality, not organizational resource allocation.
