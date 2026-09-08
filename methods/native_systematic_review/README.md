# Native systematic-review reproducibility

Utility: `native_pilot_reproduce.py`

## CPX-Q0 v2.2 reproduction

Expected raw file:
`2026-09-08_COMPENDEX_Q0_v2_2_RAW_N0245.csv`

Prepare audit + deterministic samples:

```bash
python methods/native_systematic_review/native_pilot_reproduce.py prepare \
  --raw 2026-09-08_COMPENDEX_Q0_v2_2_RAW_N0245.csv \
  --run-id CPX-Q0 \
  --outdir repro/CPX-Q0 \
  --seed 20260907 \
  -n 30 \
  --year-min 2000 \
  --year-max 2026 \
  --anchors 10.1016/j.ress.2017.01.026,10.1016/j.ress.2026.112819,10.1016/j.ress.2026.112407
```

Expected audit invariants:
- SHA-256: `2c15662b02f27a085dc39f50245d33c4f2166c63839050feb8fc2eb22f7816a8`
- rows: 245
- fields: 45
- canonical unique: 245
- duplicate key count: 0
- observed years: 2001–2026
- outside year rule: 0
- anchors: all 3 retrieved
- development sample n=30
- validation sample n=30

The reproduced development and validation `Raw_Index` sequences were verified byte-for-byte in ordering against the frozen sample selection produced in the 2026-09-08 audit.

After scientific screening, use:

```bash
python methods/native_systematic_review/native_pilot_reproduce.py analyze \
  --screened screened_sample.csv
```

For exact-key overlap/Jaccard:

```bash
python methods/native_systematic_review/native_pilot_reproduce.py compare \
  --a database_A.csv \
  --b database_B.csv
```

## Scientific boundary

The code prepares and audits samples; it does **not** replace eligibility screening. Apply the frozen family-specific screening codebook before interpreting precision or freeze decisions.
