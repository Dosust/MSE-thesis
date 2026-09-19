# Stage 6 Scope, Boundary and Functional-Unit Protocol v1

## 1. Scope statement

Stage 6 evaluates the consequences of qualified strategic interventions for the coupled Power–Transportation system.

It includes:

1. resilience diagnosis carried forward from Stage 5;
2. explicit intervention definitions;
3. intervention-induced changes to the coupled physical model;
4. resilience effectiveness;
5. resource efficiency;
6. accessibility/social-distribution consequences;
7. lifecycle energy and environmental consequences;
8. lifecycle cost consequences;
9. derivation of evidence-qualified sustainability requirements for Stage 7;
10. uncertainty and validity limits.

It excludes:

- final intervention selection or ranking;
- adaptive pathway sequencing as a primary analysis;
- unqualified P↔T mechanisms;
- automatic monetization of social/environmental impacts;
- universal sustainability weights;
- claiming carbon reduction as complete environmental sustainability;
- claiming accessibility improvement as complete social sustainability.

## 2. Physical system boundary

The physical Stage-6 foreground begins with the same qualified P–T model used by Stages 3–5.

\[
\mathfrak M^0
=
(\mathcal G,\mathbb I^{qualified},F_{\mathcal G}^{m},\mathcal U_{\rm feas})
\]

Every intervention must state which object it changes:

\[
a_k:
\quad
\mathcal G,\;
\mathbb I,\;
F,\;
\mathcal U,\;
K
\rightarrow
\text{modified object}.
\]

A strategic intervention may not introduce a cross-infrastructure causal mechanism that failed or bypassed Stage 2/3 qualification.

## 3. Two time domains

### Event/resilience time

\[
t\in[0,T_5]
\]

governs hazard, degradation, control and recovery.

### Lifecycle time

\[
\tau\in[0,H_{LC}]
\]

governs construction, operation, maintenance, replacement and end-of-life consequences.

The two horizons must not be conflated.

Financial discounting applies only to monetary streams where justified. Physical energy, emissions and accessibility are not discounted using a financial discount rate unless an independently justified method explicitly requires temporal weighting.

## 4. Functional-service specification

ISO 14040/14044 make a functional unit central to comparative life-cycle assessment.

For this thesis, the case-specific functional-service specification is represented before numerical binding as:

\[
\boxed{
FU_6
=
(
\mathcal Q_P^{req},
\mathcal Q_T^{req},
\mathcal P_{served},
\mathcal X,
H_{LC},
\Omega_6
)
}
\]

where:

- \(\mathcal Q_P^{req}\): declared power-service function;
- \(\mathcal Q_T^{req}\): declared transportation-service/accessibility function;
- \(\mathcal P_{served}\): population/critical functions/beneficiaries served;
- \(\mathcal X\): fixed geographic/system boundary;
- \(H_{LC}\): common lifecycle analysis period;
- \(\Omega_6\): common hazard/demand/scenario basis.

All intervention alternatives must satisfy the same declared function or clearly report the service difference instead of pretending functional equivalence.

## 5. Lifecycle boundary

Environmental and cost accounting should include, where relevant:

\[
\boxed{
\mathcal B_{LC}
=
\{
\text{materials/manufacture},
\text{transport},
\text{construction/installation},
\text{operation},
\text{maintenance},
\text{replacement},
\text{hazard repair},
\text{end of life}
\}
}
\]

A partial boundary is allowed only when it is explicitly labeled, justified by goal/scope, and applied consistently to all comparators.

ISO 14040 emphasizes a lifecycle perspective to reveal burden shifting between lifecycle stages.

## 6. Foreground and background data

### Foreground

Quantities directly changed by intervention \(a_k\), such as:

- line/transformer/charger/storage capacity;
- road/corridor intervention quantities;
- construction materials;
- operational electricity/fuel;
- maintenance/replacement;
- travel time/accessibility;
- service restoration;
- hazard repair.

### Background

Factors and inventories not dynamically simulated by the P–T model:

- material production factors;
- electricity/fuel environmental factors;
- manufacturing inventories;
- end-of-life factors;
- unit-cost factors.

Every background dataset must be versioned by source, year, geography, technology and unit.

## 7. Social boundary

Stage 6 uses two distinct social layers.

### Layer S1 — operational community consequences

These may include, if data support them:

- accessibility to jobs, healthcare, education, emergency services or other declared opportunities;
- power service to declared critical/community functions;
- travel-time burden;
- outage/recovery burden;
- affordability/user burden where costs are passed to users;
- spatial and population-group distribution of those consequences.

Geurs and van Wee (2004, DOI 10.1016/j.jtrangeo.2003.10.005) show that accessibility measures must be selected for theoretical validity, interpretability and data requirements, and that location/utility-based measures can improve policy evaluation.

Pereira, Schwanen and Banister (2017, DOI 10.1080/01441647.2016.1257660) establish that transport equity requires an explicit distributive principle and attention to how benefits and burdens are distributed.

### Layer S2 — lifecycle social impacts

If the thesis makes supply-chain/organizational social claims, use an explicit S-LCA scope consistent with ISO 14075:2024 and UNEP (2020), identifying relevant stakeholder categories and impact categories.

If S2 data are unavailable, the thesis must state:

\[
\boxed{
\text{operational accessibility/social distribution assessed}
\neq
\text{full social life-cycle sustainability assessed}
}
\]

## 8. Environmental boundary

Core H4 outcomes are energy and carbon, but environmental rigor is two-tiered.

### Core confirmatory layer

\[
J_{\rm energy},\qquad J_{\rm carbon}
\]

### Extended environmental layer

Where inventory quality permits, report additional impact categories using a declared LCIA method, for example EPA TRACI categories such as acidification, eutrophication, smog formation, human-health impacts and ecotoxicity.

No extended impact category is added solely because it is available in software.

## 9. Economic boundary and perspective

Cost results must declare the bearer/perspective:

\[
p\in
\{
\text{asset owner},
\text{utility/agency},
\text{user},
\text{system},
\text{society}
\}.
\]

ISO 15686-5:2017 requires an agreed period and clear cost scope for life-cycle costing. NIST SP 1197 compares future cost/benefit streams of resilience investments with the status quo and explicitly recognizes co-benefits, non-market values and uncertainty.

Different perspectives are reported separately unless a justified societal accounting convention combines them.

## 10. Boundary consistency gate

For alternatives \(a_i,a_j\),

\[
\boxed{
G_{6-BND}=PASS
}
\]

only if:

\[
FU_6^{a_i}=FU_6^{a_j},
\quad
\mathcal B_{LC}^{a_i}=\mathcal B_{LC}^{a_j},
\quad
H_{LC}^{a_i}=H_{LC}^{a_j},
\quad
\Omega_6^{a_i}=\Omega_6^{a_j},
\]

or every difference is explicitly part of the declared treatment and normalization rule.

## 11. Sources

ISO 14040:2006; ISO 14044:2006; ISO 14075:2024; ISO 15686-5:2017; UNEP (2020) Guidelines for Social Life Cycle Assessment of Products and Organizations; NIST SP 1197; EPA TRACI; Geurs & van Wee (2004); Pereira et al. (2017).
