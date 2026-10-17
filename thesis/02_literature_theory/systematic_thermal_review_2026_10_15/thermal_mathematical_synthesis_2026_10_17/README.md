# Research synthesis release — 2026-10-17

This is a **draft, evidence-bounded** mathematical synthesis of the three obtained original focal studies (Gong 2015; Kunlasing 2022; Krama 2026), adjoining foundation sources, and a new proposed Power–Electrified Transportation electrothermal hybrid model under extreme heat.

## Artifacts

1. [THREE_PAPER_SOURCE_BY_SOURCE_COMPARATIVE_MATRIX.csv](THREE_PAPER_SOURCE_BY_SOURCE_COMPARATIVE_MATRIX.csv) — 14 source-located mechanism/measurement/equation/validation records for three focal papers.
2. [FOUNDATIONAL_PRIOR_ART_AND_THIRTY_SOURCE_ACCESS.md](FOUNDATIONAL_PRIOR_ART_AND_THIRTY_SOURCE_ACCESS.md) — source-version hierarchy, prior transformer thermal models, 2025 IEEE loading-guide status, 2018 IEC guide scope, remaining access blockers and falsifiable novelty claims.
3. [COUPLED_ELECTROTHERMAL_HYBRID_MODEL_V0.md](COUPLED_ELECTROTHERMAL_HYBRID_MODEL_V0.md) — proposed derived P thermal two-node energy balances + EVSE effective thermal balance + electrical power/constraint interface, hybrid states/modes, measurement operator, conservation, solvability/identifiability, service reachability.
4. [VVUQ_IDENTIFIABILITY_AND_DATA_GATES.md](VVUQ_IDENTIFIABILITY_AND_DATA_GATES.md) — dimension, energy and solver verification; actual-observable calibration; temporal/hardware/joint-interface independent validation; consent/time-synchronization and robust service requirements.
5. [SYNTHETIC_ELECTROTHERMAL_SANITY_V0.py](SYNTHETIC_ELECTROTHERMAL_SANITY_V0.py) — standalone Python 3 synthetic sanity tests for energy balances, AC/DC loss, numerical refinement and temperature-dependent offer power. **Not calibrated, not a field scenario, not a standards implementation, and not a multi-site cross-infrastructure validation.** It intentionally has no battery capacity/SoC termination and therefore 2-hour delivered DC energy is an unconstrained port-energy integral, **not** an EV journey or battery storage claim.

### Executable check

`python3 SYNTHETIC_ELECTROTHERMAL_SANITY_V0.py`

The same locally inspected code passed its included unit/sanity checks; reported synthetic 2h output was 100.0 kWh at 25°C and 64.3074 kWh at 50°C, entirely determined by **arbitrary illustrative parameters** and intentionally omitted BMS limits. **Do not use numbers as empirical prediction or physical capability.**

### Scientific status

- **Stage 2 three-paper comparative matrix:** COMPLETE, source-bounded.
- **Stage 3 remaining priority 30:** INCOMPLETE; 6 original publisher PDFs, 1 author accepted manuscript and 1 indexed publisher article among 30; 22 priority originals still unverified. Susa 2005 original article and complete normative IEEE/IEC standards unverified.
- **Stage 4 proposed mathematics:** v0 DERIVED under listed assumptions; not fitted, proved to be formally viable, experimentally validated, or frozen.
- **Stage 5 VVUQ:** preregistered protocol/logic complete; no new raw training data or joint experiment.
- Gong and Kunlasing original ASU PDFs are secured within the conversation, not redistributed through GitHub. Krama original PDF previously verified, raw 1/5-min measurements unreceived. Corresponding-author email request reported sent by user; not independently verified.

### Existing upstream/source audits
- ../gong_original_ieee_2026_10_17/GONG_2015_ORIGINAL_IEEE_EVIDENCE_AUDIT.md
- ../kunlasing_original_ieee_2026_10_17/KUNLASING_2022_ORIGINAL_IEEE_PHYSICS_CONTROL_VALIDATION_AUDIT.md
- ../krama_original_pdf_2026_10_16/KRAMA_ORIGINAL_PDF_PHYSICS_MATHEMATICS_VALIDATION.md

**Research integrity gate:** Existing prior art covers transformer heat dynamics, thermal control of charging, and charger heat derating independently. A new coupling equation is a **hypothesis** until original physical source/control/receiver measurements are synchronized and physically attributed. No global novelty claim is made.
