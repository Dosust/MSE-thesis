# Thesis Page Budget and Compression Architecture — 160 Pages v1.0

**Status:** FROZEN WORKING DOCUMENT-CONTROL SPECIFICATION  
**Date:** 2026-09-16  
**Degree:** MSE Sustainable Engineering — CEE 599 Thesis  
**University:** Arizona State University  
**Scientific method:** EGMIV  
**Framework authority:** `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**RQ–SO–H authority:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**ASU control specification:** `ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md`  
**Master outline:** `THESIS_MASTER_OUTLINE.md`

> **Scope rule:** ASU does not impose a 160-page thesis requirement. The 160-page limit is an internal thesis scope-control decision adopted to force scientific density, remove repetition, and keep the CEE 599 manuscript proportionate to a rigorous MSE thesis. University/program requirements always override this internal page target if a conflict arises.

---

## 1. Fixed total-page constraint

The complete submitted manuscript is planned under

```math
\boxed{
P_{\mathrm{total}}
=
P_{\mathrm{prelim}}
+
P_{1:7}
+
P_{\mathrm{references}}
+
P_{\mathrm{appendices}}
=160.
}
```

The 160-page target is a **hard planning cap**, not a scientific target. No scientific claim may be weakened, unsupported, or omitted merely to meet the cap; compression must first remove redundancy, generic exposition, duplicated equations, low-value visuals, and supplementary material from the main body.

### Frozen page allocation

| Thesis component | Page budget |
|---|---:|
| Preliminary matter | **8** |
| Chapter 1 — Introduction | **10** |
| Chapter 2 — Literature Review and Scientific Foundations | **20** |
| Chapter 3 — Conceptual and Mathematical Framework | **30** |
| Chapter 4 — Research Methodology and Experimental Design | **26** |
| Chapter 5 — Results | **24** |
| Chapter 6 — Discussion and Sustainable Engineering Implications | **15** |
| Chapter 7 — Conclusions and Future Research | **6** |
| References | **11** |
| Appendices | **10** |
| **TOTAL** | **160** |

Thus the scientific main body is controlled to

```math
\boxed{
P_{1:7}=131\ \text{pages}.
}
```

---

## 2. Governing compression principle

```math
\boxed{
\textbf{Remove repetition, not science.}
}
```

Priority order for compression is

```math
\boxed{
\text{duplicate prose}
\rightarrow
\text{generic textbook exposition}
\rightarrow
\text{duplicate equations}
\rightarrow
\text{micro-headings}
\rightarrow
\text{low-information visuals}
\rightarrow
\text{supplementary detail moved to appendix/repository}.
}
```

The following must **not** be removed to save pages:

1. the canonical seven-stage framework;
2. Power–Transportation bidirectional physics and coupling;
3. Information and Organization layers required by H2;
4. the frozen H1–H5 hypothesis architecture;
5. H1 comparators `M0`, `M1`, `M2`;
6. H3 state semantics `K`, `D`, `F`, `G_rec`, `T_V`, `T_R`;
7. viability + reachability + uncertainty/probability;
8. conventional resilience-curve comparator;
9. matched intervention logic for H4;
10. sustainability consequences required for the Sustainable Engineering contribution;
11. resilience-only versus joint resilience–sustainability decision comparison for H5;
12. verification, validation, uncertainty quantification, sensitivity, and falsification;
13. RQ–SO–H–experiment–result–conclusion traceability;
14. assumptions, validity domain, and negative/null findings.

---

## 3. Chapter 1 — Introduction — 10 pages maximum

### Final structure

1.1 Background and Engineering Context  
1.2 Problem Statement and Research Gap  
1.3 Sustainable Engineering Significance  
1.4 Scope, Boundaries, and Assumptions  
1.5 Research Aim, Questions, and Objectives  
1.6 Research Hypotheses  
1.7 Proposed Contributions  
1.8 Thesis Organization

### Compression rule

- Merge general infrastructure background with coupled Power–Transportation context.
- Merge problem statement and research gap while preserving the distinction between an engineering problem and a literature-derived gap.
- Present `RQ0 + RQ1–RQ7` and `SO1–SO7` in one traceability table rather than separate mini-sections.
- Present `H1–H5` in one compact hypothesis table with comparator, primary metric family, and falsification path.
- Keep contributions explicitly **proposed** until validated.

### Required chapter output

```math
\boxed{
\text{Problem}
\rightarrow
RQ_i
\rightarrow
SO_i
\rightarrow
\mathcal H(i).
}
```

---

## 4. Chapter 2 — Literature Review and Scientific Foundations — 20 pages maximum

### Final structure

2.1 Review Method and Evidence Scope  
2.2 Interdependent Infrastructure Systems and Multilayer SoS  
2.3 Coupled Power–Transportation Systems  
2.4 Information and Organizational Dependencies  
2.5 Cascading, Hybrid, and Spatiotemporal Dynamics  
2.6 Observation, State Estimation, and Control  
2.7 Resilience, Viability, Reachability, and Uncertainty  
2.8 Intervention, Sustainability, and Engineering Decision  
2.9 Critical Synthesis and Research Gap

### Compression rule

Chapter 2 must **not** become a textbook. Long tutorials on graph theory, power flow, traffic flow, viability theory, generic optimization, and the history of resilience are excluded from the main narrative unless directly needed for a thesis claim.

Each subsection must follow

```math
\boxed{
\text{Established evidence}
\rightarrow
\text{mechanism/method}
\rightarrow
\text{limitation}
\rightarrow
\text{thesis need}.
}
```

Detailed database strings, screening records, extraction matrices, and exhaustive evidence tables belong in Appendix A or the research repository.

---

## 5. Chapter 3 — Conceptual and Mathematical Framework — 30 pages maximum

All seven scientific stages remain intact. Compression occurs by removing unnecessary sub-subsections, not by removing stages.

### Final structure and internal budget

| Component | Target pages |
|---|---:|
| Definitions, notation, critical services, and `K(t)` | 3 |
| Stage 1 — Spatiotemporal Multilayer SoS Structure | 3 |
| Stage 2 — Evidence-Grounded Causal Interdependencies | 4 |
| Stage 3 — Physics-Based Hybrid Multiscale Dynamics | 5 |
| Stage 4 — Observation, State Estimation, Organization and Control | 4 |
| Stage 5 — Uncertainty-Aware Viability and Reachability Resilience | 6 |
| Stage 6 — Resilience Diagnosis, Intervention and Sustainability Consequences | 3 |
| Stage 7 — Engineering Decision and Adaptive Transformation | 2 |
| Stage-to-stage handoff / cross-cutting VVUQ logic | integrated within the above allocation |
| **TOTAL** | **30** |

### Required mathematical chain

```math
\boxed{
K
\rightarrow
\mathcal G
\rightarrow
\mathbb I
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
(b_t,\mathcal U_t,\pi_t)
\rightarrow
\mathfrak R_T
\rightarrow
(\Delta\mathfrak R,\Delta\mathbf J_{\rm sus})
\rightarrow
\mathcal A_{R,S}^{\star}.
}
```

### Compression rule

- Eliminate separate “Stage-X Mathematical Output” subsections; end each stage with one boxed output equation and one compact engineering interpretation.
- Do not repeat definitions already fixed earlier in the chapter.
- Put long derivations in Appendix B when the main text can preserve reproducibility with the governing equations, assumptions, boundary/initial conditions, and derivation reference.
- Stage 5 receives the largest allocation because it contains the central resilience mathematics.
- Interface criticality remains a Stage-6 supporting diagnostic, not a separate framework branch.
- Adaptive pathways remain a Stage-7 supporting extension unless formally activated.

---

## 6. Chapter 4 — Research Methodology and Experimental Design — 26 pages maximum

### Final structure

4.1 EGMIV Research Design  
4.2 Evidence, Data, and Provenance  
4.3 Experimental System and Disturbance Scenarios  
4.4 Parameterization, Calibration, and Model/Algorithm Selection  
4.5 H1 — Dynamic Causal Interdependency Experiment  
4.6 H2 — Information and Organization Experiment  
4.7 H3 — Viability–Reachability Experiment  
4.8 H4 — Intervention and Sustainability Consequence Experiment  
4.9 H5 — Joint Engineering Decision Experiment  
4.10 Verification, Validation, Uncertainty Quantification, and Sensitivity  
4.11 Reproducibility and Computational Environment

### Hypothesis specification rule

Each primary experiment must be summarized through one compact specification table:

```math
\boxed{
H_i
\mid
\text{mechanism}
\mid
\text{baseline}
\mid
\text{model}
\mid
\text{data}
\mid
\text{metric}
\mid
\delta_i
\mid
\text{uncertainty}
\mid
\text{falsification}.
}
```

### Compression rule

- Do not repeat equations already derived in Chapter 3; reference them and state only implementation-specific forms.
- Put exhaustive parameter provenance in Appendix C.
- Put long pseudocode and secondary algorithm variants in Appendix B or the GitHub repository.
- Combine verification, validation, UQ, sensitivity, and reproducibility where the same protocol applies across hypotheses.
- Calibration and validation remain explicitly separate despite page pressure.

---

## 7. Chapter 5 — Results — 24 pages maximum

### Final structure

5.1 Experimental and Validation Dataset Summary  
5.2 H1 Results — Dynamic Causal Interdependency  
5.3 H2 Results — Information and Organization  
5.4 H3 Results — Viability and Reachability Resilience  
5.5 H4 Results — Intervention and Sustainability Consequences  
5.6 H5 Results — Engineering Decision under Uncertainty  
5.7 Cross-Hypothesis Robustness and Summary

### Result reporting rule

For each hypothesis, integrate

```math
\boxed{
\text{estimate/result}
+
\text{uncertainty}
+
\text{validation}
+
\text{sensitivity}
+
\text{decision status}.
}
```

### Compression rule

- Do not restate the methodology.
- Use multi-panel figures and compact tables only when they answer a declared RQ/H.
- Move exhaustive sensitivity plots, parameter sweeps, solver diagnostics, and secondary scenarios to Appendix C/D or the repository.
- Preserve negative/null results.

---

## 8. Chapter 6 — Discussion and Sustainable Engineering Implications — 15 pages maximum

### Final structure

6.1 Principal Findings  
6.2 Dynamic Interdependency and Propagation  
6.3 Information, Organization, and Control  
6.4 Viability–Reachability Resilience  
6.5 Intervention and Sustainability Consequences  
6.6 Engineering Decision and Adaptive Transformation  
6.7 Comparison with Literature and Generalizability  
6.8 Limitations, Remaining Uncertainty, and Engineering Implications

### Compression rule

Each discussion subsection must answer only:

```math
\boxed{
\text{What mechanism was demonstrated?}
\rightarrow
\text{under what conditions?}
\rightarrow
\text{with what uncertainty?}
\rightarrow
\text{what engineering decision changes?}
\rightarrow
\text{what remains unvalidated?}
}
```

Do not repeat numerical results already shown in Chapter 5 except where needed for interpretation.

---

## 9. Chapter 7 — Conclusions and Future Research — 6 pages maximum

### Final structure

7.1 Answers to Research Questions  
7.2 Hypothesis Outcomes  
7.3 Validated Contributions  
7.4 Limitations and Domain of Validity  
7.5 Future Research

### Compression rule

Use one RQ table:

| RQ | Evidence/result | Answer | Validity domain |
|---|---|---|---|

and one H table:

| Hypothesis | Comparator/test | Outcome | Evidence status |
|---|---|---|---|

Allowed outcome vocabulary:

```math
\boxed{
\text{supported}
\;|\;
\text{not supported}
\;|\;
\text{not tested / inconclusive}.
}
```

Do not introduce new evidence, equations, or results in Chapter 7.

---

## 10. References — 11 pages target

The reference list contains only works actually cited in the thesis. Evidence catalogues and screened-but-uncited records do not enter the reference list merely because they were reviewed.

The 11-page allocation is a planning target, not permission to omit required citations. If verified cited references exceed the target, space must be recovered elsewhere rather than deleting scientifically necessary references.

---

## 11. Appendices — 10 pages maximum in the submitted manuscript

The submitted thesis uses four consolidated appendices:

### Appendix A — Evidence and Search Protocol Summary
- database/search protocol summary;
- screening/eligibility summary;
- interdependency evidence catalogue summary;
- links/identifiers to full machine-readable evidence records in the repository.

### Appendix B — Extended Mathematical Derivations and Algorithms
- derivations omitted from the main body;
- pseudocode needed for reproducibility;
- solver/reference-test details that cannot fit in Chapter 4.

### Appendix C — Parameter Provenance and Supplementary VVUQ
- parameter source/provenance summary;
- additional uncertainty/sensitivity diagnostics;
- supplementary verification/validation results.

### Appendix D — Reproducibility Manifest
- software and version environment;
- code/data locations;
- random seeds where applicable;
- execution order;
- Git commit identifiers;
- data/licensing/access constraints.

### Repository rule

The GitHub repository may contain material that is scientifically necessary for auditability but not necessary to print in the 160-page manuscript, including:

- full FTEE/EGMIV extraction tables;
- raw and intermediate data where licensing permits;
- complete code;
- full parameter registries;
- exhaustive sensitivity figures;
- solver diagnostics;
- complete search exports and screening records;
- machine-readable provenance manifests.

The thesis must still contain enough information to understand, evaluate, and reproduce the central analyses without relying on undocumented external steps.

---

## 12. Figure and table policy under the 160-page cap

Every figure/table must satisfy at least one of the following:

1. defines a system/model object;
2. demonstrates an experimental result;
3. communicates uncertainty/validation;
4. compares a required baseline;
5. supports an engineering decision.

Remove or relocate visuals that are decorative, duplicate text/equations, or merely repeat a table numerically.

Preferred main-text visual roles:

```text
Chapter 1: one system/problem visual + one RQ/SO/H traceability visual/table if useful
Chapter 2: evidence/gap synthesis tables rather than many literature-summary figures
Chapter 3: one high-information visual per major mathematical block where needed
Chapter 4: experiment architecture, data/provenance, and VVUQ tables/figures
Chapter 5: result-bearing plots/tables only
Chapter 6: synthesis/trade-off/decision visuals only when they add interpretation
Chapter 7: normally no new result figures
```

---

## 13. Page-budget enforcement rule

At every major manuscript checkpoint calculate

```math
\boxed{
\Delta P_c=P_c-P_c^{\max}
}
```

for each chapter `c`.

If `\Delta P_c>0`, apply compression in this order:

1. remove repeated explanations;
2. merge micro-headings;
3. convert repeated prose into one table;
4. remove generic theory already supported by citation;
5. consolidate equations;
6. move non-primary derivations/results to appendices;
7. move audit-level supplementary material to the repository;
8. only then redistribute pages from another chapter if the scientific argument requires it.

### Hard scientific prohibition

A page overrun may **never** be solved by:

- deleting uncertainty or validation information;
- suppressing contradictory/negative results;
- removing an essential baseline;
- deleting assumptions or validity limits;
- omitting a required citation;
- collapsing viability and reachability;
- removing sustainability consequences from H4/H5;
- replacing derivation with unsupported assertion.

---

## 14. Traceability requirement

Every substantive main-text element must be traceable to at least one thesis function:

```math
\boxed{
\text{ASU/program requirement}
\;|\;
RQ_i
\;|\;
SO_i
\;|\;
H_i
\;|\;
\text{mechanism}
\;|\;
\text{model}
\;|\;
\text{experiment}
\;|\;
\text{validation}
\;|\;
\text{result}
\;|\;
\text{engineering conclusion}.
}
```

If a section, figure, table, equation, or paragraph cannot be connected to one of these functions, it is a candidate for deletion, consolidation, appendix relocation, or repository-only preservation.

---

## 15. Change control

This file freezes the current **160-page manuscript planning architecture**.

It does **not** alter:

- the canonical seven-stage scientific framework;
- the canonical RQ/SO/H v3 specification;
- EGMIV;
- H1–H5 mathematical or falsification logic;
- any immutable scientific checkpoint.

A change to the total page cap, chapter budgets, or chapter compression architecture requires an explicit versioned revision of this file. Scientific changes must continue to follow the separate scientific change-control/checkpoint rules.

---

## 16. Final frozen manuscript architecture

```math
\boxed{
\begin{array}{lr}
\text{Preliminary matter} & 8\\
\text{Chapter 1 — Introduction} & 10\\
\text{Chapter 2 — Literature Review} & 20\\
\text{Chapter 3 — Mathematical Framework} & 30\\
\text{Chapter 4 — Methodology} & 26\\
\text{Chapter 5 — Results} & 24\\
\text{Chapter 6 — Discussion} & 15\\
\text{Chapter 7 — Conclusions} & 6\\
\text{References} & 11\\
\text{Appendices} & 10\\ \hline
\mathbf{TOTAL} & \mathbf{160}
\end{array}
}
```

The governing thesis-writing rule is therefore

```math
\boxed{
\textbf{Maximum scientific information per page, minimum repetition, full validation discipline.}
}
```



**Question-to-hypothesis mapping convention:** `i=1,…,7` indexes RQ/SO; `j=1,…,5` indexes hypotheses. `\mathcal H(i)` denotes the declared mapping in `CANONICAL_RQ_SO_HYPOTHESES_V3.md`, including developmental qualification for RQ1/RQ2. It does not assert a one-to-one RQ–H correspondence.


**Question numbering amendment (2026-09-17):** Use RQ0 plus RQ1–RQ7 and SO1–SO7 from `CANONICAL_RQ_SO_HYPOTHESES_V3.md`. H1–H5 retain separate identifiers: RQ1/RQ2 are developmental inputs to H1; RQ3→H1, RQ4→H2, RQ5→H3, RQ6→H4, RQ7→H5. Any record index shared by Q/SO/H is a traceability-row key, not an assertion of equal scientific identifiers.
