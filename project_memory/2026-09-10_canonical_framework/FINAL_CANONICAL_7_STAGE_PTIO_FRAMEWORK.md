# Final Canonical 7-Stage P–T–I–O Resilience-to-Sustainability Framework

**Canonical date:** 2026-09-10  
**Status:** FINAL / CANONICAL until explicitly changed by the author.  
**Governance:** This record supersedes earlier internal mathematical formulations of the seven-stage framework while preserving the seven-stage architecture and ordering.

## Canonical framework

\[
\boxed{
\text{Structure}
\rightarrow
\text{Causality}
\rightarrow
\text{Hybrid Multiscale Dynamics}
\rightarrow
\text{Observation, Organization \& Control}
\rightarrow
\text{Controlled Viability}
\rightarrow
\text{Sustainability Translation}
\rightarrow
\text{Transformation Pathways}
}
\]

The framework concerns interdependent **Power–Transportation systems** with **Information** and **Organization** represented explicitly. Stages 1–5 form the resilience-analysis core. Stage 6 translates resilience findings into sustainability requirements. Stage 7 converts those requirements into candidate long-term transformation pathways.

---

## Stage 1 — Multilayer Structural Knowledge Base

### Purpose
Defines the coupled Power–Transportation–Information–Organization architecture, explicit interfaces, admissible relations, and evidence status.

### Main mathematical object

\[
\boxed{(\mathfrak G_1,\mathfrak E_1)}
\]

with structural core

\[
\mathfrak G_1=
\left(
\mathcal G_P,
\mathcal G_T,
\mathcal G_I,
\mathcal G_O,
\mathcal Z,
E_\times
\right),
\]

and evidence core

\[
\mathfrak E_1=
\left(
\mathcal Q_{\rm adm},
S_{ij},
\mathcal E_{\rm prov}
\right).
\]

Here \(\mathcal Z=\{z_{ij}\}\) denotes explicit cross-layer engineering or functional interfaces. A relation status may be represented as

\[
S_{ij}\in\{D,C,L,U,X\},
\]

where \(D\) = confirmed dependency, \(C\) = conditional dependency, \(L\) = latent/candidate relation, \(U\) = unresolved/unknown, and \(X\) = excluded by scope or engineering admissibility.

### Core principle

\[
\boxed{\text{No visible edge}\neq\text{proof of no dependency}.}
\]

### Main question
**What exists, what can interact, and what is known?**

### Output
\[
\boxed{\mathfrak M_1=(\mathfrak G_1,\mathfrak E_1)}
\]

---

## Stage 2 — Causal Mechanisms

### Purpose
Converts admissible structural relations into evidence-supported cause–effect pathways.

### Main mathematical object

\[
\boxed{(\mathcal E,\mathcal A_{\rm cause},m,p)}
\]

with causal graph

\[
\mathcal C=(\mathcal E,\mathcal A_{\rm cause}).
\]

A causal record may be written as

\[
c_{ij}=
(e_i,e_j,z_{ij},m_{ij},p_{ij},\gamma_{ij},\Delta t_{ij},\eta_{ij}).
\]

Mechanism type and propagation form are distinct:

\[
m_{ij}\in
\{\text{physical, functional, information/control, recovery/access, organizational, geographic exposure}\},
\]

\[
p_{ij}\in
\{\text{direct, cascade, feedback/amplification, common cause}\}.
\]

### Causal evidence rule
A causal arc enters the model only when structural plausibility, mechanism, trigger, temporal consistency, and evidence are jointly satisfied.

### Core principle

\[
\boxed{\text{hazard}\neq\text{event}\neq\text{dependency}\neq\text{propagation}.}
\]

### Main question
**Why and through which mechanism does disruption propagate?**

---

## Stage 3 — Coupled Hybrid Multiscale Dynamics

### Purpose
Models continuous physical evolution, interface dynamics, discrete failure/recovery events, operating modes, and heterogeneous timescales.

### Plant state

\[
\boxed{X=(X_P,X_T,Z)}
\]

where \(X_P\) is the power-system state, \(X_T\) is the transportation-system state, and \(Z\) contains cross-layer interface states.

### Continuous dynamics

\[
\boxed{\dot X=F_q(X,u,\eta;\theta)}
\]

with subsystem decomposition

\[
\dot X_P=f_P(X_P,Z,u_P,\eta_P),
\]

\[
\dot X_T=f_T(X_T,Z,u_T,\eta_T),
\]

\[
\dot Z=f_Z(X_P,X_T,Z,u,\eta).
\]

