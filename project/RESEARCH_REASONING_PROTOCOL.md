# Canonical Research Reasoning Protocol

**Status:** CANONICAL / CURRENT  
**Version:** 1.1  
**Effective date:** 2026-09-12  
**Scope:** entire thesis — literature, mathematics, modeling, simulation, hypotheses, experiments, verification, validation, synthesis, visualization, and sustainable-engineering decisions

---

## Governing rule

> **No claim without a definition, mechanism, evidence, assumptions, test, and boundary of validity.**

For every problem, method, equation, paper, hypothesis, or proposed innovation, reasoning follows

```math
\text{LEARN}
\rightarrow
\text{VERIFY}
\rightarrow
\text{FORMULATE}
\rightarrow
\text{DERIVE}
\rightarrow
\text{TEST}
\rightarrow
\text{VALIDATE}
\rightarrow
\text{SYNTHESIZE}
\rightarrow
\text{ADVANCE}.
```

The objective is not mathematical complication. The objective is to use the minimum mathematics necessary to explain the physics correctly, solve the engineering problem, quantify uncertainty, and produce a defensible sustainable decision.

---

## 1. LEARN — understand before judging

First ask:

```math
\text{What is it?}
\qquad
\text{Why was it created?}
\qquad
\text{What problem does it solve?}
```

For any method $M$, establish

```math
M=
\{\text{definition},\text{ mathematical object},\text{ assumptions},\text{ inputs},\text{ outputs},\text{ limitations}\}.
```

Example question:

> Can Ricci curvature help our infrastructure thesis?

We do not begin with application. We first determine the precise mathematical object, for example

```math
\kappa_{ij}=1-\frac{W_1(m_i,m_j)}{d(i,j)},
```

and establish exactly what $\kappa_{ij}$ measures, what $m_i,m_j$ represent, what metric $d$ is used, and which assumptions are required before mapping the quantity to an infrastructure problem.

---

## 2. VERIFY — establish what is actually known

Every important statement receives an epistemic status.

| Label | Meaning |
|---|---|
| `[E]` | established by external evidence |
| `[D]` | derived mathematically or logically from established material |
| `[H]` | hypothesis to be tested |
| `[P]` | thesis proposal |
| `[A]` | assumption |
| `[U]` | currently uncertain or unresolved |

Example:

- **[E]** EV charging couples transportation demand to distribution-grid loading.
- **[D]** Therefore changes in vehicle-arrival distributions can alter electrical-load trajectories.
- **[H]** Certain charging interfaces may dominate cross-system cascade propagation.
- **[P]** Test this using dynamic interface criticality.

These statements must never be collapsed into one. The evidence status of a statement must remain visible until additional evidence or derivation justifies a change.

---

## 3. FORMULATE — turn words into mathematics

Every research question should eventually become

```math
\text{variables}
+
\text{relations}
+
\text{constraints}
+
\text{objective}.
```

Example verbal statement:

> Transportation disruption delays power restoration.

Define

```math
T_i^{R}=T_i^{\rm travel}+T_i^{\rm repair}.
```

Transportation condition affects

```math
T_i^{\rm travel}=f(\mathcal G_T(t),h(t),r_i).
```

Therefore

```math
\mathcal G_T(t)
\rightarrow
T_i^{\rm travel}
\rightarrow
T_i^{R}.
```

Only after this formulation can the interdependency be investigated rigorously.

---

## 4. DERIVE — explain the mechanism

The engineering argument must have the form

```math
\text{Cause}
\rightarrow
\text{physical mechanism}
\rightarrow
\text{state change}
\rightarrow
\text{system consequence}.
```

Not merely:

> Flooding reduces resilience.

But, for example:

```math
h(x,t)
\rightarrow C_e(t)\downarrow
\rightarrow q_e(t)\downarrow
\rightarrow T_{\rm crew}\uparrow
\rightarrow T_{\rm restoration}\uparrow
\rightarrow Q_P(t)\downarrow.
```

Each arrow must eventually be associated with:

1. a governing equation or explicit functional relation;
2. empirical, experimental, theoretical, or authoritative engineering evidence;
3. explicit assumptions;
4. uncertainty and a validity domain.

An arrow is therefore a reasoning obligation, not merely a graphical connector.

---

## 5. TEST — try to destroy our own argument

For every proposed contribution $M_1$, define at least one competing baseline $M_0$:

