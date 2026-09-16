# ASU MSE Thesis Master Specification v1.0

**Status:** CURRENT THESIS CONTROL SPECIFICATION  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**School:** School of Sustainable Engineering and the Built Environment (SSEBE)  
**Method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method  
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

The scientific architecture is the frozen seven-stage framework plus EGMIV execution logic. The document architecture is the seven-chapter thesis argument.

### Scientific architecture

```math
\text{Structure}
\rightarrow\text{Causal Interdependency}
\rightarrow\text{Dynamics}
\rightarrow\text{Observation/Organization/Control}
\rightarrow\text{Viability}
\rightarrow\text{Transformation Diagnosis}
\rightarrow\text{Transformation Pathways}.
```

### Document architecture

```math
\text{Introduction}
\rightarrow\text{Literature/Theory}
\rightarrow\text{Framework}
\rightarrow\text{Methodology}
\rightarrow\text{Results}
\rightarrow\text{Discussion}
\rightarrow\text{Conclusion}.
```

## 6. EGMIV thesis-control rule

The thesis skeleton itself is treated as an engineered research artifact.

For every important thesis object `i`:

```math
\boxed{
\mathfrak T_i=(R_i,Q_i,H_i,E_i,M_i,\Phi_i,S_i,A_i,V_i,\sigma_i)
}
```

where:

- `R_i`: university/program requirement when applicable;
- `Q_i`: research question;
- `H_i`: hypothesis/proposition;
- `E_i`: admissible evidence/data;
- `M_i`: method/model;
- `\Phi_i`: decision metric;
- `S_i`: thesis section;
- `A_i`: artifact (figure/table/equation/code/data);
- `V_i`: verification/validation method;
- `\sigma_i`: status.

A broken traceability chain is a thesis defect.

## 7. Proposal as controlled release

The proposal should be treated as:

```math
\boxed{\text{Thesis Architecture Release v1.0}}
```

containing:

- Chapter 1 logic: problem, significance, scope, RQs, objectives, hypotheses;
- condensed Chapter 2: qualified evidence and gap;
- Chapter 3: proposed theoretical/mathematical architecture;
- planned Chapter 4: methodology, experiments, V&V, UQ, falsification;
- expected contribution clearly labeled as proposed rather than demonstrated.

Any later change to system boundary, hypothesis logic, confirmatory baselines, or major methodology must be versioned and justified rather than silently rewritten.

## 8. Current H1 thesis gate

Current repository authority indicates:

```math
\boxed{M_0=\text{independent},\quad M_1=\text{static/algebraic},\quad M_2=\text{dynamic causal}.}
```

The H1 model implementations and confirmatory design are substantially advanced. However, the row-level raw-data retrieval and qualification gate remains blocking. No calibration or confirmatory H1 execution is authorized until the predeclared acquisition/qualification gates are passed.

## 9. Governing thesis principle

```math
\boxed{
\textbf{Verified evidence}
\rightarrow
\textbf{mathematical representation}
\rightarrow
\textbf{frozen experiment}
\rightarrow
\textbf{result}
\rightarrow
\textbf{qualified conclusion}.
}
```

The reverse direction — conclusion first, evidence afterward — is prohibited.

## 10. Official sources

- ASU Graduate College Format Manual: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation/asu-graduate-college
- Formatting process / Format Wizard / submission: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation
- Format Checklist: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation/format-checklist
- SSEBE Sustainable Engineering MSE Handbook 2026–2027: https://ssebe.engineering.asu.edu/wp-content/uploads/sites/28/2026/07/MSE-Sustainable-Engineering-Handbook-2026-2027.pdf
- SSEBE Graduate Advising / defense procedures: https://ssebe.engineering.asu.edu/advising/graduate/
