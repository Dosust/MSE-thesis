# RS-01 / RS-02 Evidence Qualification v1

**Date:** 2026-09-16  
**Method:** EGMIV + existing engineering–sustainability evidence rules  
**Status:** PRIOR-ART / MECHANISM QUALIFICATION COMPLETE AT SCHOLARLY-PASSAGE LEVEL; thesis-specific sustainability functionals and empirical calibration remain pending  
**Parent specification:** `12_THESIS_RS_TRANSLATION_EXTENSION.md`

## 1. Gate rule

For each candidate translation path, evidence is separated into four non-substitutable claims:

```math
\boxed{
E_M\;\text{(mechanism)}
\neq
E_R\;\text{(resilience quantification)}
\neq
E_S\;\text{(sustainability consequence)}
\neq
E_D\;\text{(decision value)}.
}
```

A paper supporting `E_M` does not automatically support `E_S`. A quantified cost or social-loss term is a consequence quantity, but it is not automatically a validated sustainability assessment.

---

# 2. RS-01 — Power-to-Transportation through charging availability

## 2.1 Candidate thesis path

```math
P\text{-side electricity/charger failure}
\rightarrow
\text{charging-capacity loss}
\rightarrow
\text{EV queue/rerouting/delay}
\rightarrow
\text{mobility-service degradation}
\rightarrow
J_{access},J_{cost},J_{carbon}\;? 
```

## 2.2 Strong prior-art anchor

Wang, Abdin, Fang & Zio (2021), *Resilience assessment of electrified road networks subject to charging station failures*, Computer-Aided Civil and Infrastructure Engineering, DOI `10.1111/mice.12736`.

The paper explicitly models electrified-road-network dependence on fast-charging stations using a CTM-based two-stage system-optimal dynamic traffic assignment formulation. The modeled state/configuration includes FCS location, charger capacity, charging speed, EV driving range, charging time and state of charge. FCS failure is represented by time-dependent charging capability, including zero charging speed during complete station failure.

The paper defines:
- cumulative throughput performance as actual cumulative arrivals under failure divided by expected cumulative arrivals under no failure;
- a resilience metric based on average performance over the investigated time horizon;
- FCS cumulative utilization based on cumulative supplied energy levels;
- total travel time as the traffic-assignment objective.

It reports that longer FCS failure duration, higher EV penetration and simultaneous failures reduce resilience and increase total travel time. It also identifies resilience-critical FCSs and proposes backup-electricity placement as an operational/planning implication.

### Adjudication

```text
E_M = SUPPORTED_MECHANISM
E_R = QUANTIFIED_IN_PRIOR_ART
E_S = NOT ESTABLISHED FOR THESIS OUTCOMES
E_D = PRIOR-ART DECISION GUIDANCE EXISTS
```

Therefore the thesis must not claim novelty for

```math
\text{charger/power failure}\rightarrow\text{EV mobility resilience loss}
```

or for ranking charging stations by their resilience impact.

## 2.3 Sustainability-translation gap for RS-01

The Wang et al. model optimizes/quantifies travel-time and throughput consequences, but the retrieved evidence does not establish a complete transformation from those trajectories to carbon, lifecycle cost, or distributional accessibility outcomes.

Hence the thesis-specific unresolved step is narrower:

```math
\boxed{
Y_T(t),q_c(t),P_c(t),\text{travel/charging trajectories}
\rightarrow
J_j\text{ with declared units, horizon, data and validation}.
}
```

Candidate consequence quantities must be separately qualified. A useful indicator taxonomy exists in Ramírez-Villamil et al. (2025), DOI `10.1155/atr/8859606`, which catalogues transportation sustainability indicators including emissions, energy/electricity consumption, charging costs, travel distance/time, waiting/charging time, EV queues, demand fulfilment and service level. This taxonomy supports candidate-variable selection; it does not provide a universal causal coefficient for RS-01.

### RS-01 current state

```math
\boxed{
RS01:\quad
\mathfrak d_{P\to T}\rightarrow R_T
\;\textbf{is prior art};
\qquad
\mathfrak d_{P\to T}\rightarrow Y\rightarrow J_{sus}\rightarrow\text{validated transformation decision value}
\;\textbf{remains thesis-specific and validation-dependent}.
}
```

---

# 3. RS-02 — Transportation-to-Power through restoration access

## 3.1 Candidate thesis path

```math
\text{road disruption/congestion}
\rightarrow
\text{crew travel time}
\rightarrow
\text{repair/restoration time}
\rightarrow
\text{power service loss}
\rightarrow
J_{cost},J_{carbon},J_{access}\;?
```

