# Thesis Frozen State — Research Design v0.5

**Authority:** this file is a memory reconstruction anchored to the library artifact `Dossiya_Dakou_MSE_Thesis_Frontier_Integrated_Research_Design_v0.5.pdf` (Research Design Revision v0.5, 19 Aug 2026). It supersedes looser conversation summaries when they conflict with the frozen v0.5 design.

## 1. Working title and executable thesis scope

**Title family:** Mathematical Physics of Sustainable Infrastructure Resilience.

**v0.5 subtitle:** *Equity-Constrained Viability of Dynamic Power-Transport-Water Interfaces under Climate Stress*.

### Executable MSE core

\[
\boxed{X(t)=[X_P(t),X_T(t),X_W(t)]^T}
\]

### General extensible architecture

\[
\boxed{X_{ext}(t)=[X_P(t),X_T(t),X_W(t),X_{SW}(t),\ldots]^T}
\]

Solid Waste is retained as an extension interface, not promised as a validated four-sector executable MSE system.

## 2. Frozen contribution

Develop and test a mathematical framework that distinguishes **safe recovery reachability** from **post-recovery controlled viability** in dynamically coupled urban infrastructure, where the acceptable recovery region evolves with service, sustainability, equity, interface, institutional, financial/resource, and hazard conditions.

This is the defensible mathematical contribution. AI, Earth observation and digital twins are enabling technologies, not the core thesis object.

## 3. Hybrid coupled state

Directional interfaces are distinct:

\[
Z_{ij}(t)\neq Z_{ji}(t)\quad\text{in general}.
\]

They may encode capacity, availability, accessibility, reliability, delay, efficiency, health or restoration status.

A discrete mode captures operating/degraded/failed/isolated/restored configurations:

\[
\chi(t)=(X(t),Z(t),m(t)).
\]

Representative dynamics:

\[
\dot X_i=F_i(X_i,u_i,\eta;\theta_i)+\sum_{j\ne i}C_{ij}(X_i,X_j,Z_{ij},\eta,u;\theta_{ij}),
\]

\[
\dot Z_{ij}=G_{ij}(X_i,X_j,Z_{ij},\eta,u;\theta_{ij}),
\qquad
m^+=\Delta(m^-,X,Z,u,\eta).
\]

## 4. Observation and representation layer

Observation:

\[
Y_i(t)=H_i(X(t),\eta(t))+\varepsilon_i(t).
\]

Representation/state estimation may use engineered or learned features:

\[
e_t=E_\theta(Y_{1:t},c_t),
\]

\[
p(X_t,\eta_t\mid e_{1:t},Y_{1:t})
\quad\text{or}\quad
\widehat X_t=\Phi(e_{1:t},Y_{1:t}).
\]

A learned representation is not automatically a physical state. Annual Earth-observation embeddings are treated primarily as slow contextual covariates/spatial priors unless a validated fast-time mapping is supplied.

## 5. Population service and augmented state

For group or service class \(g\):

\[
S_g(t)=\Psi_g(\chi(t),d_g(t)).
\]

Deprivation accumulation:

\[
\dot D_g(t)=[S_g^{\min}(t)-S_g(t)]_+.
\]

Cumulative cost and environmental burden can be state variables:

\[
\dot C(t)=c(\chi,u,\alpha),\qquad
\dot E(t)=e(\chi,u,\alpha).
\]

Augmented state:

\[
\widetilde\chi(t)=(\chi(t),D_1,\ldots,D_G,C,E).
\]

## 6. Hard safety, recovery admissibility, viability and capture

Hard constraints:

\[
\boxed{K_{hard}(t)=\{\widetilde\chi:h_q(\widetilde\chi,t)\le0,\ q=1,\ldots,n_h\}}
\]

Acceptable recovery region:

\[
\boxed{K_R(t)=\{\widetilde\chi:g_k(\widetilde\chi,t)\le0,\ k=1,\ldots,n_R\}}
\]

The two sets are distinct. `K_hard` contains constraints that may not be violated during recovery; `K_R` represents time-dependent acceptable service/sustainability/equity/resource recovery requirements.

Viability target:

\[
\boxed{K_R^V(t)=\operatorname{Viab}(K_R)(t)}
\]

Safe recovery/capture basin:

\[
\boxed{B_R(t_0)=\operatorname{Capt}_{K_{hard}}(K_R^V)(t_0)}
\]

Hence:

