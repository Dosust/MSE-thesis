# Stage 2 Claim-Level Causal-Evidence Ledger v2

**Status:** ACTIVE WORKING EVIDENCE LEDGER — NO CASE RELATION ACCEPTED  
**Date:** 2026-09-18  
**Supersedes for active use:** `STAGE2_CLAIM_LEVEL_EVIDENCE_LEDGER_V1.md`  
**Stage-1 input:** locked Stage-1 supporting-evidence traceability layer + frozen `mathfrak r_e^(1)`.

## 1. Rule

Every Stage-2 causal claim must preserve the chain

~~~math
\boxed{
\text{claim}
\rightarrow
\text{source locator}
\rightarrow
\text{access depth}
\rightarrow
\text{provenance class}
\rightarrow
\text{G2 evidence use}
\rightarrow
\text{transfer boundary}
}
~~~

A source can support one or more G2 components without proving the full causal relation.

~~~math
\boxed{\text{source claim}\rightarrow\text{component evidence}\not\Rightarrow G_2(e)=\mathrm{PASS}}
~~~

## 2. Provenance classes

| Class | Meaning |
|---|---|
| `[LIT]` | Claim substantially established by the cited source. |
| `[ADAPT]` | Literature-supported concept adapted into the thesis causal-evidence workflow/notation. |
| `[THESIS]` | Thesis-defined gate, object, decision rule, uncertainty partition or synthesis. |

## 3. Access-depth classes

| Access basis | Meaning |
|---|---|
| `FULL TEXT` | Full article text/passages directly inspected. |
| `OPEN FULL TEXT` | Open article text/PDF directly inspected. |
| `PUBLISHER ARTICLE TEXT/PREVIEW` | Substantive publisher sections beyond abstract inspected. |
| `PUBLISHER ABSTRACT/HIGHLIGHTS` | Claim limited to abstract/highlights. |
| `INDEXED ABSTRACT` | Claim limited to indexed bibliographic abstract. |

No page/equation/figure locator is inferred when it was not directly exposed.

## 4. G2 evidence classes

`MECH` mechanism; `CASE` case connection; `INTF` interface/exchange; `ACT` activation; `TEMP` timing/delay; `EMP` empirical response; `OPER` operational requirement; `ALT` alternative/contrary evidence; `PARAM` parameter/heterogeneity; `UNC` uncertainty; `ORG` organizational/rule mediation; `FALS` falsification design.

## 5. Active ledger

