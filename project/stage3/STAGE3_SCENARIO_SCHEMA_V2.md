# Stage 3 — Generic Scenario Schema v2

**Status:** CANONICAL STAGE-3 SCENARIO SCHEMA  
**Effective date:** 2026-09-19  
**Purpose:** define a stable matched-scenario object before case-specific hazard values, seeds or mechanism sets are frozen.  
**Effect on current Level-2 scenario matrix:** semantic supersession only; the existing matrix remains provenance and is not authorized for causal execution until versioned against current Stage2→3 readiness.

## 1. Scenario object

\`\`\`math
\boxed{
\omega_s=
(
ID_s,
R_s,
Y_{0,s}^{phys},
\mathcal G_{0,s},
\eta_s,
D_s,
\Theta_s,
m_{0,s},
\mathbb I_s^{active},
u_s^{exo},
T_s,
\xi_s,
\mathcal M_s
).
}
\`\`\`

| Field | Meaning |
|---|---|
| \(ID_s\) | immutable/versioned scenario identifier |
| \(R_s\) | scenario role |
| \(Y_{0,s}^{phys}\) | physical initial state |
| \(\mathcal G_{0,s}\) | initial topology |
| \(\eta_s\) | hazard/environmental forcing |
| \(D_s\) | demand/exogenous operating conditions |
| \(\Theta_s\) | parameter realization/reference |
| \(m_{0,s}\) | initial mode |
| \(\mathbb I_s^{active}\) | active mechanisms |
| \(u_s^{exo}\) | prescribed matched operational input |
| \(T_s\) | horizon/timing record |
| \(\xi_s\) | stochastic realization/seed identifier |
| \(\mathcal M_s\) | comparator/model/ablation label |

## 2. Stable identity across comparators

For matched H1 realization \(r\),

\`\`\`math
\boxed{
\omega_r^{M_0}
\equiv
\omega_r^{M_1}
\equiv
\omega_r^{M_2}
}
\`\`\`

for all prespecified quantities other than the coupling representation under test.

A model label must never silently change the underlying hazard, demand, initial condition or random realization.

## 3. Comparator semantics

### M0 — independent

\`\`\`math
\mathbb I_{s,M_0}^{active}=\varnothing
\`\`\`

for cross-system coupling.

### M1 — static/algebraic comparator

M1 uses a declared static P–T coupling abstraction. It is a comparator, not evidence that a blocked dynamic causal mechanism is qualified.

### M2 — dynamic causal coupling

\`\`\`math
\boxed{
\mathbb I_{s,M_2}^{active}
\subseteq
\mathbb I_3^{ready}.
}
\`\`\`

No Stage2→3 BLOCKED or FAIL mechanism may appear as accepted dynamic causal coupling.

## 4. Mechanism-gated construction

\`\`\`text
Stage2→3 PASS    -> eligible for M2 inclusion
Stage2→3 BLOCKED -> excluded from accepted M2 execution
Stage2→3 FAIL    -> excluded; historical audit only
\`\`\`

A template may contain a placeholder for an unresolved candidate, but the executable active set must be generated from the current readiness ledger.

## 5. Ablation semantics

Let

\`\`\`math
\mathbb I_3^{ready}=\{d_1,\ldots,d_k\}.
\`\`\`

Then a mechanism ablation is

\`\`\`math
\mathbb I^{(-j)}
=
\mathbb I_3^{ready}\setminus\{d_j\}.
\`\`\`

This replaces hard-coded all-mechanism labels with a version-stable rule linked to the actually admitted mechanism set.

## 6. Hazard record

This schema does not freeze a hazard type, magnitude, geometry or probability.

Every hazard realization must carry:

\`\`\`text
hazard_id
physical variables
units
spatial support
temporal support
source/model
probability interpretation, if justified
uncertainty representation
validity domain
version
\`\`\`

If the scenario set is not generated from a justified probability model:

\`\`\`math
\boxed{
\text{scenario frequency}\neq\text{probability}.
}
\`\`\`

## 7. Randomness and common random numbers

For shared stochastic inputs across matched models:

\`\`\`math
\xi_r^{M_0}
=
\xi_r^{M_1}
=
\xi_r^{M_2}.
\`\`\`

The seed/realization manifest must be frozen before target-result inspection.

A seed is reproducibility metadata, not evidence about the physical distribution.

## 8. Scenario roles

Allowed roles are:

\`\`\`text
VERIFICATION_FIXTURE
SUBSYSTEM_BENCHMARK
COUPLED_SYNTHETIC_BENCHMARK
DEVELOPMENT
HELD_OUT
VALIDATION
CONFIRMATORY
SENSITIVITY
\`\`\`

If one case has multiple roles, the reuse must not violate independence between calibration, validation, held-out evaluation and confirmation.

## 9. Development and held-out cases

Selection must be outcome-blind with respect to target H1 results.

A held-out realistic-synthetic case demonstrates generalization within that synthetic testbed. It is not automatically observational real-world validation.

## 10. Scenario admissibility gate

\`\`\`math
\boxed{
G_{3,SCEN}(s)
=
G_{ID}
\land
G_{role}
\land
G_{input}
\land
G_{mech}
\land
G_{time}
\land
G_{prov}
\land
G_{match}.
}
\`\`\`

- \(G_{ID}\): immutable/versioned ID;
- \(G_{role}\): role declared;
- \(G_{input}\): required fields complete or explicitly DEFERRED at design stage;
- \(G_{mech}\): mechanism set allowed by comparator/readiness;
- \(G_{time}\): timing/horizon semantics complete;
- \(G_{prov}\): provenance complete;
- \(G_{match}\): comparator matching rules satisfied.

## 11. Scenario/result firewall

\`\`\`math
\boxed{
\omega_s
\neq
R(\omega_s).
}
\`\`\`

Scenario inputs are frozen independently of their target results. Any post-result change requires a versioned amendment and disclosure.

## 12. Downstream scenario identity

Where the same physical realization is reused, retain a stable base ID through:

\`\`\`math
S_3\rightarrow S_4\rightarrow S_5\rightarrow S_6\rightarrow S_7.
\`\`\`

Downstream stages may append stage-specific conditions but must preserve traceability to the base physical scenario.

## 13. Current Level-2 matrix status

The existing Level-2 matrix contains candidate mechanisms that no longer satisfy the latest causal/readiness status.

Therefore:

\`\`\`text
CURRENT LEVEL-2 SCENARIO MATRIX
= PROVENANCE / NOT AUTHORIZED FOR CURRENT CAUSAL M2 EXECUTION
\`\`\`

until versioned against this schema and the current readiness ledger.

## 14. Deferred fields

Remain DEFERRED before case/data qualification:

- final case scenario IDs;
- feeder/road identities;
- hazard values;
- parameter draws;
- seed manifest;
- horizon values;
- active mechanism memberships;
- confirmatory scenario counts.

## 15. Claim boundary

A scenario is a controlled experimental condition, not a validated physical future.
