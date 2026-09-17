#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from xml.etree import ElementTree as ET

TARGET = {
    "nodes": 50109,
    "edges": 118289,
    "signalized_junctions": 914,
    "road_length_km": 28216.0,
    "lane_length_km": 30625.0,
}

PUBLISHED_BOUNDS = {
    "south": 35.894145,
    "west": -80.198958,
    "north": 36.410277,
    "east": -79.157255,
}


def finite(x: float) -> bool:
    return math.isfinite(float(x))


def audit_network(path: Path) -> dict:
    edges = 0
    nodes = 0
    signals = 0
    road_length_m = 0.0
    lane_length_m = 0.0
    parse_ok = True
    error = None

    try:
        for _, elem in ET.iterparse(path, events=("end",)):
            if elem.tag == "edge":
                eid = elem.attrib.get("id", "")
                function = elem.attrib.get("function", "")
                if eid.startswith(":") or function == "internal":
                    elem.clear()
                    continue
                edges += 1
                lanes = [x for x in list(elem) if x.tag == "lane"]
                lengths = []
                for lane in lanes:
                    try:
                        length = float(lane.attrib["length"])
                    except (KeyError, ValueError):
                        continue
                    if finite(length) and length >= 0:
                        lengths.append(length)
                        lane_length_m += length
                # SUMO edges represent roads/road parts.  Use one representative
                # lane length for edge road length; all lane lengths contribute to
                # lane length.  If lengths differ, use the maximum and disclose it.
                if lengths:
                    road_length_m += max(lengths)
            elif elem.tag == "junction":
                jid = elem.attrib.get("id", "")
                if jid.startswith(":"):
                    elem.clear()
                    continue
                nodes += 1
                if elem.attrib.get("type") == "traffic_light":
                    signals += 1
            elem.clear()
    except (ET.ParseError, OSError) as exc:
        parse_ok = False
        error = str(exc)

    observed = {
        "nodes": nodes,
        "edges": edges,
        "signalized_junctions": signals,
        "road_length_km": road_length_m / 1000.0,
        "lane_length_km": lane_length_m / 1000.0,
    }
    discrepancy = {
        k: (observed[k] - TARGET[k]) if parse_ok else None
        for k in TARGET
    }

    discrete_match = (
        parse_ok
        and nodes == TARGET["nodes"]
        and edges == TARGET["edges"]
        and signals == TARGET["signalized_junctions"]
    )

    # Publication gives integer-km totals without an explicit rounding rule.
    # Report length discrepancies; do not convert them into an arbitrary pass/fail.
    classification = (
        "GREENEVT_BENCHMARK_MATCH_CANDIDATE"
        if discrete_match
        else "RECONSTRUCTED_SURROGATE_NOT_GREENEVT_EQUIVALENT"
    )

    return {
        "status": classification,
        "parse_ok": parse_ok,
        "error": error,
        "published_bounds": PUBLISHED_BOUNDS,
        "published_targets": TARGET,
        "observed": observed,
        "discrepancy": discrepancy,
        "gates": {
            "T2_node_count_exact": parse_ok and nodes == TARGET["nodes"],
            "T3_edge_count_exact": parse_ok and edges == TARGET["edges"],
            "T4_signalized_junction_count_exact": parse_ok and signals == TARGET["signalized_junctions"],
            "T5_road_length_reported_not_thresholded": parse_ok,
            "T6_lane_length_reported_not_thresholded": parse_ok,
            "T7_xml_parse": parse_ok,
        },
        "selection_authorized": False,
        "claim_boundary": (
            "Aggregate benchmark agreement cannot establish byte or edge-level equivalence. "
            "This validator never authorizes feeder selection by itself."
        ),
    }


def main() -> None:
    p = argparse.ArgumentParser(description="Validate a reconstructed SUMO network against published GreenEVT invariants")
    p.add_argument("--network", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    result = audit_network(Path(args.network))
    Path(args.out).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["parse_ok"] else 2)


if __name__ == "__main__":
    main()
