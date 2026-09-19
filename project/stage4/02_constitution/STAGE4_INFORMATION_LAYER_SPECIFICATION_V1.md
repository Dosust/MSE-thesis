# Stage 4 Information-Layer Specification v1

\`\`\`math
\boxed{\mathcal G_I(t)=(V_I,E_I(t))}
\`\`\`

is communication topology;

\`\`\`math
\boxed{z_I(t)}
\`\`\`

is information-system state; and

\`\`\`math
\boxed{\mathcal I_t=\{y_{0:t},messages,forecasts,reports\}}
\`\`\`

is information actually available to the estimator/operator.

\`\`\`math
\boxed{\mathcal G_I\neq z_I\neq\mathcal I_t.}
\`\`\`

Latency and freshness are distinct:

\`\`\`math
\tau_i^{info}=t_i^{recv}-t_i^{send},\qquad
\Delta_i(t)=t-u_i(t).
\`\`\`

Every case realization declares timing semantics, availability/loss, quality, and whether values are empirical, derived, synthetic, scenario-defined, or missing.
