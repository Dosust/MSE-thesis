from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from .metrics import cumulative_service_loss

@dataclass(frozen=True)
class Charger:
    bus:int
    commodity:int
    source_cell:int
    demand_share:float
    pmax_pu:float
    energy_pu_h_per_vehicle:float
    efficiency:float=1.0
    def __post_init__(self):
        if self.bus<0 or self.commodity<0 or self.source_cell<0: raise ValueError('negative index')
        if not 0<=self.demand_share<=1: raise ValueError('demand_share')
        if self.pmax_pu<0 or self.energy_pu_h_per_vehicle<=0: raise ValueError('power/energy')
        if not 0<self.efficiency<=1: raise ValueError('efficiency')

@dataclass(frozen=True)
class StaticRepairPath:
    line_index:int
    road_cells:tuple[int,...]
    freeflow_travel_time_h:float
    def __post_init__(self):
        if self.line_index<0 or self.freeflow_travel_time_h<0 or len(self.road_cells)==0: raise ValueError('repair path')

@dataclass(frozen=True)
class M1Result:
    power_results:tuple
    traffic_results:tuple
    power_service:np.ndarray
    transport_service:np.ndarray
    base_transport_service:np.ndarray
    charger_arrival_vph:np.ndarray
    charger_requested_power_pu:np.ndarray
    charger_power_pu:np.ndarray
    charger_service_vph:np.ndarray
    charger_fulfillment:np.ndarray
    ev_load_by_bus_pu:np.ndarray
    cumulative_power_service_loss_h:float
    cumulative_transport_service_loss_h:float
    max_ev_load_mapping_residual_pu:float

class StaticCoupling:
    """Memoryless H1 M1 interface maps.

    lambda_c(k) comes from same-step transport source demand only.
    p_ch,c(k)=min(pmax*g_bus, E/eta * lambda_c), with no queue state.
    Transport service is algebraically derated by same-step charging fulfillment;
    CTM state itself is not changed by charging shortage. This is deliberate M1.
    """
    def __init__(self,power,traffic,chargers):
        self.power=power; self.traffic=traffic; self.chargers=tuple(chargers)
        for c in self.chargers:
            if c.bus>=power.n_buses or c.commodity>=traffic.n_commodities or c.source_cell>=traffic.n_cells: raise ValueError('charger mapping index')
        sums={}
        for c in self.chargers: sums[(c.source_cell,c.commodity)]=sums.get((c.source_cell,c.commodity),0)+c.demand_share
        if any(v>1+1e-12 for v in sums.values()): raise ValueError('charger shares exceed 1')
    def arrival_rates(self,source_demand_vph):
        d=np.asarray(source_demand_vph,float); out=np.zeros(len(self.chargers))
        for j,c in enumerate(self.chargers): out[j]=c.demand_share*d[c.source_cell,c.commodity]
        return out
    def bus_energized(self,line_available):
        avail=np.asarray(line_available,bool)
        if avail.shape!=(len(self.power.lines),): raise ValueError('line availability shape')
        e=np.zeros(self.power.n_buses,dtype=bool); e[self.power.slack_bus]=True
        for u in self.power.topological_order:
            if not e[u]: continue
            for child,line_idx in self.power.children[u]: e[child]=bool(avail[line_idx])
        return e
    def charger_power(self,arrival_vph,bus_energized):
        lam=np.asarray(arrival_vph,float); energized=np.asarray(bus_energized,bool); preq=np.zeros(len(self.chargers)); p=np.zeros(len(self.chargers)); mu=np.zeros(len(self.chargers)); phi=np.ones(len(self.chargers))
        for j,c in enumerate(self.chargers):
            energy_limited_request=c.energy_pu_h_per_vehicle*lam[j]/c.efficiency
            preq[j]=min(c.pmax_pu,energy_limited_request)
            p[j]=preq[j]*(1.0 if energized[c.bus] else 0.0)
            mu[j]=c.efficiency*p[j]/c.energy_pu_h_per_vehicle
            phi[j]=1.0 if lam[j]<=1e-15 else min(1.0,mu[j]/lam[j])
        return preq,p,mu,phi
    def bus_ev_load(self,p_ch):
        p=np.asarray(p_ch,float); by=np.zeros(self.power.n_buses)
        for j,c in enumerate(self.chargers): by[c.bus]+=p[j]
        return by
    def commodity_fulfillment(self,arrival_vph,phi):
        lam=np.asarray(arrival_vph,float); phi=np.asarray(phi,float); num=np.zeros(self.traffic.n_commodities); den=np.zeros(self.traffic.n_commodities)
        for j,c in enumerate(self.chargers): num[c.commodity]+=lam[j]*phi[j]; den[c.commodity]+=lam[j]
        out=np.ones(self.traffic.n_commodities); mask=den>1e-15; out[mask]=num[mask]/den[mask]
        return out

