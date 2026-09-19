> **SUPERSEDED FOR ACTIVE H1 EXECUTION — 2026-09-19**
>
> This file is retained as historical implementation provenance. It predates the current Stage-2 causal gate, Stage2→3 readiness contract, Stage-3 v2 constitution, and global H1–H5 preregistration. Its three example mechanisms and legacy flat interdependency notation MUST NOT be interpreted as current case acceptance or Stage-3 authorization.
>
> Current active interpretation is governed by:
> - `project/CANONICAL_DEPENDENCY_CONTRACT_V1.md`;
> - `project/stage2/STAGE2_CASE_G2_AUDIT_V1_2026-09-19.md`;
> - `project/stage3/STAGE3_STAGE2_TO_STAGE3_INPUT_AND_READINESS_CONTRACT_V2.md`;
> - `project/stage3/STAGE3_SCIENTIFIC_CONSTITUTION_V2.md`;
> - `project/global_integration/GLOBAL_H1_H5_MASTER_PREREGISTRATION_V1.md`.
>
> Current GreenEVT/SMART-DS status: `EV_T_to_P` has Stage-2 causal PASS but Stage2→3 remains BLOCKED; `EV_P_to_T`, `SIGNAL_P_to_T`, and `REPAIR_T_to_P` remain causally BLOCKED for accepted case execution.

# H1 Mathematical Model Specification v1.0

**Status:** frozen mathematical structure for H1 implementation  
**Method:** EGMIV  
**Date:** 2026-09-13  
**Scope:** physical Powerâ€“Transportation demonstrator only; Information and Organization are deferred to H2.


We have now moved from **evidence synthesis** to the first actual mathematical model of the thesis.

```math
\boxed{ \mathfrak I_{PT} \rightarrow \{M_0,M_1,M_2\} \rightarrow F_{\mathcal G}^{(0,1,2)} \rightarrow \text{matched experiment} }
```


### 1. System boundary is now frozen

For H1 we use only the physical system required to identify the effect of dynamic coupling:

```math
\boxed{ \mathcal G_{H1} = \mathcal G_P \cup \mathcal G_T \cup \mathcal C }
```

where `\mathcal G_P` is a radial distribution network, `\mathcal G_T` is a dynamic road network, and `\mathcal C` is the set of EV charging interfaces.

Information `I` and organization `O` are **deliberately excluded from H1**. They enter H2 later. This is necessary for causal attribution: otherwise an improvement could come from information or coordination rather than from physical `P\leftrightarrow T` dynamics.

