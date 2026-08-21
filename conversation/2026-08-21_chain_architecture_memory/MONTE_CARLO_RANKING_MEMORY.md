# Frozen-Corpus PRISMA + Monte Carlo Ranking Memory

## 1. Data boundary

The ranking work in this session was explicitly closed-corpus.

Frozen dataset identity:

`Thesis_Final_Unique_Papers_325_2026-08-20(3).csv`

SHA-256:

`047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f`

Known integrity facts from the executed analysis:

- 325 input rows;
- 325 unique `Canonical_ID` values;
- 308 non-empty DOI values;
- 17 missing DOI values;
- 0 duplicate non-empty DOI values;
- 0 duplicate normalized canonical titles.

No external bibliographic data were permitted in the scoring model.

## 2. PRISMA-compatible eligibility gate

The 100k six-criterion run used PRISMA only for transparent gating/reporting, not as a ranking method.

Counts:

- `ELIGIBLE`: 321
- `METHODS_ONLY`: 3
- `HOLD`: 1
- `EXCLUDE`: 0

The HOLD record was triggered by `CONFLICTING_DOI`, following the user's fixed rule not to resolve the conflict externally.

## 3. Anti-circularity

Forbidden from scoring:

- `Final_Unique_Rank`
- `Best_Priority_Tier`
- `Max_Importance_Score`
- `Selected_Core_164`
- `Rank_76`
- `Rank_141`
- `Rank_164`

These could be used only after the new ranking was frozen for validation/disagreement analysis.

## 4. Six scoring criteria

1. Direct Relevance
2. Theory Architecture
3. Disciplinary Fit
4. Evidence Credibility
5. Primary Corpus Corroboration
6. Title Semantic Directness

Each criterion used a center `mu_ic` and confidence `rho_ic`, with feature uncertainty represented through a Beta distribution.

Concentration rule:

`kappa_ic = 4 + 96 rho_ic`

with clipped means and corresponding Beta alpha/beta parameters.

## 5. Weight uncertainty

Four scenario centers were used in criterion order:

`[Direct_Relevance, Theory_Architecture, Disciplinary_Fit, Evidence_Credibility, Primary_Corpus_Corroboration, Title_Semantic_Directness]`

Balanced:

`(0.22, 0.22, 0.16, 0.20, 0.06, 0.14)`

Theory:

`(0.15, 0.30, 0.20, 0.18, 0.04, 0.13)`

Evidence:

`(0.18, 0.18, 0.14, 0.32, 0.06, 0.12)`

Applied:

`(0.28, 0.16, 0.12, 0.18, 0.06, 0.20)`

Each realization chose a scenario uniformly and sampled weights from a Dirichlet distribution centered at that scenario.

## 6. Simulation

- official realizations: `20 × 5000 = 100000`;
- seed: `20260820`;
- substantive competition: 321 ELIGIBLE papers.

Per-paper outputs included:

- Expected Rank;
- P(Rank 1);
- P(Top 5);
- P(Top 10);
- P(Top 25);
- Mean MC Score;
- SD MC Score;
- complete rank-acceptability distribution `P(R_i=r)`.

## 7. Mathematical accuracy / convergence

For `N = 100000`:

Worst-case Bernoulli probability SE:

`SE_max = 1/(2 sqrt(N)) ≈ 0.00158114`

Worst-case 95% half-width:

`1.96 SE_max ≈ 0.00309903`

99% Hoeffding epsilon:

`epsilon = sqrt( ln(2/0.01)/(2N) ) ≈ 0.005147`

The executed analysis declared convergence PASS under the user's three requirements:

1. 95% half-width <= 0.005;
2. last-five cumulative-batch max absolute P(Top10) change <= 0.010;
3. minimum consecutive final-five Top-10 Jaccard >= 0.80.

The complete rank-acceptability matrix was also checked for row/column probability normalization.

## 8. Robust winner — 100k six-criterion model

Winner under the fixed lexicographic rule:

**Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery**

Canonical ID recorded in the executed analysis:

`P_553266e64e3d`

The scientifically correct wording is:

> the paper with the strongest robust rank under this pre-specified dataset-only uncertainty model.

Do not call it the universally best paper in the literature.

## 9. Comparison of three runs

Packages compared in the chat:

- `PRISMA_MC_325_EXECUTED_2026-08-20(3).zip`
- `PRISMA_MC_325_FULL_RUN_RESULTS(3).zip`
- `PRISMA_MC_325_HIGH_RIGOR_RUN_2026-08-20(3).zip`

### Main methodological insight

The three packages are not identical replications.

- EXECUTED: 100k, six explicit criteria, strict HOLD for conflicting DOI.
- FULL: 50k, earlier four-predictor/RSI-style framework.
- HIGH-RIGOR: 50k, refined version of the earlier four-predictor/RSI family.

Therefore cross-run rank changes largely reflect **different model specifications**, not MC sampling error.

### Cross-run leaders

The two papers most stable at the top were:

1. **Multi-timescale risk-averse restoration for interdependent water-power networks with joint reconfiguration and diverse uncertainties**.
2. **Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery**.

Interpretation:

- first paper strongly anchors dynamic coupled restoration/control under uncertainty;
- second strongly anchors sustainability/climate-resilient recovery trade-offs and broader theory architecture.

### Whole-ranking agreement reported in the comparison

Approximate Spearman correlations discussed:

- FULL ↔ HIGH-RIGOR: ~0.969
- EXECUTED ↔ HIGH-RIGOR: ~0.668
- EXECUTED ↔ FULL: ~0.645

Use these as session-recorded comparison results; if they are used in a paper, recompute directly from the archived output CSVs rather than citing this memory file alone.

### Top-set insight

FULL and HIGH-RIGOR had very strong Top-K agreement, whereas EXECUTED differed more because it explicitly rewarded the newer six-dimensional thesis architecture.

A 17-paper cross-model Top-25 intersection was identified in the chat, including papers on:

- multi-timescale water–power restoration;
- sustainability/climate transport recovery;
- interdependent resilience methodology across water/transport/electricity;
- community resilience-driven restoration;
- equitable infrastructure resilience;
- interdependent network design/restoration;
- disaster waste management under uncertainty;
- equity in resilience research;
- protection–interdiction–restoration;
- flood-driven power–wastewater co-simulation;
- infrastructure simulation frameworks.

## 10. Scientific interpretation for thesis architecture

The stable ranking evidence does **not** point toward a generic resilience-index thesis. It repeatedly emphasizes the intersection:

`coupled infrastructure + dynamic interdependency + restoration/control + uncertainty + sustainability/equity + hazard/climate`

This is consistent with the current thesis center:

`dynamic interfaces → coupled dynamics → viability/recoverability → recovery control`

## 11. Reproducibility pointers

Exact master prompt:

`prompts/PRISMA_MC_325_MASTER_PROMPT.md`

Existing Monte Carlo methods/results directories should be inspected before creating new runs. Do not rerun or overwrite blindly if a frozen result already exists.

For any publication use:

- verify input SHA-256;
- verify exact model/code version;
- distinguish 100k six-criterion results from 50k earlier-model results;
- use output CSV/JSON audit files as the primary computational evidence, not this narrative memory.