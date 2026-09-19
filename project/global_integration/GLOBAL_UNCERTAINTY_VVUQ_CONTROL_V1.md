# Global Uncertainty / VVUQ Control v1

**Date:** 2026-09-19  
**Status:** CANONICAL GLOBAL PRE-DATA UNCERTAINTY / CREDIBILITY CONTROL  
**Scope:** Stage 3→7 uncertainty, verification, validation, UQ, sensitivity, convergence, decision stability, and claim-ceiling governance  
**Empirical effect:** none.

## 1. Purpose

P1.7 freezes how uncertainty and model credibility are represented and assessed across the full thesis chain.

Permanent firewall:

~~~math
\boxed{
\text{verification}
\neq
\text{validation}
\neq
\text{calibration}
\neq
\text{uncertainty quantification}
\neq
\text{sensitivity analysis}
\neq
\text{decision stability}
\neq
\text{hypothesis adjudication}.
}
~~~

A model may be verified yet invalid for the intended use. A validated component may remain uncertain. A sensitivity ranking does not validate a model. A stable decision does not prove the physical model correct.

## 2. External credibility basis

The global architecture is informed by current authoritative VVUQ sources:

1. ASME VVUQ 1-2022 provides harmonized terminology for verification, validation and uncertainty quantification across computational modeling and simulation [1].
2. ASME VVUQ 50.1-2025 treats V&V as part of the computational-model life cycle, including requirements, development, deployment, use/maintenance and retirement [2].
3. ASME V&V 40-2018 defines a risk-informed model-credibility framework in which required credibility is commensurate with model influence on a decision and consequences of a wrong decision; ASME notes that the framework is general enough to be applied beyond medical devices [3].
4. NASA-STD-7009B establishes M&S credibility requirements tied to intended use and program/project acceptance criteria [4].
5. NASA-HDBK-7009B (2026) provides current implementation guidance for NASA-STD-7009B [5].
6. JCGM 100:2008, with Amendment 1:2026, governs expression of measurement uncertainty; JCGM 101:2008 addresses Monte Carlo propagation of measurement-model distributions [6].
7. NIST states that trustworthy digital twins require V&V and UQ throughout the lifecycle; NISTIR 8620 (2026) identifies VVUQ as a continuing standards/research challenge [7,8].

These sources justify the credibility architecture. They do not validate this thesis model or case.

## 3. Two-axis uncertainty ontology

A central P1.7 rule is:

~~~math
\boxed{
\text{uncertainty nature}
\neq
\text{uncertainty source}.
}
~~~

### 3.1 Nature axis

~~~math
Nature(U_j)
\in
\{
ALEATORY,
EPISTEMIC,
MIXED,
UNRESOLVED
\}.
~~~

- ALEATORY: variability treated as irreducible within the declared model/context.
- EPISTEMIC: lack of knowledge that may be reducible with evidence/model improvement.
- MIXED: both components are scientifically present and not collapsed.
- UNRESOLVED: current evidence is insufficient to classify the nature.

### 3.2 Source axis

~~~math
Source(U_j)
\in
\{
MEASUREMENT,
INITIAL\_STATE,
PARAMETER,
HAZARD,
DEPENDENCY,
OBSERVATION,
ESTIMATION,
INFORMATION,
ORGANIZATION,
MODEL\_FORM,
NUMERICAL,
REQUIREMENT,
INTERVENTION\_PERFORMANCE,
RESOURCE,
ACCOUNTING\_FACTOR,
DECISION\_METHOD,
VALUE\_PREFERENCE,
OTHER
\}.
~~~

Examples:
- parameter uncertainty may be EPISTEMIC, ALEATORY or MIXED;
- measurement uncertainty may combine random and systematic components;
- model-form uncertainty is not parameter uncertainty;
- requirement and value uncertainty are not physical stochastic variability.

## 4. Global uncertainty record

For each uncertainty source:

~~~math
\boxed{
\begin{aligned}
\mathfrak u_j
=(
&UID_j,
Object_j,
Owner_j,
Stage_j,
H_j,
Nature_j,
Source_j,\\
&Representation_j,
Parameters_j,
Dependence_j,
ProbSem_j,
Reducibility_j,\\
&Evidence_j,
CalibrationRole_j,
Propagation_j,
Sensitivity_j,\\
&VerificationLink_j,
ValidationLink_j,
DecisionImpact_j,
ClaimImpact_j,
Validity_j,
Status_j,
Prov_j
).
\end{aligned}
}
~~~

