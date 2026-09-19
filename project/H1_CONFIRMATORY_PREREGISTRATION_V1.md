> **SUPERSEDED FOR ACTIVE CONFIRMATORY EXECUTION — 2026-09-19**
>
> This v1 preregistration is preserved for provenance. It contains named scenario/mechanism families that were specified before the current Stage-2 causal and Stage2→3 readiness audits. The active confirmatory authority is `project/global_integration/GLOBAL_H1_H5_MASTER_PREREGISTRATION_V1.md` together with the Stage-3 v2 readiness/scenario controls.
>
> Permanent execution rule:
>
> ```math
> \boxed{\mathbb I_{s,M_2}^{active}\subseteq\mathbb I_3^{ready}}
> ```
>
> A historical scenario family does not authorize a blocked dependency.

# EGMIV H1 Confirmatory Pre-registration v1.0

**Status:** FROZEN DESIGN — NOT YET EXECUTED  
**Date:** 2026-09-14  
**Method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation  
**Models:** M0 independent; M1 static/algebraic coupling; M2 dynamic causal coupling  
**Primary purpose:** test H1a without outcome-dependent tuning; define the H1b validation shell before held-out data are examined.

## 1. Confirmatory hypothesis

\[
\boxed{
H_1:
\text{Explicit dynamic causal P–T coupling produces materially different and more defensible cascade/service trajectories than independent or static-coupling representations.}
}
\]

Operational decomposition:

\[
\boxed{
H_{1a}:
M_2\text{ produces materially different service/cascade trajectories from }M_1
}
\]

\[
\boxed{
H_{1b}:
M_2\text{ predicts held-out service/cascade trajectories more defensibly than }M_0,M_1.
}
\]

The decisive H1a comparison is **M2 vs M1**, because both models contain Power–Transportation coupling and differ mainly by explicit interface memory/delay. M2 vs M0 is secondary context.

## 2. Model freeze

No confirmatory result is admissible if the model structure is altered after the pre-registration lock without issuing a new version.

- **M0:** verified independent baseline.
- **M1:** verified memoryless static/algebraic coupling.
- **M2:** verified dynamic charger-memory + dynamic road-to-repair delay comparator.

Mandatory limiting relations already verified:

\[
M_1\rightarrow M_0
\quad\text{when interface maps are removed},
\]

\[
M_2\rightarrow M_1
\quad\text{when queue memory and dynamic repair delay are removed}.
\]

No AI controller, route-choice feedback, information layer, organizational layer, or additional dynamic interface is permitted inside H1 v1 confirmatory runs.

## 3. Confirmatory scenario universe

Define

\[
\Omega_H=
\Omega_0\cup
\Omega_C\cup
\Omega_O\cup
\Omega_R\cup
\Omega_J\cup
\Omega_D.
\]

| Family | Purpose | Mechanism |
|---|---|---|
| \(\Omega_0\) | null / intact control | no activated dynamic interface |
| \(\Omega_C\) | charging-demand stress | T→P charging demand and charger-memory activation |
| \(\Omega_O\) | charger-feeder outage | P→T loss of charging service + backlog/recovery hysteresis |
| \(\Omega_R\) | road-to-repair stress | T→P state-dependent crew access and power restoration |
| \(\Omega_J\) | joint charging + repair disruption | interaction of both physical dynamic interfaces |
| \(\Omega_D\) | explicit decoupling/zero-memory controls | nested-model falsification |

Each scenario is encoded as

\[
\omega=
(c,\ell_P,\rho_c,\tau_{\mathrm{out}},a_R,\chi_R,\theta_{\mathrm{shared}},\eta),
\]

where \(\rho_c=\lambda_c/\mu_{\max,c}\) and \(\chi_R=n/N^{jam}\).

### Scenario-value rule

No continuous stress value may be chosen because it creates a large M2 effect.

For final confirmatory execution, values must be determined **before model comparison** from:
1. empirical/event distributions;
2. independently documented engineering operating ranges;
3. benchmark truth when empirical validation is impossible.

For empirical continuous factors, the default low/central/high design points are the **10th, 50th and 90th empirical percentiles**, plus any mechanistic boundary defined by the equations (for example \(\rho_c=1\)) when it lies inside the admissible range.

