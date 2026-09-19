# Stage 6 Benchmark and Reference Protocol v1

> **STAGE-6 v2.1 AUTHORITY ALIGNMENT — 2026-09-19**
>
> SUPERSEDED FOR ACTIVE STAGE-6 BENCHMARK GOVERNANCE by `STAGE6_BENCHMARK_AND_REFERENCE_PROTOCOL_V2.md`.


## 1. Terminology firewall

\[
\boxed{
\text{baseline}
\neq
\text{benchmark problem}
\neq
\text{reference calculation}
\neq
\text{validation evidence}
\neq
\text{requirement threshold}
}
\]

Baseline: the counterfactual used to compute incremental intervention consequences.

Benchmark problem: a reproducible problem used to verify the Stage-6 methodology.

Reference calculation: an analytically/independently trusted calculation for the same quantity.

Validation evidence: independent evidence used to assess adequacy for the intended real-system claim.

Requirement threshold: a normative/engineering limit with separate provenance.

## 2. Stage-6 benchmark ladder

\[
\boxed{
B_{6,0}
\rightarrow
B_{6,1}
\rightarrow
B_{6,2}
\rightarrow
B_{6,3}
}
\]

### B6,0 — hand-verifiable accounting benchmark

A small synthetic intervention with known:

- material quantities;
- energy;
- emission factors;
- cost streams;
- travel-time/accessibility values.

Required checks:

\[
\text{manual calculation}
\approx
\text{implemented calculation}.
\]

Purpose: unit/accounting verification.

### B6,1 — constituent intervention benchmark

Power and transportation interventions evaluated separately.

Purpose:

- confirm environmental and cost accounting;
- test accessibility method on a small network;
- test intervention physical admissibility;
- audit functional-unit consistency.

### B6,2 — coupled P–T intervention benchmark

A small coupled benchmark using only Stage-2/3-qualified mechanisms.

Purpose:

- rerun intervention through coupled dynamics;
- measure \(\Delta\mathfrak R\);
- evaluate \(\Delta\mathbf J_{\rm sus}\);
- test consequence propagation and double-counting controls.

### B6,3 — final qualified Stage-6 case

The final intervention set on the qualified thesis P–T case.

Purpose: H4 execution and Stage-7 handoff.

## 3. Reference calculations

### Environmental

Use hand-calculated activity × factor identities for simple benchmark flows:

\[
I=\sum_r A_r EF_r.
\]

Where an LCA engine/database is used, benchmark selected flows against independent source values.

### Carbon

Use independent activity data and authoritative/peer-reviewed factors. For U.S. electricity where appropriate, EPA eGRID / GHG Emission Factors Hub can serve as factor references.

### Accessibility

Use a small graph for which shortest-path/generalized-cost and opportunity counts can be independently calculated.

### Cost

Use closed-form present-value checks on known streams:

\[
PV=
C_0+\sum_y\frac{C_y}{(1+r)^y}.
\]

### Social distribution

Use constructed group-level accessibility/service values with hand-checkable gaps and inequality metrics before applying the method to the full case.

## 4. Benchmark pass requirements

At minimum:

\[
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
G_{\rm no-double-count}
\land
G_{\rm reference}
\land
G_{\rm uncertainty}.
\]

No benchmark is promoted to validation evidence merely because the implementation reproduces itself.

## 5. External practice references

ISO 14040/14044 provide the environmental LCA framework.

ISO 14067 provides climate-footprint requirements/guidance.

ISO 15686-5 provides life-cycle-costing guidance for constructed assets.

ISO/TS 14076:2025 provides current environmental techno-economic assessment guidance emphasizing common production basis/functional unit, transparent boundaries, assumptions, parameters and sensitivity analysis.

NIST SP 1197 provides resilience-investment economic comparison with the status quo and uncertainty.

EPA TRACI supplies LCIA characterization factors for multiple environmental impact categories.

## 6. No benchmark cherry-picking

The final benchmark set is frozen before confirmatory H4 results.

A benchmark cannot be removed because it makes the thesis intervention look unfavorable.
