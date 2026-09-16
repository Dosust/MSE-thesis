# Canonical Notation Translation Layer v1.0

**Date:** 2026-09-16  
**Status:** ACTIVE CONTROLLED MIGRATION LAYER  
**Purpose:** prevent legacy Stage-2 notation from re-entering active thesis prose, equations, figures, code, or experiments while preserving historical/frozen source files as provenance.  
**Authority:** `CANONICAL_DEPENDENCY_CONTRACT_V1.md` > `CANONICAL_SYSTEM_DEFINITION.md` > `CANONICAL_7_STAGE_FRAMEWORK.md` > this translation layer > legacy/supporting files.

## 1. Migration principle

The repository contains historically valid reasoning documents that predate the current dependency contract. They are retained for provenance and must not be silently rewritten when doing so could obscure the evolution of the research.

Therefore migration is implemented as a controlled semantic translation layer:

```math
\boxed{
\text{legacy source}
\xrightarrow{\;\mathcal T_{\rm notation}\;}
\text{canonical active interpretation}
}
```

This layer changes notation and authority only. It does **not** change H1–H5 logic, the seven-stage order, the P–T–I–O ontology, or any empirical result.

## 2. Canonical Stage-2 dependency object

A directed dependency is

```math
\boxed{
\mathfrak d_e
=
(\mathcal C_e,\Sigma_e,\Pi_e)
}
```

with active dependency set

```math
\boxed{
\mathbb I(t)=\{\mathfrak d_e(t):e\in\mathcal E(t)\}.
}
```

The superseded flat tuple

```math
\mathfrak I_{ij}^{\alpha\beta}
=
(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t)
```

is provenance notation only and must not be used as an active primitive.

## 3. Translation rules

### T1 — one directed dependency

Legacy:

```math
\mathfrak I_{ij}^{\alpha\beta}
```

Active interpretation:

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e).
```

### T2 — a dependency/interdependency collection

Legacy shorthand:

```math
\mathfrak I
```

Active interpretation when a set is intended:

```math
\mathbb I=\{\mathfrak d_e\}.
```

Reciprocal or mediated interdependency is represented by the relevant directed dependencies and paths; it is not a new universal edge primitive.

### T3 — mechanism semantics

Use

```math
\boxed{
\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e)
}
```

where:

- `\Phi_e` is the executable mechanism/operator;
- `\gamma_e` is the activation/guard semantics;
- `\theta_e` contains only mechanism-relevant physical/empirical parameters;
- `\zeta_e` contains declared auxiliary/internal interface state where required.

There is no universal parameter vector

```math
(w_{ij},\delta_{ij},\tau_{ij},a_{ij}).
```

Delay, characteristic time, strength, memory and switching enter only when the mechanism physically requires them and are typed inside the canonical semantics.

### T4 — dynamic mapping

Legacy chains such as

```math
\mathfrak I\rightarrow F_{\mathcal G}^{m}
```

must be read as

```math
\boxed{
\mathbb I(t)
\rightarrow
\{\Phi_e\}_{e\in\mathcal E(t)}
\rightarrow
F_{\mathcal G}^{m}
}
```

with constituent-system physics preserved independently.

### T5 — H1 interpretation

The scientific logic of H1 is unchanged. The active chain is

```math
\boxed{
\text{qualified evidence}
\rightarrow
\mathfrak d_e
\rightarrow
\Phi_e
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
\{M_0,M_1,M_2\}
\rightarrow
\text{matched empirical/decision value}.
}
```

The contribution is not the existence of directed or typed dependencies; those are prior art.

### T6 — viability/interface sensitivity

The universal weight derivative

```math
-\frac{\partial\rho}{\partial w_{ij}}
```

is not canonical.

For a smooth, physically defined mechanism parameter direction `v`, use

```math
\boxed{
S_{e,v}^{\mathcal V}(Y)
=
-D_{\theta_e}\rho_g(Y;\Theta)[v].
}
```

For discrete switches, topology changes, permissions, routing changes or other nonsmooth mechanisms, use finite perturbation or actual intervention contrasts.

### T7 — regime object

Use

```math
\boxed{
\mathfrak M_k
=
(\mathcal S_k,\mathcal G_k,\mathbb I_k,F_k,\Theta_k,K_{{\rm sus},k},\mathcal U_k).
}
```

Strategic actions that alter dependency architecture use an explicitly typed transformation component such as

```math
a_k^{\mathbb I},
```

which is distinct from the Stage-2 guard `\gamma_e` and from operational control `u(t)`.

## 4. Files governed by this translation layer

Until an in-place notation-only rewrite is deliberately approved, this translation layer governs active interpretation of legacy notation in:

- `MATHEMATICAL_FOUNDATION.md`;
- `RESEARCH_HYPOTHESES.md`;
- `MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`;
- `FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`;
- `HYPOTHESIS_REFINEMENT_AFTER_ASU_AUDIT_V1.md`;
- `PUBLIC_NOVELTY_FALSIFICATION_F0_F1_F2_V1.md`.

The v1 provenance amendments remain historical evidence and are not active notation authorities.

## 5. Compilation rule

Any thesis prose, figure, code, table, equation, experiment, or automated extraction built after this file must satisfy:

```math
\boxed{
\text{legacy symbol encountered}
\Rightarrow
\mathcal T_{\rm notation}(\text{legacy symbol})
\text{ before scientific use}.
}
```

No final-thesis artifact may present the flat legacy tuple as the current dependency primitive.

## 6. Scientific invariants preserved

The following are unchanged:

```text
H1–H5 scientific logic;
seven-stage order and responsibilities;
P,T,I,O system ontology;
structure != causality != dynamics;
operational control u(t) != strategic transformation a_k;
current performance != future maintainability;
robust viability != stochastic viability;
provenance of earlier repository states.
```

## 7. Migration verification checklist

A new active artifact passes notation control only if:

1. one dependency uses `\mathfrak d_e`, not the flat tuple;
2. dependency collections use `\mathbb I` where a set is intended;
3. mechanism parameters are typed through `\Sigma_e`/`\theta_e` rather than a universal weight-delay-timescale-activation vector;
4. activation uses `\gamma_e` when referring to Stage-2 mechanism guards;
5. H4 sensitivity uses a declared physical perturbation direction or finite intervention contrast;
6. regime objects contain `\mathbb I_k`;
7. operational `u(t)` and strategic `\mathbf a_k` remain distinct;
8. no notation change is interpreted as evidence of novelty or empirical validation.

## 8. Status

```text
CANONICAL AUTHORITY: PASS
TRANSLATION RULES: PASS
LEGACY PROVENANCE PRESERVED: PASS
ACTIVE THESIS COMPILATION PROTECTED: PASS
IN-PLACE HISTORICAL FILE REWRITE: NOT REQUIRED FOR ACTIVE INTERPRETATION
SCIENTIFIC LOGIC CHANGE: NONE
```
