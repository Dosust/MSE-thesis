# MASTER PROMPT — PRISMA-Compatible Monte Carlo Ranking of the Frozen 325-Paper Thesis Corpus

## Role
Act as a reproducible systematic-review methodologist, applied mathematician, uncertainty-quantification researcher, and scientific programmer. Your task is to rank the papers in one frozen thesis dataset for the thesis **Mathematical Physics of Sustainable Infrastructure Resilience**, with emphasis on coupled infrastructure systems, dynamic interfaces, viability/reachability, recovery/control, sustainability/equity, climate/flood/waste interactions, inverse problems, uncertainty quantification, and mathematical-physics foundations.

## Absolute data boundary
Use **only** the uploaded file:

`Thesis_Final_Unique_Papers_325_2026-08-20(3).csv`

Do not search the web. Do not query Crossref, Scopus, Web of Science, IEEE Xplore, Google Scholar, publishers, citation databases, journal metrics, university repositories, or any other dataset. Do not add citation counts, impact factors, h-index values, external abstracts, external full text, author reputation, institution prestige, or publication venue prestige. If the CSV does not contain a fact, mark it unavailable rather than inventing it.

The frozen dataset must contain exactly 325 rows. Compute and report the SHA-256 hash before analysis. Abort scoring if the row count is not 325, if Canonical_ID is not unique, if non-empty DOI values are duplicated, or if exact normalized Canonical_Title duplicates remain.

## Critical methodological distinction
PRISMA 2020 is used for transparent identification, screening, eligibility, exclusion accounting, and reporting. PRISMA is **not** itself a paper-ranking algorithm. After the PRISMA-compatible eligibility layer, use a separate stochastic multi-criteria / SMAA-like Monte Carlo model to quantify ranking uncertainty.

## Anti-circularity / leakage rule
The following columns are prior/downstream ranking outputs and are **forbidden from the new score**:

- Final_Unique_Rank
- Best_Priority_Tier
- Max_Importance_Score
- Selected_Core_164
- Rank_76
- Rank_141
- Rank_164

They may be used only after the new ranking is complete for validation, rank-correlation analysis, disagreement analysis, and audit reporting. They must have exactly zero causal influence on the Monte Carlo score.

## PRISMA-compatible pre-ranking conditions
For every record i, assign exactly one status:

1. `ELIGIBLE` — substantive thesis paper allowed into Monte Carlo ranking.
2. `METHODS_ONLY` — PRISMA/reporting/systematic-review methodology retained for the thesis methods chapter but excluded from the substantive scientific-paper ranking.
3. `HOLD` — cannot be scientifically resolved from the frozen dataset alone.
4. `EXCLUDE` — fails canonical identity requirements.

Apply the following deterministic rules before any stochastic scoring:

### P0 — Frozen identity
Require non-empty Canonical_ID, Canonical_Title, Journal, and URL.

### P1 — Deduplication integrity
Require unique Canonical_ID, unique non-empty DOI, and unique normalized Canonical_Title.

### P2 — Methods-only separation
If `Relevance_259 == C_PROTOCOL_SUPPORT` or `Primary_Discipline` indicates `Systematic Review Methodology`, classify as `METHODS_ONLY`. Do not let a PRISMA guideline become the “best scientific thesis paper.”

### P3 — Critical metadata conflicts
If `Data_Quality_Notes` contains `CONFLICTING_DOI`, classify as `HOLD`. Do not silently guess or resolve the DOI with outside information.

### P4 — Substantive scope signal
A record needs at least one substantive signal from the frozen CSV: a non-empty Relevance_207; a non-protocol Relevance_259; Relevant_Hypotheses; Theory_Architecture_Anchors_or_Selection; or a thesis-aligned discipline token in Primary_Discipline/Discipline_Coverage.

### P5 — Missingness
Do not automatically exclude papers solely because Authors or Year are missing. Missing data must propagate as uncertainty, not as fabricated values.

## Scoring criteria
Construct six top-level criteria, all scaled to [0,1]. Keep them conceptually separate to limit double counting:

