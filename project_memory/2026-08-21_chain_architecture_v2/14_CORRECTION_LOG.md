# Correction Log — v1 → v2

This file records the substantive corrections found during the second audit. The v1 capsule is preserved for provenance and should not be treated as the current canonical memory.

## C1 — Demonstrator wording

### v1 problem
The demonstrator was repeatedly summarized as only “urban flooding with drainage–waste feedback” or equivalent.

### Authoritative repository state
`project/THESIS_SCOPE.md` says:

**urban flooding with waste–drainage–transport feedbacks**.

### v2 correction
Use the full scope wording. Keep P6 narrower where appropriate because the formal P6 proposition specifically targets the waste–drainage–flood feedback.

---

## C2 — Core thesis architecture versus broader research program

### v1 problem
Some memory files extended the canonical chain through design/optimization/decision as though all stages were equally part of the core MSE contribution.

### Authoritative repository state
`project/THESIS_SCOPE.md` centers the core mathematical contribution on:

```text
dynamic coupling → admissibility → viability → recovery
```

with identification/UQ upstream and control/design as extensions.

### v2 correction
Store two separate chains:

```text
CORE MSE:
D_obs → identification/UQ → F_dyn → K_R → V_R → C_R → U_recovery
```

and:

```text
BROADER PROGRAM:
... → control → design → optimize → decide → implement/learn
```

---

## C3 — P1–P7 versus H0–H7/T1

### v1 problem
The memory used constructions such as “P1/H0” and “P2/H1” too casually, implying one formal naming system.

### Authoritative repository state
Current formal registry is P1–P7. Earlier review/ranking work uses H1–H7/T1, with an earlier project H0 as well.

### v2 correction
Create an explicit crosswalk. H3 and H7 are retained as separate/legacy targets because they do not have exact P1–P7 equivalents.

---

## C4 — Frozen dataset file name

### v1 problem
The memory presented only the `(1)` file name even when discussing the archived high-rigor execution.

### Authoritative repository state
The frozen prompt uses:

`Thesis_Final_Unique_Papers_325_2026-08-20(1).csv`

The archived high-rigor run README records:

`Thesis_Final_Unique_Papers_325_2026-08-20(4).csv`

with the **same SHA-256**:

`047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f`.

### v2 correction
Use hash identity as controlling. `(4)` is a byte-identical execution copy, not a different scientific corpus.

---

## C5 — High-rigor run versus controlling comparative implementation

### v1 problem
The existence of `methods/monte_carlo/final_run_2026-08-20/README.md` could make a future chat assume the HIGH_RIGOR_RUN is automatically the controlling implementation.

### Current conversation comparison
A later three-package audit found that `FULL_RUN_RESULTS` matched the literal frozen title-architecture formula more closely on diagnostic examples, while `HIGH_RIGOR_RUN` remained a strong sensitivity replication.

### v2 correction
Preserve both facts:

- GitHub final-run summary indexes the HIGH_RIGOR_RUN archive;
- conversation-level method audit treats FULL_RUN_RESULTS as closest controlling implementation of the frozen title formula.

---

## C6 — Robust-core interpretation

### v1 problem
A single robust-core number could be mistaken for model-invariant truth.

### Current comparison
- FULL_RUN_RESULTS robust core: 75;
- HIGH_RIGOR_RUN robust core: 80;
- intersection: 73.

### v2 correction
Preserve model-specific sizes and the stable intersection rather than one universal core count.

---

## C7 — Rank-1 certainty

### v1 risk
The high-rigor Rank-1 paper could be read as an uncontested universal winner.

### Current comparison
- HIGH_RIGOR_RUN pairwise Rank1>Rank2: 0.81422;
- FULL_RUN_RESULTS pairwise Rank1>Rank2: about 0.57848;
- the alternative six-criterion model reversed the top-two ordering.

### v2 correction
Interpret the top of the corpus as **two co-dominant primary precedents plus a stable consensus core**, not one universally dominant paper.

