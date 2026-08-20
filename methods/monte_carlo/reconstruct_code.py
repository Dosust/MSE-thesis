#!/usr/bin/env python3
from pathlib import Path
import hashlib

root = Path(__file__).resolve().parent
parts = sorted((root / "code_parts").glob("part*.pyfrag"))
if len(parts) != 4:
    raise SystemExit(f"Expected 4 code parts, found {len(parts)}")
out = root / "prisma_monte_carlo_rank_325.py"
data = b"".join(p.read_bytes() for p in parts)
sha = hashlib.sha256(data).hexdigest()
expected = "951c8424bbcc8c468e579541b3549d7c324bbea185140412491c01001075b4b5"
if sha != expected:
    raise SystemExit(f"SHA-256 mismatch: {sha} != {expected}")
out.write_bytes(data)
print(f"PASS {out.name} bytes={len(data)} sha256={sha}")
