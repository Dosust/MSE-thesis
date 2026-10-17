"""Dimensionally consistent *synthetic* ODE verification toy.

No parameter here is fitted to Gong, Kunlasing, or Krama observations.
No claim of empirical validation, standard compliance, or field causality.
"""
from dataclasses import dataclass
from math import sqrt, exp

@dataclass(frozen=True)
class Toy:
    c_w: float = 3.0e5      # J/K, hypothetical winding heat capacity
    c_o: float = 9.0e5      # J/K, hypothetical transformer oil heat capacity
    c_e: float = 6.0e4      # J/K, hypothetical charger heat capacity
    g_wo: float = 150.0    # W/K
    g_oa: float = 85.0     # W/K
    g_ea: float = 80.0     # W/K
    p_core: float = 200.0  # W
    r_phase: float = 0.015 # ohm, balanced phase equivalent
    v_ll: float = 400.0    # V
    p_base: float = 35000.0# W other LV demand
    eta_evse: float = 0.94 # hypothetical constant total efficiency
    p_dc_rated: float = 50000.0 # W
    derate_at: float = 55.0     # deg C, synthetic illustrative threshold, NOT paper's firmware
    derate_slope: float = 2000.0# W/K, illustrative
    heat_fraction: float = 0.60 # synthetic loss allocation fraction


def offered_power_w(temp_c: float, p: Toy) -> float:
    return max(0.0, min(p.p_dc_rated, p.p_dc_rated - p.derate_slope * max(0.0, temp_c - p.derate_at)))


def rhs(state: tuple[float, float, float, float], ambient_c: float, p: Toy):
    """Returns thermodynamic derivatives, electrical budget and net ambient loss."""
    t_o, t_w, t_e, e_dc = state
    p_dc = offered_power_w(t_e, p)
    p_ac = p_dc / p.eta_evse
    p_charger_loss = p_ac - p_dc
    p_sec = p.p_base + p_ac
    i_phase = p_sec / (sqrt(3.0)*p.v_ll) # balanced unity PF, **toy**
    p_cu = 3.0 * i_phase**2 * p.r_phase
    p_wo = p.g_wo * (t_w - t_o)
    p_oa = p.g_oa * (t_o - ambient_c)
    p_ea = p.g_ea * (t_e - ambient_c)
    d_w = (p_cu-p_wo) / p.c_w
    d_o = (p.p_core+p_wo-p_oa) / p.c_o
    d_e = (p.heat_fraction*p_charger_loss-p_ea) / p.c_e
    return (d_o,d_w,d_e,p_dc), (p_ac,p_dc,p_cu,p_oa,p_ea,p_charger_loss)


def integrate(ambient_c: float, p: Toy=Toy(), dt=1.0, horizon=3600.0):
    steps=round(horizon/dt)
    assert steps>0 and abs(steps*dt-horizon)<1e-8
    s=(ambient_c,ambient_c,ambient_c,0.0)
    for _ in range(steps):
        ds, _ = rhs(s, ambient_c, p)
        s=tuple(x +dt*dx for x,dx in zip(s,ds))
        assert all(-273.15 < v < 250 for v in s[:3]), "numerical breakdown"
    return s


def tests():
    p=Toy()
    x=(35.,40.,60.,0.)
    d, budget=rhs(x,35.,p)
    p_ac,p_dc,p_cu,p_oa,p_ea,p_loss=budget
    assert abs(p_ac-(p_dc+p_loss)) < 1e-8, "AC/DC conservation"
    # Sum of internal transformer stored-energy derivatives equals external sources minus ambient heat transfer.
    lhs=p.c_o*d[0]+p.c_w*d[1]
    rhs_energy=p.p_core+p_cu-p_oa
    assert abs(lhs-rhs_energy)<1e-8, "internal thermal exchange should cancel"
    # Positive charger capability; monotone synthetic derating beyond the hypothetical threshold.
    assert offered_power_w(40,p)==p.p_dc_rated
    assert offered_power_w(65,p)<offered_power_w(55,p)
    assert offered_power_w(100,p)>=0
    # Isolated one-body analytic cooling and forward Euler refinement (no charging or transformer loads).
    x0,xa,g,c,t=70.,30.,80.,60000.,900.
    exact=xa+(x0-xa)*exp(-g*t/c)
    def euler(dt):
        y=x0
        for _ in range(round(t/dt)): y+=dt*(-g*(y-xa)/c)
        return y
    coarse, fine=euler(10.),euler(1.)
    assert abs(fine-exact)<abs(coarse-exact)
    # Synthetic hot-climate stress comparison is a *toy prediction*, not validation.
    cold=integrate(25.,p,dt=1.,horizon=7200.)
    hot=integrate(50.,p,dt=1.,horizon=7200.)
    assert hot[3]<cold[3], "configured toy derating reduces DC energy at higher ambient"
    # Time-step refinement of delivered DC energy (same synthetic model).
    hot_half=integrate(50.,p,dt=0.5,horizon=7200.)
    assert abs(hot[3]-hot_half[3])<0.002*hot_half[3], "toy convergence tolerance"
    print('SYNTHETIC TESTS PASS — not calibrated or validated against any experiment')
    print('2h toy DC energy (kWh), temperate/hot:',round(cold[3]/3.6e6,4),round(hot[3]/3.6e6,4))


if __name__=='__main__': tests()
