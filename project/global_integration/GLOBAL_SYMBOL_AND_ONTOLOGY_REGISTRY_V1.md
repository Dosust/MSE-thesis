# Global Symbol and Ontology Registry v1

**Date:** 2026-09-19  
**Status:** CANONICAL GLOBAL INTEGRATION REGISTRY — PRE-DATA  
**Scope:** cross-stage controlling objects, handoff objects, permanent firewalls and symbols needed for Stage 1→7 integration.  
**Case values:** DEFERRED unless already governed by a frozen stage authority.

## 1. Registry schema

Every global symbol record has:

symbol | definition | object_type | class | unit | created_stage | consuming_stages | authority | authority_blob_sha | assumptions/validity | uncertainty_owner | legacy_or_collision_alias | status

"heterogeneous/native" means component-level units must be registered before case execution.  
"N/A" means the object is a set, graph, status, mapping, or other non-physical scalar object.

## 2. Global ontology

| Symbol | Definition | Type / class | Unit | Owner → consumers | Authority @ blob | Validity / uncertainty | Alias / status |
|---|---|---|---|---|---|---|---|
| \(\mathcal S=\{P,T,I,O\}\) | thesis System-of-Systems domains | finite set / ontology | N/A | S1 → S2–S7 | STAGE1_FINAL_FRAMEWORK_V2 @ 65fe9993 | global thesis ontology | CURRENT |
| \(P,T\) | physical infrastructure systems | domain class / physical | N/A | S1 → S2–S7 | same | physical-layer scope | CURRENT |
| \(I,O\) | information and organization supporting domains | domain class / supporting | N/A | S1 → S4–S7 | same | supporting-domain scope | CURRENT |
| \(\Omega_{sys}^{+}\) | spatial, temporal, infrastructure, service, mode and jurisdiction boundary | tuple / boundary | heterogeneous | S1 → all | STAGE1_FINAL_FRAMEWORK_V2 @ 65fe9993 | case binding deferred | CURRENT |
| \(\mathcal G\) | graph/topology object inherited through stages | graph / physical structure | N/A | S1/S3 → S4–S7 | stage authorities | topology \(\neq\) state | CURRENT |
| \(\Lambda_k\) | maximum defensible claim ceiling at stage \(k\) | epistemic bound | N/A | Sk → downstream | stage constitutions | cannot increase downstream without evidence | CURRENT |
| \(\Pi_k\) | provenance/evidence map or payload | provenance object | N/A | stage owner → downstream | stage contracts | exact content stage-specific | CURRENT |

## 3. Stage 1 — structure / ontology

Authority: project/STAGE1_FINAL_FRAMEWORK_V2.md @ 65fe99930245a68259608cf3b59cc29606bbe605  
Mathematical contract: project/STAGE1_MATHEMATICAL_AND_ONTOLOGY_CONTRACT_V2.md @ 8f2c8b23fee9e8df17f6410dc3af2a0c55581de9

