# Stage 2 — Case-Independent Causal Governance Contract v1

**Canonical title:** **Stage 2 — Evidence-Grounded Causal Interdependencies**  
**Normative status:** **FROZEN FRAMEWORK AUTHORITY**  
**Execution status:** **Stage 2 remains ACTIVE; case applications are not frozen**  
**Scope:** **Power–Transportation interdependencies only**  
**Canonical RQ2:** **Why and through which mechanisms do components and layers affect each other?**  
**Canonical SO2:** Establish evidence-supported directional causal mechanisms, activation conditions, parameters, uncertainties and validity boundaries linking Power and Transportation components and layers.

---

## 1. Scientific role

Stage 1 establishes structural possibility. Stage 2 determines causal admissibility.

\`\`\`math
\boxed{
\mathfrak r_e^{(1)}
\longrightarrow
\mathfrak c_{e,c}^{(2)}
\longrightarrow
\mathfrak I_{e,c}
}
\`\`\`

where:

- \(\mathfrak r_e^{(1)}\): frozen Stage-1 structural candidate;
- \(\mathfrak c_{e,c}^{(2)}\): case-specific causal candidate under investigation;
- \(\mathfrak I_{e,c}\): qualified causal Power–Transportation interdependency in case \(c\).

Stage 2 answers:

\`\`\`math
\boxed{
\text{Which candidate }P\leftrightarrow T\text{ relations are genuinely causal,}
\;
\text{why, through what mechanism, and under what conditions?}
}
\`\`\`

The Stage-2 contribution is:

> **A case-independent causal-governance framework for Power–Transportation interdependencies that uses heterogeneous evidence to determine which candidate \(P\leftrightarrow T\) relations can be promoted to causal interdependencies, which cannot, why, and under what conditions qualified causal mechanisms activate.**

---

## 2. Case-invariance principle

Let \(D^{(c)}\) denote evidence available for case \(c\), and let \(\mathcal R_{G_2}\) denote the Stage-2 causal rules.

\`\`\`math
\boxed{
\mathcal R_{G_2}+D^{(c)}
\rightarrow
\text{case-specific causal classification}
}
\`\`\`

The rules are invariant across cases:

\`\`\`math
\boxed{
\mathcal R_{G_2}^{(1)}
=
\mathcal R_{G_2}^{(2)}
=
\cdots
=
\mathcal R_{G_2}.
}
\`\`\`

Therefore:

- case data may change;
- candidate counts may change;
- accepted causal sets may change;
- activation states may change;
- parameters may change;
- **the causal promotion rules may not be modified merely to fit a case result**.

A change to \(\mathcal R_{G_2}\) requires formal amendment and re-audit.

---

## 3. Causal interpretation criterion

A directional relation \(X_e\rightarrow Y_e\) is treated as causal only when the evidence supports a declared mechanism \(m_e\), realized interface/exchange \(\Phi_e\), activation condition \(\mathcal A_e\), validity domain \(\mathcal V_e\), and receiver response such that a feasible change in the source would change the receiver through the declared pathway while relevant rival explanations are controlled or bounded.

Conceptually:

\`\`\`math
\boxed{
P\!\left(
Y_e
\mid
do(X_e=x_1),
\mathcal A_e=1,
\mathcal V_e
\right)
\neq
P\!\left(
Y_e
\mid
do(X_e=x_0),
\mathcal A_e=1,
\mathcal V_e
\right)
}
\`\`\`

for at least two feasible source states \(x_0,x_1\), when an interventional interpretation is meaningful.

For an engineering/deterministic mechanism, the corresponding criterion may be:

\`\`\`math
\boxed{
\psi_e(x_1;\theta_e)
\neq
\psi_e(x_0;\theta_e)
}
\`\`\`

under the declared activation and validity conditions.

This criterion does not require one universal causal-identification method. Physics-based, empirical, operational, quasi-experimental, intervention-based, or other defensible evidence routes may be used when appropriate to the mechanism.

---

## 4. Two-layer causal status system

### 4.1 Evidence-maturity / causal-status ontology

For each candidate relation \(e\) in case \(c\):

| Code | Status | Meaning |
|---|---|---|
| \(S_0\) | **STRUCTURAL_ONLY** | topology, proximity or interface possibility only |
| \(S_1\) | **ASSOCIATED_ONLY** | statistical/operational association exists; causality unresolved |
| \(S_2\) | **MECHANISM_CANDIDATE** | plausible directional mechanism exists |
| \(S_3\) | **CASE_CONNECTED** | actual source–interface–receiver pathway is verified |
| \(S_4\) | **BLOCKED** | causal claim remains plausible but decisive required evidence is unavailable |
| \(S_5\) | **FALSIFIED_CLAIM** | the declared causal claim is contradicted or shown inapplicable in the declared case/domain |
| \(S_6\) | **QUALIFIED_CAUSAL** | all Stage-2 causal gates pass |

**Important:** \(S_5\) falsifies the **declared causal claim**, not every possible causal pathway between the two infrastructures.

### 4.2 G2 decision state

Final \(G_2\) decisions are only:

\`\`\`text
PASS
FAIL
BLOCKED
\`\`\`

\`OPEN\` is a workflow state before final decision.

Mapping:

\`\`\`text
G2 = PASS     -> S6 QUALIFIED_CAUSAL
G2 = FAIL     -> S5 FALSIFIED_CLAIM
G2 = BLOCKED  -> S4 BLOCKED
G2 = OPEN     -> S0/S1/S2/S3 depending on evidence maturity
\`\`\`

This prevents early-stage evidence maturity from being confused with a final causal decision.

---

## 5. Exact Stage-2 causal dossier

For every candidate relation:

\`\`\`math
\boxed{
\mathfrak D_{e,c}^{(2)}
=
\left(
\mathfrak r_e^{(1)},
\mathcal C_e,
\Sigma_e,
\Pi_e,
S_e^\theta,
S_{e,c},
G_2(e,c)
\right)
}
\`\`\`

with causal claim:

\`\`\`math
\boxed{
\mathcal C_e
=
(src_e,rec_e,d_e,\gamma_e,\Phi_e)
}
\`\`\`

and mechanism:

\`\`\`math
\boxed{
\Sigma_e
=
(m_e,\mathcal A_e,\psi_e,\theta_e,\tau_e).
}
\`\`\`

Evidence / uncertainty / validity / falsification:

\`\`\`math
\boxed{
\Pi_e
=
(
\mathcal E_e^{(2)},
\mathcal U_e,
\mathcal V_e,
\mathcal F_e
).
}
\`\`\`

Every relation must explicitly answer:

1. **Source** — what changes first?
2. **Receiver** — what responds?
3. **Direction** — \(P\rightarrow T\) or \(T\rightarrow P\)?
4. **Interface** — through what physical, operational, informational or organizational boundary?
5. **Exchange** \(\Phi_e\) — what service/resource/information/action crosses or enables the relation?
6. **Mechanism** \(m_e\) — why does the receiver respond?
7. **Activation** \(\mathcal A_e\) — under what conditions does the mechanism operate?
8. **Response** \(\psi_e\) — how does receiver state change?
9. **Parameters** \(\theta_e\) — what mechanism parameters are required?
10. **Delay/timescale** \(\tau_e\) — when does the response occur?
11. **Evidence** \(\mathcal E_e^{(2)}\) — what supports the claim?
12. **Uncertainty** \(\mathcal U_e\) — what remains unresolved?
13. **Validity** \(\mathcal V_e\) — where, when, and for which configurations does the claim apply?
14. **Falsification** \(\mathcal F_e\) — what observation/test would reject or revise the claim?

---

## 6. Hard non-causality invariants

None of the following independently establishes a causal Power–Transportation interdependency:

\`\`\`math
\boxed{
\text{topology}\neq\text{causality}
}
\`\`\`

\`\`\`math
\boxed{
\text{proximity}\neq\text{causality}
}
\`\`\`

\`\`\`math
\boxed{
\text{correlation}\neq\text{causality}
}
\`\`\`

\`\`\`math
\boxed{
\text{literature mechanism}\neq\text{case causal relation}
}
\`\`\`

\`\`\`math
\boxed{
\text{standardized interface}\neq\text{case implementation}
}
\`\`\`

\`\`\`math
\boxed{
\text{simulation assumption}\neq\text{causal evidence}
}
\`\`\`

Common-cause rule:

\`\`\`math
\boxed{
\eta\rightarrow P,
\qquad
\eta\rightarrow T
\not\Rightarrow
P\rightarrow T
\text{ or }
T\rightarrow P.
}
\`\`\`

Reciprocity rule:

\`\`\`math
\boxed{
P\leftrightarrow T
\text{ requires two separately qualified arrows: }
P\rightarrow T
\text{ and }
T\rightarrow P.
}
\`\`\`

The two directions may have different mechanisms, interfaces, activation conditions, delays, evidence, uncertainty and validity domains.

---

## 7. Universal causal gate

A candidate becomes a qualified causal P–T interdependency only through:

\`\`\`math
\boxed{
G_2(e,c)
=
G_{2-M}
\land
G_{2-C}
\land
G_{2-X}
\land
G_{2-A}
\land
G_{2-E}
\land
G_{2-V}
\land
G_{2-F}.
}
\`\`\`

| Gate | Required proof |
|---|---|
| \(G_{2-M}\) | explicit, evidence-supported, non-circular mechanism |
| \(G_{2-C}\) | actual case source–interface–receiver connection |
| \(G_{2-X}\) | exchanged/enabling quantity or service explicitly defined |
| \(G_{2-A}\) | activation conditions explicit and supported |
| \(G_{2-E}\) | evidence supports the causal claim after alternatives/contrary evidence |
| \(G_{2-V}\) | validity domain explicitly bounded |
| \(G_{2-F}\) | concrete falsification/revision test exists |

Aggregate logic:

\`\`\`text
if any decisive component = FAIL          -> G2 = FAIL
else if any required component = BLOCKED -> G2 = BLOCKED
else if all seven components = PASS      -> G2 = PASS
else                                      -> workflow state = OPEN
\`\`\`

Promotion rule:

\`\`\`math
\boxed{
G_2(e,c)=PASS
\iff
e
\text{ may be called a qualified causal Power–Transportation interdependency in case }c.
}
\`\`\`

Before \(G_2=PASS\), the relation must retain its actual status and must not be described as a qualified causal interdependency.

---

## 8. Evidence governance

Stage 2 permits heterogeneous evidence:

\`\`\`math
\boxed{
\mathcal E_e^{(2)}
=
\{
E^{physics},
E^{literature},
E^{empirical},
E^{operational},
E^{case},
E^{standard},
E^{negative}
\}.
}
\`\`\`

Evidence types have different evidentiary roles.

Examples:

- a standard may establish interface feasibility but cannot independently pass \(G_{2-C}\);
- correlation may support association but cannot independently pass \(G_{2-M}\);
- literature may establish a generic mechanism family but cannot independently pass case connection;
- simulation may test consequences of an admissible relation but cannot manufacture causal evidence.

No default weighted evidence score is authorized.

\`\`\`math
\boxed{
\text{evidence confidence}
\neq
\text{causal strength}.
}
\`\`\`

All evidence used for a final \(G_2\) decision must retain provenance and traceability.

---

## 9. Uncertainty governance

For every candidate:

\`\`\`math
\boxed{
\mathcal U_e
=
(
U_e^{conn},
U_e^{act},
U_e^{interface},
U_e^{time},
U_e^{response},
U_e^{parameter},
U_e^{alternative}
).
}
\`\`\`

Additional mechanism-specific components may be added when justified, but existing components may not be silently collapsed.

Uncertainty must not be converted into an arbitrary scalar confidence score unless a separately validated scoring model is formally introduced.

Parameter status remains distinct:

\`\`\`math
\boxed{
S_e^\theta
\in
\{
\mathrm{UNESTIMATED},
\mathrm{BOUNDED},
\mathrm{CALIBRATED},
\mathrm{VALIDATED}
\}.
}
\`\`\`

and:

\`\`\`math
\boxed{
G_2(e,c)=PASS
\not\Rightarrow
S_e^\theta=\mathrm{VALIDATED}.
}
\`\`\`

---

## 10. Causal existence, activation and strength are distinct

A qualified causal mechanism may exist but be inactive at time \(t\):

\`\`\`math
\boxed{
G_2(e,c)=PASS,
\qquad
\mathcal A_e(t)=0.
}
\`\`\`

Therefore:

\`\`\`math
\boxed{
\text{causal existence}
\neq
\text{activation}
\neq
\text{causal strength}.
}
\`\`\`

The active causal set is:

\`\`\`math
\boxed{
\mathbb I_{\mathrm{active}}^{(c)}(t)
=
\{
e:
G_2(e,c)=PASS
\land
\mathcal A_e(t)=1
\}.
}
\`\`\`

---

## 11. Candidate-status trajectory

Stage 2 must preserve the evidentiary evolution of every candidate:

\`\`\`math
\boxed{
S_{e,c}^{(0)}
\rightarrow
S_{e,c}^{(1)}
\rightarrow
\cdots
\rightarrow
S_{e,c}^{final}.
}
\`\`\`

Admissible examples include:

\`\`\`text
STRUCTURAL_ONLY
 -> MECHANISM_CANDIDATE
 -> CASE_CONNECTED
 -> QUALIFIED_CAUSAL
\`\`\`

\`\`\`text
STRUCTURAL_ONLY
 -> ASSOCIATED_ONLY
 -> MECHANISM_CANDIDATE
 -> FALSIFIED_CLAIM
\`\`\`

\`\`\`text
STRUCTURAL_ONLY
 -> MECHANISM_CANDIDATE
 -> BLOCKED
\`\`\`

No rejected, falsified or blocked relation may be silently deleted from the audit trail.

---

## 12. Case-level outputs

For case \(c\), Stage 2 returns:

\`\`\`math
\boxed{
\mathcal O_2^{(c)}
=
\left(
\mathbb I_{\mathrm{causal}}^{(c)},
\mathbb I_{\mathrm{blocked}}^{(c)},
\mathbb I_{\mathrm{falsified}}^{(c)},
\mathbb I_{\mathrm{structural}}^{(c)},
\mathbb I_{\mathrm{associated}}^{(c)},
\mathbb I_{\mathrm{candidate}}^{(c)},
\mathbf S^{(c)}
\right).
}
\`\`\`

Different cases may legitimately return different accepted causal sets:

\`\`\`math
\boxed{
D^{(1)}\neq D^{(2)}
\Rightarrow
\mathbb I_{\mathrm{causal}}^{(1)}
\neq
\mathbb I_{\mathrm{causal}}^{(2)},
}
\`\`\`

while the causal rules remain invariant.

For every qualified relation:

\`\`\`math
\boxed{
\mathfrak I_{e,c}
=
(
\mathcal C_e,
\Sigma_e,
\Pi_e,
S_e^\theta
).
}
\`\`\`

---

## 13. Stage-2 to Stage-3 boundary

Stage 2 does not simulate coupled dynamics to establish causality.

It hands Stage 3 only relations that pass causal qualification and the separate readiness gate:

\`\`\`math
\boxed{
G_{2\rightarrow3}(e,c)
=
G_2(e,c)
\land
G_P(e,c).
}
\`\`\`

\(G_P\) asks whether the accepted mechanism has a sufficiently explicit response form, parameter status, timescale and uncertainty representation for the intended Stage-3 implementation without inventing missing dynamics.

Stage 2 provides, as applicable:

\`\`\`math
\boxed{
\mathbb I_{\mathrm{causal}}^{(c)}
+
\mathcal A_e
+
\psi_e
+
\tau_e
+
\theta_e
+
\mathcal U_e
+
\mathcal V_e.
}
\`\`\`

The boundary rule is:

\`\`\`math
\boxed{
\text{Stage 2 decides which causal arrows are scientifically admissible;}
\quad
\text{Stage 3 studies their coupled dynamical consequences.}
}
\`\`\`

---

## 14. Stage-2 definition of done

Stage 2 is complete only when all required generic and case-specific obligations are satisfied.

### 14.1 Generic framework obligations

| Exit requirement | Required state |
|---|---|
| Power–Transportation causal scope | FROZEN |
| causal interpretation criterion | FROZEN |
| causal/non-causal promotion rules | FROZEN |
| \(G_2\) gates | FROZEN |
| causal-status ontology | FROZEN |
| non-causality invariants | FROZEN |
| evidence governance | FROZEN |
| uncertainty governance | FROZEN |
| causal existence vs activation vs strength distinction | FROZEN |
| Stage-2 output schema | FROZEN |
| Stage-2→3 boundary rule | FROZEN |

### 14.2 Case-execution obligations

| Exit requirement | Required state before Stage-2 closure |
|---|---|
| every selected Stage-1 P–T candidate classified | COMPLETE |
| every candidate status trajectory retained | COMPLETE |
| every final causal claim has evidence provenance | COMPLETE |
| every qualified causal relation has validity + falsifier | COMPLETE |
| every blocked relation states exact missing evidence | COMPLETE |
| every failed relation retains contradiction/rejection evidence | COMPLETE |
| case-invariance of rules tested across intended case applications | VALIDATED |
| accepted relations assessed for \(G_{2\rightarrow3}\) readiness | COMPLETE |
| RQ2 answered from the resulting causal sets and mechanisms | COMPLETE |

The generic framework may be frozen before these case-execution obligations are complete. Freezing the framework does **not** close Stage 2.

---

## 15. Final logic

\`\`\`math
\boxed{
\begin{aligned}
\mathcal E_{PT}^{(c)}
&\rightarrow
\text{candidate }P\leftrightarrow T\text{ relations}
\\
&\xrightarrow{\mathcal R_{G_2}}
\text{causal-status evolution}
\\
&\rightarrow
\{
\text{qualified causal},
\text{blocked},
\text{falsified},
\text{structural},
\text{associated},
\text{candidate}
\}
\\
&\rightarrow
\mathbb I_{\mathrm{causal}}^{(c)}
\\
&\xrightarrow{\mathcal A_e(t)}
\mathbb I_{\mathrm{active}}^{(c)}(t)
\\
&\xrightarrow{G_{2\rightarrow3}}
\text{Stage 3}.
\end{aligned}
}
\`\`\`

---

## 16. Change control

This file is normative.

Any change to the following requires a formal Stage-2 framework amendment and re-audit before use:

- title, RQ2 interpretation or P–T scope;
- causal-status ontology;
- causal interpretation criterion;
- non-causality invariants;
- \(G_2\) component gates or aggregate decision logic;
- evidence-governance rules;
- uncertainty-governance rules;
- activation/existence distinction;
- Stage-2 output schema;
- Stage-2→3 boundary rule;
- Stage-2 definition-of-done criteria.

Case-specific evidence, classifications, parameters, activation states and \(G_{2\rightarrow3}\) outcomes may evolve under this frozen framework without reopening the framework itself.
