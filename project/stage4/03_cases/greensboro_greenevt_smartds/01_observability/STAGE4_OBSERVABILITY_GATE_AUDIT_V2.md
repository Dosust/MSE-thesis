# Stage 4 Observability Gate Audit v2 — Greensboro/GreenEVT/SMART-DS

**Scope:** case realization only. General observability mathematics belongs to \`02_constitution/STAGE4_OBSERVATION_SPECIFICATION_V1.md\`.

| Gate | Result | Current evidence | Closure requirement |
|---|---|---|---|
| \`G_state\` | BLOCKED | Q05 objects trace upstream; exact Stage-3 state/model class remains open | freeze case-bound Stage-3 model/state and rebind \(Y_4^{req}\) |
| \`G_measurement\` | BLOCKED | source logs exist for Q05; P/T measurement emulation only provisional | freeze sensor/log placement, timing, noise, missingness |
| \`G_mapping\` | OPEN | Q05 mapping and candidate observation equations exist | complete dimensionally consistent \(h\) for all required states |
| \`G_rank/structural\` | BLOCKED | tests specified | execute after \(F/h/Y_4^{req}\) freeze |
| \`G_mode\` | BLOCKED | hybrid semantics generic | test every H2/Stage-5 relevant mode |
| **\`G4-OBS-case\`** | **BLOCKED** | prerequisites incomplete | close gates in causal order |

\`\`\`math
\boxed{G_{4-OBS}^{case}=BLOCKED}
\`\`\`

Interpretation: **NOT TESTED**, not evidence that the system is unobservable.
