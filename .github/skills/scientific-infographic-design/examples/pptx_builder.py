#!/usr/bin/env python3
"""Minimal, original, fully editable Chapter 1 infographic PPTX builder.

Creates three example slides (not a replacement for the 16-slide thesis deck).
Scientific source labels are visible on each slide. Layout is schematic.
Requires: python-pptx (pip install python-pptx)

Run: python pptx_builder.py --out prototype_editable.pptx
"""
from __future__ import annotations

# Deck3 v1.8: source-only conceptual prototypes. A saved/rendered graphic is NOT a
# trace-registered scientific mechanism. Supply a separately reviewed
# same-stem <image>.trace.json using deck3/examples/mechanism_trace_qa.py
# before requesting scientific mechanism certification. Do not infer laws,
# variables, evidence or bidirectional thermal causality from these shapes.


import argparse
import json
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

# Canonical authored sRGB colors; fail closed if not found, never substitute.
_PALETTE_FILE = Path(__file__).resolve().parents[2] / "deck3" / "references" / "DECK3_SRGB_PALETTE.json"
_COLOR_REGISTRY = json.loads(_PALETTE_FILE.read_text(encoding="utf-8"))
assert len(_COLOR_REGISTRY["colors"]) == 13, "Review Deck3 palette authority"
def authored_rgb(token: str) -> RGBColor:
    return RGBColor(*_COLOR_REGISTRY["colors"][token]["rgb"])

WHITE = authored_rgb("white")
BLACK = authored_rgb("black")
BLUE = authored_rgb("blue")
GREEN = authored_rgb("forest_green")
RED = authored_rgb("deep_red")
GRAY = authored_rgb("graphite")
W, H = 13.333, 7.5


def textbox(slide, x, y, w, h, text, size=18, color=BLACK, bold=False):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    frame = shape.text_frame
    frame.clear()
    frame.word_wrap = True
    p = frame.paragraphs[0]
    p.text = text
    p.font.name = "Arial"
    p.font.size = Pt(size)
    p.font.bold = bold
    p.font.color.rgb = color
    return shape


def rectangle(slide, x, y, w, h, border, thickness=2.25):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = WHITE
    shp.line.color.rgb = border
    shp.line.width = Pt(thickness)
    return shp


def vertical_arrow(slide, x, y, color):
    shp = slide.shapes.add_shape(MSO_SHAPE.DOWN_ARROW,
                                Inches(x), Inches(y), Inches(.48), Inches(.69))
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.color.rgb = color
    return shp


def horizontal_arrow(slide, x, y, color, direction="right", w=.65):
    typ = MSO_SHAPE.LEFT_ARROW if direction == "left" else MSO_SHAPE.RIGHT_ARROW
    shp = slide.shapes.add_shape(typ, Inches(x), Inches(y), Inches(w), Inches(.33))
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.color.rgb = color
    return shp


def standard_slide(prs, title, subtitle, source, note):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = WHITE
    textbox(slide, .6, .3, 12.15, .65, title, 30, BLACK, True)
    textbox(slide, .6, .98, 12.15, .52, subtitle, 17, GRAY)
    textbox(slide, .6, 6.91, 12.1, .26, source, 10, BLACK)
    textbox(slide, .6, 7.19, 12.1, .18,
            "Original schematic, not measured and not case-validated.", 8, GRAY)
    # python-pptx supports editable speaker notes on compatible versions.
    try:
        tf = slide.notes_slide.notes_text_frame
        tf.text = note
    except (AttributeError, ValueError):
        pass
    return slide


def make_slide3(prs):
    s = standard_slide(
        prs,
        "3 | Power and Electrified Transportation",
        "Electrical interaction is not itself a qualified thermal interdependency.",
        "Qian et al. (2015); Diahovchenko et al. (2023); Canonical T_e Scope V1 §§1–4A.",
        "P and T_e have separate physical boundaries. EVSE, connector, vehicle, "
        "RESS, propulsion, auxiliary electrics and transfer controls belong to T_e. "
        "Power→T_e is electrical supply; the reverse green arrow is charging-load influence, not V2G.")
    rectangle(s, .55, 2.02, 5.25, 3.43, BLUE)
    rectangle(s, 7.52, 2.02, 5.25, 3.43, GREEN)
    textbox(s, .85, 2.36, 4.45, .4, "Power System (P)", 23, BLUE, True)
    for i, value in enumerate(("Electricity supply/network",
                               "Transformer and electrical states",
                               "Operating constraints")):
        textbox(s, .86, 3.04+i*.59, 4.6, .42, value, 18)
    textbox(s, 7.82, 2.36, 4.55, .4, "Electrified Transportation (T_e)", 22, GREEN, True)
    for i, value in enumerate(("Vehicle + RESS",
                               "Propulsion + auxiliary electrical systems",
                               "Vehicle supply circuit + EVSE",
                               "Charging connector + transfer controls")):
        textbox(s, 7.84, 3.01+i*.52, 4.6, .38, value, 17)
    horizontal_arrow(s, 6.06, 3.22, BLUE, "right", 1.16)
    textbox(s, 5.94, 2.70, 1.35, .35, "Electricity supply", 12, BLUE)
    horizontal_arrow(s, 6.05, 4.58, GREEN, "left", 1.16)
    textbox(s, 5.91, 4.95, 1.43, .35, "Charging-load effect", 11, GREEN)
    textbox(s, .85, 5.83, 11.6, .45,
            "System membership ≠ active mathematical model ≠ mobility service.", 18, BLACK, True)


