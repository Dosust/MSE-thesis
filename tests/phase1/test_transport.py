import math

from phase1_exec.transport import (
    RoadLink,
    bpr_time,
    frank_wolfe_user_equilibrium,
    node_flow_residuals,
    shortest_path,
)


def _symmetric_two_path_network():
    return [
        RoadLink(1, 2, 10.0, 1.0),
        RoadLink(2, 4, 10.0, 1.0),
        RoadLink(1, 3, 10.0, 1.0),
        RoadLink(3, 4, 10.0, 1.0),
    ]


def test_bpr_is_monotone_in_flow():
    link = RoadLink(1, 2, 10.0, 5.0)
    assert bpr_time(link, 0.0) == 5.0
    assert bpr_time(link, 5.0) > bpr_time(link, 0.0)
    assert bpr_time(link, 10.0) > bpr_time(link, 5.0)


def test_frank_wolfe_symmetric_equilibrium_and_conservation():
    links = _symmetric_two_path_network()
    od = {(1, 4): 10.0}
    flow, _, gap = frank_wolfe_user_equilibrium(links, od, gap_tol=1e-10)
    assert gap <= 1e-8
    upper = flow[(1, 2)]
    lower = flow[(1, 3)]
    assert math.isclose(upper, 5.0, rel_tol=0, abs_tol=1e-6)
    assert math.isclose(lower, 5.0, rel_tol=0, abs_tol=1e-6)
    residuals = node_flow_residuals(links, flow, od)
    assert max(abs(value) for value in residuals.values()) < 1e-10


def test_declared_closure_cannot_reduce_shortest_path_when_costs_fixed():
    links = _symmetric_two_path_network()
    costs = {(link.u, link.v): link.free_time for link in links}
    baseline, _ = shortest_path(links, costs, 1, 4)
    closed, _ = shortest_path(links, costs, 1, 4, closed={(1, 2)})
    assert closed >= baseline
