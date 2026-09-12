# Phase 1B — Verification Test Matrix v1

![Status](https://img.shields.io/badge/status-PREREGISTERED%20VERIFICATION%20MATRIX-0969DA)
![Phase](https://img.shields.io/badge/phase-1B-1A7F37)

**Frozen:** 2026-09-12  
**Authority:** `PHASE1_EXPERIMENT_SPECIFICATION_V1.md` + `PHASE1_PARAMETER_REGISTER_V1.md` + `PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md`  
**Purpose:** determine whether the code solves the declared mathematics correctly before any validation or H1/H2 interpretation.  
**Rule:** verification failure blocks validation. No failed test may be removed because its result is inconvenient.

---

## 0. Evidence/application rule

```math
\boxed{
\text{GENERAL V\&V PRINCIPLE}
\rightarrow
\text{DECLARED EQUATION/MECHANISM}
\rightarrow
\text{LIMIT/INVARIANT}
\rightarrow
\text{NUMERICAL TEST}
\rightarrow
\text{PASS/FAIL}.
}
```

NASA-STD-7009B treats verification as a credibility activity in the M&S lifecycle. ASME VVUQ terminology distinguishes verification—solving/implementing the mathematical model correctly—from validation—adequately representing the real-world system for a context of use. The exact tolerances below are thesis-specific `[P]` unless explicitly sourced.

Claim tags:

```text
[E] general external V&V/software evidence;
[P] preregistered test/tolerance;
[D] derived expected consequence of the declared mathematics;
[A] modeling assumption;
[U] unresolved until execution.
```

---

# 1. Verification gate logic

Verification proceeds in this order:

```math
\boxed{
\text{environment}
\rightarrow
\text{units/schema}
\rightarrow
\text{component equations}
\rightarrow
\text{dependency limits}
\rightarrow
\text{coupled invariants}
\rightarrow
\text{convergence}
\rightarrow
\text{reproducibility}.
}
```

A scientific result is not generated until all **mandatory** tests applicable to that model variant pass.

For test `V_k`, record:

```math
\mathcal T_k
=
(ID,
object,
setup,
expected,
metric,
tolerance,
PASS/FAIL,
evidence\ artifact).
```

---

# 2. Environment and provenance tests

| ID | Object | Expected result | Metric / rule | Mandatory |
|---|---|---|---|---:|
| V-E01 | OCI runtime | exact frozen Python/OS target built | full OCI digest recorded | yes |
| V-E02 | dependency resolution | all direct/transitive dependencies install from hash-lock | resolver/install returns success; lock SHA recorded | yes |
| V-E03 | package imports | all direct packages import | zero import errors | yes |
| V-E04 | ACN Portal | upstream unit tests pass in frozen environment | 100% tests pass, except explicitly documented upstream network-dependent tests | yes |
| V-E05 | SALib | Morris and Sobol smoke computations execute | finite outputs; no API errors | yes before UQ |
| V-E06 | code state | run uses committed clean working tree | `git status` clean + code SHA recorded | yes |
| V-E07 | data identity | all used raw/processed artifacts match manifest | hashes equal manifest | yes |
| V-E08 | secret hygiene | ACN token absent from repo/logs/artifacts | automated/manual secret scan returns no token | yes |

Failure at V-E01–V-E08 means **NO MODEL EXECUTION ADMITTED AS THESIS EVIDENCE**.

---

# 3. Data and unit tests

## V-D01 — MATPOWER case ingestion

Expected `[D]`:

```text
33 buses;
baseMVA = 10;
baseKV = 12.66;
bus 24 Pd = 0.420 MW;
bus 24 Qd = 0.200 MVAr;
branch 23->24 exists and is initially energized.
```

Pass rule: exact equality for integer/topological fields; floating values agree with frozen source after declared source conversion to `<= 1e-12` absolute tolerance.

## V-D02 — Sioux Falls network ingestion

Expected:

```text
24 nodes;
76 directed links;
B=0.15;
beta=4;
links 9->10 and 10->9 exist.
```

Pass rule: exact structural equality with frozen TNTP source.

## V-D03 — Sioux Falls OD ingestion

Expected:

```text
24 zones;
total published OD flow = 360600.
```

Pass rule:

```math
\left|\sum_{od}q_{od}-360600\right|\le10^{-9}.
```

## V-D04 — ACN timestamp discipline

Every persisted ACN timestamp must be timezone-aware.

Pass:

```text
source parse = UTC/GMT aware;
local analysis conversion = America/Los_Angeles aware;
no naive datetime exists in raw-to-processed pipeline.
```

## V-D05 — ACN daily grid

Every accepted complete day must have

```math
24\times60/5=288
```

5-minute slots.

Zero active demand is encoded as zero, not missing.

## V-D06 — ACN energy reconstruction

For complete validation days:

```math
\epsilon_E(d)
=
\frac{|E_{sim}(d)-E_{data}(d)|}{\max(E_{data}(d),10^{-12})}.
```

Primary pass criterion `[P]`:

```math
\operatorname{median}_{d\in D_{val}}\epsilon_E(d)\le0.01.
```

Also report maximum and 95th percentile; the median criterion does not authorize silent deletion of high-error days.

---

# 4. Power-equation verification

## V-P01 — Branch-flow residual

For every solved branch/time point, compute residuals of the declared branch-flow equations:

```math
r_P,
\quad r_Q,
\quad r_v,
\quad r_\ell.
```

Define

```math
\epsilon_P
=
\max
\left(
\frac{|r_P|}{s_P},
\frac{|r_Q|}{s_Q},
\frac{|r_v|}{s_v},
\frac{|r_\ell|}{s_\ell}
\right),
```

with scales equal to `max(characteristic magnitude, 1e-12)` for the corresponding equation.

Pass `[P]`:

```math
\epsilon_P\le10^{-8}.
```

## V-P02 — Zero-charging limit

Set

```math
P_{ch}(t)=0.
```

Expected:

```math
p_{24}(t)=p_{24}^{base}.
```

All power outputs must equal the no-EV benchmark solution within

```math
10^{-10}
```

relative/absolute scaled tolerance.

## V-P03 — Positive-load sign check

Holding all other inputs fixed, impose

```math
P_{ch}^{(2)}>P_{ch}^{(1)}\ge0.
```

For the radial benchmark operating region, expected mechanism sign:

```math
p_{24}^{(2)}>p_{24}^{(1)}
```

exactly by construction, and the upstream real-power requirement must not decrease.

Bus-24 voltage is expected not to improve under the added positive charging load in the frozen radial case. If it does, flag for equation/sign audit; do not automatically treat this sign expectation as a universal power-system theorem outside the declared benchmark.

## V-P04 — Branch open/close event

Opening branch `(23,24)` must isolate the downstream branch segment represented by the declared topology/event logic; re-closing the same branch with unchanged loads must recover the pre-event network topology exactly.

Pass: topology hash/state vector equals expected event state.

## V-P05 — Solver failure preservation

A nonconvergent power case must return an explicit failure state and remain in the scenario ledger.

Pass: no exception handler converts nonconvergence into a plausible numeric output or silently drops the case.

---

# 5. Transportation-equation verification

## V-T01 — BPR function limits

For every link:

```math
t_a(0)=t_a^0.
```

For

```math
x_a\ge0,
```

with frozen `B_a>0`, `beta_a=4`, expected

```math
t_a(x_a)\ge t_a^0.
```

Pass: analytical unit tests to `1e-12` scaled tolerance.

## V-T02 — Frank-Wolfe convergence

Relative gap criterion:

```math
RG\le10^{-6}.
```

Maximum iterations:

```math
N_{it,T}=5000.
```

Failure to reach the criterion is recorded as verification failure for that traffic solution.

## V-T03 — Flow conservation

At each non-origin/non-destination node, assigned commodity/network flow must satisfy the implemented conservation equations within

```math
10^{-10}
```

scaled tolerance.

## V-T04 — No-closure shortest path

With the base graph, compute the crew route from node 1 to node 10 twice from identical link times.

Pass: route and cost are identical.

## V-T05 — Closure monotonicity under frozen link times

Remove `(9,10)` and `(10,9)` while holding all remaining link costs fixed at the declared state.

Because the feasible path set is reduced,

```math
\mathcal R_T^{closed}\subseteq\mathcal R_T^{base},
```

therefore

```math
T_{crew}^{closed}\ge T_{crew}^{base}
```

or `+infinity` if disconnected.

Pass: inequality holds to numerical tolerance.

## V-T06 — Reopening recovery

Restore the two removed arcs and reuse the same link costs.

Expected:

```math
T_{crew}^{reopen}=T_{crew}^{base}.
```

Pass tolerance:

```math
10^{-12}
```

relative/absolute scaled.

---

# 6. Information-mechanism verification

## V-I01 — Zero-latency identity

For deterministic error-free test input:

```math
\delta_I=0,
\qquad
\varepsilon_I=0.
```

Expected:

```math
\widetilde P_{ch}(t)=\widehat P_{ch}(t).
```

Pass to machine-level float64 tolerance.

## V-I02 — Declared delay operator

For a synthetic impulse/ramp forecast sequence, applying

```math
\delta_I=m\Delta t
```

must shift the signal by exactly `m` 5-minute slots with the declared boundary convention.

Test levels:

```text
0, 5, 15, 30 minutes -> 0, 1, 3, 6 slots.
```

Pass: exact index shift.

## V-I03 — Calibration-only statistics

`mu_daytype,s`, residual distribution and `P_ref` must be functions of `D_cal` only.

Pass: automated dependency/provenance test demonstrates no `D_val` record enters these objects.

## V-I04 — Forecast baseline rule

Before information-dependent coupled tests, the seasonal-slot forecast must satisfy

```math
RMSE_{slot,val}\le RMSE_{persistence,val}.
```

If not, the preregistered slot forecast is rejected as the operational forecast model for Phase 1; the failure is reported and no post-hoc forecast replacement is allowed inside v1.

This is a model-selection gate, not support/rejection of H2.

## V-I05 — Controller bounds

For every state:

```math
0\le u_{ch}^{max}(t)\le\bar P_{site}.
```

Pass: exact bound satisfaction within `1e-12` numerical tolerance.

---

# 7. Organizational/restoration verification

## V-O01 — Additive restoration clock

For the sequential Phase-1 mechanism:

```math
T_{restoration}
=
\tau_{decision}
+\tau_{mobilization}
+T_{crew}
+\tau_{repair}.
```

Pass: computed event time equals the analytical sum within `1e-12` minutes for deterministic test values.

## V-O02 — Zero-delay organizational limit

Set

```math
\tau_{decision}=\tau_{mobilization}=\tau_{repair}=0.
```

Expected:

```math
T_{restoration}=T_{crew}.
```

## V-O03 — No-path guard

If

```math
\mathcal R_T=\varnothing,
```

then

```math
\gamma_O=0
```

and re-energization cannot occur through the declared restoration mechanism.

Pass: no finite restoration event is scheduled until a feasible path exists.

## V-O04 — Organizational monotonicity

Holding `T_crew` fixed, increasing any nonnegative sequential delay must not reduce `T_restoration`.

Test independently for decision, mobilization and repair duration.

---

# 8. Canonical dependency-contract limit tests

## V-C01 — Remove causal operator

For each dependency `e`, set

```math
\Phi_e=0.
```

Expected: the receiving system returns to the corresponding uncoupled/baseline equation while all unrelated equations remain unchanged.

Pass: state/output difference from explicitly coded baseline is `<=1e-10` scaled tolerance for deterministic verification fixtures.

## V-C02 — Guard deactivation

Set

```math
\gamma_e=0.
```

Expected: only that dependency contribution is inactive.

Pass: unrelated dependency contributions and constituent-system laws are unchanged.

## V-C03 — Power-to-transport availability map

Event:

```math
\gamma_{PT}:1\rightarrow0
```

must produce

```math
A_{ch}:1\rightarrow0.
```

Re-energization

```math
\gamma_{PT}:0\rightarrow1
```

must restore

```math
A_{ch}:0\rightarrow1.
```

Pass: exact discrete-state transition at declared event time.

## V-C04 — Transport-to-power load map

Given aggregate charging trajectory `P_ch(t)`, the only direct load injection is

```math
p_{24}(t)=p_{24}^{base}+P_{ch}(t).
```

Pass: no charging load is duplicated at another bus or omitted from bus 24.

## V-C05 — Information-layer ablation

`N0` and `N1` must have identical `F_P`, `F_T`, benchmark parameters and physical dependency operators. Their only intended difference is the information pathway/controller treatment.

Pass: automated configuration diff contains only preregistered I-layer fields.

## V-C06 — Organizational-layer ablation

`N1` and `N2` must preserve identical physical and information equations. Their intended difference is the declared organization/access-to-restoration mechanism.

Pass: automated configuration diff contains only preregistered O-layer fields/guards/events.

---

# 9. Multi-rate and temporal verification

## V-M01 — Event ordering

For equal timestamps, event priority must be explicit and deterministic.

Frozen priority `[P]`:

```text
1. exogenous fault/road-state events;
2. observation/information update;
3. controller update;
4. constituent-system solve;
5. restoration/re-energization event;
6. output recording.
```

No ordering may depend on Python container/hash iteration order.

## V-M02 — Time-step refinement

On the designated verification day, repeat continuous/quasi-static calculations at

```text
Delta t = 5 min
Delta t_ref = 2.5 min
```

where the algorithm supports refinement.

For scalar continuous primary output `z`:

```math
\epsilon_{\Delta t}(z)
=
\frac{|z_{5}-z_{2.5}|}
{\max(|z_{2.5}|,s_z)}.
```

Pass `[P]`:

```math
\epsilon_{\Delta t}(z)\le10^{-3}.
```

Discrete event times fixed by assumptions are excluded from this convergence metric but must retain exact event ordering.

---

# 10. Determinism and stochastic reproducibility

## V-R01 — Deterministic repeat

Run the same deterministic verification fixture twice with identical `R_run`.

Pass:

```math
\frac{|z^{(1)}-z^{(2)}|}{\max(|z^{(2)}|,s_z)}\le10^{-12}
```

for every reported scalar output.

## V-R02 — Seeded stochastic repeat

For stochastic residual resampling/UQ:

```text
same scenario ID + same seed manifest -> same sampled input stream.
```

Pass: sampled arrays are bit-identical inside the frozen container.

## V-R03 — Seed separation

Distinct immutable stochastic experiment IDs must generate distinct derived seeds.

Pass: no collisions in the Phase-1 seed manifest.

---

# 11. Verification evidence artifacts

Every test execution must create a machine-readable record:

```text
verification/results/<run_id>/<test_id>.json
```

containing at minimum:

```text
test_id;
run_id;
code_sha;
data hashes;
environment/lock hashes;
input fixture hash;
expected result;
observed metric;
tolerance;
PASS/FAIL;
timestamp UTC;
error/exception if any.
```

A summary table may be generated, but the individual test records remain the auditable authority.

---

# 12. Phase-1B verification decision

Define

```math
G_V
=
\bigwedge_{k\in\mathcal T_{mandatory}}
\mathbf 1[V_k=PASS].
```

Only if

```math
\boxed{G_V=1}
```

may the workflow advance to calibration/holdout validation.

If any mandatory test fails:

```text
STATUS = VERIFICATION FAILED / VALIDATION BLOCKED.
```

A code correction is allowed, but it creates a new executable code SHA and the complete applicable verification suite must be rerun. Verification fixes do not authorize changes to the frozen scientific hypothesis, benchmark mapping, data window or confirmatory thresholds.

---

# 13. Boundary of validity

Passing this matrix demonstrates only:

> the declared Phase-1 software implementation behaves consistently with its equations, limits, transformations and numerical tolerances inside the frozen computational environment.

It does **not** demonstrate:

```text
- empirical correctness of the P–T coupling magnitude;
- transferability to a real city;
- support for H1 or H2;
- resilience or viability validity;
- novelty of the dependency framework.
```

Those questions belong to validation and later scientific tests.

---

# References

- NASA. (2024). NASA-STD-7009B, *Standard for Models and Simulations*.
- NASA. (2026). NASA-HDBK-7009B, *Implementation Guide for NASA-STD-7009B*.
- ASME. (2022). VVUQ 1, *Verification, Validation, and Uncertainty Quantification Terminology in Computational Modeling and Simulation*.
- ASME. (2009/R2021). V&V 20, *Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer* — used for general V&V reasoning, not as a claim that this P–T model is a CFD application.
