# Global Pre-Data Work Queue v2

**Date:** 2026-09-19  
**Basis:** deep repository audit of current Stage 1–7 authorities.

## P0 — repair before integration

### P0.1 Authority control
- [x] Global authority/supersession map exists.
- [x] Current H4/H5 meanings identified.
- [x] Legacy dependency notation translation authority identified.
- [x] Repository authority-drift audit completed; carry the verified classifications into the global master workbook.

Authority drift cleanup closure: **PASS — 2026-09-19**. No obsolete H4/H5 file may govern active work; legacy Stage-3 notation is explicitly quarantined.

### P0.2 Stage 3 normalization — COMPLETE
- [x] Create `project/stage3/STAGE3_SCIENTIFIC_CONSTITUTION_V2.md`.
- [x] Define active-notation Stage2→3 input contract.
- [x] Define Stage3 state/input/output/QOI ontology.
- [x] Define model-family selection schema.
- [x] Freeze time/hybrid/multirate semantics at design level.
- [x] Define generic scenario-template schema.
- [x] Define Stage3 benchmark/VVUQ schema.
- [x] Define Stage3→4 handoff.
- [x] Define Stage3 claim ceiling.
- [x] Freeze/version the Stage3 v2 constitution.

Stage 3 design normalization closure: **PASS — DESIGN/PROTOCOL ONLY; empirical Stage 3 remains NOT TESTED.**

### P0.3 Stage 6 v2.1 alignment — COMPLETE
- [x] Add explicit effectiveness `E_fx(a_k)`.
- [x] Add explicit efficiency `E_fy(a_k)` and evidence-supported resource vector.
- [x] Keep `ΔR`, `E_fx`, `E_fy`, and `ΔJ_sus` distinct.
- [x] Update H4 performance reporting while preserving canonical primary H4 eligibility `A_H4 = A_R+`.
- [x] Update Stage6→7 handoff.
- [x] Issue Stage-6 aligned workbook/versioned amendment.
- [x] Issue updated freeze/manifest.

Stage 6 v2.1 alignment closure: **PASS — DESIGN/PROTOCOL V2; empirical Stage 6 remains DEFERRED / H4 NOT TESTED.**

### P0.4 Stage 7 v2.1 alignment — COMPLETE
- [x] Receive resilience + effectiveness + efficiency + sustainability + feasibility + uncertainty.
- [x] Generate and verify Stage-7 workbook v2; exact byte identity recorded.
- [x] Add `project/stage7/README.md`.
- [x] Add searchable Stage-7 constitution/handoff and decision protocols.
- [x] Add design-freeze record.
- [x] Add finalization manifest.

Stage 7 v2.1 alignment closure: **PASS — DESIGN/PROTOCOL V2; empirical Stage 7 remains DEFERRED / H5 NOT TESTED.**

## P1 — global control plane

### P1.0 Governance synchronization — COMPLETE
- [x] Issue PRE_DATA_STAGE1_7_INTEGRATION_AUDIT_V2.md.
- [x] Update global integration README.
- [x] Reconcile current Stage 3/6/7 design status.

### P1.1 Symbol/ontology registry — COMPLETE
- [x] Build GLOBAL_SYMBOL_AND_ONTOLOGY_REGISTRY_V1.md.
- [x] Disambiguate cross-stage symbol collisions.
- [x] Quarantine legacy dependency primitive.

Fields:
`symbol | definition | type | unit | physical/epistemic/decision class | created stage | consuming stages | authority | assumptions | validity | legacy aliases`.

### P1.2 Handoff matrix — COMPLETE
- [x] Build GLOBAL_STAGE_HANDOFF_MATRIX_V1.md.
- [x] Build GLOBAL_CROSS_STAGE_NOTATION_AND_HANDOFF_NORMALIZATION_V1.md.
- [x] Resolve Stage4→5 physical-truth lineage.
- [x] Resolve Stage5→6 producer/consumer mismatch losslessly.
- [x] Run P1 backbone audit: 20/20 PASS.

For every `I(k→k+1)`:
`producer | consumer | object | mandatory fields | units/types | uncertainty | validity | fail/block behavior | claim ceiling`.

