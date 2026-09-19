# Stage 7 — Adaptive Pathway Eligibility Protocol v2

**Status:** CONDITIONAL STAGE-7 EXTENSION PROTOCOL  
**Effective date:** 2026-09-19

## 1. Canonical role

Adaptive transformation is a secondary Stage-7 extension.

\`\`\`math
\boxed{
\text{adaptive pathways}
\neq
\text{mandatory Stage-7 method}.
}
\`\`\`

The primary H5 one-stage/static decision comparison is addressed first.

## 2. Eligibility gate

\`\`\`math
\boxed{
G_{7,ADAPT}
=
G_{\rm sequential}
\land
G_{\rm information-update}
\land
G_{\rm timing}
\land
G_{\rm irreversibility}
\land
G_{\rm data}
\land
G_{\rm computational}.
}
\`\`\`

Where:
- \(G_{\rm sequential}\): decisions genuinely occur in multiple stages;
- \(G_{\rm information-update}\): future observations can alter subsequent choices;
- \(G_{\rm timing}\): intervention timing matters materially;
- \(G_{\rm irreversibility}\): lock-in, lead time, option value, or path dependence is relevant;
- \(G_{\rm data}\): state/transition/update evidence is adequate;
- \(G_{\rm computational}\): sequential analysis can be verified and sensitivity-tested.

## 3. Eligibility outcomes

- PASS: adaptive analysis is scientifically justified.
- BLOCKED: sequential relevance exists but required information is incomplete.
- FAIL/NOT REQUIRED: the one-stage decision formulation is adequate for the declared question.

Failure to activate adaptive analysis is not a thesis defect.

## 4. Conditional state transition

If PASS:

\`\`\`math
\mathfrak M_{k+1}
=
\mathcal T_{a_k}(\mathfrak M_k,\xi_k),
\`\`\`

with decision history

\`\`\`math
a_1\rightarrow a_2\rightarrow\cdots\rightarrow a_n.
\`\`\`

Every transition must define state, information, uncertainty, lead time, cost/resource use, feasibility and revision conditions.

## 5. Trigger semantics

An adaptive trigger must be:
- measurable/observable;
- linked to a decision;
- temporally available before the decision;
- associated with explicit threshold/decision logic;
- uncertainty-aware;
- prospectively frozen for confirmatory use.

No trigger is invented solely to improve retrospective performance.

## 6. Method selection

MPC, robust adaptive pathways, MDP/POMDP, real-options or other methods are admissible only when their assumptions match the problem.

Algorithm sophistication is not evidence of scientific appropriateness.

## 7. H5 separation

Unless separately preregistered, adaptive pathway results are supporting Stage-7 analysis and do not replace or redefine the primary H5 comparison.

## 8. Protected DEFERRED fields

Remain DEFERRED:
- adaptive triggers;
- transition probabilities without evidence;
- pathway horizon;
- sequencing rule;
- option values;
- preferred pathway.
