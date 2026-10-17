"""SYNTHETIC mathematical tests: delayed control, hysteresis, feeder DAE, observations.
No parameter is an experimentally fitted transformer/EVSE or certified equipment limit.
Run with Python 3 and numpy: python VERIFY_DELAY_HYBRID_DAE_OBSERVATION_V01.py
"""
from dataclasses import dataclass
from math import acos, sqrt
import numpy as np

@dataclass(frozen=True)
class Toy:
    cw:float=3e5       # winding heat capacity J/K (arbitrary)
    co:float=9e5       # oil heat capacity J/K
    cc:float=6e4       # charger heat capacity J/K
    g:float=150.       # winding-oil conductance W/K
    r:float=20.        # oil-atmosphere conductance W/K
    s:float=45.        # charger-atmosphere conductance W/K
    eta:float=.94      # charger AC/DC efficiency
    alpha:float=.7     # loss-heat fraction to modeled charger node
    rphase:float=.02   # winding equivalent per phase ohm
    vll:float=400.     # line-line RMS voltage V
    pbase:float=18000. # other transformer LV real load W
    pr:float=30000.    # charger rated DC power W
    q0:float=300.      # transformer oil heat input W
    qext:float=0.      # charger external heat W

def heat(m,p):
    h=m.rphase/m.vll**2*(m.pbase+p/m.eta)**2
    ell=m.alpha*(1./m.eta-1.)
    return h,ell

def passive_matrix(m):
    return np.array([[-m.g/m.cw,m.g/m.cw,0.],
                     [m.g/m.co,-(m.g+m.r)/m.co,0.],
                     [0.,0.,-m.s/m.cc]])

def verify_small_gain():
    m=Toy(); Lo,Lc=50.,100.  # hypothetical W/K control sensitivities
    hmax=2*m.rphase/m.vll**2*(m.pbase+m.pr/m.eta)/m.eta
    ell=m.alpha*(1/m.eta-1)
    kappa=Lo*hmax/m.r+Lc*ell/m.s
    A=passive_matrix(m)
    B=np.outer([hmax/m.cw,0.,ell/m.cc],[0.,Lo,Lc])
    spectral=max(abs(np.linalg.eigvals(np.linalg.solve(-A,B))))
    assert 0<=kappa<1
    assert np.isclose(kappa,spectral,rtol=1e-10,atol=1e-12)
    assert max(np.linalg.eigvals(A+B).real)<0
    print(f'PASS small gain, kappa={kappa:.6f}, spectral radius={spectral:.6f}')

def verify_delay():
    a,k=1./3600,3./3600    # generic feedback, NOT equipment measurement
    w=sqrt(k*k-a*a)
    tau=acos(-a/k)/w
    lam=1j*w
    assert abs(lam+a+k*np.exp(-lam*tau))<1e-12
    # Transversal rightward movement of characteristic root at first crossing.
    cross=w*w/((1+a*tau)**2+(w*tau)**2)
    assert cross>0
    print(f'PASS scalar delay stability-crossing illustration: tau={tau:.2f} s')

def verify_hysteresis():
    ton,toff=70.,65.     # Celsius, arbitrary mode guards NOT thermal ratings
    times=np.arange(1201)
    temperature=np.where(times<=600,60+.025*times,75-.025*(times-600))
    mode=0; events=[]
    for t,T in zip(times,temperature):
        if mode==0 and T>=ton:
            mode=1;events.append(('restrict',int(t)))
        elif mode==1 and T<=toff:
            mode=0;events.append(('restore',int(t)))
    assert events==[('restrict',400),('restore',1000)],events
    assert events[1][1]-events[0][1]>=(ton-toff)/.025
    print('PASS bounded-rate toy hysteresis without chattering')

def verify_feeder():
    vs,resistance=230.,.5   # single-phase toy V and ohm
    pmax=vs**2/(4*resistance)
    for p in [0.,.1*pmax,.8*pmax,pmax]:
        discriminant=vs**2-4*resistance*p
        assert discriminant>=-1e-8
        v=(vs+sqrt(max(0.,discriminant)))/2
        assert abs(v*(vs-v)/resistance-p)<1e-8
    assert vs**2-4*resistance*(pmax+1)<0
    assert abs((vs-2*(vs/2))/resistance)<1e-12
    print(f'PASS feeder quadratic and branch fold, illustrative Pmax={pmax:.0f} W')

def verify_observation_rank():
    A=passive_matrix(Toy())
    C=np.array([[0.,1.,0.],[0.,0.,1.]])
    O=np.vstack([C,C@A,C@A@A])
    assert np.linalg.matrix_rank(O)==3
    Ccharger=np.array([[0.,0.,1.]])
    assert np.linalg.matrix_rank(np.vstack([Ccharger,Ccharger@A,Ccharger@A@A]))<3
    print('PASS idealized oil+charger observation rank; charger-only deficient')

def verify_hybrid_thermal_enclosure():
    m=Toy()
    pmax=m.pr;apmax=50.;aemax=55.
    hp,ell=heat(m,pmax)
    uo=apmax+(m.q0+hp)/m.r
    uw=uo+hp/m.g
    uc=aemax+(m.qext+ell*pmax)/m.s
    rng=np.random.default_rng(20261017)
    for _ in range(500):
        p=float(rng.uniform(0,pmax))
        ap=float(rng.uniform(25,apmax));ae=float(rng.uniform(25,aemax))
        h,_=heat(m,p)
        to=uo-float(rng.uniform(0,25))
        tw=uw-float(rng.uniform(0,25))
        # At a face held at upper bound, vector field points inward.
        assert h-m.g*(uw-to)<=1e-7
        assert m.q0+m.g*(tw-uo)-m.r*(uo-ap)<=1e-7
        assert m.qext+ell*p-m.s*(uc-ae)<=1e-7
    print('PASS thermal upper-face signs under 500 synthetic modes/weather draws')

def main():
    verify_small_gain();verify_delay();verify_hysteresis()
    verify_feeder();verify_observation_rank();verify_hybrid_thermal_enclosure()
    print('ALL SYNTHETIC TESTS PASS; NO SOURCE DATA FIT OR FIELD VALIDATION')

if __name__=='__main__':main()