| Symbol | Definition | Type / class | Unit | Consumers | Validity / uncertainty | Alias / status |
|---|---|---|---|---|---|---|
| \(\mathcal G^{(1)}=(\mathcal V,\mathcal E_{intra},R,\Lambda)\) | Stage-1 multilayer structural graph | graph / physical-structural | N/A | S2–S7 | structural possibility only | CURRENT |
| \(r_i\) | entity geometry/location | geometry / physical | CRS-dependent | S2–S7 | CRS/provenance required | CURRENT |
| \(E_i^\alpha\) | semantic entity object | typed tuple / ontology | heterogeneous | S2–S7 | entity evidence/provenance | CURRENT |
| \(Y_1^{schema}\) | global alias for Stage-1 source notation \(Y=[X_P,X_T,z_I,z_O]^\top\) | structural state schema | heterogeneous/native | S1/S2 context | not Stage-3 physical truth | source alias Y(t); DISAMBIGUATED |
| \(\Gamma_e^{str}\) | structural-admissibility predicate | predicate / structural | dimensionless/status | S2 | structural admission \(\neq\) causality | CURRENT |
| \(\mathfrak r_e^{(1)}\) | Stage-1 structural relation candidate | relation tuple / structural | heterogeneous | S2 | no causal acceptance/strength | CURRENT |
| \(a_e\) | secondary Stage-1 relation metadata | metadata tuple | heterogeneous | S2 | evidence/path/arity/normative metadata | CURRENT |
| \(\gamma_e^{S1,int}\) | integration alias for Stage-1 interface semantics | interface semantic | N/A/native | S2 translation | frozen S1 meaning only | source symbol gamma_e; DISAMBIGUATED |
| \(\Phi_e^{S1,exch}\) | integration alias for Stage-1 exchanged/enabled service/resource/information/control/access semantic | carrier/service semantic | native/type | S2 translation | frozen S1 meaning only | source symbol Phi_e; DISAMBIGUATED |
| \(I_e^{struct}\) | structural-existence status | categorical status | N/A | S2 | not coupling strength | CURRENT |
| \(w_e\) | coupling strength placeholder prohibited from estimation in S1 | unresolved parameter concept | case/native | none until qualified | NOT_ESTIMATED_STAGE1 | CURRENT-PROTECTED |
| \(q_e^{evid}\) | epistemic evidence confidence | epistemic status/score | categorical or calibrated | governance | not physical strength | CURRENT |
| \(Z_1^{impl+}\) | canonical Stage-1 implementation handoff | composite handoff | heterogeneous | S2 | case values may be empty | CURRENT |

## 4. Stage 2 — causal dependency

Authority: project/CANONICAL_DEPENDENCY_CONTRACT_V1.md @ ae0b1ead2329b04ee5f55107ca18f72b02758ed0

| Symbol | Definition | Type / class | Unit | Consumers | Validity / uncertainty | Alias / status |
|---|---|---|---|---|---|---|
| \(\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)\) | canonical directed dependency | causal object | heterogeneous | S3–S7 | accepted only within declared validity | CURRENT |
| \(\mathbb I=\{\mathfrak d_e\}\) | dependency collection | set / causal | N/A | S3–S7 | status subsets preserved | legacy \(\mathfrak I\); CURRENT |
| \(\mathcal C_e=(s_e,p_e^s,r_e,p_e^r,\chi_e)\) | source/receiver/interface composition | interface tuple | heterogeneous | S3 | typed ports/carrier required | CURRENT |
| \(s_e,r_e\) | typed source and receiver | entity refs | N/A | S3 | direction encoded by order | CURRENT |
| \(p_e^s,p_e^r\) | source/receiver ports/interaction points | interface refs | geometry/type | S3 | case binding required | CURRENT |
| \(\chi_e\) | exchanged carrier/signal/service/command/authority/resource type | carrier semantic | native/type | S3 | may be nonphysical | receives S1 exchange semantic; CURRENT |
| \(\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e)\) | causal/domain-semantic block | causal tuple | heterogeneous | S3 | mechanism-specific | CURRENT |
| \(\Phi_e^{S2,op}\) | causal coupling/transition operator | operator / causal | input-output dependent | S3 | executable form required for simulation | source symbol Phi_e; DISAMBIGUATED |
| \(\gamma_e^{S2,act}\) | activation/context guard | predicate/function | dimensionless/status | S3 | activation evidence required | source symbol gamma_e; DISAMBIGUATED |
| \(\theta_e\) | mechanism parameters including delay when applicable | parameter vector | case/native | S3 | parameter uncertainty required | CURRENT |
| \(\zeta_e\) | optional dependency memory/internal state | state / physical-interface | case/native | S3 | only when mechanism requires | CURRENT |
| \(\Pi_e=(\mathcal P_e,V_e,\mathcal U_e)\) | provenance, validity and uncertainty block | epistemic tuple | heterogeneous | S3–S7 | cannot be discarded | CURRENT |
| \(\mathfrak d_e^{(3)}\) | Stage-3-ready implementation record | readiness tuple | heterogeneous | S3 | requires \(G_{2\to3}\) | CURRENT |
| \(\Xi_e\) | executable realization of dependency semantics | numerical/operator object | model-dependent | S3 | executable \(\neq\) empirically valid | CURRENT |
| \(S_e^{2\to3}\) | Stage2→3 readiness status | categorical status | N/A | S3 | PASS/BLOCKED/FAIL | CURRENT |
| \(\mathbb I_3^{ready}\) | dependencies permitted in accepted M2 dynamics | set | N/A | S3 | only readiness PASS | CURRENT |
| \(\mathbb I_3^{blocked}\) | causal/readiness-blocked ledger | set | N/A | audit | cannot drive accepted M2 | CURRENT |

