# Physics–Mathematics–Engineering Synthesis for the Fixed Power–Transportation Thesis

**Version:** V1  
**Status:** SUPPORTING METHODOLOGICAL SYNTHESIS — NON-CANONICAL  
**Repository role:** execution support for the existing seven-stage thesis; this file does **not** modify the canonical scope, RQ0–RQ7, SO1–SO7, H1–H5, or the P+T / I+O system boundary.

---

## 0. Governance and claim classes

The thesis scope remains fixed:

$$
\boxed{
P+T=\text{physical core},
\qquad
I+O=\text{supporting domains}
}
$$

and:

$$
\boxed{
\text{Stage 1}\rightarrow\text{Stage 2}\rightarrow\cdots\rightarrow\text{Stage 7}
}
$$

This synthesis only strengthens the mathematical, physical, engineering, validation, and human-centered execution of the already-defined stages.

Claim classes used below:

- **[E]** externally established evidence or method;
- **[D]** thesis derivation/adaptation of established methods;
- **[P]** proposed thesis object or conditional implementation;
- **[A]** declared modeling assumption;
- **[U]** unresolved item requiring evidence or validation.

The governing rule is:

$$
\boxed{
\text{RQ}
\rightarrow
\text{engineering need}
\rightarrow
\text{mathematical object}
\rightarrow
\text{assumptions}
\rightarrow
\text{evidence/data}
\rightarrow
\text{verification}
\rightarrow
\text{validation}
\rightarrow
\text{bounded inference}
}
$$

No method enters merely because it is mathematically sophisticated.

---

# 1. Unified scientific architecture

Multilayer-network theory provides a formal representation of systems with multiple layers and interaction types, but topology alone does not establish a causal infrastructure mechanism (De Domenico et al., 2013; Kivelä et al., 2014). Interdependent-infrastructure reviews likewise show that empirical, network, system-dynamics, agent-based, economic, and other model families serve different purposes rather than forming one universal model (Ouyang, 2014).

The thesis therefore uses the following architecture [D]:

$$
\boxed{
\mathcal G
\rightarrow
\mathfrak D_{\mathrm{qual}}
\rightarrow
\Theta_{\mathrm{id}}
\rightarrow
F_{\mathcal G}
\rightarrow
(y,\widehat Y,\mathcal U_{\mathrm{feas}})
\rightarrow
(\mathcal V,\mathcal R)
\rightarrow
\mathbf C(a)
\rightarrow
\mathcal A^\star
}
$$

with engineering interpretation:

$$
\boxed{
\text{Structure}
\rightarrow
\text{Qualified interdependency}
\rightarrow
\text{Identifiable parameters}
\rightarrow
\text{Coupled dynamics}
\rightarrow
\text{Knowledge and feasible action}
\rightarrow
\text{Resilience}
\rightarrow
\text{Intervention consequences}
\rightarrow
\text{Decision}
}
$$

The central scientific object remains the **directional Power–Transportation interdependency**; physics constrains it, mathematics formalizes it, and engineering tests and acts on it.

---

# 2. Stage 1 — System-of-Systems and multilayer structure

## 2.1 General mathematical representation [E/D]

Let the physical layer graphs be

$$
\mathcal G_P=(V_P,E_P),
\qquad
\mathcal G_T=(V_T,E_T).
$$

The bounded multilayer structure is represented as

$$
\boxed{
\mathcal G=
\left(
\mathcal G_P,
\mathcal G_T,
E_{PT}^{\mathrm{cand}},
E_{TP}^{\mathrm{cand}}
\right)
}
$$

with spatial embedding

$$
\varphi:V_P\cup V_T\rightarrow\mathbb R^2,
\qquad
v_i\mapsto r_i.
$$

A cross-layer structural relation

$$
e_{ij}\in E_{PT}^{\mathrm{cand}}\cup E_{TP}^{\mathrm{cand}}
$$

means only that interaction is structurally admissible.

The thesis preserves [D]:

$$
\boxed{
\text{structural edge}
\neq
\text{qualified dependency}
}
$$

and

$$
\boxed{
\text{co-location/common exposure}
\neq
\text{causal interdependency}.
}
$$

**Use in thesis:** Stage 1 answers what exists, where it exists, which services are provided, and where interaction could occur. It must not infer mechanism or causal direction from graph topology.

---

# 3. Stage 2 — evidence-qualified directional interdependencies

Infrastructure-interdependency research supports explicit treatment of direction, mechanism, context, and operating conditions rather than treating all cross-system relations as interchangeable (Rinaldi et al., 2001; Ouyang, 2014).

## 3.1 General dependency object [D]

