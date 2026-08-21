# MASTER RESEARCH MEMORY — Six-Chain Mathematical Physics Review

**Snapshot:** 2026-08-21, Singapore time  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Branch created for this snapshot:** `research-memory/2026-08-21-six-chain-ontology`

## 1. Purpose

This memory package preserves the scientific state reached in the conversation about identifying the **full chains and layers where mathematics and physics apply to sustainable and resilient infrastructure systems**. It is designed for rigorous recall, reproducibility, systematic-review coding, figure reconstruction, and future ChatGPT sessions.

The package must never imply that one existing paper proposed the complete architecture. The **six-chain integration is a literature-grounded synthesis**. Individual layers, theories, equations, methods, and distinctions are anchored in prior literature.

---

## 2. Central review-paper proposition

### Working title

**A Mathematical–Physical Ontology of Sustainable and Resilient Infrastructure Systems: From Governing Laws to Societal Learning**

### Core question

> **Where, exactly, do mathematics and physics enter the complete science of sustainable and resilient infrastructure systems?**

### Defensible contribution statement

> The literature contains recurrent but fragmented scientific layers. Through systematic synthesis, these layers can be organized into six interacting analytical chains spanning physical laws, knowledge generation, disturbance propagation, viability and recovery, engineering lifecycle intervention, and societal decision-learning.

The paper should therefore identify, for each layer:

- the scientific question;
- physical variables/laws;
- mathematical object/model class;
- representative formula(s);
- uncertainty treatment;
- infrastructure sector(s);
- data/observation requirements;
- representative literature;
- validation/case-study basis;
- limitations and author-stated gaps;
- whether the relation is established literature or thesis synthesis.

---

# 3. The six interacting scientific chains

## Chain I — Physical System

**Question:** What is the system?

### Full chain

`Physical Laws → Components → Topology → Interfaces → States & Flows → Dynamics → Cascades`

### Layers

1. Physical laws and constitutive foundations
2. Infrastructure components / asset states
3. System representation and topology
4. Interdependencies and interfaces
5. Coupled states, stocks, flows and capacities
6. Nonlinear / hybrid / stochastic dynamics
7. Disturbance propagation and cascading behavior

### Representative mathematics/physics

Conservation:

`∂ρ_i/∂t + ∇·J_i = s_i`

Graph/network representation:

`G=(V,E)`, `L=D−A`

Multilayer system:

`M={G^[1],...,G^[m],C}`

Dynamic interface:

`y_ij(t)=g_ij(x_i(t),x_j(t),θ_ij,τ_ij,m_ij)`

Coupled dynamics:

`ẋ_i=f_i(x_i,u_i,η_i)+Σ_{j≠i} g_ij(x_i,x_j;θ_ij)`

### Primary scientific anchors

Rinaldi et al. (2001); Ouyang (2014); Garavello (2010); Motter & Lai (2002); Buldyrev et al. (2010); Boccaletti et al. (2014); Kivelä et al. (2014); Gao et al. (2016).

### Frozen distinction

**Topology ≠ interdependency ≠ interface mechanism.**

A graph edge alone does not specify transfer law, direction, threshold, delay, capacity, mode, or failure mechanism.

---

## Chain II — Observation, Inference and Prediction

**Question:** What do we know, and how confidently do we know it?

### Full chain

`Measurement → Observability → Identification → Calibration → State Estimation → Data Assimilation → Uncertainty Quantification → Prediction`

### Representative mathematics

Observation:

`y_k=h(x_k,θ)+ε_k`

Observability:

`rank(O)=n`

Bayesian identification:

`π(θ|y) ∝ p(y|θ)π_0(θ)`

Regularized inverse inference:

`θ_hat = argmin_θ ||y−H(θ)||² + λR(θ)`

State estimation:

`p(x_k|y_1:k)`

Prediction:

`p(x_{k+1}|y_1:k)=∫p(x_{k+1}|x_k)p(x_k|y_1:k)dx_k`

### Primary anchors

Stuart (2010); Huang et al. (2019); Naderi & Shojaei (2023); Castelletti et al. (2023).

### Scientific role

This chain is epistemic: it separates the **real physical state** from what can be measured, inferred and predicted. It is the natural home for inverse problems, identifiability, Bayesian inference, data assimilation, digital twins and UQ.

---

## Chain III — Stress, Failure, Service Loss and Consequence

**Question:** How does a stressor become infrastructure failure and societal harm?

