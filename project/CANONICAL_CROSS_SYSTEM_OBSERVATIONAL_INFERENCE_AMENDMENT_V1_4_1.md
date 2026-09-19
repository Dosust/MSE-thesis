# Canonical Cross-System Observational Inference Amendment v1.4.1 — Acosta-Sequeda Alignment

**Status:** CANONICAL TERMINOLOGY-CORRECTED SUCCESSOR TO v1.4  
**Effective date:** 2026-09-19  
**Supersedes for terminology/current citation:** project/CANONICAL_OBSERVATIONAL_INFORMATIONAL_INTERDEPENDENCY_AMENDMENT_V1_4.md  
**Parent authority:** \`project/CANONICAL_SPATIOTEMPORAL_SOS_RESILIENCE_TRANSFORMATION_LENS_V1.md\`  
**Stage owner:** primarily Stage 4 — observation, estimation, information and feasible action  
**Evidence status:** Acosta-Sequeda et al. (2025), Research Square preprint; preliminary evidence, not peer-reviewed validation  
**Seven-stage architecture:** UNCHANGED  
**RQ1–RQ7 / SO1–SO7 / H1–H5:** UNCHANGED  
**Empirical effect:** NONE

## 0. Terminology correction

The word interdependency is reserved in the thesis for qualified causal dependency/interdependency semantics. This artifact therefore uses cross-system observational inference for the noncausal predictive relation. The scientific firewall and mathematical content of v1.4 are retained.

~~~math
\boxed{\text{cross-system observational inference}\neq\text{causal interdependency}.}
~~~

## 1. Scientific decision

The thesis shall permanently distinguish three relation families:

~~~math
\boxed{
\text{physical/functional causal dependency}
\neq
\text{cross-system observational/predictive relation}
\neq
\text{shared-driver association}.
}
~~~

A predictive relation may improve inference without establishing that the observed source physically causes the predicted receiver.

Permanent:

~~~math
\boxed{
y_P(t)\rightsquigarrow \widehat D_T(t+\tau)
\not\Rightarrow
P\rightarrow T.
}
~~~

The symbol \(\rightsquigarrow\) denotes predictive/informational usefulness without a causal claim.

## 2. Do not overload the canonical dependency set

The repository already uses

~~~math
\mathbb I=\{\mathfrak d_e\}
~~~

for qualified causal dependencies.

Therefore a merely predictive relation shall **not** be stored as \(\mathbb I^{info}\) unless an independently qualified causal information dependency actually exists.

Instead define the Stage-4 observational relation object:

~~~math
\boxed{
\mathfrak o^{obs}_{s\rightsquigarrow r}
=
(
y_s,
\mathcal M^{align}_{s\to r},
\tau_{obs},
\mathcal E_r,
\widehat q_r,
\mathbb U_{obs},
\Omega_{obs},
\Pi_{obs}
).
}
~~~

where:
- \(y_s\): source-system observation or feature;
- \(\mathcal M^{align}\): spatial/temporal/semantic/resolution alignment;
- \(\tau_{obs}\): observational/predictive lag;
- \(\mathcal E_r\): estimator/forecast model;
- \(\widehat q_r\): predicted receiver quantity;
- \(\mathbb U_{obs}\): uncertainty;
- \(\Omega_{obs}\): validity domain;
- \(\Pi_{obs}\): provenance/evidence.

This is not a Stage-2 dependency primitive.

## 3. Shared-driver relation

If two measured processes may respond to a common latent/exogenous driver \(L(t)\), represent conceptually:

~~~math
\boxed{
L(t)\rightarrow y_P(t),
\qquad
L(t)\rightarrow y_T(t+\tau).
}
~~~

Such a structure may explain predictive association without physical \(P\rightarrow T\) causation.

Permanent:

~~~math
\boxed{
\text{association}
\neq
\text{causal effect}.
}
~~~

A shared-driver explanation remains a hypothesis unless the driver and causal structure are independently identified.

## 4. Stage-2 causal firewall

A forecasting association, correlation, lagged feature importance, predictive accuracy gain or spatial co-variation cannot make:

~~~math
G_2^{causal}=PASS.
~~~

A physical/functional dependency still requires:
- directional causal mechanism;
- source/receiver/interface semantics;
- activation/context;
- parameters/delay where applicable;
- evidence;
- uncertainty;
- validity domain.

A predictive paper may motivate a candidate hypothesis but cannot substitute for mechanism evidence.

## 5. Stage-4 cross-system observation

Stage 4 may use observations from one infrastructure to estimate/predict quantities in another:

~~~math
\boxed{
\widehat q_T(t+\tau)
=
\mathcal E_T
\left(
\mathcal I_T^{0:t},
\widetilde y_P^{0:t}
\right).
}
~~~

with:

~~~math
\widetilde y_P
=
\mathcal M_{P\to T}^{align}(y_P).
~~~

This is an information-mediated pathway:

~~~math
\boxed{
P
\xrightarrow{\text{measurement}}
I
\xrightarrow{\text{estimation/prediction}}
\widehat q_T
\xrightarrow{\text{decision}}
u_T.
}
~~~

It is not the same as:

~~~math
P\xrightarrow{\text{physical mechanism}}T.
~~~

## 6. State, demand and observation firewall

For each infrastructure:

~~~math
\boxed{
x_P\neq D_P\neq y_P,
\qquad
x_T\neq D_T\neq y_T.
}
~~~

Interpretation:
- \(x_i\): physical state variables;
- \(D_i\): demand/use process where separately modeled;
- \(y_i\): measured/observed data.

A demand variable may be a state, input, QOI or latent quantity in a particular model, but that role must be declared rather than assumed.

## 7. Observational lag versus physical delay

Permanent:

~~~math
\boxed{
\tau_{obs}
\neq
\delta_e^{phys}
\neq
\tau_i^{info}.
}
~~~

where:
- \(\tau_{obs}\): lag providing predictive/statistical information between signals;
- \(\delta_e^{phys}\): causal propagation delay of a physical/functional mechanism;
- \(\tau_i^{info}\): communication latency where applicable.

An empirically optimal forecast lag may not be interpreted as a physical travel/propagation delay without separate evidence.

## 8. Spatial/temporal alignment before statistical inference

For heterogeneous source and target observations:

~~~math
D_P(\Omega_P,\Delta t_P),
\qquad
D_T(\Omega_T,\Delta t_T),
~~~

the thesis must first declare:

~~~math
\boxed{
\mathcal M_{P\to T}^{align}
=
(
\mathcal M^{space},
\mathcal M^{time},
\mathcal M^{resolution},
\mathcal M^{sem}
).
}
~~~

Only after alignment may the observational/predictive relation be estimated.

The alignment operation remains separate from the forecasting model and from physical causality.

## 9. Spatial heterogeneity

A cross-system observational relationship need not be spatially uniform.

A defensible form may be:

~~~math
\widehat D_T(\mathbf r,t+\tau)
=
F_{\mathbf r}
\left(
D_T^{past},
\widetilde y_P(\mathbf r,t)
\right).
~~~

A citywide coefficient or effect may be used only if aggregation is justified and spatial heterogeneity is not material to the QOI.

## 10. Transportation-mode scope

Evidence concerning bus or rail demand does not automatically generalize to road traffic, freight, repair routing or all Transportation.

Permanent:

~~~math
\boxed{
T_{\rm transit}
\neq
T_{\rm road}
\neq
T_{\rm freight}
\neq
T_{\rm repair/access}.
}
~~~

A claim must retain its mode/population/geography/time validity domain.

## 11. Cross-system information value

Forecast/estimation effectiveness is a Stage-4 information QOI, not resilience itself.

Possible metrics include registered versions of:
- RMSE;
- MAE/MAPE where mathematically appropriate;
- proper scoring rules/probabilistic calibration;
- detection lead time;
- uncertainty reduction.

Conceptually:

~~~math
\boxed{
\mathcal E_{\rm fx}^{info}
=
\mathcal F_{info}
(
\text{baseline forecast/estimate},
\text{cross-system forecast/estimate}
).
}
~~~

Permanent:

~~~math
\boxed{
\text{forecast improvement}
\neq
\text{resilience improvement}.
}
~~~

The resilience pathway requires an additional causal/control chain:

~~~math
\boxed{
\text{better information}
\rightarrow
\text{different/better feasible action}
\rightarrow
\text{changed service trajectory}
\rightarrow
\Delta\mathfrak R.
}
~~~

Each arrow must be tested or bounded.

## 12. Abnormal-regime value must be tested, not assumed

The preprint provides preliminary evidence that cross-system electricity observations improved transit forecasts during a major behavioral regime shift.

For thesis use, an analogous claim requires:
- protected out-of-sample evaluation;
- a preregistered target regime/scenario;
- a target-only baseline;
- a cross-system-information comparator;
- no future leakage;
- spatial/temporal alignment provenance;
- uncertainty and validity reporting.

A single event or city cannot support universal abnormal-regime claims.

## 13. H2 connection

P1.11.4 supplies a possible **information-layer mechanism family** for H2, but does not change H2.

A legitimate H2 information ablation may compare, under matched physical scenarios:

~~~math
\boxed{
\mathscr N_{target}
\quad\text{vs}\quad
\mathscr N_{target+xsys-info}
}
~~~

only when the cross-system observation model is preregistered, qualified and protected against leakage.

Any subsequent organization/control effect remains separately identified.

## 14. Information efficiency is separate

The source supports predictive usefulness, not resource/economic efficiency.

If later studied, information efficiency may account for:

~~~math
\boxed{
\mathbf C_{info}
=
(
\text{sensing},
\text{data access},
\text{communication},
\text{storage},
\text{computation},
\text{latency},
\text{operator burden}
).
}
~~~

Then:

~~~math
\mathcal E_{\rm fy}^{info}
=
\mathcal F
(
\mathcal E_{\rm fx}^{info},
\mathbf C_{info}
).
~~~

This is a thesis extension, not a result attributed to Acosta-Sequeda et al.

## 15. Sustainability / transformation ceiling

Cross-system forecasting may support later intervention/decision processes, but:

~~~math
\boxed{
\text{forecast improvement}
\not\Rightarrow
\text{sustainability improvement}
\not\Rightarrow
\text{infrastructure transformation}.
}
~~~

Stage 6/7 consequences require their own evidence, interventions and accounting boundaries.

## 16. Cyber-physical closed loop

The complete physical-information-control loop may be represented as:

~~~math
\boxed{
Y^{phys}
\rightarrow
y
\rightarrow
\mathcal I_t
\rightarrow
b_t/\widehat Y_t
\rightarrow
u_t
\rightarrow
Y^{phys}.
}
~~~

Cross-system observations may enrich \(\mathcal I_t\) and the estimator without entering \(Y^{phys}\) as a physical dependency.

## 17. Evidence status

Acosta-Sequeda et al. (2025) is a Research Square preprint.

Therefore it may support:
- hypothesis generation;
- preliminary empirical precedent;
- observational/predictive architecture;
- candidate Stage-4 methods.

It shall not be treated as peer-reviewed validation of the thesis model or as causal evidence for physical \(P\leftrightarrow T\) mechanisms.

## 18. P2 mandatory audit additions

P2 shall add:

~~~text
RELATION_EPISTEMIC_CLASS
CAUSAL_VS_PREDICTIVE
SHARED_DRIVER_STATUS
OBSERVATIONAL_RELATION_ID
SOURCE_OBSERVATION
TARGET_QUANTITY
STATE_VS_DEMAND_VS_OBSERVATION
OBSERVATIONAL_LAG
PHYSICAL_DELAY
INFORMATION_LATENCY
ALIGNMENT_BEFORE_INFERENCE
SPATIAL_HETEROGENEITY
TRANSPORT_MODE_SCOPE
INFORMATION_BASELINE
INFORMATION_EFFECTIVENESS_QOI
LEAKAGE_CONTROL
OUT_OF_SAMPLE_STATUS
ABNORMAL_REGIME_SCOPE
INFO_TO_ACTION_LINK
INFO_TO_RESILIENCE_LINK
INFORMATION_EFFICIENCY_STATUS
EVIDENCE_PUBLICATION_STATUS
~~~

Each applicable field is PASS / BLOCKED / DEFERRED / N/A with rationale and provenance.

## 19. Empirical firewall

~~~math
\boxed{
G_{P1.11.4}^{design}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~

No causal P–T dependency, forecast gain in the thesis case, resilience benefit, sustainability consequence or transformation result is created by this amendment.
