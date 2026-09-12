# Phase 0F — Field and Layer Ablation Protocol

**Status:** PREREGISTERED BEFORE 0F RESULT INTERPRETATION  
**Purpose:** determine which dependency components are primitive, derived, conditional, or optional without changing ontology, physics, evidence, or service definitions.

---

## 1. Controlled scientific question

What is the minimum dependency representation that preserves `K1–K8` across frozen dependencies `D1–D4`?

The experiment changes only the dependency representation.

The following are fixed:

```text
ontology M0={P,T,I,O};
dependency fact sets D1–D4;
domain physics F_P,F_T;
service maps G_k;
evidence sources;
source and receiver entities;
mechanism truth statements.
```

---

## 2. Competing candidates

### Candidate A — monolithic tuple

```math
\mathfrak d_e=(s,r,\rho,m,q,M,z,w,\delta,c,U,\mathcal H).
```

### Candidate B — layered object

```math
\mathfrak D_e=(\mathcal C_e,\Sigma_e,\Pi_e,\Xi_e).
```

No candidate receives additional facts unavailable to the other.

---

## 3. Classification rule for every field/layer

For component `x`, assign exactly one primary status:

### Primitive

`x` is primitive if removing it causes at least one frozen capability/fact to become unrecoverable and there is no preregistered deterministic derivation from the remaining representation plus globally frozen system maps.

### Derived

`x` is derived if there exists a fixed map

```math
x=\psi_x(R\setminus\{x\},Y^*,\Theta^*)
```

that reconstructs it without case-specific rules.

### Conditional primitive

`x` is conditionally primitive if it is necessary only for a defined class of dependencies, e.g. relations with autonomous internal state or non-Markovian memory.

### Optional metadata

`x` may improve indexing, reporting, implementation traceability or human interpretation but is not required to preserve `K1–K8` under the frozen test fixture.

---

## 4. Sufficiency criterion

For candidate representation `R`, define

```math
Suff(R)=1
```

iff for every `D_i`, all `K1–K8` are either:

1. represented directly in `R`; or
2. uniquely recoverable through a globally frozen, non-case-specific derivation/realization/service map.

Otherwise

```math
Suff(R)=0.
```

This distinction prevents duplication of system-level knowledge inside every edge.

---

## 5. Semantic loss

For dependency fact set `F_e`, define

```math
L_{sem}(R,e)
=
1-
\frac{|Rec_R(F_e)|}{|F_e|}.
```

A minimum sufficient representation requires

```math
L_{sem}(R,e)=0
```

for all frozen dependencies.

---

## 6. Ambiguity

Let `kappa_R(r)` be the number of admissible factual reconstructions of encoded relation `r`.

```math
E_{amb}(R,e)
=
\sum_r\log_2\!\left(\max(1,\kappa_R(r))\right).
```

The target is

```math
E_{amb}=0.
```

---

## 7. Ad-hoc complexity

```math
N_{adhoc}(R,e)
=
\text{number of case-specific exceptions, hidden fields, duplicated entities or new rules required after the freeze}.
```

Any representation requiring `N_adhoc>0` to rescue a frozen case is not minimal under v1.0.

---

## 8. Complexity vector

Use component-wise complexity only:

```math
C(R)=
(
N_{stored},
N_{independent},
N_{conditional},
N_{derived},
N_{external\ maps},
N_{adhoc}
).
```

No arbitrary scalar complexity weighting is allowed.

---

## 9. Redundancy

For representations with comparable stored components,

```math
R_{red}
=
\frac{N_{stored}-N_{independent}}{N_{stored}}.
```

Because fields and layers have different semantic granularity, cross-candidate comparison of `R_red` is allowed only after normalizing what counts as one independent semantic unit.

A conservative lower bound may be reported when only some redundancies are mathematically guaranteed.

---

## 10. Engineering-value vector

Do not collapse value to one score.

For each ablated component `x`, define

```math
\Delta \mathbf V_x
=
(\Delta V_E,\Delta V_I,\Delta V_P,\Delta V_D),
```

where:

