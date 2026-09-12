# Phase 1C — Verification-Only Executable Implementation v1

![Status](https://img.shields.io/badge/status-IMPLEMENTED%20/%20NOT%20YET%20CANONICALLY%20VERIFIED-0969DA)
![Scope](https://img.shields.io/badge/scope-Phase--1%20verification%20only-1A7F37)

**Implemented:** 2026-09-12  
**Authority:** `PHASE1_EXPERIMENT_SPECIFICATION_V1.md` + `PHASE1_VERIFICATION_TEST_MATRIX_V1.md` + `CANONICAL_DEPENDENCY_CONTRACT_V1.md`  
**Purpose:** provide the first committed executable realization of the declared mathematics without opening holdout validation or H1/H2.  
**Boundary:** this code is admitted only for verification. It does not yet constitute thesis validation evidence.

---

## 0. Method

The implementation follows

```math
\boxed{
\text{DECLARED MATHEMATICS}
\rightarrow
\text{MINIMUM EXECUTABLE FUNCTION}
\rightarrow
\text{ANALYTICAL/LIMIT FIXTURE}
\rightarrow
\text{AUTOMATED TEST}
\rightarrow
\text{CANONICAL ENVIRONMENT RERUN}.
}
```

This deliberately separates software construction from scientific interpretation.

---

# 1. Executable package

The verification-only package is

```text
phase1_exec/
```

with modules:

```text
contracts.py         canonical d_e=(C_e,Sigma_e,Pi_e) runtime primitives;
power.py             radial constant-power backward/forward-sweep solver + branch-flow residuals;
transport.py         BPR costs, deterministic shortest paths, all-or-nothing assignment, Frank-Wolfe UE;
information.py       delay operator + bounded transparent test controller;
organization.py      restoration clock + energization guard;
coupling.py          explicit T->P charging-load map and P->T availability map;
events.py            deterministic preregistered event ordering;
reproducibility.py   deterministic SHA-256-derived run seeds.
```

The package intentionally excludes Stage-5 viability mathematics and confirmatory H1/H2 aggregation.

---

# 2. Physics preservation

The power implementation solves a radial electrical model using complex per-unit voltages/currents. It does not replace the power law with a graph diffusion equation.

The transport implementation solves a Wardrop-style user-equilibrium problem through BPR link costs and Frank-Wolfe iterations. It does not reuse the electrical equations.

Therefore the executable architecture preserves

```math
\boxed{F_P\neq F_T.}
```

Cross-domain effects enter through explicit maps in `coupling.py`, consistent with the canonical dependency contract rather than through a shared artificial physics law.

---

# 3. Current automated verification coverage

The committed tests are under

```text
tests/phase1/
```

and currently exercise the following preregistered mechanisms/limits.

| Verification family | Executable fixture now present | Matrix relationship |
|---|---|---|
| canonical guard/dependency contribution | guard-off contribution is exactly zero; guard-on operator remains active | V-C01/V-C02 partial |
| radial power zero-load limit | flat 1 p.u. voltage, zero branch current | supports V-P01/V-P02 |
| branch-flow equations | P/Q balance, voltage-drop and current relation residuals checked on deterministic radial fixture | V-P01 |
| charging-load sign | added positive real load lowers receiving voltage on declared simple radial fixture | V-P03 mechanism-sign fixture |
| BPR link law | free-flow limit and monotonic nonnegative congestion effect | V-T01 |
| Frank-Wolfe UE | symmetric network converges to symmetric flow; node conservation checked | V-T02/V-T03 fixture |
| access-set reduction | removing a path cannot reduce shortest-path cost when remaining costs are fixed | V-T05 |
| information zero-delay | delay operator becomes identity | V-I01 |
| exact delay slots | 1/3/6 slot shifts corresponding to 5/15/30-minute treatment levels | V-I02 |
| controller bounds/direction | controller remains within [0,site cap] and reacts monotonically to higher forecast stress | V-I05 |
| restoration clock | additive clock, zero-delay limit, monotonicity, unreachable-path infinity | V-O01–V-O04 partial |
| P->T availability map | energized/de-energized branch maps exactly to binary charging availability | V-C03 |
| T->P load map | charging demand is added only at declared receiving bus; zero charging recovers base load exactly | V-C04/V-P02 |
| event priority | equal-time events follow frozen priority independent of input ordering | V-M01 |
| seed derivation | identical run ID -> identical seed; different IDs -> different seeds | V-R03 fixture |

These tests are **necessary but not sufficient** for `G_V=1`.

---

# 4. Tests still blocked/pending

The following cannot honestly be marked PASS until the remaining environment/data gates are resolved:

```text
V-E01–V-E08  canonical environment/provenance;
V-D01–V-D03  full immutable benchmark ingestion;
V-D04–V-D06  ACN timestamp/grid/energy reconstruction;
V-P01        full 33-bus residual across all solved states;
V-P04        actual branch 23->24 topology event on the benchmark;
V-T02–V-T06 full Sioux-Falls assignment/access calculations;
V-I03–V-I04 calibration-only forecast/provenance and holdout baseline gate;
V-C05–V-C06 nested N0/N1/N2 configuration-diff tests;
V-M02        5-minute vs 2.5-minute refinement;
V-R01–V-R02 canonical-container deterministic/stochastic repeats.
```

No pending item is inferred from passing a smaller synthetic fixture.

---

# 5. Development execution result

Before committing the implementation, the isolated verification suite was executed in a noncanonical development runtime and returned

```text
20 passed
```

for the current synthetic/unit fixtures.

This result is recorded only as **development evidence**. It does not satisfy the canonical software-environment gate because that runtime is not the frozen Python-3.11 OCI environment and does not use the resolved hash lockfile.

The authoritative verification result must be regenerated inside the locked environment with a committed code SHA.

---

# 6. Code-SHA rule

The executable model is now committed, so the prior condition

```text
EXECUTABLE_CODE_SHA = BLOCKING-PENDING
```

can be narrowed to:

```text
EXECUTABLE CODE EXISTS = YES
CANONICAL RUN CODE SHA  = to be set to the exact commit checked out by the first admitted verification run
```

The run manifest—not this document—will be authoritative for `H_code`, because later verification fixes may legitimately create a new executable SHA.

---

# 7. Why no confirmatory runner is implemented yet

A script that computes final H1/H2 now would create a procedural path around the remaining gates. Therefore Phase-1 v1 intentionally stops at verification-capable constituent and coupling functions.

The confirmatory runner may be implemented only after:

```math
V\text{-E01--E08}=PASS,
```

all required input hashes exist, and the complete applicable verification suite is executable.

---

# 8. Next authorized operation

The next allowed operation is computational infrastructure closure:

```text
1. resolve and hash the Python dependency lock inside Python 3.11/Linux-amd64;
2. build the frozen OCI image and record its immutable digest;
3. run package/environment smoke tests;
4. acquire/hash the frozen ACN source when ACN_API_TOKEN is securely available;
5. run the complete verification matrix and write per-test JSON evidence.
```

Until those conditions are met:

```math
\boxed{\text{VALIDATION BLOCKED},\qquad H_1/H_2\text{ BLOCKED}.}
```
