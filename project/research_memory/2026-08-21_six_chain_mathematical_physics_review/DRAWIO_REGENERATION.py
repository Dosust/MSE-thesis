#!/usr/bin/env python3
"""
Rebuild the six interacting scientific chains as an editable draw.io file.

Inputs:
    CHAIN_LAYER_MATRIX.csv

Outputs:
    Six_Chain_Ontology_Regenerated.drawio

Scientific rules:
- Six interacting chains, not one giant causal arrow.
- Mathematics is cross-cutting, not a seventh physical chain.
- Optimization is cross-cutting, not a lifecycle stage.
- Topology != interdependency != interface mechanism.
- Physical state != functionality != service != societal consequence.
"""

from pathlib import Path
import csv
import html
import xml.etree.ElementTree as ET
from xml.dom import minidom

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "CHAIN_LAYER_MATRIX.csv"
OUT_PATH = HERE / "Six_Chain_Ontology_Regenerated.drawio"

CHAIN_META = {
    "I":  {"title": "PHYSICAL SYSTEM",        "question": "What is the system?",                 "color": "#1F65B5", "light": "#EDF5FF"},
    "II": {"title": "OBSERVATION & INFERENCE","question": "What do we know?",                   "color": "#15858E", "light": "#EDFBFB"},
    "III":{"title": "STRESS & CONSEQUENCE",   "question": "What happens under stress?",          "color": "#C7372F", "light": "#FFF0EF"},
    "IV": {"title": "VIABILITY & RESPONSE",   "question": "Can the system survive and recover?", "color": "#6E44AD", "light": "#F6F0FF"},
    "V":  {"title": "ENGINEERING LIFECYCLE",  "question": "What can engineers do?",              "color": "#39854A", "light": "#F0FAF2"},
    "VI": {"title": "SOCIETAL DECISION",      "question": "What should society choose?",         "color": "#B77A00", "light": "#FFF8E8"},
}

DISPLAY_LAYERS = {
    "I":  ["Physical laws & constitutive foundations", "System representation & topology",
           "Interdependencies & interfaces", "Dynamics", "Cascades"],
    "II": ["Measurement, sensing & monitoring", "Observability & data quality",
           "Identification / inverse problems", "State estimation",
           "Uncertainty quantification", "Prediction"],
    "III":["Hazard", "Exposure", "Vulnerability / fragility", "Damage / failure",
           "Interdependent cascade", "Functional capacity loss", "Service loss",
           "Societal consequence"],
    "IV": ["Preparedness / absorption / robustness", "Viability", "Reachability",
           "Service continuity", "Resilience metrics", "Recovery / restoration",
           "Adaptive / feedback control"],
    "V":  ["Requirements", "Design & architecture", "Deployment / commissioning",
           "Operation & dispatch", "Deterioration / aging",
           "Maintenance / repair / replacement",
           "Planning / capacity expansion / investment timing",
           "Adaptation / transformation", "Decommissioning / circularity"],
    "VI": ["Sustainability & lifecycle impacts", "Equity / accessibility / justice",
           "Economics / finance / value", "Governance / strategic interaction",
           "Trade-offs", "Decision under uncertainty", "Implementation",
           "Learning / updating"],
}

