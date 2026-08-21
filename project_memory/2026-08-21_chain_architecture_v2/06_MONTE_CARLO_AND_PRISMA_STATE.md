# PRISMA and Closed-Corpus Monte Carlo State — Corrected v2

## 1. Two evidence processes must remain separate

### Global/systematic literature review

Purpose: search, screen, deduplicate, assess eligibility, extract evidence and test novelty/gap claims across the declared literature-search scope.

Current memory status: **not safely describable as globally complete/frozen unless the latest database-search evidence proves completion**.

### Closed-corpus Monte Carlo ranking

Purpose: rank papers **within one locked 325-record dataset** under a frozen uncertainty model.

This exercise is complete as a corpus-relative analysis.

Do not use closed-corpus ranking to claim global literature completeness or global novelty.

---

## 2. Frozen logical input

The exact master prompt locks the analysis to:

```text
Thesis_Final_Unique_Papers_325_2026-08-20(1).csv
```

Expected SHA-256:

```text
047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f
```

Expected shape:

```text
325 rows x 34 columns
```

The authoritative online archive also stores this `(1)` file under the same hash.

## 3. Archived high-rigor execution copy

The GitHub summary for the archived high-rigor run records the input file name:

```text
Thesis_Final_Unique_Papers_325_2026-08-20(4).csv
```

with **the same SHA-256**:

```text
047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f
```

Therefore `(4)` is recorded as a **byte-identical uploaded copy**, not a different scientific dataset.

Future chats should identify the frozen dataset by **hash first**, and by the prompt's logical file name `(1)` second.

---

## 4. Eligibility/accounting

Under the final four-criterion prompt/high-rigor execution:

- records supplied: 325;
- scientific records ranked: 322;
- protocol/support records excluded from scientific competition: 3;
- duplicate Canonical IDs: 0;
- duplicate normalized DOI: 0;
- duplicate normalized title: 0;
- identity-conflict warnings retained: 1.

A conflicting DOI note is not automatic scientific exclusion; identity confidence is reduced/flagged.

---

## 5. Anti-leakage rule

Historical ranking/selection variables are forbidden scientific predictors, including prior ranks, priority tiers, selection flags, source-presence counts and historical corpus IDs.

These may be used only after the new ranking as descriptive validation.

---

## 6. Final frozen score model

Only four scientific criteria are permitted:

```text
H = hypothesis/target coverage
R = direct/foundational thesis relevance
D = disciplinary fit
T = controlled title-level architecture fit
```

Evidence confidence is separate:

```text
q in (0,1]
```

Criterion uncertainty is represented through Beta distributions with concentration increasing with evidence confidence.

Weight uncertainty is represented through constrained Dirichlet sampling around:

```text
[0.30, 0.30, 0.20, 0.20]
```

with the frozen bounds defined in the master prompt.

Missing scientific criteria are not silently replaced by zero; the scientific score renormalizes over observed criteria.

Confidence-adjusted score:

```text
S = S_raw * (0.70 + 0.30 q)
```

Robust Selection Index:

```text
RSI = [mean_score * P(TopK) * q]^(1/3)
```

Operational target:

```text
K=140
```

---

## 7. Official run parameters

Frozen prompt/high-rigor execution:

- official seed: `20260820`;
- official simulations: 50,000;
- independent stability seeds: `20260821`, `20260822`;
- stability runs per independent seed: 10,000;
- alternative weighted-geometric aggregation used as sensitivity analysis;
- convergence and seed stability required.

---

## 8. Archived HIGH_RIGOR_RUN result

Repository summary: `methods/monte_carlo/final_run_2026-08-20/README.md`.

Reported:

- convergence: PASS;
- seed stability: PASS;
- alternative aggregation Spearman: `0.9918268554240491`;
- robust core (`P(Top140)>=0.90` and `q>=0.70`): 80;
- Rank 1: *Multi-timescale risk-averse restoration for interdependent water-power networks with joint reconfiguration and diverse uncertainties*;
- DOI: `10.1016/j.ress.2025.111083`;
- mean score: `0.954482`;
- RSI: `0.981585`;
- P(Top10): `0.98924`;
- P(Top140): `1.0`;
- evidence confidence `q`: `0.990870`;
- pairwise score-dominance probability over Rank 2: `0.81422`.

Important interpretation:

```text
0.81422 < 0.95
```

so the high-rigor run does **not** establish a 95% dominance claim over Rank 2.

The complete high-rigor ZIP is stored off-repository and indexed through provenance/online archive material; the GitHub final-run directory itself currently contains a summary README rather than every raw output file.

---

