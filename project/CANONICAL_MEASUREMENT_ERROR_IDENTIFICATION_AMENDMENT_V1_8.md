# Canonical Measurement Error, Identification, and Estimator Admission Amendment v1.8 — Bramoullé & Maes Alignment

**Status:** CANONICAL ADDITIVE AMENDMENT TO P1.11.7
**Effective date:** 2026-09-19
**Evidence source:** Yann Bramoullé & Sebastiaan Maes (2026), *Measurement error and peer effects in networks*, Journal of Econometrics 258, 106339, DOI 10.1016/j.jeconom.2026.106339
**Evidence role:** methodological/econometric precedent for measurement error, identification, estimator admission, and finite-sample method verification
**Power–Transportation mechanism authority:** NONE
**Sustainability authority:** NONE
**Seven-stage architecture / RQ / SO / H:** UNCHANGED
**Empirical effect:** NONE

## 1. Central epistemic rule

When an unknown scientific quantity is inferred from observations, the admissible chain is:

~~~math
\boxed{
\text{scientific model}
\rightarrow
\text{measurement model}
\rightarrow
\text{identification}
\rightarrow
\text{estimator admission}
\rightarrow
\text{estimation}
\rightarrow
\text{uncertainty propagation}
\rightarrow
\text{validation}.
}
~~~

Permanent prohibition:

~~~math
\boxed{
\text{data}
\rightarrow
\text{algorithm}
\not\Rightarrow
\text{causal conclusion}.
}
~~~

No estimator, simulator, ML method, optimizer or solver can repair an unidentified scientific quantity merely by returning a number.

## 2. Measurement model

The existing Stage-4 observation model remains authoritative:

~~~math
\boxed{
y_k
=
\Gamma_k h^{m_k}(Y_k^{phys};\theta_H)
+
\nu_k.
}
~~~

The Bramoullé–Maes noisy-regressor model supports the general methodological distinction between latent/true and observed variables; it does not supply the infrastructure-specific observation equation.

Permanent:

~~~math
\boxed{
Y^{phys}
\neq
y
\neq
\widehat Y
\neq
b_t.
}
~~~

## 3. Measurement error can create false apparent coupling

For an empirically estimated cross-system coefficient:

~~~math
\boxed{
\widehat\beta_{P\to T}\neq0
\not\Rightarrow
P\to T.
}
~~~

Likewise:

~~~math
\boxed{
\widehat\theta_e\neq0
\not\Rightarrow
G_2^{causal}(e)=PASS.
}
~~~

Measurement error, common drivers, model misspecification, omitted variables and identification failure remain distinct possible explanations for an apparent cross-system signal.

This strengthens the existing common-cause firewall:

~~~math
\boxed{
P\leftarrow\eta\rightarrow T
\neq
P\rightarrow T.
}
~~~

## 4. Identification is distinct from causal qualification

For a candidate dependency \(e\), Stage 2 asks whether the mechanism is causally defensible.

For an unknown quantity \(\vartheta\) inferred from data, an independent gate asks whether the quantity is identifiable under the declared model/measurement assumptions.

~~~math
\boxed{
G_2^{causal}(e)
\neq
G_{\rm ID}(\vartheta).
}
~~~

Thus the following state is scientifically valid:

~~~math
\boxed{
G_2^{causal}(e)=PASS,
\qquad
G_{\rm ID}(\theta_e)=BLOCKED.
}
~~~

A real mechanism may exist while its magnitude cannot be recovered from the available observations.

## 5. Identification gate

For empirically inferred quantity \(\vartheta\):

~~~math
\boxed{
G_{\rm ID}(\vartheta)
\in
\{PASS,BLOCKED,FAIL,N/A\}.
}
~~~

PASS means identification is established under explicit assumptions, data support and model structure, with sufficient strength for the intended inference.

BLOCKED means identification has not been established, or weak identification prevents the intended claim.

FAIL means the quantity is non-identifiable under the declared design/model/measurement assumptions.

N/A means no empirical identification claim is being made because the quantity is supplied by another qualified route such as authoritative engineering specification, controlled/synthetic truth, independent validated measurement, externally qualified parameter, or an explicitly propagated interval/set without point estimation. N/A does not waive provenance or uncertainty requirements.

