# CPTS High-Rigor Literature Screening Protocol

## Thesis
**Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**

## Guiding RQ
How do time-varying physical states and interdependencies between power and transportation systems determine service degradation and recovery under extreme heat, and how can targeted operational interventions reduce the resulting coupled service deficits?

## Scientific logic
**FRAMEWORK → METHOD → FINDINGS → LIMITATIONS → SYNTHESIS → CONTRIBUTION**

## Review philosophy
**ADOPT → ADAPT → TEST → COMPARE → IMPROVE**

The review does **not** try to prove that no related work exists. It reconstructs existing methods and evidence, identifies assumptions that materially limit the guiding RQ, and then determines whether a modest methodological adaptation is justified.

## Screening stages
1. **Discovery target:** 200 unique records after DOI/title deduplication.
2. **Title/abstract gate:** direct CPTS papers or indispensable physics-module papers.
3. **Scored priority screen:** 0–100 rubric.
4. **Diversity-constrained core:** 26 high-priority papers across reviews/foundations, dynamic coupling, resilience/recovery, heat/thermal physics, and interventions.
5. **Full-text extraction:** framework, equations/method, findings, author-stated limitations, assumptions, validation, inferred limitation, adopt/adapt decision.
6. **Synthesis:** method genealogy and candidate improvement.
7. **Contribution test:** only retain a proposed improvement if it materially changes explanation, prediction, service outcome, or intervention choice.

## Hard inclusion criteria
- Peer-reviewed journal article/review or a clearly traceable high-quality publication.
- Directly models coupled power–transportation systems **or** provides an indispensable physical block (charger thermal derating, transformer thermal state, EV heat-dependent energy/SOC).
- Contains a method/model/experiment, not only commentary.
- Relevant to at least one of: coupling, state/time dynamics, service degradation/recovery, extreme heat, operational intervention.
- Sufficient metadata to audit the source.

## Exclusion criteria
- Pure EV market/economic paper without physical/network coupling.
- Pure power paper with no EV/transport/thermal relevance.
- Pure traffic paper with no electric-energy coupling.
- Duplicate/preprint where a peer-reviewed version is available.
- Title-only record with no abstract/full text available for a substantive claim.
- Studies whose only relevance is generic “resilience” language.

## 0–100 scoring rubric
- RQ directness: 20
- Physics fidelity: 20
- Explicit P–T coupling: 15
- State/time dynamics: 15
- Service/resilience outcome: 10
- Mathematical/method rigor: 10
- Validation/empirical support: 5
- Intervention relevance: 5

Each dimension is coded 0–4 and scaled by its weight.

## Mandatory evidence distinction
`author_stated_limitation != reviewer_inferred_limitation != thesis_contribution`

No inferred limitation becomes a contribution until the thesis tests that the modification matters.

## Full-text extraction fields
Problem | Framework | Power model | Transport model | Interface/coupling direction | State variables | Time representation | Hazard | Equations/method | Data/parameters | Experiment | Findings | Author-stated limitations | Reviewer-inferred limitations | Assumptions | Validation/VVUQ | What to adopt | What to adapt | Candidate comparison baseline | Relevance to RQ.