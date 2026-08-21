# Provenance and Authenticity Rules

## 1. Purpose

This file defines what future chats may safely treat as exact, reconstructed, derived, or provisional.

## 2. Authenticity classes

### A. Verbatim user text

Only text known exactly from the visible conversation is labeled verbatim. See `USER_REQUESTS_VERBATIM.md`.

### B. User-provided source material

Attachment-only markdowns supplied by the user are treated as source documents. Their terminology and internal structure should be preserved when used as evidence.

### C. Assistant-generated scientific synthesis

Files such as `SIX_CHAIN_MASTER_ARCHITECTURE.md`, `TYPE_I_II_III_THESIS_FRAMEWORKS.md`, and `LITERATURE_GROUNDED_MATHEMATICS.md` are structured reconstructions/syntheses of the visible session. They are not claimed to be verbatim transcripts.

### D. Computational outputs

Monte Carlo rankings, probabilities, convergence statistics, hashes, and audit results should be verified against their original CSV/JSON/code artifacts before publication use. Narrative memory files are secondary documentation.

### E. Working thesis-proposed mathematics

Objects such as dynamic interface states `Z_ij(t)`, service mapping `Y = pi(X,Z,m)`, and a sustainability/equity admissible set `K_SE` are working synthesis objects unless a specific cited paper is shown to use the same formulation.

## 3. Content intentionally excluded

This archive does not include:

- hidden chain-of-thought;
- system/developer instructions;
- credentials/secrets;
- private connector tokens or ephemeral download URLs;
- inaccessible internal metadata;
- invented historical wording.

These exclusions are deliberate and do not reduce the scientific reproducibility of the project.

## 4. Literature citation discipline

Future chats must not convert a conceptual framework into a fake equation.

Examples:

- Rinaldi interdependency categories are a taxonomy, not a universal scalar equation.
- Kivelä/Boccaletti support multilayer-network mathematics, but a particular P–W–T–SW supra-adjacency matrix is a problem-specific instantiation.
- Buldyrev/Parshani/Gao establish interdependent-network cascade/percolation theory, but do not by themselves establish a dynamic P–W–T–SW interface-state law.
- Saint-Pierre/Aubin establish viability mathematics, but `K_SE` is a thesis-specific admissible set unless directly sourced otherwise.
- Mitchell/Bayen/Tomlin establish HJ/HJI reachability mathematics, but do not automatically prove that a high-dimensional infrastructure model is tractable.
- Coleman et al. provide equity taxonomy/evidence; a hard equity constraint function is a later mathematical formalization unless directly sourced.

## 5. Equation provenance labels

Use these labels in notes/reports:

- `SOURCE_EXACT` — exact equation/result from source, with page/equation number when possible.
- `CANONICAL_FORM` — standard mathematical form used to explain a method/theory.
- `THESIS_SPECIALIZATION` — standard theory specialized to the thesis variables/sectors.
- `THESIS_PROPOSAL` — new working formulation requiring derivation/validation.

Do not publish `THESIS_PROPOSAL` as an established literature equation.

## 6. Monte Carlo provenance

The session discussed multiple ranking implementations sharing the same frozen corpus but not the same scoring model.

Always specify:

- input filename and SHA-256;
- exact code/config version;
- scoring criteria;
- feature-uncertainty model;
- weight model;
- number of simulations;
- seed;
- PRISMA gating rules;
- convergence criteria;
- winner rule;
- output hash/manifest where available.

Do not merge the 100k six-criterion and 50k earlier-model rankings into one “replicated” result without explaining the model change.

## 7. File-location discipline

A filename mentioned in chat is not proof that a file exists on the current GitHub branch.

Before telling the user that a file is in GitHub:

1. read repository state;
2. verify exact branch/path;
3. use GitHub readback after writes;
4. record commit/PR information.

Binary artifacts stored outside GitHub should be indexed with a stable provenance pointer and hash rather than being represented by a fake text placeholder.

## 8. Architecture-version discipline

The repository contains architecture work from multiple stages. Future chats should distinguish:

- historical architecture variants;
- current six-chain ontology;
- Type I/II/III alternative frameworks;
- the thesis-specific reduced mathematical architecture.

Do not overwrite older files merely because a newer formulation exists; preserve version history and mark superseded/provisional status.

## 9. Scope discipline

The current master ontology is intentionally broader than the final MSE thesis.

Do not infer that the thesis must make original contributions in every chain.

Current intended mathematical center:

`Chain I + Chain IV`, strongly supported by `Chain II`.

Chain III supplies hazards/cascades; Chains V–VI supply downstream applications, constraints, objectives, and decisions.

## 10. Novelty claims

All novelty statements remain hypotheses until systematically falsified against the literature.

A safe working statement is:

> Potential novelty lies in the rigorous integration of explicit dynamic infrastructure interface mechanisms, identification uncertainty, service-state mapping, and sustainability/equity-constrained viability/recoverability for coupled P–W–T–SW systems under climate stress.

This is not yet a proof that no prior paper has done the same thing.

## 11. Reproducibility minimum for future work

Every important result should preserve:

- source corpus/version;
- code;
- configuration;
- software/library versions where material;
- random seeds;
- hashes;
- assumptions;
- equations and units;
- test/convergence results;
- raw outputs;
- interpretation boundary;
- link from result back to source evidence.

## 12. Future-chat rule

A future chat should begin with `FUTURE_CHAT_BOOTSTRAP.md`, then inspect the exact repository artifacts relevant to the new task. It should not rely on conversational memory alone when the repository contains a more authoritative file.