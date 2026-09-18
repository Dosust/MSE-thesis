# Stage 2 Claim-Level Causal-Evidence Ledger v1

**Status:** WORKING EVIDENCE LEDGER — NO CASE RELATION ACCEPTED  
**Date:** 2026-09-18

## 1. Rule

Every Stage-2 causal claim must identify what the source actually establishes and which G2 component it can inform. A paper can support a mechanism family without proving the case connection or the final causal relation.

~~~math
\boxed{\text{source claim}\rightarrow\text{G2 component evidence}\not\Rightarrow G_2(e)=\mathrm{PASS}}
~~~

## 2. Evidence classes

| Code | Meaning |
|---|---|
| `MECH` | mechanism plausibility/directness |
| `CASE` | case-specific source/interface/receiver linkage |
| `INTF` | interface/exchange semantics |
| `ACT` | activation/operating context |
| `TEMP` | temporal ordering/delay/timescale evidence |
| `EMP` | empirical observed response |
| `OPER` | operational/operator/engineering requirement |
| `ALT` | alternative/contrary-evidence control |
| `PARAM` | parameter/heterogeneity/sensitivity evidence |
| `ORG` | organizational/rule-mediated evidence |

## 3. Ledger

| ID | Source | Claim supported | Access/locator | G2 evidence use | Current thesis use | Non-transfer rule |
|---|---|---|---|---|---|---|
| `S2-C001` | Rinaldi et al. (2001) | Dependency/interdependency concepts require explicit direction/context and include multiple interdependency dimensions. | Publisher preview; abstract + conceptual/dimensions sections | MECH, ACT, ALT | mechanism/context vocabulary and common-cause discriminator | taxonomy ≠ case causal proof |
| `S2-C002` | McNally et al. (2007) | Intra- and cross-domain relations can be represented semantically and geographically. | Publisher abstract | CASE, INTF | entity/interface/case mapping discipline | ontology/GIS link ≠ causal relation |
| `S2-C003` | Ouyang (2014) | Different interdependent-infrastructure questions/evidence support different modeling approaches. | Highlights; abstract; modeling-approaches section | MECH, EMP, PARAM | identification-method selection | review ≠ direct evidence for a candidate |
| `S2-C004` | Filippini & Silva (2014) | Functional dependencies focus on interfaces where data, services and quantities are exchanged; structural representation precedes dynamic propagation. | `Structural analysis`; `The dynamic model` | MECH, INTF | functional mechanism and exchange semantics | dynamic assumptions cannot be imported as case truth |
| `S2-C005` | Nan & Sansavini (2015) | Technical/control and human-organizational layers can interact in a multilayer representation. | Abstract/indexed description | MECH, ORG | mediated I/O/O pathways | exact thesis layer ontology remains thesis-defined |
| `S2-C006` | Zhou et al. (2020) | Heterogeneous infrastructures may use different models linked through designed interfaces and associated variables/parameters. | Abstract; framework section; Fig. 1 description | INTF, PARAM | interface variable/response-method design | designed interface ≠ causal identification |
| `S2-C007` | Hruska et al. (2021) | Functional dependency profiles enumerate commodities, services and data required, transported or produced by assets; spatial/temporal characteristics are documented. | Full-text Methods passages | MECH, INTF, CASE | source→flow/service→receiver functional dossier | profile ≠ causal acceptance |
| `S2-C008` | Fotouhi et al. (2017) | A two-layer traffic-power model captures interdependencies with linking variables and logical constraints. | Abstract/open manuscript | MECH, INTF | executable P↔T mechanism precedent | model constraints are case/model choices |
| `S2-C009` | Fotouhi et al. (2017) | Case coupling includes power needs of traffic signals. | Case-study text around Fig. 6 | MECH, INTF, ACT | direct prior evidence for `M2-PT-01` | Minneapolis link ≠ thesis-case connection |
| `S2-C010` | Fotouhi et al. (2017) | Case coupling includes transportation access for power-network repair operations. | Case-study text around Fig. 6 | MECH, INTF, ACT | direct prior evidence for `M2-TP-01` | road proximity alone ≠ access dependency |
| `S2-C011` | Anokhin et al. (2021) | MPS and repair-crew routing/scheduling for distribution restoration must account for transportation connectivity and disrupted routes. | Full-text Introduction passages | MECH, ACT, TEMP, OPER | recovery-activated T→P access mechanism | applies when mobile resource/field intervention is required |
| `S2-C012` | Yu et al. (2025 issue) | Logical interdependencies can be mediated by human decisions and formal/informal rules. | Full text; Abstract and §§2–3 | MECH, ORG, ACT | organizational/rule-mediated causal path | rule mention alone ≠ implemented causal action |
| `S2-C013` | Yu et al. (2025 issue) | Rule statements can be translated into hypergraph/bipartite network forms; motifs can indicate logical relations. | §§2.1–2.2, §3, Figs. 2–3 | ORG, CASE | explicit actor/rule/receiver mediation path | motif frequency ≠ physical effect magnitude |
| `S2-C014` | Yu et al. (2025 issue) | Motif evidence is sensitive to document scope, informal rules and whether formal rules are implemented. | caveats/clarification section | ALT, ORG | evidence-coverage and alternative-explanation controls | incomplete rule corpus may misrepresent reality |
| `S2-C015` | Lu et al. (2025) | Supply-demand P–T dependency varies with FCS internal/external heterogeneity; dominant factors differ spatially. | Highlights; Abstract | PARAM, EMP | heterogeneity and later parameter sensitivity | quantitative dependency measure is not transferable as universal `w_e` |
| `S2-C016` | Thesis method | Causal qualification requires mechanism + case connection + exchange + activation + evidence + validity + falsification. | Stage-2 G2 specification | governance | `G2-M/C/X/A/E/V/F` | thesis-defined gate architecture; not attributed to one paper |
| `S2-C017` | Thesis method | Causal status and parameter status are independent. | Stage-2 causal object contract | governance | `G2(e)` separate from `S_e^theta` | do not infer magnitude from confidence |

## 4. Evidence gap explicitly retained

The current 11-paper set is strongest for **signal-power**, **repair-access**, interface/function semantics, organizational mediation, and post-qualification heterogeneity. It is not yet sufficient as the sole direct-evidence basis for a detailed V2G mechanism. `M2-TP-03` therefore remains OPEN and requires dedicated V2G full-text evidence before any causal qualification attempt.

## 5. No scalar evidence score

Evidence classes answer different scientific questions. No weighted sum is authorized by this ledger.

~~~math
\boxed{e_{mech}\neq e_{case}\neq e_{activation}\neq e_{empirical}\neq q_e^{evid}}
~~~