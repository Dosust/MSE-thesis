# PRISMA + Monte Carlo Ranking Conditions — 325 Dataset Only

This protocol is locked to `Thesis_Final_Unique_Papers_325_2026-08-20(2).csv` and no other literature dataset.

## Hard conditions
1. Exactly 325 input rows and all 34 required columns.
2. Unique `Canonical_ID`, unique normalized `Canonical_Title`, unique normalized nonblank DOI.
3. `CONFLICTING_DOI` => hard hold; excluded from scientific Monte Carlo.
4. `YEAR_CONFLICT` => provisional ranking only; cannot be final Tier 1.
5. `Systematic Review Methodology` / `C_PROTOCOL_SUPPORT` => PRISMA support stratum, not scientific Top-paper competition.
6. Historical rank fields (`Final_Unique_Rank`, `Rank_76`, `Rank_141`, `Rank_164`, `Max_Importance_Score`, `Best_Priority_Tier`, `Selected_Core_164`) are prohibited as primary ranking inputs.
7. Missing evidence is uncertainty, not zero.
8. No web enrichment and no other corpus may be merged.

## Scientific criteria
C1 thesis-architecture alignment; C2 mathematical/physical depth; C3 dynamic-interface relevance; C4 viability/HJ/reachability; C5 identification/inverse/UQ; C6 recovery/reliability; C7 sustainability/equity; C8 P-W-T-SW/flood relevance; C9 evidence verification; C10 record integrity.

## Stochastic model
For paper i and criterion j:

`X_ij ~ Beta(mu_ij*kappa_ij, (1-mu_ij)*kappa_ij)`.

Weights satisfy `w_j >= 0`, `sum(w)=1`, frozen lower/upper bounds, and are sampled from five Dirichlet regimes. Utility is `U_i = sum_j w_j X_ij`.

## Monte Carlo size
With epsilon=0.01, delta=0.01 and expected N=321 scientific-eligible records, the Hoeffding + union-bound requirement is 55,349 draws. Production setting is 100,000 draws per seed × 10 seeds = 1,000,000 draws.

## Robust ranking metrics
P(rank 1), P(Top 5), P(Top 10), P(Top 20), expected rank, median rank, 90th-percentile rank, mean utility and utility SD.

## Frozen robust order
1. P(Top 10) descending;
2. expected rank ascending;
3. P(rank 1) descending;
4. Canonical_ID ascending.

## Final top-tier condition
P(Top10)>=0.80, median rank<=10, Q90 rank<=25, full-text evidence indicated in dataset, no year conflict, no conflicting DOI.

## Stability
For Top 20 sets from 10 seeds, minimum pairwise Jaccard must be >=0.85. Otherwise `RANKING_UNSTABLE`.

## Scope language
The result may be called the highest-ranked paper within this frozen 325-record dataset. It must never be described as the globally best paper or as proof of novelty.
