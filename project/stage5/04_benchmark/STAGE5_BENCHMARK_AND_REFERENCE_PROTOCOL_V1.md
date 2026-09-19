# Stage 5 Benchmark and Reference Protocol v1

## Terminology

\[
\text{baseline}\neq\text{benchmark}\neq\text{reference solution}\neq\text{validation reference}\neq\text{oracle}\neq\text{ground truth}.
\]

- **Baseline**: existing method used for H3 comparison.
- **Benchmark problem**: standardized reproducible test system/scenario.
- **Reference solution**: numerically trusted solution of the same mathematical problem.
- **Validation reference**: independent evidence/high-fidelity qualified data.
- **Oracle**: ideal-information/control upper-bound diagnostic.
- **Ground truth**: known physical truth only where genuinely available.

## Conventional baseline

\[
R_{\rm curve}=
\left(
Q(t),L_{\rm svc},Q_{\min},T_{\rm rec}
\right)
\]

with each service retained separately unless aggregation is explicitly justified.

## Benchmark ladder

\[
\boxed{B_0\rightarrow B_1\rightarrow B_2\rightarrow B_3}
\]

- \(B_0\): 2–3 state mathematical verification problem with analytic/high-resolution reference.
- \(B_1\): reduced power and transport constituent systems.
- \(B_2\): small coupled P–T benchmark using only Stage-2/3 qualified mechanisms.
- \(B_3\): final qualified thesis case.

## Reference methods

Choose by mathematical structure:
- low-dimensional nonlinear: HJ/HJI or dynamic programming;
- linear/affine convex: controlled-invariant/polytope/Lagrangian set methods;
- bounded adversarial uncertainty: robust invariant/HJI differential-game formulation;
- stochastic low-dimensional: stochastic dynamic programming;
- high-dimensional coupled simulator: scenario/ensemble propagation plus verified reduced-order approximation.

No approximate method is promoted to a reference solution merely because it is convenient.
