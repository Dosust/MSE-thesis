# Global Sensitivity / Convergence / Decision-Stability Protocol v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.7 STABILITY CONTROL

## 1. Purpose

P1.7 requires that conclusions remain distinguishable from numerical noise, sampling noise, arbitrary modeling choices, and non-target decision assumptions.

Permanent:

~~~math
\boxed{
\text{sensitivity}
\neq
\text{convergence}
\neq
\text{robustness}
\neq
\text{validation}.
}
~~~

## 2. Sensitivity design

For QOI \(Q\) and uncertain/input/model factor vector \(z\):

~~~math
\boxed{
S_Q=\mathcal S(Q;z,\Omega_z).
}
~~~

Before confirmatory execution, freeze:
- QOI;
- factor set;
- factor ranges/distributions/sets;
- dependence structure;
- method;
- interaction order if relevant;
- ranking/materiality rule;
- computational budget;
- handling of failed runs.

## 3. Method-selection rule

Candidate methods:
- one-at-a-time/local derivative;
- Morris screening;
- Sobol/variance-based;
- moment-independent;
- distributional/global methods;
- mechanism/model-family ablation;
- scenario sensitivity;
- requirement-threshold sensitivity;
- decision-method/value sensitivity.

Method choice depends on:
- stochastic semantics;
- dependence;
- nonlinearity/discontinuity;
- dimensionality;
- computational cost;
- model smoothness;
- decision question.

No universal sensitivity method is mandated.

## 4. Dependence-sensitive analysis

If inputs are dependent, a method assuming independence cannot be used without justification.

~~~math
\boxed{
Dependence\ material
\Rightarrow
Sensitivity\ method\ must\ respect\ or\ explicitly\ test\ it.
}
~~~

## 5. Numerical convergence

For resolution index \(h\) or tolerance/sample sequence \(n\), define a monitored QOI/statistic:

~~~math
Q^{(1)},Q^{(2)},\ldots,Q^{(m)}.
~~~

A convergence protocol freezes:

~~~text
sequence
QOI/statistic
comparison/reference
error/stability measure
acceptance tolerance
stopping rule
maximum budget
failure rule
~~~

The tolerance must be justified relative to engineering/materiality/QOI needs.

## 6. Monte Carlo / ensemble convergence

For estimator \(\widehat\psi_N\):

~~~math
\boxed{
\widehat\psi_{N_1},
\widehat\psi_{N_2},
\ldots
}
~~~

monitor:
- estimator change;
- Monte Carlo standard error/interval where meaningful;
- tail/classification stability;
- rare-event adequacy if claimed;
- sensitivity ranking stability if used.

A large sample count alone is not convergence evidence.

## 7. Set convergence

For viability/reachability/Pareto/admissible sets, candidate diagnostics include:

~~~math
d_H(A_h,A_{h/2}),
~~~

~~~math
\mu(A_h\triangle A_{h/2}),
~~~

membership-switch fraction, or another preregistered set metric.

The metric must fit the dimensionality and scientific claim.

## 8. Classification stability

For classifications such as:
- viable/not viable;
- recoverable/not recoverable;
- effectiveness PASS/FAIL;
- resilience-effective intervention eligibility;
- admissible/nonadmissible decision;

report whether uncertainty or numerical approximation crosses the decision boundary.

If probability semantics are justified, a classification probability may be reported. Otherwise report interval/scenario/set stability.

## 9. H1 stability

Required as applicable:
- M2–M1 endpoint stability to numerical refinement;
- calibration/reference uncertainty sensitivity;
- mechanism ablation;
- model-family sensitivity;
- dependence sensitivity;
- sample convergence.

The H1 conclusion must not depend on one unresolved timestep/model family/seed set.

## 10. H2 stability

Assess:
- measurement-noise sensitivity;
- missingness/latency;
- estimator tuning;
- information topology;
- organization/resource assumptions;
- feasible-control classification.

## 11. H3 stability

Assess:
- state uncertainty;
- \(K,G_{rec},F_{unsafe}\) thresholds;
- projection \(\Pi_R\);
- viability/reachability discretization;
- sampling/probability estimate;
- selected predictive metric.

## 12. H4 stability

Assess:
- \(\delta_R\) eligibility boundary;
- \(\delta_{J,q}\);
- resource/lifecycle boundary;
- emissions/energy/cost factors;
- intervention-performance uncertainty;
- matched-effectiveness band if used.

## 13. H5 decision stability

For decision object \(D\):

~~~math
\boxed{
S_D
=
\mathcal S_D(
D;
\mathbb U_7,
\mathcal M_D,
\mathcal V_7
).
}
~~~

Assess:
- admissible-set stability;
- Pareto-membership stability;
- H5 set-distance/regret/dominance stability;
- scenario-set sensitivity;
- low-confidence-input removal;
- model-form sensitivity;
- numerical sensitivity;
- requirement-threshold sensitivity;
- normalization sensitivity;
- value/weight sensitivity;
- robustness-definition sensitivity.

## 14. Value-model rule

If no defensible value model exists:

~~~math
\boxed{
\text{ranking stability}=\text{N/A},
}
~~~

and the nondominated/admissible set remains the appropriate output.

If weights/preferences exist, sensitivity must reflect their elicitation/validity domain.

## 15. Post-result switching prohibition

After confirmatory target results are seen, do not switch:
- sensitivity method;
- convergence metric;
- stability metric;
- primary QOI;
- threshold;
- scenario exclusion rule;

to obtain a preferred conclusion.

Any such change requires a versioned amendment and affected analysis becomes exploratory unless protected independent confirmation remains.

## 16. Stability claim ceiling

A stable conclusion under a narrow uncertainty domain is stable only within that domain.

~~~math
\boxed{
Stable(D;\Omega_U)
\not\Rightarrow
Stable(D;\Omega'_U\supset\Omega_U).
}
~~~

Stability cannot exceed upstream validity/claim ceilings.
