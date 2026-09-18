# Stage 2 Causal Object Contract v1

**Status:** **SUBORDINATE MATHEMATICAL IMPLEMENTATION — GOVERNED BY FROZEN STAGE-2 CONTRACT**  
**Normative authority:** `STAGE2_CASE_INDEPENDENT_CAUSAL_GOVERNANCE_CONTRACT_V1.md`

## 1. Design principle

The Stage-2 object must preserve the frozen Stage-1 candidate while adding only causal-qualification information.

~~~math
\boxed{\mathfrak D_e^{(2)}=(\mathfrak r_e^{(1)},\mathcal C_e,\Sigma_e,\Pi_e,S_e^\theta,G_2(e))}
~~~

where `mathfrak D_e^(2)` is the complete causal-evidence dossier.

## 2. Causal claim core

~~~math
\boxed{\mathcal C_e=(src_e,rec_e,d_e,\gamma_e,\Phi_e)}
~~~

- `src_e`: source entity/state;
- `rec_e`: receiver entity/state;
- `d_e`: tested direction;
- `γ_e`: frozen interface semantics;
- `Φ_e`: frozen exchanged/enabled service/resource/information semantic.

## 3. Realized cross-interface signal

Stage 1 defines **what kind** of quantity/service is exchanged. Stage 2 may define the realized signal:

~~~math
\phi_e(t)=\text{realized interface service/resource/information/action associated with }\Phi_e.
~~~

`φ_e(t)` is not automatically numeric; it may be binary, categorical, continuous, set-valued, or event-based depending on evidence.

## 4. Mechanism block

~~~math
\boxed{\Sigma_e=(m_e,\mathcal A_e,\psi_e,\theta_e,\tau_e)}
~~~

- `m_e`: causally qualified mechanism statement;
- `A_e`: activation predicate;
- `ψ_e`: receiver-response relation class;
- `θ_e`: mechanism-specific parameters;
- `τ_e`: delay/characteristic-timescale object.

Activation is represented as:

~~~math
\boxed{\mathcal A_e(Y,t,m,\eta,z_I,z_O)\in\{0,1\}}
~~~

when binary activation is justified. More general probabilistic/set-valued activation may be used if evidence requires it.

A generic response representation is:

~~~math
\Delta y_{rec,e}(t)=\psi_e\!\left(\phi_e(t-\tau_e),Y(t),m(t);\theta_e\right).
~~~

This is a **contract form**, not a claim that every relation is continuous or differentiable.

## 5. Evidence / uncertainty / validity / falsification block

~~~math
\boxed{\Pi_e=(\mathcal E_e^{(2)},\mathcal U_e,\mathcal V_e,\mathcal F_e)}
~~~

- `E_e^(2)`: causal evidence portfolio and provenance;
- `U_e`: epistemic, parameter, measurement and model-form uncertainty relevant to the relation;
- `V_e`: declared validity domain;
- `F_e`: falsification/revision condition.

Validity should declare, where relevant: asset class, spatial scale, temporal scale, operating mode, hazard/recovery regime, technological configuration and jurisdiction/organizational regime.

## 6. Evidence portfolio

~~~math
\mathbf e_e=(e_{mech},e_{case},e_{interface},e_{activation},e_{temporal},e_{empirical},e_{operational},e_{contrary}).
~~~

No default weighted sum is defined. If a future quantitative evidence score is proposed, its calibration and decision meaning require separate justification.

## 7. Parameter status

~~~math
S_e^\theta\in\{\mathrm{UNESTIMATED},\mathrm{BOUNDED},\mathrm{CALIBRATED},\mathrm{VALIDATED}\}.
~~~

Parameter status must never be inferred from evidence confidence.

## 8. Qualified causal interdependency

Only after `G2(e)=PASS`:

~~~math
\boxed{\mathfrak I_e=(\mathcal C_e,\Sigma_e,\Pi_e,S_e^\theta)}
~~~

The Stage-1 record remains linked by immutable provenance.

## 9. Stage-3 handoff

~~~math
\boxed{\mathfrak I_e\xrightarrow{G_{2\to3}}\text{admissible coupling input to }F_{\mathcal G}^{m}}
~~~

Stage 3 may adapt `ψ_e`, `θ_e`, or `τ_e` into its chosen hybrid dynamic representation only within the Stage-2 validity/evidence limits.