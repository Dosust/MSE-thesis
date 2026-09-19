# Stage 3 — Model-Family Selection Protocol v2

**Status:** CANONICAL STAGE-3 MODEL-SELECTION PROTOCOL  
**Effective date:** 2026-09-19  
**Purpose:** select the minimum scientifically sufficient model family without outcome-driven fidelity escalation.  
**Final case-specific model:** DEFERRED.

## 1. Governing principle

\`\`\`math
\boxed{
\text{maximum necessary fidelity}
\neq
\text{maximum possible detail}.
}
\`\`\`

The selected model must be sufficiently expressive for RQ3, ready mechanisms, QOIs and VVUQ obligations while avoiding complexity that cannot be identified or validated.

## 2. Outcome-blind rule

\`\`\`math
\boxed{
\mathfrak M_3^\star
=
\mathcal F_{select}
(
RQ_3,
\mathcal QOI_3,
\mathcal T_3,
\mathbb I_3^{ready},
D,
C_{comp},
C_{VVUQ}
).
}
\`\`\`

The final family must be selected before inspecting target H1 comparison outcomes used for confirmation.

Prohibited: choosing the family that maximizes an \(M_2\) advantage.

## 3. Candidate families

Candidate families are illustrative, not mandatory.

### 3.1 Power

| Family | Appropriate when | Main limitations |
|---|---|---|
| static AC power flow | equilibrium electrical state sufficient | no temporal electromechanical dynamics |
| linearized/DistFlow | radial approximation adequate | approximation/validity-domain error |
| QSTS/OpenDSS-type | time-varying distribution loading/EV/DER response is central | quasi-static electrical dynamics and update resolution |
| dynamic DAE | fast dynamics/protection/frequency/transients materially affect QOI | high parameter/validation burden |

### 3.2 Transportation

| Family | Appropriate when | Main limitations |
|---|---|---|
| static assignment | static comparator/equilibrium only | no dynamic queue/propagation |
| CTM/macroscopic | aggregate waves/queues sufficient | aggregated network/behavior |
| DTA/mesoscopic | route/time dynamics needed at moderate cost | behavioral/calibration assumptions |
| microscopic/SUMO-type | vehicles/signals/charging/access detail is mechanism-critical | computational/calibration burden |

### 3.3 Interface family

Admissible realizations include:

- algebraic map;
- queue/service process;
- hybrid capacity/mode switch;
- event-triggered restoration/access relation;
- co-simulation exchange;
- reduced-order dynamic memory.

The interface family must follow the Stage2→3-ready mechanism rather than invent one.

## 4. Hard admissibility gates

\`\`\`math
\boxed{
G_M
=
G_{RQ}
\land
G_{QOI}
\land
G_{mech}
\land
G_{time}
\land
G_{phys}
\land
G_{data}
\land
G_{num}
\land
G_{val}.
}
\`\`\`

- \(G_{RQ}\): addresses RQ3;
- \(G_{QOI}\): represents the required QOI families;
- \(G_{mech}\): executes ready mechanisms without semantic distortion;
- \(G_{time}\): supports required event/delay/timescale semantics;
- \(G_{phys}\): respects applicable physical laws/constraints;
- \(G_{data}\): required inputs/parameters are evidence-supportable;
- \(G_{num}\): tractable and solution-verifiable;
- \(G_{val}\): intended validation evidence/reference is attainable.

Failure of any mandatory gate makes the family inadmissible for that intended use.

## 5. Selection among admissible families

When several families pass, select by minimum sufficient complexity using auditable comparison of:

- state dimension;
- parameter/identifiability burden;
- temporal/spatial resolution;
- computational cost;
- VVUQ burden;
- validation evidence;
- coupling fidelity required.

Do not collapse these into arbitrary weights. If alternatives are equivalent for intended use, prefer the simpler/reproducible family and document the tie.

## 6. H1 nested-comparator compatibility

Where possible, M0/M1/M2 should share:

- native P model;
- native T model;
- initial condition;
- hazard and demand;
- numerical accuracy targets;
- calibration evidence/budget.

Only coupling representation should change for the primary contrast.

Any unavoidable non-nested difference must be declared as a potential confound.

## 7. Complexity-confound firewall

\`\`\`math
\boxed{
\text{benefit of dynamic mechanism}
\neq
\text{benefit of extra free parameters/resolution}.
}
\`\`\`

Controls include as applicable:

- matched calibration data/budget;
- held-out evaluation;
- parameter-count disclosure;
- mechanism ablation;
- nested-limit tests;
- model-family sensitivity.

## 8. Permitted pre-result data use

Selection may use pre-result facts about:

- availability;
- provenance;
- spatial/temporal resolution;
- computational size;
- validation data.

It may not use target \(M_0/M_1/M_2\) performance to choose the confirmatory model family.

## 9. Selection record

Every case must produce:

\`\`\`text
candidate_id
domain
family
RQ gate
QOI gate
mechanism gate
time gate
physics gate
data gate
numerical gate
validation gate
complexity/identifiability note
decision = SELECTED / REJECTED / RESERVED
reason
version/date
\`\`\`

## 10. Current candidate status

Existing OpenDSS/QSTS and GreenEVT/SUMO machinery remains a strong candidate for the realistic-synthetic H1 case.

\`\`\`text
CURRENT STATUS = CANDIDATE / NOT FROZEN BY THIS FILE
\`\`\`

## 11. Model-form uncertainty

If multiple materially plausible structures survive,

\`\`\`math
\boxed{
U_M\neq U_\theta.
}
\`\`\`

Their differences must be assessed through model-form sensitivity/ensemble/alternative-structure analysis, not hidden in parameter uncertainty.

## 12. Re-selection/change control

After selection is frozen, a change requires:

1. versioned amendment;
2. scientific reason independent of target H1 outcome where possible;
3. disclosure of results already inspected;
4. sensitivity analysis when feasible.

## 13. Claim boundary

Selection means appropriate/admissible for intended use. It does not mean empirically true, validated, or superior.