Legacy primitive:

~~~math
\boxed{
\mathfrak I_{ij}^{\alpha\beta}
\text{ = LEGACY ONLY;}
\qquad
\mathfrak d_e
\text{ = CURRENT}.
}
~~~

## 5. Stage 3 — physical/hybrid dynamics

Authorities: Stage-3 ontology @ 80dd965391c672df303e46ace919a5dd6bf11ec5; Stage3→4 contract @ 8ecf4f64c0c97caa99704b130074eab50c271683

| Symbol | Definition | Type / class | Unit | Consumers | Validity / uncertainty | Status |
|---|---|---|---|---|---|---|
| \(Y^{phys}=(x_P,x_T,z_{PT})\) | physical/dynamic truth | state tuple / physical | heterogeneous/native | S4–S7 | model/case defined | CURRENT |
| \(x_P\) | power physical state/algebraic physical variables | state/algebraic / physical | native | S4–S7 | selected model family | CURRENT |
| \(x_T\) | transport physical/mobility state | state / physical | native | S4–S7 | selected model family | CURRENT |
| \(z_{PT}\) | justified P–T interface/memory state | state / physical-interface | native | S4–S7 | only if mechanism needs memory | CURRENT |
| \(z_a\) | algebraic variable | algebraic / physical | native | S3 | solver/model dependent | CURRENT |
| \(\eta(\mathbf r,t)\) | hazard/environmental forcing | exogenous forcing | hazard-dependent | S3–S7 | case model/provenance required | CURRENT |
| \(u^{exo}(t)\) | prescribed Stage-3 experimental/operational input | exogenous input | action-dependent | S3 | not Stage-4 policy | CURRENT |
| \(m(t)\) | discrete operating/disruption/recovery mode | discrete state | N/A | S3–S7 | mode semantics frozen by case | CURRENT |
| \(e_k\) | event triggering state/mode/topology transition | event object | time + metadata | S3 | event provenance required | CURRENT |
| \(q_j\) | Stage-3 physical QOI | derived metric | metric-dependent | H1/downstream | QOI \(\neq\) validation metric | CURRENT |
| \(Q(t)\) | physical service/capability trajectory | output vector | service/native | S4–S7 | service \(\neq\) resilience | CURRENT |
| \(\mathfrak M_3\) | selected Stage-3 model realization | model object | N/A | S4–S7 | claim ceiling attached | CURRENT |
| \(\mathbb U_3\) | Stage-3 uncertainty object | uncertainty object | heterogeneous | S4–S7 | parameter/IC/hazard/mechanism/model/numerical | CURRENT |
| \(Z_3\) | Stage-3 output tuple | composite output | heterogeneous | S4 | design schema | CURRENT |
| \(\Pi_{3\to4}\) | Stage3→4 companion provenance payload | provenance tuple | heterogeneous | S4/S5 integration | retains scenario/mode/active mechanisms/UQ/version | CURRENT |

Permanent:

~~~math
\boxed{Y^{phys}\neq y\neq\widehat Y\neq b_t.}
~~~

## 6. Stage 4 — observation, knowledge, organization and feasible control

Authority: STAGE4_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md @ 450440fd06088202c1266303cddf9b0e0c2a4c8c

