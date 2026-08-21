# Core Research Gap, Frozen MSE Propositions, and Novelty Discipline

## 1. Controlling distinction

This file is corrected to align with the frozen MSE research design v0.5.

The controlling thesis contribution is not a broad claim that service mapping, recovery coupling, dynamic interfaces, or Hamilton–Jacobi viability are individually absent from the literature. The thesis instead formalizes and tests a coupled infrastructure problem in which **safe recovery reachability** and **post-recovery controlled viability** are distinct objects under evolving service/sustainability/equity/resource/hazard constraints.

Executable MSE system:

\[
\boxed{X(t)=[X_P(t),X_T(t),X_W(t)]^T}
\]

General extensible architecture may add Solid Waste and other sectors.

## 2. Frozen formal objects

Hybrid physical/interface state:

\[
\chi(t)=(X(t),Z(t),m(t)),\qquad Z_{ij}(t)\neq Z_{ji}(t)\ \text{in general}.
\]

Augmented state including service deprivation/cumulative burdens:

\[
\widetilde\chi(t)=(\chi(t),D_1,\ldots,D_G,C,E).
\]

Hard safety set:

\[
\boxed{K_{hard}(t)=\{\widetilde\chi:h_q(\widetilde\chi,t)\le0\}}
\]

Acceptable recovery region:

\[
\boxed{K_R(t)=\{\widetilde\chi:g_k(\widetilde\chi,t)\le0\}}
\]

Post-recovery viable target:

\[
\boxed{K_R^V(t)=\operatorname{Viab}(K_R)(t)}
\]

Safe recovery/capture basin:

\[
\boxed{B_R(t_0)=\operatorname{Capt}_{K_{hard}}(K_R^V)(t_0)}
\]

The formal novelty must preserve:

\[
\boxed{K_{hard}\neq K_R,\qquad B_R\neq K_R^V.}
\]

## 3. Refined literature frontier

Recent work discussed in the conversation already narrows broad absence claims:
- people-centric service mappings for interdependent infrastructures exist;
- time-varying recovery coupling has been modelled;
- HJ/HJBI viability has been demonstrated in at least constrained single-sector infrastructure settings;
- AI/physics-informed/operator models provide powerful sector-specific estimation and surrogate tools.

Therefore the thesis should claim novelty only for the **specific formal composition and tested decision consequences** it can establish.

## 4. Strong complementary inverse-problem bridge

A strong thesis subproblem or follow-on contribution remains:

\[
D_{obs}
\rightarrow
p(Z_{ij}(t),\theta_{ij}\mid D_{obs})
\rightarrow
p(X(t))
\rightarrow
p(S_g(t))
\rightarrow
p(K_R,K_R^V,B_R).
\]

One possible inverse-model error metric is

\[
E_{inv}=d_H[\mathcal V(\theta^*),\mathcal V(\widehat\theta)],
\]

or an analogous boundary/classification error for \(B_R\) and \(K_R^V\).

**Status:** strong candidate bridge, not a replacement for the frozen v0.5 core unless the user explicitly re-freezes the thesis around it.

## 5. Frozen falsifiable hypothesis family

### H1 — Dynamic interface effect
Explicit time-varying directional interfaces materially change recovery-feasibility classifications relative to independent or static-coupling baselines.

Primary outputs may include recovery-basin/viability classification, service loss and repair feasibility.

### H2 — Delay and information effect
Observation latency and administrative/decision delay reduce the recovery basin or increase required intervention under otherwise identical physical damage.

### H3 — Resource/admissibility effect
Usable finance/resource constraints remove trajectories that unconstrained restoration would classify as feasible.

### H4 — Equity/service effect
Aggregate recovery can coexist with unacceptable subgroup deprivation; explicit group service floors change admissible and viable sets.

### H5 — Tractability effect
A reduced/decomposed representation preserves principal recovery/viability classifications within a predeclared tolerance while materially reducing computation.

A failure to confirm any hypothesis remains scientifically meaningful.

## 6. Core experiments

- **E1 Interface dynamics:** independent/fixed coupling vs dynamic directional \(Z_{ij}(t)\).
- **E2 Delay/observation:** immediate information/authorization vs observation and administrative lag.
- **E3 Finance/resource:** unrestricted restoration vs available/nominal liquidity and timing constraints.
- **E4 Equity/service:** aggregate objective vs group-specific service floors.
- **E5 Reduction/scalability:** full executable reference vs reduced/decomposed model, only after stable baseline implementation.

## 7. Minimum structural enhancement

A finite-perturbation baseline for recoverability criticality:

\[
C_{ij}(\delta)=\frac{M(B_R^{\alpha})-M(B_R^{\alpha+\delta e_{ij}})}{\delta}.
\]

Minimum enhancement:

\[
\boxed{\alpha^*=\arg\min_{\alpha\in\mathcal A}C_\alpha(\alpha)
\quad\text{s.t.}\quad
\widetilde\chi_0\in B_R^\alpha(t_0)}
\]

This is not ordinary graph centrality; it is a decision problem defined through recoverability geometry.

## 8. Theorem-quality ambition

Where possible, establish conditions for:

\[
\boxed{
\text{Model Definition}
\to
\text{Well-Posedness}
\to
\text{Existence}
\to
\text{Uniqueness}
\to
\text{Stability}
\to
\text{Sensitivity}
\to
\text{Identifiability}
\to
\text{Computability}
\to
\text{Validation}
}
\]

"Uniqueness" must always name the mathematical object: trajectory, inverse parameter, optimizer, control law, reachable-set/value-function solution, or another explicitly defined object.

## 9. Claim discipline

Use formulations such as:
- "the framework distinguishes safe recovery reachability from maintainable post-recovery viability";
- "the MSE demonstrator instantiates P–T–W while the mathematical architecture is extensible";
- "physics-informed learning may incorporate governing equations or invariants and must still be verified";
- "reduced reachability/decomposition is accepted only if classification/boundary fidelity criteria pass."

Avoid:
- "recovery and resilience are the same set";
- "the thesis validates a complete P–T–W–SW operational system";
- "physics-informed means physically correct";
- "HJ reachability solves the full high-dimensional infrastructure problem";
- "one recent paper proves the field lacks this method."

## 10. Novelty gate

A novelty claim is admissible only when it has:
1. systematic literature evidence with counterevidence search;
2. a precisely defined mathematical relation/object;
3. an executable implementation or formal derivation;
4. a falsification/verification test;
5. an explicit limitation and scope statement.