FORMULAS = {
    "Physical laws & constitutive foundations": "∂ρ/∂t + ∇·J = s",
    "System representation & topology": "G=(V,E), L=D−A",
    "Interdependencies & interfaces": "yᵢⱼ=gᵢⱼ(xᵢ,xⱼ;θᵢⱼ,τᵢⱼ)",
    "Dynamics": "ẋᵢ=fᵢ(xᵢ)+Σⱼgᵢⱼ(xᵢ,xⱼ)",
    "Cascades": "Lᵢ>Cᵢ ⇒ failure propagation",
    "Measurement, sensing & monitoring": "yₖ=h(xₖ,θ)+εₖ",
    "Observability & data quality": "rank(𝒪)=n",
    "Identification / inverse problems": "π(θ|y)∝p(y|θ)π₀(θ)",
    "State estimation": "p(xₖ|y₁:ₖ)",
    "Uncertainty quantification": "Σθ, Σx, posterior intervals",
    "Prediction": "p(xₖ₊₁|y₁:ₖ)",
    "Hazard": "P(H>h)",
    "Exposure": "E(s,t)",
    "Vulnerability / fragility": "P(D≥d|H=h)",
    "Damage / failure": "P_f=P[g(X,H)≤0]",
    "Interdependent cascade": "P∞(p,q), overload/percolation",
    "Functional capacity loss": "X(t)→F(t)",
    "Service loss": "L_s=1−S(t)/S₀",
    "Societal consequence": "E[C]=∫C(ℓ)p(ℓ)dℓ",
    "Preparedness / absorption / robustness": "Q(t_d⁺)/Q₀",
    "Viability": "Viab_K={x₀:∃u, x(t)∈K}",
    "Reachability": "𝓡(T)={x(T)}",
    "Service continuity": "S_g(t)≥S_g^min",
    "Resilience metrics": "L_R=∫[1−Q(t)]dt",
    "Recovery / restoration": "R(t)=[φ(t)−φ(t_d)]/[φ(t₀)−φ(t_d)]",
    "Adaptive / feedback control": "∂ₜV+min_u max_d ∇V·f=0",
    "Requirements": "g(x)≤0, h(x)=0",
    "Design & architecture": "x*=argmin J_d(x)",
    "Deployment / commissioning": "design→verified operational asset",
    "Operation & dispatch": "u*=argmin∫c(x,u)dt",
    "Deterioration / aging": "λ(t)=f_T(t)/(1−F_T(t))",
    "Maintenance / repair / replacement": "π*=argmin E[Σ c(X_t,a_t)]",
    "Planning / capacity expansion / investment timing": "max E[NPV(a,ω)]",
    "Adaptation / transformation": "a*=argmin_a max_ω L(a,ω)",
    "Decommissioning / circularity": "reverse/material-flow optimization",
    "Sustainability & lifecycle impacts": "J=[J_env,J_econ,J_soc]",
    "Equity / accessibility / justice": "S_g(t)≥S_g^min",
    "Economics / finance / value": "NPV=Σ CF_t/(1+r)^t",
    "Governance / strategic interaction": "game / mechanism / institution",
    "Trade-offs": "Pareto set 𝒫",
    "Decision under uncertainty": "a*=argmax Σ_m w_m u_m(a)",
    "Implementation": "decision→policy/finance/operations",
    "Learning / updating": "π_{t+1}(θ)∝L(D|θ)π_t(θ)",
}

COUPLINGS = [
    ("I", "II", "state ↔ evidence"),
    ("II", "III", "forecast ↔ stress"),
    ("III", "IV", "loss ↔ viability"),
    ("IV", "V", "control ↔ operation"),
    ("V", "VI", "engineering options ↔ societal choice"),
]

def load_rows():
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def add_vertex(root, cid, value, style, x, y, w, h):
    c = ET.SubElement(root, "mxCell", {
        "id": str(cid), "value": value, "style": style,
        "parent": "1", "vertex": "1"
    })
    ET.SubElement(c, "mxGeometry", {
        "x": str(x), "y": str(y), "width": str(w), "height": str(h), "as": "geometry"
    })
    return str(cid)

def add_edge(root, cid, source, target, color, dashed=False):
    style = (
        "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;"
        f"strokeColor={color};strokeWidth=2.5;endArrow=block;endFill=1;"
    )
    if dashed:
        style += "dashed=1;dashPattern=8 6;"
    c = ET.SubElement(root, "mxCell", {
        "id": str(cid), "style": style, "parent": "1",
        "source": source, "target": target, "edge": "1"
    })
    ET.SubElement(c, "mxGeometry", {"relative": "1", "as": "geometry"})

