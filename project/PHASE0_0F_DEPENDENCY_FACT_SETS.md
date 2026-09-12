# Phase 0F — Dependency Fact Sets and Capability Freeze

**Status:** FROZEN 0F TEST FIXTURE v1.0  
**Purpose:** define the dependency-level truths that must survive field/layer ablation.  
**Control:** the ontology remains the current canonical `M_0={P,T,I,O}` during 0F; no ontology change is permitted.  
**Reasoning protocol:** `LEARN -> VERIFY -> FORMULATE -> DERIVE -> TEST -> VALIDATE -> SYNTHESIZE -> ADVANCE`.

---

## 1. Scientific question

What is the minimum mathematical object required to represent one infrastructure dependency without losing causal, dynamic, evidential, executable, or engineering-service meaning?

Two candidates enter the test:

```math
\mathfrak d_e=(s,r,\rho,m,q,M,z,w,\delta,c,U,\mathcal H)
```

and

```math
\mathfrak D_e=(\mathcal C_e,\Sigma_e,\Pi_e,\Xi_e).
```

Neither is assumed correct.

---

## 2. Evidence discipline

Claim labels used in this file:

```text
[E] source/standard supported;
[D] mathematically derived from frozen definitions;
[P] proposed representation;
[A] declared assumption;
[U] unresolved.
```

Relevant external anchors retained from 0C–0E:

1. CISA's infrastructure-dependency primer treats dependencies as directional/bidirectional relations and recognizes physical, cyber, geographic and logical forms: https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/resilience-services/infrastructure-dependency-primer/learn
2. W3C PROV-O defines interoperable provenance and qualified influence objects that can carry relation-level provenance: https://www.w3.org/TR/prov-o/
3. FMI 3.x defines executable model-variable dependencies, causality and model structure; these are simulation-interface semantics rather than proof of physical causality: https://fmi-standard.org/docs/3.0.1/
4. Vagner–Spivak–Lerman formalize typed open-system wiring syntax separately from dynamical-system semantics: https://arxiv.org/abs/1408.1598
5. Structured/decorated cospans provide compositional open-system boundaries and decorations: https://arxiv.org/abs/2101.09363

These sources constrain the representation but do not by themselves establish the thesis contribution.

---

## 3. Frozen minimum capability set

The dependency representation must preserve:

```math
\mathcal K=\{K_1,\ldots,K_8\}.
```

| ID | Required capability | Failure condition |
|---|---|---|
| `K1` | typed source and receiver | source or receiver identity cannot be uniquely recovered |
| `K2` | direction | `s->r` cannot be distinguished from `r->s` |
| `K3` | causal/functional mechanism | representation states only adjacency/correlation and not how the receiver is affected |
| `K4` | state/time/context dependence | effective dependency cannot change with operating state, disturbance, control or activation context |
| `K5` | delay/latency/history where relevant | time-shifted influence cannot be represented when physically required |
| `K6` | evidence/provenance/epistemic status | physical relation state is conflated with confidence that the relation exists or is correctly parameterized |
| `K7` | mapping to an executable mathematical/model realization | relation semantics cannot be translated consistently into equations, transition logic or an accepted model interface |
| `K8` | trace to measurable system service consequence | relation cannot participate in `Delta d -> Delta X -> Delta Q` |

### Important distinction

`K7` does not require storing software code inside each dependency. It requires a well-defined realization map.

`K8` does not require duplicating the complete service model inside each dependency. It requires a traceable path from the receiver-state perturbation to the system-level service functional.

---

## 4. Common dependency truth structure

For each dependency `e`, freeze a fact vector

```math
\mathcal F_e=
(f_e^{src},
f_e^{rec},
f_e^{dir},
f_e^{mech},
f_e^{dyn},
f_e^{delay},
f_e^{prov},
f_e^{exec},
f_e^{service}).
```

This vector contains **facts**, not proposed fields. A representation passes only if those facts can be reconstructed uniquely or derived using a globally frozen, non-case-specific map.

---

# 5. Dependency D1 — feeder power -> fast-charging service

```math
D^{(1)}:
P_{feeder}\rightarrow T_{FCS}.
```

### Physical mechanism [E/D]

Available charging power constrains charging-station operation. A minimal admissible relation is

```math
0\le P_{FCS}(t)\le P_{avail}(t),
```

with charging/service rate

```math
\mu_{FCS}(t)=f_{FCS}(P_{FCS}(t),N_{port},SOC,\ldots).
```

A local dependency signature, where differentiable, is

```math
\frac{\partial \mu_{FCS}}{\partial P_{avail}}\neq0.
```

The downstream mobility-service functional may be written

```math
Q_{mob}=G_T(x_T).
```

### Frozen facts

