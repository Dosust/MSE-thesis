# Stage 1 Literature-Grounded Framework Precedents v2.0

**Status:** SUPPORTING EVIDENCE — DOES NOT AMEND THE FROZEN STAGE-1 FRAMEWORK  
**Date:** 2026-09-18  
**Supersedes:** `STAGE1_LITERATURE_GROUNDED_FRAMEWORK_PRECEDENTS_V1.md` for active supporting-evidence use  
**Frozen authority unchanged:** `project/STAGE1_FINAL_FRAMEWORK_V2.md`, `project/STAGE1_MATHEMATICAL_AND_ONTOLOGY_CONTRACT_V2.md`, `project/STAGE1_DATA_ABSTRACTION_AND_INGESTION_STANDARD_V2.md`, `thesis/00_governance/STAGE1_FRAMEWORK_FREEZE_2026-09-18.md`

## 1. Purpose

This revision strengthens **evidence traceability**, not Stage-1 theory. It separates what each paper actually establishes from how the thesis adapts that evidence into the frozen ontology.

~~~math
\boxed{\text{paper finding}\rightarrow\text{literature concept}\rightarrow\text{thesis adaptation}\rightarrow\text{frozen Stage-1 object}}
~~~

The following distinction is mandatory:

~~~math
\boxed{\text{literature precedent}\neq\text{case-specific structural verification}\neq\text{accepted causal interdependency}}
~~~

## 2. Provenance classes

| Class | Meaning |
|---|---|
| `[LIT]` | Claim/object substantially established by the cited literature. |
| `[ADAPT]` | Literature-supported concept adapted into thesis notation or workflow. |
| `[THESIS]` | Thesis-defined object, gate, controlled field, or synthesis not claimed as a published object. |

`[ADAPT]` is deliberately distinct from `[LIT]`: the fact that prior work motivates a field does not mean that paper defines the exact thesis symbol or tuple.

## 3. Access-depth discipline

| Access basis | Meaning |
|---|---|
| `FULL TEXT` | Full article text or full-text passages were available in this verification pass. |
| `PUBLISHER ARTICLE TEXT/PREVIEW` | Publisher page exposed substantive article sections beyond the abstract, but not necessarily the complete PDF. |
| `PUBLISHER ABSTRACT/HIGHLIGHTS` | Only abstract/highlights/metadata were relied upon for the listed claims. |
| `PUBLISHER PREVIEW` | Publisher preview and section headings were available; claims are limited accordingly. |

Where an exact page/equation/table/figure was not independently exposed in the accessible source, this document gives a **section-level or abstract-level locator rather than inventing a page locator**.

## 4. Corrected literature-to-ontology matrix

