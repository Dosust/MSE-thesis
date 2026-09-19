# Stage 7 — Stage 6→7 Input and Admissibility Contract v2

> **SUPERSEDED — PROVENANCE ONLY (2026-09-20)**
> Active v4-aligned replacement is the corresponding Stage-7 v3 protocol referenced in `project/stage7/README.md`.

**Status:** CANONICAL STAGE-7 INPUT / ADMISSIBILITY CONTRACT — DESIGN/PROTOCOL  
**Effective date:** 2026-09-19  
**Upstream authority:** \`project/stage6/09_handoff/STAGE6_TO_STAGE7_HANDOFF_CONTRACT_V2.md\`  
**Controlling authorities:** RQ/SO/H v3; seven-stage framework v2; intervention-performance amendment v2.1.  
**Empirical effect:** none. This contract freezes decision-entry semantics only.

## 1. Exact upstream input

Stage 7 consumes the Stage-6 v2 handoff without redefining it:

\`\`\`math
\boxed{
I_{6\to7}^{v2}
=
(
\mathcal A_6^{qual},
\Delta\mathfrak R,
\mathcal E_{\rm fx},
\mathcal E_{\rm fy},
\Delta\mathbf J_{\rm sus},
\mathcal K_{\rm sus}^{cand},
\mathbb U_6,
\Lambda_6,
\Pi_6
).
}
\`\`\`

No field may be silently dropped, merged, scalarized, or relabeled.

## 2. Candidate-record object

For each candidate intervention \(a_k\),

\`\`\`math
\boxed{
\mathbf Z_7(a_k)
=
(
a_k,
\Delta\mathfrak R^{a_k},
\mathcal E_{\rm fx}^{a_k},
\mathcal E_{\rm fy}^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k},
F^{a_k},
\mathbb U^{a_k},
\Lambda^{a_k},
\Pi^{a_k}
).
}
\`\`\`

where \(F^{a_k}\) is the Stage-7 feasibility/admissibility state.

## 3. Feasibility before preference

Define

\`\`\`math
\boxed{
G_{7,F}(a_k)
=
G_{\rm physical}
\land
G_{\rm technical}
\land
G_{\rm resource}
\land
G_{\rm requirement}
\land
G_{\rm implementation}
\land
G_{\rm validity}.
}
\`\`\`

Only applicable, evidence-supported gates are activated. A missing non-applicable gate is not automatically a failure.

The admissible candidate set is

\`\`\`math
\boxed{
\mathcal A_7^{adm}
=
\{a_k\in\mathcal A_6^{qual}:G_{7,F}(a_k)=PASS\}.
}
\`\`\`

## 4. Status semantics

- **PASS:** all mandatory feasibility conditions are supported and satisfied.
- **FAIL:** a validly evaluated mandatory condition is violated.
- **BLOCKED:** a mandatory feasibility condition cannot yet be evaluated.
- **NOT APPLICABLE:** a condition is outside the declared intervention/domain.
- **OPEN:** workflow state awaiting adjudication; not executable as PASS.

## 5. Permanent distinctions

\`\`\`math
\boxed{
\text{infeasible}
\neq
\text{dominated}
\neq
\text{unpreferred}.
}
\`\`\`

- infeasible: violates mandatory admissibility;
- dominated: feasible but worse/equal on all declared comparison dimensions and strictly worse on at least one;
- unpreferred: may be feasible and nondominated but rejected under an explicitly declared value/preference model.

## 6. Qualification and evidence inheritance

Stage 7 cannot increase the upstream claim ceiling:

\`\`\`math
\boxed{
\Lambda_7(a_k)
\le
\Lambda_6(a_k)
}
\`\`\`

for claims depending on Stage-6 quantities.

A Stage-6 quantity marked synthetic, benchmark-only, uncertain, or unresolved retains that status downstream.

## 7. Common-arm admissibility for H5

For the primary H5 contrast, both decision arms use the same:

- candidate universe;
- feasibility gate;
- Stage-6 evidence versions;
- effectiveness/efficiency records;
- uncertainty domain;
- scenario set;
- normalization rules for quantities common to both arms.

Only the information explicitly designated by the H5 comparator protocol may differ.

## 8. Feasibility uncertainty

If a mandatory condition is uncertain, Stage 7 must distinguish:

- probabilistic feasibility when probabilities are justified;
- interval/set/scenario feasibility when they are not;
- epistemically BLOCKED cases when evidence is insufficient.

Scenario frequency is not probability.

## 9. No pseudo-admission

The following cannot create PASS:

- missing Stage-6 values filled with convenient defaults;
- stakeholder preference used to waive a physical requirement;
- Pareto dominance used to excuse infeasibility;
- high resilience used to override a hard safety/requirement constraint;
- software solvability used as evidence of real-world feasibility.

## 10. Protected DEFERRED fields

This contract does not freeze:

- final intervention set;
- final case feasibility values;
- stakeholder preferences;
- final H5 decision sets;
- preferred intervention;
- H5 result.

## 11. Claim boundary

This contract determines which intervention records may enter Stage-7 decision analysis. It does not decide which intervention should be implemented.