| ID | Source | Provenance | Claim supported | Access basis / locator | G2 use | Thesis use | Non-transfer / limitation |
|---|---|---|---|---|---|---|---|
| `S2-C001` | Rinaldi et al. (2001) | [LIT]/[ADAPT] | Dependency/interdependency analysis requires explicit concepts, dimensions and system conditions. | PUBLISHER PREVIEW — abstract; concepts/definitions; interdependency-dimensions sections | MECH, ACT, ALT | dependency/context vocabulary; common-cause discriminator | taxonomy ≠ case causal proof |
| `S2-C002` | McNally et al. (2007) | [LIT]/[ADAPT] | Intra- and cross-domain infrastructure relations can be represented semantically and geographically. | PUBLISHER ABSTRACT | CASE, INTF | entity/interface/case mapping discipline | ontology/GIS relation ≠ causality |
| `S2-C003` | Ouyang (2014) | [LIT]/[ADAPT] | Interdependency questions/evidence support different modeling families. | PUBLISHER ARTICLE PREVIEW — highlights; abstract; modeling-approaches section | MECH, EMP, PARAM | method selection by mechanism/evidence | review ≠ candidate-specific evidence |
| `S2-C004` | Filippini & Silva (2014) | [LIT]/[ADAPT] | Functional dependencies concern interfaces exchanging data/services/quantities; structural analysis precedes dynamic analysis. | PUBLISHER ARTICLE TEXT/PREVIEW — Structural analysis; Dynamic model | MECH, INTF | functional exchange semantics | source dynamic assumptions cannot be imported as thesis-case truth |
| `S2-C005` | Nan & Sansavini (2015) | [LIT]/[ADAPT] | Technical/control and human-organizational layers can interact in multilayer infrastructure representations. | INDEXED/PUBLISHER ABSTRACT | MECH, ORG | mediated I/O/O paths | exact thesis layer ontology remains thesis-defined |
| `S2-C006` | Zhou et al. (2020) | [LIT]/[ADAPT] | Heterogeneous infrastructure models can be linked through explicit interfaces and associated variables/parameters. | PUBLISHER ARTICLE TEXT/PREVIEW — framework section; Fig. 1 description | INTF, PARAM | interface-variable/response-method design | designed model interface ≠ causal identification |
| `S2-C007` | Hruska et al. (2021) | [LIT]/[ADAPT] | Dependency profiles enumerate required/transported/produced commodities, services and data with spatial/temporal characteristics. | FULL TEXT — Methods/AHA passages | MECH, INTF, CASE | source→flow/service→receiver dossier | generic profile ≠ case acceptance |
| `S2-C008` | Fotouhi, Moryadee & Miller-Hooks (2017), DOI 10.1016/j.ress.2017.01.026 | [LIT] | A coupled traffic-electric-power model explicitly represents interdependencies with linking variables/logical constraints. | PUBLISHER OPEN MANUSCRIPT/PAGE — abstract; case-study coupled-network text | MECH, INTF | executable P↔T precedent | model formulation and Minneapolis case are not thesis-case proof |
| `S2-C009` | Fotouhi et al. (2017) | [LIT] | Traffic-signal power requirements create a direct P→T mechanism family. | PUBLISHER OPEN MANUSCRIPT/PAGE — case-study text around coupled network/Fig. 6 | MECH, INTF, ACT | `M2-PT-01` prior mechanism evidence | exact electrical connection, backup and thresholds must be re-established |
| `S2-C010` | Fotouhi et al. (2017) | [LIT] | Transportation access can constrain repair operations on damaged power infrastructure. | PUBLISHER OPEN MANUSCRIPT/PAGE — case-study coupled-network text | MECH, INTF, ACT | `M2-TP-01` prior mechanism evidence | proximity alone ≠ route/access dependency |
| `S2-C011` | Anokhin et al. (2021), DOI 10.1111/poms.13393 | [LIT] | MPS/repair-crew scheduling must account for energy and transportation constraints; disrupted travel routes alter routing/scheduling. | FULL TEXT / PUBLISHER ARTICLE TEXT — abstract; Introduction passages on MPS mobility, route availability and RC coordination | MECH, ACT, TEMP, OPER, UNC | recovery-activated T→P mobility/access mechanism | valid when a mobile resource/crew and physical travel are actually required |
| `S2-C012` | Yu et al. (2025 issue) | [LIT]/[ADAPT] | Logical interdependencies can be mediated by human decisions and formal/informal rules. | FULL TEXT — Abstract; §§2–3 | MECH, ORG, ACT | organizational/rule-mediated path | rule statement ≠ implemented causal action |
| `S2-C013` | Yu et al. (2025 issue) | [LIT]/[ADAPT] | Rule statements can be represented as network/hypergraph or rule-entity structures. | FULL TEXT — §§2.1–2.2; §3; Figs. 2–3 | ORG, CASE | explicit actor/rule/receiver mediation | motif occurrence ≠ physical magnitude |
| `S2-C014` | Yu et al. (2025 issue) | [LIT] | Logical-interdependency evidence is sensitive to document scope, omitted informal rules and implementation status. | FULL TEXT — caveats/clarification section | ALT, ORG, UNC | evidence-coverage control | rule corpus may be incomplete or non-operational |
| `S2-C015` | Lu et al. (2025), DOI 10.1016/j.energy.2025.135330 | [LIT]/[ADAPT] | Charging-station P–T dependency is heterogeneous across station/context characteristics. | PUBLISHER ABSTRACT/HIGHLIGHTS | PARAM, EMP, UNC | later heterogeneity/sensitivity treatment | source dependency measure is not a universal thesis weight |
| `S2-C016` | Thesis method | [THESIS] | Causal qualification requires mechanism + case connection + exchange + activation + evidence + validity + falsification. | Stage-2 G2 specification | governance | `G2-M/C/X/A/E/V/F` | thesis-defined architecture |
| `S2-C017` | Thesis method | [THESIS] | Causal status and parameter status are independent. | Stage-2 causal object contract | governance | `G2(e)` separate from `S_e^theta` | do not infer magnitude from evidence confidence |
| `S2-C018` | Zhu et al. (2021), DOI 10.1155/2021/5599073 | [LIT] | Power loss can be represented as traffic-signal loss causing roadway-capacity reduction; the study evaluates network consequences of signal failures caused by power outage. | OPEN FULL TEXT — Abstract; §1 Introduction; §2 Methodology | MECH, INTF, ACT, EMP, TEMP, UNC | strengthens `M2-PT-01`; identifies transportation response variables (travel time/speed/volume) | the paper uses a hypothetical neighborhood power grid and assumes power loss causes all signals in the affected area to fail; this assumption is not transferable as equipment-level truth |
| `S2-C019` | Zhang et al. (2025), DOI 10.1049/ein2.70010 | [LIT] | In a power-road model, power outages affect traffic lights and reduce intersection throughput; during restoration, road-system state affects emergency-resource scheduling. | OPEN/FULL TEXT PASSAGES — section “Fault Propagation and Key Issues of Urban Lifeline Systems”; power-road subsection | MECH, ACT, TEMP, OPER | corroborates phase-specific bidirectional P↔T mechanisms | coupling facilities are simplified; source itself notes real facilities are geographically distributed and may connect to multiple grid nodes |
| `S2-C020` | Shi et al. (2024), DOI 10.35833/MPCE.2023.000012 | [LIT] | Distribution restoration with repair crews/transportable power sources depends on vehicle routing; traffic-congestion uncertainty induces uncertain road travel time and is handled stochastically. | OPEN FULL TEXT / INDEXED ARTICLE — abstract; opening model/nomenclature passages | MECH, TEMP, PARAM, UNC | uncertainty model for `M2-TP-01` travel time | stochastic travel-time model is a methodological precedent, not a universal distribution for the thesis case |
| `S2-C021` | Fan et al. (2024), DOI 10.1016/j.epsr.2024.110505 | [LIT] | Post-disaster repair-crew routing depends on road states; transportation-system spatial interdependency is modeled to ensure feasible restoration decisions. | PUBLISHER ABSTRACT/HIGHLIGHTS | MECH, ACT, OPER | corroborates route-feasibility activation and road-state validity | model includes power-gas-transportation and synthetic coupled test systems; not direct thesis-case evidence |
| `S2-C022` | “Optimising repair sequences for interdependent infrastructure resilience” (2025), DOI 10.1080/10286608.2025.2602872 | [LIT] | A two-way P–T simulation explicitly represents power failures causing transportation delays via signal outages and transportation delays affecting repair-crew arrival at damaged power nodes. | PUBLISHER ABSTRACT | MECH, ACT, TEMP | joint corroboration of `M2-PT-01` and `M2-TP-01` | uses standard synthetic networks and a single-crew simulation; mechanisms require case re-establishment |
| `S2-C023` | Liu et al. (2026), DOI 10.1002/tee.70253 | [LIT] | Travel time of mobile emergency generators in the transportation network affects restoration speed of important distribution loads; real-time routing is integrated with restoration. | FULL TEXT PASSAGES — Abstract; Introduction; problem/model sections | MECH, ACT, TEMP, OPER | contemporary corroboration of mobile-resource T→P access mechanism | focused on MEGs; do not generalize automatically to every repair/resource type |
| `S2-C024` | Thesis synthesis | [THESIS] | For P0 mechanisms, uncertainty must be partitioned into connection, activation, interface-state, timing/travel, response-model and alternative-explanation uncertainty before G2-E/V can pass. | Stage-2 v2 evidence synthesis | UNC, ALT, FALS | controlled uncertainty partition for P0 dossiers | not claimed as a published taxonomy |

