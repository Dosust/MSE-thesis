# Global H1–H5 Master Preregistration v1

**Date:** 2026-09-19  
**Status:** CANONICAL GLOBAL PRE-DATA PREREGISTRATION — DESIGN/PROTOCOL  
**Scope:** H1–H5 confirmatory architecture across Stages 3–7.  
**Empirical effect:** none. No hypothesis is adjudicated by this file.  
**Highest hypothesis authority:** \`project/CANONICAL_RQ_SO_HYPOTHESES_V3.md\` @ \`e599ef2233f0e4da6b782a29aecec3799c7974c2\`.

## 1. Purpose

This file freezes, for every hypothesis \(H_i\), the global experiment object:

~~~math
\boxed{
\mathcal H_i
=
(
\text{question},
\text{baseline},
\text{treatment},
\text{held constants},
QOI,
\text{primary endpoint},
\text{materiality},
\text{scenarios},
UQ,
VVUQ,
\text{support},
\text{not-support},
\text{not-tested}
).
}
~~~

It freezes the **comparison logic and anti-bias rules**, not unsupported case values.

## 2. Global adjudication semantics

The thesis-wide final confirmatory states are:

~~~text
SUPPORTED
NOT SUPPORTED
NOT TESTED
~~~

Additional labels such as REPRESENTATION-DISTINGUISHABLE, PARTIAL, INCONCLUSIVE, EXPLORATORY, or NOT YET TESTABLE may be retained as subordinate diagnostic/workflow descriptors, but they do not replace the three global final states.

Permanent rule:

~~~math
\boxed{
\text{failed prerequisite/data/VVUQ gate}
\Rightarrow
\text{NOT TESTED},
}
~~~

not NOT SUPPORTED.

A hypothesis is NOT SUPPORTED only when the preregistered comparison is scientifically valid and executable and its materiality criterion is not met.

## 3. Universal matched-comparison rule

Unless the item is the declared treatment:

~~~math
\boxed{
\text{same relevant initial state}
+
\text{same scenario/hazard}
+
\text{same exogenous inputs}
+
\text{same evidence versions}
+
\text{same numerical accuracy target}
}
~~~

must be preserved across comparator arms.

Where stochastic inputs are shared, use common random numbers/realization IDs when scientifically justified.

## 4. Universal anti-bias rules

After the relevant preregistration freeze:

1. no primary endpoint may change because another metric produces a stronger result;
2. no materiality threshold may be chosen from observed confirmatory effect sizes;
3. no scenario may be removed because it weakens the preferred hypothesis;
4. no treatment/model/intervention may be modified using held-out target performance;
5. baseline/treatment roles may not be swapped after results;
6. calibration, verification, validation and confirmation data roles remain distinct;
7. benchmark/synthetic fixture success is not empirical validation;
8. substantive changes require a versioned amendment that declares whether target results had already been inspected.

## 5. Global scenario firewall

All hypotheses inherit the global scenario identity architecture.

For Stage-3-rooted physical scenarios:

~~~math
\omega_s
=
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
~~~

The same base \(ID_s\) must remain traceable through downstream Stages 4–7 when the physical realization is reused.

Permanent:

~~~math
\boxed{
\omega_s\neq R(\omega_s).
}
~~~

Scenario inputs are not selected from their target results.

---

# 6. H1 — Dynamic causal interdependency

## 6.1 Question

**RQ3:** How, when, and where do accepted interdependency mechanisms evolve and propagate through the coupled system?

Canonical H1:

> Under matched Power–Transportation disturbances and initial conditions, an evidence-grounded dynamic causal coupling representation provides measurable incremental explanatory or predictive information for preregistered cascade, service-loss, spatial-propagation, and recovery outcomes relative to corresponding static-coupling and independent-system representations.

## 6.2 Baseline

Primary rival:

~~~math
\boxed{
M_1=\text{static/algebraic P–T coupling}.
}
~~~

Context/reference:

~~~math
M_0=\text{independent P+T}.
~~~

The primary confirmatory contrast is \(M_2\) versus \(M_1\); \(M_0\) remains an uncoupled reference and nested-limit check.

## 6.3 Treatment

~~~math
\boxed{
M_2=\text{dynamic causal P–T coupling}.
}
~~~

Only dependencies satisfying:

~~~math
\boxed{
\mathbb I_{s,M_2}^{active}
\subseteq
\mathbb I_3^{ready}
}
~~~

may appear as accepted dynamic causal coupling.

Blocked/failed candidate mechanisms cannot be activated merely because an older scenario template contains them.

## 6.4 Held constants

For matched realization \(s\), hold fixed as applicable:

~~~math
\boxed{
Y_{0,s}^{phys},
\mathcal G_{0,s},
\eta_s,
D_s,
\Theta_{shared,s},
u_s^{exo},
T_s,
\xi_s,
\text{native P/T model},
\text{calibration budget},
\text{numerical accuracy target}.
}
~~~

Only the coupling representation under test changes.

## 6.5 QOI

Canonical H1 QOI families:

~~~text
cascade;
service loss;
spatial propagation;
recovery.
~~~

Candidate response vector:

~~~math
Z_1=
[
T_C,
N_{fail},
L_{service},
V_{spatial},
T_{recovery}
]^\top.
~~~

The current operational service-trajectory endpoint also uses \(S_P(t)\) and \(S_T(t)\).

## 6.6 Primary endpoint

Current frozen H1 operational endpoint:

~~~math
D_{PT}^{2,1}(\omega)
=
\frac{1}{T}
\int_0^T
\left[
\left(
\frac{S_P^{M_2}(t)-S_P^{M_1}(t)}{\epsilon_P}
\right)^2
+
\left(
\frac{S_T^{M_2}(t)-S_T^{M_1}(t)}{\epsilon_T}
\right)^2
\right]^{1/2}
dt,
~~~

with population statistic:

~~~math
\boxed{
\Theta_{repr}
=
\mathbb E_{\omega}
[D_{PT}^{2,1}(\omega)].
}
~~~

Held-out predictive validation, if qualified, is a separate H1b validation shell rather than a substitute for H1a.

## 6.7 Materiality

Service-resolution/materiality scales must be independent of M2–M1 target effects:

~~~math
\epsilon_s
=
\max(
u_{eng,s},
u_{obs,s},
u_{num,s}
)
~~~

when defensible engineering tolerance exists.

If \(u_{eng,s}\) cannot be justified, the result may support only a **representation-distinguishable** descriptor, not engineering materiality.

Current decision form:

~~~math
\boxed{
CI_{0.95}(\Theta_{repr})>1
}
~~~

with all verification/robustness conditions passing.

Numerical \(\epsilon_P,\epsilon_T\) values remain **DEFERRED until qualified independently**.

## 6.8 Scenarios

Use the Stage-3 generic scenario schema v2.

Older named H1 families may remain scenario templates, but executable \(M_2\) membership is regenerated from the current readiness ledger.

Final scenario IDs, counts, hazards, active-mechanism memberships and seed manifest remain DEFERRED.

## 6.9 UQ

Required:
- paired scenario/parameter draws;
- separate parameter, hazard, initial-state, mechanism/model-form and numerical uncertainty;
- evidence-traceable distributions/ranges;
- no convenience probability distributions;
- dependence-aware sensitivity when inputs are dependent;
- sampling convergence relative to the frozen decision scale.

## 6.10 VVUQ

Required:
- physical/conservation checks;
- dimensional/unit checks;
- nested limits \(M_2\to M_1\) and \(M_1\to M_0\) where applicable;
- numerical refinement/convergence;
- parameter/identifiability audit;
- equal/matched calibration evidence and budget;
- held-out validation for predictive claims;
- model-form sensitivity when multiple plausible structures remain;
- no apparent M2 advantage obtained through greater physical-constraint violation.

## 6.11 Support

H1 is **SUPPORTED** only if:
1. all prerequisite/readiness/VVUQ gates pass;
2. the matched \(M_2\) versus \(M_1\) comparison executes;
3. the primary materiality criterion is satisfied with required uncertainty support;
4. engineering-materiality language is used only when the \(\epsilon_s\) scales include defensible engineering tolerances.

A detectability-only result may be labeled REPRESENTATION-DISTINGUISHABLE but is not automatically full engineering support.

## 6.12 Not-support

H1 is **NOT SUPPORTED** only if the comparison is valid/executable and the frozen primary materiality criterion is not met.

## 6.13 Not-tested

H1 is **NOT TESTED** if any mandatory prerequisite fails or is unresolved, including:
- no Stage2→3-ready mechanism for the intended M2 test;
- invalid/missing parameterization;
- unmatched comparator setup;
- failed physics/numerical verification;
- unresolved primary threshold construction;
- invalid confirmatory data role;
- insufficient held-out truth for a predictive claim.

Current confirmatory state:

~~~text
H1 = NOT TESTED
~~~

for the current Stage-3 case until its execution/readiness gates close.

---

# 7. H2 — Information, organization and feasible control

## 7.1 Question

**RQ4:** How is the system observed, interpreted, coordinated and controlled?

Canonical H2:

> Under matched physical states and disturbances, changes in information availability and organizational conditions produce measurable differences in state-estimation quality, feasible control actions, response timing, recovery trajectories, and Stage-5 resilience outcomes.

## 7.2 Baseline

Nested reference architecture:

~~~math
\boxed{
\mathscr N_0=P+T.
}
~~~

It is an idealized/reference knowledge-control architecture, not a claim that real systems operate without information.

## 7.3 Treatment

Information contrast:

~~~math
\mathscr N_1=P+T+I,
\qquad
\mathscr N_1-\mathscr N_0=\text{information effect}.
~~~

Organization contrast:

~~~math
\mathscr N_2=P+T+I+O,
\qquad
\mathscr N_2-\mathscr N_1=\text{organization effect}.
~~~

Only prespecified Stage-4 information/organization conditions may differ.

## 7.4 Held constants

Hold matched:
- physical initial state;
- hazard/disturbance;
- physical model and solver;
- qualified physical causal mechanisms;
- physical parameters;
- service requirements;
- non-I/O exogenous conditions/resources except the explicitly manipulated organizational factor;
- scenario/random realization.

## 7.5 QOI

Current candidate family:

~~~math
Z_2
\sim
(
E_{est},
C_{unc},
\Delta AoI,
\tau_{info},
\tau_{decision},
r_U,
\tau_{response},
L_{service},
T_{rec},
P_{viable},
P_{recover}
).
~~~

This covers:
- estimation quality;
- observation latency/completeness;
- feasible-control availability;
- response delay;
- service loss;
- recovery;
- downstream Stage-5 resilience.

## 7.6 Primary endpoint

~~~text
DEFERRED.
~~~

Before confirmatory execution, one primary endpoint (or an explicitly preregistered multivariate rule), its orientation, scenario aggregation, and the logical relationship between the information and organization contrasts must be frozen.

The final H2 design must state prospectively whether the hypothesis is:
- conjunctive across the two primary contrasts; or
- one primary contrast plus a prespecified secondary contrast.

This cannot be decided after viewing results.

## 7.7 Materiality

~~~math
\boxed{
\delta_2=\mathrm{DEFERRED}.
}
~~~

The metric-specific engineering/statistical basis and uncertainty rule must be frozen independently of H2 target outcomes.

## 7.8 Scenarios

Use matched physical base scenarios inherited from the global Stage-3 scenario ID.

Stage-4 conditions may append information/organization variant IDs while preserving the same physical base ID.

No case-specific Austin or Greensboro binding is frozen by this global artifact.

## 7.9 UQ

Keep separately identifiable:
- sensing/measurement uncertainty;
- latency/missingness;
- estimation uncertainty;
- organizational/resource uncertainty;
- demand/hazard uncertainty;
- physical/model-form uncertainty;
- numerical uncertainty.

Organization cannot be represented by an unexplained scalar chosen to manufacture an effect.

## 7.10 VVUQ

Confirmatory H2 requires:
- upstream Stage-3 physical realization qualified for intended use;
- measurement/observation semantics qualified;
- estimator verification and identifiability/adequacy;
- explicit information topology/state/availability distinctions;
- explicit organizational authority/resource/action semantics;
- feasible-control construction verified;
- nested comparator check showing physical model is unchanged across \(\mathscr N_0,\mathscr N_1,\mathscr N_2\) except the declared Stage-4 treatment;
- primary metric and \(\delta_2\) frozen;
- numerical/UQ stability.

## 7.11 Support

H2 is **SUPPORTED** only after the valid matched experiment executes and the prospectively frozen H2 primary rule is satisfied under its uncertainty/VVUQ criterion.

## 7.12 Not-support

H2 is **NOT SUPPORTED** only if the full valid experiment executes and the frozen primary meaningful-effect rule is not satisfied.

## 7.13 Not-tested

H2 is **NOT TESTED** if any mandatory prerequisite is unresolved/failed, including:
- physical baseline not qualified;
- observability/measurement architecture unresolved;
- estimator invalid/unverified where used;
- organizational semantics unsupported;
- feasible-control construction unresolved;
- primary endpoint/contrast logic not frozen;
- \(\delta_2\) not frozen;
- failed VVUQ.

Current state:

~~~text
H2 = NOT TESTED
~~~

---

# 8. H3 — Viability–reachability incremental information

## 8.1 Question

**RQ5:** Under what conditions can critical coupled services remain acceptable or recover under feasible controls and uncertainty, and what additional engineering information do viability and reachability provide?

Canonical H3:

> For the declared Power–Transportation test domain, the combined uncertainty-aware viability–reachability resilience object provides measurable incremental predictive or decision-relevant information about future service maintainability and acceptable recovery beyond prespecified conventional performance/recovery-curve metrics.

## 8.2 Baseline

~~~math
\boxed{
Q_{conv}
=
\{\text{preregistered conventional performance/recovery features}\}.
}
~~~

Equivalent Stage-5 baseline:

~~~math
A_0=R_{curve}.
~~~

## 8.3 Treatment

~~~math
\boxed{
Q_{VRR}=Q_{conv}\cup\mathfrak R_T.
}
~~~

Equivalent full augmented arm:

~~~math
A_4=R_{curve}+\mathfrak R_T.
~~~

Viability-only and reachability-only additions are diagnostic ablations, not the primary H3 treatment.

## 8.4 Held constants

Across baseline and augmented information sets, hold fixed:
- physical state/history;
- disturbance/hazard realization;
- observation information;
- feasible-control semantics;
- control authority/policy family;
- \(K,G_{rec},F_{unsafe}\);
- scenario ID;
- future evaluation label;
- data split;
- downstream prediction/decision task.

Only the Stage-5 information supplied to the prediction/decision model changes.

## 8.5 QOI

Frozen candidate outcome menu:
- future loss of acceptability;
- successful acceptable recovery by deadline;
- warning lead time/time-to-event.

The final primary outcome must follow independently supportable labels and decision needs.

## 8.6 Primary endpoint

~~~math
\boxed{
\Delta Skill
=
Skill(Q_{VRR})-Skill(Q_{conv}).
}
~~~

The primary skill metric is **DEFERRED**, but its pre-data selection rule is frozen:
- proper score if calibrated probabilistic prediction + adequate labels;
- suitable classification/discrimination metric if deterministic/set-valued output + valid labels;
- lead-time/time-to-event metric if event times are reliable but probability calibration is not defensible;
- otherwise H3 remains NOT TESTED.

## 8.7 Materiality

~~~math
\boxed{
\delta_3=\mathrm{DEFERRED}.
}
~~~

Its provenance/selection rule is frozen and it cannot be set from confirmatory H3 effect sizes.

## 8.8 Scenarios

An eligible scenario must have:
- identical physical state and disturbance across arms;
- identical Stage-4 control/information assumptions;
- identical requirement/target/unsafe definitions;
- independently evaluable future outcome;
- no confirmatory-label leakage;
- complete provenance and reproducible scenario ID.

Upstream H1/H2 scenarios are candidate sources, not automatically H3-confirmatory samples.

## 8.9 UQ

Distinguish:
- state-estimation uncertainty;
- future process variability;
- parameter uncertainty;
- model-form sensitivity;
- finite-sample uncertainty;
- numerical approximation error.

Use scenario/robust reporting where probability semantics are not justified.

## 8.10 VVUQ

Confirmatory gate:

~~~math
G_{H3}
=
G_{H1/2}
\land
G_K
\land
G_U
\land
G_{\Pi}
\land
G_{alg}
\land
G_{metric}
\land
G_{\delta_3}
\land
G_{data}.
~~~

Requires verified selected algorithm, frozen state/target/unsafe sets and horizons, qualified uncertainty semantics, frozen policy/control semantics, frozen metric/materiality, and protected development/test separation.

## 8.11 Support

H3 is **SUPPORTED** only if the valid matched comparison executes and:

~~~math
\boxed{
\Delta Skill\ge\delta_3
}
~~~

under the frozen metric, data role, uncertainty and VVUQ rules.

Any interval/confidence requirement used for final adjudication must itself be frozen before confirmatory results.

## 8.12 Not-support

H3 is **NOT SUPPORTED** if all prerequisite gates pass, the qualified test executes, and:

~~~math
\Delta Skill<\delta_3.
~~~

## 8.13 Not-tested

H3 is **NOT TESTED** if any prerequisite model/data/algorithm/metric/materiality gate fails or remains unresolved.

Current state:

~~~text
H3 = NOT TESTED
~~~

---

# 9. H4 — Intervention consequences

## 9.1 Question

**RQ6:** What sustainability requirements follow from resilience diagnosis and from the effectiveness, resource efficiency, and sustainability consequences of candidate interventions?

Canonical H4:

> Across the prespecified intervention and scenario set, engineering interventions that produce meaningful resilience improvement are not equivalent in their sustainability consequence vectors; at least two resilience-effective interventions produce materially different accessibility, energy, carbon, or cost consequences under the declared comparison rule.

H4 tests sustainability-consequence heterogeneity. It does not assume every resilience intervention worsens sustainability.

## 9.2 Baseline

For each intervention consequence:

~~~math
\boxed{
a_0=\text{status-quo / no-intervention baseline}
}
~~~

defines matched changes.

The primary H4 comparison itself is between at least two qualified resilience-effective alternatives, not merely \(a_k\) versus \(a_0\).

## 9.3 Treatment

~~~math
\boxed{
a_k\in\mathcal A_6^{qual}.
}
~~~

Each intervention is a strategic model transformation:

~~~math
\mathfrak M^{a_k}
=
\Phi_a(\mathfrak M^0,a_k).
~~~

Operational control \(u(t)\) is not the treatment:

~~~math
u(t)\neq a_k.
~~~

## 9.4 Held constants

Across intervention arms freeze/share as applicable:

~~~math
\mathcal G,
\mathbb I^{qualified},
F_{\mathcal G}^{m},
Y_0,
\eta,
\mathcal U_{feas},
K,
G_{rec},
F_{unsafe},
FU_6,
\mathcal B_{LC},
H_{LC},
\Omega_6,
\text{data/factor versions}.
~~~

Use common random numbers where justified.

## 9.5 QOI

Mandatory Stage-6 output family:

~~~math
\boxed{
(
\Delta\mathfrak R^{a_k},
\mathcal E_{fx}^{a_k},
\mathcal E_{fy}^{a_k},
\Delta\mathbf J_{sus}^{a_k}
).
}
~~~

Core sustainability vector:

~~~math
\mathbf J_{sus}^{core}
=
[
J_{access},
J_{energy},
J_{carbon},
J_{cost}
]^\top.
~~~

Effectiveness and efficiency are mandatory first-class performance results but do not redefine the primary H4 endpoint.

## 9.6 Primary endpoint

Primary H4 eligibility:

~~~math
\boxed{
\mathcal A_{H4}
=
\mathcal A_R^+
=
\{
a_k:
\Delta\mathcal M_R(a_k)\ge\delta_R
\}.
}
~~~

For \(a_i,a_j\in\mathcal A_R^+\):

~~~math
\boxed{
D_J(a_i,a_j)
=
\max_{q\in\mathcal Q_6}
\frac{
|\Delta J_q(a_i)-\Delta J_q(a_j)|
}{
\delta_{J,q}
}.
}
~~~

Primary H4 condition:

~~~math
\boxed{
\exists a_i,a_j\in\mathcal A_R^+:
D_J(a_i,a_j)\ge1.
}
~~~

## 9.7 Materiality

Two materiality layers are required:

~~~math
\boxed{
\delta_R=\text{meaningful resilience-improvement threshold}
}
~~~

and native-unit consequence thresholds:

~~~math
\boxed{
\delta_{J,q}>0,\quad q\in\mathcal Q_6.
}
~~~

Their numerical values are **DEFERRED** until prospectively justified.

No arbitrary cross-dimension weights are needed for primary H4.

## 9.8 Scenarios

Use the same declared intervention/scenario domain across arms with stable base scenario IDs and identical physical forcing except the intervention.

At least two qualified resilience-effective interventions are required for confirmatory H4.

## 9.9 UQ

Report uncertainty for:

~~~math
\Delta\mathfrak R,
\mathcal E_{fx},
\mathcal E_{fy},
\Delta J_q.
~~~

Probability is used only where probability semantics are justified.

Distributional accessibility/social consequences must not be hidden by favorable aggregate means.

## 9.10 VVUQ

Require:
- upstream Stage1–5 validity;
- physical intervention admissibility;
- consistent functional unit/accounting boundary;
- consequence inventory/factor provenance;
- numerical convergence;
- uncertainty propagation;
- no double counting;
- materiality thresholds frozen independently;
- at least two comparable resilience-effective alternatives;
- matched-effectiveness sensitivity where feasible to test whether consequence heterogeneity is merely intervention-strength confounding.

## 9.11 Support

H4 is **SUPPORTED** if:
1. at least two qualified resilience-effective alternatives exist;
2. the primary \(D_J\) consequence-heterogeneity criterion is met;
3. required UQ/VVUQ passes.

## 9.12 Not-support

H4 is **NOT SUPPORTED** if at least two qualified resilience-effective alternatives exist, the valid comparison executes, and the frozen material-difference criterion is not met.

## 9.13 Not-tested

H4 is **NOT TESTED** if any primary prerequisite fails, including:
- fewer than two qualified resilience-effective alternatives;
- failed physical admissibility;
- invalid functional-unit/accounting comparability;
- missing core consequence data;
- unresolved \(\delta_R\) or \(\delta_{J,q}\);
- failed VVUQ.

Current state:

~~~text
H4 = NOT TESTED
~~~

---

# 10. H5 — Joint resilience–sustainability decision

## 10.1 Question

**RQ7:** What should be changed, where, when and in what sequence to achieve effective, efficient and sustainable infrastructure transformation under feasibility constraints and uncertainty?

Canonical H5:

> Under the declared uncertainty domain and intervention set, incorporating sustainability consequences into resilience-based engineering evaluation produces a materially different admissible or nondominated intervention set, or materially changes decision regret, relative to resilience-only evaluation.

## 10.2 Baseline

~~~math
\boxed{
\mathcal X_R
=
\mathcal X_{common}
+
\mathfrak R
}
~~~

producing:

~~~math
\mathcal A_R^\star.
~~~

## 10.3 Treatment

~~~math
\boxed{
\mathcal X_{R,S}
=
\mathcal X_{common}
+
\mathfrak R
+
\mathbf J_{sus}
}
~~~

producing:

~~~math
\mathcal A_{R,S}^\star.
~~~

Thus the treatment is the inclusion/use of sustainability-consequence information.

Effectiveness and efficiency are common information in both arms and cannot be added to only one arm and attributed to sustainability.

## 10.4 Held constants

Across H5 arms hold fixed:
- intervention universe;
- feasibility/admissibility rules;
- Stage-6 evidence versions;
- effectiveness records;
- efficiency records;
- scenario set;
- uncertainty representation;
- numerical tolerances;
- common normalization for shared quantities;
- decision machinery common to both arms;
- value model, if legitimately used identically.

## 10.5 QOI

Primary decision outputs may include:
- admissible/nondominated decision-set membership;
- set change;
- dominance change;
- regret change;
- robustness/decision stability.

Adaptive/sequential pathways are not primary H5 unless separately activated and preregistered.

## 10.6 Primary endpoint

Primary endpoint is **DEFERRED pending prospective selection** from:
- finite-set change \(D_{\mathcal A}\);
- regret change;
- dominance change;
- another justified decision-change measure consistent with the frozen decision-set construction.

Current candidate for finite sets:

~~~math
D_{\mathcal A}
=
1-
\frac{
|\mathcal A_R^\star\cap\mathcal A_{R,S}^\star|
}{
|\mathcal A_R^\star\cup\mathcal A_{R,S}^\star|
}.
~~~

The selected primary endpoint cannot change after confirmatory target results are inspected.

## 10.7 Materiality

~~~math
\boxed{
\delta_5=\mathrm{DEFERRED}.
}
~~~

The materiality basis must be engineering/statistical/decision-theoretic and prospective.

## 10.8 Scenarios

Use the same admissible candidate set, scenario IDs and uncertainty domain in both H5 arms.

Scenario frequency is not probability unless a probability model is justified.

## 10.9 UQ

Distinguish:
- aleatory uncertainty;
- epistemic uncertainty;
- model-form uncertainty;
- numerical uncertainty;
- requirement uncertainty;
- performance uncertainty;
- value/preference uncertainty.

Risk and deep uncertainty are not interchangeable.

## 10.10 VVUQ

Require:
- complete qualified Stage6→7 handoff;
- feasibility-first candidate filtering;
- frozen decision-set construction;
- frozen primary metric/materiality;
- Pareto/dominance algorithm fixtures;
- regret/robustness fixtures where used;
- scenario/uncertainty semantics;
- admissible-set stability;
- Pareto-membership stability;
- H5 set/regret stability;
- requirement/model/numerical/normalization sensitivity;
- value sensitivity if a value model is used.

## 10.11 Support

H5 is **SUPPORTED** if a valid preregistered comparison executes and the frozen primary material-decision-change criterion is satisfied.

## 10.12 Not-support

H5 is **NOT SUPPORTED** if the valid comparison executes and the frozen material-change criterion is not satisfied.

## 10.13 Not-tested

H5 is **NOT TESTED** if any prerequisite fails/remains unresolved, including:
- insufficient admissible alternatives;
- incomplete Stage6→7 handoff;
- unresolved decision-set construction;
- unsupported uncertainty semantics;
- missing primary metric/materiality;
- failed decision VVUQ/stability.

Current state:

~~~text
H5 = NOT TESTED
~~~

---

# 11. Cross-hypothesis dependency architecture

The confirmatory chain is not logically equivalent to “all previous hypotheses must be supported.”

Rather:

~~~math
\boxed{
\text{downstream execution}
\Rightarrow
\text{upstream objects valid for intended use}
}
~~~

not:

~~~math
\boxed{
H_{i-1}=\text{SUPPORTED}
\Rightarrow
\text{mandatory for }H_i.
}
~~~

A downstream hypothesis may be tested with an upstream model/object whose claim ceiling is adequate even if an upstream incremental-value hypothesis is NOT SUPPORTED, provided the downstream design remains scientifically valid and the resulting claim ceiling is adjusted.

A failed upstream **validity/readiness** gate, however, blocks dependent downstream execution.

## 12. Current pre-data freeze matrix

| H | Stage | Baseline | Treatment | Primary endpoint | Materiality | Current result |
|---|---:|---|---|---|---|---|
| H1 | 3 | M1; M0 reference | M2 dynamic causal coupling | \(\Theta_{repr}\) | independent \(\epsilon_s\); numeric values deferred | NOT TESTED |
| H2 | 4 | \(\mathscr N_0\) | \(\mathscr N_1,\mathscr N_2\) I/O contrasts | DEFERRED | \(\delta_2\) DEFERRED | NOT TESTED |
| H3 | 5 | \(Q_{conv}\) / \(R_{curve}\) | \(Q_{VRR}=Q_{conv}+\mathfrak R_T\) | \(\Delta Skill\), metric branch deferred | \(\delta_3\) DEFERRED | NOT TESTED |
| H4 | 6 | \(a_0\) for deltas; pairwise \(a_i,a_j\in A_R^+\) | \(a_k\) interventions | \(D_J\) consequence heterogeneity | \(\delta_R,\delta_{J,q}\) DEFERRED | NOT TESTED |
| H5 | 7 | \(\mathcal A_R^\star\) | \(\mathcal A_{R,S}^\star\) | set/regret/dominance metric DEFERRED | \(\delta_5\) DEFERRED | NOT TESTED |

## 13. Protected DEFERRED fields

This global freeze does not invent:
- H1 case-specific \(\epsilon_P,\epsilon_T\), final scenario IDs, active mechanism set or held-out events;
- H2 primary endpoint, contrast logic, \(\delta_2\), final I/O case realization;
- H3 selected skill metric, \(\delta_3\), final outcome branch, final test sample;
- H4 \(\delta_R,\delta_{J,q}\), final intervention set/accounting values;
- H5 primary decision-change metric, \(\delta_5\), final decision-set construction, final candidate set;
- any H1–H5 result.

## 14. Amendment rule

Any post-freeze change to:
- baseline;
- treatment;
- primary endpoint/selection rule;
- held constants;
- scenario inclusion/exclusion rule;
- uncertainty semantics;
- materiality rule/value;
- support/not-support/not-tested rule;
- VVUQ prerequisite;

requires a dated versioned amendment declaring:
1. scientific reason;
2. whether target results had already been observed;
3. whether affected analysis becomes exploratory;
4. downstream claims affected.

## 15. Source authority snapshot

| Role | File | Git blob |
|---|---|---|
| H1–H5 canonical meaning | project/CANONICAL_RQ_SO_HYPOTHESES_V3.md | e599ef2233f0e4da6b782a29aecec3799c7974c2 |
| model/experiment validation governance | thesis/00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md | 662439d04ec4297a1c5cbba047fc40c46d17db57 |
| H1 operational preregistration | project/H1_CONFIRMATORY_PREREGISTRATION_V1.md | edb4793c426c06b538f9ef3d857ad06d5c31eaac |
| Stage3 scenario authority | project/stage3/STAGE3_SCENARIO_SCHEMA_V2.md | faba67b66c4468d751dbaf4fbd4cf97fb2b907a8 |
| Stage3 model-selection authority | project/stage3/STAGE3_MODEL_FAMILY_SELECTION_PROTOCOL_V2.md | 4780c6e2c1bcd202a9dd23629aa903d4cbbb0edf |
| current H2 execution protocol | project/stage4/03_cases/greensboro_greenevt_smartds/05_H2/STAGE4_H2_EXPERIMENT_PROTOCOL_V1.md | 8f0595487fbd3b1bfc580bebc33890d67a582684 |
| earlier H2 preregistration / supporting | project/H2_PREREGISTRATION_V1.md | c43353ce943453150702726d07cd2bc4a6d4962c |
| H3 global preregistration | project/H3_PREREGISTRATION_V1.md | adfa4924bc643196eeb97139b4f2e7ffbedf69dc |
| current Stage5 H3 protocol | project/stage5/07_H3/STAGE5_H3_EXPERIMENT_PROTOCOL_V1.md | f00f64c2b1ea01e373d0c428b597427e9f65b4b8 |
| current Stage6 H4 protocol | project/stage6/06_H4/STAGE6_H4_EXPERIMENT_PROTOCOL_V2.md | 4a4f44ac4367014ea7aa63b5c548d6c22799bb57 |
| current Stage7 H5 protocol | project/stage7/STAGE7_H5_PREREGISTRATION_AND_COMPARATOR_PROTOCOL_V2.md | 93996781499c866ef02f455e8fcf9ed429c98fc9 |
| global handoff control | project/global_integration/GLOBAL_STAGE_HANDOFF_MATRIX_V1.md | 711128daad5f150016cf994e1c6da497c3c84bb7 |
| global symbol/ontology control | project/global_integration/GLOBAL_SYMBOL_AND_ONTOLOGY_REGISTRY_V1.md | 6f389265ac6e449e814534a7e61e12918a2224aa |

## 16. Freeze statement

~~~math
\boxed{
G_{P1.3}^{design}=PASS
}
~~~

means only that H1–H5 now have a common, auditable pre-data experimental architecture.

It does not mean any numerical materiality threshold or empirical result has been established.