For discrete topology events, all admissible single-component events that activate the target interface are included when computationally feasible. Any reduction must use a deterministic predeclared stratification rule and may not depend on M0/M1/M2 output differences.

## 4. Matched execution rule

For every \(\omega\in\Omega_H\),

\[
\boxed{
(X_0,\eta,D,\theta_{\mathrm{shared}},T,\Delta t,\omega)
\text{ are identical for }M_0,M_1,M_2.
}
\]

Stochastic input draws use common random numbers across models. No model receives a more favorable hazard realization, demand trajectory, initial condition, parameter draw, observation horizon, or numerical time step.

## 5. Outcomes

For services \(s\in\{P,T\}\), define independently-derived service-resolution thresholds \(\epsilon_s\).

The primary H1a endpoint is

\[
\boxed{
D_{PT}^{2,1}(\omega)=
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
dt.
}
\]

The population statistic is

\[
\boxed{
\Theta_{\mathrm{repr}}
=
\mathbb E_{\omega\sim\Omega_H}
[D_{PT}^{2,1}(\omega)].
}
\]

Secondary endpoints:

\[
L_s=\int_0^T[1-S_s(t)]dt,
\qquad
\Delta L_s^{2,1}=L_s(M_2)-L_s(M_1),
\]

plus sustained recovery time \(T_R\), event/cascade timing discrepancy, maximum charger backlog, queue-clearance time, crew-arrival time, restoration time, and all physical/numerical residuals.

## 6. Threshold derivation — frozen independently

For each service \(s\), define:
- \(u_{obs,s}\): observation/measurement uncertainty or effective resolution;
- \(u_{num,s}\): numerical/discretization uncertainty from refinement;
- \(u_{eng,s}\): externally documented smallest operationally meaningful service change, if available.

Resolution floor:

\[
\epsilon_s^{det}=\max(u_{obs,s},u_{num,s}).
\]

If an engineering tolerance exists,

\[
\boxed{
\epsilon_s=
\max(u_{eng,s},u_{obs,s},u_{num,s}).
}
\]

If no defensible \(u_{eng,s}\) exists, use \(\epsilon_s=\epsilon_s^{det}\), but **do not claim engineering materiality**. The conclusion may only be “representation-distinguishable.”

No threshold may be estimated from observed M2−M1 effect sizes.

For H1b, define the predictive threshold from the independently estimated noise floor:

\[
\boxed{
\epsilon_{pred,s}
=
Q_{0.95}(|\mathcal E_s^{noise}|).
}
\]

Training/calibration information only may be used to estimate this quantity.

## 7. Uncertainty quantification

\[
\theta=[\theta_P,\theta_T,\theta_C,\theta_R].
\]

- Tier A/B parameters may enter calibration and confirmatory UQ.
- Tier C assumptions are sensitivity-only.
- No probability distribution is chosen merely for convenience.
- Empirical/posterior distributions or documented ranges must be traceable to evidence.
- The same parameter/scenario draw is supplied to M0, M1 and M2.

Sampling starts from a reproducible Monte Carlo or low-discrepancy design and grows geometrically.

Stop only when the Monte Carlo 95% interval half-width for the primary paired representation statistic is no larger than

\[
0.1\,\epsilon_{decision},
\]

so stochastic sampling error is at least one order smaller than the frozen decision scale.

## 8. Global sensitivity analysis

Variance-based first-order and total-effect indices are used only after auditing input dependence.

For independent inputs,

\[
S_i=
\frac{\mathrm{Var}_{X_i}[\mathbb E(Y|X_i)]}
{\mathrm{Var}(Y)}.
\]

If substantial dependence exists, vanilla independent-input Sobol indices are not interpreted causally; parameters are grouped or a dependence-aware sensitivity method is required.

Sampling increases until the ranking of dominant parameters is stable across two consecutive sample-size levels and their bootstrap intervals no longer imply a rank reversal among the dominant factors.

## 9. Statistical comparison

All model differences are paired by scenario and parameter draw.

Primary uncertainty intervals use paired bootstrap/resampling over independent scenario/event units with **5,000 resamples** and 95% intervals.

Report:
- point estimate;
- 95% interval;
- full empirical distribution/quantiles;
- sign;
- scenario-stratified behavior;
- physical constraint residuals.

