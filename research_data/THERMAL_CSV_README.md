# Thermal CSV evidence-readiness pipeline (working implementation)

This pipeline is a **data qualification utility**, not completion of the MSE thesis and not a scientific validation claim.

## Scope and authority

Current thesis: **Engineering of Power–Electrified Transportation Interdependencies for Resilience**.
Governing authority: current October 2026 thermal-only SO1/SO2/SO3, physics/mathematics-first directive, canonical V3 title, equipment and evidence/non-invention authority. The older Austin/flood pipeline is historical, not a current prerequisite. AI prediction and digital-twin development are out of scope.

## Execute

Run from the repo root:

    python -m unittest discover -s tests -p 'test_thermal_csv_research.py' -v
    python scripts/thermal_csv_research.py --repo . --input-dir research_data/thermal_inputs --output-dir research_outputs/thermal_csv --strict-input

The runner generates **14 empty CSV schema templates** under the output directory. Place only attributable, permission-compatible observational data in the specified input directory; do not commit sensitive/raw operator data. Each non-source record must reference a row in source_evidence.csv. Required timestamps must be UTC. Stable equipment IDs and physical site ID must agree. Missing data are reported as blockers; no fake rows are generated.

The GitHub Action runs tests, current thermal governance checks, and the CSV readiness audit on PR or dispatch. It runs weekly on the default branch **only after** a reviewed merge. It uploads non-raw audit reports as a short-retention artifact.

## Interpreting outputs

- dataset_readiness.csv: SCHEMA_PASS means a populated CSV passed limited structural checks, NOT that source, sensors, units or physical models were independently verified.
- referential_integrity.csv: broken source or equipment references.
- linked_observation_candidates.csv: graph-connected, same-installation, exact-timestamp pairs. This is preliminary linkage, **not thermal directionality or causal identification**.
- ac_power_accounting_residuals.csv: transformer measured power minus independently labeled non-EV demand and matched EVSE AC inputs. This unresolved residual is **not** identified transformer losses, conservation verification, or a causal estimate; physical boundaries and sensor errors remain unverified.
- research_status.csv: R01–R15 data-readiness blockers, R16 deferred under active scope.
- gate_results.json: G0 indicates presence of governance files only. G1–G8 are not scientific passes.
- research_manifest.json and RESULTS_SUMMARY.md: traceable run provenance and honest status.

## Limits / next research gates

This code does NOT acquire public data automatically, infer mechanisms from correlations, calibrate transformer laws, estimate critical times, claim independent physical validation, or calculate sustainability from absent service observations.

Next, after primary source-specific datasets are legally accessed, qualify original sensor positions, timestamp alignment, physical connections, AC load decomposition, temperature-dependent control action, and held-out validation before extending SO1 through SO3.

Never turn a green GitHub Action into a claim of empirical scientific validation.
