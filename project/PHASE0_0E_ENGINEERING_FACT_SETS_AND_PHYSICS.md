# Phase 0E — Engineering Fact Sets and Physics Fixture

**Status:** FROZEN 0E TEST INPUT v1.0  
**Purpose:** define the exact engineering fact sets `F_1,...,F_5` used to test the engineering significance of the 0D type-system difference.  
**Control rule:** the same facts, equations, evidence and service definitions are supplied to `M_0` and `M_1`. Only endpoint/system typing differs.  
**Decision boundary:** this file does not decide RETAIN / REVISE / REPLACE.

---

## 1. Evidence and standards basis

The factual fixtures are intentionally minimal and mechanism-based. They are supported by established engineering standards and current coupled-infrastructure literature rather than invented solely for the ontology comparison.

### E1 — EV charging and Power–Transportation coupling

ISO 15118-1:2019 and ISO 15118-20:2022 establish interoperable EV–EVSE communication and energy-transfer use cases, including bidirectional power transfer. Current coupled Power–Transportation models explicitly link EV traffic/charging decisions, fast-charging-station queues, charging demand and distribution-network operation.

Representative sources:

- ISO 15118-1:2019, *Road vehicles — Vehicle to grid communication interface — Part 1*.
- ISO 15118-20:2022, *Road vehicles — Vehicle to grid communication interface — Part 20*.
- Song, Y., Ngoduy, D., Dantsuji, T., & Ding, C. (2025). *Dynamic equilibrium of the coupled transportation and power networks considering electric vehicles charging behavior*. Transportation Research Part A, 199, 104590. DOI: 10.1016/j.tra.2025.104590.

### E2 — Information, timing and human/organizational concerns

NIST SP 1500-201/202 and the Timing Annex treat CPS as interacting digital, analog, physical and human components and explicitly distinguish timing, data, human, functional and composition concerns. Latency is treated as a time delay introduced by a device or process.

Representative source:

- NIST SP 1500-201, *Framework for Cyber-Physical Systems: Volume 1, Overview*.
- NIST CPS Timing Annex, 2017.

### E3 — Transportation accessibility and repair restoration

Post-disaster restoration research explicitly models repair-crew routing as constrained by damaged transportation networks; degraded road accessibility delays deployment and restoration of power-system assets.

Representative sources:

- Fan, J. et al. (2024). *A post-disaster restoration model for power-gas-transportation distribution networks considering spatial interdependency and energy hubs*. Electric Power Systems Research, 233, 110505. DOI: 10.1016/j.epsr.2024.110505.
- Wang, Y. et al. (2026). *Hierarchical emergency restoration of weakly interconnected distribution systems via a transportation–crew–grid coupled framework*.

### E4 — Water extension and pump physics

ISO 9906 defines hydraulic pump output power as

```math
P_h=\rho gQH.
```

For an electrically driven pump with aggregate efficiency `eta`, a minimal electrical-input relation is

```math
P_{pump}=\frac{\rho gQH}{\eta}.
```

Power–water literature explicitly treats electrical energy for pumping as a principal Power-to-Water dependency.

Representative sources:

- ISO 9906:2012, *Rotodynamic pumps — Hydraulic performance acceptance tests*.
- Zuloaga et al. (2020), *Interdependent electric and water infrastructure modelling, optimisation and control*, IET Energy Systems Integration.

---

# 2. Common physical laws and notation

The ontology comparison is prohibited from changing these mechanisms.

## 2.1 Power subsystem

```math
\dot x_P=F_P(x_P,u_P,h_P,\vartheta_P).
```

At a feeder/bus supplying charging load, use the minimal balance

```math
P_{net}(t)=P_{base}(t)+P_{ch}(t),
```

with aggregate EV charging demand

```math
P_{ch}(t)=\sum_{n\in\mathcal N_{EV}}\chi_n(t)p_n(t),
```

where `chi_n(t)` is the charging-connection/activity state and `p_n(t)` is charging power.

The ontology is not permitted to alter the electrical laws, network constraints or state variables that determine feasible `P_ch`.

## 2.2 Transportation subsystem

```math
\dot x_T=F_T(x_T,u_T,h_T,\vartheta_T).
```

A minimal FCS queue balance is

```math
\dot n_q(t)=\lambda_{EV}(t)-\mu_{FCS}(t)
```

when the queue is active, where `lambda_EV` is arrival rate and `mu_FCS` is the effective charging-service rate.

The key reciprocal mechanism is

