# MASTER EXECUTION PROMPT

## Closed-Corpus PRISMA + Monte Carlo Ranking Protocol for `Thesis_Final_Unique_Papers_325_2026-08-20(1).csv`

You are acting as a **systematic-review methodologist, mathematical modeller, uncertainty-quantification researcher, evidence auditor, and Python reproducibility engineer**.

Your task is to rank the papers contained in **one and only one supplied dataset** for their importance to the thesis **Mathematical Physics of Sustainable Infrastructure Resilience**, using a transparent PRISMA-style closed-corpus screening layer and a mathematically auditable Monte Carlo ranking layer.

The objective is to identify the **most robustly important papers within this locked 325-record corpus**, including the best global paper and hypothesis-specific best papers, without importing information from any other file, project memory, prior corpus, website, API, database, PDF, abstract, or external source.

---

# 0. SINGLE-DATASET LOCK — NON-NEGOTIABLE

The only admissible input is:

```text
Thesis_Final_Unique_Papers_325_2026-08-20(1).csv
```

Expected SHA-256:

```text
047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f
```

Expected number of rows:

```text
325
```

Expected number of columns:

```text
34
```

Do **not**:

- read or merge the previous 207-paper dataset;
- read or merge the previous 259-paper dataset;
- read the 333-, 141-, 164-, or 76-paper files;
- use any other local file;
- use project memory as evidence;
- use web search;
- use Crossref, OpenAlex, Scopus, Web of Science, Compendex, IEEE Xplore, Google Scholar, publisher pages, or APIs;
- fetch PDFs or abstracts;
- add new papers;
- remove a paper because another corpus previously excluded it;
- replace missing values with information remembered from previous work.

If the supplied file hash differs from the frozen SHA-256, stop with:

```text
FAIL_SINGLE_DATASET_LOCK
```

This is a **closed-corpus re-analysis**. It is not a new literature search and must not be described as a globally complete PRISMA systematic search.

---

# 1. EXACT FROZEN SCHEMA

Require exactly these columns and reject schema drift:

```text
Final_Unique_Rank
Canonical_ID
Canonical_Title
Canonical_Title_Selection
Authors
Year
Journal
DOI
DOI_URL
URL
Primary_Discipline
Discipline_Coverage
Relevant_Hypotheses
Relevance_207
Relevance_259
Evidence_Stratum_207
High_Rigor_Candidate_259
Local_Full_Text_207
Verification_Status
Best_Priority_Tier
Max_Importance_Score
Selected_Core_164
Rank_76
Rank_141
Rank_164
Theory_Architecture_Anchors_or_Selection
Source_Presence
CSV_Record_Occurrences
Primary_Record_Group_Size
Merge_Basis
Alternate_Titles
207_Paper_IDs
259_Corpus_IDs
Data_Quality_Notes
```

The names `207` and `259` inside column names are allowed because they are metadata already embedded inside the locked 325-record file. They do **not** authorize loading those earlier datasets.

---

# 2. SCIENTIFIC OBJECTIVE

Let the supplied corpus be

\[
\mathcal P=\{P_1,\ldots,P_{325}\}.
\]

The scientific objective is not to reproduce an earlier rank. It is to estimate, under structured uncertainty,

\[
\boxed{
\text{importance of }P_i\text{ to the thesis within this locked dataset}
}
\]

and to quantify the stability of that ranking.

The thesis targets already represented inside the dataset are

\[
\mathcal H=\{H1,H2,H3,H4,H5,H6,H7,T1\}.
\]

Do not infer new hypotheses from outside the CSV.

---

# 3. PRISMA-STYLE CLOSED-CORPUS CONDITIONS

Use PRISMA principles only for transparent accounting and eligibility inside the supplied corpus.

Report:

```text
records_supplied = 325
internal_duplicate_canonical_id
internal_duplicate_normalized_doi
internal_duplicate_normalized_title
protocol_support_excluded_from_scientific_ranking
scientific_records_ranked
identity_conflict_warnings
```

The correct methodological label is:

```text
CLOSED_CORPUS_PRISMA_STYLE_SCREENING
```

Never claim:

```text
PRISMA search identified all relevant global literature.
```

Allowed conclusion:

> These are the most robustly ranked papers within the supplied 325-record corpus under the frozen model.

---

# 4. IDENTITY AND DUPLICATION GATE