Where required by algebraic power-flow or traffic-equilibrium constraints, a hybrid differential-algebraic form may be used:

\[
\mathcal F_q(\dot X,X,\lambda,u,\eta;\theta)=0.
\]

### Discrete events

\[
\boxed{X(t_k^+)=J_{e_k}(X(t_k^-)).}
\]

### Heterogeneous timescales

\[
\tau=
\{\tau_P,\tau_T,\tau_{PT},\tau_{TP},\tau_I,\tau_O,\tau_R\}.
\]

A useful separation is

\[
\tau_{\rm physical}=\{\tau_P,\tau_T,\tau_{PT},\tau_{TP}\},
\qquad
\tau_{\rm response}=\{\tau_I,\tau_O,\tau_R\}.
\]

### Main question
**How and when does the coupled physical system evolve?**

### Output

\[
\boxed{(X,F_q,J,\tau)}
\]

---

## Stage 4 — Observation, Organization, Feedback & Control

### Purpose
Separates sensing, information transmission, state estimation, organizational capability, decision-making, and intervention.

### Measurement

\[
\boxed{y_m(t)=H_m(X(t-\tau_m))+\nu_m(t)}
\]

### Information state
\(I(t)\) represents sensing, communication availability, latency, data quality, and related information-system conditions.

### State estimation

\[
\boxed{\hat X(t)=\mathcal E_{\rm est}(y_{[0,t]},I(t))}
\]

### Organizational state

\[
O(t)=
[R_O,A_O,C_O,W_O,D_O],
\]

where the components represent resources, authority, coordination, workforce, and response/decision capability or delay.

### Decision law

\[
\boxed{u(t)=\pi(\hat X(t),I(t),O(t))}
\]

Possible controls include switching, dispatch, rerouting, repair, V2G, backup supply, and resource allocation.

### Closed-loop logic

\[
\boxed{X\rightarrow y\rightarrow I\rightarrow\hat X\rightarrow O\rightarrow u\rightarrow X.}
\]

The full closed-loop state may be written as

\[
Y=(X,I,O).
\]

### Main question
**How does the system observe, coordinate, and respond?**

### Output

\[
\boxed{(y,H,\mathcal E_{\rm est},\hat X,I,O,\pi,u)}
\]

---

## Stage 5 — Controlled Viability

### Purpose
Determines whether acceptable coupled service can be maintained under constraints and disturbances, and quantifies distance/sensitivity to viability loss.

### Resilience/service admissible set

\[
\boxed{
K_R=
K_P\cap K_T\cap K_Z\cap K_I\cap K_O\cap K_{\rm service}
}
\]

### Finite-horizon viability

\[
\mathcal V_T(K_R)=
\left\{
Y_0:
\exists\pi,
Y^\pi(t)\in K_R,
\forall t\in[0,T]
\right\}.
\]

### Robust nonanticipative viability

\[
\boxed{
\mathcal V_T^R(K_R)=
\left\{
Y_0:
\exists\pi\in\Pi_{\rm NA},
\forall\eta\in\mathcal H,
Y^{\pi,\eta}(t)\in K_R,
\forall t\in[0,T]
\right\}
}
\]

where \(\Pi_{\rm NA}\) is the set of admissible nonanticipative policies.

### Viability boundary and signed margin

\[
\partial\mathcal V_T^R
\]

and

\[
\boxed{
\rho_{\mathcal V}(Y)=
\operatorname{sdist}(Y,\partial\mathcal V_T^R)
}
\]

with \(\rho_{\mathcal V}>0\) in the viable interior, \(\rho_{\mathcal V}=0\) on the boundary, and \(\rho_{\mathcal V}<0\) outside.

### Normalized interface criticality
Interface variables should be normalized before cross-interface comparison. A candidate local criticality is

\[
\boxed{
C_{ij}^{\mathcal V}
=-
\frac{\partial\tilde\rho_{\mathcal V}}
{\partial\tilde z_{ij}}
}
\]

or a standardized finite-difference equivalent for nonsmooth models.

### CARe / HJ computational interpretation
A Hamilton–Jacobi value function \(V^*(t,Y)\) may identify the relevant viability/reachability boundary through a zero level set,

\[
V^*(t,Y)=0,
\]

but in general

\[
\boxed{V^*(t,Y)\neq\rho_{\mathcal V}(Y).}
\]

CARe is therefore a **candidate certified computational route** for approximating/certifying the relevant boundary, not the definition of viability geometry itself.

### Main question
**Can acceptable service survive and recover?**

