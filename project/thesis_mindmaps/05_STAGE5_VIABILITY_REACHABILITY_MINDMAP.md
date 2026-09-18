# Stage 5 Mind Map — Uncertainty-Aware Viability and Reachability Resilience

**Status:** Canonical downstream stage — **NOT YET CONFIRMATORILY EXECUTED**  
**Canonical question:** RQ5 — Under what conditions can critical coupled services remain acceptable or recover under feasible controls and uncertainty, and what additional engineering information do viability and reachability provide?  
**Canonical objective:** SO5 — Determine uncertainty-aware service viability and recovery reachability, evaluate incremental value beyond conventional performance/recovery curves, and characterize interface criticality as a supporting diagnostic.  
**Hypothesis mapping:** H3 — viability-reachability incremental-information hypothesis

## GitHub-rendered mind map

~~~mermaid
flowchart LR
    S5["STAGE 5\nUncertainty-Aware Viability and Reachability Resilience"]
    Q["A. Scientific responsibility\nRQ5 — Under what conditions can critical coupled services remain acceptable or recover under feasible controls and uncertainty, and what additional engineering information do viability and reachability provide?\nSO5 — Determine uncertainty-aware service viability and recovery reachability, evaluate incremental value beyond conventional performance/recovery curves, and characterize interface criticality as a supporting diagnostic."]
    I["B. Inputs\nService-acceptable set K(t)\nStage-3/4 dynamics + belief state\nFeasible policies Pi(z_I,z_O)\nDeclared uncertainty model"]
    O["C. Mathematical / physical objects\nViability set V_alpha,T\nReach-avoid set R_beta,T\nDistance rho_V\nTime to viability loss T_V\nRecovery time T_rec\nP_viable + P_recover"]
    M["D. Mechanism / method\nControlled viability analysis\nStochastic reach-avoid analysis\nBoundary-distance diagnostics\nProbability/confidence layer\nComparator R_curve"]
    E["E. Evidence + provenance\nService thresholds\nControl feasibility\nState/uncertainty evidence\nRecovery target G_rec\nUnacceptable region F\nIndependent labels for comparison"]
    U["F. Assumptions + uncertainty\nalpha / beta not assumed\nModel + parameter uncertainty\nPolicy uncertainty\nState-estimation uncertainty\nFinite-horizon choice"]
    V["G. VVUQ + falsification\nReference-solver verification\nGrid/discretization sensitivity\nProbability calibration\nSkill / incremental-information test\nConventional-curve benchmark"]
    G["H. Gate\nG5 resilience gate\nFreeze K, G_rec, F, horizons\nFreeze alpha, beta, policy class\nH3 requires incremental value, not novelty by definition"]
    OUT["I. Output\nResilience object R_T\nMaintainability + recovery probabilities\nBoundary/time diagnostics\nSupporting interface criticality"]
    H["J. Handoff\nR_T -> Stage 6 resilience diagnosis\nCriticality is diagnostic, not intervention decision"]
    N["NON-CLAIMS\nViability alone != resilience\nProbability is not separate resilience theory\nNo superiority over R_curve assumed\nNo intervention ranking yet"]

    S5 --> Q
    S5 --> I
    S5 --> O
    S5 --> M
    S5 --> E
    S5 --> U
    S5 --> V
    S5 --> G
    S5 --> OUT
    OUT --> H
    S5 -. protected boundary .-> N

    classDef root fill:#161b22,color:#ffffff,stroke:#d4a72c,stroke-width:3px;
    classDef branch fill:#ffffff,color:#161b22,stroke:#57606a,stroke-width:1.5px;
    classDef gate fill:#fff8c5,color:#161b22,stroke:#bf8700,stroke-width:2px;
    classDef out fill:#dafbe1,color:#161b22,stroke:#1a7f37,stroke-width:2px;
    classDef non fill:#ffebe9,color:#161b22,stroke:#cf222e,stroke-width:1.5px;
    class S5 root;
    class Q,I,O,M,E,U,V branch;
    class G gate;
    class OUT,H out;
    class N non;
~~~

## Canonical mathematical objects

~~~math
\boxed{\text{Resilience}=\text{remain} + \text{return} + \text{confidence}}
~~~

~~~math
\boxed{\mathcal V_{\alpha,T}(t)=\{y:\exists\pi\;\Pr^\pi[Y_\tau\in K(\tau),\ \forall\tau\in[t,t+T]\mid\mathcal I_t]\ge\alpha\}}
~~~

~~~math
\boxed{\mathcal R_{\beta,T}(t)=\{y:\exists\pi\;\Pr^\pi[\tau_{G_{\rm rec}}\le T,\ Y_s\notin F\ \forall s<\tau_{G_{\rm rec}}\mid\mathcal I_t]\ge\beta\}}
~~~

~~~math
\boxed{\mathfrak R_T=(\mathcal V_{\alpha,T},\mathcal R_{\beta,T},\rho_{\mathcal V},T_{\mathcal V},T_{\rm rec},P_{\rm viable},P_{\rm recover})}
~~~

~~~math
\boxed{R_{\rm curve}\quad\text{versus}\quad\mathfrak R_T}
~~~

## Scientific interpretation

Stage 5 is complete only when its inputs, objects, evidence, assumptions, VVUQ logic, and gate state are mutually consistent. The map is a traceability device; it is not independent scientific authority.

## Handoff discipline

The Stage-5 output may be consumed downstream only with its provenance, uncertainty, validity domain, and unresolved limitations attached.