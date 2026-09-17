#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser(description="Render the H1 Level-2 reduced spatial twin on the authentic GreenEVT SUMO geometry.")
    ap.add_argument("--case", required=True)
    ap.add_argument("--greenevt", required=True)
    ap.add_argument("--out", default="level2_map.png")
    ap.add_argument("--dpi", type=int, default=300)
    args = ap.parse_args()

    case = json.loads(Path(args.case).read_text())
    if case.get("mode") != "realistic":
        raise SystemExit("Map rendering is reserved for realistic mode. Preview geometry is intentionally not presented as Greensboro.")

    try:
        import matplotlib.pyplot as plt
        import sumolib
    except ImportError as e:
        raise SystemExit("Install the GreenEVT requirements (matplotlib, sumolib) before rendering") from e

    net_path = Path(args.greenevt) / "data/sumo_network/greensboro.net.xml"
    net = sumolib.net.readNet(str(net_path))
    wanted = {str(e["id"]) for e in case.get("road_edges", [])}

    fig, ax = plt.subplots(figsize=(12, 10))
    for edge in net.getEdges():
        if edge.getID() not in wanted:
            continue
        shape = edge.getShape()
        if len(shape) >= 2:
            x = [p[0] for p in shape]
            y = [p[1] for p in shape]
            ax.plot(x, y, linewidth=0.7, alpha=0.7)

    bx, by = [], []
    for bus in case.get("power_buses", []):
        x, y = net.convertLonLat2XY(float(bus["lon"]), float(bus["lat"]))
        bx.append(x); by.append(y)
    ax.scatter(bx, by, s=16, zorder=3, label="selected SMART-DS buses")
    ax.set_aspect("equal", adjustable="datalim")
    ax.set_axis_off()
    ax.set_title("H1 Level 2 — Greensboro realistic synthetic spatial twin\nselected SMART-DS buses + OSM/SUMO roads")
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(args.out, dpi=args.dpi, bbox_inches="tight")
    print(args.out)


if __name__ == "__main__":
    main()