| ID | Paper | Access basis | Claim locator | What the source establishes | Thesis adaptation | Non-transfer / correction | Stage-2 carry-forward |
|---|---|---|---|---|---|---|---|
| L01 | Rinaldi, Peerenboom & Kelly (2001) | PUBLISHER PREVIEW | Abstract; section headings `Concepts and Definitions`, `Dimensions of Infrastructure Interdependencies`, `Modeling and Simulation Challenges` | [LIT] dependency/interdependency concepts; interdependency dimensions; system conditions | [ADAPT] `d_e`, `m_e^{cand}`, `c_e^{cand}`; common-cause/context reasoning | Do **not** claim that Rinaldi directly defines frozen `σ_e`; taxonomy category ≠ case relation | Stage 2: mechanism/context taxonomy; causal/common-cause discriminator |
| L02 | McNally et al. (2007) | PUBLISHER ABSTRACT + INDEXED PDF METADATA | Abstract | [LIT] intradomain vs cross-domain interactions; ontology + GIS representation | [ADAPT] semantic entity/spatial representation; INTRA/INTER structural organization | Ontology/GIS relation ≠ causal proof | Stage 2: case-connection and entity/interface traceability |
| L03 | Ouyang (2014) | PUBLISHER ARTICLE PREVIEW | Highlights; Abstract; Introduction; paper section map | [LIT] empirical, agent-based, system-dynamics, economic, network and other modeling approaches; interdependency/modeling review | [ADAPT] evidence-before-method selection; `b_e` as thesis admission-basis field | Review coverage ≠ case evidence; `b_e` is thesis-defined, not an Ouyang object | Stage 2: choose identification method by mechanism/evidence availability |
| L04 | Filippini & Silva (2014) | PUBLISHER ARTICLE TEXT/PREVIEW | Abstract; Introduction; `Overview`; `Structural analysis`; `The dynamic model`; `Quantitative resilience analysis` | [LIT] functional dependencies among components/services; interface exchange of data/services/quantities; structural analysis before dynamic analysis | [ADAPT] `f_i`, `Φ_e`; structural→dynamic boundary; `γ_e` only as thesis interface adaptation | Do not present `γ_e` as directly defined by this paper; failure propagation belongs later | Stage 2: functional mechanism + exchanged quantity; Stage 3: dynamic law |
| L05 | Nan & Sansavini (2015) | PUBLISHER/INDEXED ABSTRACT | Abstract/indexed methodological description | [LIT] multilayer hybrid representation; systems-under-control, operational-control and human-organizational components | [ADAPT] conceptual support for physical/supporting-domain decomposition, `h_e`, `ℓ_e` | Does not establish exact frozen `S={P,T,I,O}` ontology | Stage 2: mediated I/O paths and cross-scale relations |
| L06 | Zhou et al. (2020) | PUBLISHER ARTICLE TEXT/PREVIEW | Abstract; section `The framework to integrate data-driven and physics-based methods for ICI research`; Fig. 1 description | [LIT] three modules: understand infrastructure; select infrastructure-specific model/method; design interfaces using associated variables/parameters | [ADAPT] `γ_e`, `Φ_e`; interface variables/parameters; evidence-method matching | Designed model interface ≠ case-specific causal dependency | Stage 2: explicit interface variable, mechanism-response mapping, method selection |
| L07 | Hruska, McGillivary & Edsall (2021) | FULL-TEXT PASSAGES — WILEY/SCHOLAR CORPUS | Methods: AHA methodology; facility-type enumeration; dependency-type enumeration; dependency-profile generation | [LIT] function-based asset taxonomy; commodities/services/data required, transported or produced; directed multidimensional graphs; spatial/temporal characteristics | [ADAPT] `f_i`, `Φ_e`, `ℓ_e`, service traceability | Functional dependency profile ≠ case causal acceptance | Stage 2: source→required/produced flow→receiver functional dossier |
| L08 | Fotouhi, Moryadee & Miller-Hooks (2017) | PUBLISHER OPEN MANUSCRIPT/PAGE | Abstract; case-study coupled-network text around Fig. 6 | [LIT] two-layer traffic-power model; linking variables/logical constraints; traffic-signal power needs; transportation access for power-network repair | [ADAPT] direct `P→T` signal-power template; `T→P` repair-access template; `γ_e`, `Φ_e` | Their Minneapolis links/constraints cannot be transferred automatically to another case | Stage 2: strongest direct executable P↔T mechanism precedent |
| L09 | Anokhin et al. (2021) | FULL-TEXT PASSAGES — WILEY/SCHOLAR CORPUS | Abstract; Introduction passages on MPS/repair crews, transportation connectivity and alternate routes | [LIT] MPS and repair-crew routing/scheduling constrained by transportation network during distribution-system restoration | [ADAPT] recovery-activated `T→P` access mechanism; activation context = field intervention + route/resource mobility | Road proximity alone ≠ restoration dependency; dependency is conditional on restoration task/resource movement | Stage 2: activation predicate and travel/access mechanism |
| L10 | Yu et al. (2025 issue; first online 2024) | FULL TEXT — OPEN ACCESS + WILEY/SCHOLAR CORPUS | Abstract; §§2.1–2.2; §3; figures 2–3 and 10; clarification/caveats section | [LIT] formal/informal rules; syntactic → network forms; rule-entity bipartite/hypergraph representation; motifs A–C; document-scope and implementation caveats | [ADAPT] existing `m_e^{cand}` with organizational/rule-mediated class; `E_e`; `π_e=MEDIATED` where appropriate | Do not invent `m_e^{cand,org}` or `E_e^{rules}` as new frozen notation; motif frequency ≠ physical coupling strength | Stage 2: organizational/logical mediation and evidence caveats |
| L11 | Lu et al. (2025) | PUBLISHER ABSTRACT/HIGHLIGHTS | Highlights; Abstract | [LIT] supply-demand dependency model; internal/external FCS heterogeneity; urban/suburban dependency differences | [ADAPT] heterogeneity attributes; later mechanism-specific parameterization/sensitivity | Do not assign Stage-1 `w_e`; later `w_e` only if mathematically justified after causal qualification | Stage 2/3: post-qualification parameter heterogeneity and sensitivity |

## 5. Corrections relative to v1

### 5.1 Rinaldi does not directly define frozen `σ_e`

Rinaldi et al. provide foundational dependency/interdependency definitions, dimensions and system-condition reasoning. The frozen field

~~~math
\sigma_e\in\{\mathrm{INTRA},\mathrm{INTER},\mathrm{CONTEXT}\}
~~~

is a **thesis-controlled scope field**. Rinaldi informs dependency-type and context reasoning but is not cited as the direct origin of this exact controlled vocabulary.

