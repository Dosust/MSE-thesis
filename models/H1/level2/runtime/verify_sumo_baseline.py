#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
from pathlib import Path
from xml.etree import ElementTree as ET


def passenger_allowed(attrs: dict[str, str]) -> bool:
    allow = set(attrs.get("allow", "").split())
    disallow = set(attrs.get("disallow", "").split())
    return ("passenger" not in disallow) and (not allow or "passenger" in allow)


def inspect_network(net: Path) -> tuple[int, int, str | None]:
    edges = 0
    tl_logic = 0
    current_external_edge: str | None = None
    probe_edge: str | None = None

    for event, elem in ET.iterparse(net, events=("start", "end")):
        if event == "start" and elem.tag == "edge":
            edge_id = elem.attrib.get("id", "")
            if not edge_id.startswith(":"):
                edges += 1
                current_external_edge = edge_id
            else:
                current_external_edge = None
        elif event == "start" and elem.tag == "lane":
            if probe_edge is None and current_external_edge and passenger_allowed(elem.attrib):
                probe_edge = current_external_edge
        elif event == "start" and elem.tag == "tlLogic":
            tl_logic += 1
        elif event == "end":
            if elem.tag == "edge":
                current_external_edge = None
            elem.clear()

    return edges, tl_logic, probe_edge


def source_config_inputs(cfg: Path) -> dict:
    result = {
        "exists": cfg.exists(),
        "parse": False,
        "net_files": [],
        "additional_files": [],
        "route_files": [],
        "all_referenced_inputs_exist": False,
    }
    if not cfg.exists():
        return result

    root = ET.parse(cfg).getroot()
    result["parse"] = True
    base = cfg.parent

    def resolve(tag: str) -> list[dict]:
        el = root.find(f".//{tag}")
        if el is None:
            return []
        values = [v.strip() for v in el.attrib.get("value", "").split(",") if v.strip()]
        return [
            {
                "value": value,
                "resolved": str((base / value).resolve()),
                "exists": (base / value).exists(),
            }
            for value in values
        ]

    result["net_files"] = resolve("net-file")
    result["additional_files"] = resolve("additional-files")
    result["route_files"] = resolve("route-files")
    refs = result["net_files"] + result["additional_files"] + result["route_files"]
    result["all_referenced_inputs_exist"] = bool(refs) and all(x["exists"] for x in refs)
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--greenevt", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    ge = Path(a.greenevt).resolve()
    net = ge / "data/sumo_network/greensboro.net.xml"
    source_cfg = ge / "data/sumo_network/greensboro.sumocfg"

    edges, tl_logic, probe_edge = inspect_network(net)

    ver = subprocess.run(["sumo", "--version"], text=True, capture_output=True)
    network_smoke = subprocess.run(
        [
            "sumo",
            "--net-file",
            str(net),
            "--begin",
            "0",
            "--end",
            "1",
            "--no-step-log",
            "true",
        ],
        text=True,
        capture_output=True,
    )

    config_route_smoke = None
    if probe_edge is not None:
        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)
            route = td_path / "probe.rou.xml"
            cfg = td_path / "probe.sumocfg"
            route.write_text(
                "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                "<routes>\n"
                f"  <vehicle id=\"probe\" depart=\"0\"><route edges=\"{probe_edge}\"/></vehicle>\n"
                "</routes>\n"
            )
            cfg.write_text(
                "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                "<configuration>\n"
                "  <input>\n"
                f"    <net-file value=\"{net}\"/>\n"
                f"    <route-files value=\"{route}\"/>\n"
                "  </input>\n"
                "  <time><begin value=\"0\"/><end value=\"1\"/></time>\n"
                "  <report><no-step-log value=\"true\"/></report>\n"
                "</configuration>\n"
            )
            p = subprocess.run(
                ["sumo", "-c", str(cfg)],
                text=True,
                capture_output=True,
            )
            config_route_smoke = {
                "returncode": p.returncode,
                "stdout_tail": p.stdout[-4000:],
                "stderr_tail": p.stderr[-4000:],
            }

    source_inputs = source_config_inputs(source_cfg)

    checks = {
        "version_command": ver.returncode == 0,
        "edge_count": edges == 118289,
        "tlLogic_count": tl_logic == 914,
        "probe_edge_found": probe_edge is not None,
        "network_smoke": network_smoke.returncode == 0,
        "config_route_microfixture": bool(config_route_smoke)
        and config_route_smoke["returncode"] == 0,
    }
    report = {
        "scope": (
            "Frozen Greensboro network + deterministic SUMO configuration/route "
            "microfixture. This is solver/runtime qualification, not execution of "
            "the full generated GreenEVT transport scenario."
        ),
        "sumo_version_stdout": ver.stdout.strip(),
        "sumo_version_stderr": ver.stderr.strip(),
        "noninternal_edges": edges,
        "tlLogic_count": tl_logic,
        "probe_edge": probe_edge,
        "network_smoke": {
            "returncode": network_smoke.returncode,
            "stdout_tail": network_smoke.stdout[-4000:],
            "stderr_tail": network_smoke.stderr[-4000:],
        },
        "config_route_microfixture": config_route_smoke,
        "source_static_config": source_inputs,
        "source_static_config_interpretation": (
            "The repository greensboro.sumocfg references generated/scenario inputs. "
            "Missing referenced files do not invalidate the solver microfixture; "
            "full case execution must generate/materialize them before claiming a "
            "transport-case run."
        ),
        "checks": checks,
        "G_SUMO": all(checks.values()),
    }

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["G_SUMO"] else 2)


if __name__ == "__main__":
    main()
