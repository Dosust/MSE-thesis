# Cross-Cutting Mind Map — VVUQ, Falsification, Evidence and Reproducibility

**Status:** Cross-cutting thesis control — **not Stage 8**

## GitHub-rendered mind map

~~~mermaid
flowchart LR
    V["CROSS-CUTTING CONTROL\nVVUQ + falsification + provenance"]
    E["Evidence\nsource identity\nclaim support\ncontrary evidence\nvalidity domain"]
    A["Assumptions\nexplicit\nconsequence\nsensitivity test"]
    P["Parameters\nunits\nprovenance\nuncertainty\nno silent filling"]
    VER["Verification\nmath consistency\ncode tests\nsolver checks\nconvergence"]
    VAL["Validation\nindependent observations\nheld-out data\nexternal benchmark\nvalidity limits"]
    UQ["Uncertainty quantification\naleatory\nepistemic\nmodel-form\nscenario"]
    F["Falsification\npredeclared failure condition\nnegative findings retained"]
    R["Reproducibility\nversioned data\nhashes\nconfigurations\nexperiment IDs"]
    S1["S1 Structure"]
    S2["S2 Causality"]
    S3["S3 Dynamics"]
    S4["S4 Estimation + control"]
    S5["S5 Resilience"]
    S6["S6 Intervention + sustainability"]
    S7["S7 Decision"]

    V --> E
    V --> A
    V --> P
    V --> VER
    V --> VAL
    V --> UQ
    V --> F
    V --> R

    V -. governs .-> S1
    V -. governs .-> S2
    V -. governs .-> S3
    V -. governs .-> S4
    V -. governs .-> S5
    V -. governs .-> S6
    V -. governs .-> S7

    classDef root fill:#161b22,color:#ffffff,stroke:#d4a72c,stroke-width:3px;
    classDef ctrl fill:#fff8c5,color:#161b22,stroke:#bf8700,stroke-width:1.5px;
    classDef stage fill:#ffffff,color:#161b22,stroke:#57606a,stroke-width:1.2px;
    class V root;
    class E,A,P,VER,VAL,UQ,F,R ctrl;
    class S1,S2,S3,S4,S5,S6,S7 stage;
~~~

## Cross-cutting scientific rule

~~~math
\boxed{\text{Stages }1\text{--}7\subset\text{VVUQ + falsification + provenance}}
~~~

Every proposed or adapted mathematical object must expose:

~~~math
\boxed{\text{assumptions}+\text{parameters}+\text{evidence}+\text{uncertainty}+\text{verification}+\text{validation domain}}
~~~

## Failure-state discipline

~~~text
PASS     evidence satisfies the declared gate
FAIL     declared gate is contradicted or unmet
BLOCKED  required evidence/execution is unavailable
OPEN     required work remains
NOT TESTED no confirmatory evaluation has occurred
~~~

## Model-comparison control

~~~math
\boxed{M_0=\text{independent},\quad M_1=\text{static coupling},\quad M_2=\text{dynamic causal coupling}}
~~~
~~~math
\boxed{M_2\overset{?}{>}M_1}
~~~

The question mark is essential: the thesis must test incremental value rather than encode superiority into the framework.