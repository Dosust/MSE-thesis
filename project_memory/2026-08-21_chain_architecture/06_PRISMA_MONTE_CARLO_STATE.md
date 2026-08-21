# PRISMA / Closed-Corpus Monte Carlo State

## 1. Global evidence status

The project must keep two statements separate:

1. **Global PRISMA review status:** not yet complete/frozen as a globally exhaustive systematic search.
2. **Closed-corpus 325-paper Monte Carlo ranking:** completed as a ranking exercise within a locked dataset.

Do not use the second to claim the first.

## 2. Locked 325-record dataset

Authoritative closed-corpus input used in the final ranking discussion:

`Thesis_Final_Unique_Papers_325_2026-08-20(1).csv`

Frozen SHA-256:

`047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f`

Expected dimensions:

- 325 rows;
- 34 columns.

The protocol explicitly forbids importing external sources or earlier 207/259/333/141/164/76 datasets into the ranking run.

## 3. Scientific ranking eligibility

- 325 supplied records.
- 3 `C_PROTOCOL_SUPPORT` records remain in audit but are excluded from scientific ranking.
- 322 scientific records ranked in the final four-criterion implementation.
- identity conflict warnings are retained and penalized in confidence rather than automatically deleted.

## 4. Anti-leakage rule

Historical fields such as earlier ranks, selection tiers, source-presence counts and historical corpus IDs are forbidden scientific predictors. They can only be used post hoc for descriptive validation.

## 5. Frozen scientific score structure

Only four scientific criteria are permitted in the final prompt:

- H = hypothesis/target coverage;
- R = direct/foundational thesis relevance;
- D = disciplinary fit;
- T = controlled title-level architecture fit.

Evidence confidence is separate:

- `q_i` = evidence/identity confidence.

Missing scientific features are not silently set to zero; the score renormalizes over observed criteria while missingness can reduce confidence.

## 6. Monte Carlo structure

Final prompt parameters:

- official seed: `20260820`;
- official run size: 50,000;
- minimum final run: 10,000;
- target operational K: 140;
- independent reduced seed checks: 20260821 and 20260822, at least 10,000 runs each;
- baseline criterion weights: `(0.30, 0.30, 0.20, 0.20)`;
- bounded Dirichlet weight uncertainty;
- criterion uncertainty represented through Beta distributions whose concentration increases with evidence confidence `q`.

Primary adjusted score:

```text
S_i = S_raw,i * (0.70 + 0.30 q_i)
```

Robust Selection Index:

```text
RSI_i = [mean_score_i * P_i(TopK) * q_i]^(1/3)
```

Robust core rule:

```text
P(Top140) >= 0.90 and q >= 0.70
```

## 7. Final high-rigor run results preserved in this chat

The final run reported:

- 50,000 official Monte Carlo simulations;
- convergence PASS;
- independent-seed stability PASS;
- weighted-geometric alternative aggregation high rank agreement;
- 80-paper robust core in the `HIGH_RIGOR_RUN` implementation;
- operational Top-140;
- Rank-1: *Multi-timescale risk-averse restoration for interdependent water-power networks with joint reconfiguration and diverse uncertainties*, DOI `10.1016/j.ress.2025.111083`.

The discussion also compared three packages:

1. `PRISMA_MC_325_EXECUTED_2026-08-20` — six-criterion alternative/stress-test model; 321 scientific papers due to different conflict handling; 100,000 simulations.
2. `PRISMA_MC_325_FULL_RUN_RESULTS` — four-criterion + separate confidence model; 322 scientific papers; 50,000 runs; 75-paper robust core.
3. `PRISMA_MC_325_HIGH_RIGOR_RUN_2026-08-20` — four-criterion + separate confidence model; 322 papers; 50,000 runs; 80-paper robust core.

The current discussion judged `FULL_RUN_RESULTS` to be the strongest controlling implementation of the frozen title-architecture scoring formula, while `HIGH_RIGOR_RUN` is a sensitivity replication and `EXECUTED` is an alternative-model stress test.

## 8. Stable cross-model literature insight

Across the three ranking models, the most important result was not an uncontested single winner but a pair of co-dominant precedents:

1. **Multi-timescale risk-averse restoration for interdependent water-power networks...**
2. **Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery**

Four papers were reported as Top-10 in all three models:

- the multi-timescale water–power restoration paper;
- the sustainability/climate transport-recovery paper;
- *Novel methodology for resilience assessment of critical infrastructure considering the interdependencies*;
- *Community resilience-driven restoration model for interdependent infrastructure networks*.

The discussion also identified 17 papers common to all three Top-25s, 34 common to all Top-50s, and 92 common to all Top-140s.

These overlap counts are useful robustness diagnostics but remain **within the locked corpus and the compared scoring models**.

## 9. Hypothesis-specific insight preserved

The comparison found especially stable winners for H1, H2, H3, H4 and H6, while H5, H7 and T1 were more model-sensitive.

Interpretation preserved:

- H2 strongly reinforces the importance of multiscale/timescale-aware interdependent restoration;
- H3/H4/H6 highlight the sustainability/climate/recovery bridge;
- H5 exposes a distinction between recovery as sustainability/performance and recovery as dynamic control/reachability;
- H7 is sensitive to dynamic hazard-propagation versus broader multihazard-assessment framing;
- T1 lacks one uncontested precedent and therefore needs careful falsification rather than novelty rhetoric.

## 10. Epistemic limits

Allowed statement:

> These papers are robustly ranked within the supplied 325-record corpus under the declared frozen model.

Forbidden statement:

> The ranking proves which papers are globally best or proves the thesis is globally novel.

PRISMA and Monte Carlo serve different purposes:

- PRISMA = transparent search/screening/accounting;
- Monte Carlo = robustness of ranking under declared uncertainty within an eligible corpus.

Neither method mathematically proves global novelty.

## 11. Repository locations

- Master prompt: `prompts/PRISMA_Monte_Carlo_325_Single_Dataset_Master_Prompt.md`
- Older/alternate prompt: `prompts/PRISMA_MC_325_MASTER_PROMPT.md`
- Final run folder: `methods/monte_carlo/final_run_2026-08-20/`
- Code reconstruction material: `methods/monte_carlo/code_parts/`, `methods/monte_carlo/reconstruct_code.py`
- Results folder: `methods/monte_carlo/results/`
- Online/binary archive links: `provenance/ONLINE_ARCHIVE.md`
- Provenance hashes: `provenance/SHA256SUMS.txt`, `provenance/INVENTORY.csv`

## 12. Pending systematic-review condition

Before a final thesis novelty freeze, the project still requires completion/reconciliation of the declared database-search workflow and evidence review. Historical working plans included Scopus, Web of Science, Compendex and IEEE Xplore plus backward/forward citation searching. Future chats must check the current repository/protocol state before assuming these are complete.