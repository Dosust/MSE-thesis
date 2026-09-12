#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
INFILE="$ROOT/project/requirements-phase1-v1.in"
LOCKFILE="$ROOT/project/requirements-phase1-v1.lock.txt"

python -m pip install --disable-pip-version-check \
  "pip==24.0" \
  "pip-tools==7.4.1"

python -m piptools compile \
  --resolver=backtracking \
  --generate-hashes \
  --allow-unsafe \
  --output-file "$LOCKFILE" \
  "$INFILE"

python -m pip install --require-hashes -r "$LOCKFILE"
sha256sum "$LOCKFILE"
