# Thesis Full Logic Mind Map — v2.0

![Status](https://img.shields.io/badge/status-DRAFT--UNVERIFIED-D97706)
![Framework](https://img.shields.io/badge/framework-v2.1%20ALIGNED-1A7F37)
![Research Contract](https://img.shields.io/badge/RQ%2FSO%2FH-v4.0-0969DA)
![Type](https://img.shields.io/badge/type-DERIVED%20SYNTHESIS-7E22CE)

**Figure ID:** FIG-MINDMAP-THESIS-LOGIC-V2  
**Version:** 2.0  
**Date:** 2026-09-21  
**Status:** DRAFT-UNVERIFIED — scientific synchronization complete; GitHub/render QA pending  
**Evidence state:** [D] thesis-derived synthesis of canonical objects  
**Data status:** conceptual architecture with a dated execution-status branch  
**Framework authority:** [CANONICAL_7_STAGE_FRAMEWORK_V2.md](../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md)  
**Semantic alignment:** [CANONICAL_7_STAGE_FRAMEWORK_V2_1_ALIGNMENT_AMENDMENT.md](../project/CANONICAL_7_STAGE_FRAMEWORK_V2_1_ALIGNMENT_AMENDMENT.md)  
**RQ authority:** [CANONICAL_RESEARCH_QUESTIONS_V4.md](../project/CANONICAL_RESEARCH_QUESTIONS_V4.md)  
**SO/H authority:** [CANONICAL_RQ_SO_HYPOTHESES_V4.md](../project/CANONICAL_RQ_SO_HYPOTHESES_V4.md)  
**Mathematical synthesis:** [PHYSICS_MATHEMATICS_ENGINEERING_SYNTHESIS_V1.md](../project/PHYSICS_MATHEMATICS_ENGINEERING_SYNTHESIS_V1.md)  
**Current execution status:** [AUTONOMOUS_EXECUTION_STATUS.md](../project/AUTONOMOUS_EXECUTION_STATUS.md)  
**Visual QA authority:** [FRAMEWORK_VISUAL_FIDELITY_PROTOCOL_V2.md](FRAMEWORK_VISUAL_FIDELITY_PROTOCOL_V2.md)

> **Guardrail:** this map organizes the current thesis logic. It does **not** create an eighth stage, alter RQ0–RQ7, change SO1–SO7 or H1–H5, promote a case candidate, or convert a proposed construct into a result.

---

# 0. Central thesis identity

The thesis keeps architecture, spatiotemporal structure, and behavior distinct:

~~~math
\boxed{
\underbrace{\mathcal S_{PT}}_{\text{System-of-Systems architecture}}
\neq
\underbrace{\mathfrak G_{PT}(x,t)}_{\text{spatiotemporal structure}}
\neq
\underbrace{F_q[Y(x,t)]}_{\text{complex spatiotemporal behavior}}.
}
~~~

The central identity is

~~~math
\boxed{
\text{Coupled Power--Transportation infrastructure}
=
\underbrace{\text{Interdependent System of Systems}}_{\text{architecture}}
+
\underbrace{\text{Spatiotemporal complex dynamical system}}_{\text{behavior}}.
}
~~~

Physical core:

~~~math
\boxed{P+T}
~~~

Supporting knowledge/action domains:

~~~math
\boxed{I+O}
~~~

Critical electricity and mobility service requirements are an **input** to the framework, not an additional stage.

---

# 1. Master thesis logic map

~~~mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Times New Roman","fontSize":"15px","lineColor":"#475569"}}}%%
flowchart LR
    ROOT["COUPLED POWER–TRANSPORTATION<br/>INFRASTRUCTURE RESILIENCE"]
    INP["INPUT<br/>Critical electricity + mobility<br/>service requirements"]

    subgraph SPINE["SEVEN-STAGE SCIENTIFIC SPINE"]
      direction LR
      S1["1 · SPATIOTEMPORAL<br/>SYSTEM-OF-SYSTEMS<br/>STRUCTURE"]
      S2["2 · EVIDENCE-QUALIFIED<br/>SPATIOTEMPORAL DIRECTIONAL<br/>DEPENDENCIES"]
      G23["2→3 HANDOFF<br/>Identification · provenance<br/>uncertainty · dynamic readiness<br/>NOT A STAGE"]
      S3["3 · COMPLEX<br/>SPATIOTEMPORAL<br/>COUPLED DYNAMICS"]
      S4["4 · OBSERVATION · ESTIMATION<br/>ORGANIZATION · FEASIBLE CONTROL"]
      S5["5 · UNCERTAINTY-AWARE<br/>SPATIOTEMPORAL<br/>SERVICE RESILIENCE"]
      S6["6 · SPATIOTEMPORALLY TARGETED<br/>ENGINEERING INTERVENTION<br/>CONSEQUENCES"]
      S7["7 · DEFENSIBLE<br/>SPATIOTEMPORAL<br/>ENGINEERING DECISION"]
      S1 --> S2 --> G23 --> S3 --> S4 --> S5 --> S6 --> S7
    end

    CTRL["CROSS-CUTTING CONTROLS<br/>Evidence qualification · identification<br/>parameter provenance · VVUQ · sensitivity<br/>falsification · reproducibility · claim ceilings"]
    RC["RESEARCH CONTRACT<br/>RQ0 + RQ1–RQ7<br/>SO1–SO7 · H1–H5"]
    EXE["EXECUTION REALIZATIONS<br/>Gate-controlled cases / data / experiments<br/>not theory authority"]
    FND["FOUNDATIONS<br/>Systems thinking<br/>Systems engineering"]

    ROOT --> INP
    INP --> S1
    ROOT --> CTRL
    ROOT --> RC
    ROOT --> EXE
    ROOT --> FND

    INP -. "service acceptability" .-> S5
    CTRL -. "acts across Stages 1–7" .-> SPINE
    RC -. "tests scientific spine" .-> SPINE
    EXE -. "instantiates selected tests" .-> SPINE
    FND -. "reasoning discipline" .-> SPINE

    classDef root fill:#111827,color:#FFFFFF,stroke:#111827,stroke-width:3px;
    classDef stage fill:#F8FAFC,color:#111827,stroke:#334155,stroke-width:2.5px;
    classDef input fill:#ECFDF5,color:#065F46,stroke:#15803D,stroke-width:2px;
    classDef derived fill:#F5F3FF,color:#4C1D95,stroke:#7E22CE,stroke-width:2px;
    classDef control fill:#EFF6FF,color:#1E3A8A,stroke:#2563EB,stroke-width:2px;
    classDef execution fill:#FFF7ED,color:#7C2D12,stroke:#D97706,stroke-width:2px;
    classDef foundation fill:#F3F4F6,color:#374151,stroke:#6B7280,stroke-width:2px;

    class ROOT root;
    class S1,S2,S3,S4,S5,S6,S7 stage;
    class INP input;
    class G23 derived;
    class CTRL,RC control;
    class EXE execution;
    class FND foundation;
~~~

### Master scientific chain

~~~math
\boxed{
\begin{aligned}
&\text{Critical electricity and mobility services}\\
&\downarrow\\
&\text{1. Spatiotemporal System-of-Systems structure}\\
&\downarrow\\
&\text{2. Evidence-qualified directional dependencies}\\
&\downarrow\\
&\text{Identification / parameter-readiness handoff}\\
&\downarrow\\
&\text{3. Complex spatiotemporal coupled dynamics}\\
&\downarrow\\
&\text{4. Observation, estimation, organization, feasible control}\\
&\downarrow\\
&\text{5. Uncertainty-aware spatiotemporal service resilience}\\
&\downarrow\\
&\text{6. Targeted engineering intervention consequences}\\
&\downarrow\\
&\text{7. Defensible spatiotemporal engineering decision}.
\end{aligned}
}
~~~

The identification/readiness handoff is cross-stage scientific control, **not Stage 2.5**.

---

# 2. Stage 1 — Spatiotemporal System-of-Systems Structure

**Scientific job:** define what constitutes the bounded P–T SoS, where and when its entities and conditions exist, and where/when interaction could occur. Stage 1 is structural and non-causal.

~~~mermaid
flowchart TB
    S1["STAGE 1<br/>SPATIOTEMPORAL SYSTEM-OF-SYSTEMS STRUCTURE"]
    PHY["PHYSICAL CORE · P + T"]
    SUP["SUPPORT DOMAINS · I + O"]
    ST["SPACE + TIME"]
    CAND["CANDIDATE CROSS-SYSTEM<br/>INTERFACES / RELATIONS"]

    S1 --> PHY
    S1 --> SUP
    S1 --> ST
    S1 --> CAND

    PHY --> P["POWER P<br/>buses · feeders · transformers · switches<br/>generation · loads · DER · physical states"]
    PHY --> T["TRANSPORTATION T<br/>junctions · road links · signals<br/>OD demand · paths · mobility states"]

    SUP --> I["INFORMATION I<br/>measurement · communication<br/>availability · estimation"]
    SUP --> O["ORGANIZATION O<br/>authority · coordination · priorities<br/>crews · resources · timing"]

    ST --> GEO["spatial support x<br/>CRS · geography · crosswalks"]
    ST --> TIME["time support t<br/>vintage · event time · horizon<br/>characteristic timescales"]

    CAND --> CI["candidate interface locations"]
    CAND --> CR["candidate structural relations"]
    CAND --> CG["N→N · N→E · E→N · E→E · Path→N<br/>geometry only until qualified"]

    HAZ["EXOGENOUS HAZARD η(x,t)"]
    HAZ -->|"common exposure"| P
    HAZ -->|"common exposure"| T

    classDef power fill:#E5E7EB,color:#0B1F3A,stroke:#0B1F3A,stroke-width:2px;
    classDef transport fill:#ECFDF5,color:#0F766E,stroke:#0F766E,stroke-width:2px;
    classDef info fill:#EFF6FF,color:#1E3A8A,stroke:#2563EB,stroke-width:2px;
    classDef org fill:#FFFBEB,color:#78350F,stroke:#D97706,stroke-width:2px;
    classDef hazard fill:#FEF2F2,color:#991B1B,stroke:#B91C1C,stroke-width:2px;
    classDef candidate fill:#FAF5FF,color:#581C87,stroke:#7E22CE,stroke-width:2px;
    classDef stage fill:#F8FAFC,color:#111827,stroke:#334155,stroke-width:2.5px;

    class S1 stage;
    class P,PHY power;
    class T transport;
    class I info;
    class O org;
    class HAZ hazard;
    class CAND,CI,CR,CG candidate;
~~~

Structural representation:

~~~math
\boxed{
O_1=
\left(
\mathcal S_{PT},
\mathfrak G_{PT}(x,t),
Q_P,
Q_T,
\mathcal I^{cand}
\right).
}
~~~

Permanent firewall:

~~~math
\boxed{
\text{candidate interface}
\neq
\text{qualified mechanism},
\qquad
\text{common exposure}
\neq
\text{causal dependency}.
}
~~~

A multilayer/spatial graph is a representation of the SoS structure; it is not the SoS itself and does not establish causality.

---

# 3. Stage 2 — Evidence-Qualified Spatiotemporal Directional Dependencies

**Scientific job:** convert candidate relations into qualified directional mechanisms only when direction, mechanism, activation, spatiotemporal support, delay/timescale, evidence, uncertainty, and validity are established.

~~~mermaid
flowchart LR
    C["CANDIDATE RELATION<br/>I_cand"]
    Q["QUALIFICATION GATE"]
    D["QUALIFIED DIRECTIONAL<br/>DEPENDENCY I_qualified"]

    C --> Q --> D
    Q --> M["mechanism"]
    Q --> DIR["direction"]
    Q --> A["activation condition"]
    Q --> XS["spatial support"]
    Q --> TS["temporal support"]
    Q --> DEL["delay δ"]
    Q --> TAU["timescale τ"]
    Q --> E["evidence + provenance"]
    Q --> U["uncertainty"]
    Q --> V["validity domain"]

    D --> PT["P → T"]
    D --> TP["T → P"]

    FIRE["FIREWALLS<br/>co-location ≠ dependency<br/>association ≠ causality<br/>P→T does not imply T→P"]
    Q -.-> FIRE
~~~

Canonical transition:

~~~math
\boxed{
\mathcal I^{cand}
\rightarrow
\mathcal I^{qualified}.
}
~~~

Generic qualified dependency:

~~~math
\boxed{
\mathfrak d_e=
\left(
s_e,r_e,M_e,A_e,\delta_e,\tau_e,\theta_e,U_e,E_e,\Omega_e
\right).
}
~~~

This object does not imply that \(\theta_e\) is already identifiable or numerically ready.

---

# 4. Stage 2→3 handoff — identification and dynamic readiness

This handoff is cross-stage scientific control and **does not create an eighth stage**.

~~~mermaid
flowchart LR
    Q["QUALIFIED MECHANISM"]
    PDEF["Parameter definition<br/>meaning · units · equation"]
    ID["Identifiability<br/>structural + practical"]
    PROV["Parameter provenance<br/>data / literature / calibration"]
    UQ["Parameter uncertainty"]
    DR["DYNAMIC READINESS"]
    S3["ADMISSION TO STAGE 3"]

    Q --> PDEF --> ID --> PROV --> UQ --> DR --> S3

    BLOCK["FAIL / OPEN<br/>do not fabricate a numerical substitute"]
    ID -. "not identifiable" .-> BLOCK
    PROV -. "unsupported" .-> BLOCK
    UQ -. "unqualified" .-> BLOCK
~~~

~~~math
\boxed{
\text{mechanism existence}
\neq
\text{parameter identifiability}
\neq
\text{adequate parameter estimation}.
}
~~~

Conceptually:

~~~math
\boxed{
\mathcal I^{qualified}
\rightarrow
\Theta_{\rm id}
\rightarrow
\mathcal I^{ready}
\rightarrow
F_q.
}
~~~

A local diagnostic may use

~~~math
J_\theta
=
\frac{\partial H\mathcal M(\theta)}{\partial\theta},
\qquad
\mathrm{rank}(J_\theta)=\dim(\theta),
~~~

within the declared parameterization and experiment. This is a diagnostic condition, not a universal sufficiency theorem for every model family.

---

# 5. Stage 3 — Complex Spatiotemporal Coupled Dynamics

**Behavior studied:** complex spatiotemporal coupled dynamics.  
**Principal representation:** physics-based hybrid multiscale dynamics.

~~~mermaid
flowchart TB
    S3["STAGE 3<br/>COMPLEX SPATIOTEMPORAL COUPLED DYNAMICS"]
    P["Native Power physics F_P"]
    T["Native Transportation dynamics F_T"]
    C["Qualified directional coupling operators"]
    M["Hybrid mode m(t)<br/>failure · switching · restoration"]
    D["Delays + characteristic timescales"]
    H["Hazard η(x,t)"]
    Y["Coupled state Y(x,t)"]
    OUT["Electricity + mobility<br/>service trajectories"]

    S3 --> P
    S3 --> T
    S3 --> C
    S3 --> M
    S3 --> D
    S3 --> H

    P --> Y
    T --> Y
    C --> Y
    M --> Y
    D --> Y
    H --> Y
    Y --> OUT
~~~

Canonical conceptual dynamics:

~~~math
\boxed{
\frac{\partial Y(x,t)}{\partial t}
=
F_q
\left(
Y(x,t),u(x,t),\eta(x,t);
\theta,\mathcal I^{ready}(x,t)
\right).
}
~~~

Hybrid reset, where justified:

~~~math
Y^+=J_{q\rightarrow q'}(\cdot).
~~~

Directional coupling remains asymmetric in general:

~~~math
\boxed{
C_{PT}\neq C_{TP}.
}
~~~

Event time, causal/process delay, and characteristic timescale remain distinct:

~~~math
\boxed{
t_e\neq\delta_e\neq\tau_e.
}
~~~

H1 model family:

~~~math
\boxed{
M_0=\text{independent},
\qquad
M_1=\text{static coupling},
\qquad
M_2=\text{dynamic qualified coupling}.
}
~~~

Primary H1 comparison:

~~~math
\boxed{
M_2\ \text{vs}\ M_1,
\qquad
M_0\ \text{reference}.
}
~~~

---

# 6. Stage 4 — Spatiotemporal Observation, Estimation, Organization, and Feasible Control

~~~mermaid
flowchart LR
    Y["Physical truth<br/>Y(x,t)"]
    OBS["Observation<br/>y(x,t)"]
    EST["Estimated state<br/>Ŷ(x,t)"]
    IO["Information + Organization<br/>(I,O)"]
    UF["Feasible action set<br/>U_feas(x,t)"]
    U["Operational control<br/>u(x,t)"]

    Y --> OBS --> EST --> IO --> UF --> U
    U -->|"feedback"| Y

    LIM["physical possibility<br/>≠<br/>operational feasibility"]
    IO -.-> LIM
~~~

~~~math
\boxed{
Y(x,t)
\rightarrow
y(x,t)
\rightarrow
\widehat Y(x,t)
\rightarrow
(I,O)
\rightarrow
\mathcal U_{\rm feas}(x,t)
\rightarrow
u(x,t).
}
~~~

Required distinctions:

~~~math
\boxed{
Y\neq y\neq\widehat Y,
\qquad
u(x,t)\neq a_k.
}
~~~

---

# 7. Stage 5 — Uncertainty-Aware Spatiotemporal Service Resilience

~~~mermaid
flowchart TB
    K["Acceptable service set<br/>K_sus(x,t)"]
    V["VIABILITY<br/>Remain acceptable"]
    R["RECOVERY REACHABILITY<br/>Return acceptably"]
    G["UNCERTAINTY QUALIFICATION Γ_U"]
    C["Conventional service / recovery<br/>measures — comparator"]
    INC["Incremental information test<br/>H3"]
    CRIT["Interface criticality<br/>supporting diagnostic<br/>only where evidence permits"]

    K --> V
    K --> R
    G --> V
    G --> R
    V --> INC
    R --> INC
    C --> INC
    V -.-> CRIT
    R -.-> CRIT

    G --> GP["probabilistic<br/>if defensible"]
    G --> GS["scenario"]
    G --> GI["interval / bounded"]
    G --> GR["robust"]
    G --> GSA["sensitivity"]
~~~

Canonical composition:

~~~math
\boxed{
\text{Resilience}
=
\underbrace{\text{Remain}}_{\text{viability}}
+
\underbrace{\text{Return}}_{\text{reachability}}
+
\underbrace{\text{Uncertainty qualification}}_{\Gamma_U}.
}
~~~

The plus signs denote conceptual composition, not arithmetic addition.

~~~math
\boxed{
\Gamma_U=
\begin{cases}
\text{probabilistic qualification}, & \text{if a probability model is defensible},\\
\text{scenario / interval / robust / sensitivity qualification}, & \text{otherwise}.
\end{cases}
}
~~~

Top-level objects:

~~~math
\boxed{
K_{\rm sus},
\qquad
\mathcal V,
\qquad
\mathcal R,
\qquad
\Gamma_U.
}
~~~

H3 tests incremental predictive or decision-relevant information beyond prespecified conventional service/recovery measures. Superiority is not assumed.

---

# 8. Stage 6 — Spatiotemporally Targeted Engineering Intervention Consequences

Diagnosis may identify where intervention is relevant; independent requirements/evidence determine what is required. Diagnosis is therefore a supporting input, not the Stage-6 identity.

~~~mermaid
flowchart TB
    D["Supporting diagnosis<br/>critical interfaces · bottlenecks<br/>propagation / recovery sensitivity"]
    A["Engineering intervention a_k<br/>type · location · timing · scale"]
    RE["Resilience effect<br/>ΔR"]
    RR["Resource requirements<br/>direct cost · operational energy"]
    EF["Resource efficiency"]
    SUS["Admitted sustainability consequence<br/>CO2e core"]
    FEAS["Feasibility"]
    U["Uncertainty"]
    COND["Accessibility / equity<br/>CONDITIONAL — separately qualified"]
    C["Typed consequence object C(a_k)"]

    D --> A
    A --> RE
    A --> RR
    A --> EF
    A --> SUS
    A --> FEAS
    A --> U
    A -.-> COND

    RE --> C
    RR --> C
    EF --> C
    SUS --> C
    FEAS --> C
    U --> C
~~~

Canonical typed consequence object:

~~~math
\boxed{
\mathcal C(a_k)
=
\left(
\Delta\mathfrak R^{a_k},
\mathbf r^{a_k},
\mathcal E_{\rm fx}^{a_k},
\mathcal E_{\rm fy}^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k},
\mathcal F^{a_k},
\mathbf U^{a_k}
\right).
}
~~~

Permanent distinction:

~~~math
\boxed{
\text{resilience effect}
\neq
\text{effectiveness}
\neq
\text{resource requirement}
\neq
\text{resource efficiency}
\neq
\text{admitted sustainability consequence}.
}
~~~

Core resources:

~~~math
\boxed{
\mathbf r_{\rm core}
\subseteq
(C_{\rm direct},E_{\rm op}).
}
~~~

Core admitted environmental consequence:

~~~math
\boxed{
\mathbf J_{\rm sus,core}
\subseteq
(CO_{2e}).
}
~~~

Accessibility/equity is conditional on separate qualification.

---

# 9. Stage 7 — Defensible Spatiotemporal Engineering Decision

~~~mermaid
flowchart LR
    CAN["Candidate alternatives"]
    F["Feasibility"]
    N["Native-unit criteria"]
    P["Pareto / dominance"]
    RR["Robustness / regret"]
    V["Preference / value model<br/>only if independently justified"]
    DEF["DEFENSIBLE<br/>DECISION SET"]
    AD["Adaptive / sequential pathways<br/>CONDITIONAL EXTENSION"]

    CAN --> F --> N --> P --> RR --> DEF
    RR -.-> V -.-> DEF
    DEF -.-> AD
~~~

Canonical ordering:

~~~math
\boxed{
\text{feasibility}
\rightarrow
\text{native-unit criteria}
\rightarrow
\text{Pareto/dominance}
\rightarrow
\text{robustness/regret}
\rightarrow
\text{preference/value model if independently justified}.
}
~~~

Primary H5 comparison:

~~~math
\boxed{
\mathcal A_R^\star
\quad\text{vs}\quad
\mathcal A_{\rm joint}^\star.
}
~~~

Guardrail:

~~~math
\boxed{
\text{defensible}
\neq
\text{universally optimal}.
}
~~~

Adaptive/sequential pathways remain conditional and do not define primary H5.

---

# 10. RQ–SO–H research-contract branch

~~~mermaid
flowchart TB
    RQ0["RQ0<br/>Overarching synthesis question"]
    PRE["RQ1/SO1 + RQ2/SO2<br/>STRUCTURAL + DEPENDENCY<br/>PREREQUISITES"]

    H1["RQ3/SO3 → H1<br/>Dynamic qualified coupling<br/>M2 vs M1; M0 reference"]
    H2["RQ4/SO4 → H2<br/>Matched information /<br/>organization contrasts"]
    H3["RQ5/SO5 → H3<br/>Conventional measures vs<br/>viability/reachability augmentation"]
    H4["RQ6/SO6 → H4<br/>Intervention-consequence<br/>heterogeneity"]
    H5["RQ7/SO7 → H5<br/>Resilience-only vs<br/>joint engineering decision"]

    N["H1–H5 STATUS<br/>NOT TESTED unless confirmatory<br/>prerequisites close"]

    PRE --> H1
    H1 --> RQ0
    H2 --> RQ0
    H3 --> RQ0
    H4 --> RQ0
    H5 --> RQ0

    H1 --> N
    H2 --> N
    H3 --> N
    H4 --> N
    H5 --> N
~~~

Canonical mapping:

~~~math
\boxed{
RQ_1/SO_1+RQ_2/SO_2
\rightarrow
\text{structural/dependency prerequisites}.
}
~~~

~~~math
\boxed{
RQ_3/SO_3\rightarrow H_1,\quad
RQ_4/SO_4\rightarrow H_2,\quad
RQ_5/SO_5\rightarrow H_3,\quad
RQ_6/SO_6\rightarrow H_4,\quad
RQ_7/SO_7\rightarrow H_5.
}
~~~

H2 is defined by matched information/organization contrasts; a specific P+T, P+T+I, P+T+I+O implementation is subordinate to that canonical meaning.

---

# 11. Cross-cutting scientific-control branch

~~~mermaid
flowchart TB
    C["CROSS-CUTTING SCIENTIFIC CONTROLS"]
    C --> E["Evidence qualification"]
    C --> ID["Identification + identifiability"]
    C --> PP["Parameter provenance"]
    C --> VER["Verification"]
    C --> VAL["Validation"]
    C --> UQ["Uncertainty quantification"]
    C --> SA["Sensitivity analysis"]
    C --> F["Falsification / NOT TESTED logic"]
    C --> R["Reproducibility"]
    C --> CL["Claim + validity ceilings"]

    CHAIN["Qualified mechanism<br/>→ identifiable parameterization<br/>→ estimated/qualified parameter<br/>→ verified dynamics<br/>→ validation<br/>→ uncertainty propagation<br/>→ resilience<br/>→ decision"]
    C --> CHAIN
~~~

~~~math
\boxed{
\text{verification PASS}
\not\Rightarrow
\text{validation PASS}
\not\Rightarrow
\text{hypothesis support}.
}
~~~

---

# 12. Gate-controlled execution-realization branch

This branch is a dated execution snapshot, **not part of the canonical seven-stage theory**.

~~~mermaid
flowchart TB
    EX["EXECUTION REALIZATIONS<br/>Snapshot: 2026-09-21"]

    AUS["Austin AUS-P5U-2018-V1<br/>ACTIVE CASE CANDIDATE<br/>NOT YET ADMISSIBLE"]
    HOU["Houston H3 demonstrator<br/>ARCHITECTURE FROZEN<br/>CONFIRMATORY EXECUTION BLOCKED"]
    NYC["NYC / ACN H1 public architecture<br/>PARTIAL-PASS / COMPONENT<br/>VALIDATION ROLES ONLY"]

    EX --> AUS
    EX --> HOU
    EX --> NYC

    AUS --> AP["SMART-DS 2018 AUS/P5U<br/>TxDOT 2018 roads<br/>2018 radar candidate<br/>retrospective signals<br/>static flood support"]
    AUS --> AG["G0 PASS<br/>G1–G8 not all closed<br/>FINAL = NOT YET PASS"]

    HOU --> HP["SMART-DS power + H-GAC roads<br/>traffic signals + Harvey hazard support"]
    HOU --> HM["P→T signal-power<br/>T→P repair-access<br/>primary H3 architecture"]

    NYC --> NP["NYC storm-event aggregate arm"]
    NYC --> NA["ACN charging-component arm"]
~~~

No case branch changes the general theory or establishes its full validity domain.

---

# 13. Compact hierarchy for XMind / presentation conversion

~~~text
Coupled Power–Transportation Infrastructure Resilience
├── INPUT
│   └── Critical electricity + mobility service requirements
├── SEVEN-STAGE SCIENTIFIC SPINE
│   ├── 1 · Spatiotemporal System-of-Systems Structure
│   │   ├── Physical core P + T
│   │   ├── Supporting domains I + O
│   │   ├── Space + time
│   │   ├── Candidate interfaces / structural relations
│   │   └── Common hazard exposure ≠ dependency
│   ├── 2 · Evidence-Qualified Spatiotemporal Directional Dependencies
│   │   ├── P→T
│   │   ├── T→P
│   │   ├── mechanism + direction + activation
│   │   ├── space + time + delay + timescale
│   │   └── evidence + uncertainty + validity
│   ├── 2→3 HANDOFF [not a stage]
│   │   ├── parameter definition
│   │   ├── identifiability
│   │   ├── provenance
│   │   ├── uncertainty
│   │   └── dynamic readiness
│   ├── 3 · Complex Spatiotemporal Coupled Dynamics
│   │   ├── native power physics
│   │   ├── native transportation dynamics
│   │   ├── directional coupling operators
│   │   ├── hybrid modes / resets
│   │   └── propagation + service trajectories
│   ├── 4 · Observation, Estimation, Organization, Feasible Control
│   │   └── Y → y → Ŷ → (I,O) → U_feas → u
│   ├── 5 · Uncertainty-Aware Spatiotemporal Service Resilience
│   │   ├── K_sus
│   │   ├── viability — remain
│   │   ├── recovery reachability — return
│   │   ├── uncertainty qualification Γ_U
│   │   └── conventional-measure comparator
│   ├── 6 · Spatiotemporally Targeted Engineering Intervention Consequences
│   │   ├── intervention a_k
│   │   ├── resilience effect
│   │   ├── resource requirements
│   │   ├── resource efficiency
│   │   ├── admitted sustainability consequence
│   │   ├── feasibility
│   │   └── uncertainty
│   └── 7 · Defensible Spatiotemporal Engineering Decision
│       ├── feasibility
│       ├── native-unit criteria
│       ├── Pareto / dominance
│       ├── robustness / regret
│       ├── preference model if justified
│       └── adaptive pathways [conditional]
├── CROSS-CUTTING CONTROLS
│   ├── evidence qualification
│   ├── identification + parameter provenance
│   ├── verification + validation + UQ
│   ├── sensitivity + falsification
│   ├── reproducibility
│   └── claim / validity ceilings
├── RESEARCH CONTRACT
│   ├── RQ1/SO1 + RQ2/SO2 → prerequisites
│   ├── RQ3/SO3 → H1
│   ├── RQ4/SO4 → H2
│   ├── RQ5/SO5 → H3
│   ├── RQ6/SO6 → H4
│   ├── RQ7/SO7 → H5
│   └── H1–H5 = NOT TESTED unless prerequisites close
├── EXECUTION REALIZATIONS [gate-controlled]
│   ├── Austin AUS-P5U-2018-V1 — active candidate / not admissible
│   ├── Houston H3 — frozen architecture / execution blocked
│   └── NYC/ACN H1 — partial/component validation roles
└── FOUNDATIONS
    ├── systems thinking
    └── systems engineering
~~~

---

# 14. Figure interpretation rules

1. Exactly seven stages remain authoritative. Input, the Stage-2→3 identification handoff, cross-cutting controls, research contract, foundations, and case realizations are not additional stages.
2. SoS architecture, spatiotemporal structure, and complex dynamics are distinct objects.
3. P and T are physical; I and O are supporting knowledge/action domains.
4. Stage 1 is structural and non-causal.
5. A candidate interface is not a qualified dependency.
6. Co-location/common exposure is not causal P↔T dependency.
7. \(P\rightarrow T\not\Rightarrow T\rightarrow P\).
8. Mechanism qualification does not imply parameter identifiability or dynamic readiness.
9. Stage 3 studies complex spatiotemporal behavior; physics-based hybrid multiscale dynamics is its principal representation.
10. \(Y\neq y\neq\widehat Y\); physical possibility is not operational feasibility.
11. Operational control \(u(x,t)\) is distinct from persistent intervention \(a_k\).
12. Stage-5 uncertainty qualification is not universally probabilistic.
13. Viability/reachability augment rather than automatically replace conventional resilience measures.
14. Resilience effect, effectiveness, resource requirement, resource efficiency, and admitted sustainability consequence remain separate.
15. Accessibility/equity is conditional on separate qualification.
16. Stage 7 seeks defensible alternatives, not a universal scalar optimum.
17. Adaptive pathways are conditional Stage-7 extensions.
18. H1 primary comparison is \(M_2\) vs \(M_1\), with \(M_0\) reference.
19. RQ1/SO1 and RQ2/SO2 are prerequisites; H1–H5 map to RQ3–RQ7 respectively.
20. No hypothesis is supported by this figure; H1–H5 remain NOT TESTED unless their confirmatory prerequisites close.
21. Case-study and demonstrator branches are execution realizations, not theory authorities or the full validity domain.
22. No quantitative performance claim is implied by this map.

---

# 15. Visual-production metadata

| Field | Value |
|---|---|
| Figure ID | FIG-MINDMAP-THESIS-LOGIC-V2 |
| Figure role | full thesis scientific-logic map |
| Scientific authority | CANONICAL_7_STAGE_FRAMEWORK_V2.md + v2.1 alignment |
| RQ authority | CANONICAL_RESEARCH_QUESTIONS_V4.md |
| SO/H authority | CANONICAL_RQ_SO_HYPOTHESES_V4.md |
| Mathematical support | PHYSICS_MATHEMATICS_ENGINEERING_SYNTHESIS_V1.md |
| Visual QA | FRAMEWORK_VISUAL_FIDELITY_PROTOCOL_V2.md |
| Evidence state | [D] |
| Data status | conceptual; execution branch is dated status metadata |
| Typography | Times New Roman where Mermaid renderer supports it |
| P semantic color | navy |
| T semantic color | teal |
| I semantic color | blue |
| O semantic color | amber |
| Hazard semantic color | red |
| Derived/handoff semantic color | purple |
| Limitation | organizational synthesis; does not validate mechanisms, models, parameters, hypotheses, or cases |
| Current status | DRAFT-UNVERIFIED pending render QA |

---

# 16. Required QA before CANONICAL-VERIFIED

~~~text
Authority synchronization:          PASS
Stage count/order:                  PASS
Stage names/semantics:              PASS
Architecture/behavior distinction: PASS
Stage-1 non-causal semantics:       PASS
Stage-2 causal firewall:            PASS
Identification/readiness handoff:  PASS
Stage-3 behavior/representation:    PASS
Stage-4 feasible-control chain:     PASS
Stage-5 uncertainty semantics:      PASS
Stage-6 consequence typing:         PASS
Stage-7 decision semantics:         PASS
RQ/SO/H v4 traceability:            PASS
Execution/case status:              PASS as of 2026-09-21
No silent eighth stage:             PASS
No silent scientific additions:    PASS
GitHub Mermaid render QA:           OPEN
~~~

Until render QA is completed:

~~~math
\boxed{\text{STATUS = DRAFT-UNVERIFIED}}
~~~

---

# 17. Supersession statement

This v2 file supersedes THESIS_FULL_LOGIC_MINDMAP_V1.md for **current scientific interpretation** once render QA passes. V1 remains repository provenance and should not be edited into a different historical state.

Key v2 corrections include:

- v4 RQ/SO/H authority;
- v2.1 stage semantics;
- Stage-1 structural/non-causal separation;
- Stage-2 evidence-qualified directional-dependency language;
- explicit Stage-2→3 identification/readiness handoff;
- Stage-3 behavior-versus-representation distinction;
- Stage-5 uncertainty qualification replacing universal probability language;
- Stage-6 typed resilience/resource/sustainability consequences;
- Stage-7 defensible-decision semantics with conditional adaptive pathways;
- corrected H1–H5 traceability;
- case realizations demoted below theory, with Austin/Houston/NYC-ACN status represented explicitly.
