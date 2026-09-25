# Three Coupled Frameworks for the Seven-Stage Thesis — v1.0

**Canonical thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**  
**Title authority:** `CANONICAL_THESIS_TITLE_V1.md`

**Status:** SUPPORTING SYNTHESIS — NON-CANONICAL  
**Date:** 2026-09-24  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Authority:** Derived from `CANONICAL_7_STAGE_FRAMEWORK_V2_1_ALIGNMENT_AMENDMENT.md`, `CANONICAL_RESEARCH_QUESTIONS_V4.md`, and `CANONICAL_RQ_SO_HYPOTHESES_V4.md`.  
**Purpose:** Provide a compact, professional, systems-engineering grouping of the seven canonical stages without changing their scientific meaning.

---

## 1. Governing architecture

```math
\boxed{
\underbrace{S_1\leftrightarrow S_2}_{\text{Framework I}}
\rightarrow
\underbrace{S_3\leftrightarrow S_4\leftrightarrow S_5}_{\text{Framework II}}
\rightarrow
\underbrace{S_6\leftrightarrow S_7}_{\text{Framework III}}
}
```

The bidirectional arrows denote iterative scientific co-development inside a framework. They do **not** collapse distinct stage responsibilities.

The canonical seven-stage order remains:

```text
Spatiotemporal SoS Structure
→ Evidence-Qualified Directional Dependencies
→ Complex Spatiotemporal Coupled Dynamics
→ Observation / Estimation / Organization / Feasible Control
→ Uncertainty-Aware Spatiotemporal Service Resilience
→ Targeted Intervention Consequences
→ Defensible Engineering Decision
```

---

# Framework I — Structural–Mechanistic Qualification

```math
\boxed{S_1\leftrightarrow S_2}
```

**Question:** What exists, where/when can interaction occur, and which candidate relations are qualified directional mechanisms?

### Input

```math
I_I=
\left(
Q_P,Q_T,
\Omega_{sys}^{+},
D_{raw},
\Pi
\right)
```

### Transform

```math
\mathcal S_{PT}
\rightarrow
\mathfrak G_{PT}(x,t)
\rightarrow
\mathcal I^{cand}
\rightarrow
\mathcal I^{qualified}
\rightarrow
\mathcal I^{ready}
```

Stage 1 establishes **structural possibility**. Stage 2 performs **mechanism qualification**.

Permanent firewalls:

```math
\boxed{
\text{co-location}\neq\text{dependency},
\quad
\text{association}\neq\text{causality},
\quad
P\to T\not\Rightarrow T\to P,
\quad
\text{causal qualification}\neq\text{dynamic readiness}.
}
```

### Output

```math
O_I=
\left(
\mathcal S_{PT},
\mathfrak G_{PT}(x,t),
\mathcal I^{ready},
\Theta,
\Delta,
\Omega
\right)
```

---

# Framework II — Dynamic–Operational Resilience

```math
\boxed{S_3\leftrightarrow S_4\leftrightarrow S_5}
```

**Question:** How does the coupled physical system evolve, what can operators know and feasibly do, and can critical services remain acceptable or recover?

### Input

```math
I_{II}=
\left(
\mathfrak G_{PT},
\mathcal I^{ready},
Y_0^{phys},
\eta,
u^{exo},
\Theta
\right)
```

### Transform A — Stage 3: Physical dynamics

```math
\boxed{
Y_3^{phys}(t)=
\left(
x_P(t),x_T(t),z_{PT}(t)
\right)
}
```

```math
\dot x=F_{\mathcal G}^{m}(x,z,u,\eta;\Theta),
\qquad
0=G_{\mathcal G}^{m}(x,z,u,\eta;\Theta)
```

with justified hybrid reset/mode/topology operators.

### Transform B — Stage 4: Knowledge and feasible action

```math
\boxed{
Y
\rightarrow y
\rightarrow \widehat Y
\rightarrow (I,O)
\rightarrow \mathcal U_{feas}
\rightarrow u
}
```

### Transform C — Stage 5: Service resilience

```math
\boxed{
\text{Resilience}
=
\text{Remain (viability)}
+
\text{Return (reachability)}
+
\Gamma_U
}
```

with

```math
\mathcal V
=
\{Y_0:\exists u(\cdot),Y(t)\in K\},
```

```math
\mathcal R_T
=
\{Y_0:\exists u(\cdot),Y(\tau)\in G_{rec}\},
```

and, where defined,

```math
\rho_{\mathcal V}(Y)=d(Y,\partial\mathcal V).
```

### Output

```math
O_{II}
=
\left(
Y(t),
Q(t),
\widehat Y(t),
\mathcal U_{feas},
\mathcal V,
\mathcal R,
\rho_{\mathcal V},
\Gamma_U
\right)
```

### Internal dependency

```math
\boxed{
\mathcal V
=
\mathcal V
\left(
F_{\mathcal G},
\mathcal U_{feas},
K,
\Gamma_U
\right)
}
```

