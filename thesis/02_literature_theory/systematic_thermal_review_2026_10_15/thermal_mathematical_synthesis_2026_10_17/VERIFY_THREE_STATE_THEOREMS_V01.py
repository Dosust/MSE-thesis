"""Synthetic three-state electrothermal mathematics verifier.

NO parameters, temperatures, safety caps or outcomes here are empirical.
Requires numpy. Run python VERIFY_THREE_STATE_THEOREMS_V01.py
"""
from dataclasses import dataclass, replace
from math import isclose
import numpy as np

@dataclass(frozen=True)
class P:
    Cw:float=2.4e5; Co:float=7.2e5; Cc:float=7.e4 # J/K
    g:float=110.;r:float=85.;s:float=65.          # W/K
    Q0:float=240.; Qext:float=0.                  # W
    Ap:float=39.; Ae:float=45.                   # degrees C
    Pbase:float=12000.;eta:float=.94;alpha:float=.65
    Rphi:float=.018; Vll:float=400.             # ohm, V
    Pr:float=26000.                             # output DC W
    To0:float=52.; Tc0:float=48.               # synthetic onset degrees C
    so:float=2400.;sc:float=1600.              # W/K

def ell(m):return m.alpha*(1/m.eta-1.)
def H(p,m):return m.Rphi/m.Vll**2*(m.Pbase+p/m.eta)**2
def Hp(p,m):return 2*m.Rphi/m.Vll**2*(m.Pbase+p/m.eta)/m.eta
def limiter(t,start,slope,rated):return max(0.,min(rated,rated-slope*max(0.,t-start)))
def Do(to,m):return limiter(to,m.To0,m.so,m.Pr)
def Dc(tc,m):return limiter(tc,m.Tc0,m.sc,m.Pr)
def power(x,m):return min(m.Pr,Do(x[1],m),Dc(x[2],m))
def temp_of_p(p,m):
    to=m.Ap+(m.Q0+H(p,m))/m.r
    return np.array([to+H(p,m)/m.g,to,m.Ae+(m.Qext+ell(m)*p)/m.s])
def equilibrium(m):
    lo,hi=0.,m.Pr
    for _ in range(80):
        p=(lo+hi)/2
        if p>power(temp_of_p(p,m),m):hi=p
        else:lo=p
    p=(lo+hi)/2; x=temp_of_p(p,m)
    assert abs(power(x,m)-p)<1e-7
    return p,x
def rhs(x,m,command=None):
    tw,to,tc=x
    p=power(x,m) if command is None else command
    return np.array([(H(p,m)-m.g*(tw-to))/m.Cw,
         (m.Q0+m.g*(tw-to)-m.r*(to-m.Ap))/m.Co,
         (m.Qext+ell(m)*p-m.s*(tc-m.Ae))/m.Cc])
def analytic_jac(x,m):
    p=power(x,m)
    o,c=Do(x[1],m),Dc(x[2],m)
    if 0<o<min(c,m.Pr)-1e-6:a,b,branch=m.so,0.,'transformer'
    elif 0<c<min(o,m.Pr)-1e-6:a,b,branch=0.,m.sc,'charger'
    elif abs(o-m.Pr)<1e-7 and abs(c-m.Pr)<1e-7:a,b,branch=0.,0.,'rated'
    else:raise ValueError('Nondifferentiable cap tie or clipping: no Jacobian')
    h,l=Hp(p,m),ell(m)
    return np.array([[-m.g/m.Cw,(m.g-h*a)/m.Cw,-h*b/m.Cw],
         [m.g/m.Co,-(m.g+m.r)/m.Co,0.],
         [0.,-l*a/m.Cc,-(m.s+l*b)/m.Cc]]),branch,a,b
def upper(m,p,Apmax,Aemax):
    to=Apmax+(m.Q0+H(p,m))/m.r
    return np.array([to+H(p,m)/m.g,to,Aemax+(m.Qext+ell(m)*p)/m.s])
def rk4(x,dt,m,command):
    k1=rhs(x,m,command);k2=rhs(x+.5*dt*k1,m,command)
    k3=rhs(x+.5*dt*k2,m,command);k4=rhs(x+dt*k3,m,command)
    return x+dt*(k1+2*k2+2*k3+k4)/6
