# Thesis research skills catalog (V1)

**Current frozen thesis title:** *Engineering of Power–Electrified Transportation Interdependencies for Resilience* (2026-10-15 amendment V3).

Start with `.github/skills/power-ev-thermal-research/SKILL.md`. It coordinates the eight modular skills in `.github/skills/thesis-*/SKILL.md`. These modules are method and evidence controls **not approvals for any model, claim or dataset**.

| Module | Scope | Stage |
|---|---|---|
| S1 Data acquisition | primary data / provenance / checksums | acquire |
| S2 Electrical topology | verify transformer–EVSE network connections | qualify interface |
| S3 Python data engineering | clean, normalize, sync only supported sites | prepare |
| S4 Thermal physics | heat balance, cooling, derating | physical laws |
| S5 Applied mathematics | traceable ODE/DAE/hybrid model | derive |
| S6 System identification | fit physically admissible parameters | calibrate |
| S7 Experimental design / VVUQ | tests, independent holdouts and uncertainty | validate |
| S8 Resilience engineering | service state-time consequences | interpret |

**First deliverable:** an audited source registry, measurement QA file, evidenced physical-connectivity map, and directional thermal-evidence register. The dataset that does **not** exist cannot be substituted with a synthetic coupling claim.

## How to use

- Add this directory unchanged to the thesis repository (preferably a review branch).
- Invoke the orchestrator whenever a task concerns the active thesis thermal Power–T_e work.
- Keep original datasets in rights-compliant storage, not Git history; commit code, manifest hashes, and structured audit results.
- Execute `python tools/check_evidence.py --root results/<run-id>` for schema/claim-gate checks (schema gate only).

## ECE6378/RPG Lab method integration (V2, 2026-11-02)

**Still exactly eight thesis-core skills.** The supporting `.github/skills/thesis-physics-constrained-ml/SKILL.md` assists S2/S3/S5/S6/S7 and never adds a research objective. `references/ECE6378_LEARNING_MATRIX.csv` maps all 27 published-outline lectures (19–27 tentative); `references/ECE6378_VERIFIED_LEARNING_MAP.md` teaches priority/learning gates; `references/RPGLAB_CODE_TRANSFER_PROTOCOL.md` governs the three public code references; `references/PHYSICS_CONSTRAINED_ML_VVUQ.md` defines defensible M0/M1/M2 experiments.

**Execution order:** measurements/provenance + topology → power-flow and network constraints → thermal laws → reproducible M0/persistence baseline → only justified ML methods → VVUQ → bounded thermal resilience. No ML-first claims; no conversion of ampacity rating into a temperature sensor; no unverified coupling field validation.

Run both schema checks for a filled run (not just empty templates): `python tools/check_evidence.py --root <dir>` and `python tools/check_ml_experiments.py --root <dir>`.
