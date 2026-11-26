# Scopus Search 4 — Mathematical and physics-based modeling (16 October 2026)

**Database/interface:** Scopus → Advanced Search → Title, Abstract, Keywords (`TITLE-ABS-KEY`).  
**Research query:** [SCOPUS_SEARCH_04_RECORDED_QUERY.txt](SCOPUS_SEARCH_04_RECORDED_QUERY.txt) — the previously supplied Search 4 expression. **The exported CSV does not retain the original query or live result count: exact execution syntax and Scopus displayed hits still need confirmation against Scopus Search History.**  
**Original user-uploaded CSV:** `export_fc290122-aa6c-4c61-bd50-7f392adbb404_2026-10-16T160905.777621326.csv`.  
**Storage status:** Search query, research logic, and the audit metadata are committed in this GitHub branch. **The original 18.25-MB licensed bibliographic CSV has NOT been uploaded to GitHub**, pending verified institutional/Scopus authorization.

## Short purpose statement

We searched Scopus for **thermal and heat-transfer mathematical models** of transformers, power systems, EVs and charging equipment, explicitly including differential equations, state-space dynamics, heat equations, thermal networks, and finite-element/finite-volume numerical methods. This will help us identify the **governing physics and mathematical structure** underlying the two systems instead of selecting an AI method prematurely.

## How we will use the results to achieve the frozen SO1–SO3 goals

1. **SO1 — Physical mechanisms:** Screen for true Power-system and Electrified Transportation equipment. Identify heat generation, transport, thermal inertia, meaningful temperatures, operating limits, and directional interface mechanisms. Do not confuse ML `Transformer` architectures with electrical transformers.
2. **SO2 — Physics and mathematics:** Read eligible full articles, extract original **ODE/PDE/DAE or state-space governing equations**, variables/units, initial and boundary conditions, parameter meaning, conservation/constitutive assumptions, interface mapping, numerical methods, stability and identifiability as applicable.
3. **SO3 — Time-dependent service and resilience:** Determine whether published equations and measured experiments predict heat-conditioned onset/critical times, charging/thermal propagation delays, and *independently defined* electricity/mobility service shortfalls and recovery, distinguishing simulation from real measurements.
4. **Evidence and novelty:** Document how earlier models were calibrated, independently validated and uncertainty-bounded. Compare physics-only/PINN/grey-box models on **matched observed targets** if data justify that comparison; do not assert novelty solely because a specific equation/model has not appeared among screened titles.

**Interpretation rule:** Search retrieval is not relevance screening; model-based temperature prediction is not measured paired P↔Tₑ thermal transfer. Independent component measurements must not be disguised as single-site coupled data.

## Direct examination of the original CSV

| Item | Audited value |
| --- | ---: |
| Records in original CSV | **5,108** |
| Columns | **35** |
| Title nonempty | 5,108 |
| Abstract nonempty | 5,108 |
| Scopus EID nonempty | 5,108 |
| Within-file duplicated EIDs | **0** |
| DOI nonempty | **4,481** |
| EID overlap with Search 1 | 119 |
| EID overlap with Search 2 | 681 |
| EID overlap with Search 3 | 524 |
| EID overlap with **any** prior Search 1–3 | **1,283** |
| New Search 4 EIDs relative to Search 1–3 | **3,825** |
| **Unique Scopus EIDs across Searches 1–4** | **21,733** |
| Reference list column | Not present |
| File size | **18,253,181 bytes** |
| SHA-256 | `6fa53d195469a86d53236ec68bb834c8b4c5ac96f73476d526c094757edbb68e` |

**Quality caveat:** The results include papers on AI Transformer architecture and general fluid/nanofluid heat transfer, which may be irrelevant. All 5,108 are **candidate hits, not included studies**. Raw EID set union is a technical cross-search deduplication check, **not formal PRISMA screening**.

## Custody and reproduction

Elsevier's Scopus terms permit authorized scholarly use but restrict systematic reproduction, third-party sharing and storage of bulk Scopus content outside the applicable agreement; private GitHub does not automatically resolve this. See official terms: https://www.elsevier.com/legal/elsevier-website-terms-and-conditions/elsevier-scopus-terms-and-conditions . Therefore no copyrighted abstracts, correspondence records or entire original CSV were committed. Retain user-provided export only in institutionally approved storage until permissions for GitHub are confirmed.

## Reproducibility status

- Export CSV inspected and counted: **YES**
- Executed Scopus query history/screenshots checked: **NO** (the recorded text reproduces prior instruction)
- Scopus interface result count independently checked: **NO** (5,108 is verified CSV count)
- Original publisher papers read for these 5,108 records: **NOT YET**
- Screened/eligible: **NOT YET**
- Final novelty/model family claim: **NOT ESTABLISHED**

**Next action:** Verify the recorded Search 4 query in Scopus Search History; execute **Search 5 — Experimental Evidence, Validation and Physics-Informed Modeling**, export results, then deduplicate and screen the full candidate corpus for rigorous physics/mathematical extraction.
