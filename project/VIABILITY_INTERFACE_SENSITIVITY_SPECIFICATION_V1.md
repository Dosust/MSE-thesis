# Viability Interface Sensitivity Specification v1.0

**Date:** 2026-09-16  
**Status:** WORKING MATHEMATICAL SPECIFICATION — metric/functional and empirical ranking not yet frozen  
**Stage:** 5, with intervention validation in Stages 4/6/7 as appropriate  
**Canonical dependency authority:** `CANONICAL_DEPENDENCY_CONTRACT_V1.md`

## 1. Purpose

Define interface-level viability sensitivity in a form consistent with the canonical dependency contract and with prior art on viability-boundary distance, geometric robustness and kernel sensitivity.

The thesis does **not** claim novelty for distance to a viability boundary, geometric robustness, or generic sensitivity analysis of viability kernels.

## 2. Parameterized viability object

Let the verified coupled model be parameterized by

```math
\Theta
=
(\vartheta_P,\vartheta_T,\{\Sigma_e\}_{e\in\mathcal E},\Theta_I,\Theta_O),
```

where every dependency semantic object is

```math
\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e).
```

The viable set is therefore written explicitly as

```math
\mathcal V_{\rm sus}(\Theta).
```

This makes clear that changing an interface mechanism can change the viable set itself.

## 3. Baseline viability margin

For a declared state-space metric `g`, define

```math
\boxed{
\rho_g(Y;\Theta)
=
d_g\!\left(
Y,\partial\mathcal V_{\rm sus}(\Theta)
\right).
}
```

The baseline metric must be the simplest defensible scaling/geometry. A physics-informed or learned metric `g_psi` is a candidate model that must outperform or clarify a declared baseline; it is not automatically preferred.

## 4. Canonical local sensitivity

A universal scalar dependency weight `w_e` is prohibited as a primitive because the canonical dependency contract does not define one universally.

For a differentiable parameterization and a declared perturbation direction `v` in the admissible parameter subspace of `theta_e`, define

```math
\boxed{
S_{e,v}^{\mathcal V}(Y;\Theta)
=
- D_{\theta_e}\rho_g(Y;\Theta)[v].
}
```

Interpretation:

> positive `S_{e,v}^V` means the declared worsening perturbation moves the current state closer to loss of viability, according to the chosen margin convention.

The sign convention must be checked for every perturbation definition.

## 5. Finite perturbation for nonsmooth/hybrid mechanisms

If differentiability is not established, use

```math
\boxed{
S_{e,v,\varepsilon}^{\mathcal V}(Y;\Theta)
=
-\frac{
\rho_g(Y;\Theta_{e,\varepsilon v})
-
\rho_g(Y;\Theta)
}{\varepsilon}.
}
```

where `Theta_{e,epsilon v}` changes only the declared mechanism aspect under test.

For discrete guards, topology changes, authorization changes or event logic, use an intervention/ablation contrast rather than forcing a derivative.

## 6. Intervention-value quantity

Local sensitivity is a diagnostic, not sufficient evidence that an intervention is valuable.

For intervention `a` targeting dependency `e`, define an actual viability functional change

```math
\boxed{
\Delta\mathcal M_{\mathcal V}(e,a;\omega)
=
\mathcal M_{\mathcal V}^{after}(e,a;\omega)
-
\mathcal M_{\mathcal V}^{before}(\omega).
}
```

where `omega` is the declared scenario/future and `M_V` is a prespecified scalar viability functional.

Possible `M_V` choices include:

```text
state-specific boundary margin;
normalized viable-set measure;
time-to-viability loss;
robust viable coverage over a declared initial-condition set;
posterior viable mass, when observation uncertainty is the decision object.
```

The primary H4 functional must be chosen before confirmatory testing.

## 7. Equal-budget ranking rule

Interface rankings are compared only under matched intervention constraints.

Let

```math
\mathcal A_B
=
\{a:C(a)\le B\}
```

be the equal-budget admissible intervention set.