Required semantics:

| Field | Meaning |
|---|---|
| UID | immutable uncertainty ID |
| Object | uncertain quantity/object |
| Owner | scientific owner |
| Stage | first stage where it enters |
| H | affected hypothesis/hypotheses |
| Nature | ALEATORY/EPISTEMIC/MIXED/UNRESOLVED |
| Source | source class from §3.2 |
| Representation | distribution/interval/set/ensemble/covariance/model family/etc. |
| Parameters | bounds/distribution parameters/model alternatives if justified |
| Dependence | joint/dependence structure |
| ProbSem | probability semantics status |
| Reducibility | REDUCIBLE/PARTLY_REDUCIBLE/IRREDUCIBLE_IN_CONTEXT/UNKNOWN |
| Evidence | source/qualification evidence |
| CalibrationRole | calibration/inference relation |
| Propagation | method used to propagate to QOIs |
| Sensitivity | method used to assess importance |
| VerificationLink | related verification evidence |
| ValidationLink | related validation evidence |
| DecisionImpact | effect on Stage-7 decisions if relevant |
| ClaimImpact | claim ceiling affected |
| Validity | domain of uncertainty representation |
| Status | PASS/BLOCKED/FAIL/DEFERRED/N/A |
| Prov | exact provenance/version/hash |

## 5. Global uncertainty object

The thesis-level uncertainty set is:

~~~math
\boxed{
\mathbb U
=
\{
\mathfrak u_1,\ldots,\mathfrak u_m
\}.
}
~~~

For reporting convenience only:

~~~math
\boxed{
\mathbb U
=
(
U_{meas},
U_{IC},
U_{\theta},
U_{\eta},
U_{\mathbb I},
U_{obs/est},
U_{I/O},
U_M,
U_N,
U_{req},
U_{perf},
U_{res},
U_{factor},
U_D,
U_V
)
}
~~~

where the labels indicate source domains, not mutually exclusive probabilistic classes.

No source is forced into a probability distribution merely because Monte Carlo is convenient.

## 6. Probability firewall

~~~math
\boxed{
\text{probability}
\Rightarrow
\text{declared random quantity}
+
\text{population/process interpretation}
+
\text{evidence}
+
\text{dependence assumptions}
+
\text{validity domain}.
}
~~~

Permanent:

~~~math
\boxed{
\text{scenario frequency}
\neq
\text{probability},
\qquad
\text{seed}
\neq
\text{distribution evidence}.
}
~~~

If probability semantics are not justified, use intervals, sets, scenarios, model ensembles, envelopes, or other non-probabilistic representations.

Expected utility, expected regret, VaR/CVaR, probabilistic reliability and probabilistic robustness are prohibited unless probability semantics pass.

## 7. Dependence contract

Marginal uncertainty descriptions are insufficient when dependence is material.

~~~math
\boxed{
p(\mathbf u)
\neq
\prod_j p(u_j)
}
~~~

unless independence is justified.

Every joint uncertainty group records:
- dependence group ID;
- physical/epistemic reason;
- correlation/copula/joint sample/set representation if justified;
- evidence;
- sensitivity to dependence assumptions.

Uncertain quantities shared across matched arms must remain matched according to P1.6.

## 8. Reducibility contract

~~~math
\boxed{
\text{uncertainty reduction}
\neq
\text{uncertainty propagation}.
}
~~~

Reduction activities include:
- new measurements;
- improved calibration/identification;
- improved mechanism evidence;
- higher-quality source data;
- better requirement elicitation;
- model refinement where model-form uncertainty is reduced.

Propagation carries remaining uncertainty into QOIs; propagation alone does not reduce uncertainty.

## 9. Context-of-use credibility object

Every model/method credibility claim is tied to a declared context of use:

~~~math
\boxed{
CoU_\ell
=
(
UseID_\ell,
DecisionOrClaim_\ell,
QOI_\ell,
Domain_\ell,
Consequence_\ell,
ModelInfluence_\ell,
CredibilityTarget_\ell
).
}
~~~

