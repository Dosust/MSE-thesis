# Thesis Master Outline

**Status:** CURRENT DOCUMENT ARCHITECTURE / NOT ALL CHAPTER CONTENT FROZEN  
**Degree:** MSE Sustainable Engineering  
**Scientific method:** EGMIV

## Governing principle

```math
\boxed{
\text{Problem}
\rightarrow\text{Evidence/Theory}
\rightarrow\text{Framework}
\rightarrow\text{Method}
\rightarrow\text{Results}
\rightarrow\text{Discussion}
\rightarrow\text{Conclusion}.
}
```

The seven scientific stages belong primarily in Chapter 3 and are operationalized in Chapter 4. They are not the chapter structure.

---

# Preliminary matter

1. Title Page
2. Copyright page — optional
3. Abstract — maximum 350 words; ASU abstract rules apply
4. Dedication — optional
5. Acknowledgments
6. Table of Contents
7. List of Tables
8. List of Figures
9. List of Symbols / Abbreviations — if used
10. Preface — optional

---

# Chapter 1 — Introduction

## 1.1 Background and engineering context
- infrastructure interdependence;
- power–transportation coupling;
- role of information and organization;
- resilience and sustainability motivation.

## 1.2 Problem statement
State the unresolved engineering/scientific problem without claiming an unverified gap.

## 1.3 Significance to sustainable engineering
Connect technical behavior to long-term service, robustness, environmental, social, economic and institutional performance.

## 1.4 Scope and system boundary
Declare included/excluded infrastructure domains, layers, hazards, timescales, controls and validity limits.

## 1.5 Research aim
One overarching aim, stated as a testable research program rather than a result.

## 1.6 Research questions
Map RQ0 and subquestions to the framework and hypotheses.

## 1.7 Research objectives
Each objective must be verifiable and linked to an RQ and a thesis deliverable.

## 1.8 Hypotheses
Introduce `H_SYS` and `H1–H5` without results.

## 1.9 Proposed contributions
Label as proposed/expected until validated.

## 1.10 Thesis organization
Explain chapter logic.

### Chapter 1 gate

```math
\boxed{
\text{Problem}\rightarrow\text{Gap}\rightarrow\text{RQ}\rightarrow\text{Objective}\rightarrow\text{Hypothesis}
}
```

Pass only if every important claim is evidence-conditioned and every hypothesis has a mechanism.

---

# Chapter 2 — Literature Review and Theoretical Foundations

## 2.1 Systems and systems-of-systems theory
## 2.2 Infrastructure dependency and interdependency
## 2.3 Multilayer / network-of-networks representations
## 2.4 Power-system foundations relevant to coupling
## 2.5 Transportation-system foundations relevant to coupling
## 2.6 Power–transportation coupling literature
## 2.7 Information/cyber dependencies
## 2.8 Organizational/institutional dependencies
## 2.9 Dynamic, cascading and recovery models
## 2.10 Observation, estimation, communication and control
## 2.11 Viability, invariance and reachability
## 2.12 Resilience and sustainability
## 2.13 Adaptive/transformative pathways under uncertainty
## 2.14 Critical synthesis and intersection gap

For each subsection `Q` construct:

```math
\boxed{\mathcal E_Q=(E_Q^+,E_Q^-,A_Q,M_Q,V_Q,U_Q,G_Q)}
```

with supporting evidence, contrary evidence, assumptions, methods, validation evidence, uncertainty/limitations and remaining gap.

### Chapter 2 gate

Pass only if:
- search protocol executed for the declared question;
- screening/eligibility documented;
- evidence extracted;
- contrary/rival evidence included;
- gap supported rather than asserted;
- references verified;
- literature synthesis distinguishes `[E]` from `[U/H/P]`.

---

# Chapter 3 — Conceptual and Mathematical Framework

## 3.1 Definitions and notation
## 3.2 Constituent infrastructure-system representation
## 3.3 Physical–informational–organizational ontology
## 3.4 Primitive directed dependency
## 3.5 Interdependency composition
## 3.6 Dynamic dependency/interdependency structure
## 3.7 Multilayer graph and graph-to-dynamics mapping
## 3.8 Seven-stage framework
### 3.8.1 Multilayer Structure
### 3.8.2 Causal Mechanisms
### 3.8.3 Coupled Hybrid Multiscale Dynamics
### 3.8.4 Observation, Organization, Feedback and Control
### 3.8.5 Controlled Sustainable Viability
### 3.8.6 Resilience-to-Sustainability Transformation Interface
### 3.8.7 Sustainable Transformation Pathways
## 3.9 Stage-to-stage mathematical handoffs
## 3.10 Theoretical propositions and expected implications

