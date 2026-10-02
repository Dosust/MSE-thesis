# Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience
## Reproducible 200 → 26 Literature Screening Protocol

### Guiding research question
How do time-varying physical states and interdependencies between power and transportation systems determine service degradation and recovery under extreme heat, and how can targeted operational interventions reduce the resulting coupled service deficits?

## Review philosophy
The screen is designed to learn from existing science rather than to manufacture a novelty claim.

**Framework → Method → Findings → Limitations → Synthesis → Contribution**

For every full-text paper, keep separate:
1. author-stated limitations;
2. reviewer-inferred limitations;
3. any proposed thesis contribution.

## Corpus and screening
- Raw provenance corpus: 687 records from the project's Scopus/Compendex/IEEE-derived provenance map.
- Deduplicated base corpus: 404 unique master records.
- Augmented and re-deduplicated working corpus: 433 unique records, including the targeted heat-resilience audit and verified close comparators.
- Automated title/abstract/metadata screen: 200 records.
- Priority full-text corpus: 26 papers.

The 26-paper stage is **not a claim that full text has already been screened**. It is the deliberately balanced set to inspect in full text next.

## Screening dimensions
Each of the 200 records is coded on a 0–5 scale for:
- thesis scope alignment;
- physical/thermal mechanism;
- state and time representation;
- P–T coupling/interdependency;
- service/resilience output;
- intervention/control;
- mathematical/computational method;
- evidence/validation strength.

## Evidence architecture for the 26
- 3 Framework/review papers
- 8 Heat-physics papers
- 2 Closest temperature–P–T comparator papers
- 8 Core dynamic P–T papers
- 3 Service/control papers
- 2 Transferable dynamic-coupling papers

This role-based sampling prevents one mature sub-literature (for example optimization) from crowding out thermal physics, service resilience, or dynamic-coupling evidence.

## Expert anchor comparators
Five papers are intentionally retained as boundary-defining comparators because they directly test the thesis method space:
- Sun et al. — spatial/temporal modelling review of coupled P–T systems — DOI 10.1049/enc2.12034.
- Wang et al. — dynamic P–T interdependency with EV charging preferences — DOI 10.1016/j.ress.2025.112005.
- Tri-level FCS/P–T optimization with temperature effects — DOI 10.1016/j.apenergy.2025.126806.
- Krama et al. — field fast-charger thermal performance — DOI 10.1016/j.ecmx.2026.101960.
- Parker et al. — extreme-heat EV energy consumption/driving range — DOI 10.1016/j.apenergy.2024.125051.

These anchors are not treated as proof of a research gap. Their purpose is to force the thesis design to learn from the closest existing methods and physical evidence.

## Full-text extraction rule
For each of the 26, extract:
- Framework
- Systems/layers/interfaces
- Governing physics
- Mathematical method
- State variables
- Time representation
- Coupling representation
- Service/resilience output
- Data and parameters
- Experiment/case study
- Main findings
- Author-stated limitations
- Inferred limitations
- Assumptions
- Validation/VVUQ
- Adopt directly
- Adapt
- Avoid
- Candidate contribution
- Evidence/page notes

## Reproducibility
Two independent implementations were executed:
- `pt_literature_screen.py`
- `pt_literature_screen.js`

Both produced the same 26 papers in the same ranking and evidence roles.

## Interpretation rule
The ranking is a **screening priority**, not a scientific quality ranking of the papers. Final thesis claims must be based on verified full-text evidence.