### P1.3 H1–H5 master preregistration — COMPLETE
- [x] Create `GLOBAL_H1_H5_MASTER_PREREGISTRATION_V1.md`.
- [x] Freeze the 13-field master object for H1–H5.
- [x] Preserve canonical baseline/treatment/comparator semantics.
- [x] Preserve current H1 mechanism-readiness restrictions.
- [x] Keep unresolved H2/H3/H4/H5 metrics/thresholds DEFERRED.
- [x] Standardize final adjudication as SUPPORTED / NOT SUPPORTED / NOT TESTED.
- [x] Run preregistration audit: 32/32 PASS.

### P1.4 Baseline/benchmark/reference registry — COMPLETE
- [x] Create GLOBAL_BASELINE_BENCHMARK_REFERENCE_REGISTRY_V1.md.
- [x] Define global baseline/comparator subtypes.
- [x] Separate benchmark problem, verification fixture, reference solution, reference calculation and validation evidence.
- [x] Separate synthetic truth from empirical ground truth.
- [x] Type Stage-3/5/6/7 terminal B(k,3) objects as QUALIFIED_CASE, not synthetic benchmark.
- [x] Type H1–H5 baseline roles consistently with P1.3.
- [x] Prohibit unnamed reference roles in future confirmatory documentation.
- [x] Run P1.4 classification audit: 38/38 PASS.

### P1.5 Empty final-case schema — COMPLETE
- [x] Create GLOBAL_FINAL_CASE_SCHEMA_V1.md.
- [x] Create Draft 2020-12 machine schema.
- [x] Create field dictionary for all eleven case objects.
- [x] Create provenance CSV ledger.
- [x] Create admissibility gate matrix.
- [x] Bind P1.4 reference classes.
- [x] Create uncertainty template.
- [x] Preserve all case values as DEFERRED.
- [x] Run combined semantic/machine audit: 58/58 PASS.
```math
\mathcal S_{case}
=
(\mathcal G,Y_0,\theta,\eta,T,K,G_{rec},F_{unsafe},
\mathcal U_{feas},\mathcal A,\Omega).
```

### P1.6 Common scenario schema — COMPLETE
- [x] Separate immutable root scenario, experimental arm, executable run and result identity.
- [x] Create GLOBAL_SCENARIO_ID_AND_PROPAGATION_SCHEMA_V1.md.
- [x] Create Draft 2020-12 machine schema.
- [x] Create scenario field dictionary.
- [x] Create Stage 3→7 propagation matrix.
- [x] Create matched-comparison/randomness protocol.
- [x] Create empty root and seed-manifest templates.
- [x] Freeze H1–H5 matched-field/change-field semantics.
- [x] Preserve scenario-frequency ≠ probability.
- [x] Run combined scenario audit: 52/52 PASS.

### P1.7 Global uncertainty/VVUQ — COMPLETE
- [x] Create GLOBAL_UNCERTAINTY_VVUQ_CONTROL_V1.md.
- [x] Create Draft 2020-12 machine schema.
- [x] Separate uncertainty nature from uncertainty source.
- [x] Freeze probability/dependence/reducibility semantics.
- [x] Create Stage/H1–H5 uncertainty propagation matrix.
- [x] Create global VVUQ gate matrix.
- [x] Create verification/validation/acceptance protocol.
- [x] Create sensitivity/convergence/decision-stability protocol.
- [x] Create credibility/claim-ceiling matrix.
- [x] Create empty uncertainty, VVUQ-activity and context-of-use registers.
- [x] Run combined P1.7 audit: 84/84 PASS.

### P1.8 Global requirements/provenance — COMPLETE
- [x] Create GLOBAL_REQUIREMENTS_PROVENANCE_CONTROL_V1.md.
- [x] Create Draft 2020-12 machine schema.
- [x] Separate requirement kind, authority, hardness, maturity and effectivity.
- [x] Freeze source→interpretation→formalization→allocation→compliance provenance.
- [x] Freeze bidirectional traceability.
- [x] Separate qualitative source statements from numerical translations.
- [x] Create authority/type matrix.
- [x] Create Stage 1→7 / H1–H5 traceability matrix.
- [x] Create conflict/change-control protocol.
- [x] Create requirement verification/validation/compliance protocol.
- [x] Create empty requirement, provenance, change, conflict and compliance registers.
- [x] Preserve all case thresholds/weights as DEFERRED.
- [x] Run combined P1.8 audit: 104/104 PASS.

