from __future__ import annotations

import math
import os
from pathlib import Path

from phase1_exec.benchmark_io import (
    parse_case33bw,
    parse_sioux_falls_network,
    parse_sioux_falls_od,
)
from phase1_exec.power import add_real_load, branch_flow_residuals, solve_radial_bfs
from phase1_exec.transport import (
    bpr_time,
    frank_wolfe_user_equilibrium,
    node_flow_residuals,
    shortest_path,
)


def _required_path(env_name: str) -> Path:
    value = os.environ.get(env_name)
    if not value:
        raise RuntimeError(f"{env_name} must point to the frozen benchmark file")
    path = Path(value)
    if not path.is_file():
        raise RuntimeError(f"missing benchmark file: {path}")
    return path


def test_case33bw_source_schema_and_conversion():
    case = parse_case33bw(_required_path("PHASE1_CASE33BW").read_text())
    assert case.base_mva == 10.0
    assert case.base_kv == 12.66
    assert len(case.bus_mw_mvar) == 33
    assert len(case.branches) == 32
    assert case.bus_mw_mvar[24] == complex(0.420, 0.200)
    assert case.loads_pu[24] == complex(0.042, 0.020)
    branch_2324 = next(br for br in case.branches if (br.parent, br.child) == (23, 24))
    zbase = 12.66**2 / 10.0
    assert math.isclose(branch_2324.r_pu, 0.8980 / zbase, rel_tol=0, abs_tol=1e-15)
    assert math.isclose(branch_2324.x_pu, 0.7091 / zbase, rel_tol=0, abs_tol=1e-15)


def test_case33bw_full_radial_solution_balance_and_positive_load_sign():
    case = parse_case33bw(_required_path("PHASE1_CASE33BW").read_text())
    base = solve_radial_bfs(case.branches, case.loads_pu, tol=1e-12, max_iter=1000)
    assert base.converged
    residual = branch_flow_residuals(case.branches, case.loads_pu, base)
    assert residual["max"] <= 1e-8

    # Controlled verification perturbation: +0.100 MW at bus 24 = 0.01 p.u. on 10 MVA base.
    perturbed_loads = add_real_load(case.loads_pu, 24, 0.01)
    perturbed = solve_radial_bfs(case.branches, perturbed_loads, tol=1e-12, max_iter=1000)
    assert perturbed.converged
    assert abs(perturbed.voltage[24]) < abs(base.voltage[24])
    assert abs(perturbed.branch_current[(23, 24)]) > abs(base.branch_current[(23, 24)])


def test_sioux_falls_source_schema_and_od_total():
    links = parse_sioux_falls_network(_required_path("PHASE1_SIOUX_NET").read_text())
    od = parse_sioux_falls_od(_required_path("PHASE1_SIOUX_OD").read_text())
    assert len({node for link in links for node in (link.u, link.v)}) == 24
    assert len(links) == 76
    assert len(od) == 24 * 24
    assert math.isclose(sum(od.values()), 360600.0, rel_tol=0, abs_tol=1e-9)
    assert all(link.alpha == 0.15 for link in links)
    assert all(link.beta == 4.0 for link in links)
    assert any((link.u, link.v) == (9, 10) for link in links)
    assert any((link.u, link.v) == (10, 9) for link in links)


def test_sioux_falls_full_user_equilibrium_conservation_and_closure_limit():
    links = parse_sioux_falls_network(_required_path("PHASE1_SIOUX_NET").read_text())
    od = parse_sioux_falls_od(_required_path("PHASE1_SIOUX_OD").read_text())

    flows, iterations, gap = frank_wolfe_user_equilibrium(
        links,
        od,
        gap_tol=1e-6,
        max_iter=5000,
    )
    assert iterations <= 5000
    assert gap <= 1e-6

    residuals = node_flow_residuals(links, flows, od)
    assert max(abs(value) for value in residuals.values()) <= 1e-8

    costs = {
        (link.u, link.v): bpr_time(link, flows[(link.u, link.v)])
        for link in links
    }
    base_cost, base_path = shortest_path(links, costs, 1, 10)
    closed_cost, _ = shortest_path(
        links,
        costs,
        1,
        10,
        closed={(9, 10), (10, 9)},
    )
    reopen_cost, reopen_path = shortest_path(links, costs, 1, 10)

    assert math.isfinite(base_cost)
    assert closed_cost >= base_cost - 1e-12
    assert math.isclose(reopen_cost, base_cost, rel_tol=0, abs_tol=1e-12)
    assert reopen_path == base_path
