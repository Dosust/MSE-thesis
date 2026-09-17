from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import audit_inputs  # noqa: E402


def _pointer(oid: str, size: int) -> str:
    return (
        "version https://git-lfs.github.com/spec/v1\n"
        f"oid sha256:{oid}\n"
        f"size {size}\n"
    )


def test_frozen_uds_pointer_identity(tmp_path: Path):
    p = tmp_path / "data" / "UDS.db"
    p.parent.mkdir(parents=True)
    expected = audit_inputs.EXPECTED_LFS["data/UDS.db"]
    p.write_text(_pointer(expected["oid_sha256"], expected["size_bytes"]))
    record = audit_inputs.inspect_required_file(tmp_path, "data/UDS.db")
    assert record["source_identity_ok"] is True
    assert record["materialized"] is False


def test_wrong_uds_pointer_rejected(tmp_path: Path):
    p = tmp_path / "data" / "UDS.db"
    p.parent.mkdir(parents=True)
    expected = audit_inputs.EXPECTED_LFS["data/UDS.db"]
    p.write_text(_pointer("0" * 64, expected["size_bytes"]))
    record = audit_inputs.inspect_required_file(tmp_path, "data/UDS.db")
    assert record["source_identity_ok"] is False


def test_frozen_sumo_pointer_identity(tmp_path: Path):
    p = tmp_path / "data" / "sumo_network" / "greensboro.net.xml"
    p.parent.mkdir(parents=True)
    expected = audit_inputs.EXPECTED_LFS["data/sumo_network/greensboro.net.xml"]
    p.write_text(_pointer(expected["oid_sha256"], expected["size_bytes"]))
    record = audit_inputs.inspect_required_file(
        tmp_path, "data/sumo_network/greensboro.net.xml"
    )
    assert record["source_identity_ok"] is True
    assert record["materialized"] is False