### P1.9 Claim-evidence-result matrix — COMPLETE
- [x] Create GLOBAL_CLAIM_EVIDENCE_RESULT_CONTROL_V1.md.
- [x] Create Draft 2020-12 machine schema.
- [x] Register bounded thesis claim families across RQ0–RQ7/SO1–SO7/H1–H5.
- [x] Separate structural, mechanism, implementation, predictive/causal, viability, diagnostic, intervention, sustainability, requirement, decision and synthesis claims.
- [x] Freeze claim/result/status axes independently.
- [x] Bind required evidence, tests/gates, QOI/endpoints, uncertainty and validity domains.
- [x] Inherit P1.7 C0–C5 credibility ceilings.
- [x] Create wording/anti-overclaim protocol.
- [x] Preserve H1–H5 as NOT TESTED.
- [x] Create empty claim/result register template.
- [x] Run combined P1.9 audit: 128/128 PASS.

Permanent rule:

```math
\boxed{
\text{stated conclusion strength}
\le
\text{qualified evidence/result strength}.
}
```


## P2 — master artifact and freeze — COMPLETE
- [x] Build `GLOBAL_STAGE1_7_MASTER_REGISTER_V1.xlsx`.
- [x] Run notation conflict audit.
- [x] Run handoff completeness audit.
- [x] Run hypothesis/comparator consistency audit.
- [x] Run requirement-provenance audit.
- [x] Run claim-evidence audit.
- [x] Run gate-requiredness audit.
- [x] Run computation-role / provenance audit.
- [x] Preserve BLOCKED / DEFERRED / N/A / NOT_TESTED without binary coercion.
- [x] Mark every case/data-dependent field DEFERRED / BLOCKED / NOT_TESTED as scientifically appropriate.
- [x] Create `P2_GLOBAL_STAGE1_7_MASTER_REGISTER_AUDIT_V1_2026-09-20.md`.
- [x] Create `GLOBAL_STAGE1_7_DESIGN_FREEZE_V1.md`.
- [x] Record workbook SHA-256: `7906fc6eb3bc6b720d41e20315ffed3222efc6d0839add98cd21f56115749b6c`.
- [x] Pin final P2 manifest after freeze commit.

P2 design result:

~~~math
\boxed{
G_{P2}^{design}=PASS,
\qquad
11/11\ \text{global audits PASS},
\qquad
0\ \text{design contradictions}.
}
~~~

The master workbook contains 27 normalized scientific/control objects and preserves empirical blockers rather than inventing completion.

## Definition of pre-data complete

```math
\boxed{
\text{PRE-DATA COMPLETE}
\iff
\text{all design contradictions are closed}
}
```

Empirical values, datasets, calibration parameters and confirmatory outcomes are allowed to remain unresolved until the subsequent data-qualification phase.

### P1.10 P–T SoS / complex-dynamics source alignment — COMPLETE
- [x] Integrate Hall et al. service-centered System-of-Systems semantics.
- [x] Integrate Ibáñez et al. explicit energy–transport operational/planning coupling evidence.
- [x] Preserve P and T as separate constituent systems with distinct native physics.
- [x] Add transportation infrastructure/fleet/demand/control distinction.
- [x] Add OPERATION / RECOVERY / PLANNING and effect-class metadata without altering the canonical dependency primitive.
- [x] Correct singular aggregate Stage-3 interface-state semantics to mechanism-indexed/directional state notation through v2.2 amendment.
- [x] Quarantine historical H1 mechanism assumptions that conflict with current G2/readiness status.
- [x] Create causal/readiness-aware Level-2 dependency registry v2.
- [x] Add machine guard preventing a non-ready dependency from being labeled accepted M2.
- [x] Add Hall/Ibáñez to controlled Chapter-2 evidence and Chapter-1 source grounding.
- [x] Clarify generic figure arrows versus case-specific accepted dependencies.
- [x] Run source-alignment audit and record residual/open items.

Closure:

```math
\boxed{P1.10=PASS\quad\text{(semantic/control-plane alignment only)}}
```