## 6. Estimator-admission gate

Estimator selection occurs only after the estimand and identification assumptions are declared.

~~~math
\boxed{
G_{\rm EST}
=
G_{\rm estimand}
\land
G_{\rm assumptions}
\land
G_{\rm ID}
\land
G_{\rm numerical}
\land
G_{\rm uncertainty}
\land
G_{\rm validation}.
}
~~~

Permanent:

~~~math
\boxed{
\text{optimizer convergence}
\neq
\text{scientific identification}.
}
~~~

And:

~~~math
\boxed{
\text{estimator exists}
\not\Rightarrow
\text{estimator admissible for this P--T quantity}.
}
~~~

## 7. No default GMM or 2SLS

Bramoullé and Maes derive GMM/2SLS estimators for a particular linear-in-means social-network model under explicit measurement-error and asymptotic assumptions.

Therefore:

~~~math
\boxed{
\text{their estimator}
\neq
\text{default P--T estimator}.
}
~~~

The transferable rule is:

~~~math
\boxed{
\text{method selection follows structural + measurement + identification assumptions}.
}
~~~

## 8. Conditional Stage-3 parameter readiness

The existing Stage2→3 gate is not replaced.

For a Stage-3 parameter \(\theta_e\) obtained empirically, the meaning of \(G_\theta\) is strengthened:

~~~math
\boxed{
G_{\theta}^{emp}
=
G_{\rm origin}
\land
G_{\rm meas}
\land
G_{\rm ID}
\land
G_{\rm EST}
\land
G_{\mathcal U}
\land
G_{\rm domain}.
}
~~~

If \(\theta_e\) is not empirically estimated, \(G_{\rm ID}\) and \(G_{\rm EST}\) may be N/A but origin/provenance/uncertainty must still pass.

An unidentified point estimate cannot make \(G_\theta=PASS\).

## 9. Identification is cross-cutting, not a new Stage 2.5

This amendment does not insert an eighth stage or reorder the seven-stage architecture.

Identification may be needed in pre-execution calibration for Stage 3, in Stage 4 state/parameter inference, in Stage 5 observational diagnostic inference, or in Stage 6 effect/consequence estimation.

The owner is the scientific object and inference task, not a fixed numerical stage number.

## 10. True graph versus observed graph

For infrastructure structure:

~~~math
\boxed{
\mathcal G^{true}
\neq
\widetilde{\mathcal G}
}
~~~

when topology/crosswalk information is uncertain.

Bramoullé and Maes primarily analyze mismeasured characteristics while treating network structure as observed; they explicitly leave the interaction between mismeasured characteristics and mismeasured links as future work.

Therefore this source does not solve feeder-to-road crosswalk uncertainty, charger-to-bus assignment uncertainty, signal-to-feeder assignment uncertainty, or repair-access mapping uncertainty.

## 11. Network richness does not guarantee identification

~~~math
\boxed{
\mathcal G\text{ observed}
\not\Rightarrow
\vartheta\text{ identifiable}.
}
~~~

And:

~~~math
\boxed{
\text{many nodes}
\not\Rightarrow
\text{sufficient independent information}.
}
~~~

Any network-based identification argument must state its rank/variation/strength conditions or their method-specific equivalent.

## 12. Weak-identification gate

For methods susceptible to weak moments/instruments or analogous weak information:

~~~math
\boxed{
G_{\rm ID-strength}=PASS
}
~~~

requires a prespecified method-appropriate strength diagnostic.

Permanent:

~~~math
\boxed{
\text{numerical convergence}
\neq
\text{identification strength}.
}
~~~

If weak identification materially compromises inference, the parameter/result is BLOCKED for the affected claim ceiling.

## 13. Monte Carlo role

Monte Carlo may support estimator bias/variance verification under a known data-generating process, parameter uncertainty propagation, hazard/scenario sampling when probability semantics are justified, viability/recovery probability estimation when probability semantics are justified, and robustness/sensitivity studies.

Permanent:

~~~math
\boxed{
\text{Monte Carlo method verification}
\neq
\text{empirical infrastructure validation}.
}
~~~

Simulation cannot create missing mechanism evidence or missing identification.

## 14. P1.7 uncertainty ontology remains controlling

