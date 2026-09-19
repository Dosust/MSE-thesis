# Stage 7 — Decision Objective, Pareto and Value Firewall v2

**Status:** CANONICAL STAGE-7 DECISION-ONTOLOGY PROTOCOL  
**Effective date:** 2026-09-19

## 1. Decision dimensions

Stage 7 receives distinct dimensions:

\`\`\`math
\boxed{
\mathfrak R,\quad
\mathcal E_{\rm fx},\quad
\mathcal E_{\rm fy},\quad
\mathbf J_{\rm sus},\quad
F,\quad
\mathbb U.
}
\`\`\`

They must remain distinguishable through the decision pipeline.

## 2. Ordered decision logic

\`\`\`math
\boxed{
\text{feasibility}
\rightarrow
\text{native-unit objectives}
\rightarrow
\text{dominance/Pareto}
\rightarrow
\text{preference model, if justified}.
}
\`\`\`

The reverse order is prohibited.

## 3. Dominance

Let \(f_j(a)\) be consistently oriented decision dimensions for feasible interventions. Intervention \(a_i\) dominates \(a_k\) iff

\`\`\`math
f_j(a_i)\preceq f_j(a_k)\quad\forall j,
\`\`\`

and

\`\`\`math
\exists j:\; f_j(a_i)\prec f_j(a_k).
\`\`\`

Direction conventions must be declared before dominance evaluation.

Define

\`\`\`math
\boxed{
\mathcal P_7
=
\operatorname{Pareto}(\mathcal A_7^{adm}).
}
\`\`\`

## 4. Native units first

Accessibility, energy, carbon, cost, resilience, effectiveness and efficiency components retain native units/status until a justified transformation is declared.

Normalization is a mathematical transformation, not a value judgment by itself, but the choice of bounds/reference strongly affects interpretation and therefore requires provenance and sensitivity.

## 5. Value firewall

\`\`\`math
\boxed{
\text{evidence}
\neq
\text{requirement}
\neq
\text{stakeholder preference}
\neq
\text{weight}.
}
\`\`\`

Scientific literature may support consequence models or requirements. It cannot, by itself, determine stakeholder weights.

## 6. Preference model

Any value model must declare

\`\`\`math
\boxed{
\mathcal V_7
=
(
d,
\mathcal O,
\mathcal ELIC,
\mathbf w,
\mathcal N,
U_V,
\mathcal S_V
),
}
\`\`\`

where:
- \(d\): decision actor;
- \(\mathcal O\): objectives included;
- \(\mathcal ELIC\): elicitation procedure;
- \(\mathbf w\): weights/value parameters, if any;
- \(\mathcal N\): normalization/transformation;
- \(U_V\): value uncertainty;
- \(\mathcal S_V\): sensitivity protocol.

If these do not exist:

\`\`\`math
\boxed{
\text{do not invent weights}.
}
\`\`\`

The scientifically valid output remains a feasible/nondominated set.

## 7. No mandatory scalar score

\`\`\`math
\boxed{
\text{multi-dimensional decision record}
\not\Rightarrow
\text{single scalar utility}.
}
\`\`\`

A scalar score is permitted only when the value model is explicit, justified, sensitivity-tested, and not confused with empirical evidence.

## 8. Unique-winner firewall

\`\`\`math
\boxed{
\text{nondominated set}
\not\Rightarrow
\text{unique optimum}.
}
\`\`\`

A unique \(a^\star\) is defensible only when:
1. an admissible decision rule exists;
2. values/weights/constraints required by that rule are explicit;
3. uncertainty/decision stability is evaluated;
4. the rule was not selected because it favors a preferred intervention.

## 9. Stage-7 output classes

Allowed outputs include:

- admissible set;
- dominated/nondominated classification;
- Pareto front/set;
- satisficing set;
- robust nondominated set;
- regret profile;
- vulnerability domain;
- preference-sensitive ranking, when justified;
- unique preferred intervention, only under a valid value rule.

## 10. Protected DEFERRED fields

Remain DEFERRED:
- stakeholder weights;
- normalization constants tied to final case values;
- utility functions;
- unique winner;
- normative trade-off thresholds.

## 11. Claim boundary

Pareto dominance is a descriptive mathematical relation under declared objectives. It is not itself a normative recommendation.