def main():
    rows = load_rows()
    by_chain = {}
    for row in rows:
        by_chain.setdefault(row["chain"], {})[row["layer"]] = row

    mxfile = ET.Element("mxfile", {"host":"app.diagrams.net","type":"device"})
    diagram = ET.SubElement(mxfile, "diagram", {
        "id":"six-chain-reproducible", "name":"Six Chain Ontology"
    })
    model = ET.SubElement(diagram, "mxGraphModel", {
        "grid":"1","gridSize":"10","page":"1","pageScale":"1",
        "pageWidth":"5400","pageHeight":"2800","math":"0"
    })
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id":"0"})
    ET.SubElement(root, "mxCell", {"id":"1","parent":"0"})

    cid = 2
    add_vertex(
        root, cid,
        "<b>SIX INTERACTING SCIENTIFIC CHAINS FOR SUSTAINABLE & RESILIENT INFRASTRUCTURE</b>"
        "<br><font size='12'>Literature-grounded ontology; not one giant causal pipeline</font>",
        "text;html=1;align=center;verticalAlign=middle;fontFamily=Georgia;fontSize=24;fontColor=#10243E;",
        80, 30, 5100, 90
    ); cid += 1

    add_vertex(
        root, cid,
        "<b>CROSS-CUTTING MATHEMATICS:</b> ODE/PDE/DAE · networks · probability/UQ · "
        "Bayesian inverse problems · optimization · control · viability/reachability · "
        "game theory · numerics · AI/ML · MCDA/DMDU",
        "rounded=1;html=1;align=center;verticalAlign=middle;fillColor=#F6F8FB;"
        "strokeColor=#94A3B8;fontSize=14;fontColor=#334155;",
        250, 130, 3950, 55
    ); cid += 1

    row_y = 220
    row_h = 340
    gap_y = 18
    x_left = 60
    left_w = 570
    content_x = 680
    content_w = 3920
    coupling_x = 4660
    coupling_w = 600

    chain_endpoints = {}

    for chain in ["I","II","III","IV","V","VI"]:
        meta = CHAIN_META[chain]
        y = row_y + ({"I":0,"II":1,"III":2,"IV":3,"V":4,"VI":5}[chain])*(row_h+gap_y)

        add_vertex(
            root, cid, "",
            f"rounded=1;arcSize=12;fillColor={meta['light']};strokeColor={meta['color']};strokeWidth=2;",
            x_left, y, 4540, row_h
        ); cid += 1

        add_vertex(
            root, cid,
            f"<b><font size='24'>{chain}. {meta['title']}</font></b><br>"
            f"<i>{meta['question']}</i>",
            f"text;html=1;align=left;verticalAlign=top;fontFamily=Georgia;fontSize=18;"
            f"fontColor={meta['color']};",
            90, y+55, left_w-60, 110
        ); cid += 1

        selected = [x for x in DISPLAY_LAYERS[chain] if x in by_chain.get(chain, {})]
        n = len(selected)
        node_gap = 18
        node_w = (content_w - node_gap*(n-1))/n
        prev = None
        first = None

        for j, layer in enumerate(selected):
            row = by_chain[chain][layer]
            x = content_x + j*(node_w+node_gap)
            refs = html.escape(row["representative_anchors"])
            math = html.escape(FORMULAS.get(layer, ""))
            label = (
                f"<b>{html.escape(layer)}</b><br>"
                f"<font size='10'>{html.escape(row['core_question'])}</font><br><br>"
                f"<font face='Georgia'><b>{math}</b></font><br>"
                f"<font size='9' color='#475569'>{refs}</font>"
            )
            nid = add_vertex(
                root, cid, label,
                f"rounded=1;arcSize=9;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
                f"spacing=7;fillColor=#FFFFFF;strokeColor={meta['color']};strokeWidth=1.7;"
                f"fontColor=#172033;",
                x, y+52, node_w, 225
            )
            cid += 1
            if first is None:
                first = nid
            if prev is not None:
                add_edge(root, cid, prev, nid, meta["color"])
                cid += 1
            prev = nid

        chain_endpoints[chain] = (first, prev)

        feedback = {
            "I":"Adaptation changes structure, parameters and interface laws.",
            "II":"Learning updates priors, model structure and uncertainty.",
            "III":"Observed failures recalibrate hazard/fragility/cascade models.",
            "IV":"Recovery evidence updates viability boundaries and control.",
            "V":"Operational experience updates maintenance/planning/adaptation.",
            "VI":"Outcomes update values, equity weights, governance and policy.",
        }[chain]
        add_vertex(
            root, cid,
            f"<b>FEEDBACK</b><br><font size='10'>{feedback}</font>",
            f"rounded=1;html=1;align=center;verticalAlign=middle;fillColor=#FFFFFF;"
            f"strokeColor={meta['color']};dashed=1;fontColor={meta['color']};",
            coupling_x, y+105, coupling_w, 110
        ); cid += 1

    for a,b,label in COUPLINGS:
        src = chain_endpoints[a][1]
        tgt = chain_endpoints[b][0]
        add_edge(root, cid, src, tgt, "#64748B", dashed=True)
        cid += 1

    xml = minidom.parseString(ET.tostring(mxfile, encoding="utf-8")).toprettyxml(indent="  ")
    OUT_PATH.write_text(xml, encoding="utf-8")
    print(OUT_PATH)

if __name__ == "__main__":
    main()
