# Literature-Grounded Mathematics Across the Six Chains

## Evidence-label rule

Every mathematical statement in future work should be labeled mentally as one of:

1. **Established equation/form** — explicitly represented in a cited source.
2. **Canonical mathematical form** — standard theory used in the field, not claimed to be a verbatim equation from one paper.
3. **Thesis-proposed synthesis** — an adapted/new object proposed for this thesis.

This prevents false novelty and false attribution.

---

# I. Physical-System Chain

## I.1 Conservation / governing laws

Canonical conservation form:

`∂rho/∂t + div(J) = s`

Interpretation depends on sector:

- power: electrical energy/power balances;
- water: mass/momentum/hydraulic constraints;
- transportation: conservation-type traffic-flow models;
- solid waste: material accumulation/removal.

**Status:** canonical mathematical physics, not a single universal infrastructure equation.

The thesis should not claim one universal P–W–T–SW conservation law. It should retain sector-specific laws and define explicit coupling operators.

## I.2 Graph/multilayer structure

Single network:

`G = (V,E)`

Canonical multilayer/supra-adjacency form:

`A_sup = [[A^P, C^PW, C^PT, C^P,SW], [C^WP, A^W, ...], ...]`

where diagonal blocks are intra-sector networks and off-diagonal blocks encode cross-sector connections.

**Literature anchors:**

- Kivelä et al. (2014), *Multilayer networks*, DOI `10.1093/comnet/cnu016`.
- Boccaletti et al. (2014), *The structure and dynamics of multilayer networks*, DOI `10.1016/j.physrep.2014.07.001`.

**Status:** established multilayer-network mathematics.

## I.3 Infrastructure interdependency taxonomy

Rinaldi, Peerenboom & Kelly (2001) established the widely used categories:

- physical;
- cyber;
- geographic;
- logical.

**Citation:** DOI `10.1109/37.969131`.

**Status:** conceptual taxonomy, not one governing equation. Do not fabricate a “Rinaldi interdependency equation.”

## I.4 Interface mechanisms

Existing literature often represents inter-system coupling as inter-layer edges, dependency links, or coupling matrices.

A generic canonical coupling term is:

`x_i_dot = f_i(x_i) + sum_j C_ij g_ij(x_i,x_j) + b_i u_i + d_i eta_i`

**Status:** canonical networked dynamical-system form.

Potential thesis contribution: elevate the interface from a static edge `C_ij` to an explicit dynamic mechanism/state `Z_ij(t)` with its own physics, switching, degradation, capacity, or uncertainty.

Do not attribute the proposed dynamic `Z_ij(t)` formulation to Rinaldi/Kivelä unless a specific source actually formulates it.

## I.5 Hybrid dynamics

Standard hybrid representation:

`x_dot = f(x), x in C`

`x+ = g(x), x in D`

where `C` is the flow set and `D` the jump set.

**Literature anchor:** Goebel, Sanfelice & Teel, *Hybrid Dynamical Systems: Modeling, Stability, and Robustness*.

**Status:** mature general mathematics; infrastructure failure/repair modes can be mapped into this structure.

## I.6 Interdependent-network cascades/percolation

Key order parameter:

`P_infinity(p)` = mutually connected giant-component fraction.

Critical threshold:

`p_c`.

Buldyrev et al. (2010) showed abrupt collapse behavior in interdependent networks and, for the studied coupled ER setting, a critical average degree around `2.445` compared with `1` for a single ER network in the corresponding setting.

**Citation:** Buldyrev et al. (2010), DOI `10.1038/nature08932`.

Parshani et al. (2010) treated interdependency strength `q` as a control parameter and identified a critical coupling separating abrupt/continuous transition regimes.

**Citation:** DOI `10.1103/PhysRevLett.105.048701`.

Gao et al. (2012) extended percolation concepts to networks of networks.

**Citation:** DOI `10.1038/nphys2180`.

**Status:** mature network physics. Thesis novelty cannot be “interdependent networks can cascade.”

Potential thesis gap: connect dynamic interface physics and hazard-driven hybrid switching to service-level viability/recovery rather than stopping at connectivity collapse.

---

# II. Observation–Inference–Prediction Chain

## II.1 Observation equation

Canonical state-space measurement form:

`y_k = h(x_k,theta) + epsilon_k`

**Status:** standard state-space/inverse-problem representation.

## II.2 Observability

For linear `x_dot = A x`, `y = C x`, classical observability matrix:

`O = [C; CA; CA^2; ...; CA^(n-1)]`

Complete state observability condition:

`rank(O) = n`.

**Status:** mature control theory.

Thesis question: are hidden infrastructure interface/state variables observable from realistically available measurements?

## II.3 Regularized inverse problem

Canonical form:

`theta_hat = argmin_theta [ ||y_obs - G(theta)||_{Sigma^-1}^2 + lambda R(theta) ]`

**Status:** mature inverse-problem framework.

### Identifiability

Core uniqueness question:

`G(theta_1) = G(theta_2) ⇒ theta_1 = theta_2 ?`