For candidate cross-system relation \(e\), define

$$
\boxed{
\mathfrak d_e=
\left(
s_e,
r_e,
M_e,
A_e,
\delta_e,
\tau_e,
\theta_e,
U_e,
E_e,
\Omega_e
\right)
}
$$

where:

- \(s_e\): source;
- \(r_e\): receiver;
- \(M_e\): mechanism;
- \(A_e\): activation condition;
- \(\delta_e\): causal/process delay;
- \(\tau_e\): characteristic timescale;
- \(\theta_e\): mechanism parameters;
- \(U_e\): uncertainty representation;
- \(E_e\): evidence basis;
- \(\Omega_e\): validity domain.

Qualification is represented as

$$
e_{ij}^{\mathrm{cand}}
\xrightarrow[
\text{conditions, uncertainty, validity}
]{
\text{mechanism + direction + evidence}
}
d_{ij}^{\mathrm{qual}}.
$$

The directional firewall is

$$
\boxed{
P\rightarrow T
\not\Rightarrow
T\rightarrow P.
}
$$

## 3.2 Direct P–T mechanism classes [E/D]

Direct coupled traffic–power studies establish that transportation can depend on electric power and that power-system response/restoration can depend on transportation access; however, each mechanism must be separately qualified for the thesis test domain (Fotouhi et al., 2017; Zou & Chen, 2019).

Representative thesis mechanisms are therefore encoded separately [D]:

$$
d_{P\rightarrow T}^{(1)}
=
\text{power availability}
\rightarrow
\text{traffic-signal / charging / traction function},
$$

$$
d_{T\rightarrow P}^{(1)}
=
\text{transport accessibility}
\rightarrow
\text{repair/restoration feasibility},
$$

and, where independently evidenced,

$$
d_{T\rightarrow P}^{(2)}
=
\text{EV charging/V2G behavior}
\rightarrow
\text{power demand/injection}.
$$

These are **mechanism classes**, not universal claims that every mechanism is active in every case.

---

# 4. Stage 2→3 handoff — parameter identification and inverse learning

This section is the principal methodological addition of the present synthesis. It does **not** create an eighth stage. It strengthens the existing Stage 2→3 handoff.

Liu and Yin (2026) formulate transportation-equilibrium model construction as an inverse problem: unknown parameters of a forward equilibrium model are learned from empirical traffic states. Their framework separates three choices: modeling priority, metric selection, and parameterization. They also show that data resolution and noise materially affect identifiability, tractability, and out-of-sample generalization. Aswani et al. (2018) provide a statistical foundation for inverse optimization with noisy observations.

## 4.1 General forward model [E/D]

Let

$$
Y^\star(\theta)
=
\mathcal M(\theta;\xi)
$$

denote the state generated by a forward model under parameters \(\theta\) and exogenous conditions \(\xi\).

Observed data satisfy

$$
\boxed{
y^{\mathrm{obs}}
=
H\!\left(Y^\star(\theta_0)\right)+\varepsilon
}
$$

where \(H\) is the observation operator and \(\varepsilon\) collects measurement error, missingness, and other admitted discrepancies.

## 4.2 General inverse-identification problem [E/D]

A generic inverse problem is

$$
\boxed{
\widehat\theta
=
\arg\min_{\theta\in\Theta}
D\!\left(
H(Y^\star(\theta)),
y^{\mathrm{obs}}
\right)
}
$$

subject to the forward-model consistency requirements.

Following the data-fit versus model-consistency logic emphasized by Liu and Yin (2026), the thesis-adapted constrained form is [D]:

$$
\boxed{
\begin{aligned}
\widehat\theta
&=
\arg\min_{\theta,Y}
D\!\left(H(Y),y^{\mathrm{obs}}\right)\\
\text{s.t.}\quad
&G_{\mathrm{model}}(Y,\theta)\le\varepsilon_{\mathrm{model}},\\
&\theta\in\Theta_{\mathrm{admissible}}.
\end{aligned}
}
$$

For a physics model,

$$
G_{\mathrm{model}}
=
G_{\mathrm{physics}}.
$$

For an equilibrium transportation model,

$$
G_{\mathrm{model}}
=
G_{\mathrm{eq}}.
$$

The key scientific rule is

$$
\boxed{
\text{best historical fit}
\not\Rightarrow
\text{best physical/behavioral model}.
}
$$

## 4.3 Transportation-specific inverse identification [E/D]

Liu and Yin (2026) use a network-equilibrium forward problem. In thesis notation, a transportation model can be written abstractly as

$$
x_T^\star(\theta_T)
=
\operatorname{Eq}_T(\theta_T;\xi_T).
$$

Then

