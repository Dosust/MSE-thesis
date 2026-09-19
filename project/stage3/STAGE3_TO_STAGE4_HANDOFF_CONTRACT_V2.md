# Stage 3 → Stage 4 Handoff Contract v2

**Status:** CANONICAL STAGE-3 DOWNSTREAM HANDOFF  
**Effective date:** 2026-09-19  
**Upstream:** Stage-3 scientific constitution v2  
**Downstream compatibility target:** project/stage4/00_governance/STAGE4_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md

## 1. Purpose

Stage 3 produces physical/dynamic truth and model provenance. Stage 4 converts that truth into observation, information, belief, organizational feasibility and control.

\`\`\`math
\boxed{
\text{dynamics}
\rightarrow
\text{observation/knowledge/action}.
}
\`\`\`

## 2. Exact mandatory handoff

The current Stage-4 authority requires:

\`\`\`math
I_4=
(
\mathcal G,
\mathbb I^{qualified},
\mathfrak M_3,
Y^{phys},
Q,
\Lambda_3
).
\`\`\`

Therefore Stage 3 freezes:

\`\`\`math
\boxed{
I_{3\to4}
=
(
\mathcal G,
\mathbb I^{qualified},
\mathfrak M_3,
Y^{phys},
Q,
\Lambda_3
).
}
\`\`\`

This tuple matches Stage 4 exactly.

## 3. Field meanings

### \(\mathcal G\)
Structural/dynamic network representation needed to interpret the trajectory, including time-dependent topology when relevant.

### \(\mathbb I^{qualified}\)
Evidence-qualified dependency set from Stage 2, preserving status/provenance. Stage 3 separately records which subset was ready and active.

### \(\mathfrak M_3\)
Selected Stage-3 model realization, including model-family, configuration and numerical-method identifiers needed for reproducibility.

### \(Y^{phys}\)

\`\`\`math
Y^{phys}=(x_P,x_T,z_{PT})
\`\`\`

under the current Stage-3 ontology.

### \(Q\)
Declared physical service/capability trajectory derived from Stage-3 truth.

### \(\Lambda_3\)
Maximum claim level supported by Stage-3 evidence/VVUQ for that realization.

## 4. Companion provenance payload

Retain:

\`\`\`math
\Pi_{3\to4}
=
(
ID_s,
m(t),
\mathbb I^{ready},
\mathbb I^{active}(t),
\mathbb U_3,
\Theta_{ref},
T_{ref},
VVUQ_{status},
version/hash
).
\`\`\`

This does not alter the exact six-field Stage-4 contract; it supports auditability.

## 5. Stage-boundary firewall

Stage 3 does not generate these as its epistemic/decision outputs:

\`\`\`math
\boxed{
y_t,\;
\mathcal I_t,\;
\widehat Y_t,\;
b_t,\;
z_I(t),\;
z_O(t),\;
\mathcal U_{feas}(t),\;
u_t^{policy}.
}
\`\`\`

They belong to Stage 4.

## 6. Physical truth versus observation

Stage 4 constructs observation from truth, for example:

\`\`\`math
y_k
=
\Gamma_k h^{m_k}(Y_k^{phys};\theta_H)+\nu_k.
\`\`\`

Therefore:

\`\`\`math
\boxed{
Y^{phys}\neq y\neq\widehat Y\neq b_t.
}
\`\`\`

## 7. Dependency status preservation

\`\`\`math
\boxed{
\mathbb I^{active}(t)
\subseteq
\mathbb I_3^{ready}
\subseteq
\mathbb I^{qualified}.
}
\`\`\`

Stage 4 may know the qualified set but cannot silently reinterpret a mechanism excluded from the realized Stage-3 dynamics as active physical coupling.

## 8. Uncertainty separation

Stage-3 model/physical uncertainty remains attached to the truth/model through the companion provenance payload.

Stage 4 adds observation/estimation uncertainty.

\`\`\`math
\boxed{
\mathbb U_3
\neq
\mathbb U_{\widehat Y}.
}
\`\`\`

They may be propagated jointly later, but cannot be collapsed without derivation.

## 9. Control boundary

A prescribed Stage-3 input \(u^{exo}\) is scenario/model input.

Stage-4 policy output is a different object.

\`\`\`math
\boxed{
u^{exo}
\neq
u_t^{policy}.
}
\`\`\`

## 10. Claim inheritance

Stage 4 cannot make upstream physical-dynamics claims stronger than \(\Lambda_3\).

If Stage 3 is only verified/synthetic, Stage 4 may analyze sensing/control over that synthetic truth but may not call the underlying trajectory empirically validated.

## 11. Handoff gate

\`\`\`math
\boxed{
G_{3\to4}
=
G_{\mathcal G}
\land
G_{\mathbb I}
\land
G_{\mathfrak M}
\land
G_Y
\land
G_Q
\land
G_{\Lambda}
\land
G_{\Pi}.
}
\`\`\`

At design level, schema compatibility may PASS while case values remain DEFERRED. At execution, every mandatory field must be bound to a versioned realization.

## 12. Failure behavior

If a mandatory handoff object is unavailable/unqualified, the corresponding Stage-4 case claim is BLOCKED.

A missing object cannot be replaced with a pseudo-value unless explicitly labeled SYNTHETIC/ASSUMED and the claim ceiling is lowered accordingly.

## 13. Claim boundary

This contract establishes cross-stage compatibility. It does not close Stage 3 or Stage 4 empirically.
