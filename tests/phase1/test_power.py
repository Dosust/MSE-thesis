from phase1_exec.power import (
    Branch,
    add_real_load,
    branch_flow_residuals,
    solve_radial_bfs,
)


def test_zero_load_recovers_flat_voltage():
    branches = [Branch(1, 2, 0.01, 0.02), Branch(2, 3, 0.01, 0.01)]
    sol = solve_radial_bfs(branches, {}, tol=1e-14)
    assert sol.converged
    assert all(abs(abs(v) - 1.0) < 1e-14 for v in sol.voltage.values())
    assert all(abs(current) < 1e-14 for current in sol.branch_current.values())


def test_branch_flow_equations_have_small_residual():
    branches = [Branch(1, 2, 0.01, 0.02), Branch(2, 3, 0.015, 0.01)]
    loads = {2: complex(0.05, 0.02), 3: complex(0.03, 0.01)}
    sol = solve_radial_bfs(branches, loads, tol=1e-13)
    assert sol.converged
    residual = branch_flow_residuals(branches, loads, sol)
    assert residual["max"] < 1e-10


def test_added_real_load_lowers_receiving_voltage_in_simple_radial_case():
    branches = [Branch(1, 2, 0.02, 0.01)]
    base = {2: complex(0.05, 0.01)}
    sol0 = solve_radial_bfs(branches, base)
    sol1 = solve_radial_bfs(branches, add_real_load(base, 2, 0.05))
    assert abs(sol1.voltage[2]) < abs(sol0.voltage[2])
