# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![Search](https://img.shields.io/badge/evidence%20search-DE%20NOVO-1A7F37)
![FTEE](https://img.shields.io/badge/FTEE%20v2.0-CURRENT-0969DA)
![H1](https://img.shields.io/badge/M0%20%26%20M1-VERIFIED-1A7F37)
![325 Corpus](https://img.shields.io/badge/325--paper%20corpus-COVERAGE%20AUDIT%20ONLY-9A6700)

This directory is the active mathematical/scientific specification of the MSE thesis. The seven-stage framework and five-primary-hypothesis logic are frozen. The named thesis execution method is **EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method**. FTEE v2.0 remains the evidence-to-equation protocol inside EGMIV.

> **Canonical reasoning protocol:** [`RESEARCH_REASONING_PROTOCOL.md`](RESEARCH_REASONING_PROTOCOL.md) governs how every claim, method, equation, simulation, hypothesis, figure, and engineering recommendation is learned, verified, formalized, tested, validated, synthesized, and advanced.

> **Canonical execution method:** [`EGMIV_METHOD_V1.md`](EGMIV_METHOD_V1.md) governs the evidence → mechanism → interdependency → mathematical-model → validation chain.

> **Governing evidence rule:** a paper becomes primary thesis evidence only because the reproducible search finds it and the eligibility protocol qualifies it. Public-support branches may aid method development but never silently replace the formal confirmatory corpus.

---

## 1. Authority map

| Priority | File | Role | Status |
|---:|---|---|---|
| 1 | [`RESEARCH_REASONING_PROTOCOL.md`](RESEARCH_REASONING_PROTOCOL.md) | thesis-wide reasoning, verification, validation, falsification and synthesis protocol | **canonical / current** |
| 2 | [`EGMIV_METHOD_V1.md`](EGMIV_METHOD_V1.md) | evidence-grounded mechanism/model/validation execution method | **canonical / current** |
| 3 | [`THESIS_SCOPE.md`](THESIS_SCOPE.md) | current scientific scope and stage boundaries | canonical / frozen |
| 4 | [`CANONICAL_7_STAGE_FRAMEWORK.md`](CANONICAL_7_STAGE_FRAMEWORK.md) | complete seven-stage architecture and mathematics | canonical / frozen |
| 5 | [`CANONICAL_SYSTEM_DEFINITION.md`](CANONICAL_SYSTEM_DEFINITION.md) | P–T–I–O system identity and state ontology | canonical |
| 6 | [`FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md) | framework-level subsystem decomposition | canonical |
| 7 | [`STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](STAGE_2_INTERDEPENDENCY_MECHANISMS.md) | Stage-2 causal interdependency specification | frozen |
| 8 | [`STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md) | Stage-3 dynamic architecture | frozen |
| 9 | [`STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md) | Stage-4 observation-to-action architecture | frozen |
| 10 | [`STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md) | Stage-5 viability architecture | frozen |
| 11 | [`STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md`](STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md) | Stage-6 transition architecture | frozen |
| 12 | [`STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md`](STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md) | Stage-7 adaptive transformation architecture | frozen |
| 13 | [`RESEARCH_HYPOTHESES.md`](RESEARCH_HYPOTHESES.md) | five primary confirmatory hypotheses | logic frozen; thresholds unset |
| 14 | [`ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md) | confirmatory operationalization and VVUQ gates | current |
| 15 | [`H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md`](H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md) | H1 physical M0/M1/M2 competing-model specification | current / frozen structure |
| 16 | [`H1_PROGRESS_SNAPSHOT_2026-09-13.md`](H1_PROGRESS_SNAPSHOT_2026-09-13.md) | H1 execution-state snapshot | current |
| 17 | [`MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md) | demonstrator-reduction rationale and stopping rule | current methodology |
| 18 | [`FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md`](FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md) | de novo search + screening + evidence-to-equation extraction + model qualification | current primary evidence protocol |
| 19 | [`H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md`](H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md) | H1 formal-search execution protocol | frozen; authenticated execution pending |

---

## 2. Canonical reasoning and EGMIV chains

```math
\text{LEARN}\rightarrow\text{VERIFY}\rightarrow\text{FORMULATE}\rightarrow\text{DERIVE}\rightarrow\text{TEST}\rightarrow\text{VALIDATE}\rightarrow\text{SYNTHESIZE}\rightarrow\text{ADVANCE}.
```

```math
\text{Evidence}\rightarrow\text{Mechanism}\rightarrow\text{Interdependency}\rightarrow\text{Mathematical Model}\rightarrow\text{Validation}.
```

EGMIV governing rule:

> **No interdependency without direction + mechanism + mapping + type + evidence.**

---

## 3. H1 current physical experiment

The H1 physical demonstrator boundary is frozen as

```math
\mathcal G_{H1}=\mathcal G_P\cup\mathcal G_T\cup\mathcal C.
```

Information and organization remain deferred to H2 so H1 can identify physical Power–Transportation coupling without attribution confounding.

The competing representations are

```math
\boxed{M_0=\text{independent},\qquad M_1=\text{static/algebraic coupling},\qquad M_2=\text{dynamic causal coupling}.}
```

The instantiated physical interfaces remain:

- $P\rightarrow T$: grid power limits charging service;
- $T\rightarrow P$: EV charging demand becomes nodal electrical load;
- $T\rightarrow P$: road access/travel time constrains power-repair resources.

---

## 4. H1 executable verification state

### M0

Package: [`../models/H1/M0/`](../models/H1/M0/)  
Status: **verified — 13 passed, 0 failed**.

### M1

Package: [`../models/H1/M1/`](../models/H1/M1/)  
Status: **verified — 13 M1-specific tests passed, 0 failed**.

M1 preserves the verified M0 radial LinDistFlow and multi-commodity CTM solvers. It adds only memoryless same-step interface maps:

```math
p_{c,\mathrm{req}}(k)=\min\!\left(\bar p_c,\frac{E_c}{\eta_c}\lambda_c(k)\right),
```

```math
p_c^{ch}(k)=p_{c,\mathrm{req}}(k)g_{b(c)}(k),
```

```math
\mu_c(k)=\frac{\eta_cp_c^{ch}(k)}{E_c}.
```

There is **no** charger queue state, evolving interface state or dynamic repair delay in M1.

The EGMIV verification caught and corrected an accounting error before freeze: requested EV electrical demand must remain in the power-service denominator even when the charger bus is de-energized. In the benchmark outage case the valid minimum $S_P$ is therefore `0.4736842105`, not `0.60`.

M1 passed dimensional identity, exact load mapping, monotonicity, zero-demand and sufficient-capacity limits, static repair-access logic, time-step refinement, no-double-counting, outage-demand accounting, strict memorylessness, and the nested decoupling condition

```math
\boxed{M_1\rightarrow M_0\quad\text{when interface maps are removed}.}
```

Matched scenarios S0/S1/S2/S6 are stored under `models/H1/M1/reports/`. They are benchmark verification only; no engineering-materiality threshold has been applied and H1 is not confirmed.

---

## 5. Formal H1 evidence status

The exact H1 CORE search remains frozen and still requires authenticated execution in Scopus, Web of Science Core Collection, Compendex and IEEE Xplore. Public evidence remains supportive/provisional only.

---

## 6. Immediate next step

The current EGMIV progression is

```math
\boxed{M_0\;\checkmark\rightarrow M_1\;\checkmark\rightarrow\mathbf{M_2}.}
```

M2 is now authorized to add the dynamic objects deliberately excluded from M1:

```math
q_c(k+1)=q_c(k)+\Delta t[\lambda_c(k)-\mu_c(k)],
```

state/time-dependent road travel delay, delayed repair-resource transport, repair-progress state, and

```math
z_{ij}(k+1)=H_{ij}(Y_{k-\ell_{ij}},z_{ij}(k),m_k).
```

The first mandatory M2 falsification gate is

```math
\boxed{M_2\rightarrow M_1\quad\text{when queue memory and dynamic delay are removed}.}
```

No final H1 conclusion is permitted until M2, matched M0/M1/M2 experiments, identifiability/UQ/physical-admissibility gates, and the formal confirmatory evidence corpus are complete.