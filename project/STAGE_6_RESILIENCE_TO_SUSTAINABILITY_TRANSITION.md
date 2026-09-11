# Stage 6 — Resilience-to-Sustainability Transition

![Stage](https://img.shields.io/badge/Stage%206-FROZEN-1A7F37)
![Evidence](https://img.shields.io/badge/evidence-10%20passes%20%7C%2030%2B%20sources-0969DA)

**Framework label:** Stage 6 — Resilience-to-Sustainability Transformation Interface  
**Formal Stage-6 specification:** Resilience-to-Sustainability Transition  
**Status:** CANONICAL / FROZEN  
**Frozen:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Citation standard:** APA 7th edition author–date  
**Evidence basis:** targeted 10-pass research synthesis spanning resilience, adaptability/transformability, adaptation limits, lock-in, maladaptation, sustainability transitions, justice/equity, infrastructure transitions, and adaptive pathways  
**Change rule:** Do not revise this Stage-6 scientific scope unless explicitly requested and versioned.  
**Framework preservation rule:** This document formalizes Stage 6 only. It does not redefine Stages 1–5 and it does not pre-empt Stage 7 intervention sequencing.

> **Evidence notation:** `[E]` = established literature/theory; `[D]` = derived synthesis; `[P]` = proposed thesis construct requiring validation.

> **Boundary rule:** Stage 6 diagnoses whether preserving the current regime remains adequate and translates validated resilience evidence into requirements for recovery, adaptation, or transformation. It does **not** select, order, time, or optimize the intervention pathway; that is Stage 7.

---

## Frozen research question

> **When is recovery insufficient, and what conditions require adaptation or transformation?**

The essential Stage-6 transition is

```math
\underbrace{
\{K_{\mathrm{sus}},\mathcal V,\rho,T_{\mathcal V},T_K,S_{\mathcal V},S_K,S_{ij}^{\mathcal V}\}
}_{\text{Stage-5 viability evidence}}
\rightarrow
\underbrace{\text{regime-adequacy diagnosis}}_{\text{Stage 6}}
\rightarrow
\underbrace{(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)}_{\text{Stage-6 output}}.
```

Stage 6 answers three questions:

| Question | Stage-6 role |
|---|---|
| **Why must change occur?** | Diagnose inadequacy, limits, lock-in, maladaptation, structural weakness, sustainability and equity gaps. |
| **What must change?** | Translate evidence into explicit $P$–$T$–$I$–$O$ and interdependency requirements. |
| **How deep must change be?** | Classify recovery, adaptation or transformation and characterize required depth/scope/scale/pace. |

Stage 7, by contrast, determines **which interventions, in what order, at what time, under what constraints and future conditions**.

---

## 1. Current infrastructure regime

The current regime is represented by

```math
\mathfrak M_0
=
(\mathcal S,\mathcal G,\mathfrak I,F,\Theta,K_{\mathrm{sus}},\mathcal U).
```

This bundles the current system ontology, topology, causal interdependencies, dynamics, parameterization, sustainability/acceptability constraints and admissible action space. Stage 6 asks whether remaining within this regime is still defensible under validated resilience evidence and longer-horizon sustainability requirements.

---

## 2. Stage-5 evidence entering Stage 6

Define

```math
\mathcal R_5
=
\{\mathcal V,\rho,T_{\mathcal V},T_K,S_{\mathcal V},S_K,S_{ij}^{\mathcal V}\}.
```

This is a compact Stage-6 input interface, not a redefinition of Stage 5. The detailed Stage-5 definitions remain authoritative in `STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`.

Stage-5 evidence alone is not sufficient to justify long-horizon transformation. Stage 6 also requires externally justified long-term requirements

```math
\Lambda_{\mathrm{LT}}
=
\text{long-horizon sustainability, service, environmental, equity and governance requirements}.
```

This distinction is essential:

```math
\text{Stage 5: viability within the present decision/system space},
```

whereas

```math
\text{Stage 6: adequacy of that decision/system space itself}.
```

---

## 3. Transformation is not triggered by hazard occurrence alone

A major disturbance or failure is not, by itself, evidence that transformation is required:

```math
\text{major hazard}\not\Rightarrow\text{transformation},
```

```math
\text{failure}\not\Rightarrow\text{transformation}.
```

The relevant question is whether the **current regime is persistently inadequate** after considering viable recovery, adaptation capacity, long-term sustainability and justice requirements, structural causes, lock-in and maladaptation.

---

## 4. Recovery, adaptation and transformation classes

Stage 6 uses a hierarchical diagnostic rather than a universal scalar threshold.

### Recovery adequate

Recovery is adequate when feasible restoration within the current regime can re-establish acceptable operation without reproducing material long-term sustainability, lock-in, maladaptation or equity failures.

### Adaptation required

Adaptation is indicated when recovery alone is inadequate but modifications of operating rules, parameters, capacities or configurations can satisfy requirements while preserving the system's essential regime identity. Conceptually,

```math
\exists\theta'\in\Theta_A:
\mathfrak M_0(\theta')
\text{ satisfies the required criteria}.
```

### Transformation required

Transformation is indicated when meeting the requirements requires changing fundamental attributes, topology, institutional rules, cross-sector relationships or system goals:

```math
\mathfrak M_0\rightarrow\mathfrak M_1.
```

These mathematical statements are `[P]` formalizations of established recovery/adaptation/transformability distinctions; they are not universal laws.

The Stage-6 response class is

```math
c_6\in\{R,A,T\},
```

with $R$ = recovery adequate, $A$ = adaptation required and $T$ = transformation required/justified.

---

## 5. Adaptation limits

Stage 6 explicitly distinguishes

```math
L_A\in\{\mathrm{none},\mathrm{soft},\mathrm{hard}\}.
```

A **soft limit** means that a technically relevant response may exist but current financial, institutional, informational, technological, governance or capacity constraints prevent implementation. A **hard limit** means available adaptive actions cannot avoid the intolerable outcome under the defined conditions.

For the P–T–I–O framework, the principal mapping is:

| Limit family | Primary framework location |
|---|---|
| Physical/technical limit | $P,T$ |
| Information/technology limit | $I$ |
| Governance/resource/coordination limit | $O$ |
| Cross-sector/interdependency limit | $\mathfrak I$ |

---

## 6. Structural causes, lock-in and maladaptation

Repairing consequences is not the same as removing the mechanism that repeatedly generates vulnerability:

```math
\text{repairing consequences}\neq\text{removing structural causes}.
```

If the same critical interdependency is repeatedly restored after failure, a thesis-specific interdependency-lock-in diagnosis is possible:

```math
\text{critical dependency}
\rightarrow
\text{failure}
\rightarrow
\text{recovery}
\rightarrow
\text{same critical dependency}.
```

This interdependency-lock-in representation is `[P]`. It links Stage-2 causal mechanisms to Stage-5 sensitivity and Stage-6 transformation diagnosis.

Stage 6 also retains maladaptation as a separate concern: an intervention can reduce one risk while increasing future vulnerability, inequity, lock-in or environmental burden.

---

## 7. Sustainability-gap vector

A single resilience score is insufficient for the Stage-6 decision. Retain explicit sustainability gaps:

```math
\mathbf G_{\mathrm{sus}}
=
\begin{bmatrix}
G_{\mathrm{tech}}\\
G_{\mathrm{env}}\\
G_{\mathrm{econ}}\\
G_{\mathrm{eq}}\\
G_{\mathrm{gov}}
\end{bmatrix}.
```

The five components respectively represent technical/service, environmental, economic, equity/justice and governance/institutional gaps relative to justified long-horizon requirements. This vector is a proposed thesis synthesis `[P]`.

---

## 8. Diagnostic vector

Stage 6 uses a diagnostic vector rather than one arbitrary transformation score:

```math
\mathbf d_6
=
\begin{bmatrix}
d_{\mathcal V}\\
d_{\mathrm{limit}}\\
d_{\mathrm{lock}}\\
d_{\mathrm{mal}}\\
d_{\mathrm{sus}}\\
d_{\mathrm{eq}}\\
d_{\mathrm{struct}}
\end{bmatrix}.
```

| Component | Meaning |
|---|---|
| $d_{\mathcal V}$ | viability inadequacy |
| $d_{\mathrm{limit}}$ | evidence of adaptation limits |
| $d_{\mathrm{lock}}$ | lock-in/path-dependence evidence |
| $d_{\mathrm{mal}}$ | maladaptation evidence |
| $d_{\mathrm{sus}}$ | long-term sustainability gap |
| $d_{\mathrm{eq}}$ | equity/justice gap |
| $d_{\mathrm{struct}}$ | persistent structural/interdependency weakness |

The vector is `[P]`; the literature supports the underlying dimensions, not this exact seven-component construction.

---

## 9. Transformation character

Transformation should not be reduced to a binary variable. Stage 6 characterizes the required transformation by

```math
\boldsymbol{\zeta}_T
=
\begin{bmatrix}
\zeta_{\mathrm{depth}}\\
\zeta_{\mathrm{scope}}\\
\zeta_{\mathrm{scale}}\\
\zeta_{\mathrm{pace}}\\
\zeta_{\mathrm{equity}}\\
\zeta_{\mathrm{environment}}
\end{bmatrix}.
```

This is a derived/proposed `[D/P]` infrastructure transformation-requirement vector. It specifies how deep, broad, large, fast, equitable and environmentally consequential the required change must be. It does **not** choose the interventions.

---

## 10. P–T–I–O requirement set

Stage 6 translates diagnosis back into the canonical system ontology:

```math
\mathcal D_6
=
\{
\mathcal D_P,
\mathcal D_T,
\mathcal D_I,
\mathcal D_O,
\mathcal D_{\mathfrak I},
\mathcal D_{\mathrm{env}},
\mathcal D_{\mathrm{eq}}
\}.
```

| Requirement | Meaning |
|---|---|
| $\mathcal D_P$ | required changes in power-system properties |
| $\mathcal D_T$ | required changes in transportation-system properties |
| $\mathcal D_I$ | required changes in informational capability/architecture |
| $\mathcal D_O$ | required changes in organizational/governance capability/architecture |
| $\mathcal D_{\mathfrak I}$ | required changes to critical causal interdependencies |
| $\mathcal D_{\mathrm{env}}$ | environmental requirements |
| $\mathcal D_{\mathrm{eq}}$ | equity/justice requirements |

The exact requirement set is `[P]` and is the principal engineering bridge from Stage 6 to Stage 7.

---

## 11. Frozen translation operator

The canonical Stage-6 translation is

```math
\Phi_{\mathrm{ST}}
:
(\mathcal R_5,\Lambda_{\mathrm{LT}},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol{\zeta}_T).
```

This operator is a thesis construct `[P]`. It formalizes the transformation-interface role but does not imply that a unique closed-form algorithm has already been established.

The compact scientific logic is

```math
\begin{aligned}
&\text{Stage-5 viability evidence}
+\text{long-horizon sustainability requirements}\\
&\quad+\text{adaptation limits}
+\text{lock-in/maladaptation}\\
&\rightarrow\text{regime-adequacy diagnosis}
\rightarrow\{R,A,T\}
\rightarrow(\mathcal D_6,\boldsymbol{\zeta}_T).
\end{aligned}
```

---

## 12. Evidence status

| Object/concept | Status |
|---|---|
| Resilience distinct from simple rebound | `[E]` |
| Adaptability distinct from transformability | `[E]` |
| Fundamental/new-trajectory change as transformation | `[E]` |
| Soft and hard adaptation limits | `[E]` |
| Adaptation tipping/turning points | `[E]` |
| Maladaptation | `[E]` |
| Infrastructure/path/carbon lock-in | `[E]` |
| Systemic/multilevel sustainability transitions | `[E]` |
| Depth, scope, scale and pace as transformation dimensions | `[E]` |
| Distributive/equity considerations in transformation | `[E]` |
| Viability boundary $\neq$ adaptation turning point | `[D]` |
| Recovery/adaptation/transformation as regime-change classes | `[P]` |
| $\mathbf G_{\mathrm{sus}}$ | `[P]` |
| Interdependency-lock-in cycle | `[P]` |
| $\mathbf d_6$ | `[P]` |
| $\mathcal D_6$ | `[P]` |
| $\boldsymbol{\zeta}_T$ | `[D/P]` |
| $\Phi_{\mathrm{ST}}$ | `[P]` |

Freezing Stage 6 freezes this classification; proposed constructs do not become established theory merely because the stage is frozen.

---

## 13. Boundary with Stage 7

The frozen handoff is

```math
(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)
\longrightarrow
\text{Stage 7 candidate interventions and pathways}.
```

Stage 6 outputs:

- **why** change is required;
- **what system properties** must change;
- **how deep/broad/fast** the change must be.

Stage 7 will determine:

- **which interventions** satisfy those requirements;
- **in what order** they should be deployed;
- **when or under what trigger conditions** they should be activated;
- **under which technical, budgetary, organizational, sustainability, equity and uncertainty constraints** the pathway remains admissible.

This boundary is canonical.

---

## 14. Final frozen Stage-6 scope

| Item | Canonical Stage-6 specification |
|---|---|
| **Framework label** | Resilience-to-Sustainability Transformation Interface |
| **Formal specification** | Resilience-to-Sustainability Transition |
| **Question** | When is recovery insufficient, and what conditions require adaptation or transformation? |
| **Current regime** | $\mathfrak M_0=(\mathcal S,\mathcal G,\mathfrak I,F,\Theta,K_{\mathrm{sus}},\mathcal U)$ |
| **Stage-5 input** | $\mathcal R_5$ |
| **Long-horizon requirements** | $\Lambda_{\mathrm{LT}}$ |
| **Adaptation limits** | $L_A\in\{\mathrm{none},\mathrm{soft},\mathrm{hard}\}$ |
| **Sustainability gaps** | $\mathbf G_{\mathrm{sus}}$ |
| **Diagnostic vector** | $\mathbf d_6$ |
| **Response class** | $c_6\in\{R,A,T\}$ |
| **Transformation character** | $\boldsymbol{\zeta}_T$ |
| **Requirement set** | $\mathcal D_6$ |
| **Translation** | $\Phi_{\mathrm{ST}}:(\mathcal R_5,\Lambda_{\mathrm{LT}},\mathbf d_6)\mapsto(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)$ |
| **Output** | diagnosed need and requirements for recovery, adaptation or transformation — **not** the intervention pathway |
| **Stage-7 handoff** | $(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)$ |

> **STAGE 6 SCIENTIFIC SCOPE: FROZEN**

---

## Core APA 7 references

Abson, D. J., Fischer, J., Leventon, J., Newig, J., Schomerus, T., Vilsmaier, U., von Wehrden, H., Abernethy, P., Ives, C. D., Jager, N. W., & Lang, D. J. (2017). Leverage points for sustainability transformation. *Ambio, 46*(1), 30–39. https://doi.org/10.1007/s13280-016-0800-y

Béné, C., & Doyen, L. (2018). From resistance to transformation: A generic metric of resilience through viability. *Earth's Future, 6*(7), 979–996. https://doi.org/10.1002/2017EF000660

Biesbroek, R., Engbersen, D., Bonenkamp, J., Broek, E., Boon, E., Meijering, J., Nalau, J., Ford, J. D., Totin, E., Leiter, T., Gilmore, E., & Ebi, K. L. (2026). Expert agreement on key elements of transformational adaptation to climate risks. *Nature Climate Change, 16*(3), 273–280. https://doi.org/10.1038/s41558-025-02548-y

Bizer, M. A., Kirchhoff, C. J., Segal, J. L., & Patenaude, W. L. (2025). Transforming takes a village plus a willingness to break down barriers and learn: An event history study of transformation and resilience in critical infrastructure. *Journal of Environmental Management, 380*, 124980. https://doi.org/10.1016/j.jenvman.2025.124980

Doyen, L., & Gajardo, P. (2020). Sustainability standards, multicriteria maximin, and viability. *Natural Resource Modeling, 33*(3), e12250. https://doi.org/10.1111/nrm.12250

Engbersen, D., Biesbroek, R., & Termeer, C. J. A. M. (2024). Between theory and action: Assessing the transformative character of climate change adaptation in 51 cases in the Netherlands. *Global Environmental Change, 89*, 102948. https://doi.org/10.1016/j.gloenvcha.2024.102948

Fedele, G., Donatti, C. I., Harvey, C. A., Hannah, L., & Hole, D. G. (2019). Transformative adaptation to climate change for sustainable social-ecological systems. *Environmental Science & Policy, 101*, 116–125. https://doi.org/10.1016/j.envsci.2019.07.001

Folke, C., Carpenter, S. R., Walker, B., Scheffer, M., Chapin, T., III, & Rockström, J. (2010). Resilience thinking: Integrating resilience, adaptability and transformability. *Ecology and Society, 15*(4), Article 20. https://doi.org/10.5751/ES-03610-150420

Haasnoot, M., Kwakkel, J. H., Walker, W. E., & ter Maat, J. (2013). Dynamic adaptive policy pathways: A method for crafting robust decisions for a deeply uncertain world. *Global Environmental Change, 23*(2), 485–498. https://doi.org/10.1016/j.gloenvcha.2012.12.006

Kates, R. W., Travis, W. R., & Wilbanks, T. J. (2012). Transformational adaptation when incremental adaptations to climate change are insufficient. *Proceedings of the National Academy of Sciences, 109*(19), 7156–7161. https://doi.org/10.1073/pnas.1115521109

Kaya, H. D., Chan, P. W. C., Schraven, D. F. J., & Leijten, M. (2025). Infrastructure in transitions: A systematic review of how infrastructure influences and is influenced by sustainability transitions. *Environmental Innovation and Societal Transitions, 57*, 101034. https://doi.org/10.1016/j.eist.2025.101034

Köhler, J., Geels, F. W., Kern, F., Markard, J., Onsongo, E., Wieczorek, A., et al. (2019). An agenda for sustainability transitions research: State of the art and future directions. *Environmental Innovation and Societal Transitions, 31*, 1–32. https://doi.org/10.1016/j.eist.2019.01.004

Loorbach, D., Frantzeskaki, N., & Avelino, F. (2017). Sustainability transitions research: Transforming science and practice for societal change. *Annual Review of Environment and Resources, 42*, 599–626. https://doi.org/10.1146/annurev-environ-102014-021340

Magnan, A. K., Schipper, E. L. F., Burkett, M., Bharwani, S., Burton, I., Eriksen, S., Gemenne, F., Schaar, J., & Ziervogel, G. (2016). Addressing the risk of maladaptation to climate change. *WIREs Climate Change, 7*(5), 646–665. https://doi.org/10.1002/wcc.409

Markolf, S. A., Chester, M. V., Eisenberg, D. A., Iwaniec, D. M., Davidson, C. I., Zimmerman, R., et al. (2018). Interdependent infrastructure as linked social, ecological, and technological systems (SETSs) to address lock-in and enhance resilience. *Earth's Future, 6*(12), 1638–1659. https://doi.org/10.1029/2018EF000926

Seto, K. C., Davis, S. J., Mitchell, R. B., Stokes, E. C., Unruh, G., & Ürge-Vorsatz, D. (2016). Carbon lock-in: Types, causes, and policy implications. *Annual Review of Environment and Resources, 41*, 425–452. https://doi.org/10.1146/annurev-environ-110615-085934

Termeer, C. J. A. M., Dewulf, A., & Biesbroek, R. (2024). Three archetypical governance pathways for transformative change toward sustainability. *Current Opinion in Environmental Sustainability, 71*, 101479. https://doi.org/10.1016/j.cosust.2024.101479

Walker, B., Holling, C. S., Carpenter, S. R., & Kinzig, A. (2004). Resilience, adaptability and transformability in social-ecological systems. *Ecology and Society, 9*(2), Article 5. https://doi.org/10.5751/ES-00650-090205

Werners, S. E., van Slobbe, E., Bölscher, T., Oost, A., Pfenninger, S., Trombi, G., Bindi, M., & Moriondo, M. (2015). Turning points in climate change adaptation. *Ecology and Society, 20*(4), Article 3. https://doi.org/10.5751/ES-07403-200403
