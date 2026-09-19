# Stage 2 Interdependency Scope / Effect Amendment v1.1

**Date:** 2026-09-19  
**Status:** CANONICAL NARROW AMENDMENT — DERIVED METADATA ONLY  
**Parent authority:** `STAGE2_CASE_INDEPENDENT_CAUSAL_GOVERNANCE_CONTRACT_V1.md` and `../CANONICAL_DEPENDENCY_CONTRACT_V1.md`  
**Evidence basis:** Hall et al. (2016); Ibáñez et al. (2010)  
**Empirical effect:** none.

## 1. No change to the dependency primitive

The canonical dependency remains

```math
\boxed{
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e).
}
```

This amendment adds only auditable derived classifications.

## 2. Interaction-role metadata

```math
\boxed{
\kappa_e^{role}
\in
\{\mathrm{OPERATION},\mathrm{RECOVERY},\mathrm{PLANNING}\}.
}
```

A mechanism may receive more than one role when justified, but each assignment must state the modeled timescale and thesis-stage use.

Role classification does **not** imply:

```math
G_2(e)=PASS
```

or

```math
G_{2\to3}(e)=PASS.
```

## 3. Effect-class metadata

```math
\boxed{
\kappa_e^{effect}
\subseteq
\{
\mathrm{CAPACITY},
\mathrm{FLOW},
\mathrm{DEMAND},
\mathrm{DELAY},
\mathrm{ACCESSIBILITY},
\mathrm{SERVICE},
\mathrm{RECOVERY},
\mathrm{COST},
\mathrm{OTHER}
\}.
}
```

Multiple effects are allowed. The actual carrier/service remains governed by \(\chi_e\); the actual causal response remains governed by \(\Phi_e\).

## 4. Stage ownership

- Stage 2 qualifies whether the directed mechanism is causal in the declared case.
- Stage 3 executes only the physical/functional consequences needed by RQ3 and only after Stage2→3 readiness PASS.
- Recovery-role dependencies may affect restoration/recovery dynamics when qualified.
- Planning/economic effects are not silently inserted into H1 physical dynamics; they belong to later planning/intervention/decision analysis unless explicitly modeled and gated.

## 5. Transportation recovery-access minimum semantics

A repair-access candidate cannot be reduced to road adjacency. Its case claim must identify, where applicable:

```text
damaged asset
→ field task requirement
→ access point
→ mobile resource / crew
→ origin/depot
→ admissible route set
→ time-varying road/traffic state
→ arrival / repair-start consequence.
```

This requirement is consistent with the existing Q06 BLOCKED status: missing case task/resource/access mappings cannot be invented by simulation.

## 6. Non-binary consequence rule

```math
\boxed{
\text{dependency consequence}
\neq
\text{binary failure by default}.
}
```

Continuous, categorical, event-driven, hybrid or set-valued effects are admissible when supported by the mechanism and intended model use.

## 7. Claim boundary

This amendment classifies mechanisms; it does not add, delete or promote a parent mechanism family, change a G2 result, parameterize a response law, or authorize Stage-3 execution.