**Literature anchor:** Raue et al. (2009), practical/structural non-identifiability and profile likelihood, DOI `10.1093/bioinformatics/btp358`.

Potential thesis gap: interface-parameter/structure identifiability for coupled infrastructure, and propagation of identification uncertainty into resilience/viability geometry.

## II.4 Physics-informed inference

Canonical PINN loss:

`L(theta) = lambda_d L_data + lambda_f L_physics + lambda_b L_BC/IC`

**Literature anchor:** Raissi, Perdikaris & Karniadakis (2019), DOI `10.1016/j.jcp.2018.10.045`.

**Status:** PINNs themselves are not novel. A thesis must not claim novelty for using a PINN unless the scientific/mathematical contribution lies elsewhere.

## II.5 Bayesian inference

Canonical posterior:

`p(theta | y) ∝ L(y | theta) p_0(theta)`

**Status:** standard Bayesian inverse-problem/statistical form.

## II.6 Global sensitivity/UQ

First-order Sobol index:

`S_i = Var_{X_i}[ E(Y|X_i) ] / Var(Y)`

Total-effect index:

`S_Ti = 1 - Var_{X_~i}[ E(Y|X_~i) ] / Var(Y)`

**Literature anchors:**

- Sobol (2001), DOI `10.1016/S0378-4754(00)00270-6`.
- Saltelli et al. (2010), DOI `10.1016/j.cpc.2009.09.018`.

**Status:** mature UQ/sensitivity mathematics.

---

# III. Hazard–Failure–Consequence Chain

## III.1 Hazard as stochastic forcing/random field

Generic representation:

`eta = eta(s,t,omega)`

**Status:** canonical stochastic-process/random-field notation.

## III.2 Spatial dependence / copulas

Sklar-type representation:

`F(x_1,...,x_d) = C(F_1(x_1),...,F_d(x_d))`

Gaussian-copula form:

`C_Sigma(u_1,...,u_d) = Phi_Sigma(Phi^-1(u_1),...,Phi^-1(u_d))`

**Status:** established dependence modelling, not infrastructure-specific novelty.

## III.3 Fragility

Canonical lognormal fragility curve:

`P(D >= d | IM) = Phi[(ln IM - ln theta_d)/beta_d]`

where `IM` is hazard intensity, `theta_d` the median capacity and `beta_d` dispersion.

**Status:** established fragility-model form.

## III.4 Damage-induced switching

Infrastructure damage can change operating mode:

`m^- → m^+`

and thus the governing field:

`F_{m^-}(x) → F_{m^+}(x)`.

**Status:** synthesis connecting established fragility concepts with established hybrid-system mathematics.

## III.5 Function and service mapping

Proposed generic thesis mapping:

`Y(t) = pi(X(t),Z(t),m(t))`

**Status:** thesis-proposed/general systems synthesis unless a specific paper is cited for a particular `pi`.

Important literature-grounded conceptual distinction:

`physical damage ≠ functional loss ≠ critical-service loss ≠ societal consequence`.

Potential thesis contribution: formalize and verify this mapping before applying viability/recovery mathematics.

---

# IV. Resilience–Viability–Recovery Chain

## IV.1 Classical performance-loss resilience

Bruneau et al. resilience-triangle loss concept:

`LR = integral_{t0}^{t1} [100 - Q(t)] dt`

with `Q(t)` representing system quality/performance.

**Citation:** Bruneau et al. (2003), DOI `10.1193/1.1623497`.

They also formalized the influential four-R framing: robustness, redundancy, resourcefulness, rapidity.

**Status:** established resilience-performance framework.

## IV.2 Recovery ratio

Henry & Ramírez-Márquez time-dependent recovery-oriented resilience ratio:

`R(t) = [phi(t) - phi(t_d)] / [phi(t_0) - phi(t_d)]`

**Citation:** DOI `10.1016/j.ress.2011.09.002`.

**Status:** established time-dependent resilience metric. Do not claim novelty merely for a time-varying resilience curve.

## IV.3 Viability kernel

For differential inclusion `x_dot in F(x)`, canonical viability kernel:

`Viab_F(K) = {x_0 in K : exists trajectory x(.) with x(0)=x_0, x_dot in F(x), x(t) in K for all t}`

**Literature anchor:** Saint-Pierre (1994), *Approximation of the Viability Kernel*, DOI `10.1007/BF01204182`, within the Aubin/viability-theory tradition.

**Status:** established mathematical theory.

Potential thesis contribution: define physically meaningful P–W–T–SW admissibility `K_SE` and analyze how dynamic interface mechanisms deform its viability geometry.

## IV.4 Hamilton–Jacobi reachability

For nonlinear dynamics `x_dot = f(x,u,d)`, HJ/HJI value function form:

`V_t + H(x,grad V) = 0`

with reachable/avoid set represented by a level/sublevel set such as:

`R(t) = {x : V(x,t) <= 0}`

and game Hamiltonian conceptually:

`H(x,p) = min_u max_d p^T f(x,u,d)`

with min/max ordering depending on problem convention.