| Symbol | Definition | Type / class | Unit | Consumers | Validity / uncertainty | Status |
|---|---|---|---|---|---|---|
| \(Y_4^{req}\) | subset of physical truth required by H2/S5/control | state-index set | N/A | S4 | derived from declared need | CURRENT |
| \(y_k\) | observation/measurement | observation / epistemic | measurement-native | S4 | time/availability/quality/UQ retained | CURRENT |
| \(\mathcal I_t\) | information available to estimator/operator | information set | heterogeneous | S4/S5 | availability semantics required | CURRENT |
| \(b_t\) | belief/state-estimation object | epistemic state | distribution/set/ensemble | S5 | representation validated by context | CURRENT |
| \(\widehat Y_t\) | point estimate when meaningful | estimate / epistemic | state-native | S4/S5 | secondary to belief | CURRENT |
| \(\mathbb U_{\widehat Y,t}\) | estimation uncertainty | uncertainty object | covariance/set/ensemble etc. | S5 | representation-specific | CURRENT |
| \(\mathcal G_I\) | communication topology | graph / information | N/A | S4 | \(\neq z_I\neq\mathcal I_t\) | CURRENT |
| \(z_I(t)\) | information-system dynamic state | state / information | native | S5 | distinct from available info | CURRENT |
| \(\mathfrak O\) | organization structure | graph/tuple / organization | heterogeneous | S4/S5 | \(\neq z_O\) | CURRENT |
| \(z_O(t)\) | organizational dynamic state | state / organization | native | S5 | case evidence required | CURRENT |
| \(\mathcal U_{feas}\) | physically/informationally/organizationally/resource feasible controls | feasible-action set | action-native | S5/S6 | intersection of constraints | CURRENT |
| \(u_t\) | operational control action | control / decision-operational | action-native | S4/S5 | \(u_t\in\mathcal U_{feas}\) | CURRENT |

## 7. Stage 5 — viability/reachability resilience

Authorities: constitution @ 3742632c3a0eda97ec4b6fb85aeb81cb334ed4c2; handoff @ 4aecfafb8515261bb4cd3f81db00b66dfdbd9d0c

| Symbol | Definition | Type / class | Unit | Consumers | Validity / uncertainty | Status |
|---|---|---|---|---|---|---|
| \(x_R=\Pi_R(Y^{phys})\) | resilience state projection | state projection / physical | heterogeneous | S5/S6 | requires physical-truth lineage | CURRENT |
| \(\mathcal K_{req}\) | requirement authority/set | requirements object | heterogeneous | S5/S6 | provenance class required | CURRENT |
| \(K\) | acceptable/viable set induced by requirements | state constraint set | state-dependent | S5/S6 | threshold provenance required | CURRENT |
| \(G_{rec}\) | recovery target set | set / resilience | state-dependent | S5/S6 | requirement/target provenance | CURRENT |
| \(F_{unsafe}\) | forbidden/unsafe set | set / safety | state-dependent | S5/S6 | authoritative basis required | CURRENT |
| \(T\) | Stage-5 disruption/recovery horizon | time horizon | time | S5/S6 | \(T\neq H_{LC}\) | CURRENT |
| \(\mathbb U_5\) | Stage-5 uncertainty | uncertainty object | heterogeneous | S6 | retain probability semantics | CURRENT |
| \(R_{curve}\) | conventional resilience performance/recovery baseline | baseline metric/curve | metric-dependent | H3 | baseline \(\neq\) ground truth | CURRENT |
| \(\mathcal V\) | controlled viability set/kernel | set / resilience | state-space | S5/S6 | control/uncertainty dependent | CURRENT |
| \(\mathcal R\) | controlled reachability/reach-avoid object | set / resilience | state-space | S5/S6 | target/unsafe/control dependent | CURRENT |
| \(\mathfrak R_T\) | resilience evidence tuple | composite resilience object | heterogeneous | S6/S7 | remain+return+confidence semantics | CURRENT |
| \(\mathcal D_R\) | engineering resilience diagnosis | diagnostic object | heterogeneous | S6 | evidence/validity attached | CURRENT |
| \(\mathbb I_{active}\) | mechanisms active in realized resilience dynamics | set / causal-physical | N/A | S6 | subset of qualified/ready mechanisms | CURRENT |
| \(\mathbf U_{1:5}\) | cumulative uncertainty lineage | uncertainty lineage | heterogeneous | S6 | stage-resolved | CURRENT |
| \(\Omega_5\) | Stage-5 validity domain | validity-domain object | N/A/heterogeneous | S6 | must remain attached | CURRENT |

