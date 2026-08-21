# Visible User Requests — Verbatim Where Exact Text Is Available

This file preserves the user's visible instructions from the chain-architecture session. It intentionally excludes hidden system/developer instructions, hidden chain-of-thought, connector internals, and text that cannot be reconstructed exactly.

## 1. Frozen-corpus PRISMA + Monte Carlo request

The session began with a long, exact dataset-only PRISMA-compatible Monte Carlo specification beginning:

> You are acting as a **systematic-review methodologist, applied mathematician, uncertainty-quantification researcher, and scientific programmer**.
>
> Your task is to perform a **PRISMA-compatible, mathematically auditable Monte Carlo ranking** of the papers contained in one and only one frozen dataset for the thesis:
>
> **Mathematical Physics of Sustainable Infrastructure Resilience**

The exact master prompt corresponding to this request is already versioned in the repository at:

`prompts/PRISMA_MC_325_MASTER_PROMPT.md`

The request imposed, among other constraints:

- use only `Thesis_Final_Unique_Papers_325_2026-08-20(3).csv`;
- no web or external bibliographic enrichment;
- SHA-256 and 325-row integrity checks;
- exact PRISMA statuses `ELIGIBLE`, `METHODS_ONLY`, `HOLD`, `EXCLUDE`;
- `CONFLICTING_DOI` → HOLD;
- prior ranks forbidden from scoring;
- six criteria on [0,1];
- Beta feature uncertainty;
- four Dirichlet weight scenarios;
- `20 × 5000 = 100000` simulations with seed `20260820`;
- expected rank and complete rank-acceptability probabilities;
- explicit MCSE/Hoeffding/convergence tests;
- a lexicographic robust-winner rule;
- post-ranking validation only after score freeze;
- seven named output files;
- explicit statement that no external data were used and prior ranks were excluded from scoring.

## 2. ZIP request

> put all file in zip and give

## 3. Cross-run comparison

> compare the insights of those

The user supplied three run packages for comparison:

- `PRISMA_MC_325_EXECUTED_2026-08-20(3).zip`
- `PRISMA_MC_325_FULL_RUN_RESULTS(3).zip`
- `PRISMA_MC_325_HIGH_RIGOR_RUN_2026-08-20(3).zip`

## 4. Thesis role in the research chain

> what is the role of my thesis in this ?

The user then supplied an eight-position research chain centered on:

`Foundations → Representation → Dynamics → Resilience → Control → Design → Optimization → Decision/Policy`

and asked where the thesis belongs within it.

## 5. Thesis alternative at each chain position

> for and step of chain what will be the proposed alternative of my thesis

## 6. Three complete thesis types

> what will 3 types of thesis which will do every step of the chain?

This request was asked twice in the visible session and should be treated as deliberate emphasis rather than deduplicated away.

## 7. Framework construction

> design the framework of each Type I , II, and III

## 8. Framework image generation

> design the image of each framework

## 9. Separate mathematically designed images

> each type should have it own image well design and strucuture using mathematics arts to design it

## 10. Publish generated images to GitHub

> Put all genrated image in the github

The resulting framework images are versioned in:

`figures/thesis_framework_types/`

## 11. Deep understanding of chains and layers

> I want firt to deeper understant the  chains and it layers

## 12. Literature-ground every statement

> use the litterature review in each informations and give in text , formulas citations of each already existanting

This request established the evidence discipline used later in the session: distinguish existing literature mathematics from canonical forms and thesis-proposed synthesis.

## 13. Current archive request

> take time and put all those information in a githbut folder : all information everything which will help to have the whole memories of this chat with high rigor of recall and reproducibility for others futures chats

## Attachment-only source turns

Two major user-provided architecture documents appeared as attachment-only turns in the visible session and are treated as source material rather than silently rewritten user requests:

- `Pasted markdown(20260820-081500).md` — final literature-grounded six-chain wording architecture.
- `Pasted markdown(20260820-083013).md` — mathematical-depth ranking, well-posedness hierarchy, and proposed Chain I + II + IV theorem-quality research program.

Future chats should use the archived source snapshots and not invent missing wording.