#!/usr/bin/env python3
"""Reconstruct split Base64 thesis archive payloads and verify SHA-256."""
from __future__ import annotations

import base64
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAYLOADS = [
    {
        "parts_dir": ROOT / "archive/session_snapshot/textual",
        "pattern": "part*.b64",
        "output": ROOT / "archive/session_snapshot/MSE-thesis-textual-snapshot.tar.gz",
        "sha256": "8e2ab6aee07a23471554af361e35bd755f4758b1d95b0006ff23014976fadefe",
    },
    {
        "parts_dir": ROOT / "archive/binary_payloads/final325_xlsx",
        "pattern": "part*.b64",
        "output": ROOT / "archive/binary_payloads/Thesis_Final_Unique_Papers_325_2026-08-20.xlsx",
        "sha256": "2a1b7155f6d71d320fef7237ffba97375f673ee6cb4d8d3ac471bdd4a27285f0",
    },
]


def reconstruct(spec: dict[str, object]) -> None:
    parts_dir = Path(spec["parts_dir"])
    parts = sorted(parts_dir.glob(str(spec["pattern"])))
    if not parts:
        raise FileNotFoundError(f"No parts found in {parts_dir}")
    payload = "".join(p.read_text(encoding="ascii").strip() for p in parts)
    raw = base64.b64decode(payload, validate=True)
    digest = hashlib.sha256(raw).hexdigest()
    expected = str(spec["sha256"])
    if digest != expected:
        raise RuntimeError(f"SHA-256 mismatch for {parts_dir}: {digest} != {expected}")
    output = Path(spec["output"])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(raw)
    print(f"PASS {output.relative_to(ROOT)}  sha256={digest}  bytes={len(raw)}")


if __name__ == "__main__":
    for item in PAYLOADS:
        reconstruct(item)
