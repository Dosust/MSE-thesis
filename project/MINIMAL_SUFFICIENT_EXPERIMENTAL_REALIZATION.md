# Why a Reduced Demonstrator Is Scientifically Necessary

<!--
DOCUMENT STATUS: CURRENT METHODOLOGICAL RATIONALE
SOURCE: user-supplied Pasted markdown(20260911-043555).md
SOURCE_SHA256: ebfe4dc7b3404fa817ddcaf137832e6ee372fb4cfeca0a57fa6aa5cc5bb2c9e3
PRESERVATION RULE: scientific reasoning, equations, H1-H5 preservation logic, V&V/UQ arguments, and demonstrator-selection principles are preserved from the supplied source.
DISPLAY-ONLY NORMALIZATION: heading hierarchy standardized; malformed Markdown table repaired; Equation RD reformatted to GitHub-safe multiline mathematics; fragile LaTeX tag removed and replaced with a Markdown equation label.
NOTATION SYNCHRONIZATION: 2026-09-16; Stage-2 notation follows CANONICAL_DEPENDENCY_CONTRACT_V1.md without changing demonstrator-selection logic.
FREEZE BOUNDARY: this document defines the demonstrator-selection methodology and governing principle; it does not freeze the actual demonstrator topology, parameterization, hazard family, or numerical thresholds.
-->

The **reduced demonstrator does not reduce the seven-stage framework**. It reduces only the size and complexity of the experimental realization used to test the framework.

The distinction is:

```math
\boxed{ \text{Full scientific framework} \neq \text{experimental demonstrator}. }
```

The full framework remains

```math
\boxed{ P,T,I,O \rightarrow \mathbb I \rightarrow F_{\mathcal G}^{m} \rightarrow (I,\hat X,O,u) \rightarrow \mathcal V \rightarrow \Phi_{\rm ST} \rightarrow \mathfrak P_{\rm ST}. }
```

where the Stage-2 active dependency set is

```math
\mathbb I(t)=\{\mathfrak d_e(t):e\in\mathcal E(t)\},
\qquad
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e).
```

The demonstrator is a deliberately controlled subset:

```math
\boxed{ \mathcal M_D\subset\mathcal M_{\rm full} }
```

that retains **every mechanism necessary to test** **`H_1-H_5`** while removing components that do not contribute to those tests.

A better term than simply “reduced model” is therefore:

```math
\boxed{ \textbf{Minimal Sufficient Experimental Realization} }
```

of the complete framework.

---

## 1. Scientific reason: hypotheses require controlled contrasts

Our hypotheses concern specific mechanisms.

For example:

```math
H_1: \mathbb I \rightarrow F_{\mathcal G}
```

tests whether dynamic interdependencies matter.

```math
H_2: (I,O) \rightarrow (\hat X,\mathcal U,u) \rightarrow Y
```

tests information and organizational effects.

If hundreds of mechanisms change simultaneously, then after observing

```math
\Delta Y
```

we cannot determine which mechanism caused it.

The experimental requirement is therefore:

```math
\boxed{ \Delta X_i \rightarrow \Delta Y \qquad \text{while relevant competing factors are controlled}. }
```

This is why nested models are powerful:

```math
M_0=P+T,
```

```math
M_1=P+T+\text{dynamic interdependency},
```

```math
M_2=P+T+I,
```

```math
M_3=P+T+I+O.
```

Then quantities such as

```math
M_2-M_1
```

have a scientific interpretation.

With an uncontrolled full-scale implementation, that interpretation becomes much weaker.

---

## 2. Falsifiability requires limited degrees of freedom

A confirmatory hypothesis must be capable of failing.

Suppose the model contains:

```math
p=500
```

adjustable parameters, numerous topology choices and many unvalidated mechanisms.

If the prediction fails, it is always possible to say:

> another parameter needs calibration.

That creates excessive explanatory flexibility.

A strong experiment instead constrains the degrees of freedom:

```math
\boxed{ \Theta_D \subset \Theta_{\rm full}. }
```

This makes a result such as

```math
\Delta_i<\delta_i
```

meaningful evidence against the hypothesis rather than merely another opportunity to retune the model.

So reduction improves:

```math
\boxed{ \text{falsifiability}. }
```

---

## 3. Identifiability requires reduction

Suppose

```math
Y=F(\theta_1,\ldots,\theta_p).
```

