# Stage 4 Observation Specification v1

## Observation model

\`\`\`math
\boxed{y_k=\Gamma_k h^{m_k}(Y_k^{phys};\theta_H)+\nu_k}
\`\`\`

Every observation preserves

\`\`\`math
\boxed{d_{j,k}^{obs}=(y_{j,k},t_{j,k}^{meas},t_{j,k}^{recv},\gamma_{j,k},q_{j,k},source_{j,k}).}
\`\`\`

For an LTI model,

\`\`\`math
\mathcal O=[C;CA;\dots;CA^{n-1}],\qquad rank(\mathcal O_{req})=n_{req}.
\`\`\`

For nonlinear/time-stepped models use an appropriate finite-horizon/local observability Jacobian; for continuous nonlinear models use an appropriate local rank construction where its assumptions hold. For hybrid systems, test every H2/Stage-5 relevant mode.

State classifications are \`DIRECTLY_OBSERVED\`, \`ESTIMABLE\`, \`PARTIALLY_OBSERVABLE\`, or \`UNOBSERVABLE\`.

No estimator is selected before the required-state, observation-map, and observability constitution are adequate for meaningful comparison.
