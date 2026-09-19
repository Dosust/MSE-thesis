# Stage 6 Spatiotemporal Sustainability Trajectory Amendment v1.1

**Status:** CANONICAL ADDITIVE STAGE-6 ACCOUNTING AMENDMENT  
**Effective date:** 2026-09-19  
**Parent:** \`STAGE6_SUSTAINABILITY_ACCOUNTING_PROTOCOL_V1.md\`  
**Cross-stage authority:** P1.11.5  
**Empirical H4 closure:** NOT IMPLIED

## 1. Core vector retained

~~~math
\boxed{
\mathbf J_{\rm sus}^{core}
=
[
J_{\rm access},
J_{\rm energy},
J_{\rm carbon},
J_{\rm cost}
]^\top.
}
~~~

No component is automatically a requirement.

## 2. Spatiotemporal consequence operator

For each qualified component:

~~~math
\boxed{
J_j
=
\int_{t_0}^{t_f}
\int_{\Omega}
\ell_j(\mathbf r,t)\,d\mu(\mathbf r)\,dt
+
J_j^{emb}
}
~~~

or the equivalent discrete/network sum.

Every calculation declares:
- spatial domain;
- temporal/lifecycle horizon;
- system/process boundary;
- functional unit;
- perspective;
- units;
- uncertainty;
- source/provenance.

## 3. Accounting-state implementation

Where cumulative consequences need dynamic bookkeeping:

~~~math
\dot b_j=L_j(t).
~~~

These are implementation/accounting states:

~~~math
\boxed{
b_j\notin Y^{phys}
}
~~~

unless an independent physical model explicitly gives the quantity a physical-state role.

## 4. Coupled-SoS burden-shifting gate

~~~math
\boxed{
G_{\rm burden}
=
G_{\rm boundary}
\land
G_{\rm cross-sector}
\land
G_{\rm lifecycle}
\land
G_{\rm doublecount}
\land
G_U.
}
~~~

A sustainability claim is BLOCKED if a material burden is shifted outside the declared boundary without disclosure/justification.

## 5. Horizon separation

Report, when relevant:

~~~math
\mathbf J_{\rm sus}^{op}
~~~

and

~~~math
\mathbf J_{\rm sus}^{life/trans}.
~~~

Do not combine them without explicit temporal normalization/discounting/accounting rule.

## 6. Accessibility

Accessibility may serve both:
- Stage-5 service acceptability/resilience;
- Stage-6 social sustainability consequence.

Separate IDs/definitions must be retained for the two uses to avoid double counting or threshold leakage.

## 7. Cost versus efficiency

~~~math
\boxed{
J_{\rm cost}\neq\mathcal E_{\rm fy}.
}
~~~

A resource may feed both calculations, but the result objects and denominators/aggregation rules remain distinct.

## 8. Stage-7 handoff

Stage 6 passes the vector and its accounting metadata losslessly:

~~~text
component_id
value/result object
native unit
boundary_id
horizon
functional_unit
uncertainty
provenance
validity
requirement_role
claim_ceiling
~~~

## 9. Claim boundary

~~~math
\boxed{
\mathbf J_{\rm sus}\ \text{computed}
\not\Rightarrow
\text{sustainability improved}
\not\Rightarrow
H4\ \text{supported}.
}
~~~