The power layer uses a DistFlow/LinDistFlow family representation, appropriate for radial distribution-system modeling; DistFlow originates with Baran and Wu. ([IEEE Xplore](https://ieeexplore.ieee.org/document/19266?utm_source=chatgpt.com "Optimal sizing of capacitors placed on a radial distribution system | IEEE Journals & Magazine | IEEE Xplore")) The transportation layer uses a dynamic network-loading formulation based on the Cell Transmission Model, which was explicitly developed to capture queue formation, propagation, dissipation and network traffic dynamics. ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/0191261594900027?utm_source=chatgpt.com "The cell transmission model: A dynamic representation of highway traffic consistent with the hydrodynamic theory - ScienceDirect"))

---

## 2. Three physical interdependencies are now instantiated

Our canonical object

```math
\mathfrak I_{ij}^{\alpha\beta} = (E_i^\alpha,E_j^\beta,M_{ij}, w_{ij},\delta_{ij},\tau_{ij}, a_{ij},m,\mathcal H_t)
```

now has three concrete H1 instances:

| InterfaceDirectionPhysical mechanism |                  |                                                                            |
| ------------------------------------ | ---------------- | -------------------------------------------------------------------------- |
| `\mathfrak I_{PT}^{CH}`              | `P\rightarrow T` | grid power limits charging service, producing EV queues and mobility delay |
| `\mathfrak I_{TP}^{LOAD}`            | `T\rightarrow P` | EV arrivals/charging demand become electrical nodal load                   |
| `\mathfrak I_{TP}^{REP}`             | `T\rightarrow P` | road accessibility and travel time delay power repair crews/resources      |

The third mechanism is directly supported by full-text recovery modeling: Ge et al. explicitly model road-dependent delayed delivery of repair resources and fuel using delayed terms involving road travel time `\gamma(r)`. ([Springer](https://link.springer.com/article/10.1007/s40565-019-0524-7?utm_source=chatgpt.com "Co-optimization approach to post-storm recovery for interdependent power and transportation systems | Journal of Modern Power Systems and Clean Energy | Springer Nature Link"))

---

# 3. `M_0`: independent baseline

```math
\boxed{M_0=\text{independent/uncoordinated}}
```

Power evolves without endogenous transportation feedback:

```math
x_{P,k+1} = f_P(x_{P,k},u_{P,k},\eta_{P,k})
```

and transportation evolves separately:

```math
x_{T,k+1} = f_T(x_{T,k},u_{T,k},\eta_{T,k}).
```

EV charging is represented by a prescribed electrical profile:

```math
p_i^d(k) = p_i^{base}(k) + \bar p_i^{EV}(k).
```

There is no endogenous charger queue, no road-dependent electrical restoration, and no evolving cross-infrastructure state.

This is essential because Yetkin et al. explicitly show that a separate/uncoordinated power-transit representation is a legitimate comparator against coordinated operation. ([Springer](https://link.springer.com/article/10.1007/s11081-023-09878-w?utm_source=chatgpt.com "Co-optimizing the smart grid and electric public transit bus system | Optimization and Engineering | Springer Nature Link"))

---

# 4. `M_1`: static/algebraic coupling

```math
\boxed{M_1=\text{coupled but without dynamic interface memory}}
```

Charging load now enters the power network:

```math
\boxed{ p_i^d(k) = p_i^{base}(k) + \sum_{c\in\mathcal C} A_{ic}p_c^{ch}(k) }
```

where `A_{ic}=1` when charging station `c` is electrically connected to power bus `i`.

Grid availability immediately limits charging:

```math
0\leq p_c^{ch}(k) \leq \bar p_c\,g_{b(c)}(k).
```

The charging requirement can be represented algebraically as

```math
p_c^{ch}(k) \approx \min \left[ \bar p_c g_{b(c)}(k), \frac{E_c}{\eta_c}\lambda_c(k) \right].
```

But:

```math
\boxed{ q_c(k)\text{ does not exist in }M_1 }
```

so there is no accumulation of unmet charging demand.

Similarly, repair travel time is represented by a fixed or snapshot value:

```math
\bar\gamma_\ell.
```

This is our scientifically necessary middle comparator:

```math
\boxed{ \text{coupling}\neq\text{dynamic coupling}. }
```

---

# 5. `M_2`: dynamic causal coupling

This is the actual thesis candidate.

```math
\boxed{ M_2=\text{explicit dynamic causal coupling} }
```

Define

```math
X_k= \left[ e_k,\, y_k,\, n_k,\, q_k,\, R_k,\, r_k \right]
```

and interface variables

```math
z_k= \left[ p_k^{ch}, \mu_k, \lambda_k, F_k^R \right].
```

Then

```math
\boxed{ X_{k+1} = F_{\mathcal G} (X_k,z_k,u_k,\eta_k;\theta) }
```

with interface evolution

```math
\boxed{ z_{ij,k+1} = H_{ij} \left( X_{k-\ell_{ij}}, z_{ij,k}, m_k \right). }
```

That introduces actual **memory, state dependence and delay**.

---

## 6. Dynamic charging interface

Charging service rate is

```math
\boxed{ \mu_c(k) = \frac{\eta_c p_c^{ch}(k)} {E_c} }
```

with

```math
[\mu_c] = \frac{\mathrm{kWh/h}} {\mathrm{kWh/vehicle}} = \mathrm{vehicle/h}.
```

The charger queue evolves as

```math
\boxed{ q_c(k+1) = q_c(k) + \Delta t [ \lambda_c(k)-\mu_c(k) ]. }
```

We additionally impose

```math
q_c(k)\ge0
```

and

```math
\mu_c(k) \le \lambda_c(k)+\frac{q_c(k)}{\Delta t}
```

so the model cannot charge vehicles that do not exist.

This is the important distinction:

```math
\boxed{ M_1: p_c=f(\lambda_c,\text{grid}) }
```

versus

```math
\boxed{ M_2: q_c(k+1) = f(q_c(k),\lambda_c(k),\text{grid}_k). }
```

Mi et al. independently demonstrate that transient traffic states can propagate into the distribution network and that the power and transport systems can interact through evolving traffic and power states. ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0378779621000638?utm_source=chatgpt.com "Optimal operation for coupled transportation and power networks considering information propagation - ScienceDirect")) Song et al. likewise formulate a dynamic coupled equilibrium including charging behavior, station queues and traffic propagation. ([Monash Research](https://research.monash.edu/en/publications/dynamic-equilibrium-of-the-coupled-transportation-and-power-netwo/?utm_source=chatgpt.com "Dynamic equilibrium of the coupled transportation and power networks considering electric vehicles charging behavior - Monash University"))

---

# 7. Dynamic transportation state

For road/cell `a`,

```math
\boxed{ n_a(k+1) = n_a(k) + \Delta t \left[ \sum_b f_{ba}(k) - \sum_b f_{ab}(k) + d_a(k) \right]. }
```

Here

```math
n_a=[\mathrm{vehicles}]
```

and

```math
f_{ab}=[\mathrm{vehicles/hour}].
```

The road-status variable

```math
y_a(k)\in\{0,1\}
```

restricts traffic and repair-resource flow.

This gives H1 an actual spatiotemporal propagation mechanism rather than simply a graph connection.

---

# 8. Dynamic road-to-power recovery coupling

Let

```math
R_m(k)
```

denote available repair-resource/crew equivalents at transport node `m`.

Then

```math
\boxed{ R_m(k+1) = R_m(k) + \Delta t \left[ \sum_{a\in\mathrm{in}(m)} F_{a,k-\ell_a(k)}^R - \sum_{a\in\mathrm{out}(m)} F_{a,k}^R \right]. }
```

Road flow is constrained by

```math
0\le F_{a,k}^R \le \bar F_a\,y_a(k).
```

The delay is

```math
\boxed{ \ell_a(k) = \left\lceil \frac{t_a(k)} {\Delta t} \right\rceil. }
```

Thus a blocked or congested transport link can mathematically delay power restoration.

Power-component repair progress becomes

```math
\boxed{ r_\ell(k+1) = \min \left[ 1,\; r_\ell(k) + \kappa_\ell c_\ell(k)\Delta t \right] }
```

with

```math
0\leq c_\ell(k)\leq R_{m(\ell)}(k).
```

Once

```math
r_\ell(k)=1,
```

the component can become operational.

This directly operationalizes the delayed repair-resource mechanism observed in the post-storm power-transport literature. ([Springer](https://link.springer.com/article/10.1007/s40565-019-0524-7?utm_source=chatgpt.com "Co-optimization approach to post-storm recovery for interdependent power and transportation systems | Journal of Modern Power Systems and Clean Energy | Springer Nature Link"))

---

# 9. Service functions are now frozen

Electricity service:

```math
\boxed{ S_P(k) = \frac{ \sum_i\omega_i p_i^{srv}(k) }{ \sum_i\omega_i p_i^d(k) }. }
```

Mobility service:

```math
\boxed{ S_T(k) = \frac{ \text{weighted completed OD trips} }{ \text{weighted requested OD trips} }. }
```

Thus:

```math
0\le S_P,S_T\le1.
```

And cumulative service loss becomes

```math
\boxed{ L_s = \sum_k [1-S_s(k)] \Delta t, \qquad s\in\{P,T\}. }
```

No arbitrary resilience index is being introduced.

---

# 10. H1 is now directly falsifiable

The crucial comparison is not:

```math
M_2\text{ versus nothing}.
```

It is:

```math
\boxed{ M_2\;\text{vs}\;M_0 \quad\textbf{and}\quad M_2\;\text{vs}\;M_1. }
```

The strongest comparison is actually

```math
\boxed{ M_2\text{ vs }M_1 }
```

because both contain coupling. The only major difference is whether that coupling has explicit temporal state/memory.

Define representation discrepancy:

```math
\boxed{ D_S^{2,r} = \frac1T \int_0^T \left\| S^{M_2}(t) - S^{M_r}(t) \right\|_W dt, \qquad r\in\{0,1\}. }
```

H1a is supported only if this exceeds a **predeclared engineering-resolution threshold**

```math
\varepsilon_{\mathrm{repr}}
```

under matched scenarios and uncertainty propagation.

We do **not** choose `\varepsilon_{\mathrm{repr}}` after observing results.

---

## H1b has a stronger requirement

Being different is insufficient.

Let held-out service-trajectory error be

```math
\boxed{ E_S(M) = \frac1T \int_0^T \left\| \hat S_M(t)-S_{\mathrm{obs}}(t) \right\|_W dt. }
```

Then M2 only earns the claim â€œmore defensibleâ€ if

```math
E_S(M_2) < \min [ E_S(M_0),E_S(M_1) ] - \varepsilon_{\mathrm{pred}}
```

while also satisfying:

```math
\boxed{ V_g(M_2)=0 }
```

for physical-constraint violations and passing identifiability and uncertainty-calibration tests.

So:

```math
\boxed{ \text{more complicated} \not\Rightarrow \text{better model}. }
```

---

# 11. Seven experiments are now frozen

The workbook specifies the matched scenario family from no-disruption and decoupling controls through EV-demand stress, charger-feeder outage, road-constrained repair, joint disruption and held-out validation.

Every `M_0,M_1,M_2` run receives the same:

```math
\boxed{ \eta,\; X_0,\; D,\; \theta_{\mathrm{shared}}, \; T, \; \Delta t }
```

and the same stochastic draw.

Using common random numbers gives paired comparisons and avoids allowing scenario noise to masquerade as model improvement.

---

## 12. No numerical parameters were invented

This is important.

The parameter ledger now classifies quantities according to provenance:

```math
\boxed{ \text{measured/site data} > \text{peer-reviewed/full-text} > \text{benchmark} > \text{sensitivity-only assumption}. }
```

For example, charger rating `\bar p_c`, efficiency `\eta_c`, road capacity, line impedance, repair productivity `\kappa_\ell`, and OD demand cannot simply receive convenient numerical values.

A sensitivity-only assumption cannot later become an empirical thesis result.

---

# 13. Dimensional and limiting-case tests are frozen

Before any scientific simulation, the implementation must satisfy:

```math
[\mu_c] = \mathrm{veh/h},
```

```math
[q_{k+1}] = [q_k] = \mathrm{veh},
```

```math
[p_i^d] = \mathrm{kW},
```

together with vehicle, power and repair-resource conservation.

Two particularly important falsification limits are

```math
\boxed{ M_2 \rightarrow M_1 \quad \text{as dynamic memory/delay}\rightarrow0 }
```

and

```math
\boxed{ M_1,M_2 \rightarrow M_0 \quad \text{when all interface maps are removed}. }
```

If our code cannot reproduce those limits, the model implementation is scientifically invalid.

---

## Where we are now

We have completed:

```math
\boxed{ \begin{array}{c} \checkmark\ \text{H1 evidence}\\ \checkmark\ \text{mechanism extraction}\\ \checkmark\ \mathfrak I_{PT}\text{ instantiation}\\ \checkmark\ \text{system boundary}\\ \checkmark\ M_0\\ \checkmark\ M_1\\ \checkmark\ M_2\\ \checkmark\ \text{state variables}\\ \checkmark\ \text{coupling laws}\\ \checkmark\ \text{delay structure}\\ \checkmark\ \text{service functions}\\ \checkmark\ \text{parameter provenance}\\ \checkmark\ \text{dimensional checks}\\ \checkmark\ \text{scenario matrix}\\ \checkmark\ \text{falsification gates} \end{array} }
```

The **next executable step is no longer theoretical design**.

It is now:

```math
\boxed{ \textbf{IMPLEMENT }M_0 \rightarrow \textbf{VERIFY} \rightarrow M_1 \rightarrow M_2 }
```

starting with the independent power and CTM solvers and their conservation/unitÑ•ÍÑÌ‰•™½É”…‘‘¥¹œ•Ù•¸½¹”½ÕÁ±¥¹œÑ•É´¸()Q¡…ÐÍ•ÅÕ•¹¥¹œ¥Ì…±Í¼™É½é•¸¥¸Ñ¡”Ý½É­‰½½¬¸(