## 3.2 Very close prior-art anchor

Chen, Shi, Chen & Wei (2021), *A Resilience Enhancement Model for Complex Distribution Network Coupling with Human Resources and Traffic Network*, Complexity, DOI `10.1155/2021/2051719`.

This paper explicitly treats post-hurricane restoration as a coupled distribution–traffic–human-resource system. It states that road conditions alter repair-team route choice and transportation cost, while traffic time directly changes repair time and therefore distribution-system resilience. Human-resource capability further changes task execution time.

The optimization accounts for repair demand, traffic cost and repair-team capability with the objective of reducing social loss during the repair process. It defines an economic-loss-rate resilience quantity

```math
R_3=\frac{M_{\Delta}}{M_0},
```

with economic loss

```math
M
=
\sum_{i=1}^{m+n}
 e^{loss}_{x_i,k}\!\left(t(x_i)\right)L(x_i),
\qquad k\in\{1,2,3,4,5\},
```

where the five load categories are industry, business, medicine/health, government and public utilities and the loss function depends on outage duration.

The paper reports that improving repair-personnel capability increases repair rate and system resilience and decreases economic loss, while also showing that economic-loss behavior is not identical to the aggregate resilience measure because load types have heterogeneous loss consequences.

### Adjudication

```text
E_M = SUPPORTED_MECHANISM
E_R = QUANTIFIED_IN_PRIOR_ART
E_S(economic/social consequence) = QUANTIFIED_CONSEQUENCE_IN_PRIOR_ART
E_D = OPTIMIZATION/REPAIR-PLAN DECISION PRIOR ART
```

This is a close subtraction result. The thesis must not claim novelty for

```math
\text{road access}\rightarrow\text{crew delay}\rightarrow\text{power restoration}\rightarrow\text{economic/social loss}
```

as a generic chain.

## 3.3 Additional prior-art anchors

- Anokhin et al. (2021), DOI `10.1111/poms.13393`: coordinated mobile power sources and repair crews subject to energy- and transportation-network constraints for resilience delivery.
- Liu et al. (2026), DOI `10.1002/tee.70253`: real-time routing/scheduling of mobile emergency generators in coupled distribution–transportation networks; travel time affects restoration speed.
- Zhang et al. (2026), DOI `10.1002/ese3.70544`: post-disaster co-optimization includes repair time, economic loss, labor cost and repair efficiency.
- Liu et al. (2022), DOI `10.1002/eqe.3701`: demonstrates that resilience-loss-based and economic-loss-based retrofit objectives can produce different infrastructure decisions.

## 3.4 Thesis-specific residual for RS-02

The defensible residual is not the causal chain itself. It is whether the thesis can establish, on a matched P–T–I–O demonstrator and qualified data,

```math
\boxed{
\mathfrak d_e
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Y_{0:T}
\rightarrow
\{R_i,J_j\}
\rightarrow
\Phi_{ST}
\rightarrow
\Delta\text{decision value}
}
```

under explicit uncertainty and comparison against simpler/static representations.

---

# 4. Cross-path scientific conclusion

The new audit rejects the simple thesis story

```math
\text{find interdependencies}\rightarrow\text{invent resilience-sustainability mapping}.
```

A stronger thesis story is

```math
\boxed{
\text{qualify mechanisms}
\rightarrow
\text{build validated dynamic P--T--I--O trajectories}
\rightarrow
\text{keep resilience and sustainability quantities distinct}
\rightarrow
\text{derive trajectory-based consequence functionals}
\rightarrow
\text{test whether this integrated representation changes engineering decisions}.
}
```

This is the current purpose-driven residual.

---

# 5. Immediate next mathematical tasks

The next admissible specification is to define candidate consequence functionals for RS-01 and RS-02 without assigning empirical parameter values prematurely.

For a generic consequence `j`, use

```math
J_j
=
\int_0^{T_L}\ell_j(Y(t),u(t),\mathbf a,\omega,t)dt
+\phi_j(Y(T_L),\mathbf a,\omega).
```

The first candidate components to evidence-qualify are:

```math
J_{cost},\qquad J_{access},\qquad J_{carbon}.
```

Each must pass

```math
A_j
=\mathbb 1[Def_j\land Unit_j\land Data_j\land Mechanism_j\land Horizon_j\land Validation_j].
```

No parameter, threshold or weighting is to be frozen from this prior-art pass.

---

# 6. Evidence provenance

Scholarly passages were retrieved through Scholar Gateway on 2026-09-16. DOI/source documents remain authoritative. This file records a structured evidence adjudication, not a substitute for full-text verification in the final thesis corpus.
