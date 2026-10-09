#!/usr/bin/env python3
"""Deck3 scientific-geometry/manifest validator (structural only, NOT playback/physics)."""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path

PALETTE_PATH = Path(__file__).resolve().parents[2] / "references" / "DECK3_SRGB_PALETTE.json"

def load_palette(path: Path = PALETTE_PATH) -> dict:
    if not path.is_file():
        raise FileNotFoundError(f"Missing authoritative Deck3 color registry: {path}")
    p = json.loads(path.read_text(encoding="utf-8"))
    if p.get("color_space") != "sRGB" or p.get("channel_bits") != 8:
        raise ValueError("Expected canonical 8-bit sRGB")
    if len(p.get("colors", {})) != 13:
        raise ValueError("Canonical 13-color registry changed: explicit review required")
    if any(x != "#FFFFFF" for x in p.get("authored_surfaces", {}).values()):
        raise ValueError("Canonical palette defines a nonwhite authored interior")
    return p

def contrast_on_white(value: str) -> float:
    rgb = [int(value[i:i + 2], 16) / 255.0 for i in (1, 3, 5)]
    lin = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in rgb]
    return 1.05 / (0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2] + 0.05)

def bezier(p0, p1, p2, p3, t):
    if not 0 <= t <= 1:
        raise ValueError("t must lie in [0,1]")
    if not all(math.isfinite(v) for p in (p0, p1, p2, p3) for v in p):
        raise ValueError("nonfinite Bezier point")
    return tuple((1 - t) ** 3 * p0[i] + 3 * (1 - t) ** 2 * t * p1[i] +
                 3 * (1 - t) * t ** 2 * p2[i] + t ** 3 * p3[i] for i in range(2))

def bezier_head_angle(p2, p3):
    dx, dy = p3[0] - p2[0], p3[1] - p2[1]
    if not all(math.isfinite(v) for v in (dx, dy)) or math.hypot(dx, dy) < 1e-12:
        raise ValueError("degenerate endpoint tangent")
    return math.degrees(math.atan2(dy, dx))

def validate(doc: dict, palette: dict | None = None) -> list[str]:
    p = palette or load_palette()
    colors = p["colors"]
    errors = []
    objects = doc.get("objects", [])
    identifiers = [o.get("id") for o in objects]
    known = set(identifiers)
    if len(known) != len(identifiers):
        errors.append("duplicate object IDs")
    if any(not i for i in identifiers):
        errors.append("missing object ID")
    if doc.get("canvas_hex") != "#FFFFFF" or doc.get("panel_fill_hex") != "#FFFFFF":
        errors.append("non-white diagram/slide interior")
    if any(doc.get(flag) for flag in ("gradient", "shadow", "texture")):
        errors.append("forbidden gradient/shadow/texture")
    for token in doc.get("authored_color_tokens", []):
        if token not in colors:
            errors.append("unapproved authored color: " + str(token))
    allowed_status = {"OPEN", "CANDIDATE", "THESIS_DEFINED", "ESTABLISHED", "QUALIFIED"}
    for obj in objects:
        oid = str(obj.get("id"))
        if not obj.get("class") or not obj.get("parent_system") or not obj.get("alt"):
            errors.append("object lacks class/parent_system/alt: " + oid)
        if obj.get("evidence_status") not in allowed_status:
            errors.append("unknown object evidence status: " + oid)
        if obj.get("fill_hex", "#FFFFFF") != "#FFFFFF":
            errors.append("non-white authored object fill: " + oid)
        token = obj.get("color_token")
        if token is not None:
            if token not in colors:
                errors.append("unapproved object color: " + oid)
            else:
                hex_value = colors[token]["hex"]
                if obj.get("color_hex", hex_value) != hex_value:
                    errors.append("object color differs from canonical exact sRGB: " + oid)
                role = obj.get("color_role", "essential_text")
                if role not in {"essential_text", "essential_graphic", "nonessential_accent"}:
                    errors.append("unknown color role: " + oid)
                elif role != "nonessential_accent":
                    min_ratio = (p["contrast"]["normal_text_min"] if role == "essential_text"
                                 else p["contrast"]["essential_nontext_min"])
                    if contrast_on_white(hex_value) < min_ratio:
                        errors.append("low-contrast critical object color: " + oid)
    for r in doc.get("relations", []):
        rid = str(r.get("id"))
        if r.get("from") not in known or r.get("to") not in known:
            errors.append("invalid arrow endpoint: " + rid)
        if not r.get("meaning") or not r.get("direction"):
            errors.append("missing physical/methodological relation meaning: " + rid)
        token = r.get("stroke_color_token")
        if token is not None:
            if token not in colors:
                errors.append("unapproved arrow color: " + rid)
            else:
                rgb = colors[token]["hex"]
                if r.get("stroke_hex", rgb) != rgb:
                    errors.append("arrow color differs from canonical exact sRGB: " + rid)
                if contrast_on_white(rgb) < p["contrast"]["essential_nontext_min"]:
                    errors.append("low-contrast essential arrow: " + rid)
        if r.get("relation_type") == "candidate_dependency" and r.get("evidence_status") not in ("OPEN", "CANDIDATE"):
            errors.append("candidate arrow promoted to established without evidence: " + rid)
    animation = doc.get("animation", {})
    if (animation.get("effect") != "Appear" or animation.get("trigger") != "OnClick" or
            animation.get("persist") is not True or animation.get("automatic_advance") is not False):
        errors.append("animation contract differs from OnClick/Appear/persistent/no auto")
    groups = animation.get("click_groups", [])
    clicks = [g.get("click") for g in groups]
    if clicks != list(range(1, len(groups) + 1)):
        errors.append("click group sequence must be 1,2,...")
    names = [g.get("id") for g in groups]
    if len(set(names)) != len(names) or any(not n for n in names):
        errors.append("duplicate or absent animation group ID")
    for g in groups:
        if any(x not in known for x in g.get("object_ids", [])):
            errors.append("click group references unknown shape")
        if not g.get("object_ids") and not g.get("note"):
            errors.append("empty click group lacks explicit pending-production gate")
    if doc.get("core_copy", {}).get("no_visible_authoring_labels") is not True:
        errors.append("authoring headings may appear on slides")
    return errors

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    args = ap.parse_args()
    doc = json.loads(args.manifest.read_text(encoding="utf-8"))
    problems = validate(doc)
    print(json.dumps({"structural_status": "PASS" if not problems else "FAIL",
                      "palette_source": str(PALETTE_PATH),
                      "checked_objects": len(doc.get("objects", [])),
                      "checked_relations": len(doc.get("relations", [])),
                      "click_groups": len(doc.get("animation", {}).get("click_groups", [])),
                      "animation_playback_verified": False,
                      "physical_model_validated": False, "errors": problems}, indent=2))
    raise SystemExit(1 if problems else 0)

if __name__ == "__main__":
    main()