| Capability | Fact |
|---|---|
| K1 | source=`P_feeder`; receiver=`T_FCS` |
| K2 | power-to-transport direction |
| K3 | electrical-power availability constrains charger operation/service rate |
| K4 | influence depends on feeder voltage/loading, charger state and operating regime |
| K5 | electrical/control delay may be zero/negligible or explicitly modeled; the grammar must permit it |
| K6 | evidence source and calibration/validation status are distinct from feeder physical state |
| K7 | mechanism must map into `f_FCS` or equivalent executable transition/equation |
| K8 | charger-state change must trace to `Q_mob` |

---

# 6. Dependency D2 — EV forecast information -> power controller

```math
D^{(2)}:
T_{EV\ forecast}\rightarrow P_{controller}.
```

### Informational mechanism [D]

Let the received transport-side forecast be

```math
\widehat d_{EV}(t-\delta_I).
```

A power-control law may use it as

```math
u_P(t)
=
\pi_P\!\left(x_P(t),\widehat d_{EV}(t-\delta_I),q_I(t)\right),
```

where `q_I` is information quality/availability.

A local functional signature is

```math
\frac{\partial \pi_P}{\partial \widehat d_{EV}}\neq0
```

in an operating regime where the forecast is active in control.

### Frozen facts

| Capability | Fact |
|---|---|
| K1 | source=`T_EV_forecast`; receiver=`P_controller` |
| K2 | information flows T-side -> P-side |
| K3 | forecast changes feasible/selected control action rather than transmitting electrical power |
| K4 | effect depends on information quality, controller mode and operating state |
| K5 | latency `delta_I` can materially alter the received forecast/control action |
| K6 | evidence that the controller actually consumes the forecast must be recorded separately from forecast quality |
| K7 | relation maps into the controller law `pi_P` |
| K8 | changed control traces through `F_P` to electricity/charging service outputs |

---

# 7. Dependency D3 — road authority/access decision -> power-repair accessibility

```math
D^{(3)}:
T_{road\ authority}\rightarrow P_{crew\ access}.
```

### Organizational/physical mechanism [D]

Let `a_R(t)` denote an authority/access decision and define the feasible road set

```math
\mathcal R_T^{feas}(t)=\Gamma_R(x_T(t),a_R(t)).
```

Power-repair travel time is

```math
T_{crew}(t)
=
\min_{r\in\mathcal R_T^{feas}(t)}
\sum_{a\in r} t_a(x_T(t)).
```

Hence an organizational decision changes a physical feasibility set and therefore a restoration-time component.

### Frozen facts

| Capability | Fact |
|---|---|
| K1 | source=`T_road_authority`; receiver=`P_crew_access` |
| K2 | authority/access constraint acts toward repair feasibility |
| K3 | authority decision modifies the feasible route/access set |
| K4 | effect depends on hazard, road state, authority mode and current repair location |
| K5 | decision/communication/mobilization delay can enter restoration time |
| K6 | authority rule/source and evidence of operational applicability are epistemic/institutional facts |
| K7 | mechanism maps into `Gamma_R`, route feasibility and restoration scheduling logic |
| K8 | changed crew access traces to restoration and `Q_electricity` |

---

# 8. Dependency D4 — EV charging behavior -> feeder loading

```math
D^{(4)}:
T_{EV\ charging}\rightarrow P_{feeder\ load}.
```

### Physical mechanism [E/D]

Aggregate charging demand enters the power balance:

```math
P_{ch}(t)=\sum_{n\in\mathcal N_{EV}}\chi_n(t)p_n(t),
```

```math
P_L(t)=P_{base}(t)+P_{ch}(t).
```

For an active charging device,

```math
\frac{\partial P_L}{\partial p_n}=\chi_n(t)>0.
```

### Frozen facts

| Capability | Fact |
|---|---|
| K1 | source=`T_EV_charging`; receiver=`P_feeder_load` |
| K2 | transport charging demand acts toward power loading |
| K3 | electrical charging demand enters feeder real-power demand |
| K4 | influence changes with arrivals, SOC, charging policy, price/control and network state |
| K5 | scheduling/control latency can be represented if material |
| K6 | data/model provenance is separate from actual charging state |
| K7 | relation maps into the feeder/load-flow or dynamic power model |
| K8 | feeder-state change traces to `Q_electricity` and potentially `Q_mobility` |

---

## 9. Cross-case coverage

The four dependencies deliberately cover distinct mechanism classes:

```text
D1 physical P -> T;
D2 informational T -> P;
D3 organizational/authority T -> P;
D4 physical T -> P with state-dependent aggregate demand.
```

Together they force the candidate grammar to preserve direction, heterogeneous mechanism type, dynamics, delay, epistemic evidence, mathematical realization and service consequence.

---

## 10. Validation boundary

These are controlled symbolic dependencies anchored in accepted engineering mechanisms; they are not calibrated empirical estimates for a specific city/grid/road network.

Therefore 0F may establish **formal necessity, redundancy and representational sufficiency** within this fixture. It may not claim universal minimality or empirical predictive superiority without later case-study calibration and validation.
