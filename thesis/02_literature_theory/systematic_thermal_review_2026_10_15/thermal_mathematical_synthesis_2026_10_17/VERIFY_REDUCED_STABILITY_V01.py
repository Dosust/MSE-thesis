"""SYNTHETIC ONLY: numerical checks for reduced electrothermal feedback propositions.
No parameters, cap thresholds or temperatures here are experimental observations.
Run: python3 VERIFY_REDUCED_STABILITY_V01.py
"""
from dataclasses import dataclass,replace
from math import isclose

@dataclass(frozen=True)
class M:
    Ap:float=45.; Ae:float=50.       # Celsius: arbitrary ambient
    Cp:float=500000.; Ce:float=60000. # J/K: arbitrary heat capacities
    Gp:float=20.; Ge:float=45.      # W/K
    Q0:float=300.; Qext:float=0.    # W
    eta:float=.94; alpha:float=.7
    R:float=.02; V:float=400.      # ohm/volt: balanced unity-PF toy
    Pbase:float=18000.; Pr:float=30000. # W
    Tpstart:float=100.; Testart:float=65. # deg C NOT safety thresholds
    sp:float=4000.; se:float=1000. # W/K

def ell(m):return m.alpha*(1/m.eta-1)
def H(p,m):return (m.R/m.V**2)*(m.Pbase+p/m.eta)**2
def hprime(p,m):return 2*m.R/m.V**2*(m.Pbase+p/m.eta)/m.eta
def T(p,m):
    return (m.Ap+(m.Q0+H(p,m))/m.Gp,
            m.Ae+(m.Qext+ell(m)*p)/m.Ge)
def lim(temp,start,slope,rated):
    return max(0.,min(rated,rated-slope*max(0.,temp-start)))
def caps(tp,te,m):
    return lim(tp,m.Tpstart,m.sp,m.Pr),lim(te,m.Testart,m.se,m.Pr)
def P(tp,te,m):return min(m.Pr,*caps(tp,te,m))
def eq(m):
    lo,hi=0.,m.Pr
    for _ in range(80):
        mid=(lo+hi)/2
        if mid>P(*T(mid,m),m): hi=mid
        else:lo=mid
    p=(lo+hi)/2
    assert isclose(p,P(*T(p,m),m),abs_tol=1e-7)
    return p,*T(p,m)
def dyn(tp,te,m):
    p=P(tp,te,m)
    return ((m.Q0+H(p,m)-m.Gp*(tp-m.Ap))/m.Cp,
            (m.Qext+ell(m)*p-m.Ge*(te-m.Ae))/m.Ce)
def branch_J(tp,te,m):
    p=P(tp,te,m);pc,ec=caps(tp,te,m)
    if 0<pc<min(ec,m.Pr):a,b,name=m.sp,0.,'transformer'
    elif 0<ec<min(pc,m.Pr):a,b,name=0.,m.se,'charger'
    elif pc==ec==m.Pr:a,b,name=0.,0.,'rated'
    else:raise ValueError('nondifferentiable cap tie or clipping')
    h,l=hprime(p,m),ell(m)
    J=(-(m.Gp+h*a)/m.Cp,-h*b/m.Cp,
       -l*a/m.Ce,-(m.Ge+l*b)/m.Ce)
    trace=J[0]+J[3]
    determinant=J[0]*J[3]-J[1]*J[2]
    formula=(m.Gp*m.Ge+m.Gp*l*b+m.Ge*h*a)/(m.Cp*m.Ce)
    assert trace<0 and determinant>0
    assert isclose(determinant,formula,rel_tol=1e-11)
    return name,J,trace,determinant

def run():
    s=M()
    cases=[('charger',s),
      ('transformer',replace(s,Ap=60,Ae=25,Tpstart=74,Testart=120)),
      ('rated',replace(s,Ap=30,Ae=20,Tpstart=100,Testart=120))]
    for target,m in cases:
        p,tp,te=eq(m);name,J,tr,det=branch_J(tp,te,m)
        assert name==target
        d=1e-4
        fp=dyn(tp+d,te,m);fm=dyn(tp-d,te,m)
        gp=dyn(tp,te+d,m);gm=dyn(tp,te-d,m)
        finite=((fp[0]-fm[0])/(2*d),(gp[0]-gm[0])/(2*d),
                (fp[1]-fm[1])/(2*d),(gp[1]-gm[1])/(2*d))
        assert all(isclose(x,y,rel_tol=1e-5,abs_tol=1e-10)
                   for x,y in zip(finite,J)),(name,finite,J)
        pac=p/m.eta;loss=pac-p
        assert isclose(pac,p+loss,rel_tol=1e-12)
        assert isclose(m.alpha*loss,ell(m)*p,rel_tol=1e-12,abs_tol=1e-10)
        print(f'{name}: Pdc={p:.3f} W, Tp={tp:.3f} C, Te={te:.3f} C, '
              f'trace={tr:.6g} s^-1, det={det:.6g} s^-2')
    print('PASS (hypothetical model only; not experimental validation)')

if __name__=='__main__':run()
