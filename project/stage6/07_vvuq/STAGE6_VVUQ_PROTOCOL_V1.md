# Stage 6 VVUQ Protocol v1

## 1. Principle

Verification, validation, uncertainty quantification and value judgment are separate.

\[
\boxed{
\text{verification}
\neq
\text{validation}
\neq
\text{uncertainty propagation}
\neq
\text{normative weighting}
}
\]

## 2. Uncertainty taxonomy

Stage 6 distinguishes at least:

### Aleatory

- hazard occurrence/intensity;
- demand variation;
- traffic variation;
- failure/repair variability;
- operational variability.

### Epistemic

- intervention cost;
- material quantities;
- emission/energy factors;
- service life;
- maintenance frequency;
- construction quantities;
- accessibility model parameters;
- critical-service mappings;
- social/lifecycle inventory gaps.

### Model-form

- power model fidelity;
- traffic model fidelity;
- coupling representation;
- accessibility definition;
- LCA allocation/recycling method;
- lifecycle scenario;
- economic model.

### Numerical

- simulation timestep;
- solver tolerances;
- reduced-model error;
- Monte-Carlo/sampling error.

### Normative/value uncertainty

- stakeholder priorities;
- distributional principles;
- discount-rate policy choices;
- weighting choices;
- acceptable burden thresholds.

Normative uncertainty is not disguised as physical randomness.

## 3. Environmental verification

Required checks:

\[
G_{\rm ENV}
=
G_{\rm unit}
\land
G_{\rm inventory}
\land
G_{\rm boundary}
\land
G_{\rm factor}
\land
G_{\rm allocation}
\land
G_{\rm no-double-count}.
\]

For activity-factor calculations:

\[
J=\sum_r A_r EF_r,
\]

verify units and reproduce selected flows independently.

For lifecycle analyses, perform completeness, sensitivity and consistency checks consistent with ISO 14044 / ISO/TS 14074 interpretation principles.

## 4. Energy/carbon validation

Where possible:

- compare activity quantities against engineering bills of quantities/specifications;
- compare energy use against independent model/output or engineering estimates;
- compare emission factors against authoritative/independent sources;
- test temporal/geographic sensitivity of electricity factors;
- separate average attributional from marginal/consequential electricity factors.

No factor is selected because it produces a preferred intervention ordering.

## 5. Accessibility/social V&V

### Verification

- shortest paths/generalized costs reproduce hand-checkable network cases;
- opportunity counts and impedance functions reproduce known examples;
- group assignments sum consistently;
- no inaccessible OD pair is silently dropped.

### Validation

Where empirical execution later permits:

- travel-time/speed distributions against observed/qualified data;
- OD/demand structure against independent data;
- opportunity/critical-function locations against authoritative sources;
- group/area classifications against declared demographic/geographic data.

Procedural and recognition justice claims require stakeholder/process evidence; they cannot be validated from transport simulation alone.

## 6. Cost V&V

Verify:

\[
PV=
C_0+\sum_y C_y/(1+r)^y.
\]

Freeze:

- currency/base year;
- nominal versus real convention;
- discount rate source;
- cost perspective/bearer;
- escalation assumptions;
- analysis horizon;
- salvage/residual treatment.

Validate major cost quantities against independent bids, estimates, cost databases, utility/agency references or peer-reviewed/industry evidence as appropriate.

## 7. Physical intervention V&V

Before sustainability accounting:

\[
G_{6-PHY}(a_k)=PASS.
\]

Check:

- power flow/energy balance/capacity/voltage/thermal conditions relevant to the model;
- transportation conservation/capacity/connectivity/travel-state conditions;
- interface consistency;
- intervention capacity and service life;
- implementation feasibility;
- nesting/limiting behavior where the intervention magnitude tends to zero.

\[
\boxed{
\mathfrak M^{a_k}
\rightarrow
\mathfrak M^0
\quad
\text{as intervention magnitude}\rightarrow0
}
\]

when mathematically applicable.

## 8. Sampling convergence

If Monte Carlo/ensemble analysis is used, sample size is set by convergence rather than convenience.

For consequence metric \(J_q\), track:

\[
\left|
\widehat \mu_{N}
-
\widehat \mu_{2N}
\right|,
\]

quantile stability, interval width and decision-classification stability.

No fixed sample count is declared universal in this design.

## 9. Sensitivity

Sensitivity analysis targets assumptions capable of changing the engineering conclusion.

Candidates include:

- asset service life;
- grid decarbonization pathway;
- material quantities;
- emission factors;
- discount rate;
- demand growth;
- replacement/repair frequency;
- hazard frequency/intensity;
- accessibility impedance parameters;
- intervention performance.

Screening, local/global sensitivity or scenario methods may be selected according to dimensionality and model cost.

## 10. Uncertainty-aware consequence object

\[
\boxed{
\mathbf J_{\rm sus}(a;\omega,\theta,\mathcal M)
}
\]

where:

- \(\omega\): aleatory scenario;
- \(\theta\): uncertain parameters/inventories;
- \(\mathcal M\): model-form choices.

Report expected values only if the probability model is justified.

Otherwise report intervals, scenario envelopes, robust dominance or coverage.

## 11. Decision-stability diagnostic

Stage 6 does not make the final decision, but it should report whether consequence classifications change under plausible uncertainty.

For requirement \(r_q\), define:

\[
Z_q(a,\xi)
=
1[J_q(a,\xi)\text{ satisfies }r_q].
\]

Report robustness/coverage of \(Z_q\) under the justified uncertainty representation.

## 12. Claim rule

No Stage-6 result is promoted from calculated to validated solely because it has many significant digits.

Every result must retain:

\[
\boxed{
\text{estimate}
+
\text{uncertainty}
+
\text{boundary}
+
\text{provenance}
+
\text{validation domain}.
}
\]
