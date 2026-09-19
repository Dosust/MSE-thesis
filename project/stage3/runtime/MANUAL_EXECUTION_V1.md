# Manual Stage 3 Runtime Execution

This route exists because the GitHub-hosted qualification job was observed to fail before executing its first workflow step.

## Required host

Use a host satisfying:

```text
OS: Linux
architecture: amd64 / x86_64
Docker: installed and runnable
Git: installed
Git LFS: installed and able to materialize the frozen GreenEVT objects
Network: access to GitHub and GreenEVT Git-LFS
```

Do not substitute ARM execution, an unfrozen SUMO package, or a manually modified GreenEVT dataset and then call the result the same qualification experiment.

## Execute

From the thesis repository root:

```bash
chmod +x project/stage3/runtime/run_stage3_runtime_qualification.sh
project/stage3/runtime/run_stage3_runtime_qualification.sh
```

The script:

1. checks Linux/amd64 and Docker availability;
2. checks out GreenEVT commit `6aff1cac48869ccfa0183643979f5f04b04e1124`;
3. materializes and verifies the two frozen LFS objects;
4. builds the frozen historical-SUMO container;
5. executes the environment, data, OpenDSS, SUMO, Q05, sensitivity, reproducibility and provenance gates;
6. writes all evidence to `runtime_artifacts/`;
7. evaluates the authoritative aggregate runtime gate.

## Evidence required after execution

At minimum preserve:

```text
runtime_artifacts/
├── docker_build.log
├── docker_image_inspect.json
├── docker_image_id.txt
├── environment.json
├── source_bytes.json
├── opendss_baseline.json
├── sumo_baseline.json
├── q05_run1.json
├── q05_run2.json
├── reproducibility.json
├── provenance.json
├── runtime_gate.json
├── pip_freeze.txt
├── dpkg_manifest.tsv
├── gate_exit_codes.tsv
├── artifact_sha256_pre_gate.txt
└── artifact_sha256.txt
```

## Decision rule

```math
G_{RUNTIME}
=
G_{DATA}
\land
G_{ENV}
\land
G_{DSS}
\land
G_{SUMO}
\land
G_{Q05}
\land
G_{SENS}
\land
G_{REPRO}
\land
G_{PROV}.
```

Only if every term passes may the thesis record:

```math
G_{impl}(Q05,C_{DEV})=PASS.
```

A failing or blocked gate must remain visible; do not modify thresholds or source identities after observing results simply to obtain a PASS.

## Scope boundary

A runtime PASS verifies the frozen implementation environment and Q05 coupling mechanism. It does **not** establish empirical Greensboro validation, full Stage-3 closure, or H1 support. Full GreenEVT transport-case execution and solver-version sensitivity remain subsequent experiments.
