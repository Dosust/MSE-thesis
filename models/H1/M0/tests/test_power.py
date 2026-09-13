import numpy as np
import pytest
from egmiv_h1 import Line, RadialNetwork


def feeder():
    return RadialNetwork(
        n_buses=3,
        slack_bus=0,
        lines=[
            Line(0, 1, r_pu=0.01, x_pu=0.005, smax_pu=2.0),
            Line(1, 2, r_pu=0.01, x_pu=0.005, smax_pu=1.0),
        ],
        v_min_pu=0.90,
        v_max_pu=1.05,
    )


def test_radial_lindistflow_exact_small_case():
    net = feeder()
    p = np.array([0.0, 0.20, 0.10])
    q = np.array([0.0, 0.04, 0.02])
    r = net.solve(p, q)
    # Downstream aggregation: line 1->2 serves bus 2; line 0->1 serves buses 1+2.
    np.testing.assert_allclose(r.branch_p_pu, [0.30, 0.10], atol=1e-12)
    np.testing.assert_allclose(r.branch_q_pu, [0.06, 0.02], atol=1e-12)
    # v^2_child = v^2_parent - 2(rP+xQ)
    v1_sq = 1.0 - 2*(0.01*0.30 + 0.005*0.06)
    v2_sq = v1_sq - 2*(0.01*0.10 + 0.005*0.02)
    np.testing.assert_allclose(r.voltage_sq_pu, [1.0, v1_sq, v2_sq], atol=1e-12)
    assert r.max_power_balance_residual_pu < 1e-12
    assert r.service == pytest.approx(1.0)


def test_exogenous_outage_disconnects_downstream_without_hidden_control():
    net = feeder()
    p = np.array([0.0, 0.20, 0.10])
    q = np.zeros(3)
    r = net.solve(p, q, line_available=np.array([True, False]))
    np.testing.assert_array_equal(r.energized_bus, [True, True, False])
    np.testing.assert_allclose(r.served_p_pu, [0.0, 0.20, 0.0])
    assert r.service == pytest.approx(2/3)
    assert r.max_power_balance_residual_pu < 1e-12


def test_invalid_nonradial_topology_rejected():
    with pytest.raises(ValueError):
        RadialNetwork(3, 0, [Line(0,1,0.01,0.01)])