def static_repair_delay_h(path:StaticRepairPath,cell_available:np.ndarray)->float:
    a=np.asarray(cell_available,bool)
    for cell in path.road_cells:
        if cell<0 or cell>=len(a): raise ValueError('road cell index')
        if not a[cell]: return float('inf')
    return path.freeflow_travel_time_h

class M1Runner:
    def __init__(self,power,traffic,chargers):
        self.power=power; self.traffic=traffic; self.coupling=StaticCoupling(power,traffic,chargers)
    def run(self,p_base_pu,q_demand_pu,power_line_available,traffic_source_demand_vph,initial_traffic_occupancy,traffic_cell_available,service_weights_power=None,service_weights_transport=None):
        p=np.asarray(p_base_pu,float); q=np.asarray(q_demand_pu,float); pa=np.asarray(power_line_available,bool); td=np.asarray(traffic_source_demand_vph,float); tc=np.asarray(traffic_cell_available,bool); occ=np.asarray(initial_traffic_occupancy,float).copy(); K=p.shape[0]
        if p.shape!=q.shape or p.shape[1]!=self.power.n_buses: raise ValueError('power shape')
        if td.shape!=(K,self.traffic.n_cells,self.traffic.n_commodities): raise ValueError('traffic shape')
        wt=np.ones(self.traffic.n_commodities) if service_weights_transport is None else np.asarray(service_weights_transport,float)
        C=len(self.coupling.chargers); prs=[]; trs=[]; ps=np.zeros(K); ts=np.zeros(K); base_ts=np.zeros(K); lam=np.zeros((K,C)); preq=np.zeros((K,C)); pch=np.zeros((K,C)); mu=np.zeros((K,C)); phi=np.ones((K,C)); evbus=np.zeros((K,self.power.n_buses)); map_res=0.0
        for k in range(K):
            tr=self.traffic.step(occ,td[k],tc[k]); trs.append(tr); occ=tr.occupancy
            requested_flow=td[k].sum(axis=0); completed_flow=tr.completed_sink.sum(axis=0)
            den=float(np.dot(wt,requested_flow)); base_ts[k]=1 if den<=1e-15 else min(1,float(np.dot(wt,completed_flow))/den)
            lam[k]=self.coupling.arrival_rates(td[k])
            energized=self.coupling.bus_energized(pa[k])
            preq[k],pch[k],mu[k],phi[k]=self.coupling.charger_power(lam[k],energized)
            evbus[k]=self.coupling.bus_ev_load(preq[k])
            map_res=max(map_res,abs(float(preq[k].sum()-evbus[k].sum())))
            pr=self.power.solve(p[k]+evbus[k],q[k],pa[k],service_weights_power); prs.append(pr); ps[k]=pr.service
            cf=self.coupling.commodity_fulfillment(lam[k],phi[k])
            effective_completed=completed_flow*cf
            ts[k]=1 if den<=1e-15 else min(1,float(np.dot(wt,effective_completed))/den)
        return M1Result(tuple(prs),tuple(trs),ps,ts,base_ts,lam,preq,pch,mu,phi,evbus,cumulative_service_loss(ps,self.traffic.dt_h),cumulative_service_loss(ts,self.traffic.dt_h),float(map_res))