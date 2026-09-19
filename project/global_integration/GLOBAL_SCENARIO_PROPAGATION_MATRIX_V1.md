# Global Scenario Propagation Matrix v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.6 STAGE 3→7 PROPAGATION CONTROL

## 1. Propagation backbone

~~~math
\boxed{
SID_r
\rightarrow
RID_r^{S3}
\rightarrow
RID_r^{S4}
\rightarrow
RID_r^{S5}
\rightarrow
RID_{r,a}^{S6}
\rightarrow
RID_q^{S7}.
}
~~~

A downstream run may aggregate multiple parent runs but must preserve all parent ScenarioRootIDs.

## 2. Stage propagation

| Stage | Root identity preserved | Arm-specific change | Parent evidence | Output identity rule |
|---|---|---|---|---|
| S3 / H1 | SID, Y0, G0, eta, D, shared theta, m0, T, shared streams | M0/M1/M2 coupling representation and allowed mechanisms | P1.5 + Stage2→3 readiness | each model arm gets unique RunID; common SID |
| S4 / H2 | same physical SID and qualified S3 model/trajectory reference | N0/N1/N2 information/organization conditions | selected S3 parent RunID | unique S4 RunID per arm; retains SID and parent |
| S5 / H3 | same SID, physical trajectory, S4 assumptions, requirements, outcome label/data split | Q_conv vs Q_VRR information representation | S3/S4 parent lineage | unique S5 analysis RunID; same SID |
| S6 / H4 | same SID exogenous realization, base model, requirements, accounting conventions | intervention a_k and its declared model transformation | qualified S5 diagnosis + upstream lineage | unique RunID per intervention × SID |
| S7 / H5 | same ScenarioSetID, candidate set, feasibility/UQ/common decision machinery | X_R vs X_R,S information block | all qualified S6 candidate/scenario records | S7 run references ScenarioSetID + complete parent list |

## 3. H1 matching

### Held
~~~text
ScenarioRootID
Y0Ref
GraphRef
HazardRef
DemandOperatingRef
SharedParameterRef
InitialModeRef
HorizonRef
shared Seed streams
native subsystem model identity where preregistered
calibration budget
numerical accuracy target
~~~

### Changed
~~~text
ModelRef / coupling representation
ActiveMechanismIDs as required by comparator semantics
~~~

Constraint:

~~~math
\mathbb I_{M_2}^{active}\subseteq\mathbb I_3^{ready}.
~~~

## 4. H2 matching

### Held
physical root + selected physical model/version + qualified mechanisms + physical parameters + physical stochastic realization.

### Changed
information availability, latency, quality, organization/authority/resource conditions according to N0/N1/N2.

## 5. H3 matching

### Held
ScenarioRootID, trajectory/outcome, data split, observation/control assumptions, \(K,G_{rec},F_{unsafe}\), random realization.

### Changed
information supplied to the predictive/decision task:

~~~math
Q_{conv}
\quad\text{vs}\quad
Q_{conv}\cup\mathfrak R_T.
~~~

## 6. H4 matching

### Held
ScenarioRootID, hazard/demand realization, base model, requirements, FU6, lifecycle accounting boundary/horizon, factor/data versions, shared stochastic streams where meaningful.

### Changed
strategic intervention \(a_k\) and its explicit physical/resource/accounting consequences.

No intervention may receive a favorable hazard realization that its comparator does not receive.

## 7. H5 matching

### Held
ScenarioSetID, candidate universe, feasibility rules, effectiveness, efficiency, UQ representation, normalization, numerical tolerances, common decision machinery, value model if legitimately common.

### Changed
availability/use of sustainability-consequence information:

~~~math
\mathcal X_R
\quad\text{vs}\quad
\mathcal X_{R,S}.
~~~

## 8. Aggregation rule

If Stage 7 consumes multiple scenarios:

~~~math
\boxed{
Parents(RID^{S7})
=
\{RID_{r,a}^{S6}\}_{r,a\in\mathcal I}.
}
~~~

No parent may be omitted because its result is unfavorable.

## 9. Propagation status

A downstream run is BLOCKED if:
- a mandatory parent RunID is missing;
- root identity is inconsistent;
- an arm changes a held-constant field without preregistered authorization;
- model/seed/input hashes are missing;
- probability semantics are inconsistent;
- a BLOCKED/FAIL upstream object is silently promoted.
