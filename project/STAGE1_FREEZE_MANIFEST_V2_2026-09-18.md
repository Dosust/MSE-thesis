# Stage 1 Freeze Manifest v2 — 2026-09-18

**Status:** FINAL FREEZE MANIFEST  
**Scope:** Generic Stage-1 framework only; case-specific instantiations excluded.  
**Freeze decision:** `G_1^framework = PASS — FROZEN`

## 1. Frozen semantic/scientific authorities

| Artifact | Git blob SHA | Role |
|---|---|---|
| `project/CANONICAL_7_STAGE_FRAMEWORK_V2.md` | `30a9007d0720fd022f35869b50b6d2d729879653` | Seven-stage canonical architecture |
| `project/CANONICAL_RQ_SO_HYPOTHESES_V3.md` | `e599ef2233f0e4da6b782a29aecec3799c7974c2` | RQ1/SO1 and hypothesis authority |
| `project/STAGE1_FINAL_FRAMEWORK_V2.md` | `65fe99930245a68259608cf3b59cc29606bbe605` | Final Stage-1 scientific framework |
| `project/STAGE1_MATHEMATICAL_AND_ONTOLOGY_CONTRACT_V2.md` | `8f2c8b23fee9e8df17f6410dc3af2a0c55581de9` | Mathematical/ontology contract |
| `project/STAGE1_DATA_ABSTRACTION_AND_INGESTION_STANDARD_V2.md` | `cc3ddca3319df50c12f6dc95d41c3abf6cc3fa3d` | Generic data contract |
| `project/STAGE1_EXIT_GATE_AUDIT_V2_2026-09-18.md` | `efc9350568e3f686c5164224ba013a11403d47e6` | Final exit-gate audit |
| `project/stage1_v2/README.md` | `da3a51560d218f55482c0eecb0cbc17130d11d72` | v2 authority index |
| `project/stage1_v2/Stage1_Evidence_and_Ontology_Register_v2_FINAL.md` | `df5704ff1680da2f8c7d987605dec495b498c439` | Frozen literature-to-ontology authority |
| `project/stage1_v2/Stage1_Evidence_and_Ontology_Register_v2_FINAL.xlsx` | `26c4bc06a2c1657af5ad79975700a97445b3eb15` | Exact structured workbook authority |
| `project/stage1_v2/Stage1_v2_Normalization_Change_Log.md` | `bf95723864671574fdba5e542f289d747b56dd0b` | v1→v2 normalization audit |

## 2. Frozen machine/data contracts

| Artifact | Git blob SHA | Role |
|---|---|---|
| `schemas/stage1_structure.schema.json` | `69150a8deb8756ef4098c1dce0c7411a1e2b2681` | Stage-1 structural/relation schema v2.0 |
| `schemas/stage1_source_manifest.schema.json` | `af70743a9487f69f38f323a29d6bfdf853be027c` | Source/provenance schema |
| `schemas/stage1_relation_vocabulary_v2.json` | `346e6a2695cf720a571437accf0f9b0d12249ca9` | Controlled relation vocabulary |
| `methods/stage1_data/README.md` | `6ad4518433e447b5731e036c7c1eba71d9031af2` | Implementation authority map |
| `methods/stage1_data/adapter_contract.py` | `159f527e077d0f7b4a122494cec94472ca0f9394` | Runtime semantic guards |
| `methods/stage1_data/normalization.py` | `2cdbc0900a26472fb82dd55429be41a9a7e7707e` | Deterministic normalization/QA primitives |
| `tests/stage1_data/test_stage1_framework.py` | `76de381bd3719151616b19fd82cfe00343ea80b0` | 34-test case-independent verification suite |
| `tests/stage1_data/fixtures/stage1_structure_valid.json` | `ddbd05a296610870032a465daaea27edf0d51037` | v2 semantic fixture |
| `tests/stage1_data/fixtures/source_manifests.json` | `028eefd15d095b7b4d8fcf0a54f10fb6f2a84a0f` | heterogeneous source fixtures |
| `.github/workflows/stage1-framework-verification.yml` | `4dc20970b19dfa8aa8a61c6b6f43cdda6cbb56ee` | hosted verification mirror |

## 3. Synchronized repository governance

| Artifact | Git blob SHA | Role |
|---|---|---|
| `thesis/02_literature_theory/README.md` | `fc76177be78ae0e93f909e304d2325125e84d065` | Chapter-2 Stage-1 evidence authority link |
| `thesis/00_governance/THESIS_COMPLETION_GATES.md` | `bcad1ff99ef79ed2e89659ef17ba15b91b3f6090` | Stage-1 frozen completion gate |
| `thesis/00_governance/README.md` | `979c449b2fbad04f1fffc14ab15018d6844a03e2` | governance authority index |
| `project/AUTONOMOUS_EXECUTION_STATUS.md` | `881097125c61f4ddf99ae521f2b31ab689687f06` | execution-state synchronization |

## 4. Frozen scientific invariants

~~~math
\boxed{r_i=\text{spatial geometry/location}}
~~~
~~~math
\boxed{\mathfrak r_e^{(1)}=(\mathcal V_e,\sigma_e,\Gamma_e^{\rm str},\gamma_e,\Phi_e,d_e,m_e^{\rm cand},c_e^{\rm cand},s_e,\mathcal E_e)}
~~~
~~~math
\boxed{a_e=(h_e,\pi_e,\kappa_e,\ell_e,b_e,q_e^{\rm evid},\chi_e^{\rm norm})}
~~~
~~~math
\boxed{I_e^{\rm struct}\neq w_e\neq q_e^{\rm evid},\qquad w_e=\mathrm{NOT\_ESTIMATED\_STAGE1}}
~~~
~~~math
\boxed{G_1^{\rm framework}\neq G_1^{\rm case}(c)}
~~~

Stage 1 cannot use `ACCEPTED_CAUSAL`; `causal_dependency_accepted=false` is machine-enforced.

## 5. Verification evidence

Direct pre-freeze audits executed on current `main`:

~~~text
Authority / notation / governance synchronization: 16 / 16 PASS
Schema / vocabulary / fixture / runtime / test-source audit: 48 / 48 PASS
TOTAL: 64 / 64 PASS
~~~

The Python source suite contains 34 tests. GitHub-hosted Actions remains `BLOCKED-ENVIRONMENT` because jobs receive runner ID `0` and execute zero steps; this is not treated as a scientific or test failure.

## 6. Excluded from this freeze

The following remain mutable downstream case/method work and are **not** frozen by this manifest: real-case datasets; Austin/Greensboro/Singapore entity inventories; case spatial/topology QA; case crosswalks; case temporal-vintage decisions; case parameter values; Stage-2 causal acceptance; Stage-3 coupling laws/strengths; H1–H5 results.

## 7. Change control

Any semantic change to the entity object, `Gamma_e^str`, core relation object, secondary metadata, controlled evidence/existence vocabulary, existence-strength-confidence separation, normative/causal separation, CIR semantics, Stage-1 machine schema, or six G1 gates requires an explicit Stage-1 amendment/unfreeze. Nonsemantic formatting, links, comments and refactoring are allowed only if frozen meaning and tests remain unchanged.