# Correction Ledger — Verified Memory State (2026-08-21)

This file records corrections made after re-checking the existing conversation-memory archive against: (i) the frozen MSE research design v0.5, (ii) the current ChatGPT conversation file surface, (iii) the live Figma file, (iv) the Duke 2002 mathematical-sciences education taxonomy supplied by the user, and (v) the official current MSC2020 classification sources.

## Status convention

- **CORRECTED** = prior archive statement was wrong or too broad and is superseded here.
- **CLARIFIED** = prior statement was partially right but conflated distinct scopes or semantic roles.
- **RETAINED** = prior statement remains valid.
- **UNVERIFIED** = preserved as historical context but must not be used as a thesis fact without re-verification.

## C1 — Executable sector scope

**CORRECTED.** The MSE executable demonstrator is **Power–Transport–Water (P–T–W)**. Solid Waste is **not** part of the frozen executable MSE core. It is retained as an extension interface in the general architecture.

Frozen core state:

\[
X(t)=[X_P(t),X_T(t),X_W(t)]^T.
\]

General extensible state:

\[
X_{ext}(t)=[X_P(t),X_T(t),X_W(t),X_{SW}(t),\ldots]^T.
\]

Therefore any archive wording that says the primary thesis system is a fully executable P–W–T–SW model is superseded.

## C2 — Frozen thesis contribution

**CORRECTED/CLARIFIED.** The frozen contribution is not simply "dynamic interface identification → viability uncertainty." That remains a strong candidate research bridge, but the controlling MSE design v0.5 freezes a broader formal contribution:

> distinguish **safe recovery reachability** from **post-recovery controlled viability** in dynamically coupled urban infrastructure, with an evolving acceptable recovery region constrained by critical service, sustainability, equity, interfaces, institutions, finance/resources, and hazard conditions.

The four primary formal objects are:

\[
K_{hard}(t),\qquad K_R(t),\qquad K_R^V(t)=\operatorname{Viab}(K_R)(t),\qquad B_R(t_0)=\operatorname{Capt}_{K_{hard}}(K_R^V)(t_0).
\]

Do not collapse these objects into one generic "resilience set."

## C3 — Main research question

**CORRECTED.** The frozen research question is centered on a dynamically coupled **P–T–W** system:

Which disturbed states can be controlled back into an evolving acceptable service region without violating hard constraints, and which recovered states can then remain viable under continued climate disturbance and uncertainty?

## C4 — Recovery and viability semantics

**RETAINED, strengthened.**

- `K_hard(t)` = constraints that may not be violated during recovery.
- `K_R(t)` = time-dependent acceptable recovery region.
- `K_R^V(t)` = states inside `K_R` from which continued admissibility can be maintained under admissible controls/disturbances.
- `B_R(t0)` = states from which the viable target can be reached while respecting hard constraints.

Hence:

\[
\boxed{\text{Recovery reachability} \neq \text{viability}.}
\]

## C5 — Figma state

**CORRECTED.** The archive previously claimed that the active Figma page was `Candidate 1 — Wolfram Fidelity Rebuild v2` and referenced frame node `4:3`. Live inspection of the linked Figma file on 2026-08-21 found only the top-level page:

- Page `0:1`: **Candidate 1 — Sustainable Viability**
- Primary poster frame `1:2`: **Poster — Candidate 1**

Therefore the previous page/frame names must not be treated as current Figma truth.

## C6 — Exact-text archive completeness

**CORRECTED.** The original manifest declared an 8-part exact text archive. Direct GitHub checks found missing pieces (including at least parts 03, 06 and 07). That archive is therefore **incomplete and not reconstructible as declared**.

A later `exact_text_archive_v2` attempt was started but is also incomplete. Neither archive should be cited as a verified byte-complete transcript bundle.

