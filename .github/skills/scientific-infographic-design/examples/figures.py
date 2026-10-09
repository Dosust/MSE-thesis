#!/usr/bin/env python3
"""Deterministic, ORIGINAL, editable vector examples: Chapter 1 Slides 3,4,5.

Run:
    python figures.py --out ./build
Produces 1600×900 SVGs; no measured or fitted curves, no fabricated constants.

Scientific evidence on these panels is always adjacent to the relevant claim.
The full technical system definition is controlled by the thesis repository.
These are schematic examples and NOT physical system validation.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from xml.etree import ElementTree as ET

W, H = 1600, 900
BG = "#FFFFFF"
BLACK = "#000000"
BLUE = "#0072B2"    # Power
GREEN = "#176B42"   # Electrified Transportation
HEAT = "#B4232C"    # External extreme heat
GRAY = "#555D66"    # neutral outline/notes (not fill)
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)


def el(tag: str, parent: ET.Element, **attrs: str) -> ET.Element:
    return ET.SubElement(parent, f"{{{SVG}}}{tag}", attrs)


def root(title: str, subtitle: str, foot: str) -> ET.Element:
    svg = ET.Element(f"{{{SVG}}}svg", {"width": str(W), "height": str(H),
        "viewBox": f"0 0 {W} {H}", "role": "img", "aria-label": title})
    el("rect", svg, x="0", y="0", width=str(W), height=str(H), fill=BG)
    defs = el("defs", svg)
    for name, color in (("black", BLACK), ("blue", BLUE), ("green", GREEN), ("red", HEAT)):
        marker = el("marker", defs, id=f"arrow-{name}", markerWidth="15",
            markerHeight="15", refX="12", refY="7.5",
            orient="auto", markerUnits="userSpaceOnUse")
        el("path", marker, d="M 0 0 L 14 7.5 L 0 15 Z", fill=color)
    txt(svg, 75, 76, title, 42, BLACK, weight="bold")
    txt(svg, 75, 122, subtitle, 24, BLACK)
    el("line", svg, x1="75", y1="149", x2="1525", y2="149",
       stroke="#555D66", **{"stroke-width": "2"})
    el("line", svg, x1="75", y1="811", x2="1525", y2="811",
       stroke="#555D66", **{"stroke-width": "2"})
    txt(svg, 76, 842, foot, 18, BLACK)
    txt(svg, 76, 875, "Original schematic, NOT case-qualified or measured. Figure semantics follow frozen thesis authority.", 16, GRAY)
    return svg


def txt(parent: ET.Element, x: float, y: float, content: str, size: int,
        color: str = BLACK, *, weight: str = "normal") -> None:
    node = el("text", parent, x=str(x), y=str(y), fill=color,
        **{"font-family": "Arial, Helvetica, sans-serif",
           "font-size": str(size), "font-weight": weight})
    node.text = content


def panel(parent: ET.Element, x: float, y: float, w: float, h: float, border: str,
          title: str, items: list[str], *, font: int = 25) -> None:
    el("rect", parent, x=str(x), y=str(y), width=str(w), height=str(h),
       rx="12", fill=BG, stroke=border, **{"stroke-width": "5"})
    txt(parent, x+26, y+48, title, 31, border, weight="bold")
    for i, item in enumerate(items):
        txt(parent, x+27, y+104+i*48, item, font, BLACK)


def arrow(parent: ET.Element, x1: float, y1: float, x2: float, y2: float,
          color: str, tip: str) -> None:
    el("line", parent, x1=str(x1), y1=str(y1), x2=str(x2), y2=str(y2),
       stroke=color, **{"stroke-width": "7", "marker-end": f"url(#arrow-{tip})"})


def frame_label(parent: ET.Element, x: float, y: float, label: str,
                color: str, size: int = 21) -> None:
    txt(parent, x, y, label, size, color, weight="bold")


SCOPE_TE = {
    "electrically propelled road vehicle",
    "rechargeable energy-storage system",
    "electric propulsion",
    "auxiliary electrical systems",
    "vehicle power-supply circuit",
    "electric-vehicle supply equipment",
    "physical charging connection",
    "required power-transfer communication/control",
}
REGISTER = {
    "03": {
        "question": "Who owns which components, and what crosses the P/T_e boundary?",
        "included_te": set(SCOPE_TE),
        "edges": [("P", "Te", "electricity supply", "ESTABLISHED GENERAL"),
                  ("Te", "P", "charging-load influence", "ESTABLISHED GENERAL")],
    },
    "04": {
        "question": "Does shared heat imply thermal coupling?",
        "edges": [("heat", "P", "external forcing", "ESTABLISHED GENERAL"),
                  ("heat", "Te", "external forcing", "ESTABLISHED GENERAL")],
    },
    "05": {
        "question": "What is required to qualify each candidate direction?",
        "candidate_directions": {"P_to_Te", "Te_to_P"},
        "required_gates": {"operational charging restriction", "grid-side AC input"},
    },
}


def check_registry() -> None:
    if not SCOPE_TE.issubset(REGISTER["03"]["included_te"]):
        raise AssertionError("Full T_e membership omitted")
    if any(source in ("P", "Te") and target in ("P", "Te")
           for source, target, _, _ in REGISTER["04"]["edges"]):
        raise AssertionError("Shared-heat scene must NOT claim a P<->T_e thermal effect")
    if REGISTER["05"]["candidate_directions"] != {"P_to_Te", "Te_to_P"}:
        raise AssertionError("Both candidate directions must be separate")
    if "grid-side AC input" not in REGISTER["05"]["required_gates"]:
        raise AssertionError("Never infer grid thermal effect from DC output alone")


def scene03() -> ET.Element:
    s = root("3 | Power and Electrified Transportation",
             "System membership and electrical interactions ≠ demonstrated thermal interdependency",
             "Sources: Qian et al. (2015); Diahovchenko et al. (2023); canonical T_e scope V1 §§1–4A.")
    panel(s, 85, 258, 608, 386, BLUE, "Power System (P)",
          ["Electricity supply/network", "Transformer and electrical states",
           "Operating constraints", "Electricity service: separate output"])
    panel(s, 905, 258, 608, 386, GREEN, "Electrified Transportation (T_e)",
          ["Electric road vehicle + RESS", "Propulsion + auxiliary electrics",
           "Vehicle supply circuit + EVSE", "Physical connector + transfer controls"], font=23)
    # The two arrows have DIFFERENT physical meanings: energy versus load effect.
    arrow(s, 708, 364, 888, 364, BLUE, "blue")
    frame_label(s, 737, 329, "Electricity supply", BLUE, 21)
    arrow(s, 889, 518, 709, 518, GREEN, "green")
    frame_label(s, 738, 568, "Charging-load influence", GREEN, 20)
    txt(s, 250, 714, "P and T_e are distinct systems. EVSE is within T_e, never a third infrastructure.", 24)
    txt(s, 250, 763, "Electrical connection / load effect alone cannot qualify a thermal interdependency.", 23)
    return s


def scene04() -> ET.Element:
    s = root("4 | External extreme heat: independent responses",
             "A common heat exposure is NOT evidence of a cross-system thermal mechanism",
             "Sources: IEEE Std C57.91-2025 (P thermal loading); Krama et al. (2026) (tested EVSE).")
    panel(s, 623, 177, 352, 92, HEAT, "EXTREME HEAT", [], font=22)
    panel(s, 102, 404, 608, 258, BLUE, "Power System (P)",
          ["Thermal-state evolution", "      ↓", "Heat-conditioned capability"], font=27)
    panel(s, 894, 404, 608, 258, GREEN, "Transportation System (T_e)",
          ["Thermal-state evolution", "      ↓", "Heat-conditioned capability"], font=26)
    arrow(s, 705, 275, 405, 393, HEAT, "red")
    arrow(s, 895, 275, 1189, 393, HEAT, "red")
    txt(s, 344, 335, "External forcing", 21, HEAT)
    txt(s, 1104, 335, "External forcing", 21, HEAT)
    txt(s, 268, 731, "NO CROSS-SYSTEM THERMAL ARROW: two responses ≠ interdependency.", 27, BLACK, weight="bold")
    return s


def step(s: ET.Element, x: float, y: float, title: str, body: str,
         color: str, width: int = 290) -> None:
    el("rect", s, x=str(x), y=str(y), width=str(width), height="128",
       rx="9", fill=BG, stroke=color, **{"stroke-width": "4"})
    txt(s, x+15, y+40, title, 22, color, weight="bold")
    txt(s, x+15, y+85, body, 19, BLACK)


def scene05() -> ET.Element:
    s = root("5 | Qualifying two candidate thermal pathways",
             "The two directions must pass independent mechanism and interface evidence gates",
             "Sources: Qian et al. (2015); Visakh & Selvan (2023); Krama et al. (2026); scope V1.")
    xs = [90, 467, 845, 1222]
    for y, color, direction, items in [
        (239, BLUE, "CANDIDATE P → T_e — NOT CASE-QUALIFIED", [
            ("Power thermal state", "Source condition"),
            ("Heat-conditioned limit", "Operating rule required"),
            ("Charging constraint", "Actual transfer required"),
            ("Mobility service", "Service metric required"),
        ]),
        (529, GREEN, "CANDIDATE T_e → P — NOT CASE-QUALIFIED", [
            ("EVSE thermal state", "Source condition"),
            ("Charging capability", "DC derating observed?"),
            ("Grid-side AC input", "MUST VERIFY separately"),
            ("Power thermal state", "Response evidence needed"),
        ]),
    ]:
        txt(s, 90, y-36, direction, 25, color, weight="bold")
        for i, (head, sub) in enumerate(items):
            step(s, xs[i], y, head, sub, color)
            if i < 3:
                arrow(s, xs[i]+300, y+65, xs[i+1]-28, y+65,
                      color, "blue" if color == BLUE else "green")
    txt(s, 92, 726, "GATE: source law + operating controls + interface behavior + time alignment + independent service evidence", 22)
    txt(s, 92, 769, "Arrow = hypothesized mechanism; CANDIDATE = evidentiary status, not a line style.", 21, BLACK)
    return s


def write_all(destination: Path) -> list[Path]:
    check_registry()
    destination.mkdir(parents=True, exist_ok=True)
    outputs = []
    for number, factory in (("03", scene03), ("04", scene04), ("05", scene05)):
        file = destination / f"chapter1_slide_{number}.svg"
        ET.ElementTree(factory()).write(file, encoding="utf-8", xml_declaration=True)
        # Parse after write; fail on malformed SVG instead of quietly delivering it.
        ET.parse(file)
        outputs.append(file)
    return outputs


def main() -> None:
    ap = argparse.ArgumentParser(description="Create three original conceptual, cited SVG infographics.")
    ap.add_argument("--out", default="build", help="Output directory")
    ns = ap.parse_args()
    for output in write_all(Path(ns.out)):
        print(f"CREATED {output}")
    print("PASS: SVG XML parse + semantic invariants. DOMAIN PHYSICS NOT VALIDATED.")


if __name__ == "__main__":
    main()
