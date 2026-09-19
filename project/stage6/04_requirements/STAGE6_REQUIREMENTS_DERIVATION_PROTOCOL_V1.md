# Stage 6 Sustainability Requirements Derivation Protocol v1

## 1. Purpose

Stage 6 does not only measure consequences. It converts qualified evidence and intervention results into candidate requirements for Stage 7.

A consequence is descriptive:

\[
\Delta J_q(a_k).
\]

A requirement is normative:

\[
J_q(a_k)\;\mathrel{\mathcal R}\;\theta_q.
\]

The second does not follow automatically from the first.

\[
\boxed{
\text{observed consequence}
\not\Rightarrow
\text{normative threshold}
}
\]

## 2. Requirement object

Each candidate requirement is represented as:

\[
\boxed{
r_q=
(
\text{dimension},
\text{metric},
\mathcal R,
\theta_q,
\text{unit},
FU_6,
\mathcal B,
H,
\text{beneficiary/perspective},
\text{provenance},
\mathbb U_{\theta},
\text{enforcement status}
)
}
\]

where \(\mathcal R\in\{\le,\ge,=,\text{report-only}\}\).

## 3. Provenance classes

Reuse the thesis provenance logic.

### A — mandatory/authoritative

Law, regulation, adopted code, binding utility/agency requirement, contractual requirement, or directly applicable mandatory standard.

### B — formally adopted stakeholder/community/organizational goal

A documented and authorized target tied to the declared beneficiary/community/organization.

### C — scientific/engineering benchmark

Peer-reviewed literature, voluntary standard/guidance, industry convention or comparative benchmark.

### D — preregistered research assumption

A thesis-defined threshold used for sensitivity, methodological testing or experimental classification.

## 4. Promotion rule

A requirement may enter the Stage-7 hard feasible set only if:

\[
\boxed{
G_{\rm auth}
\land
G_{\rm metric}
\land
G_{\rm scope}
\land
G_{\rm unit}
\land
G_{\rm uncertainty}
\land
G_{\rm applicability}
=PASS.
}
\]

In general:

- Class A can become hard if applicable to the case.
- Class B can become hard only when the target is formally authorized for the case.
- Class C remains a benchmark/engineering target unless separately adopted.
- Class D remains a research threshold/sensitivity condition and is never relabeled A/B after results.

## 5. Sustainability requirement classes

### Social/accessibility

Examples of admissible requirement forms:

\[
A_g(a)\ge A_g^{min}
\]

or

\[
\Delta A_g(a)\ge -\theta_{loss,g}.
\]

The beneficiary group, opportunity type, time window and accessibility definition must be frozen.

An aggregate accessibility target cannot substitute for a group-specific target when the requirement is explicitly distributional.

### Energy/resource

\[
J_{\rm energy}(a)\le\theta_E
\]

or a component-specific resource cap.

### Carbon

\[
J_{\rm carbon}(a)\le\theta_C.
\]

The carbon boundary, gases, GWP convention, lifecycle stages and electricity-factor method must be declared.

### Cost

\[
J_{\rm cost}^{(p)}(a)\le\theta_{COST}^{(p)}.
\]

The perspective \(p\), currency year, discount rate and analysis period are mandatory.

### Extended environment/social

Only if the method and inventory pass the corresponding environmental or S-LCA evidence gate.

## 6. Requirements from resilience diagnosis

Stage-5 diagnosis can indicate what needs protection or improvement, but not necessarily how much.

Example logic:

\[
\mathcal D_R
\rightarrow
\text{critical service/interface}
\rightarrow
\text{candidate requirement domain}.
\]

The numerical target then requires an independent provenance source.

Thus:

\[
\boxed{
\text{diagnosis identifies relevance;}
\quad
\text{authority/evidence establishes the requirement}.
}
\]

## 7. Conflict and feasibility audit

Candidate requirements can conflict.

Define:

\[
\mathcal K_{6}^{cand}
=
\bigcap_q K_q.
\]

Before Stage 7, test whether:

\[
\mathcal K_{6}^{cand}\neq\varnothing
\]

over the qualified intervention set.

If the intersection is empty, Stage 6 reports a requirement conflict. It does not resolve the conflict by inventing weights.

## 8. Uncertainty in requirements

Distinguish:

- measurement uncertainty in the metric;
- model uncertainty in consequence prediction;
- uncertainty in the threshold itself;
- normative/value disagreement.

Physical/statistical uncertainty belongs to VVUQ.

Normative/value disagreement is not reducible to a probability distribution unless there is a justified elicitation model. It is passed to Stage 7 as value/decision uncertainty.

## 9. Requirement derivation gate

A requirement record passes only if it includes:

1. exact metric;
2. direction of preference/constraint;
3. threshold or report-only status;
4. unit;
5. functional unit;
6. system and lifecycle boundary;
7. time horizon;
8. beneficiary/cost bearer where relevant;
9. provenance class;
10. uncertainty;
11. applicability;
12. rationale;
13. conflict status;
14. Stage-7 role.

## 10. Claim ceiling

Stage 6 may state:

“Intervention \(a_k\) violates/satisfies the declared Stage-6 candidate requirement under the specified boundary and uncertainty model.”

It may not state:

“Intervention \(a_k\) is the most sustainable choice.”

That is a Stage-7 decision claim.
