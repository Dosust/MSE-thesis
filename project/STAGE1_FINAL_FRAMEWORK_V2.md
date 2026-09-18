# Stage 1 Final Framework v2.0 — Frozen Candidate

**Stage:** 1 — Spatiotemporal Multilayer System-of-Systems Structure  
**Status:** PASS — PRE-FREEZE SYNCHRONIZED TO EVIDENCE/ONTOLOGY v2  
**Date:** 2026-09-18  
**Canonical architecture authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**Canonical RQ/SO/H authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Evidence/ontology authority:** `stage1_v2/Stage1_Evidence_and_Ontology_Register_v2_FINAL.md`

## 1. Scientific responsibility

**RQ1:** What entities exist, what layers constitute the system, and where can interactions occur?

**SO1:** Define the coupled Power–Transportation system boundary, entities, layers, locations, interfaces, states and service requirements, with Information and Organization as supporting domains.

~~~math
\boxed{\text{Stage 1 = structural possibility}\qquad\text{Stage 2 = causal qualification}.}
~~~

Stage 1 establishes entities, typed layers, spatial/temporal context, same-layer structure, structurally admissible cross-layer relations, interface/service semantics, requirements and provenance. It does not accept a causal dependency, estimate coupling strength, define a dynamic coupling law, or test H1.

## 2. Typed System of Systems

~~~math
\boxed{\mathcal S=\{P,T,I,O\},\qquad\mathcal S_{\rm phys}=\{P,T\},\qquad\mathcal S_{\rm sup}=\{I,O\}.}
~~~

Power and Transportation are physical constituent systems; Information and Organization are supporting domains.

## 3. Extended system boundary

~~~math
\boxed{\Omega_{\rm sys}^{+}=(\Omega_x,\Omega_t,\Omega_{\rm infra},\Omega_{\rm service},\Omega_{\rm mode},\Omega_{\rm jur}).}
~~~

## 4. Constituent graphs and spatial/state notation

~~~math
G_P=(V_P,E_P,\lambda_P),\qquad G_T=(V_T,E_T,\lambda_T).
~~~
~~~math
\boxed{\mathcal G^{(1)}=(\mathcal V,\mathcal E_{\rm intra},R,\Lambda)},\qquad R=\{r_i\}.
~~~
~~~math
\boxed{r_i=\text{spatial geometry/location}}
~~~
~~~math
Y(t)=[X_P(t),X_T(t),z_I(t),z_O(t)]^\top.
~~~

## 5. Semantic entity object

~~~math
\boxed{E_i^\alpha=(id_i,type_i,layer_i,r_i,f_i,\mathcal Y_i,o_i,a_i,\ell_i,\mathcal D_i).}
~~~

The object records identity/type, layer, geometry, engineering function/service roles, state schema, ownership/operator roles, authority roles, modeling resolution and evidence/provenance.

## 6. Structural admissibility

~~~math
\boxed{\Gamma_e^{\rm str}=\text{Stage-1 structural-admissibility predicate}.}
~~~
~~~math
\boxed{\Gamma_e^{\rm str}=1\not\Rightarrow\text{accepted causal dependency}.}
~~~
~~~math
\boxed{\mathcal C_{\rm struct}=\{e:\Gamma_e^{\rm str}=1\}.}
~~~

## 7. Final Stage-1 relation architecture

### 7.1 Core relation object

~~~math
\boxed{\mathfrak r_e^{(1)}=(\mathcal V_e,\sigma_e,\Gamma_e^{\rm str},\gamma_e,\Phi_e,d_e,m_e^{\rm cand},c_e^{\rm cand},s_e,\mathcal E_e).}
~~~

Core meanings: participating entities; scope; structural admission; interface semantics; exchanged/enabled service/resource/information/control/access; orientation; candidate mechanism family; candidate activation context; evidence/governance status; evidence/provenance.

### 7.2 Secondary relation metadata

~~~math
\boxed{a_e=(h_e,\pi_e,\kappa_e,\ell_e,b_e,q_e^{\rm evid},\chi_e^{\rm norm}).}
~~~

Metadata: hierarchy orientation; DIRECT/MEDIATED path; pairwise/higher-order arity; modeling resolution; admission basis; evidence confidence; normative/jurisdictional admissibility.

## 8. Structural existence, strength and confidence

