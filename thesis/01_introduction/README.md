# Chapter 1 — Introduction

**Chapter-I authority:** `../../project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V2.md`  
**RQ–SO–H authority:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Writing/inference authority:** `../00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`  
**Stage-6/7 sustainability authority:** `../00_governance/SUSTAINABILITY_DIMENSION_ADMISSION_AND_ACCOUNTING_STANDARD_V1.md`  
**Sustainability status register:** `../00_governance/SUSTAINABILITY_DIMENSION_REGISTER_V1.md`  
**Metric cards:** `../00_governance/SUSTAINABILITY_METRIC_CARDS_V1.md`  
**Case/data feasibility audit:** `../00_governance/SUSTAINABILITY_CASE_DATA_FEASIBILITY_AUDIT_V1.md`  
**Current admission freeze:** `../00_governance/SUSTAINABILITY_ADMISSION_FREEZE_V1.md`

## Purpose

Establish the research contract: engineering context, problem, evidence-qualified gap, scope, research architecture, questions, objectives, hypotheses/test logic and proposed contribution. Chapter 1 does not present unverified thesis results or detailed Chapter-3/4 derivations.

## Required sections

1. **[1.1 Background and Engineering Context](01_01_background_and_engineering_context.md)**
2. **[1.2 Coupled P–T–I–O System Context](01_02_coupled_ptio_system_context.md)**
3. **[1.3 Problem Statement](01_03_problem_statement.md)**
4. **[1.4 Research Gap](01_04_research_gap.md)**
5. **[1.5 Sustainable Engineering Significance](01_05_sustainable_engineering_significance.md)**
6. **[1.6 Scope, Boundaries, and Assumptions](01_06_scope_boundaries_and_assumptions.md)**
7. **[1.7 Research Framework and Logic](01_07_research_architecture_and_scientific_logic.md)**
8. **[1.8 General Research Objective](01_08_general_research_objective.md)**
9. **[1.9 Research Questions](01_09_research_questions.md)** — RQ0 + exact RQ1–RQ7
10. **[1.10 Specific Research Objectives](01_10_specific_research_objectives.md)** — exact SO1–SO7
11. **[1.11 Research Hypotheses and Test Logic](01_11_research_hypotheses_and_test_logic.md)** — H1–H5
12. **1.12 Proposed Contributions**
13. **1.13 Thesis Organization**

Target length: **16–18 pages** within the 160-page thesis ceiling unless explicitly amended.

## Current drafted prose

Sections **1.1–1.11 now have one source of truth in this directory**. The repository root `README.md` is a project dashboard and links here rather than duplicating thesis prose.

- 1.1 fixes the dependency/interdependency terminology and establishes the engineering context.
- 1.2 defines the P–T physical core and I–O supporting domains and uses an observation–decision–action loop rather than implying that I/O are physical infrastructure layers.
- 1.3 states the engineering problem concisely and removes detailed experimental/VVUQ material that belongs later.
- 1.4 presents six bounded, counterevidence-aware gaps, explicitly explains why six gaps map to seven specific RQs, and separates research-gap evidence from global novelty.
- 1.5 establishes the Sustainable Engineering significance without conflating resilience, resource efficiency and sustainability; it uses the completed evidence audit, metric cards, case/data feasibility audit and current admission freeze.
- 1.6 defines the fit-for-purpose P–T–I–O research domain; separates common exposure from causal dependency; freezes spatial, temporal and hazard semantics; distinguishes state, operational control and persistent transformation; states the sustainability/accounting boundary; and makes assumptions, uncertainty classes, exclusions and validity limits explicit.
- 1.7 is synchronized and compressed to the canonical seven-stage framework: it defines the compact stage contract, seven-row stage specification, Stage-5 remain–return–confidence semantics, Stage-6 intervention/consequence/sustainability-requirement logic, Stage-7 decision/transformation logic, PASS/FAIL/BLOCKED handoffs, bidirectional traceability, controlled iteration, and cross-cutting V&V/UQ/reproducibility without duplicating Chapters 3–4.
- 1.8 states the exact canonical general objective, clarifies Stage-5 viability/reachability/confidence semantics, and preserves the P–T physical core with I–O supporting-domain scope.
- 1.9 reproduces the exact canonical RQ0 and RQ1–RQ7 wording, preserves the ordered RQ1→RQ7 scientific dependency, and defers SO/H detail to Sections 1.10–1.11.
- 1.10 reproduces the exact canonical SO1–SO7 wording, preserves one-to-one `RQ_k↔SO_k` traceability, distinguishes the developmental/evidence obligations of SO1–SO2 from the five hypothesis-bearing objectives, and defers comparator/test detail to Section 1.11.
- 1.11 retains the exact canonical H1–H5 wording and defines, for each hypothesis, the comparator architecture, response class, uncertainty treatment, and non-support/BLOCKED logic without importing detailed Chapter-4 derivations. It preserves H4/H5 sustainability-admission conditions, Stage-5 remain–return–confidence semantics, interface criticality as a supporting diagnostic, and adaptive transformation as a conditional extension.
- **Section 1.12 Proposed Contributions is the next Chapter-I drafting task and must use conditional proposal language only; no contribution may be written as demonstrated until the relevant evidence, validation, novelty, and hypothesis chain closes.**

