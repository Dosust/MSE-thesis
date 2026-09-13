import numpy as np
import pytest
from egmiv_h1 import Line, RadialNetwork, Cell, Turn, CTMNetwork, M0Runner


def build():
    power = RadialNetwork(3,0,[Line(0,1,0.005,0.002,2), Line(1,2,0.005,0.002,1)])
    traffic = CTMNetwork(
        [Cell(1,60,20,150,1800,0), Cell(1,60,20,150,1800,1800)],
        1,[Turn(0,1,0,1.0)],dt_h=0.01
    )
    return M0Runner(power, traffic)


def inputs(K=50):
    p=np.tile(np.array([0.0,0.15,0.10]),(K,1))
    q=np.tile(np.array([0.0,0.03,0.02]),(K,1))
    pa=np.ones((K,2),dtype=bool)
    td=np.zeros((K,2,1)); td[:,0,0]=600.0
    occ=np.zeros((2,1))
    ca=np.ones((K,2),dtype=bool)
    return p,q,pa,td,occ,ca


def test_m0_power_is_invariant_to_transport_demand():
    runner=build(); args=list(inputs())
    r1=runner.run(*args)
    args2=list(inputs()); args2[3][:,0,0]=1200.0
    r2=runner.run(*args2)
    np.testing.assert_allclose(r1.power_service,r2.power_service,atol=0,rtol=0)
    for a,b in zip(r1.power_results,r2.power_results):
        np.testing.assert_allclose(a.voltage_sq_pu,b.voltage_sq_pu,atol=0,rtol=0,equal_nan=True)


def test_m0_traffic_is_invariant_to_power_demand():
    runner=build(); args=list(inputs())
    r1=runner.run(*args)
    args2=list(inputs()); args2[0][:,1:]*=1.8
    r2=runner.run(*args2)
    np.testing.assert_allclose(r1.transport_service,r2.transport_service,atol=0,rtol=0)
    np.testing.assert_allclose(r1.completed_by_commodity,r2.completed_by_commodity,atol=0,rtol=0)


def test_m0_no_disruption_power_service_and_residuals():
    runner=build(); r=runner.run(*inputs())
    np.testing.assert_allclose(r.power_service,1.0)
    assert max(x.max_power_balance_residual_pu for x in r.power_results) < 1e-12
    assert max(x.voltage_violation_pu for x in r.power_results) == pytest.approx(0.0)
    assert max(x.thermal_violation_pu for x in r.power_results) == pytest.approx(0.0)
    assert max(x.max_conservation_residual_veh for x in r.traffic_results) < 1e-9


def test_m0_exogenous_line_outage_reduces_power_but_not_transport():
    runner=build(); args=list(inputs())
    r0=runner.run(*args)
    args_out=list(inputs()); args_out[2][10:,1]=False
    r1=runner.run(*args_out)
    assert np.all(r1.power_service[10:] < r0.power_service[10:])
    np.testing.assert_allclose(r1.transport_service,r0.transport_service,atol=0,rtol=0)

def test_transport_service_is_stepwise_completed_over_requested_flow():
    runner=build(); r=runner.run(*inputs(K=20))
    # Constant 600 veh/h request. After the two-cell travel transient the sink
    # completes 600 veh/h, so instantaneous service reaches 1 even though the
    # cumulative completed count still lags requested count by in-network vehicles.
    assert r.transport_service[-1] == pytest.approx(1.0)
    assert r.completed_by_commodity[0] < r.requested_by_commodity[0]