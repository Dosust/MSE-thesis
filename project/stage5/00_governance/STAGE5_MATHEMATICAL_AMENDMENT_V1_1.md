# Stage 5 Mathematical Amendment — v1.1

**Date:** 2026-09-19  
**Status:** CANONICAL STAGE-5 MATHEMATICAL AMENDMENT — DESIGN/PROTOCOL ONLY  
**Parent freeze:** `STAGE5_DESIGN_PROTOCOL_FREEZE_V1.md`  
**Parent constitution:** `STAGE5_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md`  
**Parent mathematical specification:** `../06_mathematics/STAGE5_MATHEMATICAL_SPECIFICATION_V1.md`  
**Change-control basis:** material scientific changes after V1 freeze require an explicit versioned amendment.  
**Scientific effect:** notation/closure correction only; no case result, H3 result, threshold, probability model, or intervention ranking is changed.

## 1. Purpose

This amendment resolves four mathematical issues while preserving RQ5/SO5/H3 and the Stage-5 meaning:

1. physical-state viability versus belief-conditioned stochastic maintainability;
2. nonanticipative admissible policies;
3. engineering recovery persistence;
4. interface criticality without a universal scalar coupling derivative.

The Stage-5 conceptual composition remains:

~~~math
\boxed{
\text{Resilience}
=
\text{Remain}
+
\text{Return}
+
\text{Confidence},
}
~~~

where (+) denotes conceptual composition, not arithmetic addition.

## 2. Physical resilience state

The reduced physical resilience state remains

~~~math
\boxed{
x_R=\Pi_R(Y^{phys}).
}
~~~

The projection (Pi_R) is itself a scientific object and must pass reduced-model/state sufficiency tests for the declared Stage-5 QOIs.

## 3. Physical-state viability

To remove state-space ambiguity, the deterministic/robust physical viability object is denoted

~~~math
\boxed{
\mathcal V_T^{x}(t)
\subseteq
\mathcal X_R.
}
~~~

A robust form is

~~~math
\boxed{
\mathcal V_T^{x,rob}(t)
=
\left\{
x_R:
\exists\pi\in\Pi^{NA},
\ \forall\xi\in\Xi,
\ x_R^{\pi,\xi}(\tau)\in K(\tau)
\ \forall\tau\in[t,t+T]
\right\}.
}
~~~

The uncertainty set (Xi) is used only when its semantics are declared. If uncertainty is stochastic rather than set-valued, the stochastic formulation below applies.

## 4. Belief-conditioned stochastic maintainability

Belief (b_t) is an epistemic object and does not belong to the same space as (x_R).

Define

~~~math
\boxed{
P_{viable}^{\star}(b_t)
=
\sup_{\pi\in\Pi^{NA}}
\Pr^{\pi}
\left[
Y_\tau\in K(\tau)
\ \forall\tau\in[t,t+T]
\mid b_t
\right].
}
~~~

The corresponding belief-space maintainability set is

~~~math
\boxed{
\mathcal V_{\alpha,T}^{b}
=
\{
b:
P_{viable}^{\star}(b)\ge\alpha
\}
\subseteq\mathcal B.
}
~~~

Permanent firewall:

~~~math
\boxed{
\mathcal V_T^{x}
\neq
\mathcal V_{\alpha,T}^{b}.
}
~~~

The former is a physical-state-space viability object. The latter is a belief-space confidence/maintainability object.

## 5. Reach-avoid recovery

Belief-conditioned recovery remains

~~~math
\boxed{
P_{recover}^{\star}(b_t)
=
\sup_{\pi\in\Pi^{NA}}
\Pr^{\pi}
\left[
\tau_{G_{rec}}\le T,
\;
Y_s\notin F_{unsafe}
\ \forall s<\tau_{G_{rec}}
\mid b_t
\right].
}
~~~

with

~~~math
\boxed{
\mathcal R_{\beta,T}^{b}
=
\{
b:
P_{recover}^{\star}(b)\ge\beta
\}.
}
~~~

When recovery is an engineering service requirement requiring persistence rather than instantaneous target entrance, define

~~~math
\boxed{
T_{rec}^{\Delta}
=
\inf
\left\{
t\ge t_d:
x_R(s)\in G_{rec}
\ \forall s\in[t,t+\Delta_{rec}]
\right\}.
}
~~~

The persistence duration (Delta_{rec}) must be requirement/evidence based and prospectively frozen. If the authoritative requirement is genuinely first-entry recovery, the simpler first-hitting-time definition remains admissible and the distinction must be stated.

## 6. Resilience geometry

The physical resilience margin is evaluated against the physical-state viability boundary:

~~~math
\boxed{
\rho_{\mathcal V}(x_R)
=
d_{g_R}
\left(
x_R,
\partial\mathcal V_T^{x}
\right).
}
~~~

Raw Euclidean distance across heterogeneous units is prohibited.

