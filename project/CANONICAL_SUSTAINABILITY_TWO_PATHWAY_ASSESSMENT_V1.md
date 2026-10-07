# Canonical Two-Pathway Sustainability Assessment V1

**Status:** CANONICAL — FROZEN THESIS SUSTAINABILITY ASSESSMENT AUTHORITY  
**Effective date:** 2026-10-07  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Thermal-scope authority:** `CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`  
**Resilience authority:** `CANONICAL_RESILIENCE_DEFINITION_V1.md`  
**Effectiveness / energy-efficiency placement authority:** `CANONICAL_EFFECTIVENESS_ENERGY_EFFICIENCY_PLACEMENT_V1.md`

## 1. Canonical definition

> **Sustainability in this thesis is assessed through two pathways: (1) the direct environmental, economic, and social consequences of thermal interdependencies on electricity and mobility services, and (2) the environmental, economic, and social consequences of engineering responses used to improve, adapt, or restore those services. Both pathways are evaluated within a declared system boundary and time horizon.**

Short form:

> **The thesis assesses sustainability through two pathways: the direct sustainability consequences of thermal interdependencies and the sustainability consequences of engineering responses. Each pathway is evaluated across environmental, economic, and social dimensions and linked to relevant SDG targets only through measurable indicators.**

## 2. One sustainability framework, two pathways

The thesis uses **one sustainability framework**, not two competing definitions.

### Pathway 1 — Direct consequence

```text
Extreme Heat
→ Thermal State / Capability Change
→ Thermal Interdependency
→ Electricity + Mobility Service Consequence
→ Sustainability Consequence
```

This pathway quantifies how the disturbance and thermal interdependency change sustainability performance relative to an appropriate reference case.

### Pathway 2 — Engineering-response consequence

```text
Improve / Adapt / Restore
→ Changed Physical State / Capability / Operation
→ Changed Electricity + Mobility Service
→ Sustainability Consequence
```

This pathway quantifies how an engineering response changes sustainability performance relative to the corresponding extreme-heat case without that response.

## 3. Sustainability dimensions

Use the vector

```math
\mathbf S =
\begin{bmatrix}
S_{\mathrm{env}}\\
S_{\mathrm{econ}}\\
S_{\mathrm{soc}}
\end{bmatrix}.
```

The three dimensions are evaluated in parallel. They are **not automatically aggregated into a single scalar sustainability score**.

### 3.1 Environmental

> **Environmental performance concerns the energy, emissions, and material/resource burden associated with providing required electricity and mobility services.**

Core indicator families:

- energy use and additional energy demand;
- energy efficiency, under the placement authority;
- electrical or conversion losses where relevant;
- greenhouse-gas emissions or equivalent climate burden where defensible emission factors are available;
- material/resource burden and equipment replacement burden where materially affected by the thermal mechanism or engineering response.

Do not add water, land, biodiversity, waste, or other environmental categories unless they are relevant to the adopted system boundary and supported by data.

### 3.2 Economic

> **Economic performance concerns the cost of providing, maintaining, disrupting, and recovering required electricity and mobility services.**

Core indicator families:

- operating and energy cost;
- maintenance and replacement cost;
- engineering-response or intervention cost;
- service-disruption cost where a defensible valuation method exists.

Do not expand this into a macroeconomic assessment unless explicitly authorized.

### 3.3 Social

> **Social performance concerns how the thermal disturbance and engineering response affect people's access to, continuity of, affordability of, equity in, and safety of electricity and mobility services.**

Core indicator families:

- service access;
- service continuity;
- affordability, where measurable;
- equity of service, where measurable;
- safety, where relevant and measurable.

The strongest default social indicators are access, continuity, and equity of service. Affordability and safety enter only when the data and causal connection are defensible.

## 4. Comparison architecture

The canonical comparison contains three cases:

```text
Reference / Baseline
→ Extreme Heat without Engineering Response
→ Extreme Heat with Engineering Response
```

Define:

```math
\mathbf S_0 = \text{sustainability indicators in the reference case},
```

```math
\mathbf S_H = \text{sustainability indicators under extreme heat without response},
```

```math
\mathbf S_A = \text{sustainability indicators under extreme heat with engineering response}.
```

Pathway 1 consequence:

```math
\Delta\mathbf S_H = \mathbf S_H-\mathbf S_0.
```

Pathway 2 consequence:

