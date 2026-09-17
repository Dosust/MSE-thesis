# Sustainability-Dimension Admission and Accounting Standard — v1.0

**Status:** CURRENT THESIS-WIDE STAGE-6/7 MEASUREMENT AUTHORITY  
**Effective date:** 2026-09-18  
**Degree:** MSE Sustainable Engineering, Arizona State University  
**Scientific authority:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Framework authority:** `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**Method authority:** `../../project/EGMIV_METHOD_V1.md`  
**Writing/inference authority:** `SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`  
**Experiment authority:** `MODEL_EXPERIMENT_VALIDATION_MATRIX.md`  
**Live dimension register:** `SUSTAINABILITY_DIMENSION_REGISTER_V1.md`

---

## 1. Purpose

This standard governs how sustainability, resource-efficiency, economic, accessibility and transformation quantities are admitted, defined, measured, compared, validated and interpreted throughout the thesis.

It prevents three common errors:

```math
\boxed{
\text{resilience improvement}
\not\Rightarrow
\text{sustainability improvement}
}
```

```math
\boxed{
\text{a quantity that sounds sustainable}
\not\Rightarrow
\text{an admissible thesis metric}
}
```

```math
\boxed{
\text{persistent infrastructure change}
\not\Rightarrow
\text{sustainable transformation}
}
```

The standard is deliberately non-compensatory: a dimension cannot become admissible merely because it scores highly on some criteria while failing a necessary scientific gate such as mechanism, data, units, accounting boundary or decision relevance.

The governing workflow is

```math
\boxed{
\text{Evidence}
\rightarrow
\text{Role typing}
\rightarrow
\text{Admission gates}
\rightarrow
\text{Metric specification}
\rightarrow
\text{Accounting boundary}
\rightarrow
\text{Comparator}
\rightarrow
\text{VVUQ}
\rightarrow
\text{H4/H5 decision use}
\rightarrow
\text{bounded inference}.
}
```

---

## 2. Scientific basis and evidence boundary

The direct coupled Power--Transportation (P--T) resilience literature already includes service restoration, budget/resource allocation, economic loss, energy use, low-carbon control, carbon-aware robust planning and persistent infrastructure investments. Therefore this thesis must not claim that resilience--sustainability integration, carbon-aware P--T resilience, or structural P--T planning is absent from the field.

Representative direct precedents include:

- Fotouhi, Moryadee, and Miller-Hooks (2017), coupled traffic--power resilience quantification, `10.1016/j.ress.2017.01.026`;
- Zou and Chen (2019), cost-effective mitigation/repair allocation in interdependent traffic--power systems, `10.1016/j.ress.2019.106557`;
- Chen et al. (2021), distribution--traffic--human recovery with repair resources and economic loss, `10.1155/2021/2051719`;
- Wang, Fang, and Zio (2022), post-disruption coupled traffic--power reconfiguration, `10.1016/j.ress.2022.108408`;
- Zhen, Lin, and Zhou (2022), planning and operation for green-port traffic--power resilience, `10.1016/j.ress.2022.108569`;
- Kong, Zhang, and Dai (2022), commercial-EV scheduling for damaged P--T restoration, `10.1109/EI256261.2022.10117220`;
- Qiu et al. (2022), P--T EV resilience control with carbon-intensity service, `10.1109/TII.2022.3166215`;
- Sun et al. (2025), low-carbon traffic resilience-enhanced robust planning with carbon-emission flow and persistent P--T investment, `10.1016/j.apenergy.2025.126258`.

Adjacent infrastructure evidence is admissible only for method transfer, not as proof of direct P--T precedent. Mitoulis, Bompa, and Argyroudis (2023), for example, explicitly separate transport-infrastructure resilience, greenhouse-gas emissions and cost (`10.1016/j.trd.2023.103800`).

Standards/frameworks are used for measurement discipline and breadth checks, not as proof that a dimension belongs in this thesis. ISO 14040/14044 govern life-cycle-assessment principles, goal/scope, inventory, impact assessment and interpretation if full LCA is activated. ISO 14067 governs product carbon-footprint quantification and permits partial carbon-footprint studies when their boundary is explicit. Envision is used only as a breadth/checklist reference for infrastructure sustainability categories; its rating system is not adopted as the thesis objective function.

---

## 3. Role ontology: every quantity must have one primary scientific role

Before admission, each candidate quantity must be assigned one primary role in the relevant experiment.

| Code | Primary role | Meaning | Example |
|---|---|---|---|
| `R-SVC` | resilience/service state | defines or measures service maintainability/recovery | electricity served, unmet trips, recovery time |
| `RES` | resource / efficiency input | resource consumed to obtain an outcome | crew-hours, MWh used, direct intervention cost |
| `SUS` | sustainability consequence | environmental/social/economic consequence explicitly measured beyond resilience itself | kg CO2e, distributional accessibility loss |
| `FEAS` | feasibility constraint | limits what can physically, financially or organizationally be done | budget, crew count, capacity, implementation time |
| `TRANS` | transformation descriptor | describes a persistent system change | added storage MW/MWh, charger location, hardened line |
| `CTX` | contextual significance only | relevant to discussion but not quantitatively modeled | biodiversity when no causal/data route exists |

A quantity may be relevant to more than one domain, but it must have **one declared primary role per confirmatory test**. This prevents double counting and semantic drift.

Examples:

```math
\boxed{
\text{travel accessibility used in }K_{\rm svc}
\Rightarrow
R\text{-SVC, not automatically SUS}
}
```

```math
\boxed{
\text{renewable capacity}
\Rightarrow
TRANS, not automatically SUS}
}
```

```math
\boxed{
\text{budget}
\Rightarrow
FEAS, not a sustainability outcome}
}
```

---

## 4. Canonical Stage-6/7 consequence object

For a persistent candidate intervention `a_k`, the thesis uses the typed consequence record

```math
\boxed{
\mathcal C(a_k)
=
\left(
\Delta\mathfrak R^{a_k},
\mathbf r^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k},
\mathcal F^{a_k},
\mathbf U^{a_k}
\right)
}
```

where:

- `\Delta\mathfrak R^{a_k}` = resilience consequence relative to the declared baseline;
- `\mathbf r^{a_k}` = resource/efficiency vector;
- `\Delta\mathbf J_{\rm sus}^{a_k}` = admitted sustainability-consequence vector;
- `\mathcal F^{a_k}` = feasibility conditions and constraints;
- `\mathbf U^{a_k}` = uncertainty associated with the consequence/decision.

This object refines but does not replace canonical H4:

```math
\boxed{
a_k\rightarrow
\left(
\Delta\mathfrak R^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k}
\right).
}
```

The additional typed vectors ensure that cost, energy, labor, budget and other quantities are not silently relabeled as complete sustainability.

---

## 5. Sustainability-Dimension Admission Matrix

For each candidate dimension `j`, define the admission record

```math
\boxed{
\mathcal A_j
=
(M_j,Q_j,X_j,D_j,U_j,B_j,K_j,V_j,S_j)
}
```

with nine non-compensatory gates.

### G1 — Mechanism (`M_j`)

**Question:** Is there a physically, operationally, economically or socially defensible causal path

```math
\boxed{
a_k\rightarrow J_j?}
```

Required evidence:

- explicit mechanism in direct/transferable literature or governing physics/accounting;
- direction of effect and intermediate variables;
- applicability conditions.

**Fail examples:** biodiversity, public health or water use added only because they are generally important sustainability topics without an intervention-to-consequence mechanism in the declared case.

### G2 — RQ/H decision relevance (`Q_j`)

**Question:** Can the quantity answer RQ6/H4 or alter the RQ7/H5 engineering decision?

A dimension must support at least one of:

```math
\text{effectiveness},
\quad
\text{resource efficiency},
\quad
\text{sustainability consequence},
\quad
\text{feasibility},
\quad
\text{decision-set change}.
```

Descriptive interest alone is insufficient.

### G3 — Construct validity and non-duplication (`X_j`)

**Question:** Does the metric represent a distinct construct rather than relabeling a quantity already used elsewhere?

Mandatory checks:

- resilience metric vs sustainability consequence;
- service accessibility vs distributional/equity accessibility;
- operational energy vs energy-derived carbon;
- direct cost vs monetized service loss;
- renewable capacity vs environmental outcome;
- recovery time vs time-dependent economic loss.

If two metrics share the same underlying quantity, the overlap must be declared and aggregation must avoid double counting.

### G4 — Data and provenance (`D_j`)

**Question:** Can the quantity be computed from admissible data with traceable provenance?

Priority:

```math
\boxed{
\text{measured/site/official data}
>
\text{peer-reviewed empirical/full-text evidence}
>
\text{qualified benchmark data}
>
\text{sensitivity-only assumption}.
}
```

Sensitivity-only assumptions cannot support empirical sustainability claims.

### G5 — Units and metric specification (`U_j`)

**Question:** Does the quantity have explicit units/dimensions and a reproducible calculation?

Examples:

- energy: `kWh`, `MWh`, `MJ`;
- carbon: `kg CO2e`, `t CO2e`;
- cost: declared currency and price year;
- labor: crew-hours/person-hours;
- accessibility: explicitly defined physical or dimensionless accessibility index;
- time: minutes/hours/days.

Dimensionless indices require their formula, normalization and reference range. Physical-unit outputs must be retained even if normalized copies are used for visualization or multi-criteria analysis.

### G6 — Accounting/system boundary (`B_j`)

**Question:** Are the included and excluded processes unambiguous?

Every admitted consequence must declare, as applicable:

1. spatial boundary;
2. temporal horizon;
3. infrastructure assets included;
4. intervention life stage(s): construction, operation, recovery, maintenance, end-of-life;
5. direct vs indirect effects;
6. baseline/reference case;
7. allocation rule where shared processes exist;
8. price/emission-factor year and geography;
9. exclusions and their expected bias.

A metric without an accounting boundary is not confirmatory.

### G7 — Comparator/counterfactual (`K_j`)

**Question:** Relative to what is the consequence interpreted?

Default H4 form:

```math
\boxed{
\Delta J_j^{a_k}
=
J_j(a_k)-J_j(a_{\rm ref})
}
```

where `a_ref` is declared before confirmatory execution.

For project-level GHG claims, the counterfactual/baseline must be explicit. If a carbon calculation is framed as a project-reduction claim, the applicable GHG project-accounting requirements must be followed rather than simply multiplying selected activity data by an emission factor and calling the difference a verified reduction.

### G8 — VVUQ / uncertainty (`V_j`)

**Question:** Can uncertainty and adequacy be assessed?

At minimum, record:

- uncertain inputs/factors;
- model/measurement uncertainty;
- sensitivity factors capable of changing the decision;
- validation/benchmark route;
- propagation method or deterministic justification;
- uncertainty reported with the result.

A metric that cannot support any defensible adequacy or uncertainty statement remains exploratory.

### G9 — MSE-scope feasibility (`S_j`)

**Question:** Can the dimension be analyzed rigorously without creating a separate thesis?

Examples of scope expansion requiring explicit activation include:

- full multi-category LCA;
- comprehensive social life-cycle assessment;
- epidemiological health-impact modeling;
- biodiversity/ecosystem-service assessment;
- economy-wide/macroeconomic modeling.

Scientific importance is not sufficient for thesis admission.

---

## 6. Gate states and admission rule

Each gate is recorded as:

- `PASS` — requirement is presently satisfied;
- `COND` — scientifically defensible but a declared prerequisite remains open;
- `FAIL` — requirement is not satisfied for the thesis scope;
- `N/A` — only when the gate is genuinely inapplicable, with justification.

No weighted score can override a failed hard gate.

Admission status is determined as follows.

### `IN`

A dimension may enter a confirmatory H4/H5 response/decision vector only when all applicable gates are `PASS` and its role is frozen.

### `CONDITIONAL`

Use when mechanism, decision relevance and construct validity pass, but one or more execution gates such as data, boundary, VVUQ or scope require completion. A conditional dimension may be developed or explored but cannot support a confirmatory claim until its open gates pass.

### `ROLE-ONLY`

Use when the quantity is essential to the thesis but belongs to `R-SVC`, `RES`, `FEAS` or `TRANS` rather than `SUS`. It must not be inserted into `\mathbf J_{\rm sus}` merely to enlarge the sustainability vector.

### `OUT`

Use when mechanism, relevance, construct validity or scope fails, or when the required evidence/data cannot be made adequate within the declared thesis.

### `CONTEXT`

Use for important sustainability topics that may be discussed as limitations/transferability but are not modeled or measured.

A data failure after preregistration produces `NOT TESTED`, not zero effect and not hypothesis falsification.

---

## 7. Evidence-strength coding

Admission status and evidence strength are distinct.

| Code | Evidence meaning |
|---|---|
| `E-PT-Q` | direct coupled P--T study quantitatively operationalizes the dimension |
| `E-PT-C` | direct coupled P--T study provides contextual/implicit support but not a quantitative sustainability metric |
| `E-ADJ-Q` | adjacent infrastructure study quantitatively operationalizes a transferable method |
| `E-STD` | recognized standard/framework governs measurement/boundary practice |
| `E-CON` | conceptual/theoretical support only |
| `E-0` | no admissible support located in the bounded audit |

Evidence code does not itself admit a dimension. For example, a dimension may have strong literature precedent but still be excluded because required data are unavailable in the selected case.

---

## 8. Canonical metric specification card

Every dimension with status `IN` or `CONDITIONAL` must have a metric card before Chapter 4 confirmatory execution.

```text
Dimension ID:
Name:
Primary role: R-SVC / RES / SUS / FEAS / TRANS / CTX
RQ/SO/H mapping:
Scientific mechanism:
Symbol:
Definition/equation:
Units:
Preferred direction: higher/lower/target-range
Baseline/reference intervention:
Spatial boundary:
Temporal horizon:
Lifecycle stage(s):
Included processes/assets:
Excluded processes/assets:
Data source(s) and provenance:
Parameter/emission-factor provenance:
Calculation/model implementation:
Uncertainty model:
Sensitivity variables:
Verification route:
Validation/benchmark route:
Comparator/counterfactual:
Materiality threshold: NOT FROZEN until preregistered
Double-counting check:
Evidence code(s):
Admission status:
Version/date:
Owner/thesis location:
```

Missing information must remain explicitly `PENDING`; it must not be replaced with invented assumptions.

---

## 9. Accounting-boundary rules

### 9.1 Carbon/GHG

A carbon result must state whether it is:

- operational/event carbon;
- intervention/construction carbon;
- partial carbon footprint;
- lifecycle carbon footprint;
- avoided/project GHG effect.

These are not interchangeable.

If a life-cycle carbon-footprint claim is made, the applicable ISO 14040/14044 and ISO 14067 principles/requirements must be followed and the exact standard version frozen. If a project-emission-reduction claim is made, an appropriate project-accounting framework and counterfactual must be declared.

The thesis must not call an operational-emissions calculation a full LCA.

### 9.2 Cost

Every cost metric must record:

- currency;
- price year;
- real vs nominal basis;
- discount rate if multi-period present-value calculations are used;
- included CAPEX/OPEX/recovery/service-loss components;
- whether service-loss monetization is already represented elsewhere.

Cost is an economic/resource consequence, not synonymous with complete economic sustainability.

### 9.3 Energy

Energy accounting must distinguish:

- electricity consumed;
- fuel energy;
- storage charge/discharge losses;
- emergency-resource energy;
- embodied energy if activated;
- renewable curtailment/absorption where relevant.

If carbon is derived from energy, the dependency must be recorded to prevent double weighting.

### 9.4 Accessibility

The thesis distinguishes:

```math
\boxed{
A_{\rm svc}(t)
\neq
A_{\rm dist}(g,t)
}
```

where `A_svc` is aggregate transportation-service accessibility and `A_dist` is population/group-distributional accessibility. The former normally belongs to resilience/service performance; the latter may be a social sustainability consequence only if population/group data, metric definition and validation pass the admission gates.

### 9.5 Materials and lifecycle impacts

Material quantity alone is a resource measure. Environmental impacts from materials require an explicit inventory/factor method and boundary. Multi-category lifecycle claims require an activated LCA protocol rather than ad hoc impact labels.

---

## 10. Anti-double-counting rules

The following are prohibited unless an explicit dependency-aware aggregation rule is justified:

1. including travel time/unmet trips in resilience and again as an identically defined sustainability metric;
2. including operational energy and energy-derived carbon in a scalar index as if independent without declaring the intended weighting/dependency;
3. including direct cost and monetized service loss when the direct cost already contains the same loss term;
4. treating renewable share/capacity both as an intervention descriptor and an environmental outcome;
5. treating recovery time as both resilience and economic loss without exposing the economic conversion model;
6. treating crew-hours both as a resource input and labor cost without noting the deterministic relationship;
7. summing normalized dimensions simply because they have been normalized.

Normalization removes units; it does not establish commensurability or preference weights.

---

## 11. H4 rule — intervention consequence heterogeneity

H4 is tested on matched scenarios and declared intervention sets.

For intervention `a_k`:

```math
\boxed{
\mathcal C(a_k)
=
(\Delta\mathfrak R^{a_k},\mathbf r^{a_k},\Delta\mathbf J_{\rm sus}^{a_k},\mathcal F^{a_k},\mathbf U^{a_k}).
}
```

The confirmatory H4 question is whether resilience-effective interventions differ materially in admitted resource/sustainability consequences.

A valid H4 comparison requires:

- same disturbance/scenario ensemble;
- same service requirements;
- same metric definitions/accounting boundaries;
- same price/emission-factor conventions;
- declared feasibility rules;
- preregistered materiality criterion `\delta_4` or equivalent;
- uncertainty on both resilience and consequence quantities.

No current document freezes a numerical `\delta_4`; selecting it after viewing confirmatory outcomes is prohibited.

---

## 12. H5 rule — decision value of sustainability information

H5 compares the same candidate intervention set under two information/decision formulations:

```math
\boxed{
\mathcal A_R^{\star}
\quad\text{vs}\quad
\mathcal A_{R,S}^{\star}.
}
```

Default Stage-7 analysis is **vector-valued and nondominance/Pareto-based** unless a scientifically justified preference model is available.

A weighted scalar score is not the default because weights encode preferences and can hide trade-offs.

Scalarization may be used only when:

1. weights/utilities have an external or explicitly elicited justification;
2. normalization is declared;
3. sensitivity to weights is reported;
4. physical-unit results remain visible;
5. the unweighted/nondominated structure is retained as a comparator where feasible.

The H5 claim is supported only if the preregistered set-change/regret/decision metric exceeds its declared materiality rule within the validation domain.

---

## 13. Transformation admission rule

The thesis distinguishes operation from persistent transformation.

```math
\boxed{
u(t)=\text{operate the current architecture}}
```

versus

```math
\boxed{
a_k=\text{persistently change architecture/capability/rules}.}
```

Examples of `u(t)`:

- switching;
- EV/V2G dispatch;
- repair routing;
- temporary traffic reconfiguration;
- emergency price/control signals.

Examples of candidate `a_k`:

- hardening or adding a line;
- adding/relocating charging infrastructure;
- adding storage or distributed/renewable generation;
- persistent road/network redundancy;
- persistent sensing/communication capability;
- durable change in repair-resource capacity;
- persistent organizational/authority arrangement, if operationalized.

An action qualifies as a **sustainable-transformation candidate** only if its persistent nature is explicit and its consequence record is evaluated under the admitted dimensions. The term does not imply that the outcome is sustainable before H4/H5 analysis.

---

## 14. VVUQ and reporting rules

For every admitted metric `J_j`, Chapter 4 must predeclare:

```math
\boxed{
J_j
=f_j(D_j,\theta_j,a_k,\omega),
\qquad
\omega\in\Omega
}
```

with data/parameter provenance and uncertainty semantics.

Required controls include, where applicable:

- dimensional/unit tests;
- independent recalculation for accounting formulas;
- conservation/balance checks;
- benchmark or published-range comparison;
- sensitivity to emission factors, prices, discount rates or demand assumptions;
- scenario uncertainty;
- numerical convergence when optimization/simulation is used;
- uncertainty intervals/distributions or explicit deterministic justification.

Reporting states are distinct:

- `0` = calculated/observed zero;
- `N/A` = not applicable by definition;
- `MISSING` = required data unavailable;
- `NOT TESTED` = prerequisite gate failed or analysis not executed.

They must never be substituted for one another.

---

## 15. Thesis-wide chapter integration

| Thesis location | Required use of this standard |
|---|---|
| **1.5 Sustainable Engineering Significance** | explain why resilience effectiveness, resource efficiency and sustainability consequences must remain distinct; cite only evidence-supported candidate dimensions |
| **1.6 Scope/Boundaries/Assumptions** | state which dimensions are IN/CONDITIONAL/OUT and the high-level accounting boundaries |
| **2.21 Resilience and Sustainability Integration** | establish evidence strength, direct P--T precedents, adjacent transferable methods and counterevidence |
| **2.23 Adaptive Infrastructure Transformation** | distinguish temporary operation from persistent transformation and establish precedent boundaries |
| **Chapter 3 Stage 6** | formally define `\mathbf r`, `\mathbf J_sus`, metric roles and transformation consequence mapping |
| **Chapter 3 Stage 7** | define feasible/nondominated decision objects without hidden preference weights |
| **Chapter 4 H4/H5** | freeze metric cards, intervention set, accounting boundaries, comparators, uncertainty and materiality rules before confirmatory execution |
| **Chapter 5** | report admitted physical-unit results and uncertainty; do not retrofit excluded metrics |
| **Chapter 6** | interpret trade-offs, rival explanations, burden shifting, limitations and transferability |
| **Chapter 7** | answer RQ6/RQ7 only for dimensions that survived the admission and VVUQ chain |

---

## 16. Freeze and amendment rules

The standard itself is stable; the live register evolves until the H4/H5 measurement freeze.

Before confirmatory H4/H5 execution, the repository must contain a dated freeze identifying:

- final candidate intervention set;
- final admitted dimension set;
- each metric card;
- baseline/reference intervention;
- accounting boundaries;
- factor/data versions;
- uncertainty model;
- materiality/decision rules.

After that freeze, changing any primary dimension, metric equation, accounting boundary, emission factor family, price basis, comparator, aggregation rule or materiality threshold requires a dated amendment stating:

1. reason for change;
2. whether confirmatory results had already been observed;
3. impact on confirmatory vs exploratory status;
4. affected RQ/H/result/conclusion IDs.

A post-result change cannot be silently presented as preregistered.

---

## 17. Completion gate for an admitted sustainability dimension

A dimension `j` is confirmatory-ready only if

```math
\boxed{
G_{\rm sus}(j)
=
M_j\land Q_j\land X_j\land D_j\land U_j\land B_j\land K_j\land V_j\land S_j.
}
```

All applicable terms must be `PASS`.

This condition is stronger than a checklist total because the gates are not mutually substitutable.

---

## 18. Governing scientific interpretation

This thesis does not define sustainable engineering as maximization of a generic sustainability score. The adopted interpretation is:

```math
\boxed{
\begin{aligned}
\text{Sustainable engineering decision}
=
&\ \text{service/resilience adequacy}\\
&+\ \text{feasible resource use}\\
&+\ \text{explicitly bounded sustainability consequences}\\
&+\ \text{uncertainty-aware comparison of alternatives}.
\end{aligned}
}
```

The plus signs are conceptual, not scalar addition.

The core scientific question is therefore not whether a candidate intervention can be labeled sustainable, but whether adding admissible sustainability/resource information changes a defensible engineering decision relative to resilience-only evaluation.

---

## 19. Key methodological references

- International Organization for Standardization. (2006). *ISO 14040:2006 Environmental management — Life cycle assessment — Principles and framework* (current edition confirmed 2022; amendments/version must be checked at execution).
- International Organization for Standardization. (2006). *ISO 14044:2006 Environmental management — Life cycle assessment — Requirements and guidelines* (current edition confirmed 2022; amendments/version must be checked at execution).
- International Organization for Standardization. (2018). *ISO 14067:2018 Greenhouse gases — Carbon footprint of products — Requirements and guidelines for quantification* (current published edition; revision status must be checked when used).
- Institute for Sustainable Infrastructure. (2018/2024 materials). *Envision Sustainable Infrastructure Framework*. Used as a breadth/checklist reference only.
- Mitoulis, S.-A., Bompa, D. V., & Argyroudis, S. (2023). Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery. *Transportation Research Part D: Transport and Environment, 121*, 103800. https://doi.org/10.1016/j.trd.2023.103800
- Sun, Y., Huang, X., Wang, G., et al. (2025). Low-carbon traffic resilience-enhanced robust planning of coupled transportation and power distribution network based on modified user equilibrium model. *Applied Energy, 397*, 126258. https://doi.org/10.1016/j.apenergy.2025.126258
- World Resources Institute & World Business Council for Sustainable Development. *GHG Protocol for Project Accounting*. Exact current version/status must be checked if project-level avoided-emissions claims are made.

---

## 20. Authority rule

When thesis text, code, figures or experiment plans use the words **sustainability**, **sustainable transformation**, **resource efficiency**, **carbon**, **energy consequence**, **accessibility consequence**, **economic consequence**, or **joint resilience--sustainability decision**, this standard and the live dimension register must be consulted.

No sustainability dimension may enter a confirmatory thesis claim outside this governance chain.