# Stage 5 B0 — Mathematical Reference Verification

**Status:** `PASS_NUMERICAL_VERIFICATION`  
**Claim ceiling:** mathematical/numerical verification only; not infrastructure validation and not H3 evidence.

## Model [D]

[
dot x_i=a_i x_i+u_i,qquad |u_i|le U_i,qquad i=1,2.
]

[
K=[-L_1,L_1]	imes[-L_2,L_2],qquad
G_{rec}=[-r_1,r_1]	imes[-r_2,r_2].
]

| coordinate | a_i | U_i | L_i | r_i |
|---|---:|---:|---:|---:|
| x1 | 1.0 | 0.6 | 1.0 | 0.1 |
| x2 | 0.8 | 0.5 | 1.0 | 0.1 |

For (c_i=U_i/a_i) and horizon (T=1),

[
v_i(T)=c_i+(L_i-c_i)e^{-a_iT},
]

[
r_i(T)=c_i-(c_i-r_i)e^{-a_iT}.
]

Hence

[
mathcal V_T^{ref}=[-0.7471517765,0.7471517765]	imes[-0.7934983615,0.7934983615],
]

[
mathcal R_T^{ref}=[-0.4160602794,0.4160602794]	imes[-0.3891022938,0.3891022938].
]

At (Delta t=0.00625), the explicit-Euler predecessor approximation gives viability/recovery Hausdorff errors (5.68686	imes10^{-4}) and (7.41789	imes10^{-4}). The last refinement orders are approximately 0.996, consistent with a first-order method.

Independent cell-center rasterization satisfies the geometric localization bound

[
epsilon_hle h/sqrt 2
]

at every tested resolution. No B3 tolerance is inferred from this benchmark.

High-dimensional viability is computationally difficult, motivating verified reference problems and approximations (Maidens et al., 2013, https://doi.org/10.1016/j.automatica.2013.03.020). Property transfer between abstractions requires quantified precision (Girard & Pappas, 2007, https://doi.org/10.1016/j.automatica.2007.01.019).

[
oxed{B_0=mathrm{PASS NUMERICAL VERIFICATION}}
]