```text
V_E = explanatory capability;
V_I = identification/traceability capability;
V_P = prediction-readiness;
V_D = engineering-decision relevance.
```

A component whose removal changes none of these and does not increase `L_sem`, `E_amb`, or `N_adhoc` is not retained as a mandatory core primitive.

---

## 11. Two complementary ablation procedures

### A. Forward construction

Start with

```math
A_0=(s,r)
```

and progressively add mechanism, carrier/type, dynamics, timing and evidence semantics.

Forward construction is diagnostic only because incremental value depends on field order.

### B. Leave-one-out necessity test

For full candidate `R` and component `x`, compute

```math
R^{-x}=R\setminus\{x\}.
```

`x` is necessary iff there exists at least one frozen dependency/capability for which removal causes:

```math
L_{sem}(R^{-x},e)>0
```

or

```math
E_{amb}(R^{-x},e)>0
```

or loss of one of `K1–K8` without a globally frozen derivation.

The leave-one-out result has priority over order-dependent forward gain.

---

## 12. Allowed global maps

Minimality is assessed at the **dependency-contract** level, so system-wide functions need not be duplicated on each relation.

Three globally fixed maps are permitted:

### Service map

```math
Q(t)=G(Y(t)).
```

Hence relation service consequence is traced as

```math
\Delta d_e
\rightarrow
\Delta \dot X_r
\rightarrow
\Delta X
\rightarrow
\Delta Q.
```

### Realization map

```math
\mathcal X:\Sigma_e\mapsto\Xi_e
```

maps formal dependency semantics to an executable implementation/equation/model interface when such a map is uniquely specified.

### Classification map

```math
\mathcal R_{class}: (\mathcal C_e,\Sigma_e)\mapsto\rho_e
```

may assign a reporting class such as physical, informational/control, or organizational/authority after the mechanism has been specified.

These maps must be fixed globally; they may not be invented separately to rescue one dependency case.

---

## 13. Primitive-vs-derived tests preregistered

The following derivations are permitted only if their mathematical conditions hold:

### Structural existence

For an actual dependency set `E`,

```math
M_e=\mathbf 1_{\{e\in E\}}.
```

Thus storing `M_e` on every actual relation is potentially redundant. A potential-edge/supergraph study may require a separate admissibility variable.

### Activation

If activation is governed by a context guard `gamma_e`,

```math
a_e(t)=\mathbf 1_{\{\gamma_e(Y,h,u,t)\ge0\}}.
```

Activation is then derived from the guard rather than an independent primitive.

### Dynamic influence strength

When differentiable and after a norm/metric is declared,

```math
w_e(t)=\left\|D_{x_s}\Phi_e\right\|.
```

For non-smooth systems, a finite-difference, gain, reachability or other explicitly defined influence measure may replace the derivative.

Therefore a generic scalar `w_e` is not automatically primitive.

### Delay/history

A delayed relation may be represented by an operator on a history segment:

```math
\Phi_e:
X_s^{[t-\bar\delta,t]}
\times X_r(t)
\rightarrow
\Delta F_r(t).
```

An explicit `delta_e` remains necessary information if the actual delay must be identified/estimated, but it need not remain a top-level field if it is a typed parameter of the mechanism operator.

---

## 14. Candidate-decision rule

0F returns one of:

```text
MONOLITHIC OBJECT SUFFICIENT;
LAYERED OBJECT SUFFICIENT;
HYBRID MINIMUM OBJECT REQUIRED.
```

Use:

- **MONOLITHIC** only if the tuple is sufficient and no layered refactoring materially reduces redundancy/ambiguity while preserving `K1–K8`.
- **LAYERED** only if `(C,Sigma,Pi,Xi)` is already minimum sufficient as declared.
- **HYBRID** if the evidence supports a smaller/refined object that absorbs or derives parts of both candidates.

This is not the final ontology decision. `RETAIN/REVISE/REPLACE` remains reserved for 0G.

---

## 15. Validity boundary

This protocol tests structural/mathematical sufficiency on four representative dependencies. It does not prove universal minimality over every possible infrastructure relation class.
