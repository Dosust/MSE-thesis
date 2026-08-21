# Project Memory

This directory contains provenance-aware memory capsules for future ChatGPT/Codex research sessions working on the MSE thesis.

## Current canonical snapshot

[`2026-08-21_chain_architecture_v2/`](2026-08-21_chain_architecture_v2/)

This is the **corrected v2** snapshot produced after re-auditing the first memory capsule against the authoritative thesis scope, mathematical foundation, proposition registry, Monte Carlo prompt/run metadata, conversation archive and provenance files.

### Start here

1. [`2026-08-21_chain_architecture_v2/README.md`](2026-08-21_chain_architecture_v2/README.md)
2. [`2026-08-21_chain_architecture_v2/00_CANONICAL_STATE.md`](2026-08-21_chain_architecture_v2/00_CANONICAL_STATE.md)
3. [`2026-08-21_chain_architecture_v2/14_CORRECTION_LOG.md`](2026-08-21_chain_architecture_v2/14_CORRECTION_LOG.md)
4. [`2026-08-21_chain_architecture_v2/PROJECT_MEMORY.json`](2026-08-21_chain_architecture_v2/PROJECT_MEMORY.json)

## Superseded snapshot

`2026-08-21_chain_architecture/` is retained for provenance but should not be used as the canonical future-chat memory. Its errors/corrections are documented in v2.

## Memory versus evidence

Memory capsules provide **high recall**. They do not replace authoritative evidence. For precise scientific claims, follow links to original literature/evidence records, datasets, prompts, code, figures, transcript files, hashes and provenance artifacts.

## Authenticity rule

A memory synthesis is not automatically a verbatim transcript. Exact transcript claims belong under `conversation/`; source integrity and binary/archive provenance belong under `provenance/`.

## Automated consistency check

The corrected v2 capsule includes:

`2026-08-21_chain_architecture_v2/validate_memory.py`

and GitHub Actions workflow:

`.github/workflows/project-memory-qa.yml`

These check repository consistency/invariants, not scientific truth or empirical validation.