1. `Direct_Relevance` — based only on Relevance_207 and Relevance_259.
2. `Theory_Architecture` — based only on Relevant_Hypotheses and Theory_Architecture_Anchors_or_Selection.
3. `Disciplinary_Fit` — based only on Primary_Discipline and Discipline_Coverage.
4. `Evidence_Credibility` — based only on Verification_Status, Evidence_Stratum_207, Local_Full_Text_207, DOI presence, and Data_Quality_Notes.
5. `Primary_Corpus_Corroboration` — based only on whether Source_Presence contains the primary 207 corpus and/or primary 259 corpus. Do not use occurrences in the 76/141/164 selected subsets as corroboration because that would reintroduce prior-selection leakage.
6. `Title_Semantic_Directness` — based only on Canonical_Title using a predeclared ontology for coupled/interdependent infrastructure, dynamics/control/viability/recovery, sector coverage (power, water, transport, waste), climate/hazard, and sustainability/equity. Because this is title-only inference, assign it lower confidence than curated evidence fields.

## Direct-relevance centers
Map the dataset’s categorical relevance fields as follows:

Relevance_207:
- CORE = 1.00
- STRONG_APPLIED = 0.86
- FOUNDATION = 0.78
- SUPPORTING = 0.58

Relevance_259:
- A_CORE_DIRECT = 1.00
- B_FOUNDATIONAL_TRANSFERABLE = 0.80
- C_SUPPORTING_METHOD_CONTEXT = 0.58
- C_PROTOCOL_SUPPORT = 0.15, but classify the paper as METHODS_ONLY before substantive ranking.

If both relevance fields are observed, use their mean and high confidence. If only one is observed, use it with moderately lower confidence. If neither is observed, use a non-informative center of 0.50 with low confidence instead of inventing relevance.

## Theory-architecture priorities
Use the dataset’s own coded dimensions with the following prior importance vector:

- H1 = 0.11
- H2 = 0.15
- H3 = 0.17
- H4 = 0.15
- H5 = 0.17
- H6 = 0.15
- H7 = 0.05
- T1 = 0.05

These priorities encode the present thesis architecture in the frozen corpus. Do not add new hypothesis labels.

A paper should receive strong theory alignment if it hits at least one high-priority hypothesis and additional coverage should provide a bounded bonus rather than an unlimited reward for having many tags. Explicit architecture anchors such as viability/reachability, recovery/control, sustainability/equity, static-dynamic interfaces, inverse/UQ, flood/waste/drainage, physics/network cascades, or reduction/decomposition increase confidence.

## Evidence-credibility principle
Evidence_Credibility must reward auditability, not prestige. Use Verification_Status, Evidence_Stratum_207, Local_Full_Text_207, DOI presence, and Data_Quality_Notes. Full-text prior audit and publisher/DOI-title audit should score highly. Abstract-only evidence should score lower. Missing DOI should reduce evidence confidence but should not automatically exclude the paper. A YEAR_CONFLICT should reduce confidence. A CONFLICTING_DOI must be HOLD, not scored.

## Stochastic feature uncertainty
For each eligible paper i and criterion c, define a center mu_ic in [0,1] and confidence rho_ic in [0,1]. Convert them to a Beta distribution:

kappa_ic = 4 + 96 rho_ic

alpha_ic = clip(mu_ic,0.01,0.99) * kappa_ic

beta_ic = (1 - clip(mu_ic,0.01,0.99)) * kappa_ic

and sample

X_ic^(b) ~ Beta(alpha_ic, beta_ic).

This makes audited/complete features concentrated and missing/weak features broad. Missingness must increase uncertainty instead of being silently treated as certainty.

## Weight uncertainty
Do not use one arbitrary fixed weighting vector. Use four predeclared scientific perspectives:

- balanced = [0.22, 0.22, 0.16, 0.20, 0.06, 0.14]
- theory_first = [0.15, 0.30, 0.20, 0.18, 0.04, 0.13]
- evidence_first = [0.18, 0.18, 0.14, 0.32, 0.06, 0.12]
- applied_direct = [0.28, 0.16, 0.12, 0.18, 0.06, 0.20]

The coordinate order is:
[Direct_Relevance, Theory_Architecture, Disciplinary_Fit, Evidence_Credibility, Primary_Corpus_Corroboration, Title_Semantic_Directness].

For each Monte Carlo draw, select one scenario uniformly and then sample local weights:

w^(b) ~ Dirichlet(80 * w_scenario).

This models both structural preference uncertainty and local weight uncertainty while forcing w_c >= 0 and sum_c w_c = 1.

