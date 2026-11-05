# Systematic Literature Review — Protocol v0.2 (Discussion Draft)
**Date:** 2026-11-05  
**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Status:** DISCUSSION ONLY — NO USER APPROVAL OF THE FOUR NEW PROTOCOL DECISIONS; NO SUPERVISOR SIGN-OFF; NOT PREREGISTERED; NOT FROZEN.  
**Authority:** Existing project canonical thesis title (V3), thermal scope and SO1–SO3. This document does not change them.

## Decision status from researcher
| Decision | Researcher response | Current determination |
|---|---|---|
| Review design | DISCUSS | No methodology approved |
| Eligibility rules | DISCUSS | No final rule set approved |
| Reviewers | DISCUSS | Reviewer configuration/availability unknown |
| Search strategy | DISCUSS | No final strategy approved or frozen |

Existing verified **historical operations**, not approvals of v0.2: 12 Scopus A0–F1 exports plus integrated S0; S0 copied query matches archived v0.1 text; native screenshot displays 5,662 documents and exported file contains 5,662 rows; the 13-export union contains 27,528 unique Scopus EIDs (not verified distinct studies); 19 DOI collision groups are unresolved. No completed human pilot, full screening, PRISMA-ScR selection flow or supervisor methodological approval is on record. Preserve original exports and audit trails.

## D1 — Review design (OPEN)
**Option A — Full JBI-method scoping review:** broad PCC-based evidence map with systematically planned multi-database retrieval, independently applied screening, transparent extraction and PRISMA-ScR reporting. Suitable for describing the breadth of coupled and component-level evidence; substantial human time/resources and comprehensive reporting required.

**Option B — Systematized/targeted engineering literature review:** reproducible searches and eligibility rules with an explicitly bounded, source-critical synthesis of governing equations and verification/validation; must not be labeled a completed JBI scoping or exhaustive systematic review if its conduct does not meet those standards. More feasible as one part of an MSE thesis.

**Option C — Tiered strategy (conditional):** formal scoping review/evidence map if A is adequately resourced, alongside a deeper focused mathematical/physical evidence synthesis. If not, use Option B and accurately disclose constraints.

**Recommendation for discussion, not decision:** prioritize a focused, reproducible engineering synthesis needed for SO1–SO3; retain a full JBI scoping claim only if two-person review and exhaustive retrieval/screening can realistically be executed before thesis deadlines. A meta-analysis is not prespecified because model types and evidence are heterogeneous.

## D2 — Eligibility rules (OPEN)
**PCC:** P = power distribution systems/transformers/feeders and electrified transport/EVSE/vehicle/battery assets; C = physical electrical/thermal directional mechanisms, state-time dynamics, measurements, heat equations, thermal limits, service effects and validation; Context = extreme heat is primary hazard, while ordinary-temperature measured/physics comparator studies remain eligible with that context marked.

**Proposed inclusion:** (I1) source dated 2000 through search date in 2026 for the time-limited indexed search; foundational earlier works can enter via separately logged citation chasing; (I2) no initial language filter; document translation/retrieval constraints; (I3) evidence or technically justified transfer to at least one SO1–SO3; (I4) distinguish connected-interface CORE, standalone supporting physical/method evidence, service/context evidence and standards/reviews; (I5) include analytic, numerical, simulated, laboratory, observational and technical reports with explicit design/evidence labels; (I6) do not exclude physical comparators merely because they are not exposed to extreme heat.

**Proposed exclusion/reclassification:** E01 wrong system/no defensible transfer; E02 no qualifying thermal/physics/interface/service relevance; E03 unrelated economic/cyber/generic AI without an established physical/service role; E04 secondary paper falsely offered as independent original measurement (reclassify as context if relevant); E05 method/source unassessable after logged attempts (prefer UNCLEAR before full text); E06 outside indexed-search year boundary (older foundation citation exception); E07 actual same bibliographic work after identity adjudication (retain aliases and search memberships).

**Required clarifications before final lock:** (1) minimal evidence needed for CORE versus SUPPORTING; (2) whether service-only context is retained in formal inclusion count or separate contextual bibliography; (3) preprints, conference reviews, retracted publications and standards handled as separate evidence classes; (4) primary unit = work/publication versus independent empirical study; (5) language/full-text unavailability rules; (6) mandatory full-text confirmation before physical validation claims. Multiple SO roles allowed per verified work.