## 6. P0 evidence interpretation

### `M2-PT-01` — P→T traffic-signal electrical service

The literature now supports a **direct mechanism family** and a modeled transportation consequence:

~~~math
\text{electrical-service loss}
\rightarrow
\text{signal-function loss/degradation}
\rightarrow
\text{intersection/control-capacity change}
\rightarrow
\text{traffic-state response}.
~~~

However, source studies frequently simplify the electrical-to-signal mapping. Therefore the thesis must separately verify: actual feeder/circuit connection, controller service requirements, backup/UPS/generator state, fallback control mode and outage duration.

### `M2-TP-01` — T→P repair/restoration access

The literature supports the conditional chain:

~~~math
\text{road state / travel time}
\rightarrow
\text{mobile-resource feasible route + arrival}
\rightarrow
\text{field intervention}
\rightarrow
\text{restoration trajectory}.
~~~

The mechanism is not continuously active. It requires a restoration task that cannot be completed without physical mobile access.

## 7. Uncertainty discipline

For a candidate `e`, record at minimum:

~~~math
\boxed{
\mathcal U_e=
(U_e^{conn},
U_e^{act},
U_e^{intf},
U_e^{time},
U_e^{resp},
U_e^{alt})
}
~~~

where these respectively denote uncertainty in case connection, activation state, interface/service state, timing/travel, receiver-response representation and alternative explanations.

This is a thesis-defined bookkeeping partition; it is not a scalar evidence-confidence score.

## 8. Evidence gap retained

- Case-specific bus/feeder↔signal crosswalks remain absent from the generic Stage-2 literature layer.
- Case-specific failed-asset↔route↔crew/resource mappings remain absent from the generic literature layer.
- Direct V2G evidence remains insufficient in the current core for `M2-TP-03`; dedicated full-text evidence is still required.
- No literature mechanism family is promoted to `G2=PASS` solely from this ledger.

## 9. No scalar evidence score

~~~math
\boxed{
e_{mech}\neq e_{case}\neq e_{activation}\neq e_{empirical}\neq q_e^{evid}
}
~~~

The ledger is categorical and traceable; it does not calculate mechanism probability, coupling strength or an overall evidence score.
