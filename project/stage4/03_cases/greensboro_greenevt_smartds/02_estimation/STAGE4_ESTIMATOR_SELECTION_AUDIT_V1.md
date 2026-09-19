# Stage 4 Estimator Selection Audit v1

**Decision:** \`SELECTION NOT AUTHORIZED / BLOCKED\`.

Estimator selection is downstream of the required-state, measurement, and observability constitution. Current case observability is not yet executable because the exact Stage-3 state/model class and Stage-4 sensor configuration are not frozen.

Candidate families retained for later assumption-compatible comparison include WLS/DSSE, Kalman-family methods, particle filtering, moving-horizon estimation, set-valued/robust estimation, and distributed estimation. No family is selected merely because it appears in the literature.

Selection criterion when authorized:

\`\`\`math
\boxed{
J_E=(\text{physics compatibility},\text{observability},\text{nonlinearity},\text{timing},\text{uncertainty output},\text{computation},\text{validation})
}
\`\`\`

A cross-system estimator is required only if RQ4/H2 needs joint P–T inference; separate constituent estimators remain admissible.
