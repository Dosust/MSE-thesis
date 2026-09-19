# Expert Mathematical Framework Audit — Phase 1: Repository-Only

**Date:** 2026-09-19  
**Scope:** Current `main` repository only; no external literature or standards used in the findings below.  
**Purpose:** Audit the mathematical framework against the repository's own canonical authorities, frozen stage constitutions, handoff contracts, manifests, and global integration controls.

## 1. Governing conclusion

```math
\boxed{
\text{The seven-stage architecture is internally coherent at DESIGN level,
but it is not empirically closed.}
}
```

The repository already enforces the most important scientific firewall:

```math
\boxed{
\text{design closure}
\neq
\text{empirical closure}
\neq
\text{hypothesis support}.
}
```

Current stage status:

| Stage | Design/framework status | Empirical/execution status |
|---|---|---|
| 1 | PASS — FROZEN v2 | case materialization may remain open |
| 2 | PASS — generic framework frozen | ACTIVE case execution; some mechanisms PASS/BLOCKED/FAIL |
| 3 | design v2 frozen | H1 NOT TESTED; runtime/case execution not closed |
| 4 | architecture finalized | G4-CASE/G4-V/G4-H2/G4-TO5 BLOCKED |
| 5 | design finalized | empirical closure NOT CLOSED; Stage6 handoff blocked |
| 6 | design protocol frozen v2 | H4 NOT TESTED |
| 7 | design protocol frozen v2 | H5 NOT TESTED |

## 2. Repository-only stage audit

### Stage 0 / framework input

The canonical repository does not define a separate Stage 0. Critical service requirements are a framework input. This is scientifically cleaner than treating the need statement as another modeling stage.

Required correction to the proposed audit framework: use a pre-stage problem/decision-context object, but do not renumber the canonical seven stages unless the framework authority is formally amended.

Recommended boundary object:

```math
\mathcal B_0=
(\Omega_x,\Omega_t,\Omega_{infra},\Omega_{service},
\Omega_{mode},\Omega_{jur},\mathcal H_\eta,
\mathcal R_{svc},\mathcal I_{use}).
```

The new field `\mathcal I_{use}` should record intended model use / decision context / claim purpose.

### Stage 1 — structure

Repository status: strong and internally controlled.

Strengths:
- structural possibility is explicitly separated from causal qualification;
- entity, geometry, service, authority and provenance semantics are typed;
- topology/proximity/correlation/common cause are explicitly prevented from becoming causal claims;
- structural existence, coupling strength and evidence confidence are separated.

Important correction: the proposed scalar
```math
C_{domain}=N_{audited}/12=1
```
is not the current canonical Stage-1 closure rule. It may remain a descriptive completeness statistic only if all 12 directed P/T/I/O cross-domain classes are explicitly within the audit universe and each is classified. It must not replace the six canonical Stage-1 gates.

### Stage 2 — causality

Repository status: conceptually strong.

The canonical logic correctly separates:
```math
G_2^{causal}
\neq
G_{2\to3}.
```

A mechanism can be causally qualified while still being numerically unready for Stage 3.

The seven G2 components (mechanism, case connection, exchange, activation, evidence, validity, falsification) are coherent as an engineering causal-qualification framework.

Claim ceiling: G2 PASS supports an evidence-grounded directed mechanism within its validity domain. It does not automatically support a statistically identified causal effect magnitude.

### Stage 3 — hybrid multiscale dynamics

Repository status: much stronger than the simplified framework proposed in the audit prompt.

The canonical v2 constitution already allows:
- ODE;
- DAE;
- QSTS;
- network flow;
- CTM/DTA;
- microscopic/mesoscopic transport;
- event-driven and co-simulation realizations.

The physical truth object is:
```math
Y^{phys}=(x_P,x_T,z_{PT}).
```

Information, belief and organizational states are correctly excluded from Stage-3 physical truth.

Required mathematical tightening:
1. make continuous-flow admissibility domains and jump/event domains explicit;
2. avoid symbol collision among graph `\mathcal G`, algebraic constraint map and transition guards;
3. distinguish physical delay from numerical communication step;
4. do not infer that distinct physical timescales automatically require a multirate integrator; this remains a solver/model-selection decision;
5. retain DAE capability because power-system formulations can contain algebraic constraints.

### Stage 4 — knowledge and action

Repository status: strong.

Permanent distinction:
```math
Y^{phys}\neq y\neq\widehat Y\neq b_t.
```

The feasible control set is correctly modeled as:
```math
\mathcal U_{feas}
=
\mathcal U_{phys}
\cap
\mathcal U_{info}
\cap
\mathcal U_{org}
\cap
\mathcal U_{resource}.
```

Required tightening: any control policy used in Stages 4–5 must be explicitly information-adapted / nonanticipative with respect to the available-information history.

### Stage 5 — viability and reachability

Repository status: mathematically promising but contains the most important remaining conceptual risk.

The repository distinguishes:
- deterministic viability;
- robust viability;
- stochastic maintainability;
- stochastic recovery reach-avoid;
- epistemic membership confidence.

However, two state spaces coexist:
1. physical resilience state `x_R=\Pi_R(Y^{phys})`;
2. belief state `b_t`.

The current stochastic sets are naturally belief-space objects, whereas
```math
\rho_{\mathcal V}=d_{g_R}(x_R,\partial\mathcal V)
```
is a physical-state-space expression.

**C1 correction:** explicitly define separate objects:
```math
\mathcal V_T^x\subseteq\mathcal X_R,
\qquad
\mathcal V_{\alpha,T}^b\subseteq\mathcal B,
```
and never compute a physical-state distance to a belief-space boundary.