This does not close P2 and does not authorize H1 execution. P2 must consume the v2 dependency registry and the current `z_{\mathbb I}` interface-state semantics.

**P1.10 manifest pin:** `PT_SOS_COMPLEX_DYNAMICS_ALIGNMENT_MANIFEST_V1.json` records the exact principal artifact identities for the source-alignment package.


### P1.11 Mandatory spatiotemporal SoS–resilience–transformation lens — COMPLETE
- [x] Consolidate spatiotemporal SoS structure as a mandatory cross-stage lens.
- [x] Preserve the canonical Stage-2 dependency primitive.
- [x] Preserve directional/interface-state and hybrid Stage-3 semantics.
- [x] Distinguish operational, recovery and transformation timescales.
- [x] Keep service, resilience, effectiveness, efficiency and sustainability as separate object classes.
- [x] Make coupled-system sustainability/burden-shifting review mandatory where applicable.
- [x] Distinguish intervention from structural transformation.
- [x] Make path-dependence/adaptive-pathway reasoning conditional on evidence/scope.
- [x] Define mandatory stage-by-stage audit questions.
- [x] Require future audits to classify applicable spatial, temporal, SoS, interdependency, dynamics, service, resilience, intervention, effectiveness, efficiency, sustainability, transformation and decision dimensions.
- [x] Run compatibility audit: 42/42 PASS.

Closure:

~~~math
\boxed{
P1.11=PASS
\quad
\text{(mandatory interpretive/control-plane lens)}
}
~~~

P2 remains the next execution task and must consume P1.11 explicitly.


#### P1.11.1 Pant spatial-risk / functional-pathway refinement — COMPLETE
- [x] Make common-cause vs cascade chronology explicit.
- [x] Make spatially coherent hazard resolution conditional on mechanism/QOI.
- [x] Separate graph paths from functional service pathways.
- [x] Preserve nearest-neighbour mappings as candidate/proxy evidence only.
- [x] Treat binary failure as a bounded special case.
- [x] Treat no-rerouting transport as a bounded approximation/benchmark.
- [x] Freeze criticality classes: topology / flow-service / hazard-conditioned / viability-sensitive.
- [x] Separate local interface criticality from spatial hotspot criticality.
- [x] Preserve risk != resilience.
- [x] Preserve asset state != service disruption != economic consequence.
- [x] Preserve recovery != transformation.
- [x] Add twelve required P2 audit fields.
- [x] Run compatibility audit: 36/36 PASS.

P2 remains the next major task.


#### P1.11.2 Barr information architecture / provenance / orchestration — COMPLETE
- [x] Separate physical SoS, model system and information/provenance system.
- [x] Separate vertical hierarchy from horizontal dependency.
- [x] Add explicit spatial, temporal and semantic alignment operations.
- [x] Preserve alignment != causal mechanism.
- [x] Preserve database representation != physical truth.
- [x] Preserve physical coupling != software coupling.
- [x] Add immutable inter-model handoff provenance record.
- [x] Require source/target variable, units, support, transformation, uncertainty, model/run/data versions and validity.
- [x] Extend physical/epistemic firewall to database representation D.
- [x] Make hazard data provenance/versioning explicit.
- [x] Preserve visualization != validation/evidence.
- [x] Separate geographic, graph and viability geometries.
- [x] Require versioned architectures for Stage-7 transformation.
- [x] Add reproducibility/auditability questions for material thesis objects.
- [x] Add eighteen P2 information-architecture audit fields.
- [x] Run compatibility audit: 48/48 PASS.

P2 remains the next major task and must consume P1.11, P1.11.1 and P1.11.2 explicitly.


