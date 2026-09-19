# Stage 6 Intervention-Performance Alignment v2

**Status:** CANONICAL STAGE-6 v2.1 ALIGNMENT RECORD  
**Effective date:** 2026-09-19  
**Controlling authority:** \`project/CANONICAL_INTERVENTION_PERFORMANCE_AMENDMENT_V2_1.md\`  
**Base package:** Stage-6 design/protocol v1  
**Change type:** semantic alignment and explicit intervention-performance typing; no empirical result is changed.

## 1. Alignment decision

The v1 Stage-6 package remains scientifically useful and is retained as provenance. The v2 alignment introduces a missing explicit sequence:

\`\`\`math
\boxed{
\mathfrak R_T
\rightarrow
\mathcal D_R
\rightarrow
a_k
\rightarrow
Y^{a_k}
\rightarrow
\left(
\Delta\mathfrak R^{a_k},
\mathcal E_{\rm fx}^{a_k},
\mathcal E_{\rm fy}^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k}
\right).
}
\`\`\`

The scientific distinctions are:

\`\`\`math
\boxed{
\text{Resilience}
\neq
\text{Effectiveness}
\neq
\text{Efficiency}
\neq
\text{Sustainability}.
}
\`\`\`

## 2. v1 objects preserved

The following v1 objects remain valid:

- strategic intervention \(a_k\);
- \(u(t)\neq a_k\);
- status-quo / BAU counterfactual;
- matched scenario logic;
- intervention physics/feasibility gate;
- functional-service specification \(FU_6\);
- lifecycle/accounting boundary \(\mathcal B_{LC}\);
- core sustainability vector \(\mathbf J_{\rm sus}\);
- requirement provenance classes;
- no-weighting firewall;
- social/accessibility distributional reporting;
- environmental/carbon/cost accounting;
- H4 consequence-heterogeneity concept;
- uncertainty distinction;
- NOT TESTED logic;
- Stage 7 as final decision stage.

## 3. v1 objects retyped

### 3.1 Resilience-effective set

The v1 set

\`\`\`math
\mathcal A_R^+
=
\{a_k:\Delta\mathcal M_R(a_k)\ge\delta_R\}
\`\`\`

is retained as a **resilience-improvement screen**, not the definition of intervention effectiveness.

### 3.2 Resource-efficiency ratios

The v1 diagnostics

\`\`\`math
\eta_{R,m}(a)
=
\frac{\Delta\mathcal M_R(a)}{\Delta R_m(a)}
\`\`\`

remain valid where mathematically admissible, but become components/diagnostics inside the broader efficiency object \(\mathcal E_{\rm fy}\).

## 4. New first-class objects

### 4.1 Effectiveness target object

\`\`\`math
\boxed{
\mathbf T_{\rm fx}^{a_k}
=
\{T_{fx,j}^{a_k}\}_{j=1}^{p_k}
}
\`\`\`

Each target record contains at least:

\`\`\`text
target_id
intervention_id
QOI/service object
direction
threshold or target relation
unit
scenario/aggregation rule
authority/provenance class
uncertainty rule
validation pointer
status
\`\`\`

No target value is invented from observed confirmatory outcomes.

### 4.2 Effectiveness object

\`\`\`math
\boxed{
\mathcal E_{\rm fx}(a_k)
=
\mathcal F_{\rm fx}
(
\text{achieved intervention outcome},
\mathbf T_{\rm fx}^{a_k}
).
}
\`\`\`

Default admissible form is vector/status based. A scalar effectiveness score is optional only if independently justified.

### 4.3 Resource vector

\`\`\`math
\boxed{
\mathbf C_{\rm res}^{a_k}
=
[
C_1^{a_k},\ldots,C_m^{a_k}
]^\top.
}
\`\`\`

Candidate dimensions include cost, implementation time, energy, crew effort, material quantity, land/space, or other evidence-supported engineering resources.

### 4.4 Efficiency object

\`\`\`math
\boxed{
\mathcal E_{\rm fy}(a_k)
=
\mathcal F_{\rm fy}
(
\text{achieved outcome},
\mathbf C_{\rm res}^{a_k}
).
}
\`\`\`

Unless weighting is justified, efficiency remains vectorial / Pareto / ratio-based rather than being forced into one scalar.

## 5. Double-counting firewall

A quantity may appear in both resource-performance and lifecycle consequence analysis only if the two accounting roles are explicit.

\`\`\`math
\boxed{
C_{\rm intervention-resource}
\neq
J_{\rm lifecycle-cost}
\quad\text{by default}.
}
\`\`\`

Every overlapping quantity must declare:

- perspective;
- temporal boundary;
- functional unit;
- included/excluded flows;
- whether it is used as resource input, sustainability consequence, or both;
- double-counting prevention rule.

## 6. Stage-6 v2 output

\`\`\`math
\boxed{
O_6^{v2}
=
(
\Delta\mathfrak R,
\mathcal E_{\rm fx},
\mathcal E_{\rm fy},
\Delta\mathbf J_{\rm sus},
\mathcal K_{\rm sus}^{cand},
\mathbb U_6,
\Lambda_6,
\Pi_6
).
}
\`\`\`

## 7. H4 continuity

The canonical H4 text is not rewritten by this alignment.

H4 remains a test of **material sustainability-consequence heterogeneity among qualified interventions**.

The v2 alignment changes the intervention-performance qualification sequence, not the scientific hypothesis.

## 8. Data firewall

The alignment freezes object definitions and gates only.

It does not freeze:

- actual effectiveness thresholds;
- resource quantities;
- efficiency ratios;
- intervention rankings;
- H4 outcomes.

Those remain DEFERRED until case evidence and confirmatory prerequisites are qualified.
