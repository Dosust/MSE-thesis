# Stage 1 Generic Data Processing Layer

**Status:** **PASS — FROZEN UNDER STAGE-1 v2 AUTHORITY**  
**Authority:** `../../project/STAGE1_DATA_ABSTRACTION_AND_INGESTION_STANDARD_V2.md`  
**Mathematical contract:** `../../project/STAGE1_MATHEMATICAL_AND_ONTOLOGY_CONTRACT_V2.md`  
**Evidence/ontology authority:** `../../project/stage1_v2/Stage1_Evidence_and_Ontology_Register_v2_FINAL.md`

## Purpose

This directory contains case-independent implementation scaffolds for converting heterogeneous structural evidence into the frozen-candidate Stage-1 v2 canonical representation.

~~~text
RAW SOURCE
  -> SOURCE ADAPTER
  -> STAGING
  -> CANONICAL INTERMEDIATE REPRESENTATION
  -> CLEAN / NORMALIZE / QA / PROVENANCE
  -> STAGE-1 STRUCTURAL HANDOFF
~~~

Case-specific code must consume this generic contract and may not redefine Stage-1 ontology, relation semantics, evidence statuses, or causal-admission rules.

## Required adapter behavior

~~~text
inspect
validate_source
parse
map_schema
normalize
emit_canonical
report_provenance
report_quality
~~~

## Canonical Stage-1 relation architecture

~~~math
\mathfrak r_e^{(1)}=(\mathcal V_e,\sigma_e,\Gamma_e^{\rm str},\gamma_e,\Phi_e,d_e,m_e^{\rm cand},c_e^{\rm cand},s_e,\mathcal E_e)
~~~
with secondary metadata
~~~math
a_e=(h_e,\pi_e,\kappa_e,\ell_e,b_e,q_e^{\rm evid},\chi_e^{\rm norm}).
~~~

## Scientific guardrails

1. Raw data are immutable.
2. No silent imputation, geometry/topology repair, CRS/unit conversion, temporal reinterpretation, aggregation/disaggregation or evidence scoring.
3. `r_i` is spatial geometry; dynamic states use `X_P,X_T,z_I,z_O,Y(t)`.
4. Stage 1 requires `causal_dependency_accepted=false`.
5. Stage 1 requires `strength_status=NOT_ESTIMATED_STAGE1`.
6. Mechanism templates remain `TEMPLATE_ONLY` and are not case claims.
7. `VERIFIED_STRUCTURAL` requires case structural evidence.
8. Common cause/context is not P→T or T→P causality.
9. Numeric evidence confidence requires an auditable method.
10. Case thresholds/tolerances are configuration, not framework constants.

## Verification

`tests/stage1_data/test_stage1_framework.py` is the generic Stage-1 v2 verification suite. The GitHub workflow mirrors the same test entry point when hosted runner execution is available.

## Framework versus case

~~~math
\boxed{G_1^{\rm framework}\neq G_1^{\rm case}(c).}
~~~

A blocked or failed case instantiation does not invalidate the frozen generic framework.