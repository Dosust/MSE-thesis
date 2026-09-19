#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

EXPECTED_GREENEVT = "6aff1cac48869ccfa0183643979f5f04b04e1124"
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path):
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def nonempty(path: Path) -> bool:
    return path.exists() and path.is_file() and path.stat().st_size > 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifacts", required=True)
    ap.add_argument("--environment", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    root = Path(a.artifacts)
    env_path = Path(a.environment)
    env = load_json(env_path) or {}
    commands = env.get("commands", {})

    required_names = [
        "docker_build.log",
        "docker_image_inspect.json",
        "docker_image_id.txt",
        "pip_freeze.txt",
        "dpkg_manifest.tsv",
        "artifact_sha256_pre_gate.txt",
        "environment.json",
        "source_bytes.json",
        "opendss_baseline.json",
        "sumo_baseline.json",
        "q05_run1.json",
        "q05_run2.json",
        "reproducibility.json",
    ]
    required = {name: root / name for name in required_names}
    file_checks = {name: nonempty(path) for name, path in required.items()}

    thesis_commit = commands.get("thesis_commit", {}).get("stdout", "")
    greenevt_commit = commands.get("greenevt_commit", {}).get("stdout", "")

    image_id = (
        required["docker_image_id.txt"].read_text().strip()
        if nonempty(required["docker_image_id.txt"])
        else ""
    )
    inspect_json = (
        load_json(required["docker_image_inspect.json"])
        if nonempty(required["docker_image_inspect.json"])
        else None
    )
    pip_freeze = (
        required["pip_freeze.txt"].read_text()
        if nonempty(required["pip_freeze.txt"])
        else ""
    )

    checks = {
        "all_required_evidence_files_nonempty": all(file_checks.values()),
        "thesis_commit_recorded": bool(SHA40.fullmatch(thesis_commit)),
        "greenevt_commit_exact": greenevt_commit == EXPECTED_GREENEVT,
        "docker_image_id_recorded": image_id.startswith("sha256:"),
        "docker_image_inspect_valid": isinstance(inspect_json, list)
        and len(inspect_json) > 0,
        "opendssdirect_lock_in_pip_freeze": "OpenDSSDirect.py==0.9.4"
        in pip_freeze,
        "dpkg_manifest_recorded": nonempty(required["dpkg_manifest.tsv"]),
        "pre_gate_hash_manifest_recorded": nonempty(
            required["artifact_sha256_pre_gate.txt"]
        ),
    }

    digests = {
        name: sha256(path)
        for name, path in required.items()
        if path.exists() and path.is_file()
    }

    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "required_files": file_checks,
        "recorded_commits": {
            "thesis": thesis_commit or None,
            "greenevt": greenevt_commit or None,
        },
        "docker_image_id": image_id or None,
        "evidence_sha256": digests,
        "checks": checks,
        "G_PROV": all(checks.values()),
    }

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["G_PROV"] else 2)


if __name__ == "__main__":
    main()