---

## C8 — GitHub final-run contents

### v1 problem
The implementation map could be read as if the complete final-run output bundle was committed in `methods/monte_carlo/final_run_2026-08-20/`.

### Repository audit
That directory currently contains a summary `README.md`; the complete high-rigor ZIP is preserved externally and referenced by the README/provenance system.

### v2 correction
State explicitly whether raw bytes are GitHub-committed or only indexed from GitHub.

---

## C9 — “Verbatim” coverage

### v1 problem
The initial current-segment request file mixed directly visible current turns with earlier request lines without enough provenance separation.

### v2 correction
Separate:

- directly visible current-segment requests;
- older requests preserved in `conversation/`;
- long user-pasted source/reference text;
- reconstructed assistant summaries.

---

## C10 — Compact six-chain wording versus expanded decomposition

### v1 problem
The expanded layers could appear to replace the compact six-chain framework discussed with the user.

### v2 correction
Preserve both the canonical compact chain and its expanded internal layer decomposition with an explicit parent-child relationship.

---

## C11 — Retracted intermediate audit impression about `\nu`

### Intermediate audit impression
During the v2 audit, connector-serialized text such as a JSON newline escape followed by `u` visually resembled `\nu`, which was initially interpreted as a literal LaTeX Greek-nu control variable.

### Recheck
A repository search did not support the claim that literal `\nu` / `\nu_t` control-variable notation was present as a source-file error. The apparent issue was a serialization/display ambiguity, not a verified scientific-document typo.

### v2 correction
**The earlier `\nu`/`\nu_t` typo claim is retracted.** Do not propagate it as a repository defect.

---

## C12 — Root README demonstrator wording

### Repository audit
The earlier root README used a shorter drainage/waste description and mentioned transportation separately.

### v2 correction
The root README was aligned with the authoritative scope phrase:

**urban flooding with waste–drainage–transport feedbacks**.

---

## C13 — Viability horizon

### Risk
A memory summary could silently generalize the current `forall t>=0` definition into a finite-horizon statement.

### v2 correction
Record the authoritative current infinite-horizon definition, while allowing a later finite-horizon/time-varying amendment only if explicitly documented.

---

## C14 — Literature identity conflict

### v1 risk
The DOI for *A Survey of Viability Theory* could be propagated despite an existing identity conflict.

### v2 correction
Do not store one DOI as verified. Record the `0328044` vs `0328045` conflict and require direct bibliographic verification.

---

## C15 — Digital twin terminology

### v1 risk
Type II could make a future chat describe the existing code scaffold as a digital twin.

### v2 correction
Digital twin remains a thesis **alternative/direction** unless an actual observation-update-calibration-validation loop is implemented.

---

## C16 — Provenance authority

### v1 weakness
Memory and source authority were not ordered strongly enough.

### v2 correction
Use:

```text
authoritative source artifact
> exact transcript/source text
> verified bibliographic/full-text evidence
> corrected v2 memory
> reconstructed summary
> v1 memory
> unaudited recollection
```

---

## C17 — Stale root `data/` tree entry

### Repository audit
The earlier root README displayed a top-level `data/` directory in the repository tree, but the audited GitHub root did not contain that directory.

### v2 correction
The README tree was changed to reflect the actual repository structure and to direct raw-dataset/binary provenance to `provenance/ONLINE_ARCHIVE.md`, `provenance/INVENTORY.csv`, and the actual GitHub tree.

---

## C18 — Concurrent unrelated repository activity

During the audit, another commit added material under `evidence/engineering_sustainability_integration_review/`. That concurrent repository activity is not automatically part of this chain-architecture memory capsule.

### v2 rule
Future chats must not infer that every new repository file belongs to the current thesis subproblem simply because it appears on `main`; route material by scientific relevance and source provenance.

---

# Result

The v1 capsule remains useful as a historical record of the first memory attempt. For any future continuation, use the v2 capsule unless a newer documented amendment supersedes it.