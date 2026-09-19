# Chapter I Citation and Evidence Traceability Audit V1

**Status:** CANDIDATE-COMPANION / ACTIVE FOR THE REVISED CHAPTER-I CANDIDATE  
**Date:** 2026-09-20  
**Candidate:** `CHAPTER_I_REVISED_EVIDENCE_GROUNDED_CANDIDATE_V1_2026-09-20.md`  
**Citation authority:** `../00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md`  
**Writing authority:** `../00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`

## 1. Audit purpose

This file records why citations were inserted, where citations are intentionally absent, and what must be checked before the candidate can be frozen.

The governing distinction is:

```math
\boxed{
\text{external scientific claim}
\rightarrow
\text{adjacent evidence}
}
```

versus

```math
\boxed{
\text{thesis scope / RQ / SO / H / derivation / proposal}
\rightarrow
\text{explicit thesis status, not decorative citation}
}
```

## 2. Section-level citation logic

| Section | Main external-evidence burden | Current citation strategy | Status |
|---|---|---|---|
| 1.1 Background | P–T mechanisms; service-centered SoS; directionality; SoS foundations | Hall; Ibáñez; Maier; Ouyang; Rinaldi; Fan; Fotouhi; Unterluggauer; Wang; Wei | PASS-CANDIDATE |
| 1.2 System context | information/organization relevance; structural vs causal relation; common cause | Chester; Helmrich; Rasoulkhani & Mostafavi; Rydén Sonesson; Kivelä; Ouyang; Rinaldi; Fan | PASS-CANDIDATE |
| 1.3 Problem | established method families; organization/action; curve vs viability/reachability; trade-offs | Doyen & De Lara; Ouyang; Poulin & Kane; Tong; Vinod & Oishi; Chester; Helmrich; Béné & Doyen; Mitoulis; Sun; Zou & Chen | PASS-CANDIDATE |
| 1.4 Research gap | established capability and documented limitations for G1–G6 | evidence placed mainly on Established/Limitation side; thesis handoff/test left as synthesis | PASS-CANDIDATE |
| 1.5 Sustainable Engineering | resilience/resource/carbon trade-offs | Chester; Mitoulis; Sun; Zou & Chen | PASS-CANDIDATE |
| 1.6 Scope | thesis boundary and validity decisions | intentionally sparse/no external citation unless a factual external requirement is invoked | PASS-CANDIDATE |
| 1.7 Framework | seven-stage thesis synthesis | no citation padding; external theory remains in earlier foundations | PASS-CANDIDATE |
| 1.8 GO | candidate thesis research contract | intentionally uncited | PASS-CANDIDATE |
| 1.9 RQs | candidate thesis research contract | intentionally uncited | PASS-CANDIDATE |
| 1.10 SOs | candidate thesis research contract | intentionally uncited | PASS-CANDIDATE |
| 1.11 Hypotheses | thesis hypotheses and comparators | intentionally uncited; evidence justification belongs to surrounding literature/evidence architecture | PASS-CANDIDATE |
| 1.12 Contributions | proposed contributions + established-foundation novelty firewall | citations only on foundations already established in literature | PASS-CANDIDATE |
| 1.13 Organization | document architecture | intentionally uncited | PASS-CANDIDATE |

## 3. Research-gap evidence pattern

Every G1–G6 paragraph is required to preserve:

```math
\boxed{
\text{Established}
\rightarrow
\text{Limitation}
\rightarrow
\text{bounded unresolved handoff}
\rightarrow
\text{thesis test}
}
```

Citations support the first two components. The latter two are thesis synthesis unless an external source directly defines the same unresolved handoff.

This avoids the invalid inference:

```math
\boxed{
\text{not observed in selected papers}
\not\Rightarrow
\text{globally absent}
}
```

## 4. High-value claim-to-source map

