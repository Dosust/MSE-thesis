# Seven-Slide Research Logic and Formula Map — v1.0

**Status:** SUPPORTING PRESENTATION SYNTHESIS — NON-CANONICAL  
**Branch:** `framework/three-coupled-frameworks-v1`  
**Authority:** Chapter I on `main` + `project/THREE_COUPLED_FRAMEWORKS_V1.md`  
**Purpose:** Explain the thesis in at most seven slides while preserving the scientific boundaries of the canonical seven-stage framework.

# Thesis title

**Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**

---

## Slide 1 — Background: Power and Transportation are distinct but coupled

### Main message
**Power and Transportation retain different physics, but selected mechanisms couple their services, operation, and recovery.**

### Three bullets
- EV charging couples mobility demand to electricity supply; electrically dependent transport functions create (P\to T) pathways.
- Transportation accessibility can constrain crews, equipment, mobile resources, and power restoration, creating (T\to P) pathways.
- Coupled P–T models already exist; the thesis therefore does not claim that interdependency itself is new. *(Rinaldi et al., 2001; Wei et al., 2018; Anokhin et al., 2021).*

### General literature formula
```math
\mathcal G_{PT}
=
\left(
V_P\cup V_T,;
E_P\cup E_T\cup E_{PT}
\right).
```

### Thesis formula
```math
\boxed{P\rightarrow T\not\Rightarrow T\rightarrow P}
```

### Visual
Two physically distinct layers: **Power** and **Transportation**. Show separate directional arrows (P\to T) and (T\to P), each attached to a named mechanism. Do not draw one generic symmetric edge.

---

## Slide 2 — Research gap: the methods exist; the scientific handoffs remain unreliable

### Main message
**The bounded gap is not missing methods; it is the reliability of the transitions from evidence to a defensible engineering decision.**

### Three bullets
- Structure or proximity does not prove a directional dependency; mechanism existence does not prove identifiability or dynamic readiness.
- A simulated trajectory does not automatically establish resilience, and resilience improvement alone does not determine an engineering decision.
- The thesis treats the problem as **integration + incremental value + validation**, not as a claim that each component method is individually new. *(Ouyang, 2014; Zhou et al., 2020; Poulin & Kane, 2021; Trucco & Petrenj, 2023).*

### General logic
```math
\text{representation}
\rightarrow
\text{model}
\rightarrow
\text{prediction}
\rightarrow
\text{decision}.
```

### Thesis gap formula
```math
\boxed{
\text{established capability}
\rightarrow
\text{documented limitation}
\rightarrow
\text{unresolved handoff}
\rightarrow
\text{thesis test}
}
```

### Visual
A chain of seven nodes with six red/blue **handoff gates** between them. Emphasize the gates, not the stages.

---

## Slide 3 — Framework I: Structural–Mechanistic Qualification

### Main message
**Framework I converts raw physical/evidence inputs into only those P–T mechanisms that are admissible for dynamic modeling.**

### Plug-in / Input
```math
I_I=
\left(
Q_P,Q_T,
\Omega_{sys}^{+},
D_{raw},
\Pi
\right).
```

**Role of the input:** declare the critical services, study boundary, raw structural data, and provenance before any causal claim.

### Transformation
```math
\boxed{
\mathcal S_{PT}
\rightarrow
\mathfrak G_{PT}(x,t)
\rightarrow
\mathcal I^{cand}
\rightarrow
\mathcal I^{qualified}
\rightarrow
\mathcal I^{ready}
}
```

**Role of the transformation:** separate structural possibility from evidence-qualified direction, mechanism, activation, uncertainty, validity, and dynamic readiness. *(Rinaldi et al., 2001; Kivelä et al., 2014; Zhou et al., 2020).*

### Output
```math
O_I=
\left(
\mathcal S_{PT},
\mathfrak G_{PT},
\mathcal I^{ready},
\Theta,
\Delta,
\Omega
\right).
```

**Role for Framework II:** prevents Framework II from simulating an interface merely because assets are close, correlated, or topologically linked.

### Firewall
```math
\boxed{
\text{structure}
\neq
\text{mechanism}
\neq
\text{causal qualification}
\neq
\text{dynamic readiness}
}
```

### Visual
**Input spheres → structural graph cuboid → candidate-interface diamond → mechanism qualification gate → output package.**

---

## Slide 4 — Framework II: Dynamic–Operational Resilience

### Main message
**Framework II determines what the coupled system physically does, what operators can know and do, and whether required services can remain or recover.**

### Plug-in / Input
```math
I_{II}
=
\left(
\mathfrak G_{PT},
\mathcal I^{ready},
Y_0^{phys},
\eta,
u^{exo},
\Theta
\right).
```

**Role of the input:** define an executable physical experiment using only qualified mechanisms, initial conditions, disturbances, forcing, and parameters.

