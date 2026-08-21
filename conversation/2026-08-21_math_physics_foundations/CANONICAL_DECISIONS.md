# Canonical Decisions and Freeze Status — 2026-08-21

This file records what changed during the session, what should currently be treated as frozen working architecture, and what remains provisional.

## A. Decisions to retain

### D1 — Theory first, application second

**Decision:** the mathematical development should begin with an abstract coupled physical system, not with named infrastructure sectors.

Preferred progression:

\[
\boxed{\text{mathematics}\to\text{mathematical physics}\to\text{sustainable resilient systems theory}\to\text{infrastructure instantiation}\to\text{engineering decision}.}
\]

**Why:** this makes the thesis potentially reusable across multiple engineering domains and forces the foundational assumptions, state spaces, dynamics, uncertainty, and viability concepts to be defined before domain-specific details are inserted.

### D2 — Keep the six-chain ontology

The six chains remain the organizing scientific ontology:

1. Physical system
2. Observation–inference–prediction
3. Hazard–failure–consequence
4. Viability–resilience–recovery–control
5. Engineering action / lifecycle
6. Sustainability–evaluation–decision

These chains are coupled and recursive, not a single chronology.

### D3 — Optimization is cross-cutting

Do not restore “Optimization” as a standalone lifecycle stage. Optimization/OR acts on design, operations, maintenance, recovery, planning, adaptation, decision, and computation.

### D4 — Viability is a central geometric object

The thesis should not be organized around one scalar resilience index. A central object is the sustainable/equitable admissible set and its viability/recovery geometry:

\[
\mathcal K_{\mathrm{SER}}=\mathcal K_{\mathrm{phys}}\cap\mathcal K_{\mathrm{service}}\cap\mathcal K_{\mathrm{sus}}\cap\mathcal K_{\mathrm{eq}},
\]

\[
\mathcal V_{\mathrm{SER}}=\operatorname{Viab}(\mathcal K_{\mathrm{SER}}).
\]

Candidate derived objects include \(\partial\mathcal V\), reachable sets, capture/recovery sets, recovery time, viable control sets, and viability margins.

### D5 — Interfaces are more than graph edges

Maintain

\[
\boxed{\text{connection}\neq\text{interdependency}\neq\text{interface mechanism}.}
\]

Dynamic interface operators/states should be explicit whenever the physics supports them.

### D6 — State, functionality, service, and consequence must be separated

Do not collapse the chain into a single performance quantity.

\[
\boxed{X\to F_{\mathrm{func}}\to S_g\to C_g.}
\]

A damaged component, a nonfunctional component, a degraded service, and a human consequence are distinct mathematical/physical objects.

### D7 — Sustainability and equity can define admissibility

Do not treat sustainability/equity only as weighted objective terms. Where scientifically and normatively justified, they can define hard constraints in \(\mathcal K\).

### D8 — Add well-posedness before resilience analysis

Before using a forward model for inference, resilience, optimization, or AI, investigate conditions for:

\[
\boxed{\text{existence}\to\text{uniqueness}\to\text{physical admissibility}\to\text{stability}\to\text{continuous dependence}.}
\]

### D9 — Add observability before identifiability

Chain II should distinguish:

\[
\boxed{\text{Observe}\to\text{Observability}\to\text{Identify}\to\text{Identifiability}\to\text{Estimate}\to\text{UQ}\to\text{Predict}.}
\]

### D10 — Separate uncertainty types

At minimum distinguish:

- aleatory uncertainty,
- epistemic/parameter uncertainty,
- structural/model-form uncertainty,
- decision/scenario uncertainty.

### D11 — Lifecycle must include end-of-life

For a genuinely whole-life mathematical framework, extend engineering action beyond adaptation to include replacement/transformation, decommissioning, reuse, recycling, and circularity.

### D12 — Multi-timescale control is necessary

Fast control, operations, restoration, maintenance, planning, and adaptation should not be forced onto one timescale.

### D13 — Verification and validation are separate

- **Verification:** did we solve the mathematical model correctly?
- **Validation:** is the mathematical model an adequate representation of reality for the declared purpose?

### D14 — AI is cross-cutting and must not replace known physics by default

Preferred doctrine:

\[
\boxed{\text{AI learns}\to\text{physics constrains}\to\text{UQ quantifies}\to\text{formal mathematics certifies where feasible}.}
\]

### D15 — Visual figures should show mathematics, not boxes describing mathematics

The Wolfram-inspired scientific-visualization direction is preferred over conventional card/infographic layouts.

---

## B. Current preferred title hierarchy

### Preferred theory-first title

**Mathematical Physics of Sustainable Resilient Systems: Foundations and Applications to Infrastructure**

### More domain-explicit alternative

**Mathematical Physics of Sustainable Resilient Infrastructure: From Fundamental Dynamics to Viability and Lifecycle Decision**

### Long-term research-program label

**Mathematical Foundations for Sustainable and Resilient Infrastructure Systems**

The title remains provisional until thesis scope and contribution are formally frozen with supervisory constraints.

---

## C. Current preferred one-sentence research program

> **Develop a mathematical-physics theory for the observation, evolution, sustainable viability, disturbance response, recovery, and lifecycle control of dynamically coupled physical systems under uncertainty, and instantiate the theory for resilient infrastructure.**

---

## D. Thesis-size versus program-size distinction

### Master's thesis candidate

The most defensible thesis-sized bridge remains:

\[
\boxed{\text{observed dynamic interfaces}\to\text{identification uncertainty}\to\text{service viability uncertainty}.}
\]

### PhD/research-program scale

A broader theory could integrate:

- structure-preserving physics,
- stochastic hybrid dynamics,
- dynamic interfaces,
- inverse problems,
- viability/reachability,
- safe control,
- lifecycle optimization,
- scientific AI.

Do not force the entire long-term program into one master's thesis.

---

## E. Claims explicitly rejected or narrowed

Do not claim:

- “interdependencies have not been studied”;
- “service mapping does not exist”;
- “recovery coupling has not been modeled”;
- “HJ reachability has never been applied to infrastructure”;
- “resilience has not been mathematically modeled”;
- “the first digital twin for infrastructure resilience” without evidence;
- “unique solution” without specifying trajectory, inverse solution, optimizer, or HJ viscosity solution.

Recent literature discussed during the session already narrows several of these broad claims.

---

## F. Current theorem ladder for a complete theory

A long-term theory may seek results of the following forms:

1. **T1 — Existence**
2. **T2 — Uniqueness**
3. **T3 — Positivity / physical admissibility / invariance**
4. **T4 — Stability / dissipativity**
5. **T5 — Observability**
6. **T6 — Identifiability**
7. **T7 — Posterior consistency / uncertainty bound**
8. **T8 — Viability existence / nonemptiness**
9. **T9 — Viability-boundary sensitivity**
10. **T10 — Recoverability / capture**
11. **T11 — Existence of safe control**
12. **T12 — Existence/structure of optimal policy/design**

This is a research-program ladder, not a commitment to prove all twelve in the master's thesis.

---

## G. What remains provisional

The following must not yet be treated as frozen final results:

- exact state dimension;
- exact PDE/ODE/DAE choice for the abstract theory;
- whether Port-Hamiltonian structure becomes core or comparison;
- exact stochastic/hybrid formulation;
- exact service and equity constraints;
- exact interface-identification data set;
- exact demonstrator sectors/city/hazard;
- final theorem set;
- final PRISMA corpus and novelty statements;
- final numerical method for high-dimensional viability;
- final AI method, if any;
- exact final thesis title.
