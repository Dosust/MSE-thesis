# Legacy Dependency Notation Migration Audit v2.0

**Date:** 2026-09-16  
**Status:** ACTIVE MIGRATION AUDIT / NO SCIENTIFIC LOGIC CHANGE  
**Authority:** `CANONICAL_DEPENDENCY_CONTRACT_V1.md` > `CANONICAL_SYSTEM_DEFINITION.md` > `CANONICAL_7_STAGE_FRAMEWORK.md` > supporting files

## 1. Purpose

The canonical Stage-2 dependency representation is

```math
\boxed{\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)}
```

and the active dependency set is

```math
\boxed{\mathbb I(t)=\{\mathfrak d_e(t):e\in\mathcal E(t)\}.}
```

Several older supporting files still contain the superseded flat object

```math
\mathfrak I_{ij}^{\alpha\beta}
=(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t)
```

or assume a universal interface parameter vector

```math
\theta_{ij}=(w_{ij},\delta_{ij},\tau_{ij},a_{ij}).
```

Those formulas are provenance/legacy notation. They must not be interpreted as current Stage-2 authority.

## 2. Audit results

| File | Current role | Legacy issue found | Migration status |
|---|---|---|---|
| `MATHEMATICAL_FOUNDATION.md` | current compact cross-stage foundation | Section 2 still defines flat `I_ij`; Section 11 uses `theta_ij=(w,delta,tau,a)`; Stage-6/7 regime objects use legacy `mathfrak I` | **MIGRATION REQUIRED** |
| `RESEARCH_HYPOTHESES.md` | canonical H1–H5 logic | H1 still prints the flat Stage-2 object; H4 assumes `theta_ij=(w,delta,tau,a)`; causal hierarchy uses legacy `mathfrak I` shorthand | **NOTATION MIGRATION REQUIRED; HYPOTHESIS LOGIC MUST NOT CHANGE** |
| `MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md` | current demonstrator-selection methodology | multiple generic/legacy references to `mathfrak I`, `delta_ij`, and ablation forms predating dependency-contract v1 | **MIGRATION/INTERPRETATION NOTE REQUIRED** |
| `FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md` | canonical framework-level decomposition | Stage-6/7 regime objects still use legacy `mathfrak I`; action superscript `a_k^{mathfrak I}` and `a_ij` activation terminology are pre-contract | **MIGRATION REQUIRED** |
| `HYPOTHESIS_REFINEMENT_AFTER_ASU_AUDIT_V1.md` | provenance amendment | uses flat tuple and `partial rho/partial w_ij` | **SUPERSEDED FOR ACTIVE INTERPRETATION BY v2** |
| `PUBLIC_NOVELTY_FALSIFICATION_F0_F1_F2_V1.md` | provenance novelty audit | uses flat tuple and universal `w_ij` sensitivity | **SUPERSEDED FOR ACTIVE INTERPRETATION BY v2** |

## 3. Already reconciled/current files

The following are consistent with the canonical contract and should govern interpretation:

```text
CANONICAL_DEPENDENCY_CONTRACT_V1.md
CANONICAL_SYSTEM_DEFINITION.md
CANONICAL_7_STAGE_FRAMEWORK.md
PHASE1_EMPIRICAL_VALIDATION_PROTOCOL.md
CANONICAL_NOTATION_RECONCILIATION_2026-09-16.md
HYPOTHESIS_REFINEMENT_AFTER_ASU_AUDIT_V2.md
PARTIAL_OBSERVATION_TO_VIABILITY_SPECIFICATION_V1.md
ORGANIZATION_TO_FEASIBLE_CONTROL_SPECIFICATION_V1.md
SUSTAINABLE_VIABILITY_CONSTRAINT_PROTOCOL_V1.md
VIABILITY_INTERFACE_SENSITIVITY_SPECIFICATION_V1.md
```

## 4. Required notation migration

### 4.1 Dependency semantics

Replace active statements of

```math
\mathfrak I_{ij}^{\alpha\beta}
```

with either

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)
```

for one directed dependency, or

```math
\mathbb I=\{\mathfrak d_e\}
```

for the represented dependency/interdependency set.

### 4.2 Mechanism parameters

Do not use

```math
\theta_{ij}=(w_{ij},\delta_{ij},\tau_{ij},a_{ij})
```

as a universal primitive.

Use

```math
\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e),
```

where `theta_e` contains only mechanism-relevant identified/calibrated parameters.

Delay belongs inside the operator/history semantics or `theta_e` only when physically relevant. Activation is represented by `gamma_e`. Influence strength is derived when meaningful.

### 4.3 Stage-5 sensitivity

Replace generic weight sensitivity by a declared perturbation of canonical dependency semantics. For smooth parameter directions:

```math
S_{e,v}^{\mathcal V}(Y)
=-D_{\theta_e}\rho_g(Y;\Theta)[v].
```

For nonsmooth/hybrid dependencies, use finite perturbation/intervention contrasts.

### 4.4 Regime object

Use

```math
\mathfrak M_k
=(\mathcal S_k,\mathcal G_k,\mathbb I_k,F_k,\Theta_k,K_{{\rm sus},k},\mathcal U_k).
```

Strategic transformation may alter the dependency set/semantics through an appropriately typed `a_k^{\mathbb I}` component, not through a Stage-2 primitive activation symbol that conflicts with the canonical guard `gamma_e`.

## 5. Change-control rule

The migration must be **notation/authority synchronization only** unless a separate versioned scientific amendment explicitly changes a hypothesis or framework statement.

In particular:

```text
H1–H5 logic remains frozen;
seven-stage order/responsibilities remain frozen;
P,T,I,O ontology remains frozen;
Phase-0 provenance is not retroactively rewritten.
```

## 6. Compilation warning

Until the files listed as `MIGRATION REQUIRED` are synchronized, final thesis prose, figures and code must use the authority order above. Automated or manual extraction from older files must not reintroduce the legacy flat tuple as current notation.

## 7. Current status

```text
AUDIT: PASS
CANONICAL AUTHORITY: CLEAR
SUPPORTING-FILE SYNCHRONIZATION: PARTIAL / PENDING
SCIENTIFIC LOGIC CHANGE: NONE
```
