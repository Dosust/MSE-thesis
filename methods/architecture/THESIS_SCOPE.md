# Architecture-Methods Scope

**Status:** ACTIVE COMPANION / NOT A SECOND SOURCE OF TRUTH  
**Canonical scope:** [`../../project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`](../../project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md) + [`../../project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md`](../../project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md)  
**Canonical framework:** [`../../project/CONCEPTUAL_FRAMEWORK_SPEC_V3.md`](../../project/CONCEPTUAL_FRAMEWORK_SPEC_V3.md) + [`../../project/MATHEMATICAL_FRAMEWORK_SPEC_V1.md`](../../project/MATHEMATICAL_FRAMEWORK_SPEC_V1.md)

This directory implements **small, auditable computational scaffolds**. It does not define an alternative thesis scope. Legacy P–T–I–O toy scaffolds in this folder remain software-QA/provenance artifacts and must defer to the current Power–Electrified Transportation scope authorities above.

## Canonical system

Current active physical-system boundary:

> **In this thesis, the electrified transportation system comprises the electrically propelled road vehicle, its rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, the vehicle power-supply circuit, electric-vehicle supply equipment, the physical charging connection, and the communication and control functions required for electrical power transfer, including bidirectional transfer where supported (ISO 6469; ISO 5474; ISO 15118; IEC 61851; IEC 62196).**

For active thesis interpretation, EVSE belongs to `T_e`; cross-system coupling/interface variables do not constitute a third physical system. The older `P,T,I,O` toy state below is retained only to document the legacy software scaffold and must not override current thesis scope.


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
