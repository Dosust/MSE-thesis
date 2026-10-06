# Mathematical Framework Specification V1

**Status:** CURRENT WORKING MATHEMATICAL-FRAMEWORK SPECIFICATION  
**Date:** 2026-10-06  
**Scope authority:** \`CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md\`  
**Conceptual counterpart:** \`CONCEPTUAL_FRAMEWORK_SPEC_V3.md\`

## 1. Purpose

Formalize the conceptual framework into a minimum set of testable mathematical objects.

The mathematical framework must preserve the same scientific topology as the conceptual framework, while replacing verbal relations with explicit mathematical definitions.

## 2. Extreme-heat forcing

\[
H(x,t)
=
[T_{\mathrm{amb}}(x,t),G_s(x,t),v_w(x,t),\Delta t,\ldots].
\]

Only variables required by the selected physical models are retained.

## 3. Subsystem states

Power:

\[
\dot X_P
=
f_P(X_P,H,Z,u_P;\theta_P).
\]

Physical charging interface:

\[
\dot Z
=
f_Z(Z,X_P,X_T,H,u_Z;\theta_Z).
\]

Electrified transportation:

\[
\dot X_T
=
f_T(X_T,H,Z,u_T;\theta_T).
\]

These are general structural forms. Each selected component retains its own defensible governing physics.

## 4. Coupled state

\[
X(t)
=
[X_P^\top(t),Z^\top(t),X_T^\top(t)]^\top.
\]

\[
\dot X
=
F(X,H,u;\theta).
\]

The coupled form is assembled from admitted component dynamics and qualified directional interfaces.

## 5. Constraints and critical transition time

For state/component \(i\):

\[
g_i(X_i,t)\le 0.
\]

Critical transition time:

\[
\tau_i^C
=
\inf\{t:g_i(X_i(t),t)=0\}.
\]

The threshold must have physical or operational evidence.

## 6. Propagation timing

For a qualified source event \(i\) and target response \(j\):

\[
\delta_{ij}
=
t_j^{\mathrm{response}}
-
\tau_i^C.
\]

This is used only when the source-target mechanism is physically admitted. It is not graph distance and not automatically a cascade measure.

## 7. Service trajectories

\[
Q_P(t)=G_P(X(t)),
\qquad
Q_T(t)=G_T(X(t)).
\]

Service acceptability:

\[
Q_P(t)\ge Q_P^{\min},
\qquad
Q_T(t)\ge Q_T^{\min}.
\]

Exact service definitions remain open until their operational indicators are frozen.

## 8. Engineering interventions

### Improve

\[
\theta'=\theta+\Delta\theta.
\]

Improve changes baseline design/physical parameters.

### Adapt

\[
u_A(t).
\]

Adapt changes operation during the heat event.

### Restore

\[
u_R(t).
\]

Restore changes the post-degradation recovery trajectory.

Do not collapse \(\Delta\theta\), \(u_A(t)\), and \(u_R(t)\) into one undifferentiated control object.

## 9. Resilience performance

A generic performance functional may be written as:

\[
R
=
\mathcal R
\left(
Q_P(\cdot),
Q_T(\cdot),
\tau^C,
\delta,
\theta',
u_A,
u_R
\right).
\]

This notation is structural only. The exact resilience functional is OPEN until the chosen performance metrics are frozen.

Candidate quantities may include:
- service deficit;
- disruption duration;
- recovery time;
- maintained service fraction.

## 10. Sustainability dimensions

Define a sustainability vector:

\[
S
=
[S_{\mathrm{soc}},S_{\mathrm{env}},S_{\mathrm{econ}}]^\top.
\]

Candidate dimension functions:

\[
S_{\mathrm{soc}}
=
\Phi_{\mathrm{soc}}(I_{\mathrm{access}},I_{\mathrm{safety}},I_{\mathrm{equity}},\ldots),
\]

\[
S_{\mathrm{env}}
=
\Phi_{\mathrm{env}}(I_{\mathrm{energy}},I_{\mathrm{emissions}},I_{\mathrm{resource}},\ldots),
\]

\[
S_{\mathrm{econ}}
=
\Phi_{\mathrm{econ}}(I_{\mathrm{cost}},I_{\mathrm{loss}},I_{\mathrm{recovery}},\ldots).
\]

The exact indicator functions and normalization are OPEN.

Sustainability assessment must include both:
- resilience/service consequences;
- intervention burdens.

## 11. Sustainable and resilient outcome

A placeholder joint mapping may be written:

\[
Y_{\mathrm{SR}}
=
\Psi(R,S).
\]

This is not yet an operational aggregation rule.

Before using \(\Psi\), the thesis must decide whether the joint decision is represented by:
- explicit constraints;
- Pareto analysis;
- multicriteria decision analysis;
- a justified scalar functional;
- another defensible approach.

No arbitrary weighting is allowed.

## 12. SDG relevance / alignment

The rigorous mapping is:

\[
S_k
\rightarrow
I_k
\rightarrow
T_m^{\mathrm{SDG}},
\]

where:
- \(S_k\) is a sustainability dimension;
- \(I_k\) is an operational indicator;
- \(T_m^{\mathrm{SDG}}\) is a relevant SDG target/indicator.

Do not map a broad sustainability dimension directly to an SDG number without an indicator/target rationale.

## 13. Visual encoding requirement

The mathematical figure must:
- omit component inventory prose when equations already define the subsystem;
- keep equations minimal and legible;
- preserve pure white backgrounds;
- preserve semantic arrow types;
- show only equations required to explain the global mathematical architecture.

## 14. Interactive extension

Inspired by visual-interactive mathematics references, an optional interactive implementation follows:

\[
\text{parameter}
\rightarrow
\text{model recomputation}
\rightarrow
\text{derived quantities}
\rightarrow
\text{visual update}.
\]

Candidate interactive parameters:
- heat intensity;
- heat duration;
- loading;
- charging demand;
- design parameter;
- adaptive control;
- recovery action.

The interactive visualization is an implementation aid, not the scientific model itself.