Framework derivation must follow:

```math
\boxed{
\text{Definitions}
\rightarrow\mathfrak d_{ij}
\rightarrow\mathfrak I_{ij}
\rightarrow\mathcal G_{\mathfrak I}(t)
\rightarrow F_{\mathcal G}
\rightarrow\text{control}
\rightarrow\mathcal V
\rightarrow\text{criticality}
\rightarrow\text{transformation}.
}
```

### Chapter 3 gate

Pass only if:
- all symbols defined;
- units and domains declared where applicable;
- assumptions explicit;
- established theory separated from proposed constructs;
- every arrow has mathematical/engineering meaning;
- dimensional/logical consistency checked;
- no equation is introduced solely for visual sophistication.

---

# Chapter 4 — Methodology and Experimental Design

## 4.1 EGMIV research method
## 4.2 Evidence-search and qualification strategy
## 4.3 Data provenance and qualification
## 4.4 Minimal sufficient experimental realization
## 4.5 H1 — dynamic interdependency experiment
## 4.6 H2 — information/organization experiment
## 4.7 H3 — controlled-viability experiment
## 4.8 H4 — interface-criticality experiment
## 4.9 H5 — adaptive-transformation experiment
## 4.10 Verification plan
## 4.11 Validation plan
## 4.12 Uncertainty quantification and sensitivity
## 4.13 Statistical/decision rules and falsification
## 4.14 Reproducibility and computational environment

For each hypothesis:

```math
\boxed{
\mathcal T_i=(H_i,M_i,B_i,\Omega_i,D_i,\theta_i,Z_i,\delta_i,\mathcal F_i)
}
```

where the hypothesis, model, baseline, domain, data, parameters, responses, decision threshold and falsification condition are declared before confirmatory execution.

### Chapter 4 gate

Pass only if:
- baselines frozen;
- scenario/test domain frozen;
- data split/qualification frozen;
- parameters have provenance;
- decision criteria fixed a priori;
- V&V and UQ plans frozen;
- falsification criteria explicit;
- calibration and validation separated.

---

# Chapter 5 — Results

## 5.1 H1 results
## 5.2 H2 results
## 5.3 H3 results
## 5.4 H4 results
## 5.5 H5 results
## 5.6 Cross-hypothesis robustness/sensitivity results

One-to-one mapping is required:

```math
\boxed{\text{Chapter 4 experiment}\longleftrightarrow\text{Chapter 5 result}.}
```

Each result should expose:

```math
\text{experiment}\rightarrow\text{estimate}\rightarrow\text{uncertainty}\rightarrow\text{threshold}\rightarrow\text{decision}.
```

### Chapter 5 gate

Pass only if:
- no result lacks a preregistered method or documented exploratory status;
- uncertainty reported;
- null/negative outcomes retained;
- no causal language exceeds design support;
- results not inflated into discussion claims.

---

# Chapter 6 — Discussion and Sustainable Engineering Implications

## 6.1 Summary of hypothesis outcomes
## 6.2 Mechanistic interpretation
## 6.3 Comparison with prior literature
## 6.4 Implications for infrastructure-system representation
## 6.5 Implications for resilience engineering
## 6.6 Sustainability implications
## 6.7 Engineering decision implications
## 6.8 Transferability/generalization limits
## 6.9 Limitations
## 6.10 Remaining uncertainty and unresolved questions

Required discussion questions:

```math
\boxed{
\begin{aligned}
&\text{What mechanism was demonstrated?}\\
&\text{Under what conditions?}\\
&\text{With what uncertainty?}\\
&\text{What engineering decision changes?}\\
&\text{What remains unvalidated?}
\end{aligned}}
```

---

# Chapter 7 — Conclusions and Future Work

## 7.1 Answers to research questions
## 7.2 Supported/rejected hypotheses
## 7.3 Theoretical contribution
## 7.4 Methodological contribution
## 7.5 Sustainable-engineering contribution
## 7.6 Practical engineering contribution
## 7.7 Limits of generalization
## 7.8 Future work

### Chapter 7 gate

Every conclusion must trace to a result and admissible evidence. No proposed contribution may be presented as demonstrated unless its validation chain closes.

---

# Back matter

- Notes — if used
- References
- Appendices
- Biographical sketch — optional under ASU rules

Recommended appendices include:
- search protocols and search records;
- screening/eligibility rules;
- FTEE extraction details;
- model equations and parameter tables;
- V&V/UQ audits;
- supplementary results;
- code/data provenance;
- approvals/permissions if applicable.
