# Configuration Contracts

This directory contains machine-readable configuration aligned with the frozen seven-stage P–T–I–O thesis framework.

| File | Purpose | Authority |
|---|---|---|
| `scientific_propositions.yaml` | P1–P10 supporting proposition registry | synchronized with `project/SCIENTIFIC_PROPOSITIONS.md` |
| `research_hypotheses.yaml` | H1–H5 primary hypothesis registry | synchronized with `project/RESEARCH_HYPOTHESES.md` |
| `example_model.json` | valid illustrative P–T–I–O model configuration | validated against `schemas/thesis_model.schema.json` |

These files are contracts for software/reproducibility. They do not replace the human-readable canonical stage specifications.

## Synchronization rules

- $P,T$ remain physical systems; $I,O$ remain informational/organizational layers.
- Primary hypothesis logic $H_1$–$H_5$ is frozen; numerical thresholds are not yet frozen.
- The proposition registry contains $P_1$–$P_{10}$ as subordinate falsifiable claims.
- Stage-4 operational control uses $u(t)$.
- Stage-7 strategic transformation uses $\mathbf a_k$ and regime $\mathfrak M_k$.
- Historical P–W–T–SW/waste–drainage configuration must not reappear in active contracts.

The GitHub scientific-architecture workflow validates these invariants automatically.