Compare candidate ranking `R_V` against at least:

```math
R_{deg},
\qquad
R_{bet},
\qquad
R_{flow/load},
\qquad
R_{static-dependency},
```

and a random/null comparator where useful.

The confirmatory comparison uses the same intervention budget, scenario set, physical model and evaluation functional for all rankings.

## 8. Scenario aggregation

If scenario probabilities are independently justified,

```math
\operatorname{Agg}_{\Omega}
=
\mathbb E_{\omega\sim p(\omega)}.
```

Under deep uncertainty without justified probabilities, use a declared robustness/satisficing statistic such as worst-case, regret, quantile over an unweighted scenario ensemble, or fraction of scenarios satisfying declared criteria. Do not call an unweighted scenario fraction a probability.

## 9. Metric comparison gate

Because geometric robustness is prior art, any candidate `g_psi` must be tested against a baseline `g_0`.

At minimum evaluate:

```math
\rho_{g_0},
\qquad
\rho_{g_\psi},
```

for:

```text
unit/scale invariance;
physical interpretability;
numerical conditioning;
ranking stability;
predictive warning value;
intervention-selection value.
```

If `g_psi` adds no material decision value, retain `g_0`.

## 10. Perturbation provenance

Every perturbation direction or intervention must state:

```text
dependency ID e;
canonical object affected: Phi_e, gamma_e, theta_e, zeta_e or C_e;
physical meaning;
units;
baseline value/state;
perturbed value/state;
intervention feasibility;
source/evidence;
uncertainty;
cost/resource requirement.
```

A dimensionless perturbation should be normalized using a physically meaningful scale, not an arbitrary numerical normalization.

## 11. H4 falsification

H4 is challenged when the viability-sensitive ranking does not provide prespecified additional intervention value over simpler rankings under matched budgets and scenarios.

Formally, for ranking `R_V` and baselines `R_b`, a candidate rule is

```math
\operatorname{Agg}_{\Omega}
\left[\Delta\mathcal M_{\mathcal V}^{(R_V)}\right]
-
\max_b
\operatorname{Agg}_{\Omega}
\left[\Delta\mathcal M_{\mathcal V}^{(R_b)}\right]
\ge\delta_4,
```

where `delta_4` must be frozen from engineering/statistical justification before confirmatory evaluation.

## 12. Verification gates

Before interpreting `S_e^V`:

1. `V_sus` computation must be verified/converged;
2. the metric must be declared and scaled consistently;
3. perturbation direction must be physically admissible;
4. finite-difference step sensitivity must be checked;
5. derivative and finite-perturbation results should agree in smooth test cases;
6. topology/guard changes must use discrete contrasts rather than invalid derivatives;
7. ranking stability under parameter uncertainty must be reported;
8. intervention validation must use the actual post-intervention dynamics, not the sensitivity score alone.

## 13. Prior-art boundary

Existing literature already establishes:

```text
distance to viability-kernel boundaries;
geometric robustness of viability kernels/resilience basins;
parameter/constraint sensitivity of viability kernels;
using safe/viable-set proximity in control decisions.
```

Representative prior art includes Alvarez & Martin's geometric robustness work and later robustness-map formulations in viability theory.

The unresolved thesis candidate is narrower:

> whether perturbations of evidence-grounded infrastructure dependency mechanisms can produce a validated interface ranking that improves intervention decisions beyond simpler structural/flow/dependency rankings in a coupled P–T system.

## 14. Current status

```text
CANONICAL PARAMETERIZATION: CONSISTENT
LOCAL/FINITE SENSITIVITY DEFINITIONS: SPECIFIED
PRIMARY VIABILITY FUNCTIONAL: NOT FROZEN
METRIC g_psi: NOT JUSTIFIED/FROZEN
K_sus / V_sus: NOT YET COMPUTED
H4 EMPIRICAL/CONFIRMATORY TEST: DEFERRED
GLOBAL NOVELTY: UNRESOLVED
```
