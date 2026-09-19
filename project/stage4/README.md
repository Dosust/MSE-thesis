# Stage 4 — Observation, State Estimation, Organization and Control

**RQ4:** *How is the system observed, interpreted, coordinated and controlled?*  
**SO4:** Evaluate how observation, state estimation, information availability, organizational constraints and feasible control affect response timing, service trajectories and recovery.  
**Evidence obligation:** H2.  
**Stage architecture status:** \`FINALIZED_V1\`  
**Case/empirical closure status:** \`NOT CLOSED / BLOCKED BY UPSTREAM AND CASE EVIDENCE\`.

## Governing rule

\`\`\`math
\boxed{
Q_4\rightarrow\mathcal C_4\rightarrow\mathcal R_4(D)\rightarrow G_4\rightarrow Z_4\rightarrow\Lambda_4\rightarrow I_{4\to5}
}
\`\`\`

Data may **block, qualify, calibrate, or validate** a scientific object; data do not define the object merely because they are available.

\`\`\`math
\boxed{D_{available}\not\rightarrow\mathcal C_4},\qquad
\boxed{D_{available}\rightarrow\mathcal R_4^{case}}
\`\`\`

## Authority chain

1. \`project/CANONICAL_7_STAGE_FRAMEWORK_V2.md\`
2. \`project/CANONICAL_RQ_SO_HYPOTHESES_V3.md\`
3. \`project/RESEARCH_REASONING_PROTOCOL.md\`
4. \`project/EGMIV_METHOD_V1.md\`
5. \`00_governance/STAGE4_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md\`
6. \`00_governance/STAGE4_GATE_SPECIFICATION_V1.md\`
7. \`02_constitution/*\` — data-independent Stage-4 specifications
8. \`03_cases/*\` — case/data realization and H2 execution
9. \`04_handoff/*\` — claim ceiling, closure, Stage-5 handoff

## Scientific constitution

\`\`\`math
\boxed{
\mathcal C_4=
(Y_4^{req},\mathcal H,\mathcal O_{obs},\mathcal I,\mathcal E,
\mathbb U_{\widehat Y},\mathcal G_I,\mathfrak O,
\mathcal U_{feas},\Pi)
}
\`\`\`

The canonical chain is

\`\`\`math
\boxed{
Y_t^{phys}\xrightarrow{\mathcal H}y_t\rightarrow\mathcal I_t
\xrightarrow{\mathcal E}b_t
\rightarrow z_O(t)
\rightarrow\mathcal U_{feas}(t)
\xrightarrow{\Pi}u_t
}
\`\`\`

with operational feedback

\`\`\`math
\boxed{u_t\rightarrow Y_{t+1}^{phys}.}
\`\`\`

## Current case result

The current GreenEVT/SMART-DS case retains only \`EV_T_to_P\` as Stage-2 causal PASS. The Stage-2→3 readiness of that mechanism and the exact Stage-3 state/model class remain incomplete. Consequently the Stage-4 **architecture is frozen**, but estimator selection, case observability closure, H2 execution, and Stage-4→5 empirical handoff remain blocked or not tested.

No downstream file may upgrade that claim ceiling without the required gates.
