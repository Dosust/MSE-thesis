#!/usr/bin/env python3
"""Generate deterministic data for the Infrastructure Viability Explorer."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from models.viability_explorer import write_experiment


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("visualization/infrastructure_viability_explorer/demo-data.json"),
    )
    args = parser.parse_args()
    path = write_experiment(args.output)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