## 8. Stage 6 — intervention performance and sustainability

Authority: constitution v2 @ 3493142f685c9520ee7f6bdf001a3dea131f2649; handoff v2 @ 9e955de444f13338987ca8669fc3aa5f6557cdc5

| Symbol | Definition | Type / class | Unit | Consumers | Validity / uncertainty | Status |
|---|---|---|---|---|---|---|
| \(a_k\) | strategic intervention | intervention / strategic decision | heterogeneous | S6/S7 | \(a_k\neq u(t)\) | CURRENT |
| \(\mathcal A_6^{qual}\) | Stage-6 qualified intervention set | set / intervention | N/A | S7 | validity-gated | CURRENT |
| \(a_0\) | status-quo baseline intervention | baseline | N/A | S6 | baseline semantics required | CURRENT |
| \(\Phi_a\) | intervention transformation operator | operator | model-dependent | S6 | distinct from dependency \(\Phi_e\) | CURRENT |
| \(FU_6\) | Stage-6 functional unit | accounting object | case-defined | S6/S7 | lifecycle accounting | CURRENT |
| \(\mathcal B_{LC}\) | lifecycle accounting boundary | boundary | time/system dependent | S6/S7 | \(T_5\neq H_{LC}\) | CURRENT |
| \(\mathbf T_{fx}\) | intervention-effectiveness target set | target/requirement object | heterogeneous | S6/S7 | provenance-tagged | CURRENT |
| \(\mathcal E_{fx}\) | target-attainment/effectiveness record | performance object | vector/status/native | S7 | resilience \(\neq\) effectiveness | CURRENT |
| \(\mathbf C_{res}\) | intervention resource vector | resource vector | heterogeneous/native | S6/S7 | evidence-supported dimensions only | CURRENT |
| \(\mathcal E_{fy}\) | resource-efficiency record | performance object | vector/ratios | S7 | no mandatory scalarization | CURRENT |
| \(\mathbf J_{sus}\) | sustainability consequence vector | consequence vector | heterogeneous/native | S7 | access/energy/carbon/cost separated | CURRENT |
| \(\Delta\mathfrak R\) | intervention-induced resilience change | resilience consequence | heterogeneous | S7 | baseline/intervention matched | CURRENT |
| \(\mathcal A_R^+\) | resilience-effective intervention set for canonical H4 | set | N/A | H4/S7 | \(\neq\mathcal A_{fx}^+\) generally | CURRENT |
| \(\mathcal A_{fx}^+\) | effectiveness-qualified set | set | N/A | S6/S7 | target-attainment PASS | CURRENT |
| \(\mathcal K_{sus}^{cand}\) | candidate sustainability/decision requirements | requirements object | heterogeneous | S7 | provenance/status retained | CURRENT |
| \(\mathbb U_6\) | Stage-6 uncertainty | uncertainty object | heterogeneous | S7 | multidimensional | CURRENT |
| \(\Pi_6\) | Stage-6 provenance map | provenance | N/A | S7 | versions/validation retained | CURRENT |

Permanent:

~~~math
\boxed{
\text{resilience}
\neq
\text{effectiveness}
\neq
\text{efficiency}
\neq
\text{sustainability}.
}
~~~

## 9. Stage 7 — engineering decision

Authority: STAGE7_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V2.md @ 38a71356b3c99d35d5b73f7b70fb7d32452f71d4

