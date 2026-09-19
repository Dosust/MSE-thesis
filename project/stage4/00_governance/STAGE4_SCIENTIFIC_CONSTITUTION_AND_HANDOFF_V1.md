# Stage 4 Scientific Constitution and Handoff v1

**Status:** CANONICAL STAGE-4 AUTHORITY  
**Effective date:** 2026-09-19  
**Supersedes:** no prior Stage-4 authority file; earlier observability v1 artifacts remain provenance.

## 1. Universal stage contract

\`\`\`math
\boxed{\mathfrak S_4=(Q_4,I_4,\mathcal C_4,\mathcal R_4,G_4,Z_4,\Lambda_4)}
\`\`\`

where \`Q4\` is the scientific question, \`I4\` admissible upstream inputs, \`C4\` the data-independent scientific constitution, \`R4\` a case realization, \`G4\` admissibility gates, \`Z4\` accepted output, and \`Lambda4\` the maximum defensible claim.

## 2. Admissible Stage-4 input

\`\`\`math
\boxed{
I_4=(\mathcal G,\mathbb I^{qualified},\mathfrak M_3,Y^{phys},Q,\Lambda_3)
}
\`\`\`

Stage 4 may not silently introduce a causal mechanism excluded by Stage 2, a state without Stage-3 semantics, or a claim stronger than \(\Lambda_3\).

## 3. Canonical Stage-4 constitution

\`\`\`math
\boxed{
\mathcal C_4=
(Y_4^{req},\mathcal H,\mathcal O_{obs},\mathcal I,
\mathcal E,\mathbb U_{\widehat Y},\mathcal G_I,
\mathfrak O,\mathcal U_{feas},\Pi)
}
\`\`\`

### 3.1 Physical truth and required states

\`\`\`math
Y_t^{phys}=(x_P(t),x_T(t),z_{PT}(t)).
\`\`\`

\`\`\`math
\boxed{
Y_4^{req}=\{Y_i\in Y^{phys}:H2_i\lor S5_i\lor C_i\}
}
\`\`\`

Parameters, exogenous inputs, derived QOIs, and software-fixture-only variables are not automatically members of \(Y_4^{req}\).

### 3.2 Observation

\`\`\`math
\boxed{y_k=\Gamma_k h^{m_k}(Y_k^{phys};\theta_H)+\nu_k}
\`\`\`

Each observation preserves measurement time, receive time, availability, quality, units, source, and uncertainty.

### 3.3 Available information

\`\`\`math
\boxed{\mathcal I_t=\{y_{0:t},\text{messages},\text{forecasts},\text{reports}\}}
\`\`\`

\`\`\`math
\boxed{\mathcal G_I\neq z_I(t)\neq\mathcal I_t.}
\`\`\`

\(\mathcal G_I\) is communication topology; \(z_I(t)\) is information-system state; \(\mathcal I_t\) is information actually available to an estimator/operator.

### 3.4 Estimation and uncertainty

\`\`\`math
\boxed{b_t=\mathcal E(\mathcal I_t,\mathfrak M_3)}
\`\`\`

When probabilistically justified,

\`\`\`math
b_t(Y)=p(Y_t\mid\mathcal I_t).
\`\`\`

A point estimate is secondary:

\`\`\`math
\widehat Y_t=\mathbb E[Y_t\mid\mathcal I_t]
\`\`\`

when meaningful. Uncertainty is generalized as

\`\`\`math
\boxed{\mathbb U_{\widehat Y,t}}
\`\`\`

and may be covariance, interval/set, ensemble/particles, or another validated representation.

### 3.5 Organization

\`\`\`math
\boxed{\mathfrak O=(V_O,E_O,A_O,R_O,\tau_O,\Xi_O)}
\`\`\`

Its dynamic state is \(z_O(t)\), therefore

\`\`\`math
\boxed{\mathfrak O\neq z_O(t).}
\`\`\`

### 3.6 Feasible control

\`\`\`math
\boxed{
\mathcal U_{feas}(t)=
\mathcal U_{phys}(t)\cap
\mathcal U_{info}(t)\cap
\mathcal U_{org}(t)\cap
\mathcal U_{resource}(t)
}
\`\`\`

The component constraint classes are evidence-grounded; this integrated intersection is a thesis-derived construct to test.

\`\`\`math
\boxed{u_t=\Pi(b_t,z_I,z_O),\qquad u_t\in\mathcal U_{feas}(t).}
\`\`\`

## 4. Case realization

\`\`\`math
\boxed{\mathcal R_4^c=\mathcal B_4(D^c;\mathcal C_4).}
\`\`\`

Every object receives four independent statuses:

\`\`\`math
S_{epistemic}\in\{E,D,H,P,A,U\},
\`\`\`

\`\`\`math
S_D\in\{DIRECT,DERIVED,PROXY,SYNTHETIC,PSEUDO,MISSING\},
\`\`\`

\`\`\`math
S_G\in\{PASS,OPEN,BLOCKED,FAIL\},
\`\`\`

\`\`\`math
S_V\in\{UNVERIFIED,VERIFIED,VALIDATED\}.
\`\`\`

These statuses must never be collapsed.

## 5. H2 architecture

\`\`\`math
\mathscr N_0=P+T,\qquad
\mathscr N_1=P+T+I,\qquad
\mathscr N_2=P+T+I+O.
\`\`\`

Matched physical initial condition, disturbance, admitted causal mechanisms, and physical parameters are held fixed. Only prespecified Stage-4 information/organizational conditions differ.

## 6. Stage-4 output

\`\`\`math
\boxed{Z_4=(b_t,\mathbb U_{\widehat Y,t},z_I(t),z_O(t),\mathcal U_{feas}(t),u_t,Z_4^{H2}).}
\`\`\`

## 7. Stage-4 → Stage-5 handoff

\`\`\`math
\boxed{
I_{4\to5}(t)=
(b_t,\mathbb U_{\widehat Y,t},\mathcal I_t,z_I(t),z_O(t),\mathcal U_{feas}(t))
}
\`\`\`

Mandatory distinctions:

\`\`\`math
Y_t^{phys}\not\equiv b_t,\qquad
\mathcal U_{phys}(t)\not\equiv\mathcal U_{feas}(t).
\`\`\`

## 8. Closure rule

\`\`\`math
\boxed{G_{4\to5}=G_{4-CON}\land G_{4-CASE}\land G_{4-V}\land G_{4-H2}.}
\`\`\`

Architecture finalization does not imply empirical closure.
