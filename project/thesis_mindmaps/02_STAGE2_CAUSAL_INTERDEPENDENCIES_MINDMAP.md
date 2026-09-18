# Stage 2 Mind Map — Evidence-Grounded Causal Interdependencies

**Status:** **AUTHORIZED NEXT STAGE — NOT YET FROZEN**  
**Canonical question:** RQ2 — Why and through which mechanisms do components and layers affect each other?  
**Canonical objective:** SO2 — Establish evidence-supported directional causal mechanisms, activation conditions, parameters, uncertainties and validity boundaries linking components and layers.  
**Hypothesis mapping:** Developmental qualification supporting H1

## GitHub-rendered mind map

~~~mermaid
flowchart LR
    S2["STAGE 2\nEvidence-Grounded Causal Interdependencies"]
    Q["A. Scientific responsibility\nRQ2 — Why and through which mechanisms do components and layers affect each other?\nSO2 — Establish evidence-supported directional causal mechanisms, activation conditions, parameters, uncertainties and validity boundaries linking components and layers."]
    I["B. Inputs\nFrozen Stage-1 relation r_e^(1)\nCandidate mechanism m_e^cand\nCandidate activation context c_e^cand\nEvidence/provenance E_e"]
    O["C. Mathematical / physical objects\nSource + receiver\nTransferred quantity/service\nMechanism Phi_e\nActivation gamma_e\nParameters theta_e\nInternal state zeta_e\nValidity V_e + uncertainty U_e"]
    M["D. Mechanism / method\nMechanism qualification\nDirectional causal screening\nActivation-condition definition\nParameter provenance\nFalsification rule\nValidity-domain declaration"]
    E["E. Evidence + provenance\nDirect P-T evidence preferred\nPeer-reviewed mechanism evidence\nOperator / technical documentation\nContrary + negative evidence retained\nCommon exposure screened separately"]
    U["F. Assumptions + uncertainty\nAleatory vs epistemic distinguished\nUnidentified parameter stays OPEN\nTransferability limits explicit\nMediated paths remain explicit"]
    V["G. VVUQ + falsification\nMechanism plausibility check\nParameter dimensional consistency\nEvidence triangulation\nFalsification condition\nPASS / FAIL / BLOCKED per relation"]
    G["H. Gate\nG2 relation-level qualification\nPASS -> admitted causal relation\nFAIL -> excluded causal claim\nBLOCKED -> unresolved evidence"]
    OUT["I. Output\nQualified causal object I_e\nAccepted set I\nRejected + unresolved candidates preserved"]
    H["J. Handoff\nI(x,t,Y,m) -> Stage 3\nOnly qualified parameters/delays may enter dynamics"]
    N["NON-CLAIMS\nCorrelation != causality\nCommon hazard != P<->T dependency\nStandard interface != case mechanism\nNo dynamic performance result yet"]

    S2 --> Q
    S2 --> I
    S2 --> O
    S2 --> M
    S2 --> E
    S2 --> U
    S2 --> V
    S2 --> G
    S2 --> OUT
    OUT --> H
    S2 -. protected boundary .-> N

    classDef root fill:#161b22,color:#ffffff,stroke:#d4a72c,stroke-width:3px;
    classDef branch fill:#ffffff,color:#161b22,stroke:#57606a,stroke-width:1.5px;
    classDef gate fill:#fff8c5,color:#161b22,stroke:#bf8700,stroke-width:2px;
    classDef out fill:#dafbe1,color:#161b22,stroke:#1a7f37,stroke-width:2px;
    classDef non fill:#ffebe9,color:#161b22,stroke:#cf222e,stroke-width:1.5px;
    class S2 root;
    class Q,I,O,M,E,U,V branch;
    class G gate;
    class OUT,H out;
    class N non;
~~~

## Canonical mathematical objects

~~~math
\boxed{\mathfrak r_e^{(1)}\xrightarrow{\text{mechanism qualification}}\mathfrak I_e}
~~~

~~~math
\boxed{\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)}
~~~

~~~math
\mathcal C_e=(s_e,p_e^s,r_e,p_e^r,\chi_e),\qquad \Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e),\qquad \Pi_e=(\mathcal P_e,V_e,\mathcal U_e)
~~~

~~~math
\boxed{\text{common exposure or correlation}\neq\text{causal dependency}}
~~~

~~~math
\boxed{\mathbb I=\mathbb I(x,t,Y,m)}
~~~

## Scientific interpretation

Stage 2 is complete only when its inputs, objects, evidence, assumptions, VVUQ logic, and gate state are mutually consistent. The map is a traceability device; it is not independent scientific authority.

## Handoff discipline

The Stage-2 output may be consumed downstream only with its provenance, uncertainty, validity domain, and unresolved limitations attached.