## 9. Three-package comparison preserved from the conversation

The current chat later compared three executions using the same locked input hash.

### Model A — `PRISMA_MC_325_EXECUTED_2026-08-20`

- alternative six-criterion model;
- 321 eligible in that implementation because of different conflict handling;
- 100,000 simulations;
- included evidence/primary-corpus corroboration inside the scientific score;
- useful as a stress test, **not compliant with the final four-criterion frozen prompt**;
- ranked the transport sustainability/climate-recovery paper first.

### Model B — `PRISMA_MC_325_FULL_RUN_RESULTS`

- 322 scientific records;
- 50,000 official runs + two 10,000-run seed checks;
- four criteria H/R/D/T with separate `q`;
- robust core: 75;
- alternative aggregation Spearman: about `0.979253`;
- Rank 1: multi-timescale water–power restoration paper;
- Rank 2: sustainability/climate transport-recovery paper;
- pairwise P(score Rank1 > Rank2): about `0.57848`.

The conversation-level audit concluded this implementation was the **closest controlling implementation of the frozen title-architecture formula**, especially because exact title-score examples matched the declared formula.

### Model C — `PRISMA_MC_325_HIGH_RIGOR_RUN_2026-08-20`

- 322 scientific records;
- 50,000 official runs + seed checks;
- robust core: 80;
- alternative aggregation Spearman: about `0.991827`;
- same Rank 1;
- pairwise Rank1 > Rank2: `0.81422`.

The conversation-level audit treated this as a **high-quality sensitivity replication**, not the controlling implementation when its title-feature encoding diverged from the literal frozen title formula for many papers.

## 10. Why Model B and Model C differed

The comparison found:

- Hypothesis_Coverage_Base identical for all 322 papers;
- Relevance_Base identical for all 322;
- Discipline_Fit differed for only a few records;
- Title_Architecture differed for many records;
- evidence-confidence `q` also differed.

Two diagnostic examples preserved from the conversation:

1. *Physics-Informed Neural Networks with Hard Constraints for Inverse Design* — the literal frozen title formula gives `0.775` when one controlled group is detected; Model B produced that exact behavior whereas Model C used a lower title score.
2. *Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery* — the title visibly spans at least four frozen controlled groups, implying title score `1.0`; Model B produced `1.0`, whereas Model C used a lower title score.

Therefore the later comparative interpretation should not be overwritten by the fact that the GitHub `final_run_2026-08-20` folder currently indexes the high-rigor package.

---

## 11. Cross-model robustness preserved from the conversation

Reported intersections across all three models:

```text
Top10  : 4 papers
Top25  : 17 papers
Top50  : 34 papers
Top100 : 68 papers
Top140 : 92 papers
```

Model B vs Model C robust-core comparison:

```text
B robust core: 75
C robust core: 80
intersection: 73
```

The four papers reported as Top-10 in all three models were:

1. *Multi-timescale risk-averse restoration for interdependent water-power networks with joint reconfiguration and diverse uncertainties*;
2. *Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery*;
3. *Novel methodology for resilience assessment of critical infrastructure considering the interdependencies*;
4. *Community resilience-driven restoration model for interdependent infrastructure networks*.

## 12. Strongest scientific interpretation

Do **not** present one universally dominant paper.

The model comparison supports a more conservative interpretation:

```text
two co-dominant primary precedents
+ a stable consensus core
+ model-sensitive ordering near the top
```

The two co-dominant precedents are the multi-timescale water–power restoration paper and the sustainability/climate transport-recovery paper.

## 13. Hypothesis-specific comparison memory

Across the three models, the discussion reported particularly stable winners for H1, H2, H3, H4 and H6, while H5, H7 and T1 were more model-sensitive.

This is useful for prioritizing falsification, but the original model-specific output files remain the authority for exact ranks/probabilities.

## 14. Valid statement boundary

Allowed:

> These results describe robust importance **within the locked 325-record corpus under the declared ranking models**.

Not allowed:

> The Monte Carlo ranking proves global literature completeness, globally best papers, or global novelty of the thesis.

## 15. Repository/provenance pointers

- frozen prompt: `prompts/PRISMA_Monte_Carlo_325_Single_Dataset_Master_Prompt.md`
- high-rigor summary: `methods/monte_carlo/final_run_2026-08-20/README.md`
- online raw archive index: `provenance/ONLINE_ARCHIVE.md`
- project inventory/hashes: `provenance/INVENTORY.csv`, `provenance/SHA256SUMS.txt`

Future work should preserve the raw comparative packages, if not already indexed, before relying on this memory file as the only record of the three-model comparison.