### Output

\[
\boxed{
(K_R,\mathcal V_T^R,\partial\mathcal V,\rho_{\mathcal V},C_{ij}^{\mathcal V})
}
\]

---

## Stage 6 — Resilience-to-Sustainability Transformation Interface

### Purpose
Converts resilience diagnosis into explicit long-term sustainability requirements without redefining the resilience core.

### Governance rule

\[
\boxed{\text{Stages 1–5 analyze resilience; Stage 6 performs explicit sustainability translation.}}
\]

Define resilience outputs

\[
R_{\rm out}=
\{\rho_{\mathcal V},C_{ij}^{\mathcal V},Q_P,Q_T,T_R,E_{\rm unserved},\text{resource demand},\text{dominant mechanisms}\}.
\]

Let \(B_{\rm sus}\) denote the sustainability baseline and \(T_{\rm sus}\) the long-term sustainability targets.

### Translation operator

\[
\boxed{
S_{\rm req}
=
\Phi_{\rm sus}(R_{\rm out},B_{\rm sus},T_{\rm sus})
}
\]

The output may include requirements for capacity, redundancy, information robustness, organizational capability, critical service, environmental performance, and related transformation needs.

### Main question
**What sustainability requirements follow from the resilience results?**

### Output

\[
\boxed{S_{\rm req}}
\]

---

## Stage 7 — Sustainable Transformation Pathways

### Purpose
Converts the Stage-6 requirements into technical, informational, organizational, environmental, and policy/planning changes implemented over time.

### Transformation decision

\[
\boxed{
a_k=
[a_k^{\rm tech},a_k^{\rm info},a_k^{\rm org},a_k^{\rm env},a_k^{\rm policy/planning}]
}
\]

### Structural transformation

\[
\boxed{
Y_{k+1}^{\rm struct}
=
\Psi_{\rm tr}(Y_k^{\rm struct},a_k)
}
\]

### Feasible pathway set

\[
\boxed{
a_{0:H}\in\mathcal A_{\rm feasible}
}
\]

and

\[
\boxed{
\mathcal P_{\rm trans}
=
\text{candidate sustainable transformation pathways}
}
\]

An optimal symbol \(a^*\) must not be introduced until a formal optimization objective, constraints, and preference/selection rule are explicitly defined.

### Main question
**What should be changed, where, when, and in what sequence?**

### Output

\[
\boxed{\mathcal P_{\rm trans}}
\]

---

# Final mathematical chain

\[
\boxed{
(\mathfrak G_1,\mathfrak E_1)
\rightarrow
(\mathcal E,\mathcal A_{\rm cause},m,p)
\rightarrow
(X,F_q,J,\tau)
\rightarrow
(y,H,\mathcal E_{\rm est},\hat X,I,O,\pi,u)
\rightarrow
(K_R,\mathcal V_T^R,\partial\mathcal V,\rho_{\mathcal V},C^{\mathcal V})
\rightarrow
(B_{\rm sus},T_{\rm sus},\Phi_{\rm sus},S_{\rm req})
\rightarrow
(a_{0:H},\Psi_{\rm tr},\mathcal P_{\rm trans})
}
\]

# Conceptual change

The framework is not reduced to

\[
\text{network}
\rightarrow
\text{resilience metric}
\rightarrow
\text{sustainability}.
\]

The canonical scientific chain is

\[
\boxed{
\text{evidence-qualified structure}
\rightarrow
\text{causal mechanisms}
\rightarrow
\text{physics}
\rightarrow
\text{feedback}
\rightarrow
\text{viability}
\rightarrow
\text{engineering requirements}
\rightarrow
\text{system transformation}
}
\]

# Canonical governance

1. The seven-stage ordering is authoritative until explicitly changed by the author.
2. Stage 1 distinguishes structural representation from evidence qualification.
3. Stage 2 distinguishes structural dependency from causal mechanism and propagation form.
4. Stage 3 is the physical/interface plant; Stage 4 contains observation, information, organization, estimation, and control.
5. Stage 5 begins from finite-horizon controlled viability and may be extended to robust nonanticipative viability.
6. CARe/HJ is a candidate computational route, not the theoretical definition of viability or signed distance.
7. Sustainability translation is explicit in Stage 6 and does not redefine Stages 1–5.
8. Stage 7 contains candidate transformation pathways; optimization is introduced only when an objective is formally defined.
9. Future literature, data, simulations, and visualizations must map into this architecture rather than silently redefining it.
10. Any substantive change must be recorded as an explicit canonical amendment/version.
