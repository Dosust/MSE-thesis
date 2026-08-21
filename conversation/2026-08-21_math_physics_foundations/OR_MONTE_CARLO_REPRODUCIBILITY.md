# Operations Research + 10,000,000-Draw Monte Carlo Reproducibility

## 1. Methodological separation

The session explicitly separated deterministic Operations Research from Monte Carlo uncertainty analysis:

\[
\boxed{\text{Monte Carlo}\neq\text{optimization}.}
\]

The uploaded IEE 574 Applied Deterministic Operations Research material was used conceptually as the deterministic backbone:

- mathematical modeling,
- linear programming,
- duality,
- sensitivity analysis,
- integer programming,
- branch-and-bound,
- cutting planes,
- network flows,
- nonlinear programming.

Monte Carlo was placed around the deterministic model to test sensitivity to uncertain evidence scores and criterion weights.

---

## 2. Concept-ranking model

For concept \(i\) and Monte Carlo realization \(r\):

\[
\boxed{S_i^{(r)}={w^{(r)}}^\top s_i^{(r)}}.
\]

Ten criterion families were used in the later 19-concept analysis:

1. industrial maturity,
2. real-world evidence,
3. human value,
4. mathematical rigor,
5. formal guarantees,
6. AI leverage,
7. SDG impact,
8. cross-sector relevance,
9. data readiness,
10. scientific novelty.

Central weights used in the recorded implementation:

\[
w_0=(0.12,0.10,0.14,0.14,0.10,0.10,0.10,0.06,0.05,0.09).
\]

Weights were sampled from a Dirichlet distribution around the central vector. Evidence scores were also perturbed, with greater uncertainty assigned to concepts with weaker real-world evidence/data readiness.

The simulation used:

\[
\boxed{N=10,000,000}
\]

and fixed seed:

`57420260821`

The results are model-conditional decision-analysis outputs, **not empirical probabilities that a technology will dominate the future**.

---

## 3. Main balanced-ranking result recorded in session

Top concepts by mean balanced score included:

1. Sustainable AI + data-center energy-water co-optimization
2. AI climate/Earth observation & hazard intelligence
3. Cyber-physical multi-infrastructure digital twins
4. Safe RL / MPC for power grids
5. AI algorithm discovery / evolutionary optimization
6. Physics-informed machine learning
7. DRL/MPC for water & wastewater
8. Deep-uncertainty adaptation / real options
9. Dynamic interface identification + Bayesian UQ

Hamilton–Jacobi viability/reachability scored lower under balanced industrial/deployment criteria because formal rigor and present industrial scalability are different objectives.

---

## 4. Objective-dependent ranking

A major conclusion was:

\[
\boxed{\text{Most industrially mature}\neq\text{most mathematically rigorous}\neq\text{highest sustainability value}\neq\text{best research frontier}.}
\]

Under a **high-rigor mathematical frontier weighting**, the leading concepts were approximately:

1. Dynamic interface identification + Bayesian UQ
2. Hamilton–Jacobi viability/reachability
3. Multi-agent distributed infrastructure control
4. Sustainable AI/data-center co-optimization
5. Physics-informed ML
6. Deep-uncertainty adaptation
7. Safe RL/MPC
8. Equity-aware robust planning

This is the ranking most relevant to the thesis research frontier, but it remains conditional on the encoded score matrix and weighting model.

---

## 5. 0–1 portfolio optimization

For concept selection:

\[
x_i\in\{0,1\}.
\]

The portfolio model used the generic structure

\[
\boxed{\max_x\sum_iV_ix_i}
\]

subject to a complexity/resource budget

\[
\sum_ic_ix_i\le B,
\]

cardinality

\[
\sum_ix_i=K,
\]

and coverage constraints requiring representation of formal safety, interface inference, human/sustainability outcomes, AI/scientific-computing acceleration, and cross-system coupling.

Under the recorded high-rigor scenario with \(K=5\) and budget \(B=24\), the exact portfolio selected:

1. Dynamic interface identification + Bayesian UQ
2. People-centric service resilience
3. Hamilton–Jacobi viability/reachability
4. Physics-informed machine learning
5. Deep-uncertainty adaptation / real options

Recorded objective value:

\[
\boxed{438.10}.
\]

---

## 6. LP relaxation / shadow-price insight

The LP relaxation indicated that the research-complexity budget was binding. The local shadow price was approximately

\[
\boxed{\lambda_B\approx1.97}
\]

objective points per additional budget unit while the current LP basis remained valid.

This is an example of how duality/sensitivity adds information beyond rankings.

---

## 7. Budget sensitivity recorded in session

| Budget | Optimal objective |
|---:|---:|
| 20 | 411.09 |
| 21 | 419.59 |
| 22 | 427.89 |
| 23 | 434.55 |
| 24 | 438.10 |
| 25 | 439.18 |
| 26 | 441.13 |
| 27 | 441.13 |
| 28 | 442.89 |
| 29 | 442.89 |
| 30 | 442.89 |

Interpretation: within this encoded model, marginal value rises strongly up to the low/mid-20s and then largely saturates.

---

## 8. Reproducibility rules

Any future rerun should record:

- code commit SHA,
- concept list/version,
- criterion definitions,
- evidence-score matrix,
- uncertainty model,
- central weights,
- Dirichlet concentration,
- seed,
- number of draws,
- portfolio constraints,
- solver/version,
- objective definition,
- sensitivity scenarios.

Never report “10 million runs prove X.” Correct phrasing is:

> “Under the declared evidence-coded decision model and uncertainty assumptions, the ranking/portfolio was robust across 10,000,000 simulated draws.”

Executable/session snapshots are stored in the `reproducibility/` subfolder.
