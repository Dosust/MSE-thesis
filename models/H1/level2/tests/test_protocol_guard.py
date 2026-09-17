from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_protocol_is_structurally_valid_but_not_confirmatory(tmp_path: Path):
    out = tmp_path / "protocol_status.json"
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "validate_protocol.py"),
            "--protocol",
            str(ROOT / "config" / "protocol_v1.json"),
            "--root",
            str(ROOT),
            "--out",
            str(out),
        ],
        check=True,
    )
    data = json.loads(out.read_text())
    assert data["status"] == "METHOD_FROZEN_INPUTS_OPEN"
    assert data["confirmatory_ready"] is False
    assert all(data["structural_gates"].values())
    assert all(data["registry_gates"].values())
    assert data["freeze_gates"]["F_confirmatory_authorization"] is False


def test_confirmatory_gate_refuses_current_protocol():
    cp = subprocess.run(
        [
            sys.executable,
            str(ROOT / "validate_protocol.py"),
            "--protocol",
            str(ROOT / "config" / "protocol_v1.json"),
            "--root",
            str(ROOT),
            "--require-confirmatory",
        ],
        capture_output=True,
        text=True,
    )
    assert cp.returncode == 3