Normalize DOI by lowercasing, stripping whitespace, removing DOI URL prefixes and `doi:`, and stripping trailing punctuation.

Normalize title using Unicode normalization, lowercase conversion, punctuation removal, and whitespace collapse.

Require:

\[
\#\{Canonical\_ID\text{ duplicates}\}=0,
\]

\[
\#\{normalized\ DOI\text{ duplicates}\}=0,
\]

and

\[
\#\{normalized\ title\text{ duplicates}\}=0.
\]

If any is non-zero, stop.

Do not perform fuzzy auto-merging because the file is already declared final-unique.

---

# 5. SCIENTIFIC RANKING ELIGIBILITY

Records with

```text
Relevance_259 = C_PROTOCOL_SUPPORT
```

remain in the audit but do not compete in the scientific thesis-paper ranking.

All other records remain rankable unless the file itself violates an identity invariant.

A `CONFLICTING_DOI` note must **not** cause automatic deletion. Keep the paper, reduce identity confidence, and flag:

```text
Identity_Conflict_Warning = TRUE
```

Identity uncertainty is not equivalent to scientific irrelevance.

---

# 6. ANTI-LEAKAGE RULE

The following historical ranking/selection fields are **forbidden predictors**:

```text
Final_Unique_Rank
Best_Priority_Tier
Max_Importance_Score
Selected_Core_164
Rank_76
Rank_141
Rank_164
Source_Presence
CSV_Record_Occurrences
207_Paper_IDs
259_Corpus_IDs
```

They may be used only **after the new Monte Carlo ranking is complete** for external validation.

Never allow

\[
\text{old rank}
\rightarrow
\text{new score}
\rightarrow
\text{new rank}.
\]

---

# 7. ONLY FOUR SCIENTIFIC SCORE CRITERIA ARE PERMITTED

Because this run is restricted to the CSV and may not read PDFs, abstracts, or external sources, do **not** invent full-text mathematical-rigor scores, physical-rigor scores, empirical-validation scores, citation counts, journal impact factors, or evidence anchors absent from the dataset.

Use only

\[
\mathbf x_i=(H_i,R_i,D_i,T_i),
\]

where:

- \(H_i\) = hypothesis/target coverage;
- \(R_i\) = direct/foundational thesis relevance;
- \(D_i\) = disciplinary fit;
- \(T_i\) = controlled title-level architecture fit.

Require

\[
0\le x_{ik}\le1.
\]

Evidence quality is represented separately by \(q_i\).

---

# 8. HYPOTHESIS-COVERAGE CRITERION

Parse only `Relevant_Hypotheses` for

```text
H1 H2 H3 H4 H5 H6 H7 T1
```

Let \(n_h\) be the number of scientifically rankable papers tagged with \(h\), and \(N\) the rankable scientific corpus size.

Set

\[
p_h=
\begin{cases}
1,&h\in\{H1,\ldots,H6\},\\
0.5,&h=H7,\\
0.75,&h=T1.
\end{cases}
\]

Define

\[
r_h
=
p_h
\log
\left(
\frac{N+1}{n_h+1}
\right)
\]

and

\[
\tilde r_h
=
\frac{r_h}{\max_j r_j}.
\]

For paper \(i\),

\[
H_i
=
0.80
\max_{h\in\mathcal H_i}
\tilde r_h
+
0.20
\min
\left(
1,
\frac{|\mathcal H_i|}{3}
\right).
\]

If `Relevant_Hypotheses` is missing:

```text
H_i = NA
```

not zero.

---

# 9. RELEVANCE CRITERION

Map `Relevance_207`:

```text
CORE            -> 1.00
STRONG_APPLIED  -> 0.85
FOUNDATION      -> 0.80
SUPPORTING      -> 0.50
```

Map `Relevance_259`:

```text
A_CORE_DIRECT                  -> 1.00
B_FOUNDATIONAL_TRANSFERABLE    -> 0.80
C_SUPPORTING_METHOD_CONTEXT    -> 0.50
C_PROTOCOL_SUPPORT             -> 0.10
```

Within a source field containing several labels, use the maximum value.

If both sources are represented,

\[
R_i
=
\frac{
R_i^{207}
+
R_i^{259}
}{2}.
\]

If only one is available, use the available source.

Do not penalize a paper merely because one historical source field is missing.

---

# 10. DISCIPLINE-FIT CRITERION

Use only `Primary_Discipline` and `Discipline_Coverage`.