With many uncertain parameters, different parameter combinations may produce essentially identical outputs:

```math
F(\theta^{(1)}) \approx F(\theta^{(2)}).
```

Then:

```math
\boxed{ Y\text{ observed} \not\Rightarrow \theta\text{ identified}. }
```

This is a parameter-identifiability problem.

More importantly for this thesis, it becomes a **mechanism-identifiability problem**:

```math
\boxed{ \text{same resilience trajectory} \leftarrow \text{multiple competing causal explanations}. }
```

The demonstrator therefore needs enough complexity to reproduce the mechanism, but not so much complexity that causal attribution becomes impossible.

---

## 4. Verification and validation become achievable

Our confirmatory matrix requires:

```math
\boxed{ \Omega_H\subseteq\Omega_V. }
```

where:

- `\Omega_H` = domain in which we test the hypothesis,
- `\Omega_V` = domain in which the model has credible validation evidence.

Every included subsystem requires:

```math
\text{verification}, \quad \text{validation}, \quad \text{uncertainty analysis}.
```

If we simultaneously model:

- generation,
- transmission,
- distribution,
- DER,
- storage,
- EVs,
- roads,
- buses,
- metro,
- regional rail,
- telecommunications,
- SCADA,
- organizational networks,
- emergency logistics,
- governance,

then each of these requires its own equations, parameters, benchmarks and uncertainty characterization.

The credibility problem grows rapidly:

```math
\boxed{ N_{\rm components} \uparrow \Rightarrow N_{\rm interfaces} \uparrow\uparrow \Rightarrow \text{V\&V burden} \uparrow\uparrow. }
```

For `n` subsystem types, there can potentially be

```math
\frac{n(n-1)}{2}
```

pairwise interaction classes even before directionality and higher-order relationships are considered.

Thus reducing the realization makes rigorous V&V possible.

---

## 5. Stage 5 creates a computational necessity

Viability analysis introduces an especially severe dimensionality problem.

Suppose the reduced viability state is

```math
Y_V\in\mathbb R^n.
```

If each dimension uses `m` discretization levels, a direct grid requires approximately

```math
\boxed{ N_{\rm grid}=m^n. }
```

For example:

```math
m=20,\qquad n=6
```

gives

```math
20^6=64\,000\,000.
```

But:

```math
n=12
```

gives

```math
20^{12}=4.096\times10^{15}.
```

Therefore:

```math
\boxed{ \text{full physical state} \neq \text{viability state}. }
```

We need a carefully justified projection:

```math
Y \longrightarrow Y_V
```

that preserves the variables governing sustainability/viability loss.

This is not an arbitrary simplification. It is a mathematically necessary form of model reduction.

---

## 6. The demonstrator must preserve mechanisms, not all assets

Reduction should occur mainly in:

```math
\boxed{ \text{number of nodes} + \text{number of components} + \text{number of state variables} + \text{number of hazards} + \text{number of interventions}. }
```

It should **not** remove the causal architecture being tested.

Therefore:

```math
\boxed{ P,T,I,O }
```

should remain represented.

Similarly, we must preserve at least the mechanisms required for:

```math
H_1-H_5.
```

That gives the preservation constraint:

```math
\boxed{ \mathfrak M(H_i) \subseteq \mathfrak M(\mathcal M_D) \qquad \forall i, }
```

where

```math
\mathfrak M(H_i)
```

is the set of mechanisms required to test hypothesis `H_i`.

---

## 7. Reduction improves uncertainty quantification

Suppose the model contains uncertain parameters

```math
\theta= [\theta_1,\ldots,\theta_p].
```

Global uncertainty analysis requires evaluating:

```math
Y=F(\theta).
```

As `p` grows, the required sampling burden also grows substantially.

For example, sensitivity analysis may require:

```math
N_{\rm sim} \propto pN
```

or even larger ensembles depending on the method.

A reduced parameter space makes possible:

```math
\boxed{ \text{Monte Carlo} + \text{Morris screening} + \text{Sobol analysis} + \text{scenario stress testing}. }
```

A very large system might technically run once but still be impossible to characterize probabilistically.

One simulation is not rigorous uncertainty analysis.

---

## 8. Reduction makes ablation possible

Ablation is essential for our thesis.

Suppose the full model is:

```math
M_{\rm full} = P+T+I+O+\mathbb I.
```

We need experiments such as:

```math
M_{\rm full}-I,
```

```math
M_{\rm full}-O,
```