A baseline admissible construction is obtained by a declared scale matrix

~~~math
D_R=\operatorname{diag}(s_1,\ldots,s_n),
\qquad
\widetilde x_R=D_R^{-1}x_R,
~~~

with

~~~math
\boxed{
\rho_{\mathcal V}(x_R)
=
\inf_{z\in\partial\mathcal V_T^{x}}
\left\|
D_R^{-1}(x_R-z)
\right\|_2.
}
~~~

The scales (s_i) must come from engineering tolerances, nondimensionalization, service resolution, measurement/model uncertainty, or another independently justified basis.

A state-dependent/Riemannian metric may be used only if it adds scientifically necessary information and has an identifiable/calibratable interpretation.

## 7. Interface criticality — no universal scalar-weight derivative

The following is **not** a universal canonical definition:

~~~math
-\frac{\partial\rho_{\mathcal V}}{\partial w_{ij}}.
~~~

Reasons:

- current Stage-2 causal semantics do not require a universal scalar (w_{ij});
- mechanisms may be discrete, conditional, hybrid, or vector-parameterized;
- (partial\mathcal V) may be nonsmooth;
- topology/mode changes can invalidate local differentiability.

### 7.1 Smooth local mechanism-parameter sensitivity

When mechanism parameter (	heta_{e,p}) is physical, identified/bounded, and local smoothness is demonstrated,

~~~math
\boxed{
C_{e,p}^{\mathcal V}
\approx
-
\frac{
\rho_{\mathcal V}(\theta_{e,p}+\Delta\theta)
-
\rho_{\mathcal V}(\theta_{e,p})
}{
\Delta\theta
}.
}
~~~

This is a local diagnostic, not a universal interface score.

### 7.2 General perturbation diagnostic

For declared resilience QOI (q),

~~~math
\boxed{
S_e^{(q)}
=
q(\mathfrak M^{\delta_e})
-
q(\mathfrak M),
}
~~~

or, for a physically meaningful continuous perturbation norm,

~~~math
\boxed{
\widetilde S_e^{(q)}
=
\frac{
q(\mathfrak M^{\delta_e})-q(\mathfrak M)
}{
\|\delta_e\|
}.
}
~~~

For a discrete mechanism/interface, a declared ablation is admissible:

~~~math
\boxed{
S_e^{(q)}
=
q(\mathfrak M^{e:\,disabled})
-
q(\mathfrak M).
}
~~~

Candidate diagnostic vector:

~~~math
\boxed{
\mathbf S_e
=
\left(
\Delta P_{viable},
\Delta P_{recover},
\Delta T_{rec},
\Delta\rho_{\mathcal V}
\right).
}
~~~

Global sensitivity and scenario sensitivity should be used when local smoothness is not justified.

## 8. Ranking firewall

~~~math
\boxed{
\text{interface sensitivity}
\neq
\text{intervention preference}.
}
~~~

Any interface ranking must report sensitivity/uncertainty/stability to the perturbation definition, model form, scenario domain, numerical approximation, and admissible parameter uncertainty.

## 9. Updated resilience object notation

Where both physical and belief-space objects are used, the Stage-5 evidence tuple is interpreted as

~~~math
\boxed{
\mathfrak R_T
=
\left(
\mathcal V_T^{x},
\mathcal V_{\alpha,T}^{b},
\mathcal R_{\beta,T}^{b},
\rho_{\mathcal V},
T_{\mathcal V},
T_{rec}^{\Delta},
P_{viable},
P_{recover}
\right),
}
~~~

with only the applicable/qualified fields populated for a specific experiment.

This notation clarifies the spaces; it does not change H3.

## 10. H3 preservation

The primary confirmatory comparison remains

~~~math
\boxed{
A_0=R_{curve}
\quad\text{vs}\quad
A_4=R_{curve}+\mathfrak R_T.
}
~~~

No superiority is assumed.

## 11. VVUQ consequences

The existing Stage-5 VVUQ protocol remains active, with these added checks:

- physical-state/belief-space type checking;
- nonanticipativity/information leakage audit;
- recovery-persistence sensitivity when (Delta_{rec}) is active;
- scale/metric sensitivity for (ho_{\mathcal V});
- interface-criticality perturbation/ranking stability;
- projection adequacy for (Pi_R).

## 12. Handoff effect

The Stage5→6 handoff object is not structurally changed. Downstream users must interpret (mathfrak R_T) using the clarified state-space/belief-space semantics above.

## 13. Claim boundary

~~~math
\boxed{
\text{Stage-5 mathematical amendment frozen}
\neq
\text{Stage-5 empirical closure}
\neq
\text{H3 support}.
}
~~~

All case thresholds, (Delta_{rec}), metric scales, probability models, interface perturbations, and H3 results remain governed by their existing evidence, preregistration and VVUQ gates.
