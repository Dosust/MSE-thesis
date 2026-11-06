# Power–Electrified Transportation Interdependencies — Definitions, Physics and S0 Screening Guide

**Recorded:** 2026-11-06  
**Thesis:** *Engineering of Power–Electrified Transportation Interdependencies for Resilience*  
**Status:** Researcher-supplied conceptual and operational definition; **proposed screening guidance** to be applied with approved I1–I6/E01–E07. This document records the user's supplied interpretation; it is **not** a new human screening decision, independent full-text verification, finalized model, supervisor approval or modification of the canonical thesis objectives.

## 1. Established infrastructure-literature definition

An **infrastructure interdependency** is a relationship in which the state, operation or performance of one infrastructure system influences, or depends upon, another infrastructure system.

| Concept | Definition | Direction |
|---|---|---|
| **Dependency** | One infrastructure relies on the state, output or functioning of another. | \(P\rightarrow T\) |
| **Interdependency — strict** | Two infrastructures mutually influence or depend upon one another. | \(P\leftrightarrow T\) |
| **Interdependency — broader usage** | A network of one-way, reciprocal or multilevel dependencies. | Multiple connected pathways |

The strict reciprocal formulation is associated with **Rinaldi, Peerenboom and Kelly (2001)** and with government infrastructure guidance. The **NIST *Community Resilience Planning Guide*** also uses *interdependency* broadly to include one-way, reciprocal and multilevel relationships.

**Thesis choice:** Use the strict bidirectional framing for the **complete Power–Transportation system**, but register and evaluate each **individual directional dependency** independently. Consequently, a study documenting only \(T\rightarrow P\) can be important CORE evidence for a specific pathway without constituting proof of a complete reciprocal physical model.

**Attribution distinction:** The published frameworks motivate the terms. Our thesis-specific definition and mathematical representation below are a proposed research synthesis, **not verbatim IEEE/NIST definitions**.

## 2. Established classes of infrastructure interdependencies

Following the widely used Rinaldi classification:

| Type | Meaning | Illustrative Power–Transportation example |
|---|---|---|
| **Physical** | Output, resource flow or physical state of one infrastructure affects another. | EV charging current changes transformer loading. |
| **Cyber / information** | Operation relies on information or communication. | Charger operation responds to a network dispatch signal. |
| **Geographical** | Spatial proximity creates shared exposure and possible coupled consequences. | Extreme heat stresses neighboring transformers and charging assets. |
| **Logical** | Policies, economic decisions or institutional rules link infrastructure operations. | Charging restrictions are imposed by an operating policy. |

Our thesis concentrates on **physical interdependencies**. Information and organization mechanisms are supporting layers and do not replace physical evidence. Geographical co-location or a common heat hazard by itself should **not** be mistaken for verified cross-infrastructure causal propagation.

## 3. Proposed operational definition for the thesis

> **Power–electrified transportation interdependency** is a physically or operationally mediated relationship in which electrical infrastructure states, constraints or services influence electrified transportation, while transportation charging demand, operating states or control actions influence electrical infrastructure. Under extreme heat, these relationships are thermally conditioned, time-dependent and capable of propagating operational restrictions or service degradation between the two systems.

This is a **thesis-specific proposed definition derived from the infrastructure literature**.

### Domains and directional physical pathways

- **Extreme-heat forcing:** ambient temperature \(T_a(t)\), potentially affecting both domains.
- **Power system (P):** transformers, feeders, voltage, electrical current, thermal states and operating capacity.
- **Electrified transportation (T):** EVs, charging equipment, charging requests, battery state of charge (SOC), delivered energy and mobility service.
- **Transportation → Power (\(T\rightarrow P\)):** EV charging demand and charger control affect electrical loading, losses, transformer temperature and available capacity.
- **Power → Transportation (\(P\rightarrow T\)):** electricity supply, voltage or temperature-conditioned equipment limits affect charging availability and delivered transportation service.

**Important:** Bidirectional influence does **not** require EV battery energy export or V2G. Charge demand may affect a transformer, while grid-side constraints affect the subsequent ability to charge. Whether both effects actually occur, close a feedback loop and propagate in time must be established for each study or modeled scenario—not assumed from physical plausibility alone.

## 4. Mathematical definition

Let \(x_P(t)\) denote relevant electrical/thermal system states and \(x_T(t)\) denote charging/transportation states. A candidate coupled continuous-time formulation is:

\[
\boxed{
\begin{aligned}
\dot{x}_P &= f_P(x_P,x_T,T_a,u),\\
\dot{x}_T &= f_T(x_T,x_P,T_a,u).
\end{aligned}
}
\]

Where differentiable, a sufficient structural signal of *direct* two-way cross-state coupling is:

\[
\frac{\partial f_P}{\partial x_T}\not\equiv 0,
\qquad
\frac{\partial f_T}{\partial x_P}\not\equiv 0.
\]

