#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from xml.etree import ElementTree as ET


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--greenevt", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    net = Path(a.greenevt) / "data/sumo_network/greensboro.net.xml"
    edges = 0
    tl_logic = 0
    for _, elem in ET.iterparse(net, events=("end",)):
        if elem.tag == "edge" and not elem.attrib.get("id", "").startswith(":"):
            edges += 1
        elif elem.tag == "tlLogic":
            tl_logic += 1
        elem.clear()

    ver = subprocess.run(["sumo", "--version"], text=True, capture_output=True)
    smoke = subprocess.run(
        ["sumo", "--net-file", str(net), "--begin", "0", "--end", "1", "--no-step-log", "true"],
        text=True,
        capture_output=True,
    )

    checks = {
        "version_command": ver.returncode == 0,
        "historical_revision": "98d19a78" in (ver.stdout + ver.stderr),
        "edge_count": edges == 118289,
        "tlLogic_count": tl_logic == 914,
        "network_smoke": smoke.returncode == 0,
    }
    report = {
        "sumo_version_stdout": ver.stdout.strip(),
        "sumo_version_stderr": ver.stderr.strip(),
        "noninternal_edges": edges,
        "tlLogic_count": tl_logic,
        "smoke_returncode": smoke.returncode,
        "smoke_stdout_tail": smoke.stdout[-4000:],
        "smoke_stderr_tail": smoke.stderr[-4000:],
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