~~~math
\boxed{I_e^{\rm struct}\neq w_e\neq q_e^{\rm evid}.}
~~~
~~~math
\boxed{I_e^{\rm struct}\in\{\mathrm{TEMPLATE\_ONLY},\mathrm{CANDIDATE},\mathrm{VERIFIED\_STRUCTURAL},\mathrm{UNRESOLVED},\mathrm{EXCLUDED}\}.}
~~~
~~~math
\boxed{w_e=\mathrm{NOT\_ESTIMATED\_STAGE1}.}
~~~

Numeric evidence confidence is admissible only with a declared auditable scoring/calibration method.

## 9. Relation evidence/governance status

~~~math
s_e\in\{K,C_N,C_U,C_L,C_S,C_E,G,U,X\}.
~~~

These are evidence/governance labels, not coupling strengths.

## 10. Permanent scientific guardrails

~~~math
\boxed{\begin{aligned}
\text{topology}&\neq\text{function},\\
\text{proximity}&\neq\text{dependency},\\
\text{correlation}&\neq\text{causality},\\
\text{standardized interface}&\neq\text{case-specific connection},\\
\text{case connection}&\neq\text{causal mechanism},\\
\text{common cause}&\neq\text{cross-infrastructure dependency},\\
\text{existence}&\neq\text{strength},\\
\text{strength}&\neq\text{evidence confidence}.
\end{aligned}}
~~~

## 11. Normative/jurisdictional structure

~~~math
\boxed{\mathcal N_1=\{N_k\}}
~~~
~~~math
\boxed{\chi_e^{\rm norm}=\mathrm{PASS}\not\Rightarrow\text{causal dependency}.}
~~~

## 12. Service and requirement traceability

~~~math
\boxed{\text{entity}\rightarrow\text{engineering function}\rightarrow\text{service role}\rightarrow\text{requirement}\rightarrow\text{measure}\rightarrow\text{threshold/rule}.}
~~~

## 13. Case-independent data architecture

~~~text
RAW -> STAGING -> CANONICAL -> DERIVED -> RELEASE
~~~

No silent imputation, CRS/unit conversion, geometry/topology repair, temporal reinterpretation, aggregation/disaggregation, crosswalk construction, evidence scoring or normative applicability inference is permitted.

Canonical intermediate representation: CIR-1 source manifest; CIR-2 semantic entities; CIR-3 intralayer edges; CIR-4 geometry; CIR-5 attributes; CIR-6 service/requirement traceability; CIR-7 Stage-1 relation records; CIR-8 assumptions; CIR-9 QA ledger; CIR-10 authority/requirements.

## 14. Operational projection and canonical handoff

~~~math
\boxed{Z_1^{\rm op}=(\Omega_{\rm sys}^{+},\mathcal S,\mathcal V,\mathcal R_{\rm intra},\mathcal R_{\rm inter},R,\mathcal E_{\rm prov}).}
~~~

Z1-op is an evidence/ontology projection; it does not silently replace the canonical implementation handoff.

~~~math
\boxed{Z_1^{\rm impl+}=(\mathcal S,\mathcal G^{(1)},R,\mathcal Y;\Omega_{\rm sys}^{+},\mathcal C_{\rm cross},\mathfrak R_1,\mathcal T_{\rm svc},\mathcal A_1,\mathcal N_1,\Pi_1).}
~~~

Here \mathfrak R_1 is the register of \mathfrak r_e^(1) relation records.

## 15. Six top-level Stage-1 gates

~~~text
G1-B  boundary explicit
G1-E  entities semantically defined
G1-I  intralayer structures physically defensible
G1-R  intersystem relation candidates explicitly characterized
G1-P  every admitted relation has traceable provenance
G1-C  premature causal claims prevented
~~~

Machine/schema/runtime checks are subordinate verification evidence under these six scientific gates.

## 16. Framework versus case

~~~math
\boxed{G_1^{\rm framework}\neq G_1^{\rm case}(c).}
~~~

## 17. Stage-1 to Stage-2 handoff

~~~math
\boxed{\mathfrak r_e^{(1)}\xrightarrow[\text{activation + validity + falsification + uncertainty}]{\text{mechanism qualification}}\mathfrak I_e.}
~~~

Stage 1 identifies what deserves causal investigation. Stage 2 determines whether a candidate relation is a genuine causal dependency and, if so, under what conditions and validity limits.

## 18. Freeze condition

Stage 1 may be frozen only after the v2 evidence register, this framework, the mathematical contract, machine schema, fixtures/runtime guards and exact repository manifest agree on the same relation architecture; all six G1 gates pass; and exact blob SHAs are recorded.