$$
\boxed{
\widehat\theta_T
=
\arg\min_{\theta_T}
D_T
\left(
H_T x_T^\star(\theta_T),
y_T^{\mathrm{obs}}
\right)
}
$$

subject to transportation equilibrium/dynamic-loading consistency.

This provides a defensible route for estimating, where data permit:

- demand parameters;
- link-performance parameters;
- route-choice parameters;
- charging-choice parameters;
- context-dependent traffic parameters.

It must not be used as evidence for \(P\rightarrow T\) or \(T\rightarrow P\).

## 4.4 Coupling-parameter identification [P]

For a qualified interface \(e\),

$$
z_e
=
C_e(x_s,x_r;\theta_e).
$$

The thesis may estimate \(\theta_e\) only where observations sufficiently excite and observe the mechanism:

$$
\boxed{
\widehat\theta_e
=
\arg\min_{\theta_e\in\Theta_e}
D_e
\left(
H_e z_e(\theta_e),
y_e^{\mathrm{obs}}
\right)
}
$$

subject to the already-qualified mechanism structure \(C_e\).

This yields the crucial distinction:

$$
\boxed{
\text{mechanism qualification}
\neq
\text{parameter estimation}.
}
$$

Stage 2 qualifies the mechanism; the Stage 2→3 handoff identifies executable numerical parameters.

## 4.5 Identifiability gate [D]

Structural identifiability requires that distinct parameter values not generate indistinguishable admissible observations:

$$
\boxed{
H\mathcal M(\theta_1)=H\mathcal M(\theta_2)
\;\Rightarrow\;
\theta_1=\theta_2.
}
$$

A local numerical diagnostic may use the sensitivity/Jacobian matrix

$$
J_\theta
=
\frac{\partial H\mathcal M(\theta)}{\partial\theta}.
$$

A necessary local rank condition is

$$
\operatorname{rank}(J_\theta)
=
\dim(\theta)
$$

within the chosen parameterization and experiment. Failure of this condition blocks unique local parameter recovery under that experiment.

The thesis therefore preserves:

$$
\boxed{
\text{parameter availability}
\neq
\text{parameter identifiability}.
}
$$

---

# 5. Stage 3 — physics-based hybrid multiscale dynamics

Zhang and Peeta (2014) demonstrate why infrastructure interdependencies require dynamic and disequilibrium treatment when the research question concerns evolution, cascading failure, recovery, and dynamic allocation. Direct P–T studies likewise use dynamic traffic and power-system models rather than relying only on static adjacency (Fotouhi et al., 2017; Zou & Chen, 2019).

## 5.1 General power-system model [D]

The exact power-model family remains case-dependent, but the general differential-algebraic structure is

$$
\boxed{
M_P\dot x_P
=
f_P(x_P,z_P,u_P,\eta_P;\theta_P)
}
$$

with algebraic constraints

$$
\boxed{
0
=
g_P(x_P,z_P,u_P,\eta_P;\theta_P).
}
$$

Possible states/variables include

$$
x_P
=
[V,\theta,f,P_{ij},Q_{ij},P_G,P_L,SOC_B,\ldots]^\top.
$$

The exact state vector must be selected only after the benchmark/case and solver are frozen.

## 5.2 Transportation conservation and network dynamics [E/D]

A continuum traffic conservation law is

$$
\boxed{
\frac{\partial k(x,t)}{\partial t}
+
\frac{\partial q(x,t)}{\partial x}
=
s(x,t)
}
$$

where \(k\) is density, \(q\) is flow, and \(s\) represents admitted sources/sinks.

For network-level models,

$$
\boxed{
\dot x_T
=
f_T(x_T,z_T,u_T,\eta_T;\theta_T)
}
$$

may summarize dynamic network loading, queues, route/departure choice, and mobility-service states.

## 5.3 EV-energy coupling [D]

For vehicle \(v\),

$$
\boxed{
\dot{SOC}_v
=
-\frac{P_v^{\mathrm{drive}}}{E_v}
+
\eta_c\frac{P_v^{\mathrm{ch}}}{E_v}
-
\frac{P_v^{\mathrm{V2G}}}{\eta_d E_v}.
}
$$

Aggregated charging demand can be represented as

$$
\boxed{
P_{\mathrm{ch}}(t)
=
\sum_{v\in\mathcal V_{\mathrm{EV}}}
\chi_v(t)P_v^{\mathrm{ch}}(t).
}
$$

Thus one admissible \(T\rightarrow P\) coupling is

$$
P_L^{\mathrm{net}}(t)
=
P_L^{\mathrm{base}}(t)
+
P_{\mathrm{ch}}(t)
-
P_{\mathrm{V2G}}(t),
$$

