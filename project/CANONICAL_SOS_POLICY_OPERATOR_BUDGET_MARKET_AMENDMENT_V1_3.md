# Canonical SoS Policy–Operator–Budget–Market Amendment v1.3 — NEXTRANS Alignment

**Status:** CANONICAL ADDITIVE AMENDMENT TO P1.11  
**Effective date:** 2026-09-19  
**Parent authority:** \`project/CANONICAL_SPATIOTEMPORAL_SOS_RESILIENCE_TRANSFORMATION_LENS_V1.md\`  
**Prior refinements:** P1.11.1 Pant spatial-risk/pathway; P1.11.2 Barr information architecture/provenance  
**Evidence role:** Peters et al. (2014), NEXTRANS integrated Transportation–Energy policy framework  
**Seven-stage architecture:** UNCHANGED  
**RQ1–RQ7 / SO1–SO7 / H1–H5:** UNCHANGED  
**Empirical effect:** NONE

## 1. Scientific decision

Power–Transportation interdependency is not restricted to direct physical network coupling.

The thesis shall distinguish at least:

~~~math
\boxed{
\text{physical/functional channels}
\neq
\text{organizational/authority channels}
\neq
\text{budget/resource channels}
\neq
\text{market/economic channels}
\neq
\text{public-policy instruments}.
}
~~~

These may interact, but they are not interchangeable scientific objects.

A complete cross-scale causal chain may therefore include:

~~~math
\boxed{
\text{policy/action}
\rightarrow
\text{behavior/demand}
\rightarrow
\text{physical network use}
\rightarrow
\text{service/performance}
\rightarrow
\text{budget/market consequence}
\rightarrow
\text{operator/investment decision}
\rightarrow
\text{transformed infrastructure}.
}
~~~

This is a conceptual system-of-systems feedback chain. Each arrow requires its own evidence, model and validity domain before empirical use.

## 2. Four interacting system views

For thesis interpretation, distinguish:

~~~math
\boxed{
\begin{aligned}
\mathscr S_{\rm phys}&=(P,T,\mathbb I_{\rm phys/func}),\\
\mathscr S_{\rm svc}&=(Q_P,Q_T),\\
\mathscr S_{\rm op}&=(\mathfrak O,\mathcal U_{\rm feas},\mathcal A_{\rm feas}),\\
\mathscr S_{\rm econ/pol}&=(B,M,\mathcal P^{pol}).
\end{aligned}
}
~~~

where:
- \(B\): budget/resource states where relevant;
- \(M\): market/economic states where relevant;
- \(\mathcal P^{pol}\): public-policy/instrument context where relevant.

Permanent:

~~~math
\boxed{
\text{physical network}
\neq
\text{service provider/operator}
\neq
\text{market actor}
\neq
\text{public authority}.
}
~~~

No actor type is inferred solely from a physical asset.

## 3. Operator and authority remain first-class Stage-4 objects

Existing Stage-4 organizational authority remains:

~~~math
\mathfrak O=(V_O,E_O,A_O,R_O,\tau_O,\Xi_O)
~~~

with dynamic organizational state \(z_O(t)\).

The operational feasible-control set remains:

~~~math
\boxed{
\mathcal U_{\rm feas}(t)
=
\mathcal U_{\rm phys}(t)
\cap
\mathcal U_{\rm info}(t)
\cap
\mathcal U_{\rm org}(t)
\cap
\mathcal U_{\rm resource}(t).
}
~~~

Budget constraints may enter \(\mathcal U_{\rm resource}\) when they actually restrict operational action.

For strategic interventions, a separate feasible action set shall be used where needed:

~~~math
\boxed{
\mathcal A_{\rm feas}^{strat}
=
\mathcal A_{\rm technical}
\cap
\mathcal A_{\rm authority}
\cap
\mathcal A_{\rm budget}
\cap
\mathcal A_{\rm implementation}.
}
~~~

Permanent:

~~~math
\boxed{
u(t)\neq a_k.
}
~~~

Operational control and strategic/public-policy intervention remain different object classes.

## 4. Operational policy versus public policy

Stage-4 operational policy remains the nonanticipative control law:

~~~math
u_t=\pi_t(b_t,z_I,z_O),\qquad \pi\in\Pi^{NA}.
~~~

To avoid notation collision, public-policy instruments shall not use \(\Pi\), because \(\Pi_e\) already denotes dependency provenance and \(\Pi^{NA}\) denotes the operational-policy class.

Use, where needed:

~~~math
\boxed{
p_k^{pol}\in\mathcal P^{pol}.
}
~~~

Permanent:

~~~math
\boxed{
\text{operational control policy }\pi_t
\neq
\text{public-policy instrument }p_k^{pol}.
}
~~~

## 5. Mechanism/channel classification

A candidate cross-sector relation shall declare its interaction channel(s), for example:

~~~text
PHYSICAL
FUNCTIONAL
GEOGRAPHIC_COMMON_CAUSE
INFORMATION
ORGANIZATIONAL_AUTHORITY
BUDGET_RESOURCE
MARKET_ECONOMIC
PUBLIC_POLICY_INDUCED
OTHER
~~~

This channel classification is metadata/evidence organization. It does not replace the canonical dependency primitive:

~~~math
\boxed{
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e).
}
~~~

Where a budget/market/policy channel is modeled causally, it requires its own source, receiver, mechanism, variables, units, timescale, uncertainty and validity domain.

## 6. Native physical/economic units are preserved

Permanent:

~~~math
\boxed{
\text{kW}
\neq
\text{vehicles/hour}
\neq
\text{minutes}
\neq
\text{currency}
\neq
\text{kg CO}_2.
}
~~~

Different mechanisms retain native physical/economic meaning and units.

No universal coupling-cost scalar may be introduced merely to make unlike systems comparable.

Aggregation/normalization belongs downstream and must satisfy Stage-7 value/normalization provenance and sensitivity controls.

## 7. Network topology, capacity and flow

Multilayer network structure is prior art and is not itself a thesis novelty claim.

The thesis shall preserve:

~~~math
\boxed{
\text{topology}
\neq
\text{capacity}
\neq
\text{flow}
\neq
\text{service}.
}
~~~

For a network element \(e\), quantities such as capacity \(c_e(t)\), flow \(q_e(t)\), travel/transfer time \(\tau_e(t)\), and availability \(a_e(t)\) may be required by the relevant mechanism.

The scientific contribution begins beyond multilayer representation: qualification of mechanism, dynamic compilation, service/resilience consequence and intervention analysis.

## 8. Policy-induced interdependency

A policy can change cross-sector interdependency indirectly:

~~~math
\boxed{
p_k^{pol}
\rightarrow
\text{technology/behavior adoption}
\rightarrow
\text{demand}
\rightarrow
\text{network state/use}
\rightarrow
\text{cross-sector consequence}.
}
~~~

It may also alter future structure:

~~~math
\boxed{
p_k^{pol}
\rightarrow
\text{investment/resource allocation}
\rightarrow
\Delta\mathcal G,\Delta\Theta,\Delta\mathbb I,\Delta\mathcal U_{\rm feas}.
}
~~~

A public-policy effect is not assumed causal merely because a scenario changes two variables together.

## 9. EV coupling is mechanism-specific

No single generic “EV dependency” is admissible.

Possible distinct mechanisms include, when evidence supports them:

~~~text
EV charging demand -> power load
charging control/pricing -> temporal load shift
V2G -> power flexibility/support
EV adoption -> fuel demand change
fuel demand change -> transport/logistics change
fuel-tax/revenue change -> road-maintenance budget
grid mix/capacity -> transport electrification consequence
charging infrastructure investment -> network transformation
~~~

Each mechanism must have separate qualification/status.

## 10. Temporal interdependency and pricing

Where pricing/control changes demand timing, the coupling is explicitly time-dependent:

~~~math
\Phi_e
=
\Phi_e(\mathbf r,t,x_P,x_T,m_e,u,\theta_e)
~~~

when that form is scientifically justified.

However, time-dependent economic response is not automatically part of Stage 3.

It enters Stage 3 only if:
1. it materially affects the declared dynamic QOI;
2. its mechanism is evidence-qualified and Stage2→3 ready;
3. its timescale is compatible with the modeled horizon;
4. its parameters/uncertainty are defensible.

Otherwise it remains an exogenous scenario, Stage-6 consequence, or Stage-7 transformation/context variable.

## 11. Equilibrium versus trajectory firewall

Permanent:

~~~math
\boxed{
Y^\ast
\neq
Y(t).
}
~~~

and:

~~~math
\boxed{
\text{general/economic equilibrium}
\neq
\text{hybrid dynamic trajectory}.
}
~~~

An equilibrium model may estimate a post-change system state under its assumptions.

Stage 3 asks how the physical coupled system evolves through disturbance, modes, feedback, controls and recovery.

Neither object may be substituted for the other.

## 12. Multiscale allocation

The established conceptual separation remains:

~~~math
\boxed{
\tau_{\rm op}
\ll
\tau_{\rm rec}
\ll
\tau_{\rm trans}.
}
~~~

Typical allocation:

~~~text
OPERATIONAL:
power loading, charging, traffic flow, signal/control response

RECOVERY:
damage, crew access, restoration, backlog

TRANSFORMATION:
technology adoption, investment, budgets, market response, public policy, capacity expansion
~~~

This is a default interpretation, not a prohibition: a mechanism is allocated by its actual timescale and QOI.

## 13. Multiple decision-makers and objectives

A System of Systems may have actors with different objective functions:

~~~math
J_P\neq J_T\neq J_G
~~~

where applicable.

Examples of objective classes include reliability, operating cost, mobility, accessibility, congestion, budget, emissions, equity and resilience.

Permanent:

~~~math
\boxed{
\text{different actor objectives}
\not\Rightarrow
\text{one common scalar utility}.
}
~~~

Actor objectives must remain separate from scientific evidence and from stakeholder weights unless an explicit Stage-7 value model exists.

## 14. Effectiveness under a coupled-system target

Effectiveness is always evaluated against the preregistered target.

If the declared target is coupled-system performance, then local improvement alone is insufficient:

~~~math
\boxed{
\mathcal E_{\rm fx}(a)
=
\mathcal F_{\rm fx}
(\text{declared coupled-system outcomes},\mathbf T_{\rm fx}).
}
~~~

This does not mean every intervention must optimize every system outcome. It means the scope of the effectiveness conclusion cannot exceed the scope of its target/QOIs.

## 15. Efficiency and opportunity/resource use

Efficiency remains separate from effectiveness and may include, where evidence and accounting boundaries support them:

~~~text
capital
time
energy
crew-hours
capacity
materials
opportunity cost
other registered resource quantities
~~~

Permanent:

~~~math
\boxed{
\text{least financial cost}
\neq
\text{highest engineering efficiency}
}
~~~

unless the declared resource/accounting boundary defines efficiency solely by financial cost.

## 16. Sustainability remains vectorial and cross-sector

The sustainability consequence object remains:

~~~math
\boxed{
\mathbf J_{\rm sus}
=
[J_{\rm access},J_{\rm energy},J_{\rm carbon},J_{\rm cost},\ldots]^\top
}
~~~

for evidence-supported dimensions.

Budget/market outcomes may be reported separately unless they are explicitly part of a sustainability metric or requirement.

No economic variable becomes a sustainability requirement without P1.8 provenance/authority.

## 17. Transformation feedback

A slow transformation transition may be represented conceptually as:

~~~math
\boxed{
\mathcal S^{(k+1)}
=
\Psi_{\rm trans}
\left(
\mathcal S^{(k)},
a_k,
p_k^{pol},
Y_k,
\mathbf J_k,
B_k,
M_k,
z_{O,k}
\right)
}
~~~

where included variables are used only if the case/evidence supports them.

This is a thesis synthesis, not an equation asserted by NEXTRANS.

The transformation mapping may change:

~~~math
\mathcal G,\quad
\Theta,\quad
\mathbb I,\quad
\mathcal U_{\rm feas},\quad
\mathcal A_{\rm feas}^{strat}.
~~~

## 18. Validation firewall

The NEXTRANS report itself identifies empirical/calibration/computational limitations.

Therefore:

~~~math
\boxed{
\text{integrated conceptual framework}
\neq
\text{validated executable model}.
}
~~~

Policy, market, budget or elasticity channels remain BLOCKED/DEFERRED until data, calibration and validation requirements are satisfied for the intended use.

## 19. P2 mandatory audit additions

P2 shall add:

~~~text
INTERACTION_CHANNEL_CLASS
PHYSICAL_VS_POLICY_ECONOMIC_CHANNEL
OPERATOR_ACTOR_ID
AUTHORITY_SCOPE
OPERATIONAL_VS_STRATEGIC_ACTION
PUBLIC_POLICY_INSTRUMENT
BUDGET_RESOURCE_LINK
MARKET_ECONOMIC_LINK
NATIVE_UNIT_PRESERVATION
CAPACITY_FLOW_STATE
TIMESCALE_CLASS
EQUILIBRIUM_VS_TRAJECTORY
COUPLED_EFFECTIVENESS_SCOPE
OPPORTUNITY_COST_STATUS
ACTOR_OBJECTIVE_STATUS
TRANSFORMATION_FEEDBACK
POLICY_ECONOMIC_VALIDATION_STATUS
~~~

Each applicable item is PASS / BLOCKED / DEFERRED / N/A with rationale and provenance.

## 20. Empirical firewall

~~~math
\boxed{
G_{P1.11.3}^{design}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~

No policy effect, elasticity, market response, budget value, operator objective, intervention result or hypothesis outcome is established by this amendment.