```math
M_1
\quad\text{vs}\quad
M_0.
```

Then formulate

```math
H_0:
M_1\text{ provides no material improvement over }M_0
```

versus

```math
H_1:
M_1\text{ changes explanation, prediction, or decision sufficiently}.
```

Example:

```math
H_0:
\operatorname{TopK}(C)
=
\operatorname{TopK}(C^{\mathcal V}).
```

If this is supported across the prespecified domain, a new viability-aware interface ranking may not be necessary. A negative result is scientifically informative rather than a failure of the research process.

---

## 6. VALIDATE — proof has several levels

Use the following validation ladder:

```math
\begin{aligned}
&\text{Logical consistency}\\
&\downarrow\\
&\text{Dimensional consistency}\\
&\downarrow\\
&\text{Mathematical consistency}\\
&\downarrow\\
&\text{Numerical verification}\\
&\downarrow\\
&\text{Sensitivity analysis}\\
&\downarrow\\
&\text{Benchmark comparison}\\
&\downarrow\\
&\text{Physical plausibility}\\
&\downarrow\\
&\text{Empirical validation}.
\end{aligned}
```

These levels are not interchangeable.

- A simulation agreeing with its assumptions is not empirical validation.
- A mathematically correct model is not automatically physically correct.
- A physically plausible model is not necessarily decision-useful.
- Validation at one operating point or domain does not automatically imply validity outside that domain.

Verification asks whether the mathematical/computational problem was solved correctly. Validation asks whether the model is adequate for its intended real-system use.

---

## 7. SYNTHESIZE — integrate evidence instead of collecting papers

Reading many papers is not synthesis.

For each question $Q$, construct

```math
\mathcal E_Q
=
\{\text{agreement},\text{ contradictions},\text{ methods},\text{ assumptions},\text{ limitations},\text{ remaining gap}\}.
```

The synthesis must answer:

1. What is already established?
2. Where do studies disagree?
3. Why do they disagree?
4. Which assumptions create those differences?
5. What remains unresolved?
6. Which unresolved part matters to the engineering problem?

The final question prevents literature review from becoming bibliography accumulation.

---

## 8. ADVANCE — contribution comes last

Only after the preceding seven steps do we state our proposed contribution.

The argument should have the structure

```math
\begin{aligned}
&\text{Literature establishes }A.\\
&\text{Engineering evidence establishes }B.\\
&A+B&\Rightarrow\text{ unresolved problem }C.\\
&\text{Existing method }M_0&\text{ cannot adequately resolve }C\text{ because of limitation }L.\\
&\therefore\quad M_1&=\text{ proposed extension}.\\
&\text{Then test }M_1&\text{ against }M_0.
\end{aligned}
```

The thesis does not begin by assuming the novelty is correct. The contribution is what remains after competing explanations, assumptions, uncertainty, validation checks, and falsification attempts have been survived.

---

## 9. Canonical argument architecture

For every important thesis statement, construct the chain

```math
\textbf{CLAIM}
\rightarrow
\textbf{EVIDENCE}
\rightarrow
\textbf{MECHANISM}
\rightarrow
\textbf{MATHEMATICS}
\rightarrow
\textbf{ASSUMPTIONS}
\rightarrow
\textbf{TEST}
\rightarrow
\textbf{RESULT}
\rightarrow
\textbf{ENGINEERING IMPLICATION}.
```

No element should be silently omitted when it materially affects the inference.

---

## 10. Example — controllability of critical interfaces

### Claim

> Some highly critical interfaces may not be protectable through post-failure response alone.

### Evidence requirement

The argument requires evidence concerning at least:

- cascade times;
- detection delays;
- communication delays;
- authorization/decision delays;
- mobilization delays;
- actuation delays.

### Mechanism

```math
\text{failure}
\rightarrow\text{detection}
\rightarrow\text{communication}
\rightarrow\text{authorization}
\rightarrow\text{mobilization}
\rightarrow\text{actuation}.
```

### Mathematics

A reduced response-time representation may be written as

```math
T_{\rm response}=T_d+T_c+T_a+T_m+T_x,
```

and compared with a cascade timescale $T_{\rm cascade}$.

If a probabilistic model for both quantities is scientifically justified, define

```math
P_{\rm control}
=
P\!\left(T_{\rm response}<T_{\rm cascade}\right).
```