### General formulas
```math
\dot x=f(x,u,\eta;\theta),
\qquad
y=h(x)+v.
```

```math
\mathcal V
=
\left\{
x_0:\exists u(\cdot),\;x(t)\in K\;\forall t\in[0,T]
\right\}.
```

### Thesis transformation
```math
\boxed{
Y^{phys}
\rightarrow y
\rightarrow \widehat Y
\rightarrow (I,O)
\rightarrow \mathcal U_{feas}
\rightarrow u
\rightarrow
(\mathcal V,\mathcal R,\rho_{\mathcal V},\Gamma_U)
}
```

```math
\boxed{
\mathcal V
=
\mathcal V
\left(
F_{\mathcal G},
\mathcal U_{feas},
K,
\Gamma_U
\right)
}
```

**Role of the transformation:** connect native P–T dynamics to observation, estimation, organizational feasibility, control, viability, and recovery. Conventional resilience curves remain comparators. *(Béné & Doyen, 2018; Poulin & Kane, 2021; Li et al., 2024).*

### Output
```math
O_{II}
=
\left(
Y,Q,\widehat Y,
\mathcal U_{feas},
\mathcal V,\mathcal R,
\rho_{\mathcal V},
\Gamma_U
\right).
```

**Role for Framework III:** supplies a resilience diagnosis and uncertainty-qualified baseline against which interventions can be tested.

### Visual
**Physics triangle → observation/estimation sphere → feasible-control gate → viability/recovery region.**

---

## Slide 5 — Framework III: Intervention–Decision Engineering

### Main message
**Framework III asks not only whether an intervention improves resilience, but whether its full consequences leave it defensible.**

### Plug-in / Input
```math
I_{III}
=
\left(
\mathcal V,
\mathcal R,
\rho_{\mathcal V},
\Gamma_U,
\mathcal A_{cand}
\right).
```

**Role of the input:** identify vulnerable/recoverable regions and define candidate engineering actions under the uncertainty inherited from Framework II.

### General decision formula
```math
\min_{a\in\mathcal A_{feas}}
\mathbf f(a),
\qquad
\mathcal P
=
\operatorname{Pareto}(\mathcal A_{feas}).
```

### Thesis transformation
```math
a_k
\rightarrow
\mathfrak M^{a_k}
\rightarrow
\mathcal C(a_k)
\rightarrow
\mathcal A_{feas}
\rightarrow
\text{Pareto}
\rightarrow
\text{robustness/regret}.
```

```math
\boxed{
\mathcal C(a_k)=
\left(
\Delta\mathfrak R^{a_k},
\mathbf r^{a_k},
\mathcal E_{fx}^{a_k},
\mathcal E_{fy}^{a_k},
\Delta\mathbf J_{sus}^{a_k},
\mathcal F^{a_k},
\mathbf U^{a_k}
\right)
}
```

**Role of the transformation:** keep resilience effect, resource requirement, efficiency, and admitted sustainability consequences separate before joint decision analysis. *(Zou & Chen, 2019; Anokhin et al., 2021).*

### Output
```math
\boxed{O_{III}=\mathcal A_{joint}^{\star}}
```

**Role of the output:** return the set of alternatives that remain defensible; it does not claim one universal optimum.

### Visual
**Intervention cone → modified-system cuboid → consequence diamond → Pareto frontier → defensible-set output.**

---

## Slide 6 — What this thesis adds

### Main message
**The proposed contribution is controlled integration and tested incremental value across the handoffs—not invention of every underlying method.**

### Three bullets
- Admit coupling dynamically only after structural, mechanism, evidence, identification, and readiness tests.
- Test whether dynamic coupling, I/O constraints, and viability/reachability add useful information beyond simpler matched comparators.
- Test whether resource efficiency and admitted sustainability consequences actually change the engineering decision set.

### Comparator formula
```math
\boxed{
M_0
\;\text{(independent)}
\quad\text{vs.}\quad
M_1
\;\text{(static coupling)}
\quad\text{vs.}\quad
M_2
\;\text{(qualified dynamic coupling)}
}
```

### Thesis hypothesis map
```math
\boxed{
RQ_3\rightarrow H_1,;
RQ_4\rightarrow H_2,;
RQ_5\rightarrow H_3,;
RQ_6\rightarrow H_4,;
RQ_7\rightarrow H_5
}
```

### Contribution chain
```math
\boxed{
\text{Representation}
\rightarrow
\text{Qualified Dependency}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Feasible Response}
\rightarrow
\text{Resilience}
\rightarrow
\text{Intervention}
\rightarrow
\text{Decision}
}
```

**Scientific status:** these are proposed contributions and hypotheses; the repository currently marks H1–H5 **NOT TESTED**.

### Visual
Three horizontal comparator tracks (M_0,M_1,M_2) entering five test gates (H_1\ldots H_5).