| Symbol | Definition | Type / class | Unit | Consumers | Validity / uncertainty | Status |
|---|---|---|---|---|---|---|
| \(\mathbf Z_7(a_k)\) | full candidate decision record | decision tuple | heterogeneous | S7 | inherits upstream claims/UQ | CURRENT |
| \(F^{a_k}\) | Stage-7 feasibility/admissibility state | status / decision constraint | N/A | S7 | evidence-gated | CURRENT |
| \(G_{7,F}\) | feasibility gate | gate | boolean/status | S7 | feasibility before preference | CURRENT |
| \(\mathcal A_7^{adm}\) | admissible intervention set | set / decision | N/A | S7 | only \(G_{7,F}=PASS\) | CURRENT |
| \(\mathcal P_7\) | Pareto/nondominated set | set / descriptive decision | N/A | S7 | objectives consistently oriented | CURRENT |
| \(\mathcal V_7\) | value/preference model | normative decision object | heterogeneous | S7 | only if justified | CURRENT-CONDITIONAL |
| \(\mathcal X_{common}\) | common H5 decision frame | comparator frame | heterogeneous | H5 | same in both arms | CURRENT |
| \(\mathcal A_R^\star\) | resilience-only decision set | decision set | N/A | H5 | primary comparator arm | CURRENT |
| \(\mathcal A_{R,S}^\star\) | resilience+sustainability decision set | decision set | N/A | H5 | sustainability added | CURRENT |
| \(D_{\mathcal A}\) | set-change/Jaccard distance | metric | dimensionless | H5 | finite-set interpretation | CURRENT |
| \(\delta_5\) | H5 materiality threshold | threshold | metric-specific | H5 | justification required | DEFERRED |
| \(\mathbb U_7\) | Stage-7 uncertainty object | uncertainty object | heterogeneous | S7 | includes value uncertainty | CURRENT |
| \(Reg(a,\omega)\) | decision regret | metric | loss-unit | S7/H5 | loss definition required | CURRENT |
| \(\Omega_{vuln}(a)\) | vulnerability scenario domain | set | N/A | S7 | diagnostic, not probability | CURRENT |
| \(S_D\) | decision-stability object | VVUQ/decision metric | heterogeneous | S7 | relative to declared domain/method | CURRENT |
| \(G_{7,ADAPT}\) | adaptive-pathway eligibility gate | conditional gate | status | S7 | not required for basic closure | CURRENT-CONDITIONAL |
| \(O_7\) | Stage-7 default output tuple | decision output | heterogeneous | thesis conclusion | claim ceiling applies | CURRENT |
| \(a^\star\) | unique preferred intervention | normative decision result | intervention ID | implementation | only with legitimate value/decision rule | DEFERRED/CONDITIONAL |

## 10. Global permanent category constraints

~~~math
\boxed{
Y_1^{schema}\not\equiv Y^{phys}
\not\equiv y
\not\equiv\widehat Y
\not\equiv b_t.
}
~~~

~~~math
\boxed{u(t)\neq a_k.}
~~~

~~~math
\boxed{
\Phi_e^{S1,exch}\neq\Phi_e^{S2,op},
\qquad
\gamma_e^{S1,int}\neq\gamma_e^{S2,act}.
}
~~~

~~~math
\boxed{
\text{service}
\neq
\text{resilience}
\neq
\text{effectiveness}
\neq
\text{efficiency}
\neq
\text{sustainability}
\neq
\text{preference}.
}
~~~

## 11. Registry-extension rule

Stage-local implementation variables not used across stages remain governed by their stage authority and are added globally only when they enter a cross-stage handoff, appear in a confirmatory hypothesis, affect a global requirement/claim, or create a notation collision.

## 12. Pre-data status

~~~text
cross-stage core symbols = REGISTERED
known symbol collisions = DISAMBIGUATED
legacy dependency primitive = QUARANTINED
case-specific numerical values = DEFERRED
empirical H1–H5 outcomes = NOT TESTED unless separately executed/authorized
~~~

