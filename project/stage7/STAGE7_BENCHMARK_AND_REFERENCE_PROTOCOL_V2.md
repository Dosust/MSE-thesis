# Stage 7 — Benchmark and Reference Protocol v2

**Status:** CANONICAL STAGE-7 BENCHMARK PROTOCOL  
**Effective date:** 2026-09-19

## 1. Benchmark ladder

\`\`\`math
\boxed{
B_{7,0}
\rightarrow
B_{7,1}
\rightarrow
B_{7,2}
\rightarrow
B_{7,3}.
}
\`\`\`

## 2. B7,0 — analytic decision fixtures

Hand-checkable fixtures must verify:
- feasibility filtering;
- dominance/Pareto membership;
- Jaccard set distance;
- regret;
- scenario-coverage robustness;
- normalization/value-model arithmetic when activated.

Claim ceiling: implementation verification only.

## 3. B7,1 — synthetic intervention table

Use a small synthetic intervention matrix with known:
- feasible/infeasible alternatives;
- dominated/nondominated alternatives;
- sustainability-induced set change;
- regret ordering.

Claim ceiling: decision-engine verification/synthetic validation only.

## 4. B7,2 — full synthetic Stage6→7 handoff

Construct a complete synthetic

\`\`\`math
I_{6\to7}^{v2}
\`\`\`

and verify:
- all fields consumed without collapse;
- H5 arms differ only by sustainability information;
- uncertainty propagated according to declared semantics;
- value firewall preserved;
- Stage-7 outputs and claim ceilings correct.

## 5. B7,3 — qualified thesis case

Only B7,3 may support confirmatory H5 once:
- Stage-6 empirical inputs are qualified;
- H5 metric/materiality are preregistered;
- scenario/uncertainty semantics are frozen;
- Stage-7 VVUQ passes.

## 6. Reference calculations

Independent hand calculations should exist for:
- at least one Pareto fixture;
- one Jaccard-distance fixture;
- one regret fixture;
- one robustness-coverage fixture;
- one weight/normalization sensitivity fixture if a value model is activated.

## 7. Benchmark gate

\`\`\`math
\boxed{
G_{B7}
=
G_{\rm feasible}
\land
G_{\rm pareto}
\land
G_{\rm H5metric}
\land
G_{\rm regret}
\land
G_{\rm robust}
\land
G_{\rm value}
\land
G_{\rm uncertainty}.
}
\`\`\`

\(G_{\rm value}\) is PASS when a value model is correctly implemented or NOT APPLICABLE when no value model is authorized.

## 8. Claim boundary

A correct decision algorithm does not validate upstream physical or sustainability models and does not establish that one intervention should be implemented.