but only where charging/V2G participation is within the declared validity domain.

## 5.4 Directional interface operators [D]

Define separate coupling operators

$$
z_{PT}(t)
=
C_{PT}
\left(
x_P(t-\delta_{PT}),
x_T(t);
\theta_{PT}
\right),
$$

$$
z_{TP}(t)
=
C_{TP}
\left(
x_T(t-\delta_{TP}),
x_P(t);
\theta_{TP}
\right).
$$

The operators are not assumed symmetric:

$$
\boxed{
C_{PT}\neq C_{TP}.
}
$$

## 5.5 Coupled hybrid delayed multirate model [D]

The thesis-level coupled model is

$$
\boxed{
\dot Y_c(t)
=
F^{m(t)}
\left(
Y_c(t),
Y_d(t),
Y(t-\boldsymbol\delta),
u(t),
\eta(r,t);
\theta,
\mathcal G(t)
\right)
}
$$

with discrete reset/event dynamics

$$
\boxed{
Y^+
=
\Psi_{e}^{m\rightarrow m'}
\left(
Y^-,
u,
\eta
\right).
}
$$

The following objects remain distinct:

$$
\boxed{
t_e
\neq
\delta_e
\neq
\tau_e,
}
$$

where \(t_e\) is event time, \(\delta_e\) is causal/process delay, and \(\tau_e\) is characteristic timescale.

## 5.6 Co-simulation architecture [E/D]

HELICS provides an established precedent for federated multi-domain co-simulation in which domain simulators retain their native models and exchange information during synchronized execution (Hardy et al., 2024).

The thesis therefore favors the integration pattern

$$
\boxed{
F_P
\;\xleftrightarrow[\;C_{TP}\;]{\;C_{PT}\;}
F_T
}
$$

with synchronization times

$$
t_0<t_1<\cdots<t_K.
$$

At synchronization time \(t_k\),

$$
z_{PT,k}=C_{PT}(x_P(t_k),x_T(t_k)),
\qquad
z_{TP,k}=C_{TP}(x_T(t_k),x_P(t_k)).
$$

This preserves native subsystem physics instead of forcing P and T into one artificial equation class.

---

# 6. Stage 4 — observation, estimation, organization, and feasible control

Human-factor and organizational resilience research shows that infrastructure response depends not only on physical state but also on information, operators, coordination, available resources, and decision structures (Magoua & Li, 2023; Gomez et al., 2019).

## 6.1 Observation model [E/D]

$$
\boxed{
y_k
=
H_k
\left(
Y(t_k-\delta_k)
\right)
+
\varepsilon_k.
}
$$

Thus

$$
\boxed{
Y
\neq
y
\neq
\widehat Y.
}
$$

## 6.2 State estimation [D]

$$
\boxed{
\widehat Y_k
=
\mathcal E
\left(
y_{0:k},
\mathcal M,
\Pi
\right),
}
$$

where \(\Pi\) contains admitted prior/model information.

A probabilistic implementation, if justified, may use the belief state

$$
b_k(Y)
=
p(Y_k\mid\mathcal I_k).
$$

This is conditional, not mandatory.

## 6.3 Human-centered feasible action [D]

Let the information available to decision agent \(a\) be

$$
\mathcal I_t^{(a)}
=
\{
y_{0:t},
\widehat Y_t,
\text{alerts},
\text{forecasts},
\text{authorized shared information}
\}.
$$

Define feasible actions as

$$
\boxed{
\mathcal U_{\mathrm{feas}}^{(a)}(t)
=
\mathcal U
\left(
\widehat Y_t,
\mathcal I_t^{(a)},
O_t,
R_t,
t
\right),
}
$$

where \(O_t\) denotes organizational/authority constraints and \(R_t\) denotes available resources.

The control policy is

$$
\boxed{
u_t
=
\pi
\left(
\widehat Y_t,
\mathcal I_t^{(a)},
O_t
\right),
\qquad
u_t\in\mathcal U_{\mathrm{feas}}^{(a)}(t).
}
$$

The human-centered interpretation is not a new thesis domain. It requires the model to represent what decision makers **know, are authorized to do, and can physically execute**.

---

# 7. Stage 5 — uncertainty-aware viability and recovery reachability

Doyen and De Lara (2010) formalize stochastic viability for constrained uncertain control systems through chance constraints and dynamic programming. Vinod and Oishi (2021) formulate stochastic target-tube reachability, including stochastic viability and reach-avoid formulations. Maidens et al. (2013) show how reach-set methods can be used to approximate viability kernels in higher-dimensional settings.

## 7.1 Service acceptability set [D]

Let

$$
Q(Y,t)
=
\begin{bmatrix}
Q_P(Y,t)\\
Q_T(Y,t)
\end{bmatrix}
$$

denote electricity and mobility service performance.

Define

$$
\boxed{
K_{\mathrm{sus}}(t)
=
\left\{
Y:
Q_P(Y,t)\ge Q_P^{\mathrm{req}}(t),
\;
Q_T(Y,t)\ge Q_T^{\mathrm{req}}(t),
\;
g_{\mathrm{phys}}(Y)\le0
\right\}.
}
$$

The requirement thresholds must be independently justified; viability theory does not create them.

## 7.2 Deterministic viability [E/D]

$$
\boxed{
\mathcal V_T
=
\left\{
Y_0\in K_{\mathrm{sus}}(0):
\exists u(\cdot)\in\mathcal U_{\mathrm{feas}}
\text{ s.t. }
Y(t)\in K_{\mathrm{sus}}(t)
\;\forall t\in[0,T]
\right\}.
}
$$

Interpretation:

$$
\boxed{
\text{Viability}=\text{Remain}.
}
$$

## 7.3 Stochastic viability [E/D]

For confidence level \(\beta\),

$$
\boxed{
\mathcal V_{\beta,T}
=
\left\{
Y_0:
\sup_{\pi}
\Pr^\pi
\left[
Y(t)\in K_{\mathrm{sus}}(t)
\;\forall t\in[0,T]
\mid Y_0
\right]
\ge\beta
\right\}.
}
$$

## 7.4 Recovery reachability [E/D]

Let \(K_{\mathrm{rec}}(T)\) be the acceptable recovered-service target.

$$
\boxed{
\mathcal R_{\beta,T}
=
\left\{
Y_0:
\sup_{\pi}
\Pr^\pi
\left[
Y(T)\in K_{\mathrm{rec}}(T),
\;
Y(t)\notin K_{\mathrm{avoid}}(t)
\right]
\ge\beta
\right\}.
}
$$

Interpretation:

$$
\boxed{
\text{Reachability}=\text{Return}.
}
$$

The thesis therefore retains

$$
\boxed{
\text{Resilience information}
=
\{\text{Remain},\text{Return},\text{Confidence}\},
}
$$

where the braces denote a set of complementary information objects, not scalar addition.

## 7.5 Conventional resilience comparator [E/D]

Poulin and Kane (2021) show that resilience curves can be represented by a performance measure \(\mathcal P(t)\), while summary metrics map an entire curve to a scalar and different metric choices can communicate different aspects of system behavior.

The thesis therefore retains conventional service trajectories

$$
\mathcal P_P(t),
\qquad
\mathcal P_T(t)
$$

and summary measures

$$
J_{\mathrm{conv}}
=
J(\mathcal P)
$$

as comparators rather than replacing them.

H3 tests whether

$$
\boxed{
\{\mathcal V,\mathcal R\}
\overset{?}{\text{ provide incremental information beyond }}
J_{\mathrm{conv}}.
}
$$

No superiority is assumed.

---

# 8. Uncertainty propagation and sensitivity

## 8.1 Uncertainty object [D]

$$
\boxed{
\mathbf U
=
\{
U_\eta,
U_{\mathbb I},
U_{\mathrm{model}},
U_\theta,
U_{\mathrm{obs}},
U_{\mathrm{int}},
U_{\mathrm{acc}}
\}.
}
$$

Uncertainty must propagate through the scientific chain:

$$
\boxed{
\mathbf U
\rightarrow
Y
\rightarrow
Q
\rightarrow
(\mathcal V,\mathcal R)
\rightarrow
\mathbf C(a)
\rightarrow
\mathcal A^\star.
}
$$

## 8.2 Local parameter sensitivity [D]

For scalar output \(J\),

$$
S_i
=
\frac{\partial J}{\partial\theta_i}.
$$

A dimensionless local elasticity may be

$$
\widetilde S_i
=
\frac{\theta_i}{J}
\frac{\partial J}{\partial\theta_i},
$$

where defined.

## 8.3 Interface-to-viability sensitivity [P]

Only after the viability object and coupling parameter are identifiable, a candidate diagnostic may be defined as

$$
\boxed{
S_{e}^{\mathcal V}
=
\frac{\partial \rho_{\mathcal V}}{\partial\theta_e},
}
$$

where \(\rho_{\mathcal V}\) is a declared viability-margin function.

This remains **proposed/conditional** until the exact margin, differentiability conditions, numerical estimator, uncertainty treatment, and validation test are frozen.

---

# 9. Stage 6 — intervention consequences

Resilience and sustainability should remain distinct evaluation dimensions. Decision-analysis literature demonstrates that infrastructure decisions can trade resilience benefits against resource consumption and environmental consequences (Faber et al., 2020).

For intervention \(a_k\), define the consequence vector [D]:

$$
\boxed{
\mathbf C(a_k)
=
\begin{bmatrix}
\Delta \mathfrak R(a_k)\\
J_{\mathrm{cost}}(a_k)\\
J_{\mathrm{energy}}(a_k)\\
J_{\mathrm{CO_2e}}(a_k)\\
J_{\mathrm{feas}}(a_k)
\end{bmatrix}.
}
$$

The exact admitted sustainability quantities remain governed by independent evidence and the declared accounting boundary.

The thesis preserves

$$
\boxed{
\text{resilience effect}
\neq
\text{effectiveness}
\neq
\text{resource requirement}
\neq
\text{resource efficiency}
\neq
\text{sustainability consequence}.
}
$$

A resource-efficiency measure may be defined, only when numerator and denominator are meaningful, as

$$
\eta_R(a_k)
=
\frac{\Delta\mathfrak R(a_k)}
{J_{\mathrm{resource}}(a_k)}.
$$

This ratio is not a universal resilience metric.

---

# 10. Stage 7 — defensible engineering decision

## 10.1 Feasible alternative set [D]

$$
\mathcal A_{\mathrm{feas}}
=
\{
a:
g_j(a)\le0,\;j=1,\ldots,m
\}.
$$

## 10.2 Pareto/nondominated set [E/D]

Let

$$
\mathbf J(a)
=
[J_1(a),\ldots,J_p(a)]^\top.
$$

Then

$$
\boxed{
\mathcal A^\star
=
\left\{
a\in\mathcal A_{\mathrm{feas}}:
\nexists a'\in\mathcal A_{\mathrm{feas}}
\text{ such that }
a'\prec a
\right\}.
}
$$

Native-unit criteria should be inspected before any preference-weighted scalarization.

## 10.3 Decision regret under uncertainty [D]

For scenario \(\omega\),

$$
\operatorname{Regret}(a,\omega)
=
J(a,\omega)
-
\min_{a'\in\mathcal A_{\mathrm{feas}}}J(a',\omega).
$$

A robust-regret criterion is

$$
\boxed{
R_{\max}(a)
=
\sup_{\omega\in\Omega}
\operatorname{Regret}(a,\omega).
}
$$

This is admissible only when the scalar objective \(J\) and uncertainty set \(\Omega\) are independently justified.

## 10.4 Adaptive pathways [P]

Dynamic Adaptive Policy Pathways provide a precedent for sequences of actions, triggers, adaptation points, and path dependence under deep uncertainty (Haasnoot et al., 2013).

The thesis should activate sequential/pathway optimization only if temporal decision structure, data, and validation are sufficient.

---

# 11. VVUQ and model credibility

ASME distinguishes verification, validation, and uncertainty quantification: verification assesses whether the computational model implements the mathematical description correctly; validation assesses agreement with the intended real-world application; uncertainty quantification evaluates how numerical and physical uncertainties affect outputs. NASA-STD-7009B similarly treats modeling-and-simulation credibility as a lifecycle concern with project-specific acceptance criteria.

The thesis therefore uses separate gates.

## 11.1 Code/equation verification [D]

For a discretized governing equation,

$$
R_h
=
\mathcal L_h(Y_h)-b_h.
$$

Require

$$
\|R_h\|
\le
\varepsilon_{\mathrm{num}}
$$

for declared numerical tolerances and conduct convergence checks where applicable.

## 11.2 Dimensional consistency [D]

Every governing equation must satisfy

$$
\boxed{
[\mathrm{LHS}]
=
[\mathrm{RHS}].
}
$$

## 11.3 Limiting-case verification [D]

Examples:

$$
\theta_{PT},\theta_{TP}\rightarrow0
\quad\Rightarrow\quad
M_2\rightarrow M_0
$$

where appropriate, and

$$
\varepsilon_{\mathrm{obs}}\rightarrow0,
\quad
\delta_{\mathrm{obs}}\rightarrow0
$$

should approach the perfect-information baseline.

## 11.4 Calibration error [D]

For observations \(y_i\) and predictions \(\widehat y_i\),

$$
\operatorname{RMSE}
=
\sqrt{
\frac{1}{N}
\sum_{i=1}^{N}
(\widehat y_i-y_i)^2
}.
$$

Calibration fit is necessary evidence, but not sufficient validation.

## 11.5 Out-of-sample generalization [E/D]

Liu and Yin (2026) emphasize evaluation under unseen conditions and show, in their numerical study, substantial differences between inverse formulations under noise and distribution shift.

The thesis validation set should include, where supported:

$$
\boxed{
\begin{aligned}
&\text{unseen demand},\\
&\text{unseen hazard realization},\\
&\text{altered operating state},\\
&\text{changed topology},\\
&\text{different coupling activation},\\
&\text{intervention counterfactual}.
\end{aligned}
}
$$

Define the generalization gap for metric \(L\) as

$$
\boxed{
\Delta_{\mathrm{gen}}
=
L_{\mathrm{test}}
-
L_{\mathrm{train}}.
}
$$

## 11.6 Decision-relevance validation [D/P]

Because the model is ultimately used for engineering decisions, model evaluation should not end at prediction error.

A candidate decision-stability diagnostic is

$$
\Delta_{\mathrm{dec}}
=
d_{\mathcal A}
\left(
\mathcal A^\star_{\mathrm{reference}},
\mathcal A^\star_{\mathrm{model}}
\right),
$$

where \(d_{\mathcal A}\) is a declared set-distance or decision-disagreement measure.

This is proposed and requires preregistration before confirmatory use.

## 11.7 Validation hierarchy [D]

$$
\boxed{
\begin{aligned}
G_1 &: \text{mathematical / physical correctness},\\
G_2 &: \text{parameter identifiability},\\
G_3 &: \text{calibration fit},\\
G_4 &: \text{out-of-sample generalization},\\
G_5 &: \text{counterfactual / intervention sensitivity},\\
G_6 &: \text{downstream decision stability}.
\end{aligned}
}
$$

Passing a lower gate does not imply passing a higher gate.

---

# 12. Comparative model hierarchy for H1

The thesis retains the controlled model hierarchy

$$
M_0
=
\text{independent P and T},
$$

$$
M_1
=
\text{static qualified coupling},
$$

$$
M_2
=
\text{dynamic qualified coupling}.
$$

The confirmatory question is

$$
\boxed{
M_2
\overset{?}{>}
M_1,
}
$$

with \(M_0\) as reference.

Matched comparison requires

$$
Y_0^{(0)}=Y_0^{(1)}=Y_0^{(2)},
$$

$$
\eta^{(0)}=\eta^{(1)}=\eta^{(2)},
$$

$$
K_{\mathrm{sus}}^{(0)}
=
K_{\mathrm{sus}}^{(1)}
=
K_{\mathrm{sus}}^{(2)},
$$

and all non-tested exogenous conditions held fixed as far as scientifically possible.

The result is not assumed. If the evidence or prerequisites are insufficient, the correct status is **NOT TESTED**.

---

# 13. Human-centered interpretation across the seven stages

Human-centered design is not introduced as a new thesis domain. It is a constraint on how the existing framework represents service, information, feasible action, and decision consequences.

The governing questions are [D]:

$$
\boxed{
\begin{array}{ll}
1.&\text{Who is the decision agent?}\\
2.&\text{What can that agent observe?}\\
3.&\text{What uncertainty remains?}\\
4.&\text{What actions are authorized and physically feasible?}\\
5.&\text{Which electricity and mobility services must be protected?}\\
6.&\text{Which resource and sustainability consequences matter?}\\
7.&\text{How stable is the decision under uncertainty?}
\end{array}
}
$$

This prevents a mathematically optimal but operationally impossible action from being labeled an engineering solution.

---

# 14. What this synthesis changes — and does not change

## 14.1 Changes to execution rigor

This synthesis explicitly adds to execution:

1. a **parameter-identification/identifiability gate** within the existing Stage 2→3 handoff;
2. a data-fit versus model-consistency distinction;
3. out-of-sample and counterfactual validation;
4. decision-relevance validation;
5. explicit propagation from parameter uncertainty to resilience and decision outputs;
6. a clearer human-centered interpretation of feasible control.

## 14.2 No changes to canonical scientific scope

This synthesis does **not**:

- add an eighth stage;
- alter RQ0–RQ7;
- alter SO1–SO7;
- alter H1–H5;
- add a new infrastructure sector;
- make AI/ML mandatory;
- make geometry mandatory;
- claim that inverse learning establishes causal interdependency;
- claim that a validated transportation model validates the full coupled P–T framework.

The central scope remains

$$
\boxed{
\text{Power–Transportation interdependencies for resilience}
}
$$

implemented through the existing evidence-to-decision chain.

---

# 15. Next-work execution rule

For each executable Stage-3 parameter or coupling law, create one parameter-evidence record:

$$
\boxed{
\theta
\mapsto
\{
\text{meaning},
\text{units},
\text{equation},
\text{source},
\text{data},
\text{identifiability},
\text{estimate},
\text{uncertainty},
\text{validation},
\text{validity domain}
\}.
}
$$

Then apply:

$$
\boxed{
\text{qualified mechanism}
\rightarrow
\text{identifiable parameterization}
\rightarrow
\text{estimated parameter}
\rightarrow
\text{verified dynamics}
\rightarrow
\text{out-of-sample validation}
\rightarrow
\text{uncertainty propagation}
\rightarrow
\text{resilience}
\rightarrow
\text{decision}.
}
$$

This is the default mathematical-scientific handoff for subsequent thesis work.

---

# References

Aswani, A., Shen, Z.-J., & Siddiq, A. (2018). Inverse optimization with noisy data. *Operations Research, 66*(3), 870–892. https://doi.org/10.1287/opre.2017.1705

De Domenico, M., Solé-Ribalta, A., Cozzo, E., Kivelä, M., Moreno, Y., Porter, M. A., Gómez, S., & Arenas, A. (2013). Mathematical formulation of multilayer networks. *Physical Review X, 3*, 041022. https://doi.org/10.1103/PhysRevX.3.041022

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008

Faber, M. H., Miraglia, S., Qin, J., & Stewart, M. G. (2020). Bridging resilience and sustainability—Decision analysis for design and management of infrastructure systems. *Sustainable and Resilient Infrastructure, 5*(1–2), 102–124. https://doi.org/10.1080/23789689.2017.1417348

Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety, 163*, 79–94. https://doi.org/10.1016/j.ress.2017.01.026

Gomez, C., González, A. D., Baroud, H., & Bedoya-Motta, C. D. (2019). Integrating operational and organizational aspects in interdependent infrastructure network recovery. *Risk Analysis, 39*(9), 1913–1929. https://doi.org/10.1111/risa.13340

Haasnoot, M., Kwakkel, J. H., Walker, W. E., & ter Maat, J. (2013). Dynamic adaptive policy pathways: A method for crafting robust decisions for a deeply uncertain world. *Global Environmental Change, 23*(2), 485–498. https://doi.org/10.1016/j.gloenvcha.2012.12.006

Hardy, T. D., Palmintier, B., Top, P., Krishnamurthy, D., & Fuller, J. C. (2024). HELICS: A co-simulation framework for scalable multi-domain modeling and analysis. *IEEE Access, 12*, 24325–24347. https://doi.org/10.1109/ACCESS.2024.3363615

Karniadakis, G. E., Kevrekidis, I. G., Lu, L., Perdikaris, P., Wang, S., & Yang, L. (2021). Physics-informed machine learning. *Nature Reviews Physics, 3*, 422–440. https://doi.org/10.1038/s42254-021-00314-5

Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks, 2*(3), 203–271. https://doi.org/10.1093/comnet/cnu016

Liu, Z., & Yin, Y. (2025). End-to-end learning of user equilibrium: Expressivity, generalization, and optimization. *Transportation Science, 59*(4), 853–882. https://doi.org/10.1287/trsc.2023.0489

Liu, Z., & Yin, Y. (2026). Constructing transportation network equilibrium models from empirical data: An inverse learning perspective. *Transportation Research Part B: Methodological, 214*, 103597. https://doi.org/10.1016/j.trb.2026.103597

Magoua, J. J., & Li, N. (2023). The human factor in the disaster resilience modeling of critical infrastructure systems. *Reliability Engineering & System Safety, 232*, 109073. https://doi.org/10.1016/j.ress.2022.109073

Maidens, J. N., Kaynama, S., Mitchell, I. M., Oishi, M. M. K., & Dumont, G. A. (2013). Lagrangian methods for approximating the viability kernel in high-dimensional systems. *Automatica, 49*(7), 2017–2029. https://doi.org/10.1016/j.automatica.2013.03.020

Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040

Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926

Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458

Zhang, P., & Peeta, S. (2014). Dynamic and disequilibrium analysis of interdependent infrastructure systems. *Transportation Research Part B: Methodological, 67*, 357–381. https://doi.org/10.1016/j.trb.2014.04.008

Zou, Q., & Chen, S. (2019). Enhancing resilience of interdependent traffic-electric power system. *Reliability Engineering & System Safety, 191*, 106557. https://doi.org/10.1016/j.ress.2019.106557

ASME. (2025–2026). *Verification, Validation and Uncertainty Quantification (VVUQ) standards portfolio*. https://www.asme.org/codes-standards/vvuq-standards

NASA. (2024). *NASA-STD-7009B: Standard for Models and Simulations*. https://standards.nasa.gov/node/263
