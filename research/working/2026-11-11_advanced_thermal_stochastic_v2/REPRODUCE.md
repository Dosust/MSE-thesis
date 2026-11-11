# Exact reproduction instructions

## Local source files, no internet or external empirical data required

Place the six unchanged original Drive-backed inputs listed by filename and SHA-256 in `ORIGINAL_INPUT_MANIFEST.json` under `/mnt/data` (or update `ROOT` in the reproducible source), including the two EPFL XLSX workbooks. Original measured files are **not included** in this package.

## Commands

```bash
python run_advanced_experiments.py
python epfl_reproduce.py
python verify_experiment_results.py
```

Both computational scripts are self-contained other than the original data and Python dependencies. The original EPFL replay script writes to `/mnt/data/thermal_extension_20261111` by default; change its output directory constant if you want output within this package.

Python dependencies: numpy, scipy, matplotlib, lxml, artifact_tool; standard-library csv, datetime, hashlib, json, zipfile. `artifact_tool` is required specifically for reading the EPFL session workbook; sparse minute-level XLSX cells are read as OOXML via ZIP using standard library primitives, avoiding excess memory.

The source archives and the prior historical results are not automatically re-downloaded or overwritten. The new audit is separate from past 2026-11-11 component tests. Numerical results may vary marginally with versions/tolerances, and physical/sensor interpretation must still be independently checked by the researcher and supervisor.

## Scientific gates

This is an **assistant-executed and source-hash-referenced working numerical study**. The 5-paper method comparisons are neither full equation-by-equation reproductions of original papers nor new field experiments. No same-site transformer and EVSE thermal transfer is empirically validated. Do not claim completed student independent implementation until reviewed and reproduced.
