# Verified 200→26 Literature Screening Run — 2026-10-02

**Thesis:** Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience  
**Repository:** `Dossiya-SE/MSE-thesis`

## Guiding research question

How do time-varying physical states and interdependencies between Power and Transportation systems determine service degradation and recovery under extreme heat, and how can targeted operational interventions reduce the resulting coupled service deficits?

## Scientific review logic

`FRAMEWORK → METHOD → FINDINGS → LIMITATIONS → SYNTHESIS → CONTRIBUTION`

The review is designed to learn how closely related studies formulate the system, what mathematics and physics they use, what they demonstrate, what assumptions and limitations bound their conclusions, and where a focused methodological improvement may be justified.

## Executed screening funnel

- 687 raw provenance records
- 404 deduplicated master records in the base corpus
- 433 unique working records after augmentation/deduplication
- 200 title/abstract/metadata records screened
- 26 priority papers selected for full-text review

**Important:** the 26-paper set is a *priority full-text corpus*. It is not yet a full-text evidence synthesis. Framework, equations, findings, author-stated limitations, assumptions, validation, and VVUQ must still be verified from the papers themselves.

## Priority evidence architecture

- 3 framework/review papers
- 8 heat/physical-mechanism papers
- 2 closest temperature–Power–Transportation comparators
- 8 core dynamic Power–Transportation papers
- 3 service/control papers
- 2 transferable dynamic-coupling papers

## Evidence discipline

Keep these distinct:

`author-stated limitation ≠ reviewer-inferred limitation ≠ thesis contribution`

A candidate methodological contribution should only be retained if a controlled comparison shows that it materially changes explanation, prediction, service-resilience assessment, or intervention choice.

## Files

- `PT_200_to_26_High_Rigor_Audit.xlsx` — complete workbook with Summary, Protocol, Screened_200, Priority_26, and FullText_Extraction sheets.
- `PT_200_screened.csv` — 200 screened records and coded scoring dimensions.
- `PT_26_high_rigor.csv` — selected 26-paper priority corpus.
- `PT_26_high_rigor_js.csv` — independent JavaScript verification output.
- `PT_200_to_26_Methodology.md` — screening methodology and decision rules.
- `pt_literature_screen.py` — Python screening implementation.
- `pt_literature_screen.js` — independent JavaScript implementation.
- `PT_200_to_26_Literature_Audit_Package.zip` — portable package containing the run artifacts.
- `SHA256SUMS.txt` — integrity hashes.

## Next scientific stage

For each of the 26 papers, reconstruct:

`Problem → Framework → Mathematical/physical method → Data/parameters → Experiment → Findings → Interpretation → Author-stated limitations → Inferred limitations → Adopt/Adapt/Test decision`

The contribution should emerge from that synthesis rather than being fixed in advance.