These derivatives are **model diagnostics**, not a universal required test. Coupling may instead appear through algebraic constraints, shared boundary variables, control laws, discrete events or switching logic, especially in hybrid/DAE network models.

### Candidate physical propagation chain

\[
\boxed{
\begin{gathered}
\text{EV charging demand}\\
\downarrow\\
\text{Transformer current and heating}\\
\downarrow\\
\text{Temperature-dependent operating capacity}\\
\downarrow\\
\text{Available EV charging power}\\
\downarrow\\
\text{Delivered mobility service}
\end{gathered}
}
\]

**Evidence qualification:** This chain is a **proposed thesis-level mechanism**. Independent sources must verify its individual links, physical connectivity, operating thresholds, parameter values, feedback policies and temporal evidence. A study measuring EV load and a separate study measuring transformer temperature do not establish a connected field pathway.

**Transformer reference:** **IEEE C57.91-2025**, the applicable loading guide for oil-immersed transformers, addresses loading, ambient-temperature effects, insulation life and temperature criteria for its specified equipment scope. It is **not** itself a definition of infrastructure interdependency. Apply relevant standards to the actual equipment, not automatically to every EVSE or battery.

## 5. Application to the S0 100-paper human-screening exercise

An individual paper can provide **CORE evidence for only one direction** without presenting an end-to-end bidirectional model. The following are **suggested screening interpretations**, not prefilled researcher judgments or replacements for I1–I6/E01–E07.

| Evidence in a study | Suggested category / directional tag |
|---|---|
| EV charging demand affects transformer winding hot-spot temperature or insulation aging | **CORE — T→P** |
| Temperature-conditioned transformer capacity changes EV charging power or service | **CORE — P→T** |
| Both directions explicitly represented as a connected feedback mechanism | **CORE — Bidirectional** |
| Transformer thermal laws without a specific EV-power interface | **SUPPORTING** |
| EV battery thermal management without a physically coupled grid interface | **SUPPORTING** |
| EV scheduling without directly specified thermal physics | **CONTEXT** or **SUPPORTING**, depending on methods and relevance |
| Generic AI with no defensible infrastructure physical/service contribution | **EXCLUDE**, subject to eligibility |

**Screening protocol:** Evaluate **all 100 randomly selected records** under the same predefined rules and independently record one decision per record: `INCLUDE_CORE`, `INCLUDE_SUPPORTING`, `INCLUDE_CONTEXT`, `EXCLUDE`, `UNCLEAR`. Record SO1/SO2/SO3 relevance, a reason, exclusion code when applicable and whether full-text clarification is needed. The paper priority ranking is **not** an inclusion decision. Retain different source roles and avoid counting background reviews as independent primary measurements.

**Governance:** A single thesis researcher makes and records the initial and final eligibility judgments; supervisor input is scientific consultation only unless applicable university procedures demand further sign-off. Do not report two independent human reviewers, agreement or kappa statistics.

## 6. Final conceptual distinctions

- **Interconnection:** Two systems are linked.
- **Dependency:** One system influences the other.
- **Interdependency:** Reciprocal or networked dependencies (state strict versus broad usage).
- **Dynamic interdependency:** Influences depend on evolving states and time.
- **Thermally conditioned dynamic interdependency:** Temperature changes the mechanisms, constraints or propagation of those influences.
- **Resilience consequence:** Resulting effects on service preservation, degradation, adaptation or recovery under disruption.

**Operational conclusion:** Use the **strict bidirectional definition for the complete system-of-systems research question**, while independently preserving qualified \(P\rightarrow T\) and \(T\rightarrow P\) evidence for literature screening and subsequent physics-based mathematical derivation. Do not claim verified system-level reciprocity, actual field service outcomes or research novelty until the respective evidence gates are met.

## 7. References / provenance

1. **Rinaldi, S. M., Peerenboom, J. P. & Kelly, T. K. (2001).** “Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies.” *IEEE Control Systems Magazine* — conceptual framework and four interdependency types.
2. **NIST Community Resilience Planning Guide** — broader infrastructure dependency/interdependency terminology. Consult the applicable NIST guide's definition directly before verbatim citation.
3. **IEEE C57.91-2025** — transformer thermal loading and aging guidance for equipment within its scope. https://standards.ieee.org/ieee/C57.91/7163/
4. **User-provided full definition and operational explanation in this conversation (2026-11-06)** — primary source for this project's proposed formalization.

**Related project files:** 
- `SLR_PROTOCOL_V0_3_RESEARCHER_APPROVED_2026-11-05.md`
- `SLR_PROTOCOL_ADDENDUM_SINGLE_RESEARCHER_SCREENING_GOVERNANCE_2026-11-06.md`

**Note on source verification:** This file preserves the supplied conceptual claims and differentiates them from proposed thesis interpretations. It does not purport to be a newly completed primary-source or standards audit.