def cubic_coeff(m,p,a,b):
    A=m.g/m.Cw; B=m.g/m.Co; R=m.r/m.Co; S=m.s/m.Cc
    F=Hp(p,m)*a/m.Cw; M=ell(m)*b/m.Cc; U=A+B+R
    c1=U+S+M;c2=A*R+B*F+U*(S+M);c3=S*(A*R+B*F)+M*A*R
    assert c1>0 and c2>0 and c3>0 and c1*c2>c3
    assert np.isclose(c1*c2-c3,
        U*(A*R+B*F)+M*B*F+U*(U+S+M)*(S+M))
    return [1.,c1,c2,c3]
def main():
    base=P()
    cases=[('charger',base),
      ('transformer',replace(base,Ap=48.,Ae=25.,To0=51.,Tc0=100.)),
      ('rated',replace(base,Ap=25.,Ae=20.,To0=100.,Tc0=100.))]
    for expected,m in cases:
        p,x=equilibrium(m)
        J,branch,a,b=analytic_jac(x,m)
        assert branch==expected and max(abs(rhs(x,m)))<1e-9
        eps=1e-3
        Jfd=np.column_stack([
            (rhs(x+eps*np.eye(3)[i],m)-rhs(x-eps*np.eye(3)[i],m))/(2*eps)
            for i in range(3)])
        assert np.allclose(J,Jfd,rtol=2e-6,atol=1e-10)
        assert np.allclose(np.poly(J),cubic_coeff(m,p,a,b),rtol=1e-10,atol=1e-20)
        eig=np.linalg.eigvals(J)
        assert max(eig.real)<0
        xx=np.array([66.,60.,50.]);d=rhs(xx,m);actual=power(xx,m)
        assert isclose(m.Cw*d[0]+m.Co*d[1],
            H(actual,m)+m.Q0-m.r*(xx[1]-m.Ap),rel_tol=1e-11)
        assert isclose(m.alpha*(p/m.eta-p),ell(m)*p,rel_tol=1e-11)
        ub=upper(m,m.Pr,m.Ap+5.,m.Ae+5.)
        assert np.all(rhs(ub,m,command=m.Pr)<1e-10)
        assert np.all(x<=ub+1e-8)
        print(f'{branch}: p={p:.3f} W, Tw={x[0]:.3f} C, '
              f'To={x[1]:.3f} C, Tc={x[2]:.3f} C, '
              f'max(Re eigenvalue)={max(eig.real):.5g} 1/s')
        assert equilibrium(replace(m,Ap=m.Ap+5))[0]<=p+1e-6
        assert equilibrium(replace(m,Ae=m.Ae+5))[0]<=p+1e-6

    # Constructive constant-power toy safety/service certificate
    service=replace(base,Ap=30.,Ae=30.,To0=120.,Tc0=120.)
    p0=.3*service.Pr; t_depart=7200.; Ereq=.99*p0*t_depart
    box=upper(service,p0,service.Ap+5.,service.Ae+5.)
    assert p0<=min(Do(box[1],service),Dc(box[2],service))
    x=np.array([30.,30.,30.]); E=0.
    for _ in range(int(t_depart/5)):
        assert np.all(x<=box+1e-8)
        assert p0<=min(Do(x[1],service),Dc(x[2],service))
        x=rk4(x,5.,service,command=p0)
        E+=5.*p0
    assert E>=Ereq and np.all(x<=box+1e-8)

    # Smooth joint negative-feedback sensitivities; analytic cubic check.
    rng=np.random.default_rng(20261017)
    m=base; p=.6*m.Pr; h=Hp(p,m);l=ell(m)
    for _ in range(150):
        a,b=rng.uniform(0.,5000.,2)
        J=np.array([[-m.g/m.Cw,(m.g-h*a)/m.Cw,-h*b/m.Cw],
          [m.g/m.Co,-(m.g+m.r)/m.Co,0.],
          [0.,-l*a/m.Cc,-(m.s+l*b)/m.Cc]])
        assert np.allclose(np.poly(J),cubic_coeff(m,p,a,b),rtol=1e-9,atol=1e-19)
        assert max(np.linalg.eigvals(J).real)<0

    print('PASS: dimensional model budget, fixed point, 3-state Routh-Hurwitz,')
    print('finite differences, hot ambient order, invariant box, toy service, 150 joint cases')
    print('ALL PARAMETERS SYNTHETIC. NOT EXPERIMENTAL VALIDATION.')
if __name__=='__main__':main()
