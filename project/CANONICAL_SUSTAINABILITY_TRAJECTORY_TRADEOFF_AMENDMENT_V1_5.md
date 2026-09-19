# Canonical Sustainability Trajectory, Accounting, and Trade-off Amendment v1.5 — Kays & Sadri Alignment

**Status:** CANONICAL ADDITIVE AMENDMENT TO P1.11  
**Effective date:** 2026-09-19  
**Parent authority:** \`project/CANONICAL_SPATIOTEMPORAL_SOS_RESILIENCE_TRANSFORMATION_LENS_V1.md\`  
**Primary stage owners:** Stage 6 sustainability consequences; Stage 7 trade-off/decision; conditional Stage-5 constraint extension only when P1.8 requirements qualify  
**Evidence role:** Kays & Sadri sustainability–resilience conceptual framework  
**Seven-stage architecture:** UNCHANGED  
**RQ1–RQ7 / SO1–SO7 / H1–H5:** UNCHANGED  
**Empirical effect:** NONE

## 1. Permanent separation

~~~math
\boxed{
\text{Sustainability}
\neq
\text{Resilience}
\neq
\text{Effectiveness}
\neq
\text{Efficiency}
\neq
\text{Preference}.
}
~~~

Resilience remains the Stage-5 remain/return/confidence capability.

Sustainability remains a Stage-6/7 consequence family over declared environmental, resource, economic and social accounting boundaries.

No scalar sustainability–resilience index is canonical.

## 2. Candidate variables are not automatically sustainability endpoints

The following may be relevant but have different ontological roles:

~~~text
temperature      -> hazard/context
speed            -> transport state/performance
delay            -> transport performance/service consequence
mobility         -> transport service
accessibility    -> service + candidate social-sustainability endpoint
energy use       -> resource/environmental consequence
GHG emissions    -> environmental consequence
cost             -> economic/resource consequence
~~~

Permanent:

~~~math
\boxed{
\text{driver}
\neq
\text{state}
\neq
\text{service}
\neq
\text{performance metric}
\neq
\text{sustainability endpoint}.
}
~~~

A source's conceptual indicator list does not become the thesis's mandatory objective set without case/evidence qualification.

## 3. Core sustainability consequence vector

The existing Stage-6 core remains:

~~~math
\boxed{
\mathbf J_{\rm sus}^{core}
=
\begin{bmatrix}
J_{\rm access}\\
J_{\rm energy}\\
J_{\rm carbon}\\
J_{\rm cost}
\end{bmatrix}.
}
~~~

Interpretation:
- \(J_{\rm access}\): accessibility/social-service consequence;
- \(J_{\rm energy}\): energy/resource consequence;
- \(J_{\rm carbon}\): GHG/carbon consequence;
- \(J_{\rm cost}\): economic/resource consequence.

Additional dimensions require qualified causal linkage, accounting boundary, data, units and uncertainty.

No scalar score is required.

## 4. Accessibility versus mobility

Permanent:

~~~math
\boxed{
\text{mobility}
\neq
\text{accessibility}.
}
~~~

Mobility concerns movement.

Accessibility concerns the ability to reach opportunities/services.

A candidate accumulated accessibility-loss quantity is:

~~~math
J_{\rm access}
=
\int_{t_0}^{t_f}
L_A(t)\,dt,
~~~

with, where supported,

~~~math
L_A(t)
=
\sum_g w_g
\left[
A_g^{ref}(t)-A_g(t)
\right]_+.
~~~

Population/group weights, reference levels and spatial units require provenance and cannot be invented.

## 5. Spatiotemporal sustainability accounting

For consequence dimension \(j\), a generic continuous representation is:

~~~math
\boxed{
J_j
=
\int_{t_0}^{t_f}
\int_{\Omega}
\ell_j
\left(
\mathbf r,t,
Y^{phys},
Q,
u,
\eta,
a_k
\right)
\,d\mu(\mathbf r)\,dt
+
J_j^{emb}.
}
~~~

where:
- \(\Omega\): declared spatial accounting domain;
- \([t_0,t_f]\): declared accounting horizon;
- \(\ell_j\): local consequence rate;
- \(d\mu\): appropriate spatial/population/network measure;
- \(J_j^{emb}\): qualified one-time/embodied consequence where applicable.

For discrete infrastructure, the spatial integral is implemented as a sum over registered assets, links, zones or population groups.

Permanent:

~~~math
\boxed{
\text{same total consequence}
\not\Rightarrow
\text{same spatial/temporal distribution}.
}
~~~

## 6. Trajectory dependence and accounting states

Many sustainability quantities are accumulated over trajectories.

Define accounting states where useful:

~~~math
\boxed{
\dot b_j(t)=L_j(t),
\qquad
b_j(t_0)=b_{j,0}.
}
~~~

For example:

~~~math
\dot b_C=L_C(t),\qquad
\dot b_E=L_E(t),\qquad
\dot b_{\rm cost}=L_{\rm cost}(t).
~~~

Define an augmented **analysis/accounting state**:

~~~math
\boxed{
\bar Y^{acct}
=
\left(
Y^{phys},
b_C,
b_E,
b_{\rm cost},
\ldots
\right).
}
~~~

Permanent firewall:

~~~math
\boxed{
Y^{phys}
\neq
\bar Y^{acct}.
}
~~~

Accounting-state augmentation does not redefine carbon, cost or cumulative energy as physical infrastructure states.

## 7. Sustainability metric versus sustainability requirement

This amendment explicitly inherits P1.8:

~~~math
\boxed{
\text{sustainability metric}
\neq
\text{sustainability requirement}.
}
~~~

A measured or computed \(J_j\) does not create a hard bound \(B_j\).

A bound may constrain admissibility only when linked to a qualified requirement record:

~~~math
RID_j
\rightarrow
\text{formal criterion}
\rightarrow
B_j(t)
\rightarrow
K(t).
~~~

Without that trace, the bound is BLOCKED for hard viability use and the quantity remains REPORT_ONLY / OBJECTIVE / SOFT_TARGET according to its registered status.

## 8. Conditional sustainable-viability extension

The canonical Stage-5 acceptability set remains:

~~~math
K(t)
=
\{
Y:
h_r(Y,t)\le 0,\ r\in\mathcal R_{\rm qualified}
\}.
~~~

A sustainability-constrained extension is admissible only when qualified hard sustainability/resource requirements exist.

Then define, on the augmented state space:

~~~math
\boxed{
K_{\rm sus}(t)
=
\left\{
\bar Y^{acct}:
\begin{array}{l}
h_r(Y^{phys},t)\le 0,\ r\in\mathcal R_{\rm service/safety},\\
b_j(t)\le B_j(t),\ j\in\mathcal R_{\rm sus}^{hard}
\end{array}
\right\}.
}
~~~

and only then:

~~~math
\boxed{
\mathcal V_{\rm sus}
=
\left\{
\bar Y_0:
\exists\pi\in\Pi^{NA},
\ \bar Y(t)\in K_{\rm sus}(t)
\right\}.
}
~~~

This is a **conditional extension**, not the default Stage-5 resilience object.

Permanent:

~~~math
\boxed{
\mathbf J_{\rm sus}\ \text{available}
\not\Rightarrow
K_{\rm sus}\ \text{authorized}.
}
~~~

## 9. Resilience–sustainability trade-offs

For intervention parameter \(q\), local opposing marginal effects may indicate a trade-off region:

~~~math
\frac{\partial R}{\partial q}
\frac{\partial S_j}{\partial q}
<0,
~~~

only when derivatives are mathematically meaningful.

For nonsmooth/discrete cases, use finite intervention contrasts instead:

~~~math
\Delta\mathfrak R(a_k),
\qquad
\Delta J_j(a_k).
~~~

The source's conceptual tipping points are not treated as calibrated thresholds.

Permanent:

~~~math
\boxed{
\text{conceptual tipping point}
\neq
\text{identified engineering threshold}.
}
~~~

## 10. Pareto before preference

For qualified interventions:

~~~math
\boxed{
\mathcal O(a_k)
=
\left(
\Delta\mathfrak R_k,
\mathcal E_{{\rm fx},k},
\mathcal E_{{\rm fy},k},
\Delta\mathbf J_{{\rm sus},k}
\right).
}
~~~

Stage 7 retains:

~~~math
\boxed{
\text{feasibility}
\rightarrow
\text{native-unit objectives}
\rightarrow
\text{Pareto/dominance}
\rightarrow
\text{robustness/regret}
\rightarrow
\text{preference, if justified}.
}
~~~

No weighted sustainability–resilience score is required.

## 11. Coupled-system accounting boundary

Every sustainability result must declare:

~~~math
\boxed{
\mathcal B_{\rm sus}
=
(
\Omega,
\mathcal T,
\mathcal S_{\rm included},
\mathcal P_{\rm included},
FU,
perspective
).
}
~~~

where:
- \(\Omega\): spatial boundary;
- \(\mathcal T\): time/lifecycle horizon;
- \(\mathcal S_{\rm included}\): systems included;
- \(\mathcal P_{\rm included}\): processes/lifecycle stages included;
- \(FU\): functional unit/reference service;
- perspective: cost/social accounting perspective where applicable.

Permanent:

~~~math
\boxed{
\text{local sector improvement}
\not\Rightarrow
\text{coupled-SoS sustainability improvement}.
}
~~~

For electrification, tailpipe reductions cannot be treated as total SoS carbon benefit unless relevant electricity-generation and infrastructure consequences are included or explicitly excluded with limitation.

## 12. Efficiency versus sustainability cost

The same cost data may appear in different objects for different questions.

~~~math
\boxed{
J_{\rm cost}
\neq
\mathcal E_{\rm fy}.
}
~~~

\(J_{\rm cost}\) is an economic consequence over a declared accounting boundary.

\(\mathcal E_{\rm fy}\) relates achieved engineering effect to resource use.

Double counting is prohibited.

## 13. Shared quantity, different scientific role

A quantity such as accessibility may enter:
1. service acceptability/resilience;
2. Stage-6 social consequence accounting.

The same raw trajectory may support both, but the definitions, aggregation, thresholds and claim roles must remain separately registered.

~~~math
\boxed{
\text{shared data}
\neq
\text{shared mathematical meaning}.
}
~~~

## 14. Operational versus transformation sustainability horizon

Distinguish:

~~~math
\boxed{
\mathbf J_{\rm sus}^{op}
\neq
\mathbf J_{\rm sus}^{life/trans}.
}
~~~

Operational consequences concern the declared event/operation/recovery horizon.

Transformation/lifecycle consequences may include construction, embodied effects, long-term operation, maintenance, replacement and end-of-life according to the registered accounting boundary.

An intervention can therefore have opposite signs across horizons.

## 15. Sustainability definition for this thesis

Working definition:

> Sustainability of the coupled Power–Transportation SoS is the consequence profile associated with delivering required infrastructure services over a declared spatial and temporal/accounting horizon, evaluated across evidence-supported environmental, resource, economic and social dimensions without hiding cross-sector burden shifting.

This definition does not imply that every consequence is a hard constraint.

## 16. Intervention outcome object

For Stage-6/7 interpretation:

~~~math
\boxed{
\mathcal O_k
=
\left(
\Delta\mathfrak R_k,
\mathcal E_{{\rm fx},k},
\mathcal E_{{\rm fy},k},
\Delta\mathbf J_{{\rm sus},k},
\Delta\mathcal S_k
\right),
}
~~~

where transformation may be represented by:

~~~math
\Delta\mathcal S_k
=
(
\Delta\mathcal G,
\Delta\Theta,
\Delta\mathbb I,
\Delta\mathcal U_{\rm feas}
)
~~~

when scientifically applicable.

Transformation is not part of the sustainability vector; it is a distinct outcome dimension that can change future sustainability/resilience trajectories.

## 17. P2 mandatory audit additions

P2 shall add:

~~~text
SUSTAINABILITY_ROLE_CLASS
DRIVER_STATE_SERVICE_ENDPOINT_CLASS
SUSTAINABILITY_VECTOR_COMPONENT
ACCOUNTING_BOUNDARY_ID
SPATIAL_ACCOUNTING_DOMAIN
TEMPORAL_ACCOUNTING_HORIZON
FUNCTIONAL_UNIT
ACCOUNTING_PERSPECTIVE
LOCAL_CONSEQUENCE_RATE
EMBODIED_CONSEQUENCE
TRAJECTORY_DEPENDENCE
ACCOUNTING_STATE_ID
PHYSICAL_VS_ACCOUNTING_STATE
METRIC_VS_REQUIREMENT
SUSTAINABILITY_REQUIREMENT_RID
HARD_BOUND_AUTHORIZATION
SUSTAINABLE_VIABILITY_STATUS
TRADEOFF_ANALYSIS_METHOD
TIPPING_POINT_EVIDENCE_STATUS
COUPLED_SOS_BOUNDARY
BURDEN_SHIFTING_CHECK
EFFICIENCY_VS_COST
SHARED_QOI_DOUBLE_COUNTING
OPERATIONAL_VS_LIFECYCLE_HORIZON
PARETO_BEFORE_PREFERENCE
~~~

Each applicable field is PASS / BLOCKED / DEFERRED / N/A with rationale and provenance.

## 18. Evidence boundary

Kays & Sadri support conceptual separation and interaction between sustainability and resilience and identify overlapping transport indicators and unresolved trade-offs.

They do not provide thesis-case carbon budgets, energy budgets, cost limits, accessibility thresholds, calibrated tipping points, or validated P–T sustainable-viability sets.

~~~math
\boxed{
\text{conceptual sustainability framework}
\neq
\text{qualified thesis requirement}
\neq
\text{validated sustainable-viability model}.
}
~~~

## 19. Empirical firewall

~~~math
\boxed{
G_{P1.11.5}^{design}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~

No H4/H5 result, sustainability improvement, hard budget, Pareto conclusion or transformation outcome is established by this amendment.
