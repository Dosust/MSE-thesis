#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path

REPO = "https://github.com/GreenEVT/GreenEVT.git"
ZIP = "https://gustavnilsson.name/files/GreenEVT.zip"
FROZEN_COMMIT = "6aff1cac48869ccfa0183643979f5f04b04e1124"
LFS_INCLUDE = "data/UDS.db,data/sumo_network/greensboro.net.xml"


def run(cmd: list[str], *, cwd: Path | None = None, env: dict | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, env=env, check=True)


def git_stdout(cmd: list[str], *, cwd: Path) -> str:
    return subprocess.check_output(cmd, cwd=cwd, text=True).strip()


def main() -> None:
    p = argparse.ArgumentParser(description="Acquire the frozen GreenEVT source for H1 Level 2.")
    p.add_argument("--dest", default="external/GreenEVT")
    p.add_argument("--method", choices=("git", "zip"), default="git")
    args = p.parse_args()

    dest = Path(args.dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        raise SystemExit(f"Refusing to overwrite existing path: {dest}")

    acquisition_status = "UNKNOWN"

    if args.method == "git":
        if shutil.which("git") is None:
            raise SystemExit("git is required")
        if subprocess.run(["git", "lfs", "version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
            raise SystemExit("git-lfs is required before acquisition")

        # Avoid implicitly accepting current upstream main or automatically
        # smudging unrelated LFS files.  Checkout the frozen commit first.
        env = os.environ.copy()
        env["GIT_LFS_SKIP_SMUDGE"] = "1"
        run(["git", "clone", REPO, str(dest)], env=env)
        run(["git", "checkout", "--detach", FROZEN_COMMIT], cwd=dest)
        resolved = git_stdout(["git", "rev-parse", "HEAD"], cwd=dest)
        if resolved != FROZEN_COMMIT:
            raise SystemExit(f"Frozen commit mismatch: expected {FROZEN_COMMIT}, got {resolved}")
        run(["git", "lfs", "pull", f"--include={LFS_INCLUDE}", "--exclude="], cwd=dest)
        acquisition_status = "FROZEN_GIT_COMMIT_CHECKED_OUT_LFS_REQUESTED"

    else:
        # Upstream GreenEVT documents this archive as a fallback when Git/LFS
        # cloning is unavailable.  An archive has no Git commit identity, so it
        # is not automatically equivalent to the frozen commit.  It must pass
        # audit_inputs.py (and any frozen file-identity checks) before use.
        if shutil.which("curl") is None and shutil.which("wget") is None:
            raise SystemExit("curl or wget is required for --method zip")
        archive = dest.parent / "GreenEVT.zip"
        if shutil.which("curl"):
            run(["curl", "-fL", ZIP, "-o", str(archive)])
        else:
            run(["wget", "-O", str(archive), ZIP])
        if shutil.which("unzip") is None:
            raise SystemExit("unzip is required")
        run(["unzip", "-q", str(archive), "-d", str(dest.parent)])
        acquisition_status = "UPSTREAM_ZIP_DOWNLOADED_IDENTITY_AUDIT_REQUIRED"

    manifest = {
        "level": 2,
        "lineage": "GreenEVT + SMART-DS Greensboro + OSM/SUMO",
        "source_repository": REPO,
        "frozen_commit": FROZEN_COMMIT,
        "alternate_archive": ZIP,
        "method": args.method,
        "destination": str(dest),
        "acquisition_status": acquisition_status,
        "required_next_step": "Run audit_inputs.py and require every source/materialization gate to pass before feeder feature extraction.",
        "claim_boundary": "realistic synthetic infrastructure; not observed Greensboro utility/event data",
    }
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