If probability distributions are not justified, use deterministic or interval-based timing margins instead of inventing probabilities.

### Hypothesis

```math
H:
P_{\rm control}\text{ materially changes intervention priority}.
```

### Test

Compare a baseline criticality measure $C_i$ with

```math
A_i=C_iP_{{\rm control},i}
```

and

```math
H_i=C_i\left(1-P_{{\rm control},i}\right).
```

### Engineering implication

```math
\begin{cases}
P_{\rm control}\approx1
&\rightarrow\text{ operational intervention may be feasible},\\
P_{\rm control}\approx0
&\rightarrow\text{ pre-emptive structural hardening may be required}.
\end{cases}
```

This is a reasoning template, not an established thesis result. Its equations, probability model, thresholds, decision rules, and transferability require independent evidence and validation before adoption.

---

## 11. Six continuous research questions

For every significant thesis decision, ask:

```math
\begin{aligned}
1.&\quad \textbf{What do we know?}\\
2.&\quad \textbf{How do we know it?}\\
3.&\quad \textbf{What mechanism explains it?}\\
4.&\quad \textbf{What remains unknown?}\\
5.&\quad \textbf{What experiment could resolve that unknown?}\\
6.&\quad \textbf{If the hypothesis is wrong, what result should we observe?}
\end{aligned}
```

Question 6 is mandatory for confirmatory reasoning because it forces the research design to specify observable failure conditions for the hypothesis.

---

## 12. Method-selection rule

Reject arguments of the form:

> Paper X used method Y, therefore this thesis should use Y.

Replace them with

```math
\begin{aligned}
&\text{Engineering problem}\\
&\downarrow\\
&\text{Observed mechanism}\\
&\downarrow\\
&\text{Scientific evidence}\\
&\downarrow\\
&\text{Mathematical structure}\\
&\downarrow\\
&\text{Candidate methods}\\
&\downarrow\\
&\text{Assumption compatibility}\\
&\downarrow\\
&\text{Benchmark comparison}\\
&\downarrow\\
&\text{Test / falsification}\\
&\downarrow\\
&\text{Validated contribution}.
\end{aligned}
```

A method is selected because its mathematical structure and assumptions are compatible with the engineering mechanism and decision problem, not because it appears in a relevant paper.

---

## 13. Minimum-mathematics principle

> **Use the minimum mathematics necessary to explain the physics correctly, solve the engineering problem, quantify uncertainty, and produce a defensible sustainable decision.**

Complexity has no intrinsic scientific value. Additional mathematical structure is justified only if it improves explanation, prediction, control, decision quality, uncertainty characterization, identifiability, or falsifiability.

---

## 14. Application to the seven-stage thesis framework

This reasoning protocol applies within and between all seven stages:

```math
\mathcal S
\rightarrow
\mathfrak I
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
(X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u)
\rightarrow
(K_{\rm sus},\mathcal V,\rho,T_{\mathcal V},T_K)
\rightarrow
\Phi_{\rm ST}
\rightarrow
\mathfrak P_{\rm ST}.
```

For every transition, ask:

> **What exactly justifies this arrow?**

The answer must ultimately be traceable to definitions, evidence, mechanism, mathematics, assumptions, tests, verification/validation results, uncertainty, and a stated domain of validity.

---

## 15. Thesis-wide source and reasoning discipline

For substantial scientific claims:

1. learn the governing theory before proposing an application;
2. search reproducibly when external evidence is needed;
3. prioritize primary theory, authoritative standards, peer-reviewed technical evidence, and validated benchmarks;
4. cite scientific support in text adjacent to the claim it supports;
5. separate source-derived evidence from thesis inference and proposal;
6. record contradictory evidence rather than suppressing it;
7. preserve the validation domain and uncertainty of every transferred model or parameter;
8. advance a thesis claim only after the competing explanations and failure conditions are explicit.

This section governs both writing and analysis: citation is not decoration; it is part of the inferential chain.

---

## 16. Operational research record

For every new object $Q$, the working record should answer at minimum

```math
Q
\mapsto
(\text{definition},\text{mechanism},\text{evidence},\text{assumptions},\text{model},\text{test},\text{validation domain},\text{uncertainty},\text{rival},\text{falsification},\text{engineering implication}).
```

This is the canonical reasoning protocol for the entire thesis until explicitly revised through a versioned update.