A second C1 correction is that admissible policies must be explicitly nonanticipative.

A third C1 correction: the proposed derivative
```math
-\partial\rho_\mathcal V/\partial w_{ij}
```
does not align cleanly with the current canonical dependency ontology because `w_{ij}` is not the canonical Stage-2 executable dependency object. Interface criticality should instead perturb a qualified mechanism parameter/operator or use ablation/finite-difference/global-sensitivity analysis.

Recovery should also distinguish first entry from sustained recovery. A dwell or persistence condition is recommended.

### Stage 6 — intervention performance and sustainability

The simplified audit prompt is outdated relative to current repository authority.

Canonical Stage 6 is not merely:
```math
R_{out}\to S_{req}.
```

It is:
```math
\mathfrak R_T
\to\mathcal D_R
\to a_k
\to\mathfrak M^{a_k}
\to Y^{a_k}
\to
(\Delta\mathfrak R,
\mathcal E_{fx},
\mathcal E_{fy},
\Delta\mathbf J_{sus})
\to\mathcal K_{sus}^{cand}.
```

The repository correctly separates:
```math
\text{resilience}
\neq
\text{effectiveness}
\neq
\text{efficiency}
\neq
\text{sustainability}.
```

Any mathematical framework figure must use this current Stage-6 structure.

### Stage 7 — engineering decision

The weighted-sum objective proposed in the audit prompt is not the current canonical default and should not be shown as the main Stage-7 equation.

Canonical sequence:
```math
\boxed{
\text{feasibility}
\to
\text{native-unit objectives}
\to
\text{Pareto dominance}
\to
\text{robustness/regret}
\to
\text{preference model only if justified}.
}
```

No weights may be invented. A unique optimum is conditional on a legitimate value model.

## 3. Cross-stage handoff audit

The repository itself identifies and controls three integration defects:

### D1 — Stage-1/Stage-2 notation collision
```math
\gamma_e^{S1,int}\neq\gamma_e^{S2,act},
\qquad
\Phi_e^{S1,exch}\neq\Phi_e^{S2,op}.
```
Status: controlled by global notation normalization.

### D2 — Stage-4→5 physical-truth lineage
Stage 4's exact output does not itself carry the physical truth needed by `x_R=\Pi_R(Y^{phys})`.
Status: controlled by companion physical-provenance carrier `\Pi_{phys}^{3:5}`.

### D3 — Stage-5→6 tuple mismatch
Producer and consumer tuples are not identical.
Status: controlled by a lossless normalized carrier `I_{5\to6}^{norm}`.

These are design-level PASS only under the normalization layer. They do not imply empirical readiness.

## 4. Mathematical redundancy / collision audit

The major collisions currently controlled or requiring control are:
- Stage-1 versus Stage-2 `\gamma_e`;
- Stage-1 versus Stage-2 `\Phi_e`;
- Stage-1 state-schema `Y` versus Stage-3 physical truth `Y^{phys}`;
- graph `\mathcal G` versus potential use of `G` for algebraic or guard objects;
- operational control `u(t)` versus strategic intervention `a_k`.

## 5. Missing mathematics before empirical closure

The strongest missing/unfinished case-level mathematics are:
- Stage-2 parameter-ready mechanism realizations;
- Stage-3 exact flow/jump admissibility domains and case solver choices;
- frozen case-specific QOI metrics and references;
- Stage-4 validated observation/estimation realization;
- Stage-5 explicit physical-space versus belief-space viability semantics;
- nonanticipative policy class;
- rigorous interface-sensitivity operator;
- sustained-recovery definition;
- case-specific sustainability inventories/functional units;
- Stage-7 preference/value model only if a unique decision is required.

## 6. Computational feasibility

Likely dominant computational bottleneck:
```math
\text{high-dimensional hybrid P--T state}
+
\text{uncertainty}
+
\text{viability/reachability}
+
\text{optimization}.
```

The repository's resilience projection `x_R=\Pi_R(Y^{phys})` is therefore essential, but it must be justified as information-preserving for the Stage-5 question.

A full viability kernel over the native microscopic SUMO × OpenDSS state is not a defensible default computational target.

## 7. Repository-only correction priorities

| ID | Severity | Correction |
|---|---|---|
| R1 | C1 | Separate physical-state and belief-space viability/reachability objects. |
| R2 | C1 | Make Stage-5 policies explicitly nonanticipative/information-adapted. |
| R3 | C1 | Replace `\partial\rho/\partial w_{ij}` as canonical interface criticality unless a differentiable canonical strength parameter is actually defined. |
| R4 | C1 | Replace simplified Stage-6 sustainability mapping with current intervention-performance-sustainability chain. |
| R5 | C1 | Remove weighted-sum Stage-7 optimum as default; use feasibility/Pareto/robustness/value firewall. |
| R6 | C2 | Make Stage-3 flow/jump domains explicit and disambiguate guard/algebraic/graph notation. |
| R7 | C2 | Treat `C_domain=1` only as optional coverage diagnostic, not Stage-1 closure gate. |
| R8 | C2 | Define sustained recovery, not merely first hitting time, where service restoration requires persistence. |
| R9 | C2 | Add intended-use/model-use context to the pre-stage scientific boundary. |
| R10 | C3 | Normalize all framework figures to current global symbol registry. |

## 8. Repository-only decision

```math
\boxed{
G_{framework}^{internal}
=
PASS\;WITH\;MAJOR\;CORRECTIONS
}
```

Interpretation: the architecture is scientifically coherent enough to continue, but the simplified mathematical-chain figure/prompt is not yet canonical and should not be frozen until R1–R6 are incorporated.

This decision does not alter H1–H5, which remain governed by their existing empirical gates.
