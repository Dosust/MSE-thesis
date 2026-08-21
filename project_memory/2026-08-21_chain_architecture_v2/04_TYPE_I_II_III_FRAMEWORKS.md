# Type I, II and III Thesis Frameworks — Corrected v2

These are three **alternative full-chain research philosophies**. They are not three simultaneous thesis requirements.

## Type I — Theory-First Mathematical Physics

### Core question

**What is mathematically possible?**

### Full research chain

```text
physical laws
→ coupled representation
→ interface mechanisms
→ coupled/hybrid dynamics
→ admissibility
→ viability/reachability
→ recovery/capture geometry
→ admissible control
→ design implications
→ decision implications
```

Compact mapping:

```text
(theta,eta) → X(t) → V_R → C_R → u → d
```

### Best fit for the current MSE

This is the strongest central identity because the authoritative scope already centers the thesis on dynamic coupling, viability and recovery geometry.

### Originality should concentrate on

- dynamic interfaces rather than generic interdependency alone;
- interface-identification reliability and viability sensitivity;
- sustainable/equitable admissibility;
- viability-boundary deformation;
- recovery/capture geometry;
- possibly interface criticality based on viability deformation.

### Risk

Trying to prove new theory at every downstream design/decision stage would make the MSE too broad.

### Image

`assets/frameworks/type_i_theory_first_framework.webp`

---

## Type II — Inference-to-Decision / Digital-Twin Direction

### Core question

**What is happening, what will happen, and what should be done now?**

### Full research chain

```text
physical system + sensing
→ observations
→ observability / inverse identification
→ state + parameter/interface estimation
→ uncertainty quantification
→ dynamic predictive model
→ forecast
→ probabilistic/uncertain viability
→ adaptive recovery control
→ adaptive design/decision
```

Compact mapping:

```text
D → p(X,theta,Z|D) → p(V_R|D) → u_t
```

### Correct terminology rule

A model should be called a **digital twin** only if the implemented system actually contains a defensible data-to-model update loop and the relevant calibration/update/validation machinery. A synthetic model scaffold alone is not an operational digital twin.

### Best contribution zone

- dynamic interface identification;
- state/parameter uncertainty;
- propagation of posterior uncertainty into viability/recovery geometry;
- adaptive control under partial observation.

### Risk

A full operational digital twin may exceed the current data and implementation scope.

### Image

`assets/frameworks/type_ii_digital_twin_framework.webp`

---

## Type III — Resilience-by-Design

### Core question

**What should be built so acceptable behavior remains possible?**

### Full research chain

```text
service / performance requirements
→ hazard scenarios
→ candidate designs
→ design-dependent coupled dynamics
→ admissibility
→ viability/recovery constraints
→ control feasibility
→ sustainability/equity constraints
→ robust/multiobjective optimization
→ investment / planning decision
```

Compact mapping:

```text
d → F_d → V_R(d) → C_R(d) → d*
```

### Best contribution zone

- viability as a design constraint;
- recoverability as a design constraint;
- robust design under climate/interface uncertainty;
- sustainability/equity constraints inside the feasible design set.

### Risk

If `V_R` and `C_R` are reduced to one scalar objective without preserving their geometry/constraint meaning, the study can become a conventional optimization thesis and lose the distinctive mathematical contribution.

### Image

`assets/frameworks/type_iii_resilience_by_design_framework.webp`

---

# Relationship among the three

Long-term research program:

```text
Type I: UNDERSTAND / PROVE WHAT IS POSSIBLE
→ Type II: INFER / PREDICT / ADAPT
→ Type III: DESIGN / OPTIMIZE / DECIDE
```

## Current MSE recommendation

The corrected recommendation is:

```text
Type-I-centered core
+ Type-II upstream identification/UQ
+ limited Type-III downstream demonstration if feasible
```

This aligns with `project/THESIS_SCOPE.md`, which explicitly says the MSE does not require an original contribution at every downstream layer simultaneously.

## Generated graphics already committed

Folder: `assets/frameworks/`

- `type_i_theory_first_framework.webp`
- `type_ii_digital_twin_framework.webp`
- `type_iii_resilience_by_design_framework.webp`
- `framework_comparison_all_types.webp`
- `README.md`
- `SHA256SUMS.txt`

The v2 memory does not claim that those graphics themselves validate any scientific hypothesis.