The correct recovery strategy is:
1. preserve current-conversation source files individually where possible;
2. preserve exact file IDs, sizes and hashes when available;
3. preserve reconstructed conversation state in a separate, explicitly non-verbatim ledger;
4. never represent unavailable transcript turns or hidden model reasoning as verbatim provenance.

## C7 — Current conversation file count

**CORRECTED.** The earlier inventory listed a `Pasted markdown(20260821-114450).md` item that is not present on the current conversation file surface. The verified current conversation surface contains six uploaded pasted-Markdown files relevant to this research session, not seven:

1. `Pasted markdown(20260820-080913).md`
2. `Pasted markdown(20260820-081300).md`
3. `Pasted markdown(20260820-081900).md`
4. `Pasted markdown(20260820-083550).md`
5. `Pasted markdown(20260821-100132).md`
6. `Pasted markdown(20260821-104549).md`

The 081900 and 083550 files were previously observed as byte-identical and both names should be retained for provenance if that hash comparison is reused.

## C8 — Mathematical taxonomy: Duke 2002 versus MSC2020

**CORRECTED.** The user-supplied Duke page is a **2002 "Core Subject Taxonomy for Mathematical Sciences Education" final draft** created to support browse/catalog mappings across educational digital libraries. It is not MSC2000/MSC2020 and should not be used as the canonical research-literature classification.

Its top-level educational categories are:
1. Elementary Mathematics
2. Logic and Foundations
3. Algebra and Number Theory
4. Discrete Mathematics
5. Geometry
6. Calculus
7. Analysis
8. Differential and Difference Equations
9. Statistics and Probability
10. Applied Mathematics
11. Mathematics History

Use this taxonomy for **human-facing educational navigation** only.

For scholarly research classification, use **MSC2020**, maintained jointly by Mathematical Reviews and zbMATH. MSC2020 is the canonical research taxonomy layer. It must not be interpreted as a prerequisite/dependency graph.

## C9 — Taxonomy is not ontology and is not a theorem graph

**CLARIFIED.**

The project now distinguishes four semantic layers:

1. **Educational browse taxonomy** — Duke 2002, optional human-navigation layer.
2. **Research subject classification** — MSC2020, canonical scholarly indexing layer.
3. **Knowledge ontology** — SKOS/OWL/RDF typed entities and relations.
4. **Formal mathematical dependency** — definitions, assumptions, lemmas, theorems and proof objects represented through formal-mathematics systems such as OMDoc/MMT and theorem provers.

A tree edge in Duke or MSC therefore does **not** mean "mathematically required before," "causes," or "proves."

## C10 — Six-chain ontology

**RETAINED.** The six chains remain distinct analytical logics linked by explicit feedback, not one causal pipeline:

I. Physical-System
II. Observation–Inference–Prediction
III. Hazard–Failure–Consequence
IV. Resilience–Viability–Recovery
V. Engineering Design–Operation–Adaptation
VI. Sustainability–Equity–Governance–Decision

Cross-cutting mathematics, optimization, UQ, computation and AI are methods that can act across multiple chains.

## C11 — AI/digital twin positioning

**CORRECTED/strengthened.** The MSE thesis is not an operational digital twin and is not an AI forecasting thesis. Earth-observation, physics-informed ML, neural operators and digital-twin systems belong upstream or computationally as observation, state-estimation, scenario-generation or surrogate technologies, subject to conservation, OOD, tail/failure-region and verification gates.

## C12 — Claim discipline

**RETAINED and made binding for future chats.** Avoid:
- first-ever claims without systematic falsification;
- claiming a complete operational P–T–W–SW validation;
- treating physics-informed learning as proof of physical correctness;
- treating average prediction error as adequate when decisions depend on thresholds/failure regions;
- claiming HJ reachability automatically solves the full high-dimensional infrastructure problem.

## Supersession rule

When this ledger conflicts with older files in this conversation-memory folder, this correction ledger and `THESIS_FROZEN_STATE_v0.5.md` take precedence unless a later user-approved research freeze explicitly supersedes them.
