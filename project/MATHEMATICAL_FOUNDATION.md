# Mathematical Foundation

## 1. Scientific object

The thesis treats sustainable infrastructure resilience as a **constrained dynamical-systems problem** on a coupled Power–Water–Transportation–Solid-Waste (P–W–T–SW) system.

The coupled state is

$$
X(t)=\begin{bmatrix}X_P(t)\\X_W(t)\\X_T(t)\\X_{SW}(t)\end{bmatrix}\in\mathcal X.
$$

The central object of interest is not a scalar resilience score. It is the geometry of admissible survival and recovery:

$$
\boxed{\partial\mathcal V_{R}}
$$

where $\mathcal V_R$ is a sustainability/equity-constrained viability kernel.

---

## 2. Governing hybrid multiscale model

A general reduced representation is

$$
\boxed{
\begin{aligned}
\dot X &= F(X,Z,m,u,\eta;\theta),\\
\varepsilon\dot Z &= G(X,Z,m,\eta;\theta),\\
m^+ &= \Phi(X,Z,m,\eta),\\
Y &= H(X,Z;\theta)+\varepsilon_Y.
\end{aligned}}
$$

with:

- $X(t)$ — coupled infrastructure state;
- $Z(t)$ — dynamic interface state;
- $m(t)$ — discrete operating/failure mode;
- $u(t)$ — intervention/recovery control;
- $\xi(t)$ — exogenous climate forcing;
- $\eta(t)$ — realized local hazard acting on infrastructure;
- $\theta$ — uncertain physical/interface parameters;
- $Y(t)$ — partial observations;
- $\varepsilon$ — interface/system timescale ratio;
- $\varepsilon_Y$ — observation error.

The model intentionally separates **sector dynamics**, **interface dynamics**, **discrete failures**, and **partial observation**.

---

## 3. Climate forcing and realized hazard

The thesis distinguishes external forcing from realized infrastructure stress:

$$
\boxed{\xi(t)\longrightarrow\eta(t)}.
$$

For the urban-flood demonstrator,

$$
\xi_{\text{rainfall}}\rightarrow \eta_{\text{flood}}.
$$

Solid-waste and drainage conditions may modify the realized hazard:

$$
X_{SW}\rightarrow B_{\text{drain}}\rightarrow\eta_{\text{flood}}\rightarrow(X_P,X_W,X_T,X_{SW}).
$$

This creates an endogenous feedback rather than treating flood intensity as purely exogenous.

---

## 4. Coupled operator representation

The system may be expressed through a time-dependent block coupling operator

$$
\mathcal A(t)=
\begin{bmatrix}
A_{PP} & A_{PW} & A_{PT} & A_{P,SW}\\
A_{WP} & A_{WW} & A_{WT} & A_{W,SW}\\
A_{TP} & A_{TW} & A_{TT} & A_{T,SW}\\
A_{SW,P} & A_{SW,W} & A_{SW,T} & A_{SW,SW}
\end{bmatrix}.
$$

The off-diagonal terms represent **interfaces/interdependencies**, not merely adjacency. A scientifically valid interface term must correspond to a specified mechanism of exchange, dependency, constraint, or intervention.

---

## 5. Sustainable and equitable admissibility

Define the admissible region

$$
\boxed{
K_R=K_{\mathrm{phys}}\cap K_{\mathrm{service}}\cap K_{\mathrm{sus}}\cap K_{\mathrm{eq}}.
}
$$

A state is admissible only if it simultaneously satisfies:

1. physical feasibility;
2. critical-service requirements;
3. sustainability constraints;
4. equity constraints.

Therefore

$$
\boxed{\text{operational recovery}\not\Rightarrow\text{sustainable-equitable recovery}.}
$$

---

## 6. Viability kernel

For admissible controls $u(\cdot)\in\mathcal U$, define

$$
\boxed{
\mathcal V_R=
\left\{x_0\in K_R:\exists u(\cdot)\in\mathcal U\;\text{s.t.}\;X(t;x_0,u,\eta,\theta)\in K_R\;\forall t\ge0\right\}.
}
$$

