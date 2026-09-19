# Stage 6 → Stage 7 Handoff Contract v2

> **SUPERSEDED — PROVENANCE ONLY (2026-09-20)**
> Active v4-aligned replacement is specified by the Stage-6 v3 authorities referenced in `project/stage6/README.md`. Do not use this file as the current H4/requirements/handoff/freeze authority.

**Status:** CANONICAL STAGE-6→7 HANDOFF — v2.1 ALIGNED  
**Effective date:** 2026-09-19  
**Purpose:** pass qualified intervention performance and sustainability consequences to Stage 7 without embedding a Stage-6 preference.

## 1. Handoff object

\`\`\`math
\boxed{
I_{6\to7}^{v2}
=
\left(
\mathcal A_6^{qual},
\Delta\mathfrak R,
\mathcal E_{\rm fx},
\mathcal E_{\rm fy},
\Delta\mathbf J_{\rm sus},
\mathcal K_{\rm sus}^{cand},
\mathbb U_6,
\Lambda_6,
\Pi_6
\right).
}
\`\`\`

## 2. Meanings

- \(\mathcal A_6^{qual}\): physically/causally admissible interventions;
- \(\Delta\mathfrak R\): resilience changes;
- \(\mathcal E_{\rm fx}\): target-attainment/effectiveness records;
- \(\mathcal E_{\rm fy}\): resource-efficiency records;
- \(\Delta\mathbf J_{\rm sus}\): separate sustainability consequences;
- \(\mathcal K_{\rm sus}^{cand}\): candidate requirements with provenance/status;
- \(\mathbb U_6\): uncertainty representation;
- \(\Lambda_6\): validity/claim limits;
- \(\Pi_6\): evidence/provenance map.

## 3. Per-intervention record

Each \(a_k\) passed to Stage 7 includes:

1. intervention ID and complete intervention definition;
2. qualification/physics status;
3. scenario/domain;
4. resilience change;
5. effectiveness target set;
6. effectiveness status/margins/coverage;
7. resource vector;
8. efficiency ratios/vector/Pareto information;
9. accessibility/social vector;
10. lifecycle energy;
11. lifecycle carbon;
12. lifecycle cost by perspective;
13. extended consequences where qualified;
14. uncertainty/scenario ranges;
15. applicable requirements and pass/fail/coverage;
16. data/factor versions;
17. validation status;
18. claim ceiling.

## 4. Legacy efficiency diagnostic mapping

The v1 \(\boldsymbol\eta_R\) object is retained only as a component of:

\`\`\`math
\mathcal E_{\rm fy}.
\`\`\`

It is no longer a substitute for the complete efficiency object.

## 5. No hidden weighting

\`\`\`math
\boxed{
I_{6\to7}^{v2}
\not\ni
w^\top
[
\mathcal E_{\rm fx},
\mathcal E_{\rm fy},
\mathbf J_{\rm sus}
]
}
\`\`\`

unless an explicit Stage-7 value model authorizes such weighting.

## 6. Requirement statuses

Retain:

- HARD-AUTHORITATIVE;
- HARD-ADOPTED-STAKEHOLDER;
- SOFT-TARGET;
- ENGINEERING-BENCHMARK;
- RESEARCH-SENSITIVITY;
- REPORT-ONLY.

No lower-authority target is silently promoted.

## 7. Uncertainty

Pass separate aleatory, epistemic, model, numerical and normative uncertainty. Probabilities are passed only where justified.

## 8. Handoff gate

\`\`\`math
\boxed{
G_{6-HANDOFF}
=
G_{\mathcal A}
\land
G_{\Delta R}
\land
G_{EFX}
\land
G_{EFY}
\land
G_{J}
\land
G_{K}
\land
G_{U}
\land
G_{\Lambda}
\land
G_{\Pi}.
}
\`\`\`

## 9. Stage-7 activation

Stage 7 design may proceed before Stage-6 empirical execution.

Final decision execution may use only intervention records whose required Stage-6 validity gates have passed.

## 10. Claim boundary

Stage 6 reports what each intervention achieves, what resources it uses, and what consequences follow. Stage 7 decides what should be selected under the declared decision model.
