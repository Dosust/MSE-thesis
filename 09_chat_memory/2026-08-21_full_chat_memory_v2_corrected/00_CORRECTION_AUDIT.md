# V2 Correction Audit — Superseding the First Chat-Memory Capsule

**Audit timestamp:** 2026-08-21T22:22:00+08:00  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Publication branch:** `archive-import`  
**V1 status:** retained as historical provenance; **do not delete**.  
**V2 status:** corrected recall source for future chats.

## Confirmed errors / weaknesses corrected

1. **Incomplete online publication was overstated.** V1 was described as if the full rich capsule were online, but the verified GitHub folder exposed only 8 top-level memory files while the local capsule contained 17 structured files. V2 publishes the complete corrected set and a manifest.
2. **“Scientific freeze” wording was too strong.** The conceptual architecture may be provisionally frozen, but the PRISMA novelty-falsification package explicitly says `BLOCKED_PENDING_DATABASE_EXPORTS`. V2 therefore distinguishes `WORKING_ARCHITECTURE_FREEZE` from `NOVELTY_FREEZE = NOT_YET_ALLOWED`.
3. **207-corpus role was ambiguous.** The 207 corpus is retained as an important literature-anchor source for the six-chain explanation; it is **not** the current authoritative ranking dataset. The locked 325-record corpus is the ranking dataset for the later Monte Carlo work.
4. **`A Survey of Viability Theory` DOI conflict.** Raw 207 metadata contains `10.1137/0328045`. SIAM identifies the article as `10.1137/0328044`; the 325 corpus also uses `10.1137/0328044` and flags `CONFLICTING_DOI`. V2 preserves the raw source value but uses the verified DOI only in the corrected bibliography.
5. **Multilayer-network identities were conflated.** Kivelä et al. = *Multilayer networks* (`10.1093/comnet/cnu016`); Boccaletti et al. = *The structure and dynamics of multilayer networks* (`10.1016/j.physrep.2014.07.001`); De Domenico et al. = *Mathematical Formulation of Multilayer Networks* (`10.1103/PhysRevX.3.041022`). V2 keeps them separate.
6. **Equity-paper title variants were not clearly reconciled.** V2 uses the 325 canonical title for the 2020 Coleman–Esmalian–Mostafavi article and preserves the 207 variants as raw-source variants rather than silently merging them.
7. **Notation collision: `M`.** V1 used `M` both for interface states and a possible mass/DAE matrix. V2 uses lowercase `m(t)` for dynamic interfaces and `\mathsf M(X)` only for a mass/DAE matrix.
8. **Notation collision: coupling vs capture.** V2 uses `\Gamma` for cross-sector coupling and reserves `\mathcal C` for capture/recoverability sets.
9. **Service mapping was not consistently placed before admissibility.** V2 explicitly uses `Y=\pi(X,Z,m)` and defines service/equity constraints through that mapping before viability is computed.
10. **Admissible-set dimensionality was underspecified.** V2 defines the admissible set on the physical/hybrid state with service constraints pulled back through `\pi`, instead of intersecting sets living in incompatible spaces without explanation.
11. **Viability quantifiers were incomplete under uncertainty.** V2 distinguishes nominal, robust/adversarial, and stochastic viability rather than writing a single `\exists u` definition for every case.
12. **Hausdorff sensitivity was written as if the derivative must exist.** V2 states compactness/non-emptiness requirements and uses a `limsup` sensitivity unless differentiability of the set map is proven.
13. **Projection/timescale notation could collide.** V2 uses `\mathsf P` for state-space projection and `\Pi_{\rm int}` for the interface/system timescale ratio. `\Pi_M` is retained only as a legacy alias.
14. **Monte Carlo protocols were conflated.** V2 separates: (A) the earlier 10-criterion code bundle with an expected 321 eligible records and planned 1,000,000 total draws; (B) the later four-criterion closed-corpus FULL run with 322 ranked records and 50,000 official draws; and (C) the six-criterion EXECUTED sensitivity run with 321 ranked records. They are not interchangeable.
15. **A single universal Rank-1 paper was overstated.** Across the three models the scientifically defensible result is a robust Top-2 cluster: the multi-timescale water–power restoration paper and the sustainability/climate-resilience transport-recovery paper. Exact #1 is model-sensitive.
16. **Framework-image provenance needed an error record.** Initial WebP GitHub objects were Base64 text and did not render. The files were later replaced with valid binary WebP blobs; V2 records both the failure and repair commit.
17. **Filename case mismatch.** V1 instructions referred to `state.json` although the actual file was `STATE.json`. V2 standardizes on `STATE.json`.
18. **Transcript completeness was overstated.** V2 separates `VERBATIM_VISIBLE_TEXT`, `VISIBLE_RESPONSE_ARCHIVE`, `RESEARCH_STATE_SUMMARY`, and `UNAVAILABLE_RAW_TEXT`. No reconstructed wording is labeled forensic/verbatim.

## Audit invariant

A future chat must not collapse:

`raw corpus metadata != verified bibliography != literature claim != thesis integrating notation != candidate novelty`.