\[
\boxed{\text{safe recovery reachability}\neq\text{maintainable post-recovery viability}.}
\]

## 7. Minimum structural enhancement

A finite perturbation interface-criticality baseline can be written as

\[
C_{ij}(\delta)=\frac{M(B_R^{\alpha})-M(B_R^{\alpha+\delta e_{ij}})}{\delta}.
\]

Minimum enhancement:

\[
\boxed{\alpha^*=\arg\min_{\alpha\in\mathcal A}C_\alpha(\alpha)
\quad\text{s.t.}\quad
\widetilde\chi_0\in B_R^\alpha(t_0)}
\]

Recoverability criticality is therefore not ordinary graph centrality.

## 8. Main research question

Which disturbed states of a dynamically coupled power-transport-water system can be controlled back into an evolving acceptable service region without violating hard constraints, and which recovered states can then remain viable under continued climate disturbance and uncertainty?

## 9. Frozen falsifiable hypotheses

### H1 — Dynamic interface effect
Explicit time-varying directional interfaces materially change recovery-feasibility classifications relative to independent or static-coupling baselines.

### H2 — Delay and information effect
Observation latency and administrative/decision delay reduce the recovery set or increase required intervention under otherwise identical physical damage.

### H3 — Resource/admissibility effect
Usable liquidity/resource constraints remove trajectories that unconstrained restoration would classify as feasible.

### H4 — Equity/service effect
Aggregate recovery can coexist with unacceptable subgroup deprivation; explicit group service floors change admissible and viable sets.

### H5 — Tractability effect
A reduced/decomposed representation preserves principal recovery/viability classifications within a predeclared tolerance while materially reducing computational cost.

Failure to confirm a hypothesis remains scientifically useful; model complexity must be justified by measurable classification/decision effects.

## 10. Core falsification experiments

- **E1 Interface dynamics:** independent/fixed coupling vs dynamic directional \(Z_{ij}(t)\).
- **E2 Delay/observation:** immediate information/authorization vs observation and administrative lag.
- **E3 Finance/resource:** unrestricted restoration vs available/nominal liquidity and timing constraints.
- **E4 Equity/service:** aggregate objective vs group-specific minimum service floors.
- **E5 Reduction/scalability:** highest-fidelity executable reference vs reduced/decomposed state/interface model, only after stable baseline implementation.

## 11. Implementation sequence

1. Freeze notation and research-question/hypothesis ledger before adding equations.
2. Recode systematic-review corpus using frontier fields and quantify evidence paths.
3. Implement the P–T–W synthetic/geospatially anchored testbed and physical residual checks before learned surrogates.
4. Implement and unit-test `K_hard` and `K_R` as distinct code objects.
5. Validate the smallest tractable reachability/viability solver on an analytic or toy benchmark first.
6. Run E1–E4; add E5 only when a fidelity tolerance can be declared meaningfully.
7. Add Earth-observation or physics-AI surrogates only after the physics baseline passes conservation/OOD/extreme-event checks.
8. Populate final results only from immutable run artifacts passing claim-to-code traceability.

## 12. Required work products

- PRISMA systematic review with explicit counterevidence to novelty claims.
- Frozen notation/assumptions document including units, dimensions, interface semantics and uncertainty sets.
- Executable P–T–W testbed with reproducible configuration and deterministic seeds where appropriate.
- Unit/integration tests for conservation, interface directionality, causal/non-anticipative control, admissibility semantics and traceability.
- Core falsification experiments with declared metrics/tolerances.
- Results ledger linking every claim to evidence, model version, code commit/hash, run configuration, test status and figure/table.

## 13. AI/digital-twin position

The thesis is **not** presented as an operational digital twin or as an AI forecasting system. It develops a formal mathematical-physics framework for coupled infrastructure recoverability and viability. Digital-twin, EO and physics-AI methods are evaluated as enabling observation, estimation, surrogate and scenario technologies when their physical semantics, temporal resolution, uncertainty and validation are adequate.

## 14. Binding scope guards

Do not promise in the MSE:
- an operational city digital twin;
- a live utility deployment;
- a validated national four-sector system;
- a universal foundation model;
- an end-to-end AI controller;
- formal certification of real infrastructure safety.

## 15. Final freeze criterion

A main thesis claim is ready to freeze only when it has all five:

1. literature-supported rationale;
2. mathematically defined object;
3. executable code representation;
4. verification/falsification test;
5. explicit limitation.

Anything missing one of these remains provisional.
