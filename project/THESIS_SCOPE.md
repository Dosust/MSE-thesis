# MSE Thesis Scope

**Status:** CANONICAL CURRENT SCOPE — 2026-10-06  
**Canonical scope authority:** [`CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md`](CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md)  
**Current authority index:** [`CURRENT_THESIS_AUTHORITY_INDEX_V1.md`](CURRENT_THESIS_AUTHORITY_INDEX_V1.md)  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering

## Current system

```text
Power System P
↔
Physical Power–Transport Interfaces I_PT
↔
Electrified Transportation T
```

Current transport mode:

```text
Road transport
→ battery-electric road transportation
→ grid-connected EV charging
```

Status: **WORKING-FROZEN**.

Exact charging context remains **OPEN**.

## Current hazard

```text
Extreme heat
```

represented externally as:

```math
H(x,t).
```

Common heat exposure is not itself a P–T dependency.

## Current mathematical focus

```math
X(t)=[X_P^\top,Z^\top,X_T^\top]^\top,
```

```math
\dot X=F(X,H,u;\theta),
```

with derived state-time quantities:

```math
X(t)
\rightarrow
\{\tau_i^C,\delta_{ij},Q_P(t),Q_T(t)\}.
```

The active focus is therefore:

```text
physical state
+ time
+ transition timing
+ propagation timing
+ electricity/mobility service
```

## Engineering cycle

```text
Improve → Adapt → Restore → Learn → Improve
```

This is the thesis-defined engineering cycle.

## Current open objects

- exact charging context;
- exact physical/interface state variables;
- exact service metrics;
- exact interventions;
- final narrowed RQ/SO/H;
- final novelty claim;
- final case/data object.

## Historical scope

Earlier P–W–T–SW material, the September P–T–I–O seven-stage architecture, RQ1–RQ7/H1–H5 package, Austin/P3 work, and broad sustainability/transformation architecture are **historical/provenance material unless explicitly re-admitted** by the current scope amendment.

They are preserved; they are not current scope authority where they conflict with the 2026-10-06 amendment.
