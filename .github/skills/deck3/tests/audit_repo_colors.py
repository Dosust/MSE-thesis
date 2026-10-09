#!/usr/bin/env python3
"""Audit the active, authored design palette, without recoloring real photographs.

Usage: python .github/skills/deck3/tests/audit_repo_colors.py
Exit 1 for nonregistered design hex and literal RGB colors in active visual generators.
Historical archives, scientific data and photographed raster pixels are not modified.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REGISTRY = ROOT / ".github/skills/deck3/references/DECK3_SRGB_PALETTE.json"
CODE_LOCATIONS = (
    ROOT / ".github/skills/deck3/examples",
    ROOT / ".github/skills/scientific-infographic-design/examples",
    ROOT / ".github/skills/visquill-interactive-visualization/examples",
    ROOT / "visualization",
)
SUFFIXES = {".py", ".css", ".js", ".ts", ".tsx", ".jsx", ".svg", ".html"}
HEX = re.compile(r"(?<![A-Za-z0-9])#[0-9a-fA-F]{6}(?![A-Za-z0-9])")
RGB = re.compile(r"\\bRGBColor\\s*\\(\\s*(\\d+)\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)\\s*\\)")
# CSS RGB literals, excluding alpha-transparent pixels with a==0; all others must be exact.
RGBA = re.compile(r"\\brgba?\\(\\s*(\\d+)\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)\\s*(?:,\\s*([0-9.]+)\\s*)?\\)")


def audit():
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    tokens = {entry["hex"].upper() for entry in registry["colors"].values()}
    failures = []
    scanned = 0
    for folder in CODE_LOCATIONS:
        if not folder.exists():
            continue
        for path in folder.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in SUFFIXES:
                continue
            if any(part in {"build", "dist", "archive", "__pycache__", "node_modules"} for part in path.parts):
                continue
            scanned += 1
            body = path.read_text(encoding="utf-8")
            for lineno, line in enumerate(body.splitlines(), 1):
                # Ignore scientific examples of contrast formulas and fully transparent masking.
                for match in HEX.finditer(line):
                    if match.group().upper() not in tokens:
                        failures.append(f"{path.relative_to(ROOT)}:{lineno}: unauthorized HEX {match.group()}")
                for rx in (RGB, RGBA):
                    for match in rx.finditer(line):
                        rgb = tuple(int(x) for x in match.groups()[:3])
                        if rx is RGBA and match.group(4) is not None and float(match.group(4)) == 0:
                            continue
                        if any(x > 255 for x in rgb) or "#" + "".join(f"{x:02X}" for x in rgb) not in tokens:
                            failures.append(f"{path.relative_to(ROOT)}:{lineno}: unauthorized literal RGB {rgb}")
    return scanned, failures


if __name__ == "__main__":
    files, violations = audit()
    for violation in violations:
        print("FAIL:", violation)
    print(f"Active visual source files checked: {files}; violations: {len(violations)}")
    if violations:
        raise SystemExit(1)