## D3 — Reviewers and screening (OPEN)
**Preferred:** Two independent human reviewers of titles/abstracts and eligible full texts, blinded to AI preliminary decisions. Reasons and independent decisions logged; resolve discrepancies by consensus or third adjudicator. Neither an AI assessment nor duplicate runs of the same AI count as two human reviewers.

**Calibration correction:** The prepared **25-record paper set is deliberately stratified** (5 preliminary core, 6 supporting, 9 uncertain, 5 provisional exclusions); use it as a *challenge/calibration* set but do not describe it as a JBI-recommended simple random 25. If pursuing formal JBI conduct, draw an additional random 25 from the relevant screening frame for the independent pilot and record agreement; JBI gives an illustrative threshold of at least 75% agreement before main screening. Pilot outcomes are not yet completed.

**Feasibility alternative:** If two independent reviewers are unavailable, explicitly adopt and justify a limited single-reviewer or verification-subsample approach under a differently labeled review, or document divergence from JBI; obtain supervisor agreement. Do not retroactively claim independent JBI-conformant screening.

**Record fields:** bibliographic ID, source/provenance, title/abstract access, reviewer identity, stage, decision (include/exclude/unclear), role, reason code, date, disagreement, adjudication and full-text retrieval outcome.

## D4 — Search strategy (OPEN)
**Already executed and immutable:** Scopus A0–F1 (12 thematic searches) and S0 integrated P AND T AND H, years 2000–2026; S0 full copied query matches archive, native result count 5,662; export count 5,662. Historical counts are *retrieval*, not eligibility.

**Proposed next search plan:** Retain 13 native Scopus queries as historical baseline. Evaluate reproducibility, database filters/date and source-specific evidence. Test held-out seed-paper retrieval and inspect a representative human-reviewed random S0 100 plus 30 targeted noise sample (keep distinct denominators). Use other databases (IEEE Xplore, Web of Science, Compendex where accessible) with platform-specific translated terms; separate original standards/technical reports and citation chaining. Record exact strings, timestamps, search field limits, hit counts, export files/hashes, and amendments. Validate cross-EID identities manually before merging; preserve 19 shared-DOI collision groups until resolved. **Do not freeze S0 as universal search until the strategy is evaluated and approved.** Source-native execution timestamp and active UI refinements for S0 remain not independently captured.

## Scientific extraction and deliverable gates (proposed, not yet satisfied)
For each human-included study extract, with original page/figure/equation citation: asset/site topology; directional physical mechanism; measured versus simulated states; temperature/heat/loss equations, units, parameters, boundary conditions, thermal time constants; controller/derating status; power and mobility demand, required/delivered energy; uncertainties; validation method, dataset and independence; limitations and applicability to SO1–SO3. An evidence map must distinguish direct connected thermal observation from separate-site component validation and simulation. No model or novelty claim may exceed the primary evidence.

**Review-completion gates:** versioned signed protocol and amendment log; documented per-database searches; reproducible bibliographic consolidation; calibrated human screening workflow; full-text selection and traceable reasons; populated scientific evidence matrix; closest-prior-art challenge; accurate PRISMA-ScR checklist/diagram only if genuinely following a scoping review; thesis Chapter 2 integration.

## Open decisions requiring researcher discussion and supervisor consultation
1. Choose A, B, or conditional C, with realistic reviewer/time capacity.
2. Resolve all six eligibility ambiguities in D2; approve or amend codes.
3. Confirm number and identity/role of independent human reviewers and conflict resolution.
4. Confirm databases/search stopping rules and chronology; approve or revise S0 as candidate strategy.
5. Record approvals by person, role and date; until then keep all decisions **DISCUSSION / PENDING**.

## Methodological authorities
- ASU Library review types: https://libguides.asu.edu/evidence_synthesis/types
- ASU Library scoping review guidance: https://libguides.asu.edu/evidence_synthesis/scoping-review
- JBI piloting: https://jbi-global-wiki.refined.site/space/MANUAL/2049540102/10.2.7.1%2BPiloting%2Bthe%2Bselection%2Bof%2Bstudies
- JBI evidence selection: https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862769/10.2.7%20Data%20extraction
- PRISMA-ScR: https://www.prisma-statement.org/scoping

**Change log:** v0.2 separates four researcher's DISCUSS decisions from earlier verified search operations; adds methodological alternatives, eligibility adjudication issues, reviewer feasibility alternatives and random-versus-targeted pilot distinction. No frozen project authority was edited.
