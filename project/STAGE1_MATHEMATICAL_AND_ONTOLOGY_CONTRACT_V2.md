# Stage 1 Mathematical and Ontology Contract v2.0

**Status:** **PASS — FROZEN**  
**Date:** 2026-09-18  
**Authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md` + `CANONICAL_RQ_SO_HYPOTHESES_V3.md` + `stage1_v2/Stage1_Evidence_and_Ontology_Register_v2_FINAL.md`

## 1. Provenance classes

Established theory, adapted theory, thesis-defined objects, assumptions and case instantiations remain explicitly separated as `[LIT]`, `[ADAPT]`, `[THESIS]`, `[ASSUMP]`, `[CASE]`.

## 2. System ontology

~~~math
\mathcal S=\{P,T,I,O\},\quad\mathcal S_{\rm phys}=\{P,T\},\quad\mathcal S_{\rm sup}=\{I,O\}.
~~~

## 3. Boundary and state notation

~~~math
\Omega_{\rm sys}^{+}=(\Omega_x,\Omega_t,\Omega_{\rm infra},\Omega_{\rm service},\Omega_{\rm mode},\Omega_{\rm jur}).
~~~
~~~math
\boxed{r_i=\text{spatial geometry/location}},\qquad Y(t)=[X_P,X_T,z_I,z_O]^\top.
~~~

## 4. Entity object

~~~math
\boxed{E_i^\alpha=(id_i,type_i,layer_i,r_i,f_i,\mathcal Y_i,o_i,a_i,\ell_i,\mathcal D_i).}
~~~

## 5. Structural relation admission

~~~math
\boxed{\Gamma_e^{\rm str}\in\{0,1\}}
~~~
for evaluated case relations. Mechanism templates carry an explicit template/N-A state rather than a fabricated case predicate.

~~~math
\Gamma_e^{\rm str}=1\not\Rightarrow\mathfrak I_e.
~~~

## 6. Core relation object

~~~math
\boxed{\mathfrak r_e^{(1)}=(\mathcal V_e,\sigma_e,\Gamma_e^{\rm str},\gamma_e,\Phi_e,d_e,m_e^{\rm cand},c_e^{\rm cand},s_e,\mathcal E_e).}
~~~

~~~math
\sigma_e\in\{\mathrm{INTRA},\mathrm{INTER},\mathrm{CONTEXT}\},\qquad s_e\in\{K,C_N,C_U,C_L,C_S,C_E,G,U,X\}.
~~~

## 7. Secondary relation metadata

~~~math
\boxed{a_e=(h_e,\pi_e,\kappa_e,\ell_e,b_e,q_e^{\rm evid},\chi_e^{\rm norm}).}
~~~

If path is MEDIATED, mediator path is explicit. If arity is PAIRWISE, exactly two participating entities are allowed. Higher-order representation is used only where pairwise decomposition loses mechanism meaning.

## 8. Structural existence, strength, confidence

~~~math
\boxed{I_e^{\rm struct}\neq w_e\neq q_e^{\rm evid}.}
~~~
~~~math
I_e^{\rm struct}\in\{\mathrm{TEMPLATE\_ONLY},\mathrm{CANDIDATE},\mathrm{VERIFIED\_STRUCTURAL},\mathrm{UNRESOLVED},\mathrm{EXCLUDED}\}.
~~~
~~~math
\boxed{w_e=\mathrm{NOT\_ESTIMATED\_STAGE1}.}
~~~

No Stage-1 record may use ACCEPTED_CAUSAL, a causal-effect estimate, or a functional coupling magnitude.

## 9. Evidence confidence

Evidence confidence is epistemic confidence, not physical coupling magnitude. Numeric scoring requires an explicit auditable method and provenance; otherwise use UNSCORED or categorical confidence.

## 10. Paths and common cause

~~~math
\pi_e\in\{\mathrm{DIRECT},\mathrm{MEDIATED}\}.
~~~
~~~math
\boxed{\eta\rightarrow P\ \text{and}\ \eta\rightarrow T\not\Rightarrow P\rightarrow T\ \text{or}\ T\rightarrow P.}
~~~

## 11. Normative admissibility

~~~math
\chi_e^{\rm norm}\in\{\mathrm{PASS},\mathrm{CONDITIONAL},\mathrm{BLOCKED},\mathrm{N/A},\mathrm{N/A\_TEMPLATE}\}.
~~~
~~~math
\boxed{\chi_e^{\rm norm}=\mathrm{PASS}\not\Rightarrow\mathfrak I_e.}
~~~

## 12. Assumptions

~~~math
A_k^{(1)}=(\text{statement},\text{reason},\text{evidence},\text{consequence},\text{sensitivity test}).
~~~

No assumption may remain hidden in cleaning, temporal harmonization, matching, topology repair, aggregation/disaggregation, crosswalk construction, evidence scoring or normative interpretation.

## 13. Stage-1 non-claims

Stage 1 does not establish accepted causal dependency, coupling magnitude, dynamic law, propagation delay/timescale, cascade outcome, viability/reachability result, intervention effectiveness, sustainability consequence or decision optimum.

## 14. Stage-1 handoff

~~~math
\boxed{Z_1^{\rm impl+}=(\mathcal S,\mathcal G^{(1)},R,\mathcal Y;\Omega_{\rm sys}^{+},\mathcal C_{\rm cross},\mathfrak R_1,\mathcal T_{\rm svc},\mathcal A_1,\mathcal N_1,\Pi_1).}
~~~

## 15. Six scientific gates

~~~text
G1-B boundary
G1-E entities
G1-I intralayer structure
G1-R intersystem relations
G1-P provenance
G1-C causal restraint
~~~

## 16. Stage-2 boundary

~~~math
\boxed{\mathfrak r_e^{(1)}\xrightarrow{G_2}\mathfrak I_e}
~~~

G2 requires mechanism evidence, activation qualification, parameter/uncertainty treatment, validity boundaries and falsification logic.

## 17. Freeze state

~~~math
\boxed{G_1^{\rm framework}=\mathrm{PASS\ —\ FROZEN}.}
~~~

This contract is frozen by `thesis/00_governance/STAGE1_FRAMEWORK_FREEZE_2026-09-18.md`. Semantic changes require an explicit Stage-1 amendment or unfreeze.