---

## Slide 7 — End-to-end scientific contract and why it matters

### Main message
**Every framework must produce an output credible enough to become the next framework's input; otherwise the final decision is not scientifically defensible.**

### Three bullets
- Framework I prevents unsupported dependencies from entering the simulator.
- Framework II prevents unobservable states, infeasible actions, or unqualified uncertainty from becoming resilience claims.
- Framework III prevents a resilience gain from being mistaken automatically for a sustainable or defensible decision.

### Governing architecture
```math
\boxed{
\underbrace{(S_1\leftrightarrow S_2)}_{F_I}
\rightarrow
\underbrace{(S_3\leftrightarrow S_4\leftrightarrow S_5)}_{F_{II}}
\rightarrow
\underbrace{(S_6\leftrightarrow S_7)}_{F_{III}}
}
```

### Cross-cutting credibility
```math
\boxed{
\mathcal H
=
\{
\text{Evidence},
\text{Provenance},
\text{Identification},
\text{Verification},
\text{Validation},
\text{UQ},
\text{Falsification},
\text{Reproducibility}
\}
}
```

### Model-adequacy question
```math
\boxed{
M
\overset{?}{\mathrm{adequate}}
(Q,\Omega,D,E)
}
```

### Final research logic
```math
\boxed{
\text{physical evidence}
\rightarrow
\mathcal I^{ready}
\rightarrow
\mathcal M_{phys}
\rightarrow
\widehat Y,\mathcal U_{feas}
\rightarrow
\mathcal V,\mathcal R
\rightarrow
\mathcal C(a)
\rightarrow
\mathcal A_{joint}^{\star}
}
```

### Visual
One continuous **Input → Transform → Output → Input** pipeline across the three frameworks, with a single credibility band underneath all of them.

---

# Presentation reference set

1. Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). *Identifying, understanding, and analyzing critical infrastructure interdependencies.* IEEE Control Systems Magazine, 21(6), 11–25. https://doi.org/10.1109/37.969131
2. Ouyang, M. (2014). *Review on modeling and simulation of interdependent critical infrastructure systems.* Reliability Engineering & System Safety, 121, 43–60. https://doi.org/10.1016/j.ress.2013.06.040
3. Kivelä, M., Arenas, A., Barthelemy, M., et al. (2014). *Multilayer networks.* Journal of Complex Networks, 2(3), 203–271. https://doi.org/10.1093/comnet/cnu016
4. Wei, W., Wu, L., Wang, J., & Mei, S. (2018). *Network equilibrium of coupled transportation and power distribution systems.* IEEE Transactions on Smart Grid, 9(6), 6764–6779. https://doi.org/10.1109/TSG.2017.2723016
5. Zhou, S., Yang, Y., Ng, S. T., Xu, J. F., & Li, D. (2020). *Integrating data-driven and physics-based approaches to characterize failures of interdependent infrastructures.* International Journal of Critical Infrastructure Protection, 31, 100391. https://doi.org/10.1016/j.ijcip.2020.100391
6. Anokhin, D., Dehghanian, P., Lejeune, M. A., & Su, J. (2021). *Mobility-As-A-Service for Resilience Delivery in Power Distribution Systems.* Production and Operations Management, 30(8), 2492–2521. https://doi.org/10.1111/poms.13393
7. Béné, C., & Doyen, L. (2018). *From Resistance to Transformation: A Generic Metric of Resilience Through Viability.* Earth's Future, 6(7), 979–996. https://doi.org/10.1002/2017EF000660
8. Poulin, C., & Kane, M. B. (2021). *Infrastructure resilience curves: Performance measures and summary metrics.* Reliability Engineering & System Safety, 216, 107926. https://doi.org/10.1016/j.ress.2021.107926
9. Trucco, P., & Petrenj, B. (2023). *Characterisation of resilience metrics in full-scale applications to interdependent infrastructure systems.* Reliability Engineering & System Safety, 235, 109200. https://doi.org/10.1016/j.ress.2023.109200
10. Li, J., Xu, X., Yan, Z., Wang, H., & Chen, Y. (2024). *Dynamic flow equilibrium of transportation and power distribution networks considering flexible traveling choices and voltage quality improvement.* CSEE Journal of Power and Energy Systems. https://doi.org/10.17775/CSEEJPES.2022.04810
11. Zou, Q., & Chen, S. (2019). *Enhancing resilience of interdependent traffic-electric power system.* Reliability Engineering & System Safety, 191, 106557. https://doi.org/10.1016/j.ress.2019.106557

---

## Governance note

This document is a presentation/supporting synthesis. It does **not** replace the canonical seven-stage framework, Chapter-I authorities, RQ/SO/H authorities, or frozen stage governance. Any formula labeled “thesis formula” or “thesis transformation” is part of the thesis synthesis unless explicitly attributed to a literature source.
