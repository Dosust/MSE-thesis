# Stage 4 Estimation and Uncertainty Specification v1

\`\`\`math
\boxed{b_t=\mathcal E(\mathcal I_t,\mathfrak M_3)}
\`\`\`

When probabilistic assumptions are justified,

\`\`\`math
b_t(Y)=p(Y_t\mid\mathcal I_t).
\`\`\`

A point estimate is a summary of \(b_t\), not the definition of Stage 4.

\`\`\`math
\boxed{\mathbb U_{\widehat Y,t}\in\{\Sigma_t,\widehat{\mathcal X}_t^\alpha,\text{interval},\text{ensemble/particles},\ldots\}}
\`\`\`

The uncertainty representation must follow estimator assumptions; covariance is not imposed universally. Validation requires state error where a reference exists, uncertainty calibration/coverage, robustness to missing/delayed observations, numerical verification, benchmark/held-out validation, and a declared validity domain.

Estimator families remain candidates until case observability/model/data requirements are frozen. AI/ML is not a default substitute for observability or physics.
