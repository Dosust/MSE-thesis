# Reproducibility Checklist for Future Thesis Chats

A future chat should use this checklist before declaring that it has correctly recovered or reproduced the thesis state.

## A. Scope recovery

- [ ] Read `project/THESIS_SCOPE.md`.
- [ ] Confirm working title and precise formulation.
- [ ] Confirm sectors are P–W/Drainage–T–SW.
- [ ] Confirm demonstrator is urban flooding with waste–drainage–transport feedbacks.
- [ ] Confirm `∂V_R` is the central geometric object.
- [ ] Confirm core contribution is dynamic coupling → admissibility → viability → recovery.
- [ ] Do not promote downstream design/decision extensions to equal core novelty without an explicit scope amendment.

## B. Mathematical-state recovery

- [ ] Read `project/MATHEMATICAL_FOUNDATION.md`.
- [ ] Preserve `X`, `Z`, `m`, `u`, `xi`, `eta`, `theta`, `Y` meanings.
- [ ] Preserve `xi → eta` distinction.
- [ ] Preserve `K_R=K_phys ∩ K_service ∩ K_sus ∩ K_eq`.
- [ ] Preserve distinction among `V_R`, `C_R`, and `tau_R`.
- [ ] Preserve current infinite-horizon viability definition unless a documented amendment changes it.
- [ ] Do not treat `d_H` as the only permissible deformation diagnostic without justification.

## C. Proposition recovery

- [ ] Read `project/SCIENTIFIC_PROPOSITIONS.md`.
- [ ] Confirm current formal IDs are P1–P7.
- [ ] Read `03_HYPOTHESIS_PROPOSITION_CROSSWALK.md` before referring to H0–H7/T1.
- [ ] Do not silently map H3 or H7 to a current P proposition.
- [ ] Treat propositions as testable/falsifiable, not already established facts.

## D. Six-chain recovery

- [ ] Preserve the compact six-chain wording.
- [ ] Use expanded layers as decomposition, not replacement.
- [ ] Route new tasks to one or more chains before choosing methods.
- [ ] Keep cross-cutting tools (optimization, UQ, ML, numerical analysis, Bayesian methods) separate from physical lifecycle layers.

## E. Literature recovery

- [ ] Use `05_LITERATURE_EVIDENCE_MAP.md` only as a routing memory.
- [ ] Return to authoritative corpus/full text for final citation.
- [ ] Verify title/authors/year/venue/DOI.
- [ ] Verify exact proposition/equation supported.
- [ ] Preserve identity-conflict flags, especially the viability-survey DOI conflict.
- [ ] Do not convert a candidate gap into novelty without direct falsification search.

## F. Closed-corpus Monte Carlo recovery

- [ ] Read the frozen master prompt.
- [ ] Confirm logical input `(1)` and SHA-256.
- [ ] Confirm 325 × 34 expectation.
- [ ] Preserve 322 scientific / 3 protocol-support accounting for the final four-criterion implementation.
- [ ] Preserve four scientific criteria H/R/D/T and separate evidence confidence `q`.
- [ ] Preserve anti-leakage rules.
- [ ] Keep `(4)` as a byte-identical execution copy, not a second corpus.
- [ ] Distinguish FULL_RUN_RESULTS, HIGH_RIGOR_RUN and EXECUTED models.
- [ ] Do not average raw scores across incompatible models.
- [ ] State results only within the locked 325-record corpus.

## G. Code/model recovery

- [ ] Inspect `methods/architecture/` before describing implemented capability.
- [ ] Treat current Python/Julia architecture code as synthetic/reference QA unless later calibration is documented.
- [ ] Distinguish software-test success from scientific validation.
- [ ] Re-run tests/workflows when scientific definitions or code change.
- [ ] If using a reduced model, require a viability/recovery preservation or conservative-bounding test.

## H. Figure recovery

- [ ] Check `assets/math-art/` and `assets/frameworks/`.
- [ ] Use generated images as conceptual/model architecture, not empirical evidence.
- [ ] Preserve checksums where supplied.
- [ ] Prefer state-space/operator/sensitivity/reachability visuals for future scientific figures.

## I. Transcript/authenticity recovery

- [ ] Read `conversation/AUTHENTICITY_LIMITS.md`.
- [ ] Search exact conversation files before reconstructing wording.
- [ ] Distinguish directly visible verbatim, archived verbatim, user-supplied reference text and reconstructed assistant summaries.
- [ ] Never archive hidden chain-of-thought/system instructions/secrets as project transcript.

## J. Artifact provenance

- [ ] Check the actual GitHub tree before saying a file is committed.
- [ ] Check `provenance/ONLINE_ARCHIVE.md` for raw external artifacts.
- [ ] Check `provenance/INVENTORY.csv` and hashes for identity.
- [ ] Distinguish “indexed in GitHub” from “raw bytes committed in GitHub.”
- [ ] Do not automatically incorporate concurrent unrelated repository material.

## K. Change control

- [ ] If changing title, sectors, demonstrator, proposition, model, dataset lock or score protocol, create a dated amendment.
- [ ] Preserve the old version.
- [ ] Identify dependent figures/code/results.
- [ ] Re-run affected analysis.
- [ ] Do not retroactively describe old results as if they used the new protocol.

## L. Current scientific next step

Unless redirected by the user:

- [ ] Decompose Chain I sector-by-sector.
- [ ] Establish equations, state variables and units for Power.
- [ ] Establish equations, state variables and units for Water/Drainage.
- [ ] Establish equations, state variables and units for Transportation.
- [ ] Establish equations, state variables and units for Solid Waste.
- [ ] Define cross-sector interdependencies.
- [ ] Define actual interface mechanisms.
- [ ] Define dynamic interface states/laws.
- [ ] Derive characteristic timescales.
- [ ] Specify failure/recovery modes.
- [ ] Test well-posedness, stability, sensitivity and identifiability assumptions.
- [ ] Only then freeze the coupled forward model.

## Completion criterion

A future chat has recovered the project correctly only if it can explain not just **what the thesis says**, but also:

```text
what is authoritative
what is historical
what is proposed
what is corpus-derived
what is synthetic
what is validated
what remains pending
```

That distinction is essential to reproducibility.