```math
M_{\rm full}-\mathfrak d_e,
```

or a prespecified mechanism-parameter/activation contrast

```math
(\theta_e,\gamma_e)\rightarrow(\theta_e^{(0)},\gamma_e^{(0)}),
```

as well as

```math
M_{\rm dynamic}-M_{\rm static}.
```

Then we measure:

```math
\Delta T_C, \quad \Delta L_{\rm service}, \quad \Delta\rho, \quad \Delta T_{\mathcal V}.
```

This answers:

```math
\boxed{ \text{Which mechanism actually produced the improvement?} }
```

rather than merely:

```math
\text{Did the complete model produce an interesting result?}
```

---

## 9. Reduction permits competing-model experiments

The research should not compare:

```math
\text{our framework} \quad\text{vs}\quad \text{nothing}.
```

It should compare scientifically meaningful alternatives.

For H1:

```math
\boxed{ M_{H1}^{(0)} = P+T\text{ independent} }
```

```math
\boxed{ M_{H1}^{(1)} = P-T\text{ static coupling} }
```

```math
\boxed{ M_{H1}^{(2)} = P-T\text{ dynamic causal coupling}. }
```

For H3:

```math
\boxed{ Q_C \quad\text{vs}\quad Q_C+Q_{\mathcal V}. }
```

For H5:

```math
\boxed{ \Pi_{\rm fixed} \quad\text{vs}\quad \pi_{\rm adaptive}. }
```

A controlled demonstrator makes these competing representations comparable.

---

## 10. Reduction improves reproducibility

Another researcher should eventually be able to reproduce:

```math
\boxed{ \text{inputs} \rightarrow \text{model} \rightarrow \text{experiment} \rightarrow \text{result}. }
```

A demonstrator with:

- publicly available benchmark networks,
- documented parameter sets,
- transparent equations,
- manageable computation,
- version-controlled code,

is considerably more reproducible than a giant integrated system dependent on inaccessible proprietary data.

For an academic thesis:

```math
\boxed{ \text{reproducibility} > \text{unnecessary realism}. }
```

The strongest model is not necessarily the largest model.

---

## 11. Reduction separates framework validity from case-study specificity

This is also important conceptually.

The seven-stage framework is general:

```math
\boxed{ \mathcal F_{\rm framework}. }
```

The numerical case is one realization:

```math
\boxed{ \mathcal R_1(\mathcal F_{\rm framework}). }
```

We should not claim:

```math
\mathcal R_1 = \mathcal F_{\rm framework}.
```

Instead:

```math
\boxed{ \mathcal R_1 \text{ tests selected theoretical propositions generated by } \mathcal F_{\rm framework}. }
```

Therefore the thesis can legitimately say:

> The framework is general, whereas its empirical/computational evaluation is performed through a bounded demonstrator.

That is normal scientific practice.

---

## 12. Reduction does not mean toy modeling

This is important.

There are three levels:

```math
\boxed{ \text{toy model} < \text{minimal sufficient demonstrator} < \text{full operational digital twin}. }
```

We do **not** want an oversimplified toy model.

The demonstrator must retain:

### Physical realism

```math
F_P,\qquad F_T.
```

### Causal dependency/interdependency semantics

```math
\mathfrak d_e^{PT},\qquad \mathfrak d_{e'}^{TP},\qquad \mathbb I^{PT}(t).
```

### Information dynamics

```math
I\rightarrow\hat X.
```

### Organizational constraints

```math
O\rightarrow\mathcal U.
```

### Control

```math
u=\pi(\hat X,I,O).
```

### Viability

```math
\mathcal V_{\rm sus}^{u,T}.
```

### Transformation

```math
\mathfrak M_k\rightarrow\mathfrak M_{k+1}.
```

So the correct objective is:

```math
\boxed{ \text{minimum size} \quad \textbf{subject to} \quad \text{maximum preservation of hypothesis-relevant mechanisms}. }
```

---

## 13. We can formalize the reduction problem

This is useful mathematically.

Let:

```math
\mathcal M_{\rm full}
```

denote the complete conceptual model and

```math
\mathcal M_D
```

a candidate demonstrator.

Define a model-complexity functional:

```math
C(\mathcal M_D) = c_1n_{\rm states} + c_2n_{\rm parameters} + c_3n_{\rm interfaces} + c_4n_{\rm scenarios} + c_5T_{\rm computational}.
```