Controlled weights:

```text
Mathematics / Control / Reachability / Viability / Inverse / Optimization / UQ -> 1.00
Infrastructure Systems                                                       -> 1.00
Reliability / Resilience Engineering                                         -> 0.95
Physics / Complex Networks                                                   -> 0.95
Sustainable Engineering                                                      -> 0.90
Industrial Ecology                                                           -> 0.90
Cross-disciplinary Methods                                                   -> 0.75
Systematic Review Methodology                                                -> 0.30
```

For matched groups \(d_{ij}\),

\[
D_i
=
0.80\max_jd_{ij}
+
0.20
\min
\left(
1,\frac{m_i}{4}
\right).
\]

This rewards centrality and useful interdisciplinary breadth without allowing breadth to dominate.

---

# 11. TITLE-ARCHITECTURE CRITERION

Use only `Canonical_Title` and a frozen controlled vocabulary covering:

```text
interface/coupling
identification/inverse/UQ
timescale/dynamic/static approximation
viability/reachability/Hamilton-Jacobi
recovery/restoration/resilience
sustainability/equity/industrial ecology
power/water/transport/waste/infrastructure
flood/climate/hazard/debris/blockage/cascade
model reduction/decomposition/conservative error
```

Do not use embeddings, LLM semantic scoring, external knowledge, or ad-hoc reclassification.

For detected group strengths \(t_{ij}\),

\[
T_i
=
0.70\max_jt_{ij}
+
0.30
\min
\left(
1,\frac{g_i}{4}
\right).
\]

If no controlled architecture term appears, set

\[
T_i=0.20.
\]

Absence from the title is not proof of absence from the paper.

---

# 12. EVIDENCE-CONFIDENCE MODEL

Construct

\[
q_i\in(0,1].
\]

Use only:

```text
Verification_Status
Local_Full_Text_207
High_Rigor_Candidate_259
Evidence_Stratum_207
Canonical_Title_Selection
Merge_Basis
Data_Quality_Notes
DOI
```

Verification mapping:

```text
FULL_TEXT_EVIDENCE_PRIOR_AUDIT                    -> 1.00
publisher verification                            -> 0.92
PROJECT_MASTER_DOI_TITLE_AUDITED                   -> 0.88
LOCAL_METADATA_VERIFIED                            -> 0.82
CURATED_PRIOR_AUDIT                                -> 0.75
ABSTRACT_ONLY_PRIOR_AUDIT                          -> 0.70
verified preprint                                  -> 0.65
otherwise                                          -> 0.60
```

Full-text/access:

```text
YES          -> 1.00
ONLINE_PAGE  -> 0.75
UNKNOWN      -> 0.55
NO           -> 0.35
missing      -> 0.55
```

High-rigor candidate:

```text
True     -> 1.00
False    -> 0.40
missing  -> 0.65
```

Evidence stratum:

```text
A       -> 1.00
A/B     -> 0.90
B       -> 0.80
missing -> 0.65
```

Identity confidence must use `Canonical_Title_Selection`, `Merge_Basis`, `Data_Quality_Notes`, and DOI presence.

A `CONFLICTING_DOI` strongly lowers identity confidence but does not automatically exclude the paper.

Aggregate by weighted geometric mean:

\[
q_i
=
\exp
\left(
\sum_j a_j\log c_{ij}
\right),
\qquad
\sum_ja_j=1.
\]

Use weights:

```text
verification           0.30
full-text/access       0.18
high-rigor flag        0.15
evidence stratum       0.10
identity quality       0.22
metadata completeness  0.05
```

---

# 13. MISSINGNESS

Never use

\[
NA=0.
\]

Let \(\mathcal O_i\) be the observed scientific criteria for paper \(i\).

All scores are renormalized over \(\mathcal O_i\):

\[
S_{i,\mathrm{raw}}^{(m)}
=
\frac{
\sum_{k\in\mathcal O_i}
w_k^{(m)}
X_{ik}^{(m)}
}{
\sum_{k\in\mathcal O_i}
w_k^{(m)}
}.
\]

Missingness instead reduces evidence confidence.

---

# 14. UNCERTAIN CRITERION VALUES

For each observed criterion mean \(\mu_{ik}\),

\[
X_{ik}^{(m)}
\sim
\operatorname{Beta}
(\alpha_{ik},\beta_{ik}).
\]

Set

\[
\kappa_i
=
8+52q_i,
\]

