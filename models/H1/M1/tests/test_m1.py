import numpy as np
import pytest
from egmiv_h1 import Line,RadialNetwork,Cell,Turn,CTMNetwork,M0Runner,M1Runner,Charger,StaticCoupling,StaticRepairPath,static_repair_delay_h


def build(dt=0.01,chargers=True):
    power=RadialNetwork(3,0,[Line(0,1,0.005,0.002,2.0),Line(1,2,0.005,0.002,1.0)],v_min_pu=0.9)
    traffic=CTMNetwork([Cell(1,60,20,150,1800,0),Cell(1,60,20,150,1800,1800)],1,[Turn(0,1,0,1.0)],dt_h=dt)
    cs=[Charger(bus=2,commodity=0,source_cell=0,demand_share=1.0,pmax_pu=0.08,energy_pu_h_per_vehicle=0.0001,efficiency=0.9)] if chargers else []
    return power,traffic,cs

def inputs(K=120):
    p=np.tile([0.0,0.15,0.10],(K,1)); q=np.tile([0.0,0.03,0.02],(K,1)); pa=np.ones((K,2),bool)
    td=np.zeros((K,2,1)); td[:,0,0]=600.0; occ=np.zeros((2,1)); ca=np.ones((K,2),bool)
    return p,q,pa,td,occ,ca

# G1 dimensional identity encoded numerically: mu = eta*p/E in veh/h.
def test_g1_charging_service_dimensional_identity():
    p,t,cs=build(); cp=StaticCoupling(p,t,cs); lam=np.array([600.0]); preq,pc,mu,phi=cp.charger_power(lam,np.array([True,True,True]))
    assert mu[0]==pytest.approx(cs[0].efficiency*pc[0]/cs[0].energy_pu_h_per_vehicle)
    assert 0<=phi[0]<=1

# G2 no double-counting in bus load map.
def test_g2_ev_power_maps_exactly_once_to_power_buses():
    p,t,cs=build(); cp=StaticCoupling(p,t,cs); pc=np.array([0.06]); by=cp.bus_ev_load(pc)
    assert by.sum()==pytest.approx(pc.sum()); assert by[2]==pytest.approx(0.06); assert np.count_nonzero(by)==1

# G3 monotonicity under loss of electrical availability.
def test_g3_grid_loss_cannot_increase_charger_power_or_service():
    p,t,cs=build(); cp=StaticCoupling(p,t,cs); lam=np.array([600.0])
    req1,pc1,mu1,_=cp.charger_power(lam,np.array([True,True,True])); req0,pc0,mu0,_=cp.charger_power(lam,np.array([True,True,False]))
    assert pc0[0]<=pc1[0] and mu0[0]<=mu1[0]; assert pc0[0]==0 and mu0[0]==0

# G4 M1 -> M0 when interface map is removed (no chargers).
def test_g4_decoupling_limit_m1_equals_m0():
    p,t,_=build(chargers=False); args=inputs(); r0=M0Runner(p,t).run(*args); r1=M1Runner(p,t,[]).run(*args)
    np.testing.assert_allclose(r1.power_service,r0.power_service,atol=1e-12)
    np.testing.assert_allclose(r1.transport_service,r0.transport_service,atol=1e-12)
    assert r1.max_ev_load_mapping_residual_pu<1e-15

# G5 zero EV/transport demand -> charging coupling vanishes and M1=M0.
def test_g5_zero_demand_limit():
    p,t,cs=build(); args=list(inputs()); args[3][:]=0.0
    r0=M0Runner(p,t).run(*args); r1=M1Runner(p,t,cs).run(*args)
    np.testing.assert_allclose(r1.charger_power_pu,0.0)
    np.testing.assert_allclose(r1.power_service,r0.power_service,atol=1e-12)
    np.testing.assert_allclose(r1.transport_service,r0.transport_service,atol=1e-12)