P-values, if shown, are secondary and never replace effect size + uncertainty + threshold comparison.

## 10. H1a decision rule

- **A0 — Verification:** all numerical, conservation, nesting and physical-admissibility gates pass.
- **A1 — Threshold validity:** \(\epsilon_P,\epsilon_T\) are frozen independently of model differences.
- **A2 — Primary effect:** the 95% paired interval for \(\Theta_{repr}\) lies completely above 1.
- **A3 — Robustness:** the conclusion survives predeclared UQ and is not generated solely by a post-hoc selected scenario.
- **A4 — Physical admissibility:** no apparent M2 advantage is obtained through greater constraint violation.

Adjudication:
- **SUPPORTED:** A0–A4 pass and thresholds include engineering tolerances.
- **REPRESENTATION-DISTINGUISHABLE:** A0–A4 pass but only detectability/resolution thresholds exist.
- **PARTIAL:** the effect is confined to a predeclared mechanism stratum.
- **NOT SUPPORTED:** the primary interval is not wholly above threshold or robustness/physics gates fail.

## 11. H1b held-out validation shell

H1b is not tested using synthetic self-generated truth alone.

Calibration and validation units must be independent events/cases, not separate time points from the same event.

No held-out observation may be used for parameter fitting, threshold derivation, model-structure modification, or scenario selection.

If the available event set cannot provide independent calibration events and at least two independent validation events for each mechanism class being claimed, H1b remains exploratory.

Primary held-out error:

\[
E_{PT}(M)
=
\frac1T
\int_0^T
\|\widehat S_M(t)-S_{obs}(t)\|_Wdt.
\]

\[
\Delta E=
E_{PT}(M_2)-\min\{E_{PT}(M_0),E_{PT}(M_1)\}.
\]

H1b requires the 95% paired interval for \(\Delta E\) to lie completely below \(-\epsilon_{pred}\), together with zero material physics violations, acceptable uncertainty calibration, identifiable or meaningfully bounded M2-specific parameters, and no test-data refitting.

If independent truth is unavailable, H1b is **NOT YET TESTABLE**.

## 12. Stopping and anti-bias rules

After pre-registration lock:
1. no primary outcome may change because another metric gives a stronger result;
2. no threshold may change after viewing confirmatory M0/M1/M2 differences;
3. no scenario may be removed because it weakens H1;
4. no M2 state/parameter may be added using held-out performance;
5. solver/time-step changes require re-running all three models;
6. substantive protocol changes create v2.0 while v1.0 remains archived;
7. benchmark tests remain verification only;
8. H1 cannot be called confirmed until the authenticated Scopus/WoS/Compendex/IEEE evidence branch is completed and reconciled.

## 13. Required confirmatory outputs

- immutable scenario registry;
- parameter/provenance registry;
- model/version/commit identifiers;
- random seeds or sequence identifiers;
- paired raw M0/M1/M2 outputs;
- physical/numerical residuals;
- UQ convergence audit;
- sensitivity indices + uncertainty;
- primary/secondary outcome tables;
- scenario-stratified results;
- gate-by-gate H1a adjudication;
- H1b validation only if independent truth exists.

## 14. Methodological grounding

This design follows the VVUQ separation of verification, validation and uncertainty quantification used in ASME computational-model credibility standards. Variance-based global sensitivity uses the Sobol/Saltelli framework. Common random numbers preserve paired comparisons and reduce stochastic comparison noise.

Key references:
- ASME. Verification, Validation and Uncertainty Quantification standards.
- Sobol, I. M. (2001). *Mathematics and Computers in Simulation, 55*, 271–280. DOI: 10.1016/S0378-4754(00)00270-6.
- Saltelli, A., et al. (2010). *Computer Physics Communications, 181*(2), 259–270. DOI: 10.1016/j.cpc.2009.09.018.
- Stout, N. K., et al. (2009). Common-random-number simulation comparison methodology.

## 15. Lock state

\[
\boxed{
M_0,M_1,M_2\ \text{verified}
\rightarrow
\text{H1 confirmatory design frozen}
\rightarrow
\textbf{threshold provenance acquisition}
\rightarrow
\textbf{confirmatory UQ execution}
}
\]

**Do not run final confirmatory H1a analysis until all threshold-provenance fields are populated and frozen.**