\[
\alpha_{ik}
=
\mu_{ik}\kappa_i,
\qquad
\beta_{ik}
=
(1-\mu_{ik})\kappa_i.
\]

Numerically clip exact means only to

\[
[10^{-4},1-10^{-4}]
\]

before Beta parameterization.

Higher-confidence records therefore receive narrower uncertainty distributions.

---

# 15. UNCERTAIN WEIGHTS

Baseline:

\[
\bar{\mathbf w}
=
(0.30,0.30,0.20,0.20)
\]

for

```text
Hypothesis_Coverage
Relevance
Discipline_Fit
Title_Architecture_Fit
```

Sample

\[
\mathbf w^{(m)}
\sim
\operatorname{Dirichlet}
\left(
100\bar{\mathbf w}
\right)
\]

subject to:

```text
Hypothesis_Coverage      0.18 <= w <= 0.42
Relevance                0.18 <= w <= 0.42
Discipline_Fit           0.10 <= w <= 0.30
Title_Architecture_Fit   0.08 <= w <= 0.30
```

and

\[
\sum_kw_k^{(m)}=1.
\]

Use rejection sampling. Fail if a retained vector violates the simplex or bounds.

---

# 16. PRIMARY SCORE

For run \(m\),

\[
S_{i,\mathrm{raw}}^{(m)}
=
\frac{
\sum_{k\in\mathcal O_i}
w_k^{(m)}X_{ik}^{(m)}
}{
\sum_{k\in\mathcal O_i}
w_k^{(m)}
}.
\]

Require monotonicity:

\[
\frac{\partial S_i}
{\partial X_{ik}}
\ge0.
\]

Apply confidence:

\[
\boxed{
S_i^{(m)}
=
S_{i,\mathrm{raw}}^{(m)}
\left[
0.70+0.30q_i
\right].
}
\]

Require:

\[
0\le S_i^{(m)}\le1.
\]

---

# 17. MONTE CARLO EXECUTION

Official random seed:

```text
20260820
```

Primary run:

```text
M = 50,000
```

Minimum final-run size:

```text
M >= 10,000
```

Anything below 10,000 is smoke testing only.

---

# 18. OUTPUT DISTRIBUTIONS

For every scientific paper calculate:

\[
\hat\mu_i,
\qquad
\hat\sigma_i,
\qquad
SE_{MC,i}
=
\frac{\hat\sigma_i}{\sqrt M}.
\]

Also calculate:

```text
score 2.5% quantile
median score
score 97.5% quantile
mean rank
rank 2.5% quantile
median rank
rank 97.5% quantile
P(Top 10)
P(Top 25)
P(Top 50)
P(Top 100)
P(Top K)
```

Default operational target:

```text
K = 140
```

but K is not a scientific claim about the required literature size.

Require:

\[
P(Top10)
\le
P(Top25)
\le
P(Top50)
\le
P(Top100)
\le
P(TopK).
\]

---

# 19. ROBUST SELECTION INDEX

Define

\[
\boxed{
RSI_i
=
\left[
\hat\mu_i
P_i^{(K)}
q_i
\right]^{1/3}.
}
\]

Final rank order:

1. descending RSI;
2. descending mean Monte Carlo score;
3. descending \(P(TopK)\);
4. ascending `Canonical_ID`.

Never use historical rank fields as tie-breakers.

---

# 20. ROBUST CORE

Report both:

```text
Operational Top-K
```

and

```text
Robust Core
```

Define robust core by

\[
P_i^{(K)}
\ge0.90
\]

and

\[
q_i\ge0.70.
\]

The robust core must be allowed to contain fewer or more than K papers.

---

# 21. CONVERGENCE

Split the official simulation into two halves.

Require for the leading candidate set:

\[
\max SE_{MC,i}
\le0.0025,
\]

\[
\max
\left|
\hat\mu_i^{(1)}
-
\hat\mu_i^{(2)}
\right|
\le0.010,
\]

\[
\max
\left|
P_i^{(K,1)}
-
P_i^{(K,2)}
\right|
\le0.020,
\]

and whole-ranking Spearman stability

\[
\rho_S\ge0.98.
\]

Failure produces:

```text
PROVISIONAL_RANKING_QA_NOT_FULLY_PASSED
```

---

# 22. RANDOM-SEED STABILITY

Repeat reduced simulations using:

```text
20260821
20260822
```

