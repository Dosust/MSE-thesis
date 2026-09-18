# Architecture-Methods Scope

**Status:** ACTIVE COMPANION / NOT A SECOND SOURCE OF TRUTH  
**Canonical scope:** [`../../project/THESIS_SCOPE.md`](../../project/THESIS_SCOPE.md)  
**Canonical framework:** [`../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`](../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md)

This directory implements **small, auditable computational scaffolds** for the frozen P–T–I–O thesis framework. It does not define an alternative thesis scope.

## Canonical system

```math
\mathcal S=\{P,T,I,O\},
```

where $P,T$ are the physical Power and Transportation systems and $I,O$ are the informational and organizational layers.

The canonical state is

```math
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix}.
```

The computational chain supported by this directory is

```math
\mathbb I
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
(\widehat Y,\mathcal U,u)
\rightarrow
\mathfrak R_T
\rightarrow
(a_k,\Delta\mathfrak R,\Delta\mathbf J_{\rm sus})
\rightarrow
\mathcal A_{R,S}^{\star}.
```

## What belongs here

| Content | Purpose |
|---|---|
| Julia scaffold | transparent toy P–T–I–O coupled dynamics for software QA |
| Python geometry utilities | finite-dimensional viability/geometry baselines and smoke tests |
| configuration/schema files | machine-readable contracts aligned with the frozen framework |
| CI checks | syntax, configuration, rendering and scientific-drift checks |

## What does **not** belong here

This folder must not reintroduce superseded P–W–T–SW, waste–drainage, or other historical architectures. Historical models remain in Git history/archive only.

The toy code in this folder is **not a calibrated case study and not thesis evidence**. It exists to test software interfaces, notation, numerical plumbing and reproducibility before the validated numerical demonstrator is specified.
