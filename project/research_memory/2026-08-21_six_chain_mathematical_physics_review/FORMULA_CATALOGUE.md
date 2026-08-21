# Formula Catalogue

These formulas are representative mathematical structures. The repository must distinguish:
1. equations explicitly established in cited literature;
2. canonical equations used to formalize a literature-grounded layer;
3. thesis-specific notation/synthesis.

## I. Physical system

### Conservation
\[
\frac{\partial \rho_i}{\partial t}+\nabla\cdot J_i=s_i
\]

### Network / multilayer representation
\[
G=(V,E), \qquad L=D-A
\]

\[
\mathcal M=\{G^{[1]},\ldots,G^{[m]},C\}
\]

### Dynamic interface
\[
y_{ij}(t)=g_{ij}(x_i(t),x_j(t),\theta_{ij},\tau_{ij},m_{ij})
\]

### Coupled dynamics
\[
\dot x_i=f_i(x_i,u_i,\eta_i)+\sum_{j\neq i}g_{ij}(x_i,x_j;\theta_{ij})
\]

\[
\dot X=F(X,U,\eta,\Theta)
\]

## II. Observation and inference

### Observation model
\[
y_k=h(x_k,\theta)+\varepsilon_k
\]

### Linear observability
\[
\mathcal O=
\begin{bmatrix}
C\\CA\\CA^2\\ \vdots\\ CA^{n-1}
\end{bmatrix},\qquad
\operatorname{rank}(\mathcal O)=n
\]

### Bayesian identification
\[
\pi(\theta\mid y)\propto p(y\mid\theta)\pi_0(\theta)
\]

### Regularized inverse problem
\[
\hat\theta=
\arg\min_\theta
\|y-\mathcal H(\theta)\|^2+\lambda R(\theta)
\]

### State estimation
\[
p(x_k\mid y_{1:k})
\]

### Prediction
\[
p(x_{k+1}\mid y_{1:k})
=
\int p(x_{k+1}\mid x_k)p(x_k\mid y_{1:k})dx_k
\]

## III. Hazard and consequence

### Hazard exceedance
\[
P(H>h)
\]

### Fragility
\[
P(D\ge d\mid H=h)
\]

### Failure probability
\[
P_f=P[g(X,H)\le 0]
\]

### Service deficit
\[
L_s(t)=1-\frac{S(t)}{S_0}
\]

### Expected consequence
\[
\mathbb E[C]=\int C(\ell)p(\ell)d\ell
\]

### State-to-society chain
\[
X(t)\rightarrow F(t)\rightarrow S(t)\rightarrow C(t)
\]

## IV. Viability, resilience, recovery and control

### Viability kernel
\[
\operatorname{Viab}_K=
\{x_0\in K:\exists u(\cdot),\ x(t;x_0,u)\in K,\ \forall t\}
\]

### Reachable set
\[
\mathcal R(T)=\{x(T):x(0)=x_0,\ u\in\mathcal U,\ d\in\mathcal D\}
\]

### HJI reachability
\[
\partial_tV+\min_u\max_d\nabla V^\top f(x,u,d)=0
\]

### Bruneau-type resilience loss
\[
L_R=\int_{t_0}^{t_1}[1-Q(t)]dt
\]

### Henry–Ramírez-Márquez recovery ratio
\[
R(t)=\frac{\phi(t)-\phi(t_d)}{\phi(t_0)-\phi(t_d)}
\]

### Generic recovery dynamics
\[
\dot r=F_R(r,u,b,\mathcal G)
\]

## V. Engineering lifecycle

### Constrained design
\[
x^\star=\arg\min_xJ_d(x)
\quad\text{s.t.}\quad g(x)\le0,\ h(x)=0
\]

### Optimal operation
\[
u^\star=\arg\min_u\int_0^T c(x(t),u(t))dt
\]

### Reliability / hazard rate
\[
R(t)=P(T_f>t),\qquad
\lambda(t)=\frac{f_T(t)}{1-F_T(t)}
\]

### Sequential maintenance policy
\[
\pi^\star=\arg\min_\pi\mathbb E\left[\sum_t c(X_t,a_t)\right]
\]

### Robust adaptation
\[
a^\star=\arg\min_a\max_{\omega\in\Omega}L(a,\omega)
\]

## VI. Societal decision

### Multi-objective vector
\[
\mathbf J(a)=
[J_{\mathrm{cost}},J_{\mathrm{carbon}},J_{\mathrm{reliability}},
J_{\mathrm{resilience}},J_{\mathrm{equity}},J_{\mathrm{service}}]^\top
\]

### Pareto set
\[
\mathcal P=\{a\in A:\nexists a'\in A\text{ such that }\mathbf J(a')\prec\mathbf J(a)\}
\]

### Weighted MCDA
\[
U(a)=\sum_{k=1}^{m}w_ku_k(a)
\]

### Equity service floor
\[
S_g(t)\ge S_g^{\min},\qquad \forall g
\]

### Bayesian learning
\[
\pi_{t+1}(\theta)\propto p(D_{t+1}\mid\theta)\pi_t(\theta)
\]
