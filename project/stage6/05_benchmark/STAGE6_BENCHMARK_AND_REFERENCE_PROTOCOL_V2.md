# Stage 6 Benchmark and Reference Protocol v2

**Status:** CANONICAL STAGE-6 v2 BENCHMARK PROTOCOL  
**Effective date:** 2026-09-19  
**Supersedes for active benchmark semantics:** v1 benchmark protocol.

## 1. Terminology firewall

\`\`\`math
\boxed{
\text{baseline}
\neq
\text{benchmark}
\neq
\text{reference}
\neq
\text{validation evidence}
\neq
\text{requirement threshold}.
}
\`\`\`

## 2. Benchmark ladder

\`\`\`math
\boxed{
B_{6,0}
\rightarrow
B_{6,1}
\rightarrow
B_{6,2}
\rightarrow
B_{6,3}.
}
\`\`\`

### B6,0 — accounting/unit fixtures

Verify:

- units/signs;
- present-value identities;
- activity × factor identities;
- accessibility hand cases;
- requirement logic;
- effectiveness PASS/FAIL logic;
- efficiency denominator/ratio guards.

### B6,1 — subsystem consequence benchmark

Verify consequence calculations for P-side and T-side intervention cases independently.

Must include, where applicable:

\`\`\`math
\Delta\mathfrak R,\quad
\mathcal E_{\rm fx},\quad
\mathcal E_{\rm fy},\quad
\Delta\mathbf J_{\rm sus}.
\`\`\`

### B6,2 — coupled P–T intervention benchmark

A controlled coupled benchmark using Stage-2/3-qualified mechanisms.

Required outputs:

\`\`\`math
\boxed{
a_k
\rightarrow
(
\Delta\mathfrak R,
\mathcal E_{\rm fx},
\mathcal E_{\rm fy},
\Delta\mathbf J_{\rm sus}
).
}
\`\`\`

Purpose:

- verify intervention propagation;
- verify target-attainment logic;
- verify resource-performance calculations;
- verify consequence accounting;
- test cross-domain double-counting controls.

### B6,3 — final qualified Stage-6 case

Purpose:

- execute H4 under the frozen intervention-performance architecture;
- generate the Stage6→7 qualified handoff.

## 3. Effectiveness reference tests

At least one hand-checkable target-attainment example must verify:

- operator direction;
- unit;
- threshold;
- aggregation rule;
- uncertainty classification;
- PASS/FAIL result.

If probabilistic/coverage semantics are used, their reference calculation must also be reproducible.

## 4. Efficiency reference tests

For every resource-performance ratio used, include:

- a positive stable denominator fixture;
- a near-zero denominator rejection fixture;
- a sign-change/uncertain-denominator fixture where relevant;
- a vector/Pareto comparison example.

No arbitrary epsilon may be inserted to make an unstable ratio computable.

## 5. Sustainability references

Retain v1 environmental, carbon, accessibility/social and cost reference calculations.

All external factors retain source/version/provenance.

## 6. Benchmark gate

\`\`\`math
\boxed{
G_{B6}
=
G_{\rm units}
\land
G_{\rm balance}
\land
G_{\rm boundary}
\land
G_{\rm baseline}
\land
G_{\rm EFX}
\land
G_{\rm EFY}
\land
G_{\rm no-double-count}
\land
G_{\rm reference}
\land
G_{\rm uncertainty}.
}
\`\`\`

## 7. No benchmark cherry-picking

The benchmark set is frozen before confirmatory H4 result inspection.

A benchmark is not removed because it produces an unfavorable intervention result.

## 8. Claim boundary

Passing benchmark tests verifies the method at the declared level; it does not prove that a real intervention is effective, efficient or sustainable.