Section 1.5 must not introduce a sustainability dimension merely because it is normatively desirable or common in broad sustainability frameworks. It may discuss only quantities whose scientific role is clear (`R-SVC`, `RES`, `SUS`, `FEAS`, `TRANS`, or `CTX`) and whose current scope/admission state is controlled by `SUSTAINABILITY_ADMISSION_FREEZE_V1.md`.

At the current freeze, direct cost, operational electrical energy and carbon/GHG are **planned core consequence families but remain confirmatory-CONDITIONAL** because the Austin candidate case, final intervention set, metric-specific data/boundaries and VVUQ are not all frozen. Distributional accessibility/equity and crew-hours are conditional extensions. Full LCA, water, biodiversity, public-health, broad social-sustainability and macroeconomic modeling are outside the current quantitative core.

## Governing logic

```math
\boxed{
\text{Context}
\rightarrow\text{Problem}
\rightarrow\text{Gap}
\rightarrow\text{Scope}
\rightarrow\text{Framework}
\rightarrow\text{Questions}
\rightarrow\text{Objectives}
\rightarrow\text{Hypotheses}
\rightarrow\text{Proposed contribution}
}
```

Scientific stage meaning remains controlled by framework v2:

```math
\boxed{
\text{Structure}
\rightarrow\text{Causal Interdependencies}
\rightarrow\text{Hybrid Dynamics}
\rightarrow\text{Observation/Estimation/Organization/Control}
\rightarrow\text{Viability + Reachability + Probability}
\rightarrow\text{Intervention + Sustainability Consequences}
\rightarrow\text{Engineering Decision}
}
```

## Terminology rule

Use the following distinction consistently in Chapter 1:

```math
\boxed{
\begin{aligned}
\text{directional dependency mechanism:}&\quad P\rightarrow T\ \text{or}\ T\rightarrow P,\\
\text{interdependency:}&\quad \text{coupled condition with reciprocal directional dependencies}.
\end{aligned}}
```

Common hazard exposure and spatial co-location do not by themselves establish a causal dependency.

## Traceability rule

- RQ0 is overarching.
- RQ1–RQ7 correspond one-to-one with SO1–SO7.
- G1 supports RQ1/RQ2 and SO1/SO2; these carry developmental/evidence obligations supporting H1.
- G2 → RQ3/SO3 → H1.
- G3 → RQ4/SO4 → H2.
- G4 → RQ5/SO5 → H3.
- G5 → RQ6/SO6 → H4.
- G6 → RQ7/SO7 → H5.

Six gaps therefore support seven specific questions; seven questions do **not** imply seven hypotheses.

## Intervention-performance rule

Preserve:

```math
\boxed{\text{effectiveness}\neq\text{efficiency}\neq\text{sustainability}}.
```

For Stage 6–7 work, also preserve the typed consequence record:

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
\right).
}
```

Interface criticality is a supporting diagnostic. Adaptive/sequential transformation is a supporting Stage-7 extension unless separately activated and preregistered.

## Evidence discipline

- factual background/significance claims require qualified sources;
- gap claims must trace to Chapter-2 synthesis and, for novelty, the separate reproducible novelty audit;
- `[H]`, `[P]` and `[A]` statements must not be written as established facts;
- proposal-stage results language is prohibited unless an already executed verification/method result is explicitly identified and bounded;
- externally sourced claims use adjacent verified APA 7 author–date citations;
- exact claim strength must not exceed evidence or validation domain;
- sustainability claims must distinguish direct P–T evidence from adjacent transferable evidence;
- cost, budget, energy, carbon, accessibility, resource use and transformation descriptors must not be collapsed into one generic sustainability category without role typing and admission;
- a `CONDITIONAL` metric may be described as planned/qualified but not as a measured or confirmatory-ready quantity;
- Section 1.5 significance language must not imply that carbon-aware P–T resilience, low-carbon planning or persistent P–T infrastructure transformation is absent from prior research.

## Exit gate

See `../00_governance/THESIS_COMPLETION_GATES.md`. Chapter 1 is not complete until the exact v3 questions/objectives/hypotheses, Chapter-I v2 flow, evidence discipline and proposed-contribution status are synchronized. Sections 1.5 and 1.6 must remain consistent with the current sustainability admission freeze and Austin case-admissibility state; Section 1.7 must preserve the seven-stage conceptual architecture while deferring detailed mathematics to Chapter 3.
