#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.metadata as md
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

EXPECTED_PYTHON = (3, 11, 16)
EXPECTED_GREENEVT = "6aff1cac48869ccfa0183643979f5f04b04e1124"
EXPECTED_SUMO = "98d19a78148690294144002f8e1a18a28e5579cc"


def cmd(args: list[str], cwd: str | None = None) -> dict:
    p = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    return {
        "command": args,
        "returncode": p.returncode,
        "stdout": p.stdout.strip(),
        "stderr": p.stderr.strip(),
    }


def pkg(name: str) -> str | None:
    try:
        return md.version(name)
    except md.PackageNotFoundError:
        return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--thesis-root", default=".")
    ap.add_argument("--greenevt", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    thesis = Path(a.thesis_root).resolve()
    ge = Path(a.greenevt).resolve()

    versions = {
        n: pkg(n)
        for n in [
            "OpenDSSDirect.py",
            "dss-python",
            "dss-python-backend",
            "numpy",
            "pytest",
        ]
    }
    versions.update(
        {
            "python": sys.version,
            "python_tuple": list(sys.version_info[:3]),
            "platform": platform.platform(),
            "machine": platform.machine(),
        }
    )

    commands = {
        "git": cmd(["git", "--version"]),
        "git_lfs": cmd(["git", "lfs", "version"]),
        "sumo": cmd(["sumo", "--version"]),
        "sumo_source_commit": cmd(
            ["git", "-C", "/opt/sumo-src", "rev-parse", "HEAD"]
        ),
        "cmake": cmd(["cmake", "--version"]),
        "compiler": cmd(["g++", "--version"]),
        "pip_check": cmd([sys.executable, "-m", "pip", "check"]),
        "thesis_commit": cmd(["git", "rev-parse", "HEAD"], cwd=str(thesis)),
        "greenevt_commit": cmd(["git", "rev-parse", "HEAD"], cwd=str(ge)),
    }

    checks = {
        "python_exact_3_11_16": tuple(sys.version_info[:3]) == EXPECTED_PYTHON,
        "linux_amd64": platform.system() == "Linux"
        and platform.machine() in {"x86_64", "AMD64"},
        "opendssdirect_0_9_4": versions["OpenDSSDirect.py"] == "0.9.4",
        "numpy_1_26_4": versions["numpy"] == "1.26.4",
        "greenevt_commit_exact": commands["greenevt_commit"]["stdout"]
        == EXPECTED_GREENEVT,
        "sumo_source_commit_exact": commands["sumo_source_commit"]["stdout"]
        == EXPECTED_SUMO,
        "sumo_executable": commands["sumo"]["returncode"] == 0,
        "git_lfs_executable": commands["git_lfs"]["returncode"] == 0,
        "pip_check": commands["pip_check"]["returncode"] == 0,
        "thesis_commit_recorded": commands["thesis_commit"]["returncode"] == 0
        and len(commands["thesis_commit"]["stdout"]) == 40,
    }

    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "expected": {
            "python": ".".join(map(str, EXPECTED_PYTHON)),
            "greenevt_commit": EXPECTED_GREENEVT,
            "sumo_source_commit": EXPECTED_SUMO,
            "OpenDSSDirect.py": "0.9.4",
            "numpy": "1.26.4",
            "architecture": "linux/amd64",
        },
        "environment_variables": {
            k: os.environ.get(k)
            for k in [
                "PYTHONHASHSEED",
                "OMP_NUM_THREADS",
                "OPENBLAS_NUM_THREADS",
                "MKL_NUM_THREADS",
                "NUMEXPR_NUM_THREADS",
                "SUMO_HOME",
                "PYTHONPATH",
            ]
        },
        "versions": versions,
        "commands": commands,
        "checks": checks,
        "G_ENV": all(checks.values()),
    }

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["G_ENV"] else 2)


if __name__ == "__main__":
    main()