def make_slide4(prs):
    s = standard_slide(
        prs,
        "4 | Extreme heat: independent system responses",
        "Common external forcing does not automatically establish cross-system thermal coupling.",
        "IEEE C57.91-2025 (transformer loading); Krama et al. (2026) (one charger case).",
        "The figure deliberately contains no thermal Power–Transportation cross-system arrow. "
        "Any exact active thermal states and derating rules remain case- and evidence-dependent.")
    rectangle(s, 5.04, 1.69, 3.25, .76, RED)
    textbox(s, 5.49, 1.87, 2.7, .4, "EXTERNAL EXTREME HEAT", 18, RED, True)
    vertical_arrow(s, 3.12, 2.71, RED)
    vertical_arrow(s, 9.75, 2.71, RED)
    rectangle(s, .73, 3.61, 5.62, 2.28, BLUE)
    rectangle(s, 6.98, 3.61, 5.62, 2.28, GREEN)
    textbox(s, 1.04, 3.95, 4.75, .45, "Power thermal state", 22, BLUE, True)
    textbox(s, 1.05, 4.76, 4.82, .8, "Heat-conditioned capability / constraint", 18)
    textbox(s, 7.28, 3.95, 4.96, .45, "Transportation thermal state", 22, GREEN, True)
    textbox(s, 7.30, 4.76, 4.89, .8, "Heat-conditioned capability / constraint", 18)
    textbox(s, 2.1, 6.21, 9.6, .47,
            "NO P ↔ T_e THERMAL ARROW: shared exposure ≠ interdependency", 20, BLACK, True)


def _candidate_step(s, x, y, w, title, sub, color):
    rectangle(s, x, y, w, 1.10, color, 1.9)
    textbox(s, x+.14, y+.11, w-.20, .38, title, 17, color, True)
    textbox(s, x+.14, y+.54, w-.20, .44, sub, 12, BLACK)


def make_slide5(prs):
    s = standard_slide(
        prs,
        "5 | Candidate directions: qualify each mechanism",
        "Directional thermal effects need actual source, interface and receiver evidence.",
        "Qian et al. (2015); Visakh & Selvan (2023); Krama et al. (2026); canonical scope.",
        "Two separate CANDIDATE lanes; source-level prior art does not prove the integrated mechanisms. "
        "AC-side input behavior must be documented before translating EVSE DC derating into transformer loading.")
    xs, width = [.64, 3.83, 7.02, 10.21], 2.55
    rows = [
        (2.04, BLUE, "CANDIDATE P → T_e — NOT CASE-QUALIFIED",
         [("P thermal state", "source"),
          ("Power constraint", "operating rule"),
          ("Charging restriction", "actual interface"),
          ("Mobility service", "requirement")]),
        (4.42, GREEN, "CANDIDATE T_e → P — NOT CASE-QUALIFIED",
         [("EVSE thermal state", "source"),
          ("Charging capability", "device behavior"),
          ("Grid-side AC input", "must verify"),
          ("Power thermal state", "response")]),
    ]
    for y, color, heading, items in rows:
        textbox(s, .7, y-.46, 11.8, .40, heading, 17, color, True)
        for i, (main, sub) in enumerate(items):
            _candidate_step(s, xs[i], y, width, main, sub, color)
            if i < 3:
                horizontal_arrow(s, xs[i]+width+.10, y+.42, color, "right", .40)
    textbox(s, .75, 6.08, 11.7, .53,
            "Gate: thermal source → operating rule → actual interface → receiver → defined service", 18)


def build(path):
    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)
    make_slide3(prs)
    make_slide4(prs)
    make_slide5(prs)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(path))
    # Smoke check the archived deck can be read and contains editable shapes.
    opened = Presentation(str(path))
    assert len(opened.slides) == 3
    assert all(len(s.shapes) >= 12 for s in opened.slides)
    assert all(not any(sh.shape_type == 13 for sh in s.shapes) for s in opened.slides)
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="example_editable.pptx")
    ns = ap.parse_args()
    print(f"PASS: wrote editable prototype {build(ns.out)}")
    print("SOURCE-ONLY: valid editable PPTX is NOT a trace-registered or physically validated mechanism.")


if __name__ == "__main__":
    main()