#### P1.11.3 NEXTRANS policy/operator/budget/market feedback — COMPLETE
- [x] Separate physical/functional, organizational, budget/resource, market/economic and public-policy channels.
- [x] Preserve Stage-4 organization and feasible-control authority.
- [x] Separate operational control from strategic/public-policy intervention.
- [x] Avoid Pi notation collision by using p_pol / P_pol for public-policy instruments.
- [x] Preserve native units; prohibit universal coupling cost without justified downstream aggregation.
- [x] Preserve topology != flow != capacity != service.
- [x] Make policy-induced interdependency admissible only through qualified mechanisms.
- [x] Treat EV interactions as multiple mechanism-specific channels.
- [x] Preserve equilibrium != dynamic trajectory.
- [x] Keep policy/market/budget dynamics out of Stage 3 unless mechanism/QOI/readiness justify inclusion.
- [x] Preserve multi-actor objectives without inventing one scalar utility.
- [x] Extend effectiveness to coupled-system targets only when prospectively declared.
- [x] Allow opportunity/resource costs only with supported accounting boundaries.
- [x] Add transformation feedback through policy/behavior/demand/budget/investment only when evidence supports it.
- [x] Add policy/economic calibration and validation firewall.
- [x] Add seventeen P2 audit fields.
- [x] Run compatibility audit: 46/46 PASS.

P2 remains the next major task and must consume P1.11, P1.11.1, P1.11.2 and P1.11.3.


#### P1.11.4 Acosta-Sequeda observational / cross-system inference — COMPLETE
- [x] Separate predictive relation, shared-driver association and physical causal dependency.
- [x] Avoid overloading canonical dependency set I with noncausal predictive relations.
- [x] Define Stage-4 observational relation object and noncausal arrow rightsquigarrow.
- [x] Preserve forecasting association != G2 causal PASS.
- [x] Allow cross-system observations to enrich Stage-4 information/estimation.
- [x] Freeze x != demand != observation semantics.
- [x] Separate observational lag, physical propagation delay and information latency.
- [x] Require spatial/temporal/resolution/semantic alignment before inference.
- [x] Preserve spatial and transportation-mode validity domains.
- [x] Define information effectiveness separately from resilience.
- [x] Require target-only baseline and protected out-of-sample evaluation.
- [x] Require explicit abnormal-regime testing for regime-shift claims.
- [x] Require info -> action -> service -> resilience trace for resilience claims.
- [x] Preserve forecast improvement != information efficiency != sustainability != transformation.
- [x] Retain preprint publication status in evidence interpretation.
- [x] Create additive global symbol/ontology amendment.
- [x] Add twenty-two P2 audit fields.
- [x] Run compatibility audit: 50/50 PASS.

P2 remains the next major task and must consume P1.11 through P1.11.4.


#### P1.11.5 Kays–Sadri sustainability / resilience / trade-off alignment — COMPLETE
- [x] Preserve sustainability != resilience != effectiveness != efficiency.
- [x] Classify temperature/speed/delay/mobility/accessibility/energy/emissions by scientific role instead of treating all as sustainability endpoints.
- [x] Retain vector sustainability core: accessibility, energy, carbon, cost.
- [x] Make sustainability accounting explicitly spatial, temporal and boundary-dependent.
- [x] Add trajectory/accounting states without redefining physical infrastructure state.
- [x] Preserve sustainability metric != sustainability requirement.
- [x] Preserve canonical Stage-5 K as the default acceptability set.
- [x] Permit K_sus / sustainable viability only when qualified hard sustainability requirements exist.
- [x] Treat conceptual tipping points as hypotheses/regions, not calibrated thresholds.
- [x] Preserve Pareto-before-preference Stage-7 logic.
- [x] Require coupled P–T accounting boundary and burden-shifting checks.
- [x] Preserve J_cost != efficiency.
- [x] Separate operational from lifecycle/transformation sustainability horizons.
- [x] Add sustainability accounting/trade-off protocol.
- [x] Add twenty-five P2 audit fields.
- [x] Run compatibility audit: 54/54 PASS.

P2 remains the next major task and must consume P1.11 through P1.11.5.


