#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import shutil
import subprocess
from pathlib import Path

REPO = "https://github.com/GreenEVT/GreenEVT.git"
ZIP = "https://gustavnilsson.name/files/GreenEVT.zip"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def main() -> None:
    p = argparse.ArgumentParser(description="Acquire GreenEVT for H1 Level 2.")
    p.add_argument("--dest", default="external/GreenEVT")
    p.add_argument("--method", choices=("git", "zip"), default="git")
    args = p.parse_args()
    dest = Path(args.dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        raise SystemExit(f"Refusing to overwrite existing path: {dest}")

    if args.method == "git":
        if shutil.which("git") is None:
            raise SystemExit("git is required")
        run(["git", "clone", REPO, str(dest)])
        if subprocess.run(["git", "lfs", "version"], cwd=dest, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
            subprocess.run(["git", "lfs", "pull"], cwd=dest, check=True)
        else:
            raise SystemExit("GreenEVT uses Git LFS. Install git-lfs and run `git lfs pull` in the cloned repository.")
    else:
        if shutil.which("curl") is None and shutil.which("wget") is None:
            raise SystemExit("curl or wget is required for --method zip")
        archive = dest.parent / "GreenEVT.zip"
        if shutil.which("curl"):
            run(["curl", "-L", ZIP, "-o", str(archive)])
        else:
            run(["wget", "-O", str(archive), ZIP])
        if shutil.which("unzip") is None:
            raise SystemExit("unzip is required")
        run(["unzip", str(archive), "-d", str(dest.parent)])

    manifest = {
        "level": 2,
        "lineage": "GreenEVT + SMART-DS Greensboro + OSM/SUMO",
        "source_repository": REPO,
        "alternate_archive": ZIP,
        "destination": str(dest),
        "claim_boundary": "realistic synthetic infrastructure; not observed Greensboro utility/event data",
    }
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
