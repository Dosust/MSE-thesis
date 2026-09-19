# Stage 6 Efficiency Resource and Evaluation Protocol v2

**Status:** CANONICAL STAGE-6 EFFICIENCY PROTOCOL  
**Effective date:** 2026-09-19  
**Authority:** Canonical Intervention-Performance Amendment v2.1  
**Purpose:** represent resource-performance explicitly without forcing heterogeneous resources into an unjustified scalar.

## 1. Definition

Efficiency asks:

> What evidence-supported resources were required to obtain the achieved intervention outcome?

\`\`\`math
\boxed{
\text{Efficiency}
=
\text{resource use relative to achieved outcome}.
}
\`\`\`

It is not effectiveness:

\`\`\`math
\boxed{
\text{efficient}
\not\Rightarrow
\text{effective}.
}
\`\`\`

and:

\`\`\`math
\boxed{
\text{effective}
\not\Rightarrow
\text{efficient}.
}
\`\`\`

## 2. Resource vector

For \(a_k\),

\`\`\`math
\boxed{
\mathbf C_{\rm res}^{a_k}
=
[
C_1^{a_k},\ldots,C_m^{a_k}
]^\top.
}
\`\`\`

Candidate resource dimensions include:

- incremental implementation cost;
- implementation time;
- crew/person-hours;
- material quantity;
- implementation energy;
- equipment/fleet utilization;
- land/space;
- outage/work-window burden;
- other engineering resources with qualified evidence.

A candidate dimension enters confirmatory efficiency analysis only if definition, unit, boundary, provenance and uncertainty treatment are explicit.

## 3. Resource record

Every resource component requires:

\`\`\`text
resource_id
intervention_id
definition
unit
incremental/absolute flag
perspective
temporal boundary
functional unit
source/provenance
uncertainty
validation status
double-counting flag
status
\`\`\`

## 4. Efficiency representation

The primary Stage-6 efficiency object is:

\`\`\`math
\boxed{
\mathcal E_{\rm fy}(a_k)
=
(
\mathbf C_{\rm res}^{a_k},
\boldsymbol\eta_R^{a_k},
\mathcal P_{\rm fy}^{a_k},
\Lambda_{\rm fy}^{a_k}
).
}
\`\`\`

where:

- \(\mathbf C_{\rm res}\): resource vector;
- \(\boldsymbol\eta_R\): valid resource-performance ratios;
- \(\mathcal P_{\rm fy}\): vector/Pareto dominance relations in resource-performance space;
- \(\Lambda_{\rm fy}\): validity/claim limits.

## 5. Ratio diagnostics

For a positive, resolvable incremental resource denominator:

\`\`\`math
\eta_{R,m}(a)
=
\frac{\Delta\mathcal M_R(a)}
{\Delta R_m(a)}.
\`\`\`

A target-based alternative may use an achieved-effect quantity \(g_{\rm fx}(a)\) when its meaning and units are justified.

Ratios are prohibited when:

- denominator crosses zero under uncertainty;
- denominator is numerically indistinguishable from zero;
- sign convention makes interpretation unstable;
- numerator and denominator represent incompatible functional/service bases.

Then report:

\`\`\`math
(
\text{achieved outcome},
\Delta R_m
)
\`\`\`

rather than inventing a stabilizing constant.

## 6. Multi-resource efficiency

No default weighted sum is authorized:

\`\`\`math
\boxed{
\mathcal E_{\rm fy}
\neq
w^\top\boldsymbol\eta_R
}
\`\`\`

unless a value model is independently justified.

Preferred representations are:

- native-unit resource vector;
- normalized ratios with explicit reference values;
- Pareto dominance;
- bounded efficiency classes;
- scenario-robust resource-performance relations.

## 7. Efficiency versus sustainability accounting

A resource may also have sustainability consequences, but the roles must remain explicit.

Example:

\`\`\`math
C_{\rm capex}^{resource}
\neq
J_{\rm cost}^{lifecycle}
\quad\text{by default}.
\`\`\`

Likewise implementation energy may be a resource while lifecycle energy is a broader consequence.

Every shared quantity must declare:

- which boundary is used for efficiency;
- which boundary is used for sustainability;
- whether values are incremental or absolute;
- how double counting is prevented.

## 8. Efficiency V&V gate

\`\`\`math
\boxed{
G_{6-EFY}
=
G_{res}
\land
G_{unit}
\land
G_{boundary}
\land
G_{denom}
\land
G_{unc}
\land
G_{valid}
\land
G_{double}.
}
\`\`\`

PASS requires:

- resource inventory sufficiently complete;
- units/perspective explicit;
- boundaries frozen;
- denominator mathematically admissible;
- uncertainty propagated;
- intended-use validation adequate;
- no unacknowledged double counting.

## 9. Efficiency uncertainty

Report uncertainty for both achieved outcome and resource denominator.

For ratio \(\eta=N/D\), ratio uncertainty must not be approximated as negligible when denominator uncertainty is material.

If distributions are not defensibly probabilistic, use interval/scenario envelopes.

## 10. Matched comparison

Efficiency comparisons across interventions require common:

- scenario;
- functional/service specification;
- resource definition;
- accounting perspective;
- temporal boundary;
- target/resilience output definition.

## 11. Deferred values

Remain DEFERRED:

- actual resource quantities;
- resource distributions;
- ratio thresholds;
- normalization references;
- efficiency dominance results;
- any scalar efficiency index.

## 12. Claim boundary

An efficiency result describes resource-performance under its declared boundary. It does not establish sustainability, equity, resilience sufficiency, or final engineering preference.
