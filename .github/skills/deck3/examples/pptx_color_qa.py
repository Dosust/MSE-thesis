#!/usr/bin/env python3
"""Deck3 exact-color OOXML audit for visible slide-authored PowerPoint objects.

This checks explicit slide shape colors/backgrounds, unresolved scheme/theme colors,
gradients and effects. It does not inspect raster figure pixels, science, figure
occupancy, contrast, PowerPoint playback, masters or photograph authenticity.
"""
from __future__ import annotations
import argparse
import json
import re
from collections import Counter
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET

PALETTE = Path(__file__).resolve().parents[1] / "references" / "DECK3_SRGB_PALETTE.json"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
SLIDE = re.compile(r"^ppt/slides/slide[0-9]+\\.xml$")

def check(path: str | Path) -> dict:
    path = Path(path)
    colors = json.loads(PALETTE.read_text(encoding="utf-8"))
    assert colors["color_space"] == "sRGB" and len(colors["colors"]) == 13
    allowed = {c["hex"][1:].upper() for c in colors["colors"].values()}
    white = colors["authored_surfaces"]["canvas"].lstrip("#").upper()
    errors, named, slides = [], Counter(), 0
    with ZipFile(path) as ppt:
        invalid_zip = ppt.testzip()
        if invalid_zip:
            errors.append("PPTX invalid ZIP member: " + invalid_zip)
        for name in ppt.namelist():
            if not SLIDE.match(name):
                continue
            slides += 1
            try:
                root = ET.fromstring(ppt.read(name))
            except ET.ParseError as ex:
                errors.append(name + ": malformed XML " + str(ex))
                continue
            bg = root.find("./" + P + "cSld/" + P + "bg")
            if bg is None:
                errors.append(name + ": explicit white slide background absent")
            else:
                bg_values = [c.attrib.get("val","").upper() for c in bg.iter(A+"srgbClr")]
                if bg_values != [white]:
                    errors.append(name + ": nonwhite or unresolved slide background " + repr(bg_values))
            for el in root.iter():
                if el.tag in {A+"gradFill", A+"effectLst", A+"effectDag", A+"pattFill"}:
                    if el.tag != A+"effectLst" or len(el):
                        errors.append(name + ": prohibited gradient, shadow/effect or pattern")
                if el.tag == A+"schemeClr":
                    errors.append(name + ": unresolved theme/schemeClr cannot certify exact sRGB")
                if el.tag == A+"srgbClr":
                    v = el.attrib.get("val","").upper()
                    named[v] += 1
                    if v not in allowed:
                        errors.append(name + ": off-palette authored sRGB " + v)
    if slides < 1:
        errors.append("No slide XML detected")
    return {"path":str(path), "status":"EXPLICIT_SLIDE_COLOR_SOURCE_PASS_NOT_RENDER_CERTIFIED" if not errors else "BLOCKED",
            "slides":slides,"visible_srgb_counts":dict(named),"errors":errors,
            "limits":["Does not audit raster imagery, theme master colors that are not applied, projected readability, physical semantics, or playback",
                     "Does not infer that any colored native filled shape is semantically valid."]}

def main():
    pa=argparse.ArgumentParser(description=__doc__)
    pa.add_argument("pptx",type=Path)
    args=pa.parse_args()
    result=check(args.pptx)
    print(json.dumps(result,indent=2))
    raise SystemExit(bool(result["errors"]))

if __name__=="__main__":
    main()
