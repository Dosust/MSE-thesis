# Master Branch Architecture — Full Thesis Logic

**Scientific identity:** Coupled Power–Transportation infrastructure as an **interdependent System of Systems** with **complex dynamical behavior**. Information and Organization are supporting domains.

## GitHub-rendered master map

~~~mermaid
flowchart LR
    K["INPUT: Critical service requirements K(t)"]
    S1["STAGE 1: Structure\nRQ1 / SO1\nPASS - FROZEN"]
    S2["STAGE 2: Causal interdependencies\nRQ2 / SO2\nNEXT - AUTHORIZED"]
    S3["STAGE 3: Hybrid multiscale dynamics\nRQ3 / SO3 -> H1"]
    S4["STAGE 4: Observation + estimation + organization + control\nRQ4 / SO4 -> H2"]
    S5["STAGE 5: Viability + reachability + confidence\nRQ5 / SO5 -> H3"]
    S6["STAGE 6: Diagnosis + intervention + sustainability consequences\nRQ6 / SO6 -> H4"]
    S7["STAGE 7: Engineering decision + transformation\nRQ7 / SO7 -> H5"]
    V["CROSS-CUTTING: VVUQ + falsification + provenance"]

    K --> S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7
    V -. applies to .-> S1
    V -. applies to .-> S2
    V -. applies to .-> S3
    V -. applies to .-> S4
    V -. applies to .-> S5
    V -. applies to .-> S6
    V -. applies to .-> S7

    classDef root fill:#161b22,color:#ffffff,stroke:#d4a72c,stroke-width:3px;
    classDef stage fill:#ffffff,color:#161b22,stroke:#57606a,stroke-width:1.5px;
    classDef frozen fill:#dafbe1,color:#1a1f24,stroke:#1a7f37,stroke-width:2px;
    classDef cross fill:#fff8c5,color:#1a1f24,stroke:#bf8700,stroke-width:2px;
    class K root;
    class S1 frozen;
    class S2,S3,S4,S5,S6,S7 stage;
    class V cross;
~~~

## Scientific branch hierarchy

~~~text
Coupled Power-Transportation Infrastructure Resilience
|
|-- INPUT: Critical service requirements K(t)
|
|-- 1. STRUCTURE
|   |-- P + T physical systems
|   |-- I + O supporting domains
|   |-- entities, geometry, intralayer topology
|   `-- structurally admissible relation candidates
|
|-- 2. CAUSALITY
|   |-- source -> receiver
|   |-- exchanged service/resource
|   |-- mechanism + activation condition
|   `-- parameter + uncertainty + validity + falsification
|
|-- 3. DYNAMICS
|   |-- subsystem physics
|   |-- hybrid events and modes
|   |-- multiscale temporal/spatial propagation
|   `-- M0 / M1 / M2 comparator architecture
|
|-- 4. KNOWLEDGE + ACTION
|   |-- measurement
|   |-- state estimation / belief
|   |-- information + organization
|   `-- feasible control set + policy
|
|-- 5. RESILIENCE
|   |-- remain: viability
|   |-- return: reachability
|   `-- confidence: probability under uncertainty
|
|-- 6. INTERVENTION + CONSEQUENCES
|   |-- resilience diagnosis
|   |-- candidate engineering intervention
|   |-- rerun coupled trajectory
|   `-- resilience + accessibility + energy + carbon + cost
|
`-- 7. DECISION + TRANSFORMATION
    |-- feasibility
    |-- resilience-sustainability trade-space
    |-- nondominated / regret-aware choice
    `-- optional adaptive sequence when justified
~~~

## Canonical mathematical chain

~~~math
\boxed{
K(t)
\rightarrow
(\mathcal S,\mathcal G,R)
\rightarrow
\mathbb I(x,t,Y,m)
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Y(x,t)
\rightarrow
(y,\widehat Y,z_I,z_O,\mathcal U,u)
\rightarrow
\mathfrak R_T
\rightarrow
(a_k,\Delta\mathfrak R,\Delta\mathbf J_{\rm sus})
\rightarrow
\mathcal A_{R,S}^{\star}
}
~~~

## Controlled stage handoffs

| From | To | Handoff logic |
|---|---|---|
| Input | Stage 1 | Service requirements define what the architecture must support |
| Stage 1 | Stage 2 | `r_e^(1)` structural candidate -> causal qualification |
| Stage 2 | Stage 3 | Accepted mechanism set `I(x,t,Y,m)` -> coupled dynamics |
| Stage 3 | Stage 4 | True trajectories / service states -> observation and action architecture |
| Stage 4 | Stage 5 | Estimated state + feasible policies -> maintainability/recovery analysis |
| Stage 5 | Stage 6 | Resilience object -> diagnosis -> candidate interventions |
| Stage 6 | Stage 7 | Intervention consequence vectors -> decision under uncertainty |

## Status boundary

Stage 1 is frozen at the generic-framework level. Stage 2 is the next scientific construction. The later branches are canonical design targets and must not be interpreted as completed empirical results.