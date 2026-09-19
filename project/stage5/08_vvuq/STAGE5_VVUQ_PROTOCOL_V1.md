# Stage 5 VVUQ Protocol v1

Verification, validation and uncertainty quantification are separate credibility questions.

## Required numerical chain

\[
R_{\rm ref}
\rightarrow
\text{grid refinement}
\rightarrow
\text{time refinement}
\rightarrow
\text{set convergence}
\rightarrow
\text{probability convergence}
\rightarrow
\text{full-model consistency}.
\]

## Set convergence

Candidate diagnostics:

\[
d_H(\mathcal V_h,\mathcal V_{h/2}),
\]

\[
\mu(\mathcal V_h\triangle\mathcal V_{h/2}),
\]

and the analogous quantities for reachability sets.

## Probability convergence

Report Monte-Carlo/ensemble uncertainty for:

\[
P_{\rm viable},\qquad P_{\rm recover}.
\]

Confidence/credible intervals or justified finite-sample bounds must accompany estimates.

## Reduced-model fidelity

\[
G_{5-RM}:
\quad
Z_5(\Pi_R(Y))\approx Z_5(Y)
\]

for preregistered Stage-5 QOIs and target-set classifications.

## Validation

Validation is against held-out trajectories, empirical evidence where available, or a qualified higher-fidelity reference. Benchmark agreement alone is not validation.

## Thresholds

No numerical convergence/validation tolerances are frozen here. They must be derived from reference-solution convergence, pilot computation, measurement/model uncertainty and engineering significance before confirmatory execution.
