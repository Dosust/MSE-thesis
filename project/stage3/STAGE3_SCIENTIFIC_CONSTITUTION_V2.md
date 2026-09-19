# Stage 3 Scientific Constitution v2

**Status:** CANONICAL STAGE-3 DESIGN AUTHORITY  
**Effective date:** 2026-09-19  
**Stage:** 3 — Physics-Based Hybrid Multiscale Dynamics  
**RQ/SO authority:** \`project/CANONICAL_RQ_SO_HYPOTHESES_V3.md\`  
**Dependency authority:** \`project/CANONICAL_DEPENDENCY_CONTRACT_V1.md\`  
**Supersedes for active Stage-3 governance:** \`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md\` as active authority; that file remains supporting theory/provenance.  
**Empirical closure:** NOT IMPLIED.

## 1. RQ3 / SO3 / H1

### RQ3

> **How, when, and where do accepted interdependency mechanisms evolve and propagate through the coupled system?**

### SO3

> **Develop and verify a physics-based hybrid multiscale dynamic model and test its incremental explanatory or predictive value against independent and static-coupling representations.**

### H1

> **Under matched Power–Transportation disturbances and initial conditions, an evidence-grounded dynamic causal coupling representation provides measurable incremental explanatory or predictive information for preregistered cascade, service-loss, spatial-propagation, and recovery outcomes relative to corresponding static-coupling and independent-system representations.**

H1 superiority is not assumed.

## 2. Universal Stage-3 contract

\`\`\`math
\boxed{
\mathfrak S_3
=
(Q_3,I_3,\mathcal C_3,\mathcal R_3,G_3,Z_3,\Lambda_3).
}
\`\`\`

Where:

- \(Q_3\): RQ3/SO3/H1 scientific obligation;
- \(I_3\): admissible upstream input schema;
- \(\mathcal C_3\): case-independent Stage-3 constitution;
- \(\mathcal R_3\): case realization built from qualified data without altering \(\mathcal C_3\);
- \(G_3\): design, case, VVUQ and experiment gates;
- \(Z_3\): accepted Stage-3 output;
- \(\Lambda_3\): maximum defensible claim.

## 3. Admissible Stage-3 input

\`\`\`math
\boxed{
I_3=
\left(
\mathcal G_0,
\mathbb I_3^{ready},
Y_0^{phys},
\eta,
u^{exo},
\Theta,
\mathcal Q,
\Lambda_2
\right).
}
\`\`\`

All case-specific values may remain DEFERRED during design freeze.

### 3.1 Admission requirements

- \(\mathcal G_0\) must satisfy Stage-1 structural authority.
- Each dynamic causal dependency must satisfy the Stage2→3 readiness contract.
- \(Y_0^{phys}\) must satisfy the Stage-3 ontology.
- \(\eta\) must have declared meaning, units, provenance and validity.
- \(u^{exo}\) is a prescribed physical/operational input, not Stage-4 policy output.
- \(\Theta\) must be registered; unknown values remain OPEN/DEFERRED.
- \(\mathcal Q\) must have declared service semantics.
- Stage 3 may not make a claim stronger than \(\Lambda_2\) permits for upstream mechanisms.

## 4. Case-independent constitution

Define

\`\`\`math
\boxed{
\mathcal C_3=
(
\mathcal O_3,
\mathcal F_3,
\mathcal T_3,
\mathcal M_3^{cand},
\Omega_3,
\mathbb U_3,
\mathcal B_3,
\mathcal V_3,
\mathcal H_1
),
}
\`\`\`

where:

- \(\mathcal O_3\): Stage-3 state/input/output/QOI ontology;
- \(\mathcal F_3\): admissible hybrid-dynamic operator semantics;
- \(\mathcal T_3\): time/event/delay/multirate semantics;
- \(\mathcal M_3^{cand}\): admissible model-family set and selection rule;
- \(\Omega_3\): generic scenario schema;
- \(\mathbb U_3\): Stage-3 uncertainty taxonomy;
- \(\mathcal B_3\): benchmark ladder;
- \(\mathcal V_3\): VVUQ obligations;
- \(\mathcal H_1\): frozen comparator architecture and claim logic.

## 5. Physical truth and state ownership

\`\`\`math
\boxed{
Y_3^{phys}(t)
=
(x_P(t),x_T(t),z_{PT}(t)).
}
\`\`\`

The information/decision quantities

\`\`\`math
y_t,\mathcal I_t,\widehat Y_t,b_t,z_I(t),z_O(t),
\mathcal U_{feas}(t),u_t^{policy}
\`\`\`

are Stage-4 objects and are not Stage-3 physical state.

A dependency-specific \(\zeta_e\) may contribute to \(z_{PT}\) only when it represents genuine physical/interface memory needed by a Stage2→3-ready mechanism.

## 6. Generic hybrid-dynamic semantics

Stage 3 admits heterogeneous subsystem equations rather than forcing all infrastructures into one equation class.

For continuous/quasi-continuous state \(x\), algebraic variables \(z_a\), discrete state/mode \(m\), topology \(\mathcal G\), and active ready dependencies:

\`\`\`math
\boxed{
\dot x
=
F_{\mathcal G}^{m}
\left(
x,z_a,u^{exo},\eta;
\Theta,
\Xi_{\mathbb I^{active}}
\right),
}
\`\`\`

\`\`\`math
\boxed{
0=
G_{\mathcal G}^{m}
\left(
x,z_a,u^{exo},\eta;\Theta
\right),
}
\`\`\`

with event updates

\`\`\`math
x(t_k^+)=R_{e_k}(x(t_k^-),z_a(t_k^-),m(t_k^-),\eta),
\`\`\`

\`\`\`math
m(t_k^+)=\Delta_m(m(t_k^-),Y^{phys}(t_k^-),e_k),
\`\`\`

\`\`\`math
\mathcal G(t_k^+)
=
\Delta_{\mathcal G}
(\mathcal G(t_k^-),Y^{phys}(t_k^-),e_k).
\`\`\`

The abstract notation allows ODE, DAE, QSTS, network-flow, CTM/DTA, mesoscopic/microscopic, event-driven or validated co-simulation realizations.

## 7. Mechanism-to-dynamics bridge

The required scientific chain is

\`\`\`math
\boxed{
\mathfrak d_e
\xrightarrow{G_{2\to3}}
\mathfrak d_e^{(3)}
\xrightarrow{\mathcal X_3}
\Xi_e
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Y^{phys}(t)
\rightarrow
Q(t).
}
\`\`\`

The receiver's native physics remains distinct from the cross-system mechanism.

\`\`\`math
\boxed{
F_r\neq\Phi_e.
}
\`\`\`

Coupling modifies or constrains native physics; it does not replace it.

## 8. Time and multirate semantics

Stage 3 must distinguish:

\`\`\`math
\boxed{
t_{event}
\neq
\delta_e
\neq
\tau_e^{char}
\neq
\Delta t_{solver}
\neq
\Delta t_{comm}
\neq
T_{horizon}.
}
\`\`\`

No numerical value is frozen by this constitution. Values must be justified by model fidelity, mechanism timing, numerical convergence, and case evidence.

## 9. Model-family selection

The final Stage-3 model is not selected by looking for favorable H1 results.

\`\`\`math
\boxed{
\mathfrak M_3^\star
=
\mathcal F_{select}
(
RQ_3,
\mathcal QOI_3,
\mathcal T_3,
\mathbb I_3^{ready},
D,
C_{comp},
C_{VVUQ}
).
}
\`\`\`

Selection must satisfy hard admissibility gates before computational convenience is considered. Among admissible families, use the minimum sufficient fidelity that can answer RQ3 and meet VVUQ obligations.

Current software/model candidates remain candidates until the model-family protocol is applied to a qualified case.

## 10. H1 comparator architecture

The existing H1 architecture is preserved:

\`\`\`math
\boxed{
M_0=\text{independent }P+T,
}
\`\`\`

\`\`\`math
\boxed{
M_1=\text{static/algebraic coupling},
}
\`\`\`

\`\`\`math
\boxed{
M_2=\text{dynamic causal coupling}.
}
\`\`\`

### 10.1 Matched experiment rule

For realization \(r\),

\`\`\`math
\omega_r^{M_0}
=
\omega_r^{M_1}
=
\omega_r^{M_2}
\`\`\`

for all prespecified quantities that are not the coupling representation under test.

### 10.2 Dynamic mechanism rule

\`\`\`math
\boxed{
\mathbb I_{s,M_2}^{active}
\subseteq
\mathbb I_3^{ready}.
}
\`\`\`

Blocked or failed dependencies cannot be activated as accepted M2 causal mechanisms.

### 10.3 Prediction versus divergence

With qualified independent reference \(y^R\),

\`\`\`math
E_q^{(M)}
=
d_q(y_q^{(M)},y_q^R)
\`\`\`

may support predictive/explanatory comparison when \(d_q\) is prospectively frozen.

Without a qualified reference, report only model divergence or omitted-dynamics effects, not predictive superiority.

## 11. QOI ownership

Stage-3 primary H1 families remain:

- cascade;
- service loss;
- spatial propagation;
- recovery.

Exact confirmatory metrics remain DEFERRED until the reference and context of use are qualified.

Physical consequences such as ENS, delay, queues or recovery time are not automatically model-error scores.

Stage-5 viability/reachability quantities cannot be used to choose the Stage-3 model.

## 12. Uncertainty

The Stage-3 taxonomy is

\`\`\`math
\boxed{
\mathbb U_3
=
(
U_\theta,
U_{IC},
U_\eta,
U_{\mathbb I},
U_M,
U_N
).
}
\`\`\`

Where:

- \(U_\theta\): parameter uncertainty;
- \(U_{IC}\): initial-condition uncertainty;
- \(U_\eta\): hazard/forcing uncertainty;
- \(U_{\mathbb I}\): mechanism/mapping uncertainty;
- \(U_M\): model-form uncertainty;
- \(U_N\): numerical uncertainty.

Aleatory and epistemic components must be distinguished where meaningful. Scenario frequency is not probability unless the scenario-generation process justifies a probability interpretation.

## 13. Case realization

\`\`\`math
\boxed{
\mathcal R_3^c
=
\mathcal B_3(D^c;\mathcal C_3).
}
\`\`\`

A case realization binds:

- actual network/topology;
- selected model families;
- initial state;
- forcing;
- active Stage2→3-ready dependencies;
- parameter values/distributions;
- numerical resolutions;
- scenario IDs;
- reference data;
- VVUQ acceptance criteria.

The binding process may populate DEFERRED fields but may not modify the case-independent semantics after target-result inspection without a versioned amendment.

## 14. Stage-3 gate architecture

### 14.1 Design gates

\`\`\`math
\boxed{
G_{3,DESIGN}
=
G_{3-CON}
\land
G_{3-IN}
\land
G_{3-ONT}
\land
G_{3-TIME}
\land
G_{3-MODEL}
\land
G_{3-SCEN}
\land
G_{3-UQ}
\land
G_{3-VVUQ}
\land
G_{3-HANDOFF}
\land
G_{3-CLAIM}.
}
\`\`\`

These govern architecture closure only.

### 14.2 Case/execution gates

The existing execution-gate family remains valid for the realized case, including causal admission/readiness, model class, state space, well-posedness, physics, coupling, synchronization, parameter identifiability, UQ, numerical verification, V&V, QOI freeze and matched experiment authorization.

\`\`\`math
\boxed{
G_{3,DESIGN}=PASS
\not\Rightarrow
G_{3,CASE}=PASS.
}
\`\`\`

## 15. Benchmark and VVUQ requirement

The Stage-3 benchmark ladder is

\`\`\`math
\boxed{
B_{3,0}\rightarrow B_{3,1}\rightarrow B_{3,2}\rightarrow B_{3,3}
}
\`\`\`

for analytic/unit fixtures, independent subsystem verification, coupled synthetic verification, and qualified case application respectively.

Verification, validation and UQ remain separate obligations. A preview software fixture cannot validate the thesis model.

## 16. Stage-3 output

\`\`\`math
\boxed{
Z_3=
(
\mathfrak M_3,
Y^{phys}(t),
\mathcal G(t),
m(t),
\mathbb I^{active}(t),
Q(t),
\mathbb U_3,
\Lambda_3
).
}
\`\`\`

For formal handoff to Stage 4, this output is projected onto the exact Stage-4 admissible-input contract.

## 17. Claim ceiling \(\Lambda_3\)

Stage-3 claim levels are ordered:

### \(\Lambda_{3,0}\) — specification only
Architecture/model semantics exist; no executable evidence.

### \(\Lambda_{3,1}\) — verification
Implementation reproduces analytic/software fixtures and applicable limiting cases.

### \(\Lambda_{3,2}\) — realistic-synthetic developmental evidence
Reproducible model/mechanism differences are demonstrated in a qualified realistic-synthetic case.

### \(\Lambda_{3,3}\) — predictive/explanatory comparison
Requires qualified independent reference, frozen QOI metrics and completed VVUQ.

### \(\Lambda_{3,4}\) — confirmatory H1 adjudication
Requires all preregistration/data/VVUQ gates and authorized matched \(M_0/M_1/M_2\) execution.

No result may be described at a higher level than the evidence permits.

## 18. Explicitly DEFERRED before case/data qualification

This constitution does not freeze:

- development or held-out feeder IDs;
- road subnetwork;
- hazard magnitude/geometry/duration;
- charger or repair parameter values/distributions;
- currently blocked causal mechanisms;
- final case-specific model family;
- solver or communication timestep values;
- independent reference;
- exact primary H1 distance metrics;
- numerical acceptance tolerances;
- UQ convergence threshold;
- \(\delta_1\);
- H1 result.

## 19. Scientific firewall

\`\`\`math
\boxed{
\text{design closure}
\neq
\text{case closure}
\neq
\text{model validation}
\neq
\text{H1 support}.
}
\`\`\`

Unknown evidence remains OPEN/BLOCKED/DEFERRED. It is never replaced by a convenient value solely to permit execution.