## Monte Carlo score
For eligible paper i in draw b:

S_i^(b) = sum_c w_c^(b) X_ic^(b).

Rank all eligible substantive papers in descending S_i^(b). Let R_i^(b) be the resulting rank.

Run exactly 20 independent cumulative batches of 5,000 draws using seed 20260820, for a total of 100,000 draws unless computationally impossible. If computationally impossible, report the actual N and do not claim the target precision.

## Rank-robustness statistics
For every eligible paper report at minimum:

- Expected_Rank = mean_b R_i^(b)
- P_Rank_1 = P(R_i=1)
- P_Top_5 = P(R_i<=5)
- P_Top_10 = P(R_i<=10)
- P_Top_25 = P(R_i<=25)
- Mean_MC_Score = mean_b S_i^(b)
- SD_MC_Score = sd_b S_i^(b)
- full rank-acceptability probabilities P(R_i=r), r=1,...,N_eligible

Do not report a single deterministic score without its uncertainty and rank acceptability.

## Mathematical precision checks
For N Monte Carlo draws, calculate the worst-case standard error for any rank-acceptability probability:

SE_max = 1/(2 sqrt(N)).

Report the worst-case 95% half-width:

1.96 * SE_max.

For N=100,000 this should be approximately 0.00310.

Also report the 99% Hoeffding bound for a bounded [0,1] mean score:

epsilon_0.99 = sqrt(log(2/0.01)/(2N)).

For N=100,000 this should be approximately 0.00515.

## Convergence conditions
The run passes convergence only if all are true:

1. worst-case 95% probability half-width <= 0.005;
2. across the last five cumulative batches, the maximum absolute change in any paper’s P_Top_10 is <= 0.010;
3. the minimum Jaccard similarity between consecutive last-five top-10 sets based on Expected_Rank is >= 0.80.

If convergence fails, report failure. Do not hide it. Increase draws only if explicitly permitted.

## Pre-specified “best paper” decision rule
Among ELIGIBLE substantive papers only, identify the best paper lexicographically by:

1. smallest Expected_Rank;
2. if tied, largest P_Top_10;
3. if tied, largest P_Rank_1;
4. if tied, largest Mean_MC_Score;
5. if tied, smallest SD_MC_Score;
6. if still tied, Canonical_ID ascending for deterministic reproducibility.

Do not select the paper merely because it had an old rank of 1.

## Validation only after ranking
After the Monte Carlo ranking is frozen, compare it against Final_Unique_Rank, Rank_76, Rank_141, and Rank_164 using rank correlations on comparable records. Clearly label all such comparisons `VALIDATION_ONLY_NOT_USED_IN_SCORING`.

Also inspect large rank disagreements. A disagreement is not automatically an error; it may reveal that the new stochastic model differs from previous deterministic prioritization.

## Required outputs
Write all outputs to a dedicated directory and produce:

1. `01_PRISMA_Gated_All_325.csv` — all 325 records with PRISMA status/reason plus criterion centers/confidences.
2. `02_MC_Ranked_Eligible.csv` — full robust ranking of eligible substantive papers.
3. `03_MC_Top_50.csv` — top 50.
4. `04_Prior_Rank_Validation_Only.csv` — validation correlations only.
5. `05_Rank_Acceptability_Matrix.csv` — P(Rank=r) matrix.
6. `06_Audit.json` — file hash, counts, settings, seed, criteria, weight scenarios, convergence diagnostics, best-paper rule, best paper, and limitations.
7. `07_README.txt` — concise reproducibility summary.

## Required final report
The final response must state:

- exact input filename and SHA-256;
- 325-record frozen-corpus check;
- counts of ELIGIBLE, METHODS_ONLY, HOLD, and EXCLUDE;
- exact Monte Carlo draw count and seed;
- convergence results and mathematical precision bounds;
- top paper with Canonical_ID, full title, DOI, Expected_Rank, P_Rank_1, P_Top_10, Mean_MC_Score, and SD_MC_Score;
- top 10 table;
- explicit statement that prior rank fields were excluded from scoring;
- explicit statement that no external data were used;
- limitations caused by missing authors/year/full text or title-only semantic inference;
- downloadable output files.

Never claim that Monte Carlo proves the objectively “true” best paper. State that it identifies the paper with the strongest **robust rank under the pre-specified dataset-only model and uncertainty assumptions**.