#### P1.11.6 Source / authority reconciliation — COMPLETE
- [x] Register Pant, Barr, NEXTRANS, Acosta-Sequeda and Kays–Sadri in Chapter-2 controlled evidence.
- [x] Pin exact supplied PDF byte identities with SHA-256.
- [x] Create source-page/section → claim → repository-rule mapping.
- [x] Separate repository consistency from source support and case validation.
- [x] Reclassify all 54 P1.11.5 audit items on the source-support axis.
- [x] Preserve SUSTAINABILITY_ADMISSION_FREEZE_V1 as controlling current H4/H5 scope.
- [x] Reclassify the access/energy/carbon/cost tuple as broad screening/accounting schema, not confirmatory sustainability core.
- [x] Keep cost and operational energy in resource/economic roles under the current freeze.
- [x] Keep distributional accessibility conditional.
- [x] Keep embodied GHG and full LCA outside the current confirmatory core.
- [x] Set Kays-derived hard sustainability constraints to BLOCKED.
- [x] Correct mandatory dimensions -> mandatory screening dimensions.
- [x] Correct universal strict timescale ordering to case-dependent characteristic horizons.
- [x] Default NEXTRANS budget/market/public-policy variables to DEFERRED / STAGE-7 CONTEXT unless explicitly activated.
- [x] Replace current Acosta terminology with cross-system observational inference.
- [x] Add deterministic repository test for reconciliation invariants.
- [x] Run P1.11.6 repository-consistency audit: 36/36 PASS.
- [x] Run deterministic post-commit invariant verification: 21/21 PASS.

P2 is now the next major execution task and must consume P1.11.6 as the authority-reconciliation layer.


#### P1.11.7 Li–Mostafavi computational-role architecture — COMPLETE
- [x] Register Li & Mostafavi (2025) in Chapter-2 controlled evidence.
- [x] Pin exact supplied PDF byte identity with SHA-256.
- [x] Add source-page/section → claim → repository-rule mappings.
- [x] Separate physical system, observation, feature, index, pattern and decision objects.
- [x] Define MECHANISTIC / OBSERVATIONAL / DECISION computation lanes without replacing seven stages.
- [x] Use \mathcal D_raw for raw datasets to avoid collision with D_i demand/use.
- [x] Add explicit spatial/temporal analysis-support alignment.
- [x] Add Stage-4 feature/reference-state pipeline.
- [x] Preserve association/feature importance/PCA loading != physical causality/interface strength.
- [x] Preserve data-driven characterization != Stage-3 physical dynamics.
- [x] Preserve formal Stage-5 resilience R_T != diagnostic products D_R.
- [x] Preserve PCA/clustering as diagnostics, not viability or causal proof.
- [x] Preserve socioeconomic attribute != social-sustainability endpoint.
- [x] Preserve current sustainability admission freeze.
- [x] Preserve observational clusters != intervention effects.
- [x] Add computation-role/output-claim protocol.
- [x] Add twenty-five P2 computational audit fields.
- [x] Run P1.11.7 repository-consistency audit: 48/48 PASS.
- [x] Run deterministic post-commit invariant verification: 20/20 PASS.

P2 remains the next major task and must consume P1.11.7 computation-role semantics.


#### P1.11.8 Bramoullé–Maes measurement-error / identification reconciliation — COMPLETE
- [x] Register Bramoullé & Maes (2026) in Chapter-2 controlled evidence.
- [x] Pin exact supplied PDF byte identity with SHA-256.
- [x] Add source-page/section → claim → repository-rule mappings.
- [x] Preserve measurement model before inferential estimation.
- [x] Separate causal qualification G2 from parameter identification G_ID.
- [x] Permit G2=PASS with G_ID=BLOCKED.
- [x] Add estimator-admission gate G_EST.
- [x] Add weak-identification diagnostics/strength status.
- [x] Preserve optimizer convergence != scientific identification.
- [x] Preserve GMM/2SLS as source-specific methods, not P–T defaults.
- [x] Clarify Monte Carlo as method verification/UQ rather than empirical infrastructure validation.
- [x] Preserve true-graph vs observed-graph uncertainty as unresolved where applicable.
- [x] Extend Stage-3 empirical parameter readiness.
- [x] Extend Stage-4 measurement→identification→estimation control.
- [x] Preserve P1.7 uncertainty ontology and map the six-label summary into it.
- [x] Add Stage-6 quantity-origin and uncertainty-lineage classes.
- [x] Replace universal effect-size>uncertainty rule with representation-aware G_resolve.
- [x] Extend P1.11.7 computation record rather than create a competing object.
- [x] Run P1.11.8 repository-consistency audit: 52/52 PASS.
- [x] Run deterministic post-commit invariant verification: 22/22 PASS.

P2 remains the next major task and must consume P1.11.8 identification/measurement semantics.