```math
\lambda_{EV}\longrightarrow P_{ch}
```

and

```math
P_{available}\longrightarrow\mu_{FCS}\longrightarrow n_q\longrightarrow Q_{mobility}.
```

## 2.3 Information/control relation

Let the EV-demand estimate be

```math
\widehat d_{EV}(t)=\mathcal E_I\!\left(y_T[0,t],z_I(t)\right).
```

With information delay `delta_I`, a power-control action may be represented as

```math
u_P(t)=\pi_P\!\left(x_P(t),\widehat d_{EV}(t-\delta_I)\right).
```

The physical state then evolves through the unchanged power law

```math
\dot x_P=F_P(x_P,u_P,h_P,\vartheta_P).
```

This distinguishes information transport from physical energy transport.

## 2.4 Organizational/restoration relation

Let `R_T(t)` be the set of currently feasible road routes for a repair crew. Crew travel time is

```math
T_{travel}(t)=\min_{r\in R_T(t)}\sum_{a\in r}t_a(x_T(t)).
```

For sequential response processes, use

```math
T_{response}
=
\tau_{decision}
+
\tau_{coordination}
+
\tau_{mobilization}
+
T_{travel}
+
\tau_{repair}.
```

When tasks overlap, the arithmetic sum is replaced by the corresponding critical-path completion time; the ontology comparison does not change this rule.

## 2.5 Water subsystem for V5

The third-domain stress test introduces an independent water state `x_W` and law

```math
\dot x_W=F_W(x_W,u_W,h_W,\vartheta_W),
```

with

```math
F_W\neq F_P,
\qquad
F_W\neq F_T.
```

A minimal tank balance is

```math
A_t\dot h(t)=Q_{in}(t)-Q_{out}(t).
```

The pump coupling is

```math
P_{pump}(t)=\frac{\rho gQ(t)H(t)}{\eta(t)}.
```

Thus electrical availability can constrain water pumping while water retains its own hydraulic state and governing equations.

---

# 3. Frozen fact set `F_1` — V1 reciprocal physical EV charging coupling

```math
\mathcal F_1=\{f_{11},\ldots,f_{1,10}\}.
```

| ID | Frozen engineering fact |
|---|---|
| `f11` | the feeder is a Power physical entity |
| `f12` | the FCS/mobility charging interface is treated as a Transportation physical entity in the frozen V1 fixture |
| `f13` | feeder electrical availability constrains feasible charging power |
| `f14` | EV arrival/charging activity is a Transportation-state quantity |
| `f15` | aggregate charging demand satisfies `P_ch=sum chi_n p_n` |
| `f16` | charging demand enters the feeder electrical load/balance |
| `f17` | available charging power/capacity affects FCS service rate and therefore queue/mobility state |
| `f18` | `P->T` and `T->P` mechanisms are directional and physically different |
| `f19` | effective coupling varies with charging occupancy, arrivals, electrical limits and time |
| `f1,10` | the coupled state can affect both electricity and mobility service outputs |

Cardinality:

```math
|\mathcal F_1|=10.
```

---

# 4. Frozen fact set `F_2` — V2 information-mediated coupling

```math
\mathcal F_2=\{f_{21},\ldots,f_{29}\}.
```

| ID | Frozen engineering fact |
|---|---|
| `f21` | EV-demand/arrival forecast originates from Transportation information |
| `f22` | the receiving controller is a Power information/control entity |
| `f23` | information transmission/processing has a nonnegative delay `delta_I` |
| `f24` | information quality/forecast error is distinct from the physical Transportation state |
| `f25` | the power controller may use delayed/estimated EV demand to select `u_P` |
| `f26` | `u_P` changes a Power physical setpoint/feasible operating trajectory |
| `f27` | the information relation is not itself an electrical-energy flow |
| `f28` | changing delay or information quality can change the selected control action |
| `f29` | the resulting control action can propagate to electricity and charging-service consequences |

Cardinality:

```math
|\mathcal F_2|=9.
```

---

# 5. Frozen fact set `F_3` — V3 organizational coupling

```math
\mathcal F_3=\{f_{31},\ldots,f_{39}\}.
```