Then choose:

**Equation RD — Minimal sufficient demonstrator optimization**

```math
\mathcal M_D^*
=
\arg\min_{\mathcal M_D} C(\mathcal M_D)
```

subject to

```math
\begin{aligned}
\text{C1: }& P,T,I,O\text{ represented},\\
\text{C2: }& \mathfrak M(H_i) \subseteq \mathfrak M(\mathcal M_D),
\quad \forall i=1,\ldots,5,\\
\text{C3: }& H_i\text{ remains falsifiable},\\
\text{C4: }& \Omega_H\subseteq\Omega_V,\\
\text{C5: }& \text{parameters sufficiently identifiable},\\
\text{C6: }& \text{V\&V feasible},\\
\text{C7: }& \text{UQ computationally feasible},\\
\text{C8: }& \text{key outputs preserved with required accuracy}.
\end{aligned}
```

This equation is a **[P] methodological formalization** for the thesis—not an established universal optimization model.

But it captures exactly what we mean by reduction.

---

## 14. Hypothesis-preservation criterion

The most important condition is:

```math
\boxed{ \forall H_i, \quad \exists C_i \text{ such that } \mathcal M_D \text{ permits a discriminatory critical test of }H_i. }
```

In words:

> The demonstrator is acceptable only if every primary hypothesis still has an experiment capable of distinguishing it from its strongest rival.

Therefore reduction stops when removing another component would eliminate:

- a mechanism,
- an observable,
- a competing hypothesis,
- or a critical experiment.

This gives us a rigorous **stopping rule for simplification**.

---

## 15. What should actually be reduced

| Element | Full framework | Demonstrator strategy |
|---|---|---|
| Power | generation + transmission + distribution + DER + charging + traction | select the minimum physically relevant subset |
| Transportation | roads + EV + buses + urban rail + regional rail + multimodal | retain only modes needed for tested couplings |
| Information | complete sensing/comms/data/automation/interoperability architecture | retain sensing-delay-estimation mechanisms |
| Organization | governance + decision + coordination + workforce + logistics + learning | retain decision/resource/mobilization mechanisms |
| Hazards | multi-hazard | one primary disturbance family |
| Geography | potentially regional/national | controlled network/city-scale case |
| Transformation actions | large intervention library | small representative `P,T,I,O,\mathbb I` library |
| State dimension | full physical state | full simulation state + separate reduced viability state |

Notice:

```math
\boxed{ \text{layers remain;} \quad \text{resolution decreases}. }
```

That is the essential distinction.

---

## 16. What must never be reduced away

The following are non-negotiable because they form the thesis logic:

```math
\boxed{ P,T,I,O }
```

```math
\boxed{ \mathbb I=\{\mathfrak d_e\} }
```

```math
\boxed{ F_{\mathcal G} }
```

```math
\boxed{ X\rightarrow y\rightarrow I\rightarrow\hat X\rightarrow O\rightarrow u }
```

```math
\boxed{ \mathcal V_{\rm sus} }
```

and at least one:

```math
\boxed{ \mathfrak M_0 \rightarrow \mathfrak M_1 }
```

Stage-7 transformation.

If a supposed reduction removes these, it is no longer a demonstrator of the full thesis framework.

---

## 17. Final methodological statement for the thesis

A thesis-ready explanation could be:

> **Reduced demonstrator rationale.** The proposed seven-stage framework describes a general class of multilayer physical–informational–organizational infrastructure systems and is not itself reduced. For confirmatory evaluation, however, a minimal sufficient experimental realization is required. The demonstrator deliberately limits the number of assets, state variables, interfaces, disturbance classes and transformation alternatives while preserving all causal mechanisms required to discriminate the primary research hypotheses. This reduction supports mechanism identifiability, controlled counterfactual comparison, model verification and validation, uncertainty quantification, computational tractability of controlled-viability calculations, and reproducibility. Reduction therefore concerns **model resolution rather than scientific scope**. Components are removed only when their omission does not eliminate a hypothesis-relevant mechanism, observable, competing explanation or critical test.

Mathematically:

```math
\boxed{ \textbf{Reduce complexity, not causal content.} }
```

Or even more precisely:

```math
\boxed{ \mathcal M_D^* = \text{minimum-complexity realization preserving the discriminatory power of }H_1-H_5. }
```

That should be the governing principle when we select the actual `P-T-I-O` demonstrator.