The required credibility level must be commensurate with intended use, model influence, and consequence of incorrect use, consistent with the risk-informed logic of ASME V&V 40 and intended-use logic of NASA-STD-7009B [3,4].

No universal scalar credibility score is imposed by P1.7.

## 10. Global VVUQ evidence record

For every credibility activity:

~~~math
\boxed{
\mathfrak v_\ell
=
(
VID_\ell,
Object_\ell,
CoU_\ell,
Class_\ell,
QOI_\ell,
Reference_\ell,
Metric_\ell,
Acceptance_\ell,
UConsidered_\ell,
Evidence_\ell,
Independence_\ell,
Validity_\ell,
Status_\ell,
\Lambda_\ell
).
}
~~~

Allowed activity classes:

~~~text
CODE_VERIFICATION
SOLUTION_VERIFICATION
DATA_PIPELINE_VERIFICATION
CALIBRATION
VALIDATION
UQ_PROPAGATION
SENSITIVITY_ANALYSIS
UQ_CONVERGENCE
CLASSIFICATION_STABILITY
DECISION_STABILITY
CREDIBILITY_ACCEPTANCE
~~~

## 11. Verification hierarchy

### 11.1 Code verification

Question:

~~~math
\boxed{
\text{Did we solve/implement the equations and logic as intended?}
}
~~~

Typical evidence:
- unit/dimensional tests;
- conservation identities;
- analytic solutions;
- sign tests;
- event/reset tests;
- nested limits;
- regression tests;
- deterministic reproducibility;
- algorithm fixtures.

Code verification does not validate physical adequacy.

### 11.2 Solution verification

Question:

~~~math
\boxed{
\text{How large is numerical/discretization/solver/sampling error?}
}
~~~

As applicable:
- timestep refinement;
- spatial/network/grid refinement;
- communication-step refinement;
- event-time sensitivity;
- nonlinear/optimization tolerance refinement;
- stochastic sampling convergence;
- surrogate/emulator error verification.

Numerical error must be assessed relative to the QOI and intended claim, not only raw state error.

### 11.3 Data-pipeline verification

Required where data are transformed into case/model inputs:
- unit conversion;
- CRS/time conversion;
- joins/crosswalks;
- missing-data handling;
- aggregation;
- state reconstruction;
- scenario materialization;
- source/hash/version consistency.

A correct solver with a corrupted data pipeline is not credible.

## 12. Calibration is not validation

~~~math
\boxed{
D_{cal}
\neq
D_{val},
\qquad
\text{calibration fit}
\neq
\text{validation evidence}.
}
~~~

Where independence is required:

~~~math
D_{cal}\cap D_{val}=\varnothing.
~~~

Calibration records must state:
- calibrated parameters;
- calibration data;
- objective/likelihood/loss;
- identifiability;
- prior/constraints if used;
- uncertainty after calibration;
- overfitting/generalization controls.

A parameter fitted to validation/confirmatory targets cannot later be described as independently validated without a new independent dataset.

## 13. Validation contract

Validation asks whether the model/method is adequate for the declared context of use.

Every validation activity must prospectively define:

~~~math
\boxed{
(
CoU,
QOI,
Reference,
Metric,
Aggregation,
Acceptance,
ReferenceUncertainty,
ModelUncertainty,
Independence,
ValidityDomain
).
}
~~~

Validation status:

~~~text
VALIDATED_FOR_DECLARED_USE
NOT_VALIDATED_FOR_DECLARED_USE
NOT_TESTED
~~~

"Validated" without a declared use/domain/QOI is prohibited.

Benchmark agreement or synthetic truth can support verification/synthetic validation but cannot be relabeled empirical validation.

## 14. Validation metric rule

A validation metric must measure the discrepancy relevant to the intended QOI/use.

A small error in an irrelevant variable is not validation of the target claim.

Multivariate validation metrics may be used when justified; ASME VVUQ 20.1-2024 is an available domain-specific reference for multivariate validation concepts, but P1.7 does not mandate it [1].

No validation acceptance threshold may be selected after inspecting confirmatory validation errors.

## 15. UQ propagation contract

Propagation method must match uncertainty semantics.