**Literature anchor:** Mitchell, Bayen & Tomlin (2005), DOI `10.1109/TAC.2005.851439`.

**Status:** established reachability/HJI mathematics and viscosity-solution theory.

## IV.5 Recoverability / capture

Canonical viability-theory concept:

`Capt(K) = {x_0 : exists admissible control and finite T such that x(T) in K}`

**Status:** capture/reachability concept is established mathematically; exact sustainable/equitable infrastructure definition is thesis-specific.

Critical separation:

- `x_0 in Viab(K)` — admissibility can be maintained;
- `x_0 notin Viab(K)` but `x_0 in Capt(K)` — disrupted but recoverable;
- `x_0 notin Capt(K)` — nonrecoverable under available actions.

## IV.6 Control

Control existence question:

`exists u(.) ?`

Optimal recovery question:

`u* = argmin_u J(x,u)` subject to dynamics and recovery/admissibility constraints.

**Status:** optimal control itself is mature. Novelty must lie in the problem structure, interface physics, admissibility geometry, proofs, or algorithms.

---

# V. Engineering Design–Operation–Adaptation Chain

## V.1 Design optimization

Canonical form:

`d* = argmin_{d in D} J(d)`

subject to physical/engineering constraints.

**Status:** mature optimization structure.

Existing infrastructure literature includes interface/coupling topology design and resilience-oriented infrastructure design.

## V.2 Defender–attacker–defender structure

Conceptual tri-level form:

`max_d min_a max_r P(d,a,r)`

where first defender chooses protection/design, attacker chooses damage, and second defender operates/restores the damaged system. Sign/order depends on loss/performance convention.

**Literature anchor:** Ouyang (2017) interdependent power–water resilience enhancement under localized attacks, DOI `10.1016/j.ejor.2017.04.022`.

**Status:** tri-level resilience optimization is established.

## V.3 Two-stage stochastic planning

Canonical form:

`min_x [ c^T x + E_xi Q(x,xi) ]`

**Status:** mature stochastic-programming architecture.

Infrastructure corpus includes multiobjective/two-stage stochastic expansion and resilience planning; e.g. Tiong et al. DOI `10.1016/j.ijcip.2023.100588`.

---

# VI. Sustainability–Equity–Governance–Decision Chain

## VI.1 Sustainability/resilience trade-offs

Do not assume `resilience = sustainability`.

Representative multiobjective synthesis:

`min_d [ Cost(d), RecoveryTime(d), CO2(d), ServiceLoss(d), Inequity(d), FailureRisk(d) ]`

**Status:** canonical multiobjective synthesis; exact vector is thesis/problem-specific.

A major corpus anchor is:

**Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery**, DOI `10.1016/j.trd.2023.103800`.

## VI.2 Equity

Equity literature distinguishes dimensions such as:

- distributional-demographic;
- distributional-spatial;
- procedural;
- capacity equity.

**Literature anchor:** Coleman et al. (2024), DOI `10.1038/s44304-024-00022-x`.

**Status:** conceptually developed but less mathematically standardized than HJ reachability or Sobol sensitivity.

A constraint such as `g_equity(x) <= threshold` would be a thesis/problem formalization, not a universal Coleman equation.

## VI.3 Pareto optimality

For vector objective `f(d)`, a feasible point `d*` is Pareto optimal if no feasible `d` weakly improves all objectives and strictly improves at least one.

**Status:** mature multiobjective optimization.

---

# Maturity map — what is already populated vs. where integration may be novel

## Mature / already populated

- sector physics and conservation laws;
- graph and multilayer representations;
- infrastructure interdependency taxonomies;
- percolation/cascading failure in interdependent networks;
- hybrid dynamical systems;
- inverse problems and identifiability;
- Bayesian inference / state estimation;
- PINNs;
- UQ/global sensitivity;
- classical resilience curves;
- viability theory;
- HJ/HJI reachability;
- optimal/recovery control;
- restoration scheduling;
- interface/coupling optimization;
- stochastic/multiobjective infrastructure design.

## Narrower integration opportunities identified in this project

1. **Dynamic interface-state physics** rather than treating an interface only as a static edge.
2. **Interface identifiability → uncertainty → viability-geometry uncertainty**.
3. Explicit **physical state → function → critical-service** mapping before resilience evaluation.
4. **Sustainability/equity as admissibility geometry** rather than only final indicators.
5. Coupled **hybrid cascade + viability/reachability + recovery control** analysis for P–W–T–SW under climate stress.
6. Theorem-quality conditions for well-posedness/stability/identifiability of the reduced coupled model before numerical optimization.

# Novelty discipline

A defensible thesis statement should say that existing mathematical theories are being **coupled and specialized** to a new infrastructure problem architecture, rather than claiming those theories themselves were invented here.

A strong wording is:

> The thesis develops and analyzes a coupled hybrid mathematical-physics framework in which dynamic infrastructure interfaces determine hazard propagation and service evolution, sustainability and equity define the admissible state geometry, and viability, reachability and recoverability characterize resilience and feasible recovery.

This wording still requires later PRISMA-based novelty falsification before final publication claims.