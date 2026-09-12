# Phase 1B — Confirmatory H1/H2 Matrix v1

![Status](https://img.shields.io/badge/status-PREREGISTERED%20CONFIRMATORY%20MATRIX-0969DA)
![Scope](https://img.shields.io/badge/scope-H1%2FH2%20Phase--1-1A7F37)

**Frozen:** 2026-09-12  
**Authority:** `RESEARCH_HYPOTHESES.md` + `PHASE1_EXPERIMENT_SPECIFICATION_V1.md` + `PHASE1_VERIFICATION_TEST_MATRIX_V1.md`  
**Purpose:** fix the exact Phase-1 model contrasts, effect metrics, engineering-significance thresholds, scenario aggregation and falsification logic before final holdout outcomes are inspected.  
**Boundary:** this matrix tests H1/H2 on the bounded semi-empirical demonstrator. It does not exhaust the full thesis hypotheses across all hazards, infrastructures or real cities.

---

## 0. Scientific rule

The confirmatory logic follows

```math
\boxed{
\text{mechanism}
\rightarrow
\text{competing models}
\rightarrow
\text{prespecified outcome}
\rightarrow
\text{engineering effect size}
\rightarrow
\text{scenario aggregation}
\rightarrow
\text{falsification rule}.
}
```

Claim tags:

```text
[E] general scientific/engineering evidence;
[P] preregistered thesis choice;
[D] derived implication;
[A] explicit assumption;
[U] unresolved until execution.
```

The experiment is benchmark-calibrated and semi-empirical. Therefore the primary confirmatory logic is based on **prespecified engineering effect sizes and scenario coverage**, not on treating benchmark days as an unlimited iid population and reporting a single p-value.

---

# 1. Common scenario domain

Let

```math
\Omega_{val}
=
\{\omega_1,\ldots,\omega_{N_{val}}\}
```

be the frozen complete-day holdout scenarios from `D_val` after the preregistered quality filter.

Each scenario contains exactly the same:

```text
ACN holdout charging observations;
33-bus benchmark;
Sioux Falls benchmark;
fault time t0 = 12:00;
benchmark mapping;
solver tolerances;
software/data versions.
```

Only the model mechanism under comparison changes.

The same `omega` must be evaluated under every model in a paired contrast.

---

# 2. Engineering-scale normalization

Different outputs have different units. We therefore do **not** sum raw volts, minutes and kWh.

For output component `j`, define the normalized paired difference

```math
\Delta_j(A,B;\omega)
=
\frac{|Z_j^A(\omega)-Z_j^B(\omega)|}{s_j(\omega)}.
```

The positive scale `s_j` is fixed before results and represents the thesis-specific minimum engineering difference regarded as material for this demonstrator.

These scales are `[P]`, not universal standards.

## 2.1 Common scales

| Output | Symbol | Engineering scale `s_j` | Rationale |
|---|---|---:|---|
| minimum voltage magnitude | `V_min` | `0.01 p.u.` | one percentage-point voltage-magnitude shift |
| voltage-violation duration | `T_Vviol` | `15 min` | three 5-min model intervals |
| unserved EV energy | `E_unserved^EV` | `0.05 E_req(omega)` | 5% of scenario requested EV energy |
| charging service fraction | `Q_mobility^charge` | `0.05` | five percentage-point service shift |
| crew travel time | `T_crew` | `10 min` | material operational travel-time change for bounded demonstrator |
| restoration time | `T_restoration` | `15 min` | one quarter-hour restoration shift |

If

```math
E_{req}(\omega)=0,
```

that scenario is not informative for EV-service contrasts and is excluded **only from the EV-energy component**, not from the scenario itself or other outputs.

---

# 3. Multivariate effect distance

For a prespecified component set `J`, define

```math
D_J(A,B;\omega)
=
\|\boldsymbol\Delta_J(A,B;\omega)\|_\infty
=
\max_{j\in J}\Delta_j(A,B;\omega).
```

Why `[D/P]`:

```text
- every component is first converted to an engineering-significance unit;
- no arbitrary weighted sum is introduced;
- D >= 1 means at least one prespecified output changed by at least one declared meaningful scale;
- all component differences are still reported, so the max norm cannot hide which quantity caused the result.
```

The confirmatory normalized threshold is

```math
\boxed{\delta_1=\delta_2=1}
```

in engineering-scale units.

This does **not** mean H1 and H2 have the same physical threshold; their underlying component scales and outcome sets differ.

---

# 4. Scenario aggregation

Primary aggregation is the paired-scenario median:

```math
\operatorname{Agg}_{\Omega}[D]
=
\operatorname{median}_{\omega\in\Omega_{val}}D(\omega).
```

Reason `[P/D]`: the median limits domination by one unusual charging day while preserving the paired holdout design.

Also report, descriptively,

```math
R_{mat}
=
\frac{1}{|\Omega_{val}|}
\sum_{\omega\in\Omega_{val}}
\mathbf 1[D(\omega)\ge1].
```

`R_mat` is a **scenario-coverage fraction**, not a probability unless a probability model over validation days is independently justified.

## Optional uncertainty interval `[P]`

If

```math
N_{val}\ge21,
```

report a 95% moving-block bootstrap interval for the median using 7-day blocks and 2000 replicates, with bootstrap RNG derived from the frozen seed policy.

This interval is supplementary. The confirmatory decision remains based on the prespecified median effect rule below.

---

# 5. H1 — Dynamic causal physical interdependency

## 5.1 Thesis hypothesis

```text
H1: Under coupled P–T disturbances, explicitly modeling dynamic interdependency mechanisms produces materially different service/physical trajectories from independent or static-coupling representations.
```

Phase 1 tests the **physical-coupling component** of H1 before Stage-5 resilience mathematics.

---

## 5.2 Competing models

```math
\mathscr C_0
=
\text{independent }P+T,
```

with

```math
\Phi_{TP}=0,
\qquad
\Phi_{PT}=0.
```

```math
\mathscr C_1
=
\text{static coupled }P-T,
```

using frozen calibration-period mean charging demand while energized plus the same declared binary feeder-availability mapping.

```math
\mathscr C_2
=
\text{dynamic causal }P-T,
```

using time-varying 5-minute ACN-derived charging demand and the declared power-availability guard.

All non-coupling parameters/equations are identical.

---

## 5.3 H1 isolation fixture

To avoid confounding physical coupling with information/organization, the H1 confirmatory fixture uses:

```text
ideal information: delta_I = 0 and no injected information error;
no road closure;
no decision/mobilization delay;
a common fixed repair duration/event rule across C0/C1/C2;
identical fault timing and charging-day forcing.
```

Thus the contrast isolates

```math
\boxed{
\text{physical dependency representation}
}
```

rather than simultaneously testing I/O layers.

---

## 5.4 H1 outcome set

```math
J_{H1}
=
\{
V_{min},
T_{Vviol},
E_{unserved}^{EV},
Q_{mobility}^{charge}
\}.
```

For baseline

```math
b\in\{0,1\},
```

define

```math
D_b^{H1}(\omega)
=
D_{J_{H1}}
(\mathscr C_2,\mathscr C_b;\omega).
```

---

## 5.5 H1 confirmatory rule

The dynamic model demonstrates a **material Phase-1 representation difference** against baseline `b` when

```math
\operatorname{median}_{\omega\in\Omega_{val}}
D_b^{H1}(\omega)
\ge1.
```

H1 is **supported in the bounded Phase-1 domain** only if the criterion holds against **both** preregistered baselines:

```math
\boxed{
\operatorname{median}D_0^{H1}\ge1
\quad\land\quad
\operatorname{median}D_1^{H1}\ge1.
}
```

H1 is **challenged** if either declared contrast fails its threshold.

Why strict conjunction `[P]`: H1 claims added value relative to both independent and static representations; passing only the weaker independent baseline is insufficient evidence that dynamic causal coupling matters beyond static coupling.

No direction of effect is imposed for H1: the dynamic representation may improve or worsen an output. The confirmatory question is whether it materially changes the declared trajectory/performance quantities.

---

# 6. H2 — Information and organizational mechanisms

## 6.1 Thesis hypothesis

```text
H2: Information degradation and organizational constraints materially alter feasible response and recovery relative to a physical-only representation.
```

Phase 1 decomposes H2 into two **mechanism-identifiable contrasts** rather than collapsing information and organization into one change.

---

# 7. H2-I — Information contribution

## 7.1 Competing models

```math
\mathscr N_0=P+T
```

with dynamic physical coupling, ideal information and immediate organizational availability.

```math
\mathscr N_1=P+T+I
```

adds the frozen information delay/error mechanism and fixed information-dependent test controller while leaving physical equations unchanged.

## 7.2 Confirmatory information treatment

The confirmatory degradation level is frozen as

```math
\boxed{\delta_I=30\text{ min}.}
```

The preregistered levels

```math
0,5,15,30\text{ min}
```

are still run to inspect dose-response behavior, but only 30 min is the primary H2-I contrast. This prevents choosing the most favorable latency after results are visible.

Residual/error draws use only the frozen calibration residual distribution and seed manifest.

## 7.3 H2-I outcomes

```math
J_I
=
\{
V_{min},
T_{Vviol},
E_{unserved}^{EV},
Q_{mobility}^{charge}
\}.
```

Define

```math
D_I(\omega)
=
D_{J_I}(\mathscr N_1,\mathscr N_0;\omega).
```

### H2-I rule

```math
\boxed{
\operatorname{median}_{\omega}D_I(\omega)\ge1
}
```

is required for a material information-layer effect in Phase 1.

Secondary mechanistic diagnostics:

```text
RMSE_I and MAE_I;
controller saturation fraction;
peak charging power;
forecast-vs-persistence performance.
```

These explain the mechanism but do not replace the primary effect rule.

---

# 8. H2-O — Organizational/access contribution

## 8.1 Controlled contrast

Apply the **same** road-closure forcing to both sides of the contrast.

```math
\mathscr N_1
```

contains the physical road state but **does not map road accessibility into restoration timing**; restoration follows the common idealized organizational baseline.

```math
\mathscr N_2=P+T+I+O
```

adds the declared

```math
\text{road accessibility}
\rightarrow
T_{crew}
\rightarrow
T_{restoration}
\rightarrow
\text{re-energization}
```

mechanism with frozen central organizational assumptions.

This keeps the exogenous road closure identical and isolates the **organizational/access dependency**, not the mere existence of a road disruption.

## 8.2 H2-O outcomes

```math
J_O
=
\{
T_{crew},
T_{restoration},
E_{unserved}^{EV},
Q_{mobility}^{charge}
\}.
```

Define

```math
D_O(\omega)
=
D_{J_O}(\mathscr N_2,\mathscr N_1;\omega).
```

## 8.3 Mandatory direction checks

Because the Phase-1 sequential restoration mechanism contains only nonnegative added delays and a reduced feasible route set, the following are mechanistic expectations:

```math
T_{restoration}^{N2}\ge T_{restoration}^{N1},
```

and, during an outage affecting the charging interface,

```math
E_{unserved}^{EV,N2}\ge E_{unserved}^{EV,N1},
```

```math
Q_{mobility}^{charge,N2}\le Q_{mobility}^{charge,N1}.
```

A violated direction check triggers **mechanism/code audit**, not a reinterpretation of H2.

## 8.4 H2-O rule

```math
\boxed{
\operatorname{median}_{\omega}D_O(\omega)\ge1
}
```

and all applicable mandatory direction checks must pass.

---

# 9. Overall H2 decision

Because the scientific hypothesis explicitly names both information and organization, the bounded Phase-1 test uses conjunction:

```math
\boxed{
H2_{P1}\text{ supported}
\iff
\operatorname{median}D_I\ge1
\land
\operatorname{median}D_O\ge1
\land
\text{direction checks pass}.
}
```

If only one mechanism passes, report:

```text
H2 NOT SUPPORTED AS STATED IN PHASE 1;
information component: supported/challenged;
organization component: supported/challenged.
```

Do not rewrite H2 after seeing which component succeeds.

---

# 10. Validation prerequisite

No H1/H2 result is computed unless

```math
G_V=1
```

from the full mandatory verification matrix and the relevant component/data validation gates pass.

In particular:

```text
- ACN replay/energy reconstruction must pass;
- forecast model-selection gate must be resolved;
- all data/software/code hashes must be frozen;
- no holdout retuning is permitted.
```

If verification or required component validation fails, the scientific status is

```text
H1/H2 = NOT TESTED
```

not `unsupported`.

This prevents software/data failure from being misinterpreted as hypothesis falsification.

---

# 11. Uncertainty reporting

For every primary contrast report:

```text
component-wise paired differences;
normalized component effects Delta_j;
scenario distance D;
median D;
scenario coverage R_mat;
optional block-bootstrap interval when N_val >= 21;
uncertainty/sensitivity results for declared epistemic factors.
```

No uncertainty interval may be used to erase a preregistered effect-size failure.

Organizational parameters remain assumed/epistemic in Phase 1 v1. Therefore even if H2-O passes, the allowed conclusion is a **controlled mechanism result**, not field calibration of real restoration organizations.

---

# 12. Multiple-comparison discipline

Primary confirmatory decisions are limited to:

```text
H1: C2 vs C0 and C2 vs C1;
H2-I: N1 vs N0 at delta_I = 30 min;
H2-O: N2 vs N1 under the frozen closure/central assumptions.
```

Other latency levels, UQ scenarios, secondary outputs and plots are explanatory/sensitivity analyses unless explicitly promoted by a future preregistered version.

This avoids selecting favorable contrasts after inspection.

---

# 13. Allowed conclusions

## If H1 passes

Allowed:

> Within the frozen benchmark-calibrated Phase-1 domain, dynamic causal P–T coupling produced engineering-significant differences relative to both independent and static-coupling baselines according to the preregistered multivariate effect criterion.

Not allowed:

```text
- universal superiority of dynamic coupling;
- validation for all real P–T systems;
- proof of cascading resilience theory.
```

## If H2 passes

Allowed:

> Within the frozen Phase-1 demonstrator, explicitly represented information degradation and organizational/access constraints each produced engineering-significant changes under the preregistered mechanism contrasts.

Not allowed:

```text
- field-valid organizational delay estimates;
- universal human/organizational resilience law;
- causal identification from observational city data.
```

---

# 14. Advance rule

Only after:

```math
G_V=1,
```

required component validation succeeds, and H1/H2 results are frozen, may the thesis advance to the next scientific layer:

```math
\boxed{
\mathfrak d_e
\rightarrow
F_{SoS}
\rightarrow
X(t)
\rightarrow
Q(t)
\rightarrow
\text{Stage-5 viability/resilience experiments}.
}
```

Phase 1 results may support, challenge or restrict the dependency model. They do not permit silently redesigning the Stage-2 contract after confirmatory inspection.
