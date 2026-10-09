#!/usr/bin/env python3
"""Deck3 authored-source color gate. Source-only: does NOT certify rendered PPTX.
SVG scientific figure fills/strokes/CSS are auditable; photographic PNG pixels are not.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
import xml.etree.ElementTree as ET

_PALETTE = Path(__file__).resolve().parents[1] / "references" / "DECK3_SRGB_PALETTE.json"
_HEX = re.compile(r"^#[0-9a-fA-F]{6}$")
_ATTRS = {"fill", "stroke", "color", "stop-color", "flood-color"}
_UNSUPPORTED = {"currentcolor", "inherit", "initial", "unset", "transparent"}
_GRADIENT_TAGS = {"linearGradient", "radialGradient", "filter", "pattern"}

def canonical_colors() -> set[str]:
    doc = json.loads(_PALETTE.read_text(encoding="utf-8"))
    if doc.get("color_space") != "sRGB" or len(doc.get("colors", {})) != 13:
        raise ValueError("Invalid canonical Deck3 color authority")
    return {x["hex"].upper() for x in doc["colors"].values()}

def _hex_or_error(value: str, location: str, allowed: set[str], errors: list[str]) -> None:
    raw = value.strip()
    if raw.lower() == "none":
        return
    if not _HEX.fullmatch(raw):
        errors.append(f"{location}: unauthorized nonliteral/unsupported color {raw!r}")
    elif raw.upper() not in allowed:
        errors.append(f"{location}: off-palette authored color {raw.upper()}")

def audit_svg(path: str | Path) -> dict:
    source = Path(path)
    try:
        root = ET.parse(source).getroot()
    except ET.ParseError as exc:
        return {"path": str(source), "status": "BLOCKED", "errors": [f"malformed SVG: {exc}"]}
    permitted = canonical_colors()
    errors = []
    checked = 0
    for node in root.iter():
        kind = node.tag.rsplit("}", 1)[-1]
        if kind in _GRADIENT_TAGS:
            errors.append(f"prohibited SVG effect: {kind}")
        for key, val in node.attrib.items():
            name = key.rsplit("}", 1)[-1].lower()
            if name in _ATTRS:
                checked += 1
                _hex_or_error(val, f"{kind}.{name}", permitted, errors)
            elif name == "style":
                for declaration in val.split(";"):
                    if ":" not in declaration:
                        continue
                    prop, value = declaration.split(":", 1)
                    if prop.strip().lower() in _ATTRS:
                        checked += 1
                        _hex_or_error(value, f"{kind}.style.{prop.strip()}", permitted, errors)
        # Raw SVG style sheets can bypass inspection; fail closed.
        if kind == "style" and (node.text or "").strip():
            errors.append("SVG <style> stylesheet not parsed by color gate; rewrite using exact attrs")
    if not any(n.tag.rsplit("}",1)[-1] == "svg" for n in [root]):
        errors.append("not SVG root")
    # Source background must be explicitly white if a background rectangle is authored.
    # A blank/transparent canvas does not prove a white slide; check at PPTX assembly.
    return {"path": str(source),
            "status": "SVG_SOURCE_PALETTE_PASS_NOT_RENDER_CERTIFIED" if not errors else "BLOCKED",
            "checked_color_attributes": checked, "errors": errors}

def check_figure_source(png_path: str | Path, declared_kind: str | None = None) -> dict:
    png_path = Path(png_path)
    vector = png_path.with_suffix(".svg")
    if vector.exists():
        return audit_svg(vector)
    if declared_kind == "authentic_photograph":
        return {"path": str(png_path), "status": "AUTHENTIC_PHOTO_EXCEPTION_REQUIRES_MANUAL_REVIEW",
                "errors": [], "requires": ["photo provenance", "no artificial tint/overlay", "rendered slide"] }
    return {"path": str(png_path), "status": "COLOR_NOT_VERIFIED_RASTER_ONLY",
            "errors": [], "requires": ["editable source/semantic palette registry", "visual and PPTX audit"]}

def main():
    ap=argparse.ArgumentParser(description="Exact Deck3 authored SVG palette gate; not a presentation certification")
    ap.add_argument("image", type=Path)
    ap.add_argument("--kind", choices=["scientific_diagram","authentic_photograph"], default="scientific_diagram")
    args=ap.parse_args()
    result = audit_svg(args.image) if args.image.suffix.lower()==".svg" else check_figure_source(args.image,args.kind)
    print(json.dumps(result,indent=2))
    raise SystemExit(1 if result["status"] in {"BLOCKED","COLOR_NOT_VERIFIED_RASTER_ONLY"} else 0)

if __name__=="__main__":
    main()
