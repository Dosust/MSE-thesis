# ASU MSE Thesis Master Specification v1.1

**Status:** CURRENT THESIS CONTROL SPECIFICATION  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**School:** School of Sustainable Engineering and the Built Environment (SSEBE)  
**Method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method  
**Framework authority:** `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**RQ–SO–H authority:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V2.md`  
**Reasoning authority:** `../../project/RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Verification date for ASU requirements:** 2026-09-16

## 1. Purpose

This specification connects formal ASU/SSEBE requirements to the thesis scientific method, chapter architecture, evidence system, mathematical framework, experiments, validation, and final document.

```math
\boxed{
\text{ASU Requirement}
\rightarrow
\text{Scientific Claim}
\rightarrow
\text{Evidence}
\rightarrow
\text{Method}
\rightarrow
\text{Result}
\rightarrow
\text{Thesis Location}
\rightarrow
\text{Verification}.
}
```

## 2. Authority hierarchy

```math
\boxed{
\text{ASU Graduate College}
>
\text{SSEBE MSE handbook}
>
\text{chair/GSC decisions}
>
\text{approved style guide}
>
\text{internal conventions}.
}
```

If two requirements conflict, the higher authority controls. Internal repository conventions are never treated as university requirements.

## 3. Verified program-level requirements

From the 2026–2027 Sustainable Engineering MSE Handbook:

- Thesis culminating experience: `CEE 599 Thesis`, 6 credit hours.
- Students initially enter a non-thesis option and must secure an eligible faculty advisor/chair before thesis enrollment.
- The Graduate Supervisory Committee contains at least three faculty members including the chair; at least two must be tenured or tenure-track SSEBE faculty.
- The thesis culminates in an open oral defense.
- Research is expected to be of sufficient breadth/depth to be publishable in a concentration-related journal.
- Thesis research should reflect approximately 750 hours of thoughtful work.
- Research must follow the scientific method, be objective and reproducible, demonstrate independent/original/creative inquiry, and use predefined measurable hypotheses or developmental goals/objectives.

These are compliance requirements, not optional internal preferences.

## 4. Verified Graduate College document requirements

The Graduate College controls thesis/dissertation formatting. Current verified requirements include:

- ASU Format Wizard required for documents going through Graduate College format review.
- Graduate College Format Manual supersedes the selected style guide when they conflict.
- 1.25-inch left/right margins; 1-inch top/bottom margins.
- Consistent approved TrueType font and size throughout, subject to limited stated exceptions.
- Main body generally double-spaced; specified exceptions may be single-spaced.
- Abstract maximum: 350 words; no first-person plural `we`, `our`, or `us`.
- Preliminary matter follows ASU sequence; main text begins page 1.
- Complete defense-ready document uploaded through iPOS at least 10 business days before defense.
- Defense must be scheduled through iPOS at least 10 business days before the defense date.

## 5. Scientific architecture versus document architecture

```math
\boxed{\mathcal A_{science}\neq\mathcal A_{document}.}
```

The scientific architecture is the canonical seven-stage framework v2.0 plus the frozen v2 RQ–SO–H logic and EGMIV execution method. The document architecture is the seven-chapter thesis argument.

### Scientific architecture v2.0

```math
\boxed{
\text{Critical Service Requirements}
\rightarrow
\text{Spatiotemporal SoS Structure}
\rightarrow
\text{Causal Interdependencies}
\rightarrow
\text{Hybrid Multiscale Dynamics}
\rightarrow
\text{Observation / Estimation / Organization / Control}
\rightarrow
\text{Viability + Reachability + Probability}
\rightarrow
\text{Intervention + Sustainability Consequences}
\rightarrow
\text{Engineering Decision}.
}
```

The Stage-5 resilience object is

```math
\boxed{
\mathfrak R_T(t)
=
\left(
\mathcal V_{\alpha,T},
\mathcal R_{\beta,T},
\rho_{\mathcal V},
T_{\mathcal V},
T_{\rm rec},
P_{\rm viable},
P_{\rm recover}
\right).
}
```

Conventional performance/recovery curves remain a comparator, not a discarded method. The thesis tests whether `\mathfrak R_T` adds incremental decision or predictive information.

### Document architecture

```math
\text{Introduction}
\rightarrow
\text{Literature/Theory}
\rightarrow
\text{Framework}
\rightarrow
\text{Methodology}
\rightarrow
\text{Results}
\rightarrow
\text{Discussion}
\rightarrow
\text{Conclusion}.
```

## 6. Canonical research logic and traceability

The v2 primary research logic is frozen in `../../project/CANONICAL_RQ_SO_HYPOTHESES_V2.md` and mirrored in `RQ_SO_H_TRACEABILITY_V2.md`.

```math
\boxed{
RQ_i
\rightarrow
SO_i
\rightarrow
H_i
\rightarrow
\text{mechanism}
\rightarrow
\text{metric}
\rightarrow
\text{baseline}
\rightarrow
\text{experiment}
\rightarrow
\text{uncertainty}
\rightarrow
\text{falsification}
\rightarrow
\text{result}
\rightarrow
\text{engineering conclusion}.
}
```

The five primary tests are:

```math
H_1:\quad M_2\ \text{vs}\ M_1\ \text{vs}\ M_0,
```

```math
H_2:\quad P+T\ \text{vs}\ P+T+I\ \text{vs}\ P+T+I+O,
```

```math
H_3:\quad R_{\rm curve}\ \text{vs}\ R_{\rm curve}+\mathfrak R_T,
```

```math
H_4:\quad a_k\rightarrow\left(\Delta\mathfrak R^{a_k},\Delta\mathbf J_{\rm sus}^{a_k}\right),
```

```math
H_5:\quad \mathcal A_R^{\star}\ \text{vs}\ \mathcal A_{R,S}^{\star}.
```

Interface criticality is a Stage-6 supporting diagnostic. Adaptive transformation pathways are a Stage-7 supporting extension. They are not the primary H4/H5 claims under v2.0.

## 7. EGMIV thesis-control rule

The thesis skeleton itself is treated as an engineered research artifact.

For every important thesis object `i`:

```math
\boxed{
\mathfrak T_i
=
(R_i,Q_i,O_i,H_i,E_i,M_i,\Phi_i,S_i,A_i,V_i,\sigma_i)
}
```

where:

- `R_i`: university/program requirement when applicable;
- `Q_i`: research question;
- `O_i`: specific objective;
- `H_i`: hypothesis/proposition;
- `E_i`: admissible evidence/data;
- `M_i`: method/model;
- `\Phi_i`: decision metric;
- `S_i`: thesis section;
- `A_i`: artifact (figure/table/equation/code/data);
- `V_i`: verification/validation method;
- `\sigma_i`: status.

A broken traceability chain is a thesis defect.

## 8. Evidence and citation-control rule

Scientific literature is used to justify why a question, mechanism, mathematical object, comparator, or engineering outcome is legitimate. It is not automatically evidence of novelty.

```math
\boxed{
\text{scientific support}
\neq
\text{novelty proof}.
}
```

Under `RESEARCH_REASONING_PROTOCOL.md` v1.2:

- every externally sourced scientific claim must carry an adjacent verified APA 7 author–date citation;
- externally adopted/adapted equations, algorithms, parameter values, thresholds, datasets, and standards require adjacent source attribution;
- thesis-derived claims are marked as derivation, hypothesis, proposal, or assumption rather than decorated with irrelevant citations;
- novelty/gap claims require a separate reproducible search and boundary audit.

The canonical RQ–SO–H file records literature foundations for all five primary research questions and hypotheses. Key foundation classes include interdependency/cascade modeling (Rinaldi et al., 2001; Ouyang, 2014; Tong et al., 2025), information/governance effects (Helmrich et al., 2021; Rydén Sonesson et al., 2021), resilience curves and stochastic viability/reachability (Doyen & De Lara, 2010; Poulin & Kane, 2021; Vinod & Oishi, 2021), and resilience–sustainability engineering decision trade-offs (Liu et al., 2024; Sánchez-Silva et al., 2025; Zhu & Zhang, 2026).

## 9. Proposal as controlled release

The proposal should be treated as:

```math
\boxed{\text{Thesis Architecture Release v2.0}}
```

containing:

- Chapter 1 logic: problem, significance, scope, RQ0/RQ1–RQ5, general objective, SO1–SO5, H1–H5;
- condensed Chapter 2: qualified evidence and theoretical foundations;
- Chapter 3: canonical seven-stage v2 mathematical architecture;
- planned Chapter 4: H1–H5 methodology, experiments, V&V, UQ, and falsification;
- expected contribution clearly labeled as proposed rather than demonstrated.

Any later change to system boundary, hypothesis logic, confirmatory baselines, primary metrics, or major methodology must be versioned and justified rather than silently rewritten.

## 10. Confirmatory execution gates

### H1

Current repository authority indicates:

```math
\boxed{M_0=\text{independent},\quad M_1=\text{static/algebraic},\quad M_2=\text{dynamic causal}.}
```

The H1 model implementations and confirmatory design are substantially advanced. However, the row-level raw-data retrieval and qualification gate remains blocking. No calibration or confirmatory H1 execution is authorized until the predeclared acquisition/qualification gates are passed.

### H3–H5

H3–H5 scientific logic is frozen, but confirmatory execution remains blocked until hypothesis-specific preregistration fixes the following:

```text
H3: K, G_rec, F, T, alpha, beta, uncertainty model, primary Skill metric, delta_3
H4: intervention set, resilience-effective criterion, sustainability accounting boundary, D_J, delta_4
H5: A_R*, A_R,S*, uncertainty treatment, set/regret metric, delta_5
```

Probability distributions may be used only when evidentiary support is adequate. Otherwise, deterministic, interval-based, scenario-based, or nonprobabilistic robustness methods must be used instead of invented probabilities.

## 11. Governing thesis principle

```math
\boxed{
\text{Verified evidence}
\rightarrow
\text{mathematical representation}
\rightarrow
\text{frozen experiment}
\rightarrow
\text{result}
\rightarrow
\text{qualified conclusion}.
}
```

The reverse direction — conclusion first, evidence afterward — is prohibited.

## 12. Current synchronization status

```math
\boxed{
\text{Framework v2}
\rightarrow
\text{RQ--SO--H v2 frozen}
\rightarrow
\text{master outline synchronized}
\rightarrow
\text{master specification synchronized}
\rightarrow
\text{root abstract / entry-point synchronization}
\rightarrow
\text{H3--H5 preregistration}.
}
```

## 13. Official sources

- ASU Graduate College Format Manual: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation/asu-graduate-college
- Formatting process / Format Wizard / submission: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation
- Format Checklist: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation/format-checklist
- SSEBE Sustainable Engineering MSE Handbook 2026–2027: https://ssebe.engineering.asu.edu/wp-content/uploads/sites/28/2026/07/MSE-Sustainable-Engineering-Handbook-2026-2027.pdf
- SSEBE Graduate Advising / defense procedures: https://ssebe.engineering.asu.edu/advising/graduate/

Full APA 7 references for the scientific evidence anchors are maintained in `../../project/CANONICAL_RQ_SO_HYPOTHESES_V2.md`.