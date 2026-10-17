"""SOURCE-CONSISTENT AC MATH + SYNTHETIC reachability toy.

AC nodal equations conform to MATPOWER's documented bus-current/power equations.
Feeder values, thermal parameters, safety limits, charger caps, and weather are entirely
hypothetical. This is not a MATPOWER software run or field validation.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from functools import lru_cache
from itertools import product
from math import sqrt, isclose
import numpy as np
from scipy.optimize import root, brentq
from scipy.linalg import expm

@dataclass(frozen=True)
class Model:
    vs: float=230.0
    rf: float=0.15
    xf: float=0.08
    rtr: float=0.025
    eta: float=0.94
    pr: float=12000.0
    cw: float=2e5; co:float=6e5; cc:float=5e4
    gwo:float=80.; goa:float=18.; gca:float=22.
    q0:float=130.
    qexternal:float=0.
    alpha:float=.70
    to_guard:float=65.; tc_guard:float=65.
    ko:float=500.; kc:float=350.
    max_tw:float=76.; max_to:float=72.; max_tc:float=78.
    vmin:float=213.
    imax:float=49.

@dataclass(frozen=True)
class Scenario:
    name: str
    ambient_p: float; ambient_c:float
    base_p:float; base_q:float

@dataclass(frozen=True)
class AC:
    vr:complex
    current:complex
    p_send:float
    q_send:float
    p_loss_feeder:float
    q_loss_feeder:float
    det:float

class PFError(ValueError):pass

def feeder(m:Model, pdc:float, sc:Scenario)->AC:
    """Exact high-voltage branch balanced three-phase constant-power 2-bus AC PF."""
    if pdc<0 or pdc>m.pr:raise PFError('DC power outside rated interval')
    pt=(sc.base_p+pdc/m.eta)/3.0
    qt=sc.base_q/3.0
    z=complex(m.rf,m.xf)
    B=m.vs*m.vs-2*(m.rf*pt+m.xf*qt)
    disc=B*B-4*abs(z)**2*(pt*pt+qt*qt)
    if B<=0 or disc<0:raise PFError('No high-voltage positive bus-voltage root')
    vm2=(B+sqrt(disc))/2
    if vm2<=0:raise PFError('nonpositive receiving voltage')
    vr=(vm2+np.conjugate(z)*complex(pt,qt))/m.vs
    current=np.conjugate(complex(pt,qt)/vr)
    assert abs(complex(m.vs,0)-vr-z*current)<1e-8
    assert abs(3*vr*np.conjugate(current)-complex(3*pt,3*qt))<1e-7
    sender=3*m.vs*np.conjugate(current)
    loss=3*abs(current)**2*z
    assert abs(sender-complex(3*pt,3*qt)-loss)<1e-7
    return AC(complex(vr),complex(current),sender.real,sender.imag,loss.real,loss.imag,disc)

def validate_numeric_powerflow(m:Model, sc:Scenario, pdc:float):
    sol=feeder(m,pdc,sc)
    z=complex(m.rf,m.xf)
    s=complex((sc.base_p+pdc/m.eta)/3,sc.base_q/3)
    def residual(x):
        vr=complex(*x)
        i=(m.vs-vr)/z
        mismatch=vr*np.conjugate(i)-s
        return (mismatch.real,mismatch.imag)
    rr=root(residual,[sol.vr.real*.985,sol.vr.imag*1.02+1e-3],method='hybr',tol=1e-12)
    assert rr.success or np.linalg.norm(rr.fun)<1e-7
    assert abs(complex(*rr.x)-sol.vr)<1e-6
    return sol

def cap_o(t,m):return max(0.0,min(m.pr,m.pr-m.ko*max(0,t-m.to_guard)))
def cap_c(t,m):return max(0.0,min(m.pr,m.pr-m.kc*max(0,t-m.tc_guard)))

def a_matrix(m):
    return np.array([[-m.gwo/m.cw,m.gwo/m.cw,0],
                     [m.gwo/m.co,-(m.gwo+m.goa)/m.co,0],
                     [0,0,-m.gca/m.cc]],dtype=float)

@lru_cache(maxsize=None)
def thermal_expm(m,dt):return expm(a_matrix(m)*dt)

def thermal_step(m:Model, x, ac:AC, pdc:float, sc:Scenario, dt:float=1200.):
    """Exact affine thermal flow for piecewise-constant AC loading, weather, and DC dispatch."""
    current_abs=abs(ac.current)
    hcu=3*m.rtr*current_abs**2
    heat_c=m.alpha*(pdc/m.eta-pdc)
    forcing=np.array([hcu/m.cw,(m.q0+m.goa*sc.ambient_p)/m.co,
                      (m.qexternal+heat_c+m.gca*sc.ambient_c)/m.cc])
    A=a_matrix(m)
    equilibrium=np.linalg.solve(-A,forcing)
    x0=np.array(x,dtype=float)
    end=equilibrium+thermal_expm(m,dt)@(x0-equilibrium)
    def at(t):return equilibrium+thermal_expm(m,round(float(t),10))@(x0-equilibrium)
    d0=A@x0+forcing
    d1=A@end+forcing
    peaks=np.maximum(x0,end)
    # Winding/oil 2x thermal block has at most one interior turning point per state.
    for j in (0,1):
        if d0[j]*d1[j]<0:
            troot=brentq(lambda t:(A@at(t)+forcing)[j],0.,dt,xtol=1e-8)
            peaks[j]=max(peaks[j],at(troot)[j])
    return end,peaks,hcu

def check_stage(m, x, pdc, sc, dt):
    try:ac=feeder(m,pdc,sc)
    except PFError:return False,np.array(x),None,'AC no solution'
    if abs(ac.vr)<m.vmin:return False,np.array(x),None,'voltage'
    if abs(ac.current)>m.imax:return False,np.array(x),None,'current'
    end,peak,hcu=thermal_step(m,x,ac,pdc,sc,dt)
    if np.any(peak>np.array([m.max_tw,m.max_to,m.max_tc])+1e-8):
        return False,end,(ac,peak),'thermal'
    if pdc>min(cap_o(peak[1],m),cap_c(peak[2],m))+1e-8:
        return False,end,(ac,peak),'derating'
    return True,end,(ac,peak),'ok'

def scan(m,scenarios,controls,N=6,dt=1200.,energy_required_kwh=17.):
    xinit=np.array([51.,50.,55.]); best=None
    threshold=energy_required_kwh*3.6e6
    total=0;allowed=0
    for sched in product(controls,repeat=N):
        total+=1
        energy=sum(sched)*dt
        if energy+1e-5<threshold:continue
        allok=True
        per_scenario=[]
        for sc in scenarios:
            x=xinit.copy()
            max_seen=x.copy()
            for p in sched:
                ok,x,aux,reason=check_stage(m,x,p,sc,dt)
                if aux is not None:max_seen=np.maximum(max_seen,aux[1])
                if not ok:allok=False;break
            if not allok:break
            per_scenario.append((sc.name,np.round(max_seen,3).tolist()))
        if allok:
            allowed+=1
            key=(energy,max(sched),sched)
            if best is None or key<best[0]:best=(key,per_scenario)
    return dict(examined=total,feasible=allowed,best=best,required_kwh=energy_required_kwh)

def tests_and_demo():
    m=Model()
    scs=[Scenario('warm',35.,39.,9000.,1800.),
         Scenario('extreme',53.,55.,12000.,2500.)]
    for sc in scs:
        for p in (0.,4000.,8000.,12000.):
            ac=validate_numeric_powerflow(m,sc,p)
            assert abs(ac.p_send-(sc.base_p+p/m.eta+ac.p_loss_feeder))<1e-8
            assert abs(ac.q_send-(sc.base_q+ac.q_loss_feeder))<1e-8
            assert 3*m.rtr*abs(ac.current)**2>=0
    mfold=replace(m,vs=230.,rf=.5,xf=0.,pr=90000.)
    pmax=mfold.vs*mfold.vs/(4*mfold.rf)
    sc0=Scenario('one phase equivalent',25.,25.,0.,0.)
    ac_fold=feeder(mfold,3*pmax*mfold.eta,sc0)
    assert abs(abs(ac_fold.vr)-mfold.vs/2)<1e-5
    try:feeder(mfold,3*(pmax+1)*mfold.eta,sc0)
    except PFError:pass
    else:raise AssertionError('AC fold infeasibility must be detected')
    result=scan(m,scs,(0.,4000.,8000.,12000.),6,1200.,17.)
    assert result['best'] is not None, result
    print('AC complex-power and scipy.root crosschecks PASSED (8 synthetic load cases)')
    print('AC high-voltage branch fold PASSED')
    print('two-scenario finite open-loop toy reachability:',result)
    bad=scan(m,scs,(0.,4000.,8000.,12000.),6,1200.,25.)
    assert bad['best'] is None
    print('INFEASIBLE 25 kWh toy mission: rated 12 kW * 2 h = 24 kWh bound')
    print('ALL ASSERTIONS PASSED — NO experimental data or field-validation claims')

if __name__=='__main__':tests_and_demo()
