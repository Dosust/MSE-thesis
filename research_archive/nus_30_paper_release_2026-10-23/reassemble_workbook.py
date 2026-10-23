#!/usr/bin/env python3
"""Reassemble the exact validated 30-paper XLSM workbook from Git blobs."""
from pathlib import Path
import hashlib
ROOT = Path(__file__).resolve().parent
PARTS = sorted((ROOT / "workbook_parts").glob("workbook.part*"))
EXPECTED_PARTS = 10
EXPECTED_HASH = "cba6747c1c18e83f4a86677d1971bdbc010b9e7f7c61d0060b75f358ddea550a"
DEST = ROOT / "NUS_30_LP_Constraint_Corrected_2026-10-23.xlsm"
if len(PARTS) != EXPECTED_PARTS:
    raise SystemExit(f"Expected {EXPECTED_PARTS} parts, found {len(PARTS)}")
hasher = hashlib.sha256()
with DEST.open("wb") as result:
    for part in PARTS:
        payload = part.read_bytes()
        hasher.update(payload)
        result.write(payload)
if hasher.hexdigest() != EXPECTED_HASH:
    DEST.unlink(missing_ok=True)
    raise SystemExit("Checksum mismatch; removed invalid output")
print("Verified workbook:", DEST)