Allowed methods include:
- analytical propagation;
- Monte Carlo;
- ensemble propagation;
- interval/set methods;
- scenario propagation;
- polynomial/quadrature methods;
- verified surrogate/emulator propagation.

JCGM 101 supports Monte Carlo propagation for measurement models [6]; it does not by itself justify probabilistic semantics for deep uncertainty, requirements, model-form alternatives, or value judgments.

Every propagation record states:
- inputs;
- joint/dependence assumptions;
- method;
- convergence assessment;
- output QOIs;
- numerical error;
- coverage/domain;
- reproducibility identity.

## 16. Sensitivity analysis contract

Sensitivity analysis answers:

~~~math
\boxed{
\text{Which uncertainties materially influence which QOIs/decisions?}
}
~~~

It does not establish truth.

Workflow:

~~~math
\boxed{
\text{screening}
\rightarrow
\text{global/local sensitivity as justified}
\rightarrow
\text{interaction/dependence analysis}
\rightarrow
\text{engineering interpretation}.
}
~~~

Candidate methods include Morris, Sobol/variance-based, derivative/local, moment-independent, scenario ablation, model-family ablation, and decision sensitivity.

Method selection depends on dimension, dependence, computational budget, model regularity, and uncertainty semantics.

## 17. Convergence contract

No universal sample count or tolerance is authorized.

Every convergence protocol freezes prospectively:

~~~text
QOI/statistic
sequence of discretizations/sample sizes
reference/comparison rule
tolerance/materiality basis
repeat/bootstrap rule if used
stopping rule
maximum budget/failure behavior
~~~

Examples:
- numerical refinement;
- Monte Carlo estimator stability;
- viability/reachability set convergence;
- effectiveness classification stability;
- sustainability consequence stability;
- Pareto/admissible-set stability.

## 18. Stage-3 uncertainty/VVUQ

Primary uncertainty domains:

~~~math
\boxed{
\mathbb U_3
=
(
U_{\theta},
U_{IC},
U_{\eta},
U_{\mathbb I},
U_M,
U_N
).
}
~~~

P1.7 preserves the Stage-3 distinction:

~~~math
U_M\neq U_{\theta}.
~~~

Required credibility chain:
- code verification;
- solution verification;
- subsystem validation;
- coupled synthetic benchmark;
- qualified-case validation/reference comparison where available;
- UQ convergence;
- H1 sensitivity/robustness.

H1 cannot be adjudicated when mandatory VVUQ gates remain blocked.

## 19. Stage-4 uncertainty/VVUQ

Stage-4 additions include:

~~~math
\boxed{
(
U_{meas},
U_{missing},
U_{latency},
U_{obs},
U_{\widehat Y},
U_I,
U_O,
U_{\mathcal U_{feas}}
).
}
~~~

Required checks:
- observation/data-pipeline verification;
- estimator numerical verification;
- state-error validation where qualified truth/reference exists;
- uncertainty calibration/coverage where probabilistically meaningful;
- missing/delayed-observation stress tests;
- organization/resource assumption sensitivity;
- control-feasibility classification stability.

Organization uncertainty cannot be encoded as an arbitrary scalar without evidence/meaning.

## 20. Stage-5 uncertainty/VVUQ

Stage-5 adds:

~~~math
\boxed{
(
U_{\Pi_R},
U_K,
U_{G_{rec}},
U_{F_{unsafe}},
U_{alg},
U_{prob},
U_{set}
).
}
~~~

Required:
- reduced-state projection fidelity;
- viability/reachability algorithm verification;
- grid/time/set convergence;
- probability/ensemble convergence where used;
- requirement-threshold sensitivity;
- held-out/qualified-reference validation;
- H3 information-value stability.

Benchmark agreement alone is not Stage-5 validation.

## 21. Stage-6 uncertainty/VVUQ

Stage-6 adds:

~~~math
\boxed{
(
U_{a},
U_{target},
U_{EFX},
U_{resource},
U_{EFY},
U_{boundary},
U_{factor},
U_{J_{sus}}
).
}
~~~

Required:
- physical intervention V&V;
- effectiveness threshold/QOI/aggregation checks;
- resource inventory and efficiency denominator checks;
- lifecycle/accounting boundary audit;
- activity/factor source validation;
- accessibility/energy/carbon/cost UQ;
- double-counting audit;
- classification stability;
- matched-effectiveness/resource sensitivity.