| ID | Frozen engineering fact |
|---|---|
| `f31` | the road authority is a Transportation organizational entity |
| `f32` | road accessibility is a Transportation physical/operational state |
| `f33` | an authority/coordination decision can change feasible access or routing conditions |
| `f34` | the repair crew is a Power organizational/resource entity |
| `f35` | crew deployment requires use of the Transportation network |
| `f36` | crew travel/mobilization time depends on road state and feasible routes |
| `f37` | repair action changes the Power restoration trajectory |
| `f38` | response completion depends on decision, coordination, mobilization, travel and repair timing |
| `f39` | the mechanism affects electricity restoration and emergency-access service consequences |

Cardinality:

```math
|\mathcal F_3|=9.
```

---

# 6. Frozen fact set `F_4` — V4 mediated `P->T->P` feedback

```math
\mathcal F_4=\{f_{41},\ldots,f_{4,10}\}.
```

| ID | Frozen engineering fact |
|---|---|
| `f41` | an initiating Power disruption changes a Power physical state |
| `f42` | Power loss can degrade transport charging/signalling functionality through a declared dependency |
| `f43` | degraded Transportation state can increase travel time or reduce accessibility |
| `f44` | Power-repair crew deployment depends on Transportation accessibility |
| `f45` | delayed crew arrival can delay repair/restoration of the Power system |
| `f46` | the resulting system-level reciprocity is mediated and need not be a reciprocal edge between the same two assets |
| `f47` | the path has ordered event times and causal delays |
| `f48` | common-cause exposure must be distinguished from induced cross-system propagation |
| `f49` | feedback strength can be state/time dependent |
| `f4,10` | the closed path can affect electricity, mobility and emergency-access services |

Cardinality:

```math
|\mathcal F_4|=10.
```

A local sensitivity signature for a nontrivial mediated feedback is, where differentiable,

```math
\frac{\partial T_{rest}}{\partial x_P}
=
\frac{\partial T_{rest}}{\partial T_{crew}}
\frac{\partial T_{crew}}{\partial x_T}
\frac{\partial x_T}{\partial x_P},
```

with a nonzero product indicating an active causal pathway in that operating regime. This derivative is a local diagnostic, not a universal definition of interdependency.

---

# 7. Frozen fact set `F_5` — V5 third-domain Water extension

```math
\mathcal F_5=\{f_{51},\ldots,f_{5,10}\}.
```

| ID | Frozen engineering fact |
|---|---|
| `f51` | Water is a third independently meaningful physical infrastructure domain |
| `f52` | Water has its own hydraulic state variables such as pressure/head/flow/storage |
| `f53` | Water retains a domain law `F_W` distinct from `F_P` and `F_T` |
| `f54` | a water-storage state can satisfy the mass balance `A_t dh/dt=Q_in-Q_out` |
| `f55` | pump hydraulic output is `rho g Q H` and electrical input depends on efficiency |
| `f56` | electrical availability can constrain pump operation and therefore water state/service |
| `f57` | Water has a measurable service output `Q_water` |
| `f58` | adding Water must not change the existing semantics of P–T relations |
| `f59` | Water may have informational and organizational entities/functions analogous in role class but not identical in physics to P/T entities |
| `f5,10` | new P–W, T–W, information and organizational relations must use the same frozen relation payload form |

Cardinality:

```math
|\mathcal F_5|=10.
```

---

# 8. Dimensional-consistency audit

The principal physical equations satisfy:

```math
[P_{ch}]=\mathrm{W},
```

```math
[\rho gQH]
=\frac{\mathrm{kg}}{\mathrm{m^3}}
\frac{\mathrm{m}}{\mathrm{s^2}}
\frac{\mathrm{m^3}}{\mathrm{s}}
\mathrm{m}
=\mathrm{W},
```

and

```math
[A_t\dot h]=\mathrm{m^2}\frac{\mathrm m}{\mathrm s}=\mathrm{m^3/s}=[Q].
```

The 0E ontology comparison is invalid if either representation changes these dimensions, laws or physical parameter meanings.

---

# 9. Equal-information ledger

For every `F_k`, both models receive:

```text
- identical entity identities;
- identical domain-affiliation evidence;
- identical aspect/function facts;
- identical mechanism fields;
- identical state/time/delay facts;
- identical provenance/evidence facts;
- identical governing equations;
- identical service definitions.
```

Therefore any measured difference in 0E must arise from the ontology/type representation, not from unequal physical or evidential information.

---

# 10. Scientific validity boundary

These are symbolic mechanism-verification cases, not calibrated empirical predictions. They are sufficient for testing semantic preservation, type ambiguity, composability and physics preservation. They are not sufficient for claims about numerical resilience gains, predictive accuracy, recovery improvement or real-world causal effect size.