The proposed six-label summary

~~~math
(
U_{\rm meas},
U_{\rm struct},
U_{\rm param},
U_{\rm model},
U_{\rm scenario},
U_{\rm numerical}
)
~~~

is retained only as a reporting projection. It does not replace the broader P1.7 two-axis ontology.

Mapping examples:

~~~text
U_meas      -> MEASUREMENT / OBSERVATION
U_struct    -> DEPENDENCY and/or MEASUREMENT and/or MODEL_FORM
U_param     -> PARAMETER / ESTIMATION
U_model     -> MODEL_FORM
U_scenario  -> HAZARD / INITIAL_STATE / DEPENDENCY / other scenario-owned source
U_numerical -> NUMERICAL
~~~

The paper directly supports mainly:

~~~math
\boxed{
U_{\rm meas}
\rightarrow
U_{\rm param}.
}
~~~

## 15. Parameter uncertainty must propagate into Stage 3

A point estimate alone is not the canonical parameter representation when uncertainty is material.

Depending on justified probability semantics:

~~~math
\theta_e
\sim
p(\theta_e\mid\mathcal D,\mathcal M_{\rm meas})
~~~

or use an interval/set/ensemble:

~~~math
\theta_e\in\Theta_e^{U}.
~~~

The representation must follow P1.7 probability semantics.

## 16. Resilience quantities inherit epistemic uncertainty

The physical resilience object remains distinct from its estimated/uncertain evaluation.

Do not redefine the physical metric. Instead propagate uncertainty into the computed resilience result:

~~~math
\boxed{
\mathbb U_{\rho}
=
\mathcal P_{\rho}
\left(
\mathbb U_{\widehat Y},
\mathbb U_{\theta},
\mathbb U_{\eta},
\mathbb U_{\mathbb I},
\ldots
\right).
}
~~~

Probability-valued \(P_{\rm viable}\) and \(P_{\rm recover}\) remain conditional on qualified probability semantics.

## 17. Stage-6 quantity-origin class

Every material intervention/resource/sustainability quantity shall record:

~~~text
DIRECT_MEASURED
DIRECT_ACCOUNTED
SIMULATED
ESTIMATED
INFERRED
DERIVED_COMPOSITE
~~~

A quantity may have a chain of origins, which must be retained.

## 18. Effect-resolution gate

The scalar shorthand "effect size > uncertainty floor" is not universal.

Instead:

~~~math
\boxed{
G_{\rm resolve}(\Delta q)
=
PASS
}
~~~

only when the prespecified uncertainty representation resolves the engineering conclusion required by the claim.

Admissible methods may include interval/set sign robustness, confidence/credible interval criteria, posterior probability criteria, scenario-envelope robustness, decision-regret stability, or sensitivity-based sign stability, when scientifically justified.

Permanent:

~~~math
\boxed{
\text{computed improvement}
\neq
\text{resolved engineering improvement}.
}
~~~

## 19. Extension of the P1.11.7 computation record

Do not create a competing computation object.

Extend the existing record with:

~~~text
measurement_model_id
estimand_id
identification_required
identification_status
identification_assumptions
identification_strength_method
identification_strength_status
estimator_id
estimator_admission_status
parameter_origin_class
quantity_origin_class
measurement_error_model
network_observation_status
weak_identification_diagnostic
uncertainty_lineage
effect_resolution_gate
~~~

## 20. Source boundary

Bramoullé and Maes directly support measurement-error false positives/smearing in their network model, identification under explicit conditions, estimator construction after identification, weak-instrument/moment caution, Monte Carlo finite-sample assessment, and the unresolved extension to mismeasured links.

They do not directly support any specific P–T dependency, infrastructure parameter value, thesis Stage-3 equation, viability/reachability formulation, sustainability scope, or universal estimator family.

## 21. Permanent doctrine

~~~math
\boxed{
\text{COMPUTATION}
=
\text{scientific instrument},
\quad
\text{not scientific authority}.
}
~~~

And:

~~~math
\boxed{
\text{model output}
\neq
\text{physical truth}
\neq
\text{causal evidence}
\neq
\text{decision}.
}
~~~

## 22. Empirical firewall

~~~math
\boxed{
G_{P1.11.8}^{design}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~
