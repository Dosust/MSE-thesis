# Stage 5 Sustainability-Constraint Firewall v1

**Status:** CANONICAL ADDITIVE STAGE-5 CLARIFICATION  
**Effective date:** 2026-09-19  
**Parent:** \`STAGE5_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md\` and \`STAGE5_MATHEMATICAL_AMENDMENT_V1_1.md\`  
**Purpose:** prevent sustainability consequence metrics from silently becoming viability constraints  
**Empirical H3 closure:** NOT IMPLIED

## 1. Default Stage-5 object is unchanged

~~~math
\boxed{
K(t)
=
\{
Y:
h_r(Y,t)\le0,\ r\in\mathcal R_{\rm qualified}
\}.
}
~~~

Stage 5 remains resilience-focused.

## 2. Sustainability metric does not imply constraint

~~~math
\boxed{
J_j\ \text{defined/computed}
\not\Rightarrow
J_j\le B_j\ \text{is authoritative}.
}
~~~

A hard sustainability/resource bound requires a P1.8-qualified requirement record with:
- RID/version;
- source/authority;
- applicability;
- formal expression;
- threshold/bound;
- units;
- spatial/temporal aggregation;
- uncertainty;
- validity/effectivity.

## 3. Conditional augmented state

If a qualified cumulative bound genuinely requires trajectory memory, an accounting state may be appended:

~~~math
\bar Y^{acct}
=
(Y^{phys},b).
~~~

Permanent:

~~~math
\boxed{
Y^{phys}\neq\bar Y^{acct}.
}
~~~

## 4. Conditional sustainable-viability object

Only after all relevant hard-constraint gates pass may a separate extension be formed:

~~~math
K_{\rm sus}(t)
\subseteq
\mathcal X_{phys}\times\mathcal X_{acct}
~~~

and a corresponding sustainable-viability set computed.

This does not replace:
- \(\mathcal V_T^x\);
- \(\mathcal V_{\alpha,T}^b\);
- H3's canonical viability/reachability test.

Any sustainable-viability result is a separately scoped analysis unless prospectively incorporated into a future preregistered hypothesis.

## 5. BLOCKED rule

If a proposed carbon/energy/cost/accessibility bound lacks authoritative provenance:

~~~math
\boxed{
G_{K_{\rm sus}}=BLOCKED.
}
~~~

The underlying sustainability metric may still be reported in Stage 6.

## 6. Claim boundary

~~~math
\boxed{
\text{sustainable-viability computation}
\neq
\text{H3 support}
\neq
\text{proof that the system is sustainable}.
}
~~~