$\mathcal V_R$ contains the states from which at least one admissible intervention strategy can preserve admissibility.

The principal geometric diagnostic is the viability boundary

$$
\partial\mathcal V_R.
$$

---

## 7. Recovery / capture geometry

Viability and recovery are distinct. Define the capture/recovery set

$$
\boxed{
\mathcal C_R=
\left\{x_0:\exists u(\cdot),\exists T<\infty\;\text{s.t.}\;X(T;x_0,u)\in\mathcal V_R\right\}.
}
$$

The minimum recovery-time map is

$$
\boxed{
\tau_R(x_0)=\inf\left\{T:\exists u(\cdot),\;X(T;x_0,u)\in\mathcal V_R\right\}.
}
$$

This yields three classes:

$$
\boxed{\text{viable}\;|\;\text{recoverable but nonviable}\;|\;\text{nonrecoverable}.}
$$

---

## 8. Dynamic-interface deformation

The thesis compares a dynamic-interface model

$$
\mathcal V_{\mathrm{dyn}}=\mathcal V(Z(t))
$$

with a static approximation

$$
\mathcal V_{\mathrm{static}}=\mathcal V(\bar Z).
$$

A set-distance measure such as a Hausdorff-type metric can quantify deformation:

$$
\boxed{
\Delta_{\mathcal V}=d_H\left(\mathcal V_{\mathrm{dyn}},\mathcal V_{\mathrm{static}}\right).
}
$$

A key nondimensional quantity is

$$
\boxed{
\rho_{ij}=\frac{\tau_{\mathrm{interface},ij}}{\tau_{\mathrm{system}}}.
}
$$

The regimes $\rho_{ij}\ll1$, $\rho_{ij}\approx1$, and $\rho_{ij}\gg1$ motivate tests of when static coupling is an acceptable approximation.

---

## 9. Inverse problems and uncertainty

The upstream identification problem is

$$
\boxed{
\mathcal D_{\mathrm{obs}}\longrightarrow p(\mathcal G,\theta,Z\mid\mathcal D_{\mathrm{obs}}).
}
$$

A central reliability question is how identification uncertainty changes inferred viability geometry. One diagnostic is

$$
\boxed{
E_{\mathrm{inv}}=d_H\left(\mathcal V(\theta^\star),\mathcal V(\widehat\theta)\right).
}
$$

For probabilistic analysis, the deterministic membership question $x\in\mathcal V_R$ can be extended to

$$
P(x\in\mathcal V_R\mid\mathcal D_{\mathrm{obs}}).
$$

---

## 10. Control, design, and optimization

A viability-preserving control set can be written formally as

$$
\mathcal U_V(x)=\left\{u:F(x,u,\eta)\in T_{K_R}(x)\right\},
$$

where $T_{K_R}(x)$ is the tangent cone to $K_R$ at $x$ where this representation is valid.

Introduce design variables

$$
d=\{\text{capacity, topology, redundancy, storage, interface hardening}\}.
$$

Then

$$
d\longrightarrow\mathcal V_R(d),\qquad d\longrightarrow\mathcal C_R(d).
$$

A downstream resilience-constrained design problem may take the form

$$
\min_d J(d)
$$

subject to

$$
\operatorname{Vol}(\mathcal V_R(d))\ge V_{\min},\qquad
\tau_R(d)\le\tau_{\max},
$$

plus explicit sustainability, equity, physical, and budget constraints.

---

## 11. Scientific questions

The architecture is organized around three geometric questions:

$$
\boxed{
\begin{aligned}
Q_1 &: \text{What moves the viability boundary?}\\
Q_2 &: \text{How uncertain is that boundary?}\\
Q_3 &: \text{What interventions or designs move it in a favorable direction?}
\end{aligned}}
$$

These questions define the bridge from mathematical physics to sustainable engineering decisions.