| Claim family | Source role | Principal sources |
|---|---|---|
| infrastructure should be reasoned about through services / SoS | theory/architecture | Hall et al. (2016); Maier (1998) |
| energy and transportation can remain separate networks while interacting | architecture/planning precedent | Ibáñez et al. (2010) |
| P–T charging/traffic/power coupling is established | mechanism/model precedent | Wei et al. (2019); Unterluggauer et al. (2022); Fotouhi et al. (2017); Wang et al. (2026) |
| transport accessibility can constrain power restoration | mechanism evidence | Fan et al. (2024) |
| structural/geographic relation is not automatically causal dependency | taxonomy/mechanism foundation | Rinaldi et al. (2001); Ouyang (2014); Kivelä et al. (2014) |
| information/governance/human conditions affect resilience response | socio-technical evidence | Chester et al. (2021); Helmrich et al. (2021); Rasoulkhani & Mostafavi (2018); Rydén Sonesson et al. (2021) |
| resilience curves are performance/recovery summaries with metric dependence | comparator foundation | Poulin & Kane (2021); Trucco & Petrenj (2023) |
| viability/reachability address constrained maintainability/target attainment | mathematical foundation | Béné & Doyen (2018); Doyen & De Lara (2010); Vinod & Oishi (2021) |
| resilience interventions can involve cost/carbon/resource trade-offs | intervention/sustainability evidence | Mitoulis et al. (2023); Sun et al. (2025); Zou & Chen (2019) |
| interdependent-infrastructure research remains concerned with dynamic evolution and trade-offs | review/gap support | Tong et al. (2025) |
| EV charging infrastructure can be planned for coupled resilience under uncertainty | P–T resilience planning precedent | Wen et al. (2025) |

## 5. Metadata checks completed in current improvement cycle

The following recent/high-risk references were checked against publisher or authoritative bibliographic records during the 2026-09-20 improvement cycle:

- Wang et al. (2026), `Reliability Engineering & System Safety`, 268, 112005, DOI `10.1016/j.ress.2025.112005`.
- Wen et al. (2025), `IEEE Transactions on Smart Grid`, 16(1), 491–504, DOI `10.1109/TSG.2024.3390657`.
- Sun et al. (2025), `Applied Energy`, 397, 126258, DOI `10.1016/j.apenergy.2025.126258`.
- Tong et al. (2025), `International Journal of Critical Infrastructure Protection`, 51, 100793, DOI `10.1016/j.ijcip.2025.100793`.
- Mitoulis et al. (2023), `Transportation Research Part D`, 121, 103800, DOI `10.1016/j.trd.2023.103800`.
- Rydén Sonesson et al. (2021), `Safety Science`, 142, 105383, DOI `10.1016/j.ssci.2021.105383`.

Older/core references are inherited from the repository’s existing accepted Chapter-I and Stage-1/2 evidence set; they still require the normal final comprehensive-reference QA before submission.

## 6. Intentional non-citation decisions

The following are not externally cited merely because they are important:

- `P+T=physical core, I+O=supporting domains` as the adopted thesis ontology;
- the seven-stage framework as a thesis synthesis;
- the candidate GO/RQ/SO wording;
- H1–H5 as hypotheses;
- `M_0,M_1,M_2` comparator definitions;
- the rule that the named development case belongs in Chapter 4;
- scope exclusions and accounting-boundary choices;
- proposed contributions C1–C6.

External foundations are cited around these constructs where needed, but the thesis must not imply that a single paper authored the integrated research architecture.

## 7. Remaining blockers before freeze

### Citation/reference block
- run final exact in-text ↔ reference-list one-to-one check;
- verify every DOI and bibliographic field in the final reference manager/export;
- verify any direct quotation against the original full text and page locator;
- ensure final Word/LaTeX rendering uses hanging indents and ASU spacing.

### Evidence block
- do not promote a citation-supported general statement to a case-specific mechanism without Stage-2 qualification;
- do not infer novelty from the reference set;
- do not use a review as proof of a quantitative case parameter when a primary source is required.

### Governance block
The revised GO/RQ/SO/H wording remains **candidate wording**. Citation completion does not itself authorize replacement of the frozen canonical research contract.

## 8. Citation QA decision

```text
Adjacent claim support:     PASS-CANDIDATE
Reference coverage:         PASS-CANDIDATE
Recent-source metadata:     PASS-CANDIDATE
Final global reference QA:  OPEN
Canonical contract status:  CANDIDATE / NOT FROZEN
```

Therefore:

```math
\boxed{
G_{cite}^{candidate}=PASS
\qquad
G_{freeze}=BLOCKED\;\text{pending governance synchronization and final reference QA}
}
```