with at least 10,000 runs each.

Require:

\[
\rho_S\ge0.95
\]

for full-rank comparison and

\[
Jaccard(TopK_{\mathrm{official}},TopK_{\mathrm{seed}})
\ge0.90.
\]

---

# 23. ALTERNATIVE AGGREGATION

Run a sensitivity model using weighted geometric aggregation:

\[
G_i^{(m)}
=
\exp
\left(
\frac{
\sum_{k\in\mathcal O_i}
w_k^{(m)}
\log X_{ik}^{(m)}
}{
\sum_{k\in\mathcal O_i}
w_k^{(m)}
}
\right).
\]

Apply the same confidence adjustment.

Report Spearman agreement between primary and alternative mean ranks.

Do **not** label ordinary weight analysis as Sobol sensitivity: Dirichlet weights are dependent through the simplex constraint.

---

# 24. WEIGHT SENSITIVITY

For the Top-25 papers calculate the association between each sampled criterion weight and the paper's adjusted score.

Store:

```text
Canonical_ID
Canonical_Title
Criterion_Weight
Pearson_Correlation_Weight_vs_Adjusted_Score
```

---

# 25. PAIRWISE DOMINANCE

For each pair among Top-25:

\[
D_{ij}
=
P(S_i>S_j)
\]

with estimator

\[
\hat D_{ij}
=
\frac1M
\sum_{m=1}^{M}
\mathbf1
[
S_i^{(m)}>S_j^{(m)}
].
\]

Interpretation:

```text
approximately 0.50 -> ordering unresolved
>= 0.95            -> strong dominance under the frozen model
```

---

# 26. HYPOTHESIS-SPECIFIC RANKINGS

For each target

```text
H1 H2 H3 H4 H5 H6 H7 T1
```

filter the papers tagged with that target and rank them by the final RSI.

Output:

```text
Hypothesis
Hypothesis_Rank
Canonical_ID
Canonical_Title
DOI
Monte_Carlo_Global_Rank
Robust_Selection_Index
Mean_Score
Evidence_Confidence_q
```

Do not infer target membership externally.

---

# 27. HISTORICAL-RANK VALIDATION

Only after the new ranking is complete, compare it descriptively with:

```text
Final_Unique_Rank
Rank_76
Rank_141
Rank_164
Max_Importance_Score
Selected_Core_164
```

These fields may never alter the new result.

---

# 28. REQUIRED OUTPUTS

Generate:

```text
01_monte_carlo_rank_all_scientific.csv
02_operational_top_140.csv
03_robust_core_probability_ge_0_90.csv
04_hypothesis_specific_rankings.csv
05_feature_matrix.csv
06_pairwise_dominance_top25.csv
07_weight_sensitivity_top25.csv
08_seed_stability.csv
09_criterion_spearman_correlation.csv
10_external_validation_against_historical_rank_columns.csv
11_closed_corpus_prisma_accounting.csv
12_protocol_support_not_scientifically_ranked.csv
run_manifest.json
```

The main table must contain:

```text
Monte_Carlo_Rank
Canonical_ID
Canonical_Title
Authors
Year
Journal
DOI
Relevant_Hypotheses
Primary_Discipline
Evidence_Confidence_q
Hypothesis_Coverage_Base
Relevance_Base
Discipline_Fit_Base
Title_Architecture_Fit_Base
Mean_Score
SD_Score
MCSE
Score_CI2.5
Median_Score
Score_CI97.5
Mean_Rank
Rank_CI2.5
Median_Rank
Rank_CI97.5
P_Top10
P_Top25
P_Top50
P_Top100
P_Top140
Robust_Selection_Index
Identity_Conflict_Warning
```

---

# 29. REPRODUCIBILITY MANIFEST

Record:

```text
input path
input SHA256
protocol/config SHA256
Python version
platform
random seed
Monte Carlo run count
weight distribution
weight bounds
confidence model
convergence thresholds
scientific predictors
confidence fields
forbidden predictor fields
closed-corpus PRISMA counts
best paper
final QA status
```

Explicitly state:

> Ranks only records contained in the supplied 325-row CSV. No external search, full-text reading, web verification, or other project files were used.

---

# 30. MATHEMATICAL QA INVARIANTS

Verify:

