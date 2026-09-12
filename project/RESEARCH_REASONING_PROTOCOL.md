# Canonical Research Reasoning Protocol

**Status:** canonical cross-cutting reasoning protocol  
**Effective date:** 2026-09-12  
**Scope:** entire thesis — literature, mathematics, modeling, simulation, hypotheses, figures, experiments, verification, validation, synthesis, and engineering decisions

---

## Governing rule

```math
\boxed{\textbf{No claim without a definition, mechanism, evidence, assumptions, test, and boundary of validity.}}
```

For every problem, method, equation, paper, hypothesis, or proposed innovation, reasoning follows:

```math
\boxed{\text{LEARN}\rightarrow\text{VERIFY}\rightarrow\text{FORMULATE}\rightarrow\text{DERIVE}\rightarrow\text{TEST}\rightarrow\text{VALIDATE}\rightarrow\text{SYNTHESIZE}\rightarrow\text{ADVANCE}}
```

The purpose is not mathematical complication. The purpose is to use the minimum mathematics necessary to explain the physics correctly, solve the engineering problem, quantify uncertainty, and produce a defensible sustainable decision.

---

## 1. LEARN — understand before judging

First ask:

```math
\boxed{\text{What is it? Why was it created? What problem does it solve?}}
```

For any method `M`, establish:

```math
M=\{\text{definition},\text{mathematical object},\text{assumptions},\text{inputs},\text{outputs},\text{limitations}\}.
```

Example question:

> Can Ricci curvature help our infrastructure thesis?

We do not begin with application. We first determine the mathematical object, for example

```math
\kappa_{ij}=1-\frac{W_1(m_i,m_j)}{d(i,j)},
```

and understand exactly what `\kappa_{ij}` measures before mapping it to an infrastructure problem.

---

## 2. VERIFY — establish what is actually known

Every important statement receives an epistemic status:

```math
\boxed{
\begin{array}{ll}
[E] & \text{Established by evidence}\\
[D] & \text{Derived mathematically}\\
[H] & \text{Hypothesis}\\
[P] & \text{Our proposal}\\
[A] & \text{Assumption}\\
[U] & \text{Currently uncertain}
\end{array}}
```

Example:

- **[E]** EV charging couples transportation demand to distribution-grid loading.
- **[D]** Therefore changes in vehicle-arrival distributions can alter electrical load trajectories.
- **[H]** Certain charging interfaces may dominate cross-system cascade propagation.
- **[P]** We test this using dynamic interface criticality.

These statements must never be collapsed into one.

---

## 3. FORMULATE — turn words into mathematics

Every research question should eventually become:

```math
\boxed{\text{variables}+\text{relations}+\text{constraints}+\text{objective}}
```

Example verbal statement:

> Transportation disruption delays power restoration.

Define

```math
T_i^{R}=T_i^{\mathrm{travel}}+T_i^{\mathrm{repair}}.
```

Transportation condition affects

```math
T_i^{\mathrm{travel}}=f(\mathcal G_T(t),h(t),r_i).
```

Therefore

```math
\boxed{\mathcal G_T(t)\rightarrow T_i^{\mathrm{travel}}\rightarrow T_i^{R}.}
```

Only after formulation can the interdependency be investigated rigorously.

---

## 4. DERIVE — explain the mechanism

The engineering argument must have the form

```math
\boxed{\text{Cause}\rightarrow\text{physical mechanism}\rightarrow\text{state change}\rightarrow\text{system consequence}.}
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

Each arrow should receive:

1. a governing equation or explicit functional relation;
2. empirical or theoretical evidence;
3. assumptions;
4. uncertainty characterization.

---

## 5. TEST — try to destroy our own argument

For every proposed contribution `M_1`, define a baseline `M_0`:

```math
\boxed{M_1\quad\text{vs}\quad M_0.}
```

Then formulate competing hypotheses:

```math
H_0:\ M_1\text{ provides no material improvement over }M_0
```

versus

```math
H_1:\ M_1\text{ changes explanation, prediction, or decision sufficiently}.
```

Example:

```math
H_0:\operatorname{TopK}(C)=\operatorname{TopK}(C^{\mathcal V}).
```

If this is true, a new viability-aware interface ranking may not be necessary. The proposed method must therefore survive an explicit falsification attempt.

---

## 6. VALIDATE — proof has several levels

Use the validation ladder:

```math
\boxed{
\begin{array}{c}
\text{Logical consistency}\\
\downarrow\\
\text{Dimensional consistency}\\
\downarrow\\
\text{Mathematical consistency}\\
\downarrow\\
\text{Numerical verification}\\
\downarrow\\
\text{Sensitivity analysis}\\
\downarrow\\
\text{Benchmark comparison}\\
\downarrow\\
\text{Physical plausibility}\\
\downarrow\\
\text{Empirical validation}
\end{array}}
```

These levels are not interchangeable.

- A simulation agreeing with its assumptions is not empirical validation.
- A mathematically correct model is not automatically physically correct.
- A physically plausible model is not necessarily decision-useful.

Verification asks whether the mathematical/computational problem was solved correctly. Validation asks whether the model is adequate for its intended real-system use.

---

## 7. SYNTHESIZE — integrate evidence instead of collecting papers

Reading many papers is not synthesis.

For each question `Q`, construct

```math
\boxed{\mathcal E_Q=\{\text{agreement},\text{contradictions},\text{methods},\text{assumptions},\text{limitations},\text{remaining gap}\}.}
```

The synthesis must answer:

1. What is already established?
2. Where do studies disagree?
3. Why do they disagree?
4. What assumptions create those differences?
5. What remains unresolved?
6. Which unresolved part matters to our engineering problem?

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
&\text{Existing method }M_0&\text{ cannot adequately resolve }C\text{ because }L.\\
&\therefore\quad M_1&=\text{our proposed extension}.\\
&\text{We test }M_1&\text{ against }M_0.
\end{aligned}
```

