# Stage 5 Mathematical Specification v1

## Service regions

\[
K(t)=K_P(t)\cap K_T(t)\cap K_{PT}(t)\cap K_{\rm operational}(t).
\]

\(G_{\rm rec}\) is the desired recovered region and is distinct from \(K\).  
\(F_{\rm unsafe}\) is the forbidden/unacceptable region.

## Deterministic viability

\[
\mathcal V_T(t)=
\left\{
x_R(t)\in K(t):
\exists\pi,\ 
x_R(\tau)\in K(\tau)\ \forall\tau\in[t,t+T]
\right\}.
\]

## Robust viability

\[
\mathcal V_T^{rob}=
\left\{
x_0:
\exists\pi\;\forall\xi\in\Xi,\ 
x_t^{\pi,\xi}\in K(t)
\right\}.
\]

## Stochastic maintainability

\[
P_{\rm viable}^{*}(b_t)
=
\sup_{\pi\in\Pi(z_I,z_O)}
\Pr^\pi
\left[
Y_\tau\in K(\tau),
\forall\tau\in[t,t+T]
\mid b_t
\right].
\]

\[
\mathcal V_{\alpha,T}
=
\{b:P_{\rm viable}^{*}(b)\ge\alpha\}.
\]

## Stochastic recovery reach-avoid

\[
P_{\rm recover}^{*}(b_t)
=
\sup_{\pi\in\Pi(z_I,z_O)}
\Pr^\pi
\left[
\tau_{G_{\rm rec}}\le T,\ 
Y_s\notin F_{\rm unsafe}\ \forall s<\tau_{G_{\rm rec}}
\mid b_t
\right].
\]

\[
\mathcal R_{\beta,T}
=
\{b:P_{\rm recover}^{*}(b)\ge\beta\}.
\]

## Epistemic membership confidence vs future dynamic probability

Keep separate:

\[
P_{\rm inV}(t)=
\Pr[Y_t\in\mathcal V_T\mid\mathcal I_t]
\]

from \(P_{\rm viable}^{*}\), which includes future uncertainty and control.

## Resilience object

\[
\mathfrak R_T(t)=
\left(
\mathcal V_{\alpha,T},
\mathcal R_{\beta,T},
\rho_{\mathcal V},
T_{\mathcal V},
T_{\rm rec},
P_{\rm viable},
P_{\rm recover}
\right).
\]

## Geometry

Raw Euclidean distance across mixed units is prohibited. Define

\[
\rho_{\mathcal V}
=
d_{g_R}(x_R,\partial\mathcal V),
\]

where \(g_R\) is justified by nondimensionalization, engineering tolerances, service scales, or another physically meaningful metric.

## Probability gate

A stochastic formulation is admissible only when a probability model has passed evidence/calibration checks. Otherwise use robust, interval, set-valued or scenario formulations.
