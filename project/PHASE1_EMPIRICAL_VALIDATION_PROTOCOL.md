# Phase 1 — Empirical / Executable Dependency Validation Protocol

![Status](https://img.shields.io/badge/status-PREREGISTERED-0969DA)
![Phase](https://img.shields.io/badge/phase-1%20validation-1A7F37)

**Preregistered:** 2026-09-12  
**Dependency contract:** `CANONICAL_DEPENDENCY_CONTRACT_V1.md`  
**Purpose:** validate whether the revised dependency contract can be parameterized, executed, falsified and linked to measurable Power–Transportation consequences before viability/resilience claims are attempted.  
**Rule:** No confirmatory threshold, model variant, parameter-estimation rule, validation split or primary outcome may be changed after inspecting final confirmatory results without a versioned amendment.

---

## 1. Scientific transition

Phase 0 established a theoretical representation result.

Phase 1 asks whether the representation can survive contact with engineering data and executable models.

The validation chain is

```math
\boxed{
\text{evidence}
\rightarrow
(\mathcal C_e,\Sigma_e,\Pi_e)
\rightarrow
\Xi_e
\rightarrow
\Delta X
\rightarrow
\Delta Q.
}
```

The scientific objective is not to obtain the most complex coupled simulation. It is to determine whether a small set of declared dependencies is identifiable, executable, falsifiable and predictive enough to justify later resilience/viability analysis.

---

## 2. Phase-1 research questions

### `RQ1-P1` — Physical dependency validity

Can a feeder-to-fast-charging-station dependency be parameterized so that the coupled model predicts charging-power/availability and mobility consequences more accurately than uncoupled or static-coupling baselines over the declared validation domain?

### `RQ1-P2` — Information-mediated dependency validity

Does adding measured/declared forecast quality and latency improve prediction of the power-side control trajectory relative to models that omit or idealize the information pathway?

### `RQ1-P3` — Organizational/restoration dependency validity

Can road accessibility, authority/resource state and crew-routing constraints explain and predict restoration timing sufficiently to distinguish an organizational/restoration dependency from a purely physical network model?

### `RQ1-P4` — Contract adequacy

Across the three dependency classes, can

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)
```

represent the mechanism without case-specific structural modification?

---

## 3. Minimum executable dependency set

The Phase-1 validation laboratory is restricted to three mechanisms.

### `D_P` — physical Power-to-Transportation

```math
P_{feeder}
\rightarrow
T_{FCS}.
```

### `D_I` — information-mediated Transportation-to-Power

```math
T_{EV\ forecast}
\rightarrow
P_{controller}.
```

### `D_O` — organizational/restoration Transportation-to-Power

```math
T_{road/access}
\rightarrow
P_{crew/restoration}.
```

No fourth mechanism is added in Phase 1 unless a declared consistency test demonstrates that one of the three cannot exercise a required part of the canonical contract.

---

## 4. Common constituent-system physics

The physical infrastructure states remain distinct:

```math
\dot x_P
=
F_P(x_P,u_P,h_P;\vartheta_P),
```

```math
\dot x_T
=
F_T(x_T,u_T,h_T;\vartheta_T),
```

with

```math
\boxed{F_P\neq F_T}
```

in general.

Cross-domain dependence enters only through declared coupling terms or hybrid transitions.

The canonical continuous form is

```math
\dot x_r
=
F_r(x_r,u_r,h_r;\vartheta_r)
+
\gamma_e
\Phi_e(x_s,x_r,\zeta_e,\nu;\theta_e).
```

For event-driven dependencies, use

```math
x_r^+
=
\Psi_e(x_s,x_r,\zeta_e,\nu;\theta_e)
```

under the declared guard `gamma_e`.

---

## 5. Physical dependency model `D_P`

### 5.1 Interface object

```math
\mathcal C_{P}
=
(P_{feeder},p_P,T_{FCS},p_T,\chi_P),
```

where `chi_P` denotes electrical-power availability/capability at the charging interface.

### 5.2 Minimal power-side quantity

At the charging connection,

```math
P_{net}(t)
=
P_{base}(t)+P_{ch}(t).
```

A minimal aggregate charging representation is

```math
P_{ch}(t)
=
\sum_{n=1}^{N_{EV}}
\chi_n(t)p_n(t).
```

Where distribution-network fidelity is required, the feeder equations must be chosen explicitly before calibration, for example an AC power-flow/DistFlow/DAE model consistent with the available validation data.

### 5.3 Transport-side charging service

A minimal FCS queue relation is

```math
\dot n_q(t)
=
\lambda_{EV}(t)-\mu_{FCS}(t),
```

with charging service rate dependent on available charging power/capacity through the declared `Phi_P`.

### 5.4 Candidate causal operator

```math
\Phi_P:
(x_P,x_T;\theta_P)
\mapsto
\Delta \mu_{FCS}
```

or an equivalent validated mapping from electrical state/capacity to charging availability and transport service.

The exact functional form is **not frozen here**; the candidate family and selection criterion must be frozen before final calibration.

---

## 6. Information dependency model `D_I`

### 6.1 Interface object

```math
\mathcal C_I
=
(T_{EV\ forecast},p_I^s,P_{controller},p_I^r,\chi_I),
```

where `chi_I` is the forecast/information signal.

### 6.2 Measurement / forecast relation

Let

```math
\widehat d_{EV}(t)
=
d_{EV}(t)+\varepsilon_I(t),
```

with latency

```math
\widehat d_{EV}^{obs}(t)
=
\widehat d_{EV}(t-\delta_I).
```

### 6.3 Control dependence

```math
u_P(t)
=
\pi_P\!\left(
x_P(t),
\widehat d_{EV}^{obs}(t);
\theta_I
\right).
```

The information dependency is demonstrated only if changes in forecast error/latency cause reproducible changes in the receiving control/action trajectory under otherwise controlled conditions.

---

## 7. Organizational/restoration dependency model `D_O`

### 7.1 Interface object

```math
\mathcal C_O
=
(T_{road/access},p_O^s,P_{crew/restoration},p_O^r,\chi_O),
```

where `chi_O` denotes feasible access/authority/resource availability rather than a physical flow.

### 7.2 Feasible-route set

Let

```math
\mathcal R_T(t)
```

be the set of feasible crew routes under current transport and authorization conditions.

A minimal travel-time functional is

```math
T_{travel}(t)
=
\min_{r\in\mathcal R_T(t)}
\sum_{a\in r} t_a(x_T(t)).
```

### 7.3 Response-time decomposition

For sequential non-overlapping response activities,

```math
\begin{aligned}
T_{response}
={}&
\tau_{decision}
+\tau_{coordination}
+\tau_{mobilization}\\
&+T_{travel}
+\tau_{repair}.
\end{aligned}
```

If activities overlap, Phase 1 must use the corresponding critical-path completion time rather than an arithmetic sum.

### 7.4 Hybrid mechanism

An admissible form is

```math
\gamma_O(t)
=
\mathbf 1_{\{\mathcal R_T(t)\neq\varnothing\}}
\mathbf 1_{\{A_O(t)=1\}},
```

where `A_O` represents the declared authorization/organizational condition.

The exact organizational state model must remain interpretable and parameterized from evidence rather than tuned as a generic resilience coefficient.

---

## 8. Confirmatory model families

### H1 family — dynamic interdependency

```math
\mathscr C_0
=
\text{independent }P+T,
```

```math
\mathscr C_1
=
\text{static coupled }P\text{--}T,
```

```math
\mathscr C_2
=
\text{dynamic causal coupling using the canonical dependency contract}.
```

The distinction between `C1` and `C2` must be frozen at the mechanism level, not merely through different parameter values.

### H2 family — information and organization

```math
\mathscr N_0=P+T,
```

```math
\mathscr N_1=P+T+I,
```

```math
\mathscr N_2=P+T+I+O.
```

Each nested model must use the same physical equations and calibration data for components retained across variants.

---

## 9. Primary Phase-1 outcome vector

Before final testing, define the primary output vector as

```math
Z
=
\begin{bmatrix}
L_{service}\\
T_{recovery}\\
E_{state}\\
E_{control}
\end{bmatrix},
```

where:

```text
L_service  = declared integrated service-loss metric;
T_recovery = declared recovery-time metric;
E_state    = state-prediction error over the validation horizon;
E_control  = controller/action trajectory error where relevant.
```

`N_fail` and `P_control` may be retained as secondary outputs when the demonstrator definition supports them unambiguously.

The exact normalization and units must be declared before confirmatory runs.

---

## 10. Confirmatory hypotheses for Phase 1

### `H1-P1`

Dynamic causal coupling changes the declared validation outcome sufficiently relative to both independent and static-coupling baselines:

```math
D_b
=
D\!\left(
Z^{\mathscr C_2},
Z^{\mathscr C_b}
\right),
\qquad b\in\{0,1\}.
```

The confirmatory rule is

```math
D_b\ge\delta_1.
```

`D` and `delta_1` must be frozen after pilot/scoping analysis and before confirmatory evaluation.

### `H2-P1`

Information and organizational degradation materially change feasible control and downstream outcomes:

```math
D\!\left(
Z^{\mathscr N_2},
Z^{\mathscr N_0}
\right)
\ge\delta_2.
```

The incremental contrasts

```math
\mathscr N_1-\mathscr N_0
```

and

```math
\mathscr N_2-\mathscr N_1
```

must also be reported separately.

### Falsification principle

If the richer dependency representation does not improve explanatory/predictive adequacy beyond the declared threshold while increasing complexity, Phase 1 must report that failure rather than reinterpret the result as support.

---

## 11. Parameter and identifiability register

Every calibrated or inferred parameter receives a record before final calibration.

| Field | Required entry |
|---|---|
| symbol | mathematical symbol |
| mechanism | `D_P`, `D_I` or `D_O` |
| physical/operational meaning | exact interpretation |
| units | SI or explicitly declared dimensionless unit |
| prior/source | measurement, standard, literature, engineering assumption |
| estimation method | direct measurement, optimization, Bayesian inference, system identification, bounded calibration |
| calibration data | dataset/time window/scenario |
| validation data | independent dataset/time window/scenario |
| uncertainty representation | standard uncertainty, interval, distribution, ensemble, scenario bound |
| structural identifiability | identifiable / not identifiable / not assessed |
| practical identifiability | strong / weak / unidentifiable under available data |
| sensitivity | local/global measure used |
| epistemic state | value recorded in `Pi_e` |
| freeze status | pilot / frozen / excluded |

No parameter may be classified as `measured` if it was calibrated.

No parameter may be classified as `validated` merely because it was used to fit the calibration data.

---

## 12. Identifiability tests

Where analytically feasible, perform structural-identifiability analysis before numerical estimation.

At minimum, Phase 1 must perform practical identifiability checks using one or more of:

```text
profile likelihood;
posterior concentration / Bayesian diagnostics;
Fisher-information or sensitivity-rank diagnostics;
parameter correlation analysis;
synthetic-data recovery;
repeated-start calibration stability.
```

A parameter is not retained in the confirmatory model merely because an optimizer returns a value.

If two parameters cannot be distinguished with available data, the protocol requires one of:

```text
reparameterization;
fixing one parameter from independent evidence;
reporting an identifiable combination;
removing the parameter/mechanism;
classifying the result as non-identifiable.
```

---

## 13. Verification before validation

The executable model must pass verification before empirical validation results are interpreted.

### 13.1 Dependency-off limit

```math
\Phi_e=0
```

must recover the declared uncoupled model.

### 13.2 Guard-off limit

```math
\gamma_e=0
```

must eliminate the dependency contribution without modifying unrelated subsystem physics.

### 13.3 Zero-delay limit

For delayed mechanisms,

```math
\delta_e\rightarrow0
```

must recover the no-delay formulation.

### 13.4 Conservation / balance checks

Where applicable, verify electrical power balance, vehicle/queue conservation and resource/crew accounting.

### 13.5 Dimensional consistency

Every term in a governing equation must have consistent dimensions.

### 13.6 Numerical verification

At minimum:

```text
solver tolerance study;
time-step refinement;
event-time convergence;
co-simulation communication-step sensitivity if applicable;
repeatability with fixed random seeds;
regression tests for all three dependency-off limits.
```

No empirical fit compensates for failed numerical verification.

---

## 14. Calibration and validation separation

Phase 1 uses an explicit separation between parameter estimation and validation.

Preferred hierarchy:

```text
1. independent benchmark/standard values where available;
2. calibration subset for unknown parameters;
3. validation subset not used in fitting;
4. out-of-regime stress scenarios used only for robustness/extrapolation assessment.
```

If data scarcity prevents a clean holdout set, use a declared blocked cross-validation or leave-one-scenario-out strategy rather than reusing the same observations without correction.

The domain of validation must be stated explicitly:

```math
\Omega_V.
```

Hypothesis claims are restricted to

```math
\Omega_H\subseteq\Omega_V
```

unless extrapolation is separately justified.

---

## 15. Validation metrics

Validation must compare model predictions against independent observations or benchmark outputs for declared quantities of interest.

For scalar/trajectory variable `y`, examples include

```math
RMSE
=
\sqrt{
\frac{1}{N}
\sum_{k=1}^{N}
(\hat y_k-y_k)^2
},
```

```math
MAE
=
\frac{1}{N}
\sum_{k=1}^{N}
|\hat y_k-y_k|,
```

and a normalized error declared before testing.

For multivariate outputs, use a declared multivariate distance or component-wise acceptance rule rather than collapsing unrelated units into an arbitrary scalar.

Validation acceptance thresholds must be tied to engineering use, measurement uncertainty, baseline performance or a prespecified practical tolerance.

---

## 16. Uncertainty quantification

Distinguish at least:

```text
measurement uncertainty;
parameter uncertainty;
input/scenario uncertainty;
model-form discrepancy;
numerical uncertainty;
epistemic uncertainty in whether a dependency exists or is correctly specified.
```

Measurement uncertainty should follow a declared metrological treatment consistent with JCGM/GUM principles where applicable.

For nonlinear uncertainty propagation, Monte Carlo or another justified method may be used.

The uncertainty representation must be propagated to the declared outputs rather than reported only at parameter level.

---

## 17. Sensitivity analysis

Use a staged approach.

### Screening

Use local derivatives, Morris screening or another low-cost method to remove negligible parameters where justified.

### Global analysis

For retained uncertain parameters, use an appropriate global method such as Sobol indices or variance-/distribution-based alternatives when the assumptions are satisfied.

Sensitivity analysis must distinguish:

```text
sensitivity of the physical model;
sensitivity of the dependency mechanism;
sensitivity of the service output.
```

A large sensitivity is not evidence that a parameter is well identified.

---

## 18. Model-form comparison

The model comparison must penalize flexibility conceptually and not reward a richer model solely for fitting calibration data better.

Required contrasts include:

```text
uncoupled vs static coupled;
static coupled vs dynamic causal;
physical-only vs +information;
+information vs +information+organization.
```

Report both goodness-of-fit and out-of-sample validation performance.

Where statistical likelihood models are available, information criteria or predictive log scores may be added, but they do not replace physical plausibility and V&V checks.

---

## 19. Epistemic update rule for `Pi_e`

Each dependency starts Phase 1 with a declared epistemic state.

After verification/calibration/validation, update

```math
\Pi_e=(\mathcal P_e,V_e,\mathcal U_e)
```

according to evidence.

Example progression:

```text
HYPOTHESIZED
-> PARAMETERIZED
-> NUMERICALLY_VERIFIED
-> EMPIRICALLY_SUPPORTED
```

or

```text
HYPOTHESIZED
-> PARAMETERIZED
-> NOT IDENTIFIABLE
```

or

```text
HYPOTHESIZED
-> VALIDATION FAILED.
```

Failure states are retained in the audit trail and are not deleted from the evidence history.

---

## 20. Standards / credibility anchors

Phase 1 adopts the following as methodological anchors where technically applicable:

```text
NASA-STD-7009B — model-and-simulation credibility practices and acceptance criteria;
ASME VVUQ 1-2022 — verification/validation/UQ terminology;
ASME V&V 20-2009 (R2021) — validation comparison and uncertainty concepts where the variable-at-validation-point logic is applicable;
JCGM 100:2008 and JCGM supplements — expression and propagation of measurement uncertainty;
FMI 3.0.2 — executable dynamic-model exchange/co-simulation/scheduled execution if FMUs are used;
ISO 15118-20:2022 — EV/EVSE communication and bidirectional power-transfer message semantics where applicable.
```

These standards provide terminology, interfaces or credibility methods; they do not validate the thesis model automatically.

---

## 21. Reproducibility requirements

Before confirmatory results are accepted, archive:

```text
source code and exact commit;
configuration files;
input datasets or public download instructions;
data preprocessing scripts;
parameter registry;
random seeds;
solver/tool versions;
scenario definitions;
calibration/validation split;
unit tests;
verification outputs;
final result tables generated from code rather than manual transcription.
```

The full result should be reproducible as

```math
\boxed{
\text{data}
\rightarrow
\text{configuration}
\rightarrow
\text{model}
\rightarrow
\text{experiment}
\rightarrow
\text{result}.
}
```

---

## 22. Phase-1 acceptance gates

A dependency is **not** eligible for Phase-2 resilience/viability use unless it passes all applicable gates.

### `P1-G1` — semantic/causal specification

`C_e`, `Sigma_e` and `Pi_e` are complete enough to identify what is being claimed.

### `P1-G2` — dimensional/physical consistency

No governing equation violates units, conservation or declared domain laws.

### `P1-G3` — numerical verification

Solver/timestep/event/co-simulation checks pass declared tolerances.

### `P1-G4` — identifiability

Required parameters are identifiable enough for the intended claim, or uncertainty is explicitly bounded and propagated.

### `P1-G5` — independent validation

Prediction error is within prespecified engineering tolerance on data not used for calibration.

### `P1-G6` — baseline discrimination

The richer dependency model demonstrates prespecified added value over its strongest relevant baseline or the corresponding hypothesis is reported as unsupported.

### `P1-G7` — provenance/auditability

`Pi_e` and the computational provenance are complete enough for another researcher to reproduce the evidence chain.

A failed gate blocks that dependency from confirmatory Phase-2 use unless the protocol is amended and rerun.

---

## 23. Phase-1 stopping rule

Phase 1 is complete when each of `D_P`, `D_I`, `D_O` has one of the following auditable statuses:

```text
VALIDATED FOR DECLARED DOMAIN;
PARTIALLY SUPPORTED / RESTRICTED DOMAIN;
NOT IDENTIFIABLE;
VALIDATION FAILED;
NOT EXECUTABLE WITH AVAILABLE DATA.
```

The project does not need all three dependencies to validate successfully to produce a scientifically useful result.

A failed dependency is itself evidence about framework applicability or data requirements.

---

## 24. Prohibited practices

Phase 1 prohibits:

```text
changing hypotheses after viewing confirmatory outcomes;
using validation data for tuning without relabeling the analysis exploratory;
adding parameters solely to rescue fit;
calling calibration validation;
calling numerical convergence empirical validation;
claiming causal validity from simulator coupling alone;
reporting point estimates without uncertainty where uncertainty is material;
using Phase-2 viability quantities before the underlying Phase-1 dependencies pass their gates.
```

---

## 25. Transition to Phase 2

Only validated/restricted-domain dependencies may enter the resilience/viability experiment.

The transition is

```math
\boxed{
\mathfrak d_e^{validated}
\rightarrow
F_{SoS}
\rightarrow
Y(t)
\rightarrow
Q(t)
\rightarrow
\mathcal V,
\rho,
T_{\mathcal V},
P_{control}.
}
```

Phase 2 then tests resilience/viability hypotheses using the validated mechanism set rather than unverified conceptual links.

---

## 26. Current freeze boundary

This protocol freezes:

```text
three dependency classes;
model-family contrasts;
V&V order;
identifiability requirement;
calibration/validation separation;
Phase-1 gate logic;
prohibition on using unvalidated dependencies in confirmatory viability analysis.
```

It does **not yet freeze**:

```text
specific benchmark network;
final data source;
exact numerical parameter values;
exact thresholds delta_1, delta_2;
exact primary distance D;
exact simulation solver/toolchain.
```

Those items must be frozen in a Phase-1 experiment specification **before final confirmatory runs**.

---

## 27. Immediate next implementation task

The next technical artifact should be a bounded experiment specification containing:

```text
1. exact benchmark Power network;
2. exact benchmark Transportation network;
3. exact FCS placement/interface;
4. exact data source and time resolution;
5. equations for F_P and F_T;
6. candidate functional forms for Phi_P, Phi_I, Psi_O;
7. parameter registry;
8. calibration/validation split;
9. numerical solver/co-simulation architecture;
10. frozen acceptance tolerances and hypothesis thresholds.
```

No simulation results should be treated as confirmatory until that experiment specification is committed.