### 5.2 Filippini & Silva primarily support function/service semantics and structure-before-dynamics

The strongest transferable objects are `f_i`, `Φ_e`, and the methodological boundary between structural and dynamic analysis. `γ_e` remains a thesis interface-semantic adaptation rather than a direct Filippini object.

### 5.3 Yu et al. must use frozen notation

No derivative notation such as `m_e^{cand,org}` or `E_e^{rules}` is introduced. Rule-mediated organizational evidence is represented through existing frozen fields:

~~~math
m_e^{\rm cand}=\text{rule-mediated / organizational mechanism family},\qquad
\mathcal E_e=\text{rule/document evidence},\qquad
\pi_e=\mathrm{MEDIATED}\ \text{when an explicit actor/rule path exists}.
~~~

### 5.4 Stage-1 figure wording is non-causal

Replace the ambiguous prompts `HOW?` and `WHEN?` with:

~~~text
CANDIDATE MECHANISM FAMILY?
CANDIDATE OPERATING / ACTIVATION CONTEXT?
~~~

Stage 1 records candidate mechanism/context descriptors; Stage 2 determines whether the mechanism genuinely operates in the declared case.

### 5.5 Dependency-strength language is deferred

Lu et al. provide evidence that quantified P–T dependency can be heterogeneous across FCS context. Stage 1 therefore retains:

~~~math
\boxed{w_e=\mathrm{NOT\_ESTIMATED\_STAGE1}}
~~~

and v2 describes Lu primarily as a precedent for **later mechanism-specific parameterization and sensitivity**, not as authority to assign a universal Stage-1 edge weight.

## 6. Revised Stage-1 visual evidence layer

~~~text
EVIDENCE LAYER
Literature • GIS • asset records • operator evidence
standards/requirements • empirical observations
                         ↓
                  r_e^(1)
WHO PARTICIPATES?
WHERE / AT WHAT RESOLUTION?
WHAT INTERFACE / SERVICE?
WHAT CANDIDATE DIRECTION?
WHAT CANDIDATE MECHANISM FAMILY?
WHAT CANDIDATE OPERATING / ACTIVATION CONTEXT?
WHAT EVIDENCE / PROVENANCE?

I_e^struct != w_e != q_e^evid
w_e = NOT_ESTIMATED_STAGE1
~~~

The correct summary is:

~~~math
\boxed{\text{evidence-grounded structural relation candidate}\neq\text{causally qualified interdependency}}
~~~

## 7. Claim-level traceability

The active claim-level ledger is maintained separately in `STAGE1_CLAIM_LEVEL_EVIDENCE_LEDGER_V2.md`. A literature claim should not enter thesis prose or a figure merely because the paper is in the bibliography; the ledger must identify the exact claim, source locator, access depth, provenance class, thesis use, and transfer boundary.

## 8. Stage-2 carry-forward — informational only

Stage-1 precedent evidence is **not** automatically Stage-2 causal evidence.

| Paper | Carry-forward role |
|---|---|
| Rinaldi et al. | mechanism/context taxonomy; dependency/interdependency distinction; common-cause controls |
| Ouyang | method selection according to evidence/modeling context |
| Filippini & Silva | functional dependency and exchanged data/service/quantity semantics |
| Zhou et al. | interface variables/parameters and heterogeneous-model interface design |
| Hruska et al. | functional source/requirement/flow/receiver dependency profile |
| Fotouhi et al. | direct P→T signal-power and T→P repair-access executable precedents |
| Anokhin et al. | recovery-activated T→P mobility/access mechanism and routing constraints |
| Yu et al. | rule-mediated organizational/logical paths and evidence-scope caveats |
| Lu et al. | post-qualification heterogeneity and parameter/sensitivity precedent |

~~~math
\boxed{\text{Stage-1 precedent evidence}\neq\text{Stage-2 causal evidence}}
~~~

## 9. Defensible Stage-1 synthesis claim

Existing studies establish important foundations for infrastructure dependency taxonomies, ontology/GIS representation, functional dependencies, multilayer architectures, interface-based model integration, organizational/logical interdependencies, and direct Power–Transportation models. The thesis contribution at Stage 1 is the **controlled synthesis** that makes these ingredients interoperable while separating structural admissibility, case evidence, causal qualification, coupling strength, evidence confidence, and normative admissibility.

This is a synthesis claim, not an exhaustive novelty claim.

## 10. Governance

This file is supporting evidence only. It does not modify frozen Stage-1 objects, controlled vocabularies, schemas, G1 gates, or the Stage-1→Stage-2 handoff. Any semantic change to frozen Stage 1 requires the explicit amendment/unfreeze procedure.

~~~math
\boxed{G_1^{\rm framework}=\mathrm{PASS\ —\ FROZEN}}
~~~