### Full chain

`Hazard → Exposure → Vulnerability → Fragility → Damage/Failure → Interdependent Cascade → Functional Loss → Service Loss → Human/Socio-technical Response → Consequences → Risk/Criticality`

### Mandatory state-to-society mapping

`X(t) → F(t) → S(t) → C(t)`

where:

- `X(t)` = physical state;
- `F(t)` = functionality/capability;
- `S(t)` = delivered service;
- `C(t)` = consequence to population/economy/environment/institutions.

### Representative mathematics

Hazard exceedance:

`P(H>h)`

Fragility:

`P(D≥d | H=h)`

Failure probability:

`P_f=P[g(X,H)≤0]`

Service deficit:

`L_s(t)=1−S(t)/S_0`

Expected consequence:

`E[C]=∫C(ℓ)p(ℓ)dℓ`

### Primary anchors

Argyroudis et al. (2019); Motter & Lai (2002); Buldyrev et al. (2010); Poulin & Kane (2021); Davidson et al. (2022); Mühlhofer et al. (2023); Magoua & Li (2023).

### Frozen distinction

**Physical damage ≠ component functionality ≠ delivered service ≠ societal consequence.**

---

## Chain IV — Viability, Resilience, Recovery and Control

**Question:** Can the system remain acceptable, survive disturbance, recover and be controlled?

### Full chain

`Preparedness → Absorption → Robustness → Viability → Reachability → Service Continuity → Resilience → Recoverability → Restoration → Resource Allocation → Adaptive Control → New State`

### Representative mathematics

Viability kernel:

`Viab_K={x_0∈K : ∃u(.), x(t;x_0,u)∈K, ∀t}`

Reachable set:

`R(T)={x(T): x(0)=x_0, u∈U, d∈D}`

Hamilton–Jacobi–Isaacs reachability:

`∂_t V + min_u max_d ∇Vᵀf(x,u,d)=0`

Bruneau-type resilience loss:

`L_R=∫[1−Q(t)]dt`

Henry–Ramírez-Márquez recovery ratio:

`R(t)=[φ(t)−φ(t_d)]/[φ(t_0)−φ(t_d)]`

Generic recovery dynamics:

`r_dot=F_R(r,u,b,G)`

### Primary anchors

Bruneau et al. (2003); Henry & Ramírez-Márquez (2012); Hosseini et al. (2016); Saint-Pierre (1994); Mitchell et al. (2005); Bansal et al. (2017); Lygeros et al. (1999); Ouyang & Wang (2015); Xu et al. (2026); Castelletti et al. (2023).

### Frozen distinctions

- Viability/reachability are not synonyms for resilience metrics.
- Recovery/restoration must be explicit; it has dynamics, sequencing and resource constraints.

---

## Chain V — Engineering Lifecycle

**Question:** What can engineers design, operate, maintain, plan and adapt?

### Full chain

`Requirements → Design → Deploy → Commission → Operate → Monitor → Age → Maintain → Repair/Replace → Retrofit/Expand → Plan → Adapt → Transform → Decommission/Circularize`

### Representative mathematics

Constrained design:

`x*=argmin_x J_d(x)` subject to `g(x)≤0`, `h(x)=0`

Optimal operation:

`u*=argmin_u ∫c(x(t),u(t))dt`

Reliability/hazard rate:

`R(t)=P(T_f>t)`

`λ(t)=f_T(t)/(1−F_T(t))`

Sequential maintenance:

`π*=argmin_π E[Σ_t c(X_t,a_t)]`

Robust adaptation:

`a*=argmin_a max_{ω∈Ω} L(a,ω)`

### Primary anchors

D’Ambrosio et al. (2015); Castelletti et al. (2023); Frangopol et al. (2004); Xu et al. (2026); Dittrich et al. (2016); Bonjean Stanton & Roelich (2021); Ding et al. (2023); Bocchini et al. (2014).

### Frozen correction

**Optimization is cross-cutting. It is not a lifecycle stage.**

Optimization acts on design, operation, control, recovery, maintenance, planning, adaptation and societal trade-offs.

---

## Chain VI — Societal Decision and Learning

**Question:** What should society choose?

### Full cycle

`Evaluate → Trade Off → Decide → Implement → Observe Outcomes → Learn → Re-evaluate`

### Evaluation dimensions

`Sustainability + Equity + Risk + Economics/Finance + Governance + Human Behaviour`

