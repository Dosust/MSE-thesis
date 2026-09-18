# Stage 2 G2 Gate Specification v1

**Status:** **SUBORDINATE GATE IMPLEMENTATION — GOVERNED BY FROZEN STAGE-2 CONTRACT**  
**Normative authority:** `STAGE2_CASE_INDEPENDENT_CAUSAL_GOVERNANCE_CONTRACT_V1.md`

## 1. Purpose

`G2` determines whether a frozen Stage-1 structural candidate may be promoted to a **causally qualified interdependency**. It is not a literature-screening score and not a coupling-strength metric.

## 2. Component gates

| Gate | Question | PASS | FAIL | BLOCKED |
|---|---|---|---|---|
| `G2-M` Mechanism | Is there a physically, operationally, informational or institutionally interpretable mechanism linking source to receiver? | Mechanism is explicit, evidence-supported, and non-circular. | Proposed mechanism is contradicted or physically/operationally impossible. | Mechanism is plausible but decisive evidence is unavailable. |
| `G2-C` Case connection | Are the actual source/interface/receiver connected in the declared case? | Case mapping/crosswalk/asset or operational evidence verifies the connection. | Case evidence shows no relevant connection. | Required case data are unavailable/inaccessible. |
| `G2-X` Exchange/interface | Is what crosses/enables the relation explicitly defined? | Interface and realized service/resource/information/action are measurable or logically defined. | No defensible transmitted/enabled quantity exists. | Interface exists but exchange semantics cannot yet be verified. |
| `G2-A` Activation | Are the conditions under which the mechanism operates explicit and supported? | Trigger/state/mode/event is defined and evidence-consistent. | Claimed mechanism operates under conditions contradicted by evidence. | Activation conditions remain unobserved/unknown. |
| `G2-E` Evidence | Does the evidence portfolio support the causal claim after considering alternatives and contrary evidence? | Multiple relevant evidence components support the claim; contradictions are resolved or bounded. | Strong contrary evidence or alternative explanation invalidates the causal claim. | Evidence is insufficient or unavailable without decisive contradiction. |
| `G2-V` Validity | Is the domain of applicability declared? | Spatial, temporal, asset, operating/hazard and technological limits are explicit enough for use. | Claim is demonstrably invalid in the proposed domain. | Limits cannot yet be established. |
| `G2-F` Falsification | Is there a concrete observation/test that could reject or force revision of the claim? | Falsifier/revision condition is explicit and observable/testable. | Claim is formulated so it cannot be falsified. | Required test/observation is not yet available. |

## 3. Aggregate logic

Final causal status uses only:

~~~text
PASS
FAIL
BLOCKED
~~~

`OPEN` is a workflow state before the final G2 decision.

~~~math
\boxed{
G_2^{\rm causal}(e)=\bigwedge_{g\in\{M,C,X,A,E,V,F\}}G_{2-g}(e)
}
~~~

Operational decision rule:

~~~text
if any decisive component = FAIL      -> G2 = FAIL
else if any required component = BLOCKED -> G2 = BLOCKED
else if all seven components = PASS   -> G2 = PASS
else                                  -> workflow state = OPEN
~~~

## 4. Parameter-readiness gate is separate

Parameter identification is not required to establish that a mechanism exists, but Stage 3 cannot invent missing coupling dynamics.

~~~math
\boxed{G_{2\to3}(e)=G_2^{\rm causal}(e)\land G_{2-P}(e)}
~~~

`G2-P` passes when the mechanism has a sufficiently explicit logical/functional/quantitative response representation and parameter status for the intended Stage-3 implementation. This may be `BOUNDED`, `CALIBRATED`, or `VALIDATED` depending on the model form; `UNESTIMATED` is not automatically a causal failure but may block Stage-3 numerical execution.

## 5. Prohibited shortcuts

None of the following can independently produce `G2=PASS`:

~~~math
\boxed{
\text{proximity},\ 
\text{topological adjacency},\ 
\text{correlation},\ 
\text{common exposure},\ 
\text{literature mechanism family},\ 
\text{standard compliance},\ 
\text{expert assertion}
}
~~~

Each may contribute evidence to a specific component gate, but causal promotion requires the full declared logic.

## 6. Audit record required for every candidate

Every final G2 decision must record: candidate ID, exact causal claim, seven component decisions, evidence IDs, unresolved alternatives, parameter status, validity domain, falsifier, reviewer/date/version, and downstream Stage-3 readiness.