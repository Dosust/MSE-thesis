"""Deterministic parsers for the frozen Phase-1 benchmark sources.

The parsers are deliberately narrow: they support the exact MATPOWER case33bw
and TNTP Sioux Falls source formats frozen in PHASE1_DATA_MANIFEST_V1.md.
They do not silently repair malformed inputs.
"""
from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Dict, List, Tuple

from .power import Branch
from .transport import RoadLink


@dataclass(frozen=True)
class Case33BW:
    base_mva: float
    base_kv: float
    loads_pu: Dict[int, complex]
    branches: Tuple[Branch, ...]
    bus_mw_mvar: Dict[int, complex]


def _matrix_block(text: str, name: str) -> str:
    pattern = re.compile(
        rf"mpc\.{re.escape(name)}\s*=\s*\[(.*?)\];",
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise ValueError(f"MATPOWER matrix {name!r} not found")
    return match.group(1)


def _numeric_rows(block: str) -> List[List[float]]:
    rows: List[List[float]] = []
    for raw in block.splitlines():
        line = raw.split("%", 1)[0].strip()
        if not line:
            continue
        if line.endswith(";"):
            line = line[:-1]
        values = line.split()
        try:
            row = [float(value) for value in values]
        except ValueError as exc:
            raise ValueError(f"non-numeric matrix row: {raw!r}") from exc
        rows.append(row)
    return rows


def parse_case33bw(text: str) -> Case33BW:
    """Parse the frozen MATPOWER ``case33bw.m`` source.

    The source stores Pd/Qd in kW/kVAr and branch r/x in ohms, then converts
    them internally. We reproduce those explicit source conversions here.
    """
    base_match = re.search(r"mpc\.baseMVA\s*=\s*([0-9.eE+-]+)\s*;", text)
    if not base_match:
        raise ValueError("mpc.baseMVA not found")
    base_mva = float(base_match.group(1))

    bus_rows = _numeric_rows(_matrix_block(text, "bus"))
    branch_rows = _numeric_rows(_matrix_block(text, "branch"))
    if not bus_rows:
        raise ValueError("empty bus matrix")

    base_kv = bus_rows[0][9]
    if base_mva <= 0.0 or base_kv <= 0.0:
        raise ValueError("invalid power-system base")

    bus_mw_mvar: Dict[int, complex] = {}
    loads_pu: Dict[int, complex] = {}
    for row in bus_rows:
        if len(row) < 13:
            raise ValueError("unexpected MATPOWER bus row width")
        bus = int(row[0])
        p_mw = row[2] / 1000.0
        q_mvar = row[3] / 1000.0
        bus_mw_mvar[bus] = complex(p_mw, q_mvar)
        loads_pu[bus] = complex(p_mw / base_mva, q_mvar / base_mva)

    # kV^2 / MVA has units of ohms.
    z_base_ohm = base_kv * base_kv / base_mva
    branches: List[Branch] = []
    for row in branch_rows:
        if len(row) < 13:
            raise ValueError("unexpected MATPOWER branch row width")
        parent, child = int(row[0]), int(row[1])
        status = int(row[10])
        if status not in (0, 1):
            raise ValueError("branch status must be binary")
        if status == 0:
            continue
        branches.append(
            Branch(
                parent=parent,
                child=child,
                r_pu=row[2] / z_base_ohm,
                x_pu=row[3] / z_base_ohm,
            )
        )

    return Case33BW(
        base_mva=base_mva,
        base_kv=base_kv,
        loads_pu=loads_pu,
        branches=tuple(branches),
        bus_mw_mvar=bus_mw_mvar,
    )


def parse_sioux_falls_network(text: str) -> Tuple[RoadLink, ...]:
    """Parse the frozen Sioux Falls TNTP network file."""
    links: List[RoadLink] = []
    metadata_links = re.search(r"<NUMBER OF LINKS>\s+(\d+)", text)
    metadata_nodes = re.search(r"<NUMBER OF NODES>\s+(\d+)", text)
    if not metadata_links or not metadata_nodes:
        raise ValueError("required Sioux Falls network metadata missing")

    after_metadata = text.split("<END OF METADATA>", 1)
    if len(after_metadata) != 2:
        raise ValueError("TNTP end-of-metadata marker missing")

    for raw in after_metadata[1].splitlines():
        line = raw.strip()
        if not line or line.startswith("~"):
            continue
        if line.endswith(";"):
            line = line[:-1]
        fields = line.split()
        if len(fields) < 10:
            raise ValueError(f"unexpected TNTP network row: {raw!r}")
        u = int(fields[0])
        v = int(fields[1])
        capacity = float(fields[2])
        free_time = float(fields[4])
        alpha = float(fields[5])
        beta = float(fields[6])
        links.append(RoadLink(u, v, capacity, free_time, alpha, beta))

    expected_links = int(metadata_links.group(1))
    expected_nodes = int(metadata_nodes.group(1))
    nodes = {node for link in links for node in (link.u, link.v)}
    if len(links) != expected_links:
        raise ValueError(f"expected {expected_links} links, parsed {len(links)}")
    if len(nodes) != expected_nodes:
        raise ValueError(f"expected {expected_nodes} nodes, parsed {len(nodes)}")
    return tuple(links)


def parse_sioux_falls_od(text: str) -> Dict[Tuple[int, int], float]:
    """Parse the frozen Sioux Falls TNTP OD-demand file."""
    zones_match = re.search(r"<NUMBER OF ZONES>\s+(\d+)", text)
    total_match = re.search(r"<TOTAL OD FLOW>\s+([0-9.eE+-]+)", text)
    if not zones_match or not total_match:
        raise ValueError("required Sioux Falls OD metadata missing")
    zones = int(zones_match.group(1))
    published_total = float(total_match.group(1))

    od: Dict[Tuple[int, int], float] = {}
    origin = None
    for raw in text.splitlines():
        origin_match = re.match(r"\s*Origin\s+(\d+)\s*$", raw)
        if origin_match:
            origin = int(origin_match.group(1))
            continue
        if origin is None:
            continue
        for destination, demand in re.findall(
            r"(\d+)\s*:\s*([0-9.eE+-]+)\s*;", raw
        ):
            key = (origin, int(destination))
            if key in od:
                raise ValueError(f"duplicate OD pair {key}")
            od[key] = float(demand)

    expected_pairs = zones * zones
    if len(od) != expected_pairs:
        raise ValueError(f"expected {expected_pairs} OD cells, parsed {len(od)}")
    total = sum(od.values())
    if abs(total - published_total) > 1e-9:
        raise ValueError(
            f"published OD total {published_total} differs from parsed total {total}"
        )
    return od
