# Claim–Evidence Register

**Purpose:** prevent unsupported claims, hidden assumptions, and retrospective evidence selection.

## Governing chain

```math
\boxed{
\text{Claim}
\rightarrow\text{Evidence}
\rightarrow\text{Mechanism}
\rightarrow\text{Mathematics}
\rightarrow\text{Assumptions}
\rightarrow\text{Test}
\rightarrow\text{Result}
\rightarrow\text{Engineering implication}.
}
```

## Epistemic status

| Label | Meaning |
|---|---|
| `[E]` | established by admissible external evidence |
| `[D]` | derived mathematically/logically from established material |
| `[H]` | hypothesis to be tested |
| `[P]` | thesis proposal/construct |
| `[A]` | explicit assumption |
| `[U]` | unresolved/uncertain |
| `[R]` | result produced by a frozen/declared experiment |

At proposal stage, `[R]` should be limited to already executed and explicitly identified method-development/verification results.

## Required fields

| Field | Description |
|---|---|
| Claim ID | stable identifier `C###` |
| Claim | exact wording |
| Status | `[E]/[D]/[H]/[P]/[A]/[U]/[R]` |
| Claim type | theoretical / physical / empirical / computational / sustainability / design |
| Source/evidence | source IDs or repository evidence objects |
| Mechanism | causal/physical warrant |
| Mathematical object | equation/model if applicable |
| Assumptions | explicit conditions |
| Validity domain | where claim applies |
| Rival/alternative | competing explanation/model |
| Test/falsification | what would challenge it |
| Uncertainty | evidence/model uncertainty |
| Thesis location | chapter/section |
| Artifact links | figure/table/equation/code/data IDs |
| Status date | last review date |

## Initial canonical claims

| ID | Claim | Status | Evidence / authority | Mathematical object | Test / gate | Thesis location |
|---|---|---|---|---|---|---|
| C001 | Power and transportation can exhibit directional and reciprocal cross-system dependencies | `[E]` | qualified interdependency/P–T literature; H1 evidence program | `\mathfrak I_{PT}` | evidence admissibility | Ch.2 |
| C002 | Dynamic causal P–T coupling can produce materially different trajectories from static/independent representations | `[H]` | H1 | `M_0,M_1,M_2` | H1 confirmatory test | Ch.3–5 |
| C003 | Information degradation and organizational constraints can alter the feasible response set | `[H]` | H2 evidence + Stage 4 theory | `\mathcal U(z_I,z_O)` | H2 | Ch.3–5 |
| C004 | Current service performance and future maintainability are not equivalent concepts | `[D/H]` | viability theory + H3 design | `\mathcal V,\rho,T_{\mathcal V}` | H3 | Ch.2–5 |
| C005 | Viability-sensitive interface ranking can outperform static structural rankings under equal budgets | `[P/H]` | thesis proposal | `S_{ij}^{\mathcal V}` | H4 | Ch.3–5 |
| C006 | Adaptive trigger-based transformation can improve robustness relative to fixed intervention sequences under declared deep uncertainty | `[H]` | H5 | `\boldsymbol\pi_{ST}` vs `\Pi_F` | H5 | Ch.3–5 |
| C007 | The seven-stage sequence is a thesis synthesis, not an already established literature framework | `[D/P]` | literature synthesis + project architecture | stages 1–7 | Chapter 2 synthesis | Ch.2–3 |
| C008 | The thesis framework must preserve constituent physics while standardizing cross-system interdependency representation | `[P]` | theoretical-foundation work | `\Sigma_\alpha,\mathfrak d,\mathfrak I` | theoretical + demonstrator validation | Ch.3 |

## Registration rule

Before a major new statement is promoted into Chapter 1, 2, 3, 6, or 7, it should receive a Claim ID or be traceable to an existing registered claim.

A literature citation alone does not automatically promote a claim to `[E]`; relevance, evidence type, population/system, validity domain and limitations must be checked.