### Representative mathematics

Multi-objective vector:

`J(a)=[J_cost,J_carbon,J_reliability,J_resilience,J_equity,J_service]^T`

Pareto set:

`P={a∈A : no a' dominates a}`

MCDA utility:

`U(a)=Σ_k w_k u_k(a)`

Equity/service floor:

`S_g(t)≥S_g^min  ∀g`

Bayesian/sequential learning:

`π_{t+1}(θ) ∝ p(D_{t+1}|θ)π_t(θ)`

### Primary anchors

Bocchini et al. (2014); Navarro & Yepes (2019); Coleman et al. (2024); Endo et al. (2023); Meng et al. (2024); Hausken et al. (2025); Dittrich et al. (2016); Bonjean Stanton & Roelich (2021).

### Frozen distinction

Sustainability, equity, economics/finance, governance and human behaviour are **not downstream physical states**. They are evaluative, normative, behavioral and institutional dimensions acting on and around the physical system.

---

# 4. Cross-chain couplings

The framework is six interacting chains, not one giant arrow.

- **I ↔ II:** physical system state ↔ evidence/observations
- **II ↔ III:** forecast/uncertainty ↔ hazard and stress characterization
- **III ↔ IV:** service loss/consequence ↔ viability and recovery requirements
- **IV ↔ V:** control/recovery ↔ operations, maintenance and engineering action
- **V ↔ VI:** engineering alternatives ↔ societal evaluation and choice
- **VI → I:** implementation/adaptation changes topology, capacities, interface laws and system parameters
- **VI → II:** learning updates priors, inference models and monitoring priorities

Long-loop logic:

`decision → implementation → system outcome → observation → learning → revised model/values → new decision`

---

# 5. Cross-cutting mathematical engines

These are vertical capabilities, not sequential lifecycle stages:

1. ODEs/PDEs/DAEs
2. dynamical systems
3. graph theory and multilayer network science
4. probability and stochastic processes
5. statistics
6. Bayesian inference
7. inverse problems and identifiability
8. uncertainty quantification
9. reliability/risk theory
10. optimization / operations research
11. optimal, robust, stochastic and model-predictive control
12. viability theory and reachability
13. Hamilton–Jacobi / HJI equations
14. differential games / game theory
15. numerical analysis and simulation
16. data assimilation / digital twins
17. machine learning / physics-informed AI
18. MCDA / multi-objective analysis
19. DMDU / robust decision making / adaptive pathways
20. lifecycle and degradation models

---

# 6. Literature anchors that define the intellectual backbone

Core physical/interdependency/network anchors:

- Rinaldi, Peerenboom & Kelly (2001), DOI `10.1109/37.969131`
- Ouyang (2014), DOI `10.1016/j.ress.2013.06.040`
- Garavello (2010), DOI `10.3934/nhm.2010.5.565`
- Motter & Lai (2002), DOI `10.1103/PhysRevE.66.065102`
- Buldyrev et al. (2010), DOI `10.1038/nature08932`
- Boccaletti et al. (2014), DOI `10.1016/j.physrep.2014.07.001`
- Kivelä et al. (2014), DOI `10.1093/comnet/cnu016`
- Gao, Barzel & Barabási (2016), DOI `10.1038/nature16948`

Inference/observation anchors:

- Stuart (2010), DOI `10.1017/S0962492910000061`
- Huang et al. (2019), DOI `10.1177/1369433218811540`

Hazard/service/consequence anchors:

- Argyroudis et al. (2019), DOI `10.1016/j.ress.2019.106567`
- Poulin & Kane (2021), DOI `10.1016/j.ress.2021.107926`
- Davidson et al. (2022), DOI `10.1080/10286608.2022.2067848`
- Mühlhofer et al. (2023), DOI `10.1016/j.ress.2023.109194`
- Magoua & Li (2023), DOI `10.1016/j.ress.2022.109073`

Resilience/viability/recovery/control anchors:

- Bruneau et al. (2003), DOI `10.1193/1.1623497`
- Henry & Ramírez-Márquez (2012), DOI `10.1016/j.ress.2011.09.002`
- Hosseini et al. (2016), DOI `10.1016/j.ress.2015.08.006`
- Saint-Pierre (1994), DOI `10.1007/BF01204182`
- Mitchell, Bayen & Tomlin (2005), DOI `10.1109/TAC.2005.851439`
- Bansal et al. (2017), DOI `10.1109/CDC.2017.8263977`
- Lygeros, Tomlin & Sastry (1999), DOI `10.1016/S0005-1098(98)00193-9`
- Ouyang & Wang (2015), DOI `10.1016/j.ress.2015.03.011`
- Xu et al. (2026), DOI `10.1111/risa.70220`
- Castelletti et al. (2023), DOI `10.1016/j.arcontrol.2023.03.013`

