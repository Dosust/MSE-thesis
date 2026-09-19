# Stage 3 Directional Interface-State Amendment v2.2

**Date:** 2026-09-19  
**Status:** CANONICAL NARROW MATHEMATICAL AMENDMENT — DESIGN/PROTOCOL ONLY  
**Parent authorities:** `STAGE3_STATE_INPUT_OUTPUT_QOI_ONTOLOGY_V2.md`; `STAGE3_SCIENTIFIC_CONSTITUTION_V2.md`; `STAGE3_DESIGN_PROTOCOL_FREEZE_V2.md`  
**Scientific effect:** notation/type clarification only; no case mechanism, parameter, validation result or H1 result changes.

## 1. Problem corrected

The frozen v2 package writes the physical truth as

```math
Y_3^{phys}=(x_P,x_T,z_{PT}).
```

That aggregate symbol can be misread as requiring one common interface state for all reciprocal P–T mechanisms. This would conflict with the directional dependency contract because \(P\to T\) and \(T\to P\) can have different mechanism states, dimensions, units, activation, delays and memory.

## 2. Current interface-state object

Define

```math
\boxed{
z_{\mathbb I}(t)
=
\operatorname{col}
\left\{
\zeta_e(t):
e\in\mathbb I^{active}(t),
\ \zeta_e\neq\varnothing
\right\}.
}
```

Only Stage2→3-ready mechanisms may contribute an accepted interface state.

If no active ready mechanism requires independent memory,

```math
z_{\mathbb I}=\varnothing.
```

## 3. Directional grouping

When useful,

```math
\boxed{
z_{\mathbb I}
=
\operatorname{col}
\left(
z_{P\to T},
z_{T\to P},
z_{other}
\right),
}
```

where each block is itself mechanism-indexed.

There is no requirement that

```math
z_{P\to T}=z_{T\to P}.
```

## 4. Corrected physical truth notation

Current controlled interpretation is

```math
\boxed{
Y_3^{phys}(t)
=
\left(
x_P(t),
x_T(t),
z_{\mathbb I}(t)
\right).
}
```

The old \(z_{PT}\) remains a compatibility alias meaning "aggregate P–T interface-memory container" only.

## 5. Mechanism mapping

For each ready dependency,

```math
\mathfrak d_e
\xrightarrow{G_{2\to3}}
\mathfrak d_e^{(3)}
\xrightarrow{\mathcal X_3}
\Xi_e.
```

If \(\zeta_e\) has an evolution law,

```math
\dot\zeta_e
=
g_e(\zeta_e,x_P,x_T,m,\eta,u^{exo};\vartheta_e),
```

or an admissible discrete/hybrid equivalent is used.

Memoryless mechanisms contribute no artificial state.

## 6. H1 consequence

M0/M1/M2 definitions are unchanged. The amendment only requires that the M2 "dynamic" distinction be attributable to **ready mechanism-specific temporal state/history**, not to a generic interface variable with ambiguous semantics.

## 7. Stage-4 boundary

Information and organizational states remain Stage-4 objects:

```math
z_{\mathbb I}^{physical}
\neq
z_I
\neq
z_O
\neq
b_t.
```

## 8. Current case status

No current Greensboro dependency is promoted by this amendment.

```text
EV_T_to_P      G2 PASS      Stage2→3 BLOCKED
EV_P_to_T      G2 BLOCKED   Stage2→3 BLOCKED
SIGNAL_P_to_T  G2 BLOCKED   Stage2→3 BLOCKED
REPAIR_T_to_P  G2 BLOCKED   Stage2→3 BLOCKED
```

Therefore accepted case M2 coupling remains unauthorized until a dependency reaches Stage2→3 PASS.

## 9. Claim boundary

```math
\boxed{
\text{directional state clarification}
\neq
\text{causal promotion}
\neq
\text{implementation verification}
\neq
\text{H1 support}.
}
```
