---
name: thesis-scientific-data-acquisition
description: Evidence-controlled scientific data acquisition for the active extreme-heat Power System–Electrified Transportation thermal-interdependency thesis; follow the orchestrator and repository canonical governance.
---

# Scientific data acquisition

**Prerequisite:** Load `.github/skills/power-ev-thermal-research/SKILL.md` and its current authority/gates before using this module.

## Trigger and objective
Activate for original KIT / SINTEF / KU Leuven / EPFL / Qatar / bus-depot / OPSD data, repository discovery, metadata validation or bulk transfer. Acquire primary measured records without confusing them with calculated or synthetic data.

## Steps
1. Search official institution/operator/publisher, Zenodo, DataCite, Crossref, Dryad or recognized project repositories; use Firecrawl/Elicit only for *discovery*, and DOI/publisher/original metadata for admission.
2. Record title, DOI, version, authors, publisher, license, source landing page, original URL, retrieval UTC, hardware, site, instrumentation, sensor semantics, temporal resolution, and declared measured/calculated status.
3. Download only legally accessible original files, respecting API/download size limits and data-sharing permissions. Stream large transfers; record HTTP status, declared and actual bytes, SHA-256 and any publisher-supplied hash. Never silently replace an original file.
4. Preserve `raw/` read-only; use local/Drive secure archives for bulky original source data. GitHub retains code/registries/manifests only unless rights, size and permission explicitly permit data.
5. Register result as `ACQUIRED_VERIFIED`, `METADATA_ONLY`, `REQUEST_REQUIRED`, `BLOCKED`, or `REJECTED` with exact evidence basis. Dataset count ≠ distinct installation count; deduplicate DOI-version and file hashes.

## Outputs and gate
`source_registry.csv`, `download_log.csv`, checksum manifest, evidence-level decision. **Pass only** when primary provenance, data type, legal access and content match the claim. Search snippet-only datasets remain OPEN. Research-side discovery never upgrades thermal coupling.

### ECE6378 / RPG Lab overlay (S1)
Use published ECE6378 L6 (grid meters) and the original three lab repository descriptions *for source discovery only*. Record original release vs planned/unreleased course teaching files, provenance, DOI, original checksum, synthetic-vs-measured status, and license. Do not add course example synthetic test networks to the measured field-data portfolio. See orchestrator `references/ECE6378_VERIFIED_LEARNING_MAP.md`.
