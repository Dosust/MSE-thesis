"""Generate a canonical JSON report for non-ACN Phase-1 benchmark verification."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .benchmark_io import parse_case33bw, parse_sioux_falls_network, parse_sioux_falls_od
from .power import add_real_load, branch_flow_residuals, solve_radial_bfs
from .transport import (
    bpr_time,
    conjugate_frank_wolfe_user_equilibrium,
    node_flow_residuals,
    shortest_path,
)


def build_report(case33bw: Path, sioux_net: Path, sioux_od: Path) -> dict:
    case = parse_case33bw(case33bw.read_text())
    power = solve_radial_bfs(case.branches, case.loads_pu, tol=1e-12, max_iter=1000)
    if not power.converged:
        raise RuntimeError("IEEE-33 radial solver did not converge")
    p_residual = branch_flow_residuals(case.branches, case.loads_pu, power)

    perturbed_loads = add_real_load(case.loads_pu, 24, 0.01)
    power_plus = solve_radial_bfs(case.branches, perturbed_loads, tol=1e-12, max_iter=1000)
    if not power_plus.converged:
        raise RuntimeError("IEEE-33 perturbed radial solver did not converge")

    links = parse_sioux_falls_network(sioux_net.read_text())
    od = parse_sioux_falls_od(sioux_od.read_text())
    flows, t_iterations, gap = conjugate_frank_wolfe_user_equilibrium(
        links, od, gap_tol=1e-6, max_iter=5000
    )
    if gap > 1e-6:
        raise RuntimeError(
            f"Sioux Falls CFW did not satisfy frozen relative-gap criterion: {gap}"
        )
    t_residuals = node_flow_residuals(links, flows, od)
    costs = {
        (link.u, link.v): bpr_time(link, flows[(link.u, link.v)])
        for link in links
    }
    crew_base, path_base = shortest_path(links, costs, 1, 10)
    crew_closed, path_closed = shortest_path(
        links, costs, 1, 10, closed={(9, 10), (10, 9)}
    )

    return {
        "power": {
            "base_mva": case.base_mva,
            "base_kv": case.base_kv,
            "active_branches": len(case.branches),
            "iterations": power.iterations,
            "residual_max": p_residual["max"],
            "min_voltage_pu": min(abs(v) for v in power.voltage.values()),
            "bus24_voltage_pu": abs(power.voltage[24]),
            "branch_23_24_current_pu": abs(power.branch_current[(23, 24)]),
            "perturbation_mw": 0.100,
            "bus24_voltage_plus_0p1mw_pu": abs(power_plus.voltage[24]),
            "branch_23_24_current_plus_0p1mw_pu": abs(
                power_plus.branch_current[(23, 24)]
            ),
        },
        "transport": {
            "solver": "conjugate-frank-wolfe",
            "nodes": len({n for link in links for n in (link.u, link.v)}),
            "links": len(links),
            "od_total": sum(od.values()),
            "iterations": t_iterations,
            "relative_gap": gap,
            "max_node_balance_residual": max(abs(v) for v in t_residuals.values()),
            "scaled_node_balance_residual": max(abs(v) for v in t_residuals.values())
            / max(sum(od.values()), 1.0),
            "crew_base_cost": crew_base,
            "crew_closed_cost_fixed_link_costs": crew_closed,
            "crew_base_path": [list(edge) for edge in path_base],
            "crew_closed_path": [list(edge) for edge in path_closed],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case33bw", type=Path, required=True)
    parser.add_argument("--sioux-net", type=Path, required=True)
    parser.add_argument("--sioux-od", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = build_report(args.case33bw, args.sioux_net, args.sioux_od)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, sort_keys=True, indent=2, separators=(",", ": ")) + "\n"
    )


if __name__ == "__main__":
    main()