#### P1.11.8.1 Gate-semantics normalization — COMPLETE
- [x] Separate G_EST^admit from G_VAL^result.
- [x] Remove post-estimation validation from pre-estimation estimator admission.
- [x] Separate G_ID^struct from G_ID^strength.
- [x] Permit structural PASS with strength BLOCKED.
- [x] Add POINT / SET_PARTIAL / N_A_NONINFERENTIAL identification types.
- [x] Prevent observationally inferred sets/intervals from being mislabeled N/A.
- [x] Normalize source integration to STATUS=(REPO,SOURCE,CASE).
- [x] Remove CASE_VALIDATED from source-support vocabulary.
- [x] Add MONTE_CARLO_METHOD_TEST computation class.
- [x] Add UNCERTAINTY_PROPAGATION computation class.
- [x] Preserve Monte Carlo method test != propagation != case validation.
- [x] Add Stage-3 pre/post empirical-parameter gates.
- [x] Add Stage-4 corrected inference chain.
- [x] Preserve P1.7 uncertainty authority.
- [x] Preserve sustainability scope unchanged.
- [x] Add normalized P2 fields.
- [x] Run P1.11.8.1 repository-consistency audit: 32/32 PASS.
- [x] Run deterministic post-commit invariant verification: 24/24 PASS.

P2 remains the next major task and must consume P1.11.8.1.


## P3 — CASE / DATA QUALIFICATION + EXECUTION READINESS — IN PROGRESS

~~~math
\boxed{
G_{P2}^{design}=PASS
\not\Rightarrow
G_{data}=PASS
\not\Rightarrow
G_{case,exec}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~

### P3.0 control-plane initialization
- [x] Bind P3 to frozen P2 design.
- [x] Create P3_CASE_DATA_EXECUTION_READINESS_PROTOCOL_V1.md.
- [x] Create P3_CASE_DATA_EXECUTION_READINESS_REGISTER_V1.xlsx.
- [x] Create P3 Austin initialization audit.
- [x] Add fail-closed machine readiness instrument.
- [x] Add P3 regression tests.
- [x] Normalize repository CI dependencies / supported Python matrix.
- [x] Make absent optional SVG assets N/A rather than a hard CI failure.
- [x] Observe post-commit Scientific Architecture QA — RUNNER_START_BLOCKED at run 35456457022; no recorded step/log.
- [x] Observe post-commit Python package matrix — RUNNER_START_BLOCKED at run 35456456998; all matrix jobs had no recorded step/log.
- [x] Observe Austin public-data qualification run — RUNNER_START_BLOCKED at run 35456457060; no recorded step/log.
- [ ] Re-establish GitHub Actions runner availability and observe at least one executed workflow step before claiming repository execution readiness.

### P3.1 Austin case qualification
- [ ] Close G1 power materialization / feeder realization.
- [ ] Close G2 common spatial support.
- [ ] Close G3 transport topology.
- [ ] Close G4 traffic observations.
- [ ] Close G5 P→T semisynthetic mapping.
- [ ] Close G6 T→P repair access.
- [ ] Close G7 flood exposure.
- [ ] Close G8 QC/provenance.
- [ ] Freeze final feeder under the pre-result minimum-state rule.
- [ ] Set final_case_admissibility=true only if G0–G8 all PASS.

### P3.2 execution readiness
- [ ] Qualify all required G, Y0, theta, eta, T, K, G_rec, F_unsafe, U_feas, A, Omega fields for the planned experiment.
- [ ] Close applicable identification/estimator/result-validation gates.
- [ ] Freeze H1–H5 execution inputs/materiality criteria before result inspection.
- [ ] Authorize confirmatory execution only after case and repository execution gates PASS.

~~~text
P3 CONTROL PLANE = PASS
FINAL CASE = BLOCKED
H1–H5 = NOT_TESTED
~~~


### P3.0.1 Execution-gate semantics — COMPLETE
- [x] Separate G_case,adm from G_exp,exec.
- [x] Add explicit G_runner to G_repo,exec.
- [x] Replace overloaded F_required(experiment) with O_req(E).
- [x] Version initial + controlled-retry runner evidence.
- [x] Update machine readiness instrument to fail closed on repository and experiment-object readiness.
- [x] Preserve H1-H5 = NOT_TESTED.

Next scientific work remains public-data materialization/qualification and feeder/case gates.