Engineering/sustainability/decision anchors:

- D’Ambrosio et al. (2015), DOI `10.1016/j.ejor.2014.12.039`
- Frangopol et al. (2004), DOI `10.1002/pse.180`
- Bocchini et al. (2014), DOI `10.1061/(ASCE)IS.1943-555X.0000177`
- Navarro & Yepes (2019), DOI `10.1155/2019/6134803`
- Dittrich et al. (2016), DOI `10.1016/j.ecolecon.2015.12.006`
- Bonjean Stanton & Roelich (2021), DOI `10.1016/j.techfore.2021.120939`
- Coleman et al. (2024), DOI `10.1038/s44304-024-00022-x`
- Endo et al. (2023), DOI `10.1177/1087724X221130284`
- Meng et al. (2024), DOI `10.1016/j.sftr.2024.100312`
- Hausken et al. (2025), DOI `10.1016/j.ress.2025.111123`
- Ding et al. (2023), DOI `10.1016/j.jclepro.2023.135981`

---

# 7. Provenance and authenticity rules

1. `USER_REQUESTS_VERBATIM.md` preserves visible user text without correcting wording.
2. Assistant-output summaries are explicitly labeled reconstructed when not byte-for-byte preserved.
3. The six-chain architecture is a synthesis, not attributed to a single paper.
4. A citation next to a representative generic equation normally supports the **concept/method family**, unless source-level verification establishes that exact equation in that source.
5. Full copyrighted PDFs should not be copied into GitHub merely for memory; store DOI, metadata, lawful derived evidence and provenance while keeping full texts in authorized library/Zotero/local storage.
6. Future sessions should append dated snapshots/change logs rather than silently rewriting historical requests.

---

# 8. Reproducibility assets in this folder

- `README.md` — module navigation and frozen high-level state
- `USER_REQUESTS_VERBATIM.md` — exact visible user requests
- `ASSISTANT_OUTPUT_INDEX_RECONSTRUCTED.md` — reconstructed output history
- `SIX_CHAIN_ONTOLOGY.md` — canonical architecture
- `FORMULA_CATALOGUE.md` — equation catalogue
- `FROZEN_DISTINCTIONS.md` — scientific corrections that should not regress
- `REVIEW_PAPER_CONCEPT.md` — proposed review article and coding schema
- `ANCHOR_REFERENCES.md` — DOI-level anchor literature
- `CHAIN_LAYER_MATRIX.csv` — machine-readable layer ontology
- `SCIENTIFIC_STATE.json` — machine-readable frozen state
- `PROVENANCE.md` — authenticity/evidence rules
- `FUTURE_CHAT_BOOTSTRAP.md` — future-chat handoff
- `DRAWIO_REGENERATION.py` — deterministic figure regeneration

---

# 9. Recommended next research operations

1. Freeze the review protocol around this ontology.
2. Search Scopus, Web of Science, Compendex and IEEE Xplore using layer-specific and cross-chain terms.
3. Code each included paper against `CHAIN_LAYER_MATRIX.csv`.
4. Track explicit equations and whether each is verbatim, adapted or generic.
5. Build a paper × layer × mathematics × physics × sector matrix.
6. Compute layer coverage and cross-chain fragmentation.
7. Identify papers that bridge two or more chains.
8. Test whether dynamic-interface identification, viability uncertainty, service-to-population mapping and equity constraints remain underdeveloped.
9. Use full-text evidence to distinguish author-stated gaps from thesis-inferred gaps.
10. Keep Draw.io figures generated from the structured ontology rather than manually drifting away from the evidence state.

# 10. Future-chat rule

A future assistant should read `README.md`, `SCIENTIFIC_STATE.json`, `FUTURE_CHAT_BOOTSTRAP.md`, `FROZEN_DISTINCTIONS.md` and `CHAIN_LAYER_MATRIX.csv` before modifying the architecture. Any proposed addition/removal should state whether it is:

- established in literature;
- an interpretation/synthesis;
- a thesis-original proposition;
- a future hypothesis requiring falsification.
