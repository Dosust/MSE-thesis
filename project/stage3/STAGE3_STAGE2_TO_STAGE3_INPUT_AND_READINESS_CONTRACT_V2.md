# Stage 3 — Stage 2→3 Input and Readiness Contract v2

**Status:** CANONICAL STAGE-3 INPUT CONTRACT — DESIGN/PROTOCOL  
**Effective date:** 2026-09-19  
**Upstream authority:** \`project/CANONICAL_DEPENDENCY_CONTRACT_V1.md\`; \`project/stage2/STAGE2_G2_GATE_SPECIFICATION_V1.md\`  
**Downstream authority:** \`project/stage3/STAGE3_SCIENTIFIC_CONSTITUTION_V2.md\`  
**Scope:** case-independent Stage-2 causal-object admission into Stage-3 executable dynamics.  
**Empirical effect:** none. This contract freezes semantics and gates only; it does not qualify any new mechanism or parameter.

## 1. Purpose

Stage 2 answers whether a directed mechanism is causally defensible in a declared case. Stage 3 requires an additional question:

> Is the causally qualified mechanism sufficiently specified, bounded, typed, and implementable for the intended dynamic calculation?

Therefore:

\`\`\`math
\boxed{
G_2^{causal}(e,c)=PASS
\;\not\Rightarrow\;
G_{2\to3}(e,c)=PASS.
}
\`\`\`

A mechanism may be causally supported while numerical execution remains blocked.

## 2. Canonical Stage-2 object

Every directed dependency enters this gate only in the active canonical form

\`\`\`math
\boxed{
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)
}
\`\`\`

with

\`\`\`math
\mathcal C_e=(s_e,p_e^s,r_e,p_e^r,\chi_e),
\`\`\`

\`\`\`math
\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e),
\`\`\`

\`\`\`math
\Pi_e=(\mathcal P_e,V_e,\mathcal U_e).
\`\`\`

The superseded flat dependency representation may appear only in explicit migration/provenance notes. It is not an admissible active Stage-3 input.

## 3. Stage-3-ready dependency object

Define the Stage-3 implementation record

\`\`\`math
\boxed{
\mathfrak d_e^{(3)}
=
\left(
\mathfrak d_e,
\Xi_e,
\tau_e^{char},
\Lambda_e^{impl},
S_e^{2\to3}
\right),
}
\`\`\`

where:

| Field | Meaning |
|---|---|
| \(\mathfrak d_e\) | the causally governed Stage-2 dependency object |
| \(\Xi_e\) | verified executable realization of the causal semantics for the selected model family |
| \(\tau_e^{char}\) | optional characteristic mechanism timescale when scientifically meaningful; not a universal primitive |
| \(\Lambda_e^{impl}\) | implementation validity domain and numerical/physical restrictions |
| \(S_e^{2\to3}\) | final readiness status: PASS, BLOCKED, or FAIL |

\(\tau_e^{char}\) is metadata derived from the mechanism/system model when relevant. A causal delay remains inside \(\theta_e\) or the operator history domain as specified by the canonical dependency contract.

## 4. Executable realization

Stage 3 does not replace the Stage-2 semantics. It compiles them:

\`\`\`math
\boxed{
\mathcal X_3:
(\Sigma_e,\mathfrak M_3)
\mapsto
\Xi_e.
}
\`\`\`

Admissible \(\Xi_e\) realizations include, depending on the model family:

- an ODE/DAE term;
- an algebraic coupling relation;
- a hybrid reset or guard-triggered transition;
- a topology/capacity update;
- an event/discrete-state transition;
- an FMI/HELICS or equivalent co-simulation mapping;
- another explicitly verified numerical function.

The implementation technology is not causal evidence:

\`\`\`math
\boxed{
\Xi_e\text{ executable}
\;\not\Rightarrow\;
\mathfrak d_e\text{ empirically valid}.
}
\`\`\`

## 5. Readiness gate

For intended case \(c\) and intended Stage-3 model use \(m\),

\`\`\`math
\boxed{
G_{2\to3}(e,c,m)
=
G_2^{causal}
\land G_{\Phi}
\land G_{\theta}
\land G_{\mathcal U}
\land G_{\rm unit}
\land G_{\rm time}
\land G_{\rm impl}
\land G_{\rm valid}.
}
\`\`\`

### 5.1 Component gates

| Gate | PASS | BLOCKED | FAIL |
|---|---|---|---|
| \(G_2^{causal}\) | current Stage-2 causal gate PASS | decisive causal evidence unavailable | Stage-2 causal claim rejected |
| \(G_{\Phi}\) | response/operator semantics explicit enough for intended model use | form plausible but unresolved | form contradicts physics/evidence or is circular |
| \(G_{\theta}\) | every required parameter is fixed, bounded, calibrated, or explicitly represented as uncertainty at sufficient status for intended use | required parameter remains unestimated/unsupported | parameterization violates known domain/physics |
| \(G_{\mathcal U}\) | uncertainty/bounds/provenance declared for influential unresolved quantities | required uncertainty characterization missing | uncertainty treatment is demonstrably invalid |
| \(G_{\rm unit}\) | exchanged quantities, ports, signs, and dimensions are compatible | unit/type mapping incomplete | dimensional/type inconsistency |
| \(G_{\rm time}\) | activation, delay/history, event ordering and required timescale semantics are defined | timing semantics incomplete | timing semantics contradict the mechanism |
| \(G_{\rm impl}\) | executable mapping \(\Xi_e\) exists and passes minimum verification fixtures | implementation absent/incomplete | implementation fails verification |
| \(G_{\rm valid}\) | implementation is used only inside declared spatial/temporal/asset/operating domain | applicability unresolved | intended use lies outside justified domain |

Stage-2 falsification and provenance obligations remain inherited and cannot be weakened by Stage 3.

## 6. Aggregate status logic

\`\`\`text
if any decisive gate = FAIL
    -> S_e^(2→3) = FAIL
else if any required gate = BLOCKED
    -> S_e^(2→3) = BLOCKED
else if all required gates = PASS
    -> S_e^(2→3) = PASS
else
    -> workflow state remains OPEN until adjudicated
\`\`\`

The final handoff uses only PASS/BLOCKED/FAIL. OPEN is a workflow state, not an executable status.

## 7. Admissible Stage-3 dependency sets

Define

\`\`\`math
\boxed{
\mathbb I_{3}^{ready}
=
\{\mathfrak d_e^{(3)}:S_e^{2\to3}=PASS\}.
}
\`\`\`

For auditability also retain

\`\`\`math
\mathbb I_{3}^{blocked}
=
\{\mathfrak d_e^{(3)}:S_e^{2\to3}=BLOCKED\},
\`\`\`

\`\`\`math
\mathbb I_{3}^{failed}
=
\{\mathfrak d_e^{(3)}:S_e^{2\to3}=FAIL\}.
\`\`\`

Only \(\mathbb I_3^{ready}\) may be instantiated as accepted dynamic causal coupling in an \(M_2\) case realization.

## 8. Minimum record required per dependency

Every Stage2→3 audit record must contain:

\`\`\`text
dependency_id
case_id / applicability domain
source entity + source port
receiver entity + receiver port
carrier/service/action
Phi_e response/operator definition
gamma_e activation rule
theta_e parameter record IDs
zeta_e memory/internal-state rule, if used
causal delay/history semantics, if used
characteristic timescale, if reported
uncertainty record IDs
units/sign convention
executable realization / implementation pointer
verification fixtures
validation/evidence status
validity domain
falsifier/revision condition
S_e^(2→3)
reviewer/date/version/provenance
\`\`\`

Unknown values remain explicitly unresolved. No undocumented default may convert BLOCKED to PASS.

## 9. Required implementation verification

Before \(G_{\rm impl}=PASS\), the executable realization must satisfy all applicable tests:

\`\`\`math
\Phi_e=0
\Rightarrow
\text{declared uncoupled receiver limit},
\`\`\`

\`\`\`math
\gamma_e=0
\Rightarrow
\text{dependency inactive},
\`\`\`

and, where delay is present,

\`\`\`math
\delta_e\to0
\Rightarrow
\text{declared zero-delay limit}.
\`\`\`

Also require as applicable:

- unit and sign consistency;
- conservation/balance consistency;
- event-order consistency;
- bounded-domain behavior;
- timestep/communication-step sensitivity;
- reproducibility.

## 10. H1 comparator consequence

For any scenario \(s\),

\`\`\`math
\boxed{
\mathbb I_s^{active}
\subseteq
\mathbb I_3^{ready}.
}
\`\`\`

Therefore an \(M_2\) scenario may not activate a BLOCKED or FAILED mechanism.

\(M_1\) may contain a declared static/algebraic comparator abstraction, but such a comparator must not be described as evidence that a blocked dynamic causal mechanism is qualified.

\(M_0\) contains no cross-system causal coupling by definition.

## 11. Failure behavior

### BLOCKED
A BLOCKED relation is retained in the audit ledger but excluded from accepted \(M_2\) execution. The scientific status is:

\`\`\`text
NOT READY FOR STAGE-3 EXECUTION
\`\`\`

not causal falsification.

### FAIL
A FAIL relation is excluded from accepted Stage-3 use in the declared domain. Re-entry requires new evidence and a versioned re-audit.

### Missing parameter or uncertainty
Missing parameter evidence is never filled by tuning to obtain a desired H1 result.

## 12. Current case illustration — status only, not a new freeze

The current Stage-3 audit records that \(EV_{T\to P}\) has causal support but remains blocked at Stage2→3 readiness because parameter/uncertainty binding is incomplete. Other candidate mechanisms currently blocked at Stage 2 remain excluded.

This statement records existing status; this v2 contract does not promote or demote any mechanism.

## 13. Stage2→3 handoff object

The case-independent handoff schema is

\`\`\`math
\boxed{
I_{2\to3}
=
(
\mathcal G,
\mathbb I_3^{ready},
\mathbb I_3^{blocked},
\Pi_{2\to3},
\Lambda_2
).
}
\`\`\`

Only \(\mathbb I_3^{ready}\) can drive accepted Stage-3 causal dynamics. The blocked ledger is carried solely for traceability and future evidence closure.

## 14. Prohibited shortcuts

The following cannot produce \(G_{2\to3}=PASS\):

- spatial proximity alone;
- graph adjacency alone;
- correlation alone;
- a literature mechanism family without case binding;
- existence of executable software;
- successful code execution;
- fitting a free parameter to Stage-3 target outputs;
- using blocked relations because a scenario template expects them.

## 15. Claim boundary

This contract establishes only **admission/readiness semantics**.

It does not establish:

- correctness of any case parameter;
- validity of a final Stage-3 model family;
- predictive superiority of \(M_2\);
- empirical cascade/recovery behavior;
- H1 support;
- resilience/viability conclusions.

Those require later case realization, VVUQ, reference qualification, and confirmatory execution.