This is the required structure of a defensible research contribution.

---

## Canonical argument architecture

For every thesis statement, construct the chain

```math
\boxed{
\textbf{CLAIM}
\rightarrow\textbf{EVIDENCE}
\rightarrow\textbf{MECHANISM}
\rightarrow\textbf{MATHEMATICS}
\rightarrow\textbf{ASSUMPTIONS}
\rightarrow\textbf{TEST}
\rightarrow\textbf{RESULT}
\rightarrow\textbf{ENGINEERING IMPLICATION}}
```

Every arrow is itself a reasoning obligation: it must be justified, not merely drawn or asserted.

---

## Example — controllability of critical interfaces

### Claim

```math
\boxed{\text{Some highly critical interfaces cannot be protected through post-failure response.}}
```

### Evidence needed

Literature, experiment, or incident evidence should establish quantities such as:

- cascade times;
- detection delays;
- communication delays;
- authority/decision delays;
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

```math
T_{\rm response}=T_d+T_c+T_a+T_m+T_x.
```

Compare with

```math
T_{\rm cascade}.
```

Define

```math
\boxed{P_{\rm control}=P(T_{\rm response}<T_{\rm cascade}).}
```

### Hypothesis

```math
H_1:\ P_{\rm control}\text{ materially changes intervention priority}.
```

### Test

Compare conventional criticality

```math
C_i
```

with controllable criticality

```math
A_i=C_iP_{\rm control,i}
```

and hardening priority

```math
H_i=C_i(1-P_{\rm control,i}).
```

### Engineering implication

```math
\boxed{
\begin{cases}
P_{\rm control}\approx1 &\rightarrow \text{operational intervention},\\
P_{\rm control}\approx0 &\rightarrow \text{pre-emptive structural hardening}.
\end{cases}}
```

This example remains a proposed argument structure until its definitions, evidence base, assumptions, statistical interpretation, and decision thresholds are separately verified and validated.

---

## Continuous six-question discipline

For almost every thesis decision ask:

```math
\boxed{
\begin{aligned}
1.&\quad\textbf{What do we know?}\\
2.&\quad\textbf{How do we know it?}\\
3.&\quad\textbf{What mechanism explains it?}\\
4.&\quad\textbf{What remains unknown?}\\
5.&\quad\textbf{What experiment could resolve that unknown?}\\
6.&\quad\textbf{If our hypothesis is wrong, what result should we observe?}
\end{aligned}}
```

Question 6 is mandatory for confirmatory claims because it forces falsifiability.

---

## Rejected reasoning pattern

Reject arguments of the form:

```math
\boxed{\text{Paper X used method Y, therefore we should use Y.}}
```

Replace them with:

```math
\boxed{
\begin{array}{c}
\text{Engineering problem}\\
\downarrow\\
\text{Observed mechanism}\\
\downarrow\\
\text{Scientific evidence}\\
\downarrow\\
\text{Mathematical structure}\\
\downarrow\\
\text{Candidate methods}\\
\downarrow\\
\text{Assumption compatibility}\\
\downarrow\\
\text{Benchmark}\\
\downarrow\\
\text{Test/falsification}\\
\downarrow\\
\text{Validated contribution}
\end{array}}
```

A method is selected because its mathematical structure and assumptions are compatible with the engineering mechanism and decision problem, not because it appears in a relevant paper.

---

## Minimum-mathematics principle

The governing optimization principle for methodological complexity is:

```math
\boxed{\textbf{Use the minimum mathematics necessary to explain the physics correctly, solve the engineering problem, quantify uncertainty, and produce a defensible sustainable decision.}}
```

Complexity has no intrinsic scientific value. Additional mathematical structure is justified only if it improves explanation, prediction, control, decision quality, uncertainty characterization, or falsifiability.

---

## Application to the seven-stage thesis framework

This reasoning protocol is cross-cutting. It applies within and between all seven stages:

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

```math
\boxed{\text{What exactly justifies this arrow?}}
```

The answer must ultimately be traceable to definitions, evidence, mechanism, mathematics, assumptions, tests, verification/validation results, and a stated domain of validity.
