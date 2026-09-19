# Stage 3 — State, Input, Output and QOI Ontology v2

**Status:** CANONICAL STAGE-3 ONTOLOGY — DESIGN/PROTOCOL  
**Effective date:** 2026-09-19  
**Authority:** Stage-1 structure; Stage-2 dependency contract; Stage2→3 readiness contract v2; Stage-4 constitution v1.  
**Purpose:** eliminate state/parameter/QOI and Stage-3/Stage-4 ownership ambiguity before case binding.

## 1. Core ownership rule

Stage 3 generates the physical/dynamic truth used by Stage 4.

\`\`\`math
\boxed{
\text{Stage-3 dynamic truth}
\neq
\text{Stage-4 observation/knowledge/decision state}.
}
\`\`\`

The canonical Stage-3 physical truth is

\`\`\`math
\boxed{
Y_3^{phys}(t)
=
\bigl(x_P(t),x_T(t),z_{PT}(t)\bigr).
}
\`\`\`

where:

- \(x_P\): power-system physical states and algebraic physical variables as selected by the model family;
- \(x_T\): transportation-system physical/mobility states;
- \(z_{PT}\): only those cross-system/interface dynamic states or memories required to make accepted P–T mechanisms executable, e.g. an EV charging backlog/occupancy state when explicitly justified.

\(z_{PT}\) is not a generic storage location for information or organization variables.

## 2. Mandatory Stage-3 / Stage-4 distinction

\`\`\`math
\boxed{
Y^{phys}
\neq
y
\neq
\widehat Y
\neq
b_t.
}
\`\`\`

The following are **not Stage-3 output states**:

\`\`\`math
y_t,\quad
\mathcal I_t,\quad
\widehat Y_t,\quad
b_t,\quad
z_I(t),\quad
z_O(t),\quad
\mathcal U_{feas}(t),\quad
u_t^{policy}.
\`\`\`

They belong to Stage 4 under its current constitution.

Stage 3 may receive a prescribed/exogenous input trajectory \(u^{exo}(t)\) needed to reproduce a physical experiment or baseline. That does not make Stage 3 the owner of the Stage-4 decision policy.

## 3. Variable classes

Every Stage-3 symbol must be assigned exactly one primary class for a declared model realization.

| Class | Symbol family | Meaning |
|---|---|---|
| dynamic state | \(x(t)\) | state requiring initial condition and temporal evolution |
| interface/memory state | \(z_{PT}(t)\) or \(\zeta_e(t)\) | justified cross-system dynamic memory |
| algebraic variable | \(z_a(t)\) | instantaneous constraint variable solved with state |
| exogenous forcing | \(\eta(t,\mathbf r)\) | hazard/environmental input not determined by Stage-3 dynamics |
| prescribed input | \(u^{exo}(t)\) | externally specified physical/operational input for the Stage-3 experiment |
| parameter | \(\theta\) | fixed or uncertain model quantity, not a state |
| mode | \(m(t)\) | discrete operating/disruption/recovery mode |
| event | \(e_k\) | occurrence that triggers reset/mode/topology change |
| topology | \(\mathcal G(t)\) | current graph/connectivity/availability state |
| dependency | \(\mathfrak d_e^{(3)}\) | ready directed mechanism record |
| QOI | \(q(Y,\mathcal G,m)\) | derived quantity used for engineering/model comparison |
| service output | \(Q(t)\) | declared physical service/capability map |

No symbol may silently change class between experiments.

## 4. State admission rule

A candidate quantity belongs to \(Y_3^{phys}\) only if all applicable conditions pass:

\`\`\`math
G_X
=
G_{dyn}
\land
G_{phys}
\land
G_{needed}
\land
G_{identified}
\land
G_{nonredundant}.
\`\`\`

Where:

- \(G_{dyn}\): the quantity has genuine temporal state/memory semantics;
- \(G_{phys}\): it represents physical/interface dynamic truth rather than knowledge about truth;
- \(G_{needed}\): it is required by the selected mechanism/model/QOI;
- \(G_{identified}\): meaning, units, initialization rule and update law are declared;
- \(G_{nonredundant}\): it is not a duplicate of another Markov-equivalent state.

If a quantity is merely observed, estimated, inferred, or chosen by an operator, it does not pass \(G_{phys}\) for Stage-3 state ownership.

## 5. Power-system ontology

The final \(x_P\) depends on the selected model family and remains case-deferred.

Admissible examples include:

\`\`\`math
V_i,\theta_i,P_{ij},Q_{ij},I_{ij},P_G,P_L,SOC_B,
\`\`\`

plus equipment availability/mode variables where required.

The ontology does not require all examples to be states. In a QSTS or power-flow realization, many are algebraic outputs rather than dynamic states.

## 6. Transportation-system ontology

The final \(x_T\) also depends on model family.

Admissible examples include:

- link density/flow/speed;
- queue length;
- vehicle position/speed;
- OD demand state where dynamically represented;
- EV battery SOC where required by the mechanism;
- route/accessibility physical state;
- charging occupancy/backlog when represented as a physical interface process.

Again, model-family choice determines which are states versus algebraic/derived variables.

## 7. Interface state \(z_{PT}\)

Use \(z_{PT}\) only for accepted Stage2→3-ready mechanisms requiring independent dynamic memory.

Examples may include:

- charging queue/backlog;
- interface occupancy;
- progressive physical interface degradation;
- a reduced-order memory state justified by \(\zeta_e\).

If a mechanism is memoryless:

\`\`\`math
\zeta_e=\varnothing
\quad\Rightarrow\quad
\text{no artificial }z_{PT}\text{ state is introduced}.
\`\`\`

## 8. Exogenous forcing and prescribed input

The hazard field is represented generically as

\`\`\`math
\eta(\mathbf r,t).
\`\`\`

Its values, geometry, and stochastic law remain DEFERRED until case qualification.

A prescribed Stage-3 input \(u^{exo}\) may encode a fixed operating schedule/control trajectory used to hold experiments matched. It must be:

- externally specified before target-result inspection;
- distinct from Stage-4 feasible-control decisions;
- held matched where required by H1.

## 9. Parameters

Parameters are not states.

Every Stage-3 parameter must retain:

\`\`\`text
symbol
meaning
unit
mechanism/model
source
status
distribution/bounds if uncertain
aleatory/epistemic classification
identifiability status
validation pointer
validity domain
\`\`\`

A parameter whose value evolves because of modeled physics must be reclassified as a state or input rather than silently treated as time-varying \(\theta\).

## 10. Modes, events and topology

Keep the discrete operating mode explicit:

\`\`\`math
m(t)\in\mathcal M.
\`\`\`

Events are indexed occurrences

\`\`\`math
e_k=(t_k,\text{type},\text{target},\text{cause},\text{provenance})
\`\`\`

that may update state, mode, or topology.

Topology is distinct from state:

\`\`\`math
\mathcal G(t)
\neq
Y^{phys}(t),
\`\`\`

although topology changes may be functions of state/events.

## 11. QOI ontology

Stage-3 QOIs are derived from physical trajectories and are not automatically resilience metrics.

\`\`\`math
q_j(t)
=
\mathcal H_j
\bigl(
Y^{phys}(t),\mathcal G(t),m(t)
\bigr).
\`\`\`

### Primary H1 QOI families

The current canonical families are:

1. cascade;
2. service loss;
3. spatial propagation;
4. recovery.

Their exact predictive/explanatory distance metrics remain DEFERRED until the reference and context of use are qualified.

### Secondary physical QOIs

Existing Level-2 examples may be retained when appropriate:

- \(J_P\), \(J_T\);
- ENS;
- power/transport recovery times;
- charging queue burden;
- repair-access time;
- transport delay.

These are physical consequences, not automatically model-error scores.

## 12. Ownership firewall with Stage 5

The following are not Stage-3 QOIs for purposes of selecting the Stage-3 model:

\`\`\`math
\mathcal V,\quad
\mathcal R,\quad
P_{viable},\quad
P_{recover},\quad
\rho_{\mathcal V},\quad
\rho_g.
\`\`\`

They belong to Stage 5 or later.

This prevents circularity:

\`\`\`math
\boxed{
\text{Stage-5 viability result}
\not\rightarrow
\text{Stage-3 model selection criterion}.
}
\`\`\`

## 13. Service map

Stage 3 evaluates a declared service/capability map

\`\`\`math
\boxed{
Q(t)=\mathcal Q(Y^{phys}(t),\mathcal G(t),m(t)).
}
\`\`\`

The definition and unit of each service component must be inherited from Stage 1/requirements or explicitly versioned before use.

Service \(Q\) is distinct from a resilience summary of the service trajectory.

## 14. Stage-3 output ontology

The accepted Stage-3 output schema is

\`\`\`math
\boxed{
Z_3=
\left(
\mathfrak M_3,
Y^{phys}(t),
\mathcal G(t),
m(t),
\mathbb I^{active}(t),
Q(t),
\mathbb U_3,
\Lambda_3
\right).
}
\`\`\`

This is a scientific schema. Case-specific dimensions, values and resolutions remain DEFERRED.

## 15. Required symbol-registry fields

The future global symbol registry must record for every Stage-3 object:

\`\`\`text
symbol
definition
primary class
shape/type
unit
created stage
consuming stages
source authority
initialization rule if state
update/evaluation rule
uncertainty owner
validity domain
legacy aliases
case status
\`\`\`

## 16. Prohibited category errors

The following are prohibited:

\`\`\`math
\text{state}\equiv\text{parameter},
\`\`\`

\`\`\`math
\text{QOI}\equiv\text{validation metric},
\`\`\`

\`\`\`math
\text{service}\equiv\text{resilience},
\`\`\`

\`\`\`math
Y^{phys}\equiv b_t,
\`\`\`

\`\`\`math
u^{exo}\equiv u_t^{policy}.
\`\`\`

## 17. Claim boundary

This ontology fixes scientific ownership and typing only. It does not select the final model family, choose case variables, determine parameter values, validate a trajectory, or adjudicate H1.
