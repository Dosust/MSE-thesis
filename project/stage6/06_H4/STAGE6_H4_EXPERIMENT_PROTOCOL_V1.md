# Stage 6 H4 Experiment Protocol v1

## 1. Canonical H4

H4: Across the prespecified intervention and scenario set, engineering interventions that produce meaningful resilience improvement are not equivalent in their sustainability consequence vectors; at least two resilience-effective interventions produce materially different accessibility, energy, carbon, or cost consequences under the declared comparison rule.

H4 tests consequence heterogeneity.

It does not test whether every intervention has a trade-off and it does not select the Stage-7 winner.

## 2. Experimental unit

An experimental unit is:

\[
e=
(
a_k,
\omega_s,
Y_0,
\mathfrak M^0,
u/\pi,
FU_6,
\mathcal B_{LC},
H_{LC}
).
\]

Only \(a_k\) changes across intervention arms unless another factor is explicitly declared.

## 3. Matched conditions

Freeze/share across arms:

\[
\boxed{
\mathcal G,
\mathbb I^{qualified},
F_{\mathcal G}^{m},
Y_0,
\eta,
\mathcal U_{\rm feas},
K,
G_{\rm rec},
F_{\rm unsafe},
FU_6,
\mathcal B_{LC},
H_{LC},
\Omega_6,
\text{data/factor versions}
}
\]

and use common random numbers when stochastic simulation permits.

## 4. Primary resilience-effectiveness screen

\[
\mathcal A_R^+
=
\left\{
a_k:
\Delta\mathcal M_R(a_k)\ge\delta_R
\right\}.
\]

\(\delta_R\) is frozen from Stage-5 engineering significance/numerical resolution before H4 confirmatory results.

If fewer than two qualified resilience-effective alternatives remain, the H4 consequence-heterogeneity test is:

\[
\boxed{\text{NOT TESTED}}
\]

under the thesis-wide prerequisite rule.

## 5. Primary sustainability outcomes

\[
\mathbf J_{\rm sus}^{core}
=
[
J_{\rm access},
J_{\rm energy},
J_{\rm carbon},
J_{\rm cost}
]^\top.
\]

Each component has a preregistered direction, unit, boundary and materiality threshold.

## 6. Material heterogeneity without arbitrary weights

For \(q\in\mathcal Q_6\), let \(\delta_{J,q}>0\) be the preregistered material difference in native units.

Define:

\[
\boxed{
D_J(a_i,a_j)
=
\max_{q\in\mathcal Q_6}
\frac{
\left|
\Delta J_q(a_i)-\Delta J_q(a_j)
\right|
}{
\delta_{J,q}
}
}
\]

This is not a sustainability utility score. It is a material-difference detector.

Primary H4 condition:

\[
\boxed{
\exists\,a_i,a_j\in\mathcal A_R^+,\quad
D_J(a_i,a_j)\ge1.
}
\]

No cross-dimension weights are required.

## 7. Preferred matched-effectiveness analysis

Where a sufficient intervention set exists, compare alternatives within a resilience-effectiveness band:

\[
\left|
\Delta\mathcal M_R(a_i)
-
\Delta\mathcal M_R(a_j)
\right|
\le\epsilon_R.
\]

This reduces confounding between “different sustainability consequence” and “simply much larger intervention effect.”

\(\epsilon_R\) is derived prospectively from Stage-5 resolution/engineering significance.

## 8. Social/distributional H4 reporting

For accessibility/social outcomes, do not test only:

\[
\bar A.
\]

Also retain:

\[
A_g,\qquad
g=1,\ldots,G,
\]

for preregistered groups/areas where data support them.

A favorable mean with a materially adverse declared group effect is reported explicitly; it is not hidden by averaging.

## 9. Uncertainty-aware comparison

For probabilistically justified uncertainty, report distributions/intervals for:

\[
\Delta J_q(a_k),
\quad
\Delta\mathcal M_R(a_k).
\]

For deep/epistemic uncertainty without defensible probabilities, report scenario/interval robustness rather than converting scenario frequency into probability.

H4 materiality thresholds are engineering/scientific thresholds, not p-value thresholds.

## 10. H4 adjudication

### Supported

At least two qualified resilience-effective alternatives exist and the preregistered consequence-heterogeneity criterion is met with the required uncertainty support.

### Not supported

At least two qualified resilience-effective alternatives exist, the test is valid/executable, and none meets the preregistered material-difference criterion.

### Not tested

Any prerequisite gate fails, including insufficient qualified alternatives, invalid boundary comparability, failed physical admissibility, missing core consequence data or failed VVUQ.

## 11. Diagnostics

Report:

- componentwise \(\Delta J_q\);
- resilience gain \(\Delta\mathcal M_R\);
- resource-efficiency ratios where mathematically admissible;
- group-level accessibility/social consequences;
- lifecycle-stage contribution;
- sensitivity/uncertainty;
- burden-shifting patterns.

No “best intervention” is concluded in Stage 6.
