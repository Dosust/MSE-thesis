# Authenticity and Provenance Rules — v2

## 1. Evidence hierarchy

Use this hierarchy when resolving conflicts:

```text
A. exact authoritative source artifact
B. exact transcript/source text
C. verified bibliographic/full-text evidence
D. corrected v2 memory synthesis
E. reconstructed assistant summary
F. superseded v1 memory
G. unaudited model recollection
```

## 2. Transcript classes

### VERBATIM_CURRENT_VISIBLE
Exact wording copied from the currently visible conversation.

### VERBATIM_REPOSITORY_ARCHIVE
Exact wording already preserved in `conversation/`.

### USER_SUPPLIED_REFERENCE_VERBATIM
Long text pasted by the user and preserved exactly as source/reference material.

### RECONSTRUCTED_SUMMARY
Scientifically faithful summary where exact assistant wording is not preserved.

Do not label a reconstructed summary as verbatim.

## 3. Scientific evidence classes

Use:

```text
VERIFIED_FULL_TEXT
VERIFIED_METADATA
CORPUS_DERIVED
MATHEMATICAL_DEFINITION
MATHEMATICAL_TEMPLATE
PROPOSED_HYPOTHESIS
PROPOSED_MECHANISM
SYNTHETIC_QA
EMPIRICAL_RESULT
IDENTITY_CONFLICT
PENDING
```

## 4. Literature rule

A memory citation/DOI is not the final bibliographic authority. Before thesis publication:

- verify identity;
- verify DOI;
- verify title/authors/year/venue;
- verify exact proposition/equation from full text where needed;
- record page/section/evidence anchor.

## 5. Mathematical rule

Do not confuse:

- a definition with a theorem;
- a numerical approximation with an exact set;
- one optimizer solution with proof of uniqueness;
- a synthetic benchmark with empirical validation;
- a high rank with causal importance;
- an architectural diagram with evidence of mechanism magnitude.

## 6. PRISMA/ranking rule

PRISMA search/screening and Monte Carlo ranking serve different purposes.

Closed-corpus ranking supports statements only inside the declared corpus/model.

It does not prove global novelty or global literature completeness.

## 7. Artifact-storage rule

Before saying an artifact is “in GitHub,” verify that it appears in the GitHub tree.

If only an online/Drive link and hash are stored in GitHub, say:

```text
indexed in GitHub; raw bytes preserved externally
```

not:

```text
raw file committed to GitHub
```

## 8. Versioning rule

Do not silently overwrite a scientific definition after results exist.

When an architecture/protocol changes:

1. retain old version;
2. create amendment/correction record;
3. state what changed;
4. state why;
5. identify affected results;
6. rerun dependent analysis where necessary.

This is why v1 is preserved and v2 supersedes it for recall.

## 9. Hidden/runtime exclusion

Do not archive or claim to archive:

- hidden chain-of-thought;
- system/developer instructions;
- credentials/secrets;
- connector internals;
- inaccessible private runtime material.

## 10. Current project-specific caution

The following phrases require evidence before use:

- “globally novel”;
- “globally complete literature”;
- “validated digital twin”;
- “mathematically proven”;
- “unique optimal solution”;
- “causal interface effect”;
- “exact viability kernel” when only finite-grid approximation was computed.

## 11. Future-chat behavior

A future chat should use memory to recover context quickly, then reopen the relevant authoritative files before making a precise scientific claim.

Memory is optimized for **recall**; source artifacts are optimized for **authority**.