# G6 unlimited-enough grid + charger means no mobility degradation from charging.
def test_g6_sufficient_charging_capacity_preserves_base_transport_service():
    p,t,_=build(); cs=[Charger(2,0,0,1.0,pmax_pu=1.0,energy_pu_h_per_vehicle=0.0001,efficiency=1.0)]
    r=M1Runner(p,t,cs).run(*inputs())
    np.testing.assert_allclose(r.charger_fulfillment,1.0,atol=1e-12)
    np.testing.assert_allclose(r.transport_service,r.base_transport_service,atol=1e-12)

# Coupled outage must affect static mobility service but not CTM state itself.
def test_feeder_outage_reduces_m1_transport_service_algebraically_without_queue_memory():
    p,t,cs=build(); args=list(inputs()); args[2][50:,1]=False
    r=M1Runner(p,t,cs).run(*args)
    assert np.all(r.charger_power_pu[50:,0]==0)
    assert np.all(r.charger_fulfillment[50:,0]==0)
    assert np.all(r.transport_service[50:]<=r.base_transport_service[50:]+1e-12)
    assert not hasattr(r,'queue')

# T->P: raising same-step transport demand cannot reduce EV power while unsaturated.
def test_transport_demand_increase_increases_or_saturates_ev_power():
    p,t,cs=build(); cp=StaticCoupling(p,t,cs)
    a=cp.arrival_rates(np.array([[300.0],[0.0]])); b=cp.arrival_rates(np.array([[900.0],[0.0]]))
    ra,pa,_,_=cp.charger_power(a,np.ones(3,bool)); rb,pb,_,_=cp.charger_power(b,np.ones(3,bool)); assert rb[0]>=ra[0] and pb[0]>=pa[0]

# Static repair access: snapshot only, no dynamic memory.
def test_static_repair_access_snapshot():
    path=StaticRepairPath(line_index=1,road_cells=(0,1),freeflow_travel_time_h=0.2)
    assert static_repair_delay_h(path,np.array([True,True]))==pytest.approx(0.2)
    assert np.isinf(static_repair_delay_h(path,np.array([True,False])))

# Time-step refinement in M1 benchmark should preserve terminal service and mapped energy closely.
def test_m1_time_step_refinement_benchmark():
    vals=[]
    for dt in (0.01,0.005,0.0025):
        p,t,cs=build(dt=dt); K=round(1.2/dt); args=list(inputs(K)); r=M1Runner(p,t,cs).run(*args)
        vals.append((r.transport_service[-1],np.sum(r.charger_power_pu)*dt))
    for st,_ in vals: assert st==pytest.approx(vals[0][0],abs=1e-10)
    for _,e in vals: assert e==pytest.approx(vals[0][1],rel=1e-10,abs=1e-12)

# No charger-share double counting.
def test_charger_share_over_one_rejected():
    p,t,_=build(); cs=[Charger(1,0,0,0.7,1,0.001),Charger(2,0,0,0.4,1,0.001)]
    with pytest.raises(ValueError): StaticCoupling(p,t,cs)

# Outage must not erase requested EV electrical demand from S_P denominator.
def test_outage_preserves_requested_ev_demand_in_power_service_denominator():
    p,t,cs=build(); args=list(inputs(K=2)); args[2][1,1]=False
    r=M1Runner(p,t,cs).run(*args)
    assert r.charger_requested_power_pu[1,0] > 0
    assert r.charger_power_pu[1,0] == 0
    assert r.power_service[1] < 0.6

# M1 defining property: no interface memory. Recovery is instantaneous once same-step inputs recover.
def test_m1_interface_is_memoryless_after_outage_recovery():
    p,t,cs=build(); cp=StaticCoupling(p,t,cs); lam=np.array([600.0])
    _,p0,_,phi0=cp.charger_power(lam,np.array([True,True,False]))
    req1,p1,mu1,phi1=cp.charger_power(lam,np.array([True,True,True]))
    req2,p2,mu2,phi2=cp.charger_power(lam,np.array([True,True,True]))
    assert p0[0]==0 and phi0[0]==0
    np.testing.assert_allclose(req1,req2); np.testing.assert_allclose(p1,p2); np.testing.assert_allclose(mu1,mu2); np.testing.assert_allclose(phi1,phi2)
    assert phi1[0]==pytest.approx(1.0)