Therefore Stages 3–5 must mature together: physics constrains estimation/control, and feasible control changes viability and recovery.

---

# Framework III — Intervention–Decision Engineering

```math
\boxed{S_6\leftrightarrow S_7}
```

**Question:** What engineering changes alter resilience, resource use and admitted sustainability consequences, and which alternatives remain defensible?

### Input

```math
I_{III}
=
\left(
\mathcal V,
\mathcal R,
\rho_{\mathcal V},
\Gamma_U,
\mathcal A_{cand}
\right)
```

### Transform A — Stage 6: Intervention consequences

For intervention

```math
a_k=
(\text{type},\text{location},\text{timing},\text{scale},\text{resources}),
```

evaluate

```math
\mathfrak M
\xrightarrow{a_k}
\mathfrak M^{a_k}
\rightarrow
\mathcal C(a_k).
```

Canonical consequence object:

```math
\boxed{
\mathcal C(a_k)=
\left(
\Delta\mathfrak R^{a_k},
\mathbf r^{a_k},
\mathcal E_{fx}^{a_k},
\mathcal E_{fy}^{a_k},
\Delta\mathbf J_{sus}^{a_k},
\mathcal F^{a_k},
\mathbf U^{a_k}
\right)
}
```

Permanent distinction:

```math
\boxed{
\text{resilience effect}
\neq
\text{effectiveness}
\neq
\text{resource requirement}
\neq
\text{resource efficiency}
\neq
\text{admitted sustainability consequence}.
}
```

### Transform B — Stage 7: Defensible decision

```math
\boxed{
\text{feasibility}
\rightarrow
\text{native-unit criteria}
\rightarrow
\text{Pareto/dominance}
\rightarrow
\text{robustness/regret}
\rightarrow
\text{preference/value model only if justified}
}
```

### Output

```math
O_{III}
=
\mathcal A_{joint}^{\star}
```

where `defensible` does not imply one universally optimal alternative.

---

# Cross-cutting credibility layer

The three frameworks are governed by:

```math
\boxed{
\text{Evidence}
+
\text{Provenance}
+
\text{Identification}
+
\text{Verification}
+
\text{Validation}
+
\text{Uncertainty Quantification}
+
\text{Falsification}
+
\text{Reproducibility}
}
```

The model-credibility lifecycle is:

```math
\boxed{
\text{Reality}
\rightarrow
\text{Model}
\rightarrow
\text{Verify}
\rightarrow
\text{Calibrate}
\rightarrow
\text{Validate}
\rightarrow
\text{Falsify}
\rightarrow
\text{Quantify uncertainty}
\rightarrow
\text{Test viability}
\rightarrow
\text{Decide robustly}
\rightarrow
\text{Observe again}
}
```

A model is not treated as universally correct. It is admitted only for a declared context of use, quantity of interest, validity domain and evidence base.

```math
\boxed{
M
\overset{?}{\text{adequate}}
(Q,\Omega,D,E)
}
```

---

# Input → Transform → Output summary

```text
FRAMEWORK I
INPUT      critical services + system boundary + evidence
TRANSFORM  structure → candidate interfaces → qualified/ready mechanisms
OUTPUT     graph + dynamically ready dependencies

FRAMEWORK II
INPUT      graph + ready mechanisms + initial state + disturbance
TRANSFORM  physical dynamics → observation/estimation/control → viability/reachability
OUTPUT     trajectories + feasible controls + resilience state

FRAMEWORK III
INPUT      resilience diagnosis + candidate interventions
TRANSFORM  intervention consequences → feasibility → Pareto → robustness/regret
OUTPUT     defensible intervention set
```

---

# Visual grammar for publication figure

Use a clean left-to-right landscape composition.

- **Framework I:** Light Sky Blue / neutral cool tone.
- **Framework II:** deeper blue / navy emphasis because it is the physical-mathematical core.
- **Framework III:** light blue with stronger outline; no gold.
- **Inputs:** circles/spheres.
- **Transforms:** rectangles / cuboids.
- **Qualification or decision gates:** diamonds.
- **Synthesis/output:** pyramidal or trapezoidal forms only when they encode narrowing/aggregation.
- **Inter-framework handoff:** thick solid arrows.
- **Within-framework iteration:** bidirectional arrows.
- **Cross-cutting credibility:** continuous bottom band across all three frameworks.
- Avoid decorative shapes that do not encode scientific meaning.

Official accent palette:

```text
Light Sky Blue  RGB(135,206,250)  #87CEFA
Deep Sky Blue   RGB(0,191,255)    #00BFFF
Charcoal / Navy / White for structure and contrast
NO GOLD
```

---

## Scientific status

This file is a communication and synthesis artifact. It **does not supersede** the canonical seven-stage framework, RQ/SO/H authority, Stage-1 freeze, Stage-3 constitution, or Stage-6/7 governance.

The seven stages remain the scientific authority; the three-framework grouping is a higher-level systems-engineering organization for manuscript communication, visualization and computational workflow design.