## 11. Post-audit mathematical-normalization additions — 2026-09-19

**Authority:** `GLOBAL_MATHEMATICAL_CHAIN_CORRECTION_AND_FREEZE_V1.md` plus the cited stage amendments.

These additions do not change RQ/SO/H meanings or empirical status. They disambiguate the mathematical spaces and policy semantics required by the expert audit.

| Symbol | Definition | Type / class | Unit | Owner → consumers | Authority | Status |
|---|---|---|---|---|---|---|
| (mathcal C_{use}) | declared model/analysis/decision context of use | validity/intended-use object | N/A | input/global → S1–S7 | global mathematical-chain freeze v1 | CURRENT |
| (C_m) | Stage-3 continuous-flow/admissibility domain in mode (m) | hybrid domain / physical | state-dependent | S3 | Stage-3 hybrid-domain clarification v2.1 | CURRENT |
| (D_m) | Stage-3 jump/event domain in mode (m) | hybrid domain / physical | state-dependent | S3 | Stage-3 hybrid-domain clarification v2.1 | CURRENT |
| (A_{mathcal G}^{m}) | algebraic/network constraint operator; integration alias for parent (G_{mathcal G}^{m}) | operator / physical | equation-dependent | S3 | Stage-3 hybrid-domain clarification v2.1 | CURRENT-ALIAS |
| (J_e) | compact reset/mode/topology transition operator | hybrid jump map | model-dependent | S3 | Stage-3 hybrid-domain clarification v2.1 | CURRENT |
| (mathcal F_t^I) | sigma-algebra/filtration generated by information available through time (t) | information filtration / epistemic | N/A | S4 → S5 | Stage-4 policy information-adaptation amendment v1.1 | CURRENT |
| (Pi^{NA}) | nonanticipative/information-adapted operational policy class | policy set | action-dependent | S4 → S5 | Stage-4 v1.1 + Stage-5 v1.1 | CURRENT |
| (mathcal V_T^{x}) | physical-state viability object in resilience state space (mathcal X_R) | set / physical resilience | state-space | S5 → S6 | Stage-5 mathematical amendment v1.1 | CURRENT |
| (mathcal V_{alpha,T}^{b}) | belief-space stochastic maintainability set | set / epistemic resilience | belief-space | S5 → S6 | Stage-5 mathematical amendment v1.1 | CURRENT |
| (mathcal R_{eta,T}^{b}) | belief-space stochastic recovery/reach-avoid set | set / epistemic resilience | belief-space | S5 → S6 | Stage-5 mathematical amendment v1.1 | CURRENT |
| (T_{rec}^{Delta}) | sustained-recovery time with declared persistence interval (Delta_{rec}) where required | recovery QOI | time | S5 → S6/S7 | Stage-5 mathematical amendment v1.1 | CURRENT-CONDITIONAL |
| (D_R) | declared resilience-state scaling matrix for dimensionally coherent baseline geometry | normalization object | state-unit dependent | S5 | Stage-5 mathematical amendment v1.1 | CURRENT-CONDITIONAL |
| (S_e^{(q)}) | mechanism/interface perturbation effect on declared resilience QOI (q) | diagnostic sensitivity | QOI-dependent | S5/S6 diagnostic | Stage-5 mathematical amendment v1.1 | CURRENT |
| (mathbf S_e) | vector-valued interface sensitivity diagnostic | diagnostic vector | heterogeneous | S5/S6 diagnostic | Stage-5 mathematical amendment v1.1 | CURRENT |

Permanent new space firewall:

~~~math
oxed{
mathcal V_T^{x}

eq
mathcal V_{alpha,T}^{b}.
}
~~~

Permanent policy firewall:

~~~math
oxed{
piinPi^{NA}
Rightarrow
pi_t	ext{ uses only information available through }t.
}
~~~

Permanent criticality rule:

~~~math
oxed{
-partialho_{mathcal V}/partial w_{ij}
	ext{ is not a universal canonical interface-criticality definition.}
}
~~~
