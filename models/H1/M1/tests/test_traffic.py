import numpy as np
import pytest
from egmiv_h1 import Cell, Turn, CTMNetwork


def chain(dt=0.01):
    cells = [
        Cell(1.0, 60.0, 20.0, 150.0, 1800.0, 0.0),
        Cell(1.0, 60.0, 20.0, 150.0, 1800.0, 1800.0),
    ]
    turns = [Turn(0,1,0,1.0)]
    return CTMNetwork(cells, 1, turns, dt_h=dt)


def test_ctm_closed_system_conserves_vehicles():
    net = CTMNetwork(
        cells=[Cell(1,60,20,150,1800,0), Cell(1,60,20,150,1800,0)],
        n_commodities=1,
        turns=[Turn(0,1,0,1.0)],
        dt_h=0.01,
    )
    n0 = np.array([[10.0],[5.0]])
    r = net.step(n0)
    assert r.max_conservation_residual_veh < 1e-10
    assert r.occupancy.sum() == pytest.approx(n0.sum())
    assert r.min_occupancy_veh >= 0


def test_ctm_source_to_sink_global_conservation_over_time():
    net = chain()
    n = np.zeros((2,1))
    admitted = 0.0
    completed = 0.0
    for _ in range(100):
        r = net.step(n, source_demand_vph=np.array([[600.0],[0.0]]))
        admitted += net.dt_h * r.admitted_source.sum()
        completed += net.dt_h * r.completed_sink.sum()
        n = r.occupancy
        assert r.max_conservation_residual_veh < 1e-9
        assert r.max_jam_excess_veh < 1e-9
    assert n.sum() + completed == pytest.approx(admitted, abs=1e-8)


def test_ctm_cfl_violation_rejected():
    with pytest.raises(ValueError):
        CTMNetwork([Cell(1,60,20,150,1800)], 1, [], dt_h=0.02)  # max = 1/60 h


def test_multicommodity_conservation():
    net = CTMNetwork(
        [Cell(1,60,20,150,1800,0), Cell(1,60,20,150,1800,1800)],
        2,
        [Turn(0,1,0,1.0), Turn(0,1,1,1.0)],
        dt_h=0.01,
    )
    n = np.array([[12.0, 8.0],[0.0,0.0]])
    r = net.step(n)
    assert r.occupancy.sum() + net.dt_h*r.completed_sink.sum() == pytest.approx(n.sum())

def test_multicommodity_conservation_is_checked_per_commodity():
    net = CTMNetwork(
        [Cell(1,60,20,150,1800,0), Cell(1,60,20,150,1800,1800)],
        2,
        [Turn(0,1,0,1.0), Turn(0,1,1,1.0)],
        dt_h=0.01,
    )
    n = np.array([[12.0, 8.0],[2.0,1.0]])
    src = np.array([[100.0,50.0],[0.0,0.0]])
    r = net.step(n, src)
    assert np.max(r.conservation_residual_by_commodity_veh) < 1e-10