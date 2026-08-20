# Final High-Rigor Closed-Corpus PRISMA + Monte Carlo Run

Run date: 2026-08-20

## Frozen input

- Dataset: `Thesis_Final_Unique_Papers_325_2026-08-20(4).csv`
- Input SHA-256: `047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f`
- Records supplied: **325**
- Scientific records ranked: **322**
- Protocol/support records excluded from scientific competition: **3**
- Duplicate Canonical IDs: **0**
- Duplicate normalized DOIs: **0**
- Duplicate normalized titles: **0**
- Identity-conflict warnings retained: **1**

The byte identity matches the frozen 325-paper dataset even though this uploaded copy has the suffix `(4)`.

## Monte Carlo execution

- Official runs: **50,000**
- Official seed: `20260820`
- Operational K: **140**
- Independent stability seeds: `20260821`, `20260822`
- Stability runs per independent seed: **10,000**
- Protocol/config SHA-256: `4845ff4e6b348c6272d472cf8de0334c71de6e3e276431ebf5c96cfc80e9e847`

## QA

- Convergence: **PASS**
- Seed stability: **PASS**
- Max MCSE among leading candidates: `0.0001259138953173533`
- Max half-run mean-score difference among leading candidates: `0.00039458274841308594`
- Max half-run Top-140 probability difference among leading candidates: `0.0040000000000000036`
- Half-run whole-ranking Spearman: `0.9999324266159341`
- Alternative weighted-geometric rank Spearman: `0.9918268554240491`
- Robust core size (`P(Top140)>=0.90` and `q>=0.70`): **80**

Independent-seed stability:

| Seed | Runs | Top-140 Jaccard | Full-rank Spearman | Pass |
|---:|---:|---:|---:|---|
| 20260821 | 10,000 | 1.000000 | 0.999782 | PASS |
| 20260822 | 10,000 | 0.985816 | 0.999530 | PASS |

A second execution with the same official seed and 50,000 primary runs reproduced the primary ranking and deterministic audit outputs byte-for-byte.

## Rank 1 within the locked corpus

**Multi-timescale risk-averse restoration for interdependent water-power networks with joint reconfiguration and diverse uncertainties**

- DOI: `10.1016/j.ress.2025.111083`
- Mean score: `0.954482`
- RSI: `0.981585`
- P(Top 10): `0.98924`
- P(Top 140): `1.00000`
- Evidence confidence q: `0.990870`
- Pairwise score-dominance probability over Rank 2: `0.81422`

The final rank is robust under the frozen model, but the Rank-1 versus Rank-2 pairwise ordering is **not** a 95% dominance claim.

## Best paper by hypothesis / target

- **H1:** *Resilience performance analysis of interdependent infrastructures using Fault Tree and Dynamic Bayesian Network* — DOI `10.1016/j.ress.2026.112541`
- **H2:** *Multi-timescale risk-averse restoration for interdependent water-power networks with joint reconfiguration and diverse uncertainties* — DOI `10.1016/j.ress.2025.111083`
- **H3:** *Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery* — DOI `10.1016/j.trd.2023.103800`
- **H4:** *Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery* — DOI `10.1016/j.trd.2023.103800`
- **H5:** *Multi-timescale risk-averse restoration for interdependent water-power networks with joint reconfiguration and diverse uncertainties* — DOI `10.1016/j.ress.2025.111083`
- **H6:** *Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery* — DOI `10.1016/j.trd.2023.103800`
- **H7:** *Resilience assessment framework for critical infrastructure in a multi-hazard environment: Case study on transport assets* — DOI `10.1016/j.scitotenv.2020.136854`
- **T1:** *Community resilience-driven restoration model for interdependent infrastructure networks* — DOI `10.1016/j.ijdrr.2019.101228`

## Complete run archive

The full output bundle is preserved online in Google Drive:

`https://drive.google.com/file/d/1MjNXjvEO4SAwP6bXe2nd7ObRAV2HdT5g/view?usp=drivesdk`

File: `PRISMA_MC_325_HIGH_RIGOR_RUN_2026-08-20.zip`

SHA-256: `ea43cc2bc02eeac0073af353e4da236e7d7e10a1240addcbce1364020a9e139d`

The ZIP contains the complete scientific ranking, operational Top-140, robust core, H1–H7/T1 rankings, feature matrix, Top-25 pairwise dominance, weight sensitivity, independent-seed stability, criterion correlations, historical-rank validation, closed-corpus PRISMA accounting, protocol-support records, run manifest, final Markdown summary, and SHA-256 registry.

## Scientific interpretation boundary

The valid conclusion is:

> These are the most robustly ranked papers **within the locked 325-record corpus under the frozen PRISMA-style Monte Carlo model**.

The run does not prove that the Rank-1 paper is universally the best paper in the global literature.