```math
\Delta\mathbf S_A = \mathbf S_A-\mathbf S_H.
```

Total change relative to the reference case:

```math
\mathbf S_A-\mathbf S_0
=
(\mathbf S_H-\mathbf S_0)
+
(\mathbf S_A-\mathbf S_H).
```

This algebraic decomposition is valid only when the same indicator definition, units, system boundary, accounting convention, and time horizon are used across the compared cases.

## 5. Indicator directionality and interpretation

Each sustainability indicator must declare:

- definition and unit;
- system boundary;
- time horizon;
- reference case;
- whether higher values are beneficial or burdensome;
- data source and uncertainty;
- any normalization or functional basis.

Do not interpret the sign of `ΔS` generically across mixed indicators. For example, higher emissions are adverse while higher service access is beneficial.

## 6. Service basis / functional basis

Sustainability indicators must remain connected to the electricity and mobility services actually delivered.

Where scientifically appropriate, compare burdens or costs per declared functional/service unit, for example:

```math
\frac{\text{environmental burden}}{\text{declared electricity or mobility service}},
```

or

```math
\frac{\text{economic cost}}{\text{declared electricity or mobility service}}.
```

The exact functional unit is **OPEN** until the electricity- and mobility-service metrics are frozen. A ratio is not mandatory when an absolute system-level indicator is the correct decision quantity.

## 7. SDG linkage rule

SDGs are an **interpretation layer after measurement**, not a causal or modeling layer.

Canonical mapping:

```text
Measured Sustainability Indicator
→ Sustainability Dimension
→ Relevant SDG Target / Indicator
```

Do not map a broad dimension directly to an SDG number without an indicator-to-target rationale.

Do not infer SDG contribution from thematic similarity alone.

Exact SDG targets remain **OPEN** until the corresponding thesis indicators are defined and measured.

## 8. Relationship to resilience

Resilience and sustainability remain distinct:

```text
Resilience
= ability to maintain or recover required electricity and mobility services through disturbance and recovery
```

```text
Sustainability
= environmental + economic + social consequences associated with providing those services and with engineering responses
```

Permanent rule:

```text
Resilience improvement ≠ sustainability improvement
```

An engineering response may improve resilience while increasing energy use, emissions, cost, material burden, or social inequity. Conversely, a sustainability benefit does not by itself establish resilience.

## 9. Effectiveness and energy-efficiency placement

The controlling placement is defined by `CANONICAL_EFFECTIVENESS_ENERGY_EFFICIENCY_PLACEMENT_V1.md`:

```text
Effectiveness → Resilience / Engineering-Response Assessment
Energy Efficiency → Environmental Sustainability
```

Preserve:

```text
Effectiveness ≠ Energy Efficiency ≠ Sustainability
Effective Resilience Response ≠ Sustainable Response
```

## 10. Anti-double-counting rule

The same physical consequence must not be counted twice within or across dimensions without an explicit reason.

Examples:

- electrical energy loss may be an environmental energy indicator; if monetized, the economic value must be labeled as a separate monetary representation of the same physical loss;
- service disruption may support both an economic cost and a social-access consequence, but the measures must remain distinct and must not be summed without a justified aggregation method.

## 11. Scope and feasibility boundary

This framework does **not** require:

- a full life-cycle assessment;
- a full social life-cycle assessment;
- economy-wide cost-benefit analysis;
- universal sustainability optimization;
- one scalar sustainability score;
- all SDGs;
- all environmental, economic, or social indicators.

Only indicators that are relevant to the thermal-interdependency mechanism, electricity/mobility service consequence, or engineering response and supported by data are admitted.

## 12. Research-objective relationship

The frozen GO and SO1–SO3 remain unchanged unless separately amended.

The two-pathway sustainability assessment is a **bounded downstream interpretation/assessment of the service consequences and engineering responses**. It does not create a fourth primary objective by itself.

## 13. Permanent thesis distinctions

```text
Thermal state ≠ capability ≠ service ≠ resilience ≠ sustainability
```

```text
Direct thermal-interdependency sustainability consequence
≠
engineering-response sustainability consequence
```

```text
Measured indicator ≠ sustainability dimension ≠ SDG target
```

## 14. Reopen conditions

This authority may be changed only through an explicit versioned amendment authorized by the user, supervisor/chair/committee direction, contradictory evidence or infeasibility, or a higher ASU/SSEBE requirement.