If an efficiency denominator crosses/includes zero, suppress the ratio and report numerator/denominator separately.

## 22. Stage-7 uncertainty/VVUQ

Stage-7 adds:

~~~math
\boxed{
(
U_{decision},
U_{scenario},
U_{normalization},
U_{robustness},
U_{req},
U_V
).
}
~~~

Required:
- algorithm verification;
- admissible/Pareto/regret/set-distance verification;
- scenario aggregation verification;
- input/model validation inheritance;
- requirement-threshold sensitivity;
- model-form/numerical sensitivity;
- normalization sensitivity;
- value/weight sensitivity when a value model exists;
- Pareto/admissible-set/H5 decision stability.

Permanent:

~~~math
\boxed{
\text{risk}
\neq
\text{deep uncertainty}.
}
~~~

Without justified probabilities, use scenario/set/robustness language.

## 23. Cross-stage propagation

An uncertainty source may be transformed but may not silently disappear.

For uncertainty record \(U_j\):

~~~math
\boxed{
U_j^{S_k}
\xrightarrow{\mathcal P_{k\to k+1}}
U_j^{S_{k+1}}
}
~~~

or the handoff must explicitly record:
- resolved/reduced;
- marginalized/aggregated;
- conditionally irrelevant;
- absorbed into another uncertainty object;
- excluded with justification.

Silent dropping is prohibited.

## 24. Hypothesis impact map

### H1
Affected by:
- parameter/IC/hazard/dependency/model-form/numerical/reference uncertainty.

Primary risk:
apparent M2–M1 difference caused by numerical/model-flexibility or unequal calibration rather than dynamic causal information.

### H2
Affected by:
- measurement/missingness/latency/estimation/information/organization/resource uncertainty.

Primary risk:
apparent information/organization benefit produced by unrealistic observation/organization assumptions.

### H3
Affected by:
- state-estimation/model/requirement/algorithm/probability/set-approximation uncertainty.

Primary risk:
apparent viability/reachability benefit produced by threshold/label leakage or numerical set error.

### H4
Affected by:
- intervention-performance/resource/boundary/factor/accessibility/cost/model uncertainty.

Primary risk:
sustainability heterogeneity caused by inconsistent functional units/boundaries or intervention-strength confounding.

### H5
Affected by:
- all inherited uncertainties plus requirement, decision-method, scenario, normalization and value uncertainty.

Primary risk:
decision-set change caused by methodological/value specification rather than sustainability information.

## 25. Hypothesis adjudication rule

For every \(H_i\):

~~~math
\boxed{
G_{H_i}^{VVUQ}=PASS
}
~~~

is required before final SUPPORTED / NOT SUPPORTED adjudication.

If a mandatory VVUQ prerequisite is unresolved:

~~~math
\boxed{
H_i=\text{NOT TESTED},
}
~~~

not NOT SUPPORTED.

## 26. Claim-ceiling rule

For a result \(R\) depending on objects \(O_R\):

~~~math
\boxed{
\Lambda_R
\le
\min_{o\in O_R}
\Lambda_o.
}
~~~

And for downstream stages:

~~~math
\boxed{
\Lambda_{k+1}
\le
\min(
\Lambda_k,
\Lambda_{new,k+1}
).
}
~~~

Numerical precision, large sample size, or stable rankings cannot raise a claim above the weakest required validation/evidence ceiling.

## 27. Decision-stability rule

A Stage-7 decision claim must identify whether the conclusion persists under all prespecified non-target uncertainties.

Decision-stability outputs may include:
- feasible-set membership stability;
- Pareto-membership stability;
- preferred-set/ranking stability if a valid value model exists;
- H5 set-distance stability;
- regret stability;
- robustness-definition sensitivity.

A stable decision over invalid inputs is not a validated decision.

## 28. Credibility acceptance rule

P1.7 does not impose a universal numerical credibility score.

For each context of use, acceptance requires:
- required verification evidence;
- required validation evidence;
- uncertainty representation/propagation;
- sensitivity/convergence;
- credibility target/acceptance rule;
- claim ceiling.

If the required credibility target is not met:

~~~text
NOT ACCEPTED FOR DECLARED USE
~~~

even if individual VVUQ activities pass.

## 29. Global P1.7 gate

~~~math
\boxed{
\begin{aligned}
G_{P1.7}^{design}
={}&
G_{taxonomy}
\land G_{registry}
\land G_{prob}
\land G_{dependence}
\land G_{verification}\\
&\land G_{calibration}
\land G_{validation}
\land G_{propagation}
\land G_{sensitivity}
\land G_{convergence}\\
&\land G_{stage}
\land G_{hypothesis}
\land G_{claim}
\land G_{decision}.
\end{aligned}
}
~~~

Design PASS means the uncertainty/VVUQ architecture is complete. It does not mean any model or hypothesis has passed empirical VVUQ.

## 30. Protected DEFERRED fields

P1.7 does not invent:
- uncertainty distributions/bounds;
- dependence/correlation coefficients;
- sample counts;
- convergence tolerances;
- validation metrics/thresholds not already justified;
- calibration priors/objectives;
- credibility scores;
- model-risk scores;
- decision-stability thresholds;
- H1–H5 results.

## 31. External references

[1] ASME, VVUQ standards portfolio and VVUQ 1-2022 terminology. https://www.asme.org/codes-standards/vvuq-standards  
[2] ASME, VVUQ 50.1-2025 Guide to a Model Life Cycle Approach That Incorporates Verification, Validation, and Uncertainty Quantification. https://www.asme.org/codes-standards/find-codes-standards/vvuq501-vvuq-50-1-guide-to-a-model-life-cycle-approach-that-incorporates-verification-validation-and-uncertainty-quantification  
[3] ASME, V&V 40-2018 Assessing Credibility of Computational Modeling through Verification and Validation. https://www.asme.org/codes-standards/find-codes-standards/assessing-credibility-of-computational-modeling-through-verification-and-validation-application-to-medical-devices  
[4] NASA, NASA-STD-7009B Standard for Models and Simulations. https://standards.nasa.gov/node/263  
[5] NASA, NASA-HDBK-7009B. https://standards.nasa.gov/node/198  
[6] JCGM/BIPM publications, including JCGM 100:2008, Amendment 1:2026 and JCGM 101:2008. https://www.bipm.org/en/committees/jc/jcgm/publications  
[7] NIST, Credibility Consideration for Digital Twins in Manufacturing. https://www.nist.gov/publications/credibility-consideration-digital-twins-manufacturing  
[8] NISTIR 8620, Digital Twins Workshops Summary Report, 2026. https://doi.org/10.6028/NIST.IR.8620

## 32. Repository authority snapshot

- STAGE3_UNCERTAINTY_BENCHMARK_VVUQ_PROTOCOL_V2.md @ 83abc66ff5f5d0f66c421847fa789832ac94ab24
- STAGE4_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md @ 450440fd06088202c1266303cddf9b0e0c2a4c8c
- STAGE4_ESTIMATION_VALIDATION_V1.md @ 864b7a9687d24a680669f08f68a5ae7235815238
- STAGE5_VVUQ_PROTOCOL_V1.md @ 2c62b12bece9d4ab041255c63c040c9efa407639
- STAGE6_VVUQ_PROTOCOL_V2.md @ f050d5d334f2e2a6587785241b30c9ae5606db55
- STAGE7_VVUQ_AND_DECISION_STABILITY_PROTOCOL_V2.md @ dad9344f78260587a2177954c0dee4d033e33a1b
- GLOBAL_FINAL_CASE_UNCERTAINTY_TEMPLATE_V1.md @ 6b579589ad0295a4b997a6ba41a2aedd4973e48d
- GLOBAL_H1_H5_MASTER_PREREGISTRATION_V1.md @ 9b80cb8a2bbb882b53ed5dd3f86d007596e0e9f6
- GLOBAL_SCENARIO_ID_AND_PROPAGATION_SCHEMA_V1.md @ d05039649c0ac69f4c57ae93e178dff077eb0b6e

## 33. Freeze interpretation

~~~math
\boxed{
G_{P1.7}^{design}=PASS
}
~~~

means the uncertainty, VVUQ, credibility and claim-limit architecture is frozen at pre-data design level.

It does not verify or validate any empirical model, case, intervention, decision or hypothesis.