\[
\boxed{
\begin{aligned}
&N_{\mathrm{input}}=325,\\
&N_{\mathrm{CanonicalID\ duplicates}}=0,\\
&N_{\mathrm{DOI\ duplicates}}=0,\\
&N_{\mathrm{title\ duplicates}}=0,\\
&\sum_k w_k^{(m)}=1\quad\forall m,\\
&l_k\le w_k^{(m)}\le u_k,\\
&0\le S_i^{(m)}\le1,\\
&0\le P_i^{(K)}\le1,\\
&P(Top10)\le P(Top25)\le P(Top50)\le P(Top100)\le P(TopK),\\
&\text{no forbidden predictor leakage},\\
&N_{\mathrm{scientific}}+N_{\mathrm{protocol}}=325.
\end{aligned}
}
\]

Failure of any invariant produces `FAIL`.

---

# 31. FINAL SCIENTIFIC LANGUAGE

Allowed:

> Paper X is Rank 1 within the locked 325-record corpus under the frozen PRISMA-style Monte Carlo model and passed the specified convergence and sensitivity checks.

Not allowed:

> Paper X is mathematically proven to be the best paper in the entire global literature.

Allowed:

> The Top-140 is an operational thesis subset; the robust core contains papers whose Top-140 probability and evidence confidence exceed the prespecified thresholds.

Not allowed:

> Exactly 140 papers are scientifically necessary.

---

# 32. EXECUTION ORDER

```text
A. Verify exact input SHA256.
B. Verify 325 rows and exact 34-column schema.
C. Audit Canonical_ID, DOI and normalized-title duplicates.
D. Freeze configuration and protocol hash.
E. Separate C_PROTOCOL_SUPPORT records from scientific ranking.
F. Assert historical ranking columns are not predictors.
G. Build H, R, D and T scientific features.
H. Build evidence confidence q separately.
I. Audit criterion correlations descriptively.
J. Run official Monte Carlo simulation with seed 20260820.
K. Compute score/rank distributions and Top-K probabilities.
L. Compute RSI and final global ranking.
M. Compute robust core.
N. Run convergence tests.
O. Run weighted-geometric alternative aggregation.
P. Run independent-seed stability checks.
Q. Compute Top-25 pairwise dominance.
R. Compute Top-25 weight sensitivity.
S. Produce H1-H7/T1-specific rankings.
T. Compare historical rank fields only as post-hoc validation.
U. Generate CSV outputs and run_manifest.json.
V. Print final status and Rank-1 paper.
```

---

# 33. FINAL CONSOLE SUMMARY

```text
========================================================================
CLOSED-CORPUS PRISMA + MONTE CARLO PAPER RANKING
========================================================================
INPUT FILE:
INPUT SHA256:
PROTOCOL/CONFIG SHA256:
RECORDS SUPPLIED: 325
INTERNAL DUPLICATES:
PROTOCOL/SUPPORT RECORDS NOT SCIENTIFICALLY RANKED:
SCIENTIFIC RECORDS RANKED:
IDENTITY WARNINGS:
MONTE CARLO RUNS:
OFFICIAL SEED:
CONVERGENCE PASS:
SEED STABILITY PASS:
ALTERNATIVE AGGREGATION RANK SPEARMAN:
ROBUST CORE SIZE:

BEST PAPER WITHIN THIS LOCKED DATASET:
RANK 1:
DOI:
RSI:
MEAN SCORE:
P(TOP K):
EVIDENCE CONFIDENCE:
IDENTITY WARNING:

BEST H1:
BEST H2:
BEST H3:
BEST H4:
BEST H5:
BEST H6:
BEST H7:
BEST T1:

FINAL STATUS:
ROBUST_WITHIN_LOCKED_325_CORPUS
or
PROVISIONAL_RANKING_QA_NOT_FULLY_PASSED
or
FAIL
========================================================================
```

# 34. MOST IMPORTANT RULE

The procedure answers only

\[
\boxed{
\text{Which papers are most robustly important within this exact 325-record dataset?}
}
\]

It does **not** answer

\[
\boxed{
\text{Which papers are globally the best in all literature?}
}
\]

The scientific strength of the result comes from the frozen input, anti-leakage design, explicit uncertainty, probability-of-selection analysis, convergence tests, seed stability, alternative aggregation, and reproducible mathematical invariants—not from claiming evidence the dataset does not contain.

Use the supplied executable Python implementation `prisma_monte_carlo_rank_325.py` without changing the frozen equations or predictor set unless an amendment is documented before execution.
