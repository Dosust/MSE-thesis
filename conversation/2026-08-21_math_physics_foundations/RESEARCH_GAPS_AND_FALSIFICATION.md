# Research Gaps, Industrial Gaps, and Falsification Rules

This file preserves the gap logic developed during the session. It is intentionally conservative: broad novelty claims were narrowed whenever newer literature supplied counterexamples.

## 1. Real-world / industrial gap families

The broad evidence scan identified recurring practice problems around:

1. preventive resilience finance,
2. implementation/enforcement of standards and plans,
3. technical and institutional capacity,
4. high-quality local risk data,
5. fragmented operational data and interoperability,
6. cross-sector dependency/interface visibility,
7. service/user consequence modeling,
8. cybersecurity and trust in connected infrastructure,
9. climate nonstationarity and multi-hazard readiness,
10. aging assets and condition uncertainty,
11. recovery coordination under scarce resources.

For the mathematical-physics thesis, the most relevant practice gap is not necessarily the most frequently reported one. The strongest interface with the thesis is:

> **Operators often know dependencies exist but do not possess sufficiently trusted, dynamic, cross-system measurements to quantify their operational coupling and propagate that uncertainty into formal service-safety decisions.**

---

## 2. Scientific gap families

Recurring scientific gaps discussed in the session include:

- dynamic/time-varying interdependencies and interfaces,
- empirical identification/calibration/validation of coupling,
- uncertainty quantification and propagation,
- benchmark/validation data and interoperability,
- human, institutional, logical and service dependencies,
- scalable formal viability/reachability,
- physics-consistent multi-system coupling,
- state → functionality → service → consequence mapping,
- compound/multi-hazard models,
- recovery under dynamic uncertainty/scarce resources,
- long-term adaptation/nonstationarity,
- equity/procedural-justice integration,
- solid-waste coupling within broader interdependent systems.

These are not all equally novel. Some are mature fields with open subproblems; others are narrower integration gaps.

---

## 3. Gap claims that were explicitly narrowed

### Service mapping

Broad claim rejected:

> “Multi-infrastructure models lack service-state mapping.”

Reason: recent people-centric resilience work, including Zhang et al. (2026), explicitly maps multi-system operation to population/service states and demonstrates that performance-centric formulations can misrepresent affected populations.

Revised gap:

> Service-oriented mappings are becoming stronger, but they are still weakly integrated with empirically identified dynamic coupling uncertainty and formal sustainable/equitable viability guarantees.

### Dynamic recovery coupling

Broad claim rejected:

> “Dynamic recovery coupling has not been modeled.”

Reason: Jiang et al. (2026) introduced time-varying recovery coupling/cascading structures and GNN-guided recovery optimization.

Revised gap:

> The harder issue is whether dynamic failure/recovery couplings are **identified/calibrated from operational observations** and whether their epistemic uncertainty is propagated into formal service-level viability/recovery guarantees.

### Hamilton–Jacobi reachability

Broad claim rejected:

> “HJ reachability has never been applied to infrastructure.”

Reason: HJ/reachability has infrastructure applications, and a 2026 Waste-to-Energy study explicitly uses constrained HJBI viability under uncertain waste inflow.

Revised gap:

> The frontier is the scalable integration of formal viability/reachability with empirically inferred multi-system interfaces, uncertainty, service consequences, and lifecycle control.

---

## 4. Strongest current candidate gap

The strongest current formulation is:

\[
\boxed{
\begin{aligned}
&\text{Dynamic failure/recovery couplings and people-centric service mappings are increasingly modeled,}\\
&\textbf{but empirically identified dynamic coupling uncertainty remains weakly connected}\\
&\textbf{to sustainable/equitable service-level viability boundaries and formal recovery/control guarantees.}
\end{aligned}}
\]

Candidate end-to-end bridge:

\[
\boxed{
D_{obs}
\to p(Z_{ij}(t),\theta_{ij}\mid D_{obs})
\to p(X(t))
\to p(S_g(t))
\to p(\mathcal V_{SER})
\to \text{safe recovery/control}.
}
\]

This is a **candidate gap to falsify**, not a global novelty theorem.

---

## 5. Candidate research propositions

### P1 — Dynamic interface effect

Dynamic interfaces materially deform the viable region relative to static coupling:

\[
\Delta_{\mathcal V}=d_H(\mathcal V_{dynamic},\mathcal V_{static}).
\]

### P2 — Interface-identification uncertainty

Interface/parameter estimation uncertainty materially changes the inferred viability geometry:

\[
E_{inv}=d_H[\mathcal V(\theta^\star),\mathcal V(\widehat\theta)].
\]

### P3 — Timescale-separation validity

Static interface approximations are valid only in specified regimes of

\[
\rho_{ij}=\frac{\tau_{interface,ij}}{\tau_{system}}.
\]

### P4 — Sustainability/equity deformation

Adding sustainability and equity constraints changes viable geometry relative to purely technical constraints:

\[
\mathcal V(K_{tech})\neq\mathcal V(K_{SER}).
\]

### P5 — Recovery adds information beyond viability

\[
\mathcal C_R\setminus\mathcal V_R
\]

contains states that are not presently viable but are formally recoverable.

### P6 — Waste/drainage/flood feedback

Where physically justified, endogenous material/waste blockage can alter realized hazard and shift viability/recovery geometry.

### P7 — Reduced models must preserve decision-relevant geometry

A reduced model should either preserve or conservatively bound the full-order viability/recovery conclusions used for decisions.

---

## 6. Falsification protocol

For each candidate gap/proposition:

1. **Define the exact claim.** Avoid “no one has done X” unless exhaustive evidence supports it.
2. **Search synonyms and neighboring fields.** E.g., interface/coupling/dependency/interaction; viability/safe set/invariance/reachability.
3. **Separate general mathematics from application novelty.** HJ theory can be mature while a specific application bridge remains sparse.
4. **Record counterexamples.** A paper that closes part of the gap should narrow the claim rather than be ignored.
5. **Track evidence status.** Proposed relation vs literature-supported relation vs theorem-level implication.
6. **Prefer missing-edge claims.** E.g. \(p(\theta\mid D)\to p(\mathcal V)\) rather than claiming entire fields are absent.
7. **Check data realism.** A mathematically elegant gap is not useful if the required variables cannot be observed or bounded.
8. **Check thesis feasibility.** Distinguish master's-sized proof/computation from PhD-scale program.

---

## 7. Literature maturity map

Current working maturity classification:

| Area | Working assessment |
|---|---|
| Infrastructure interdependency taxonomy | Very mature |
| Multilayer/network representation | Very mature |
| Cascading-network failure | Very mature |
| Classical resilience metrics | Very mature |
| Restoration optimization | Very mature |
| Viability/HJ reachability as general mathematics | Very mature |
| Inverse problems as general mathematics | Very mature |
| Equity metrics in resilience | Growing / mature in parts |
| Dynamic interface identification | Much narrower |
| Interface-identification uncertainty → viability boundaries | Much narrower |
| Sustainability/equity as hard viability constraints | Narrower integration |
| Capture/recovery geometry for multi-system coupling | Narrower |
| Waste–drainage–flood feedback within viability analysis | Narrower combined problem |

The thesis should seek novelty in **specific mathematical coupling**, not ownership of mature fields.
