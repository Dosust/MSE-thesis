# Global Scenario Field Dictionary v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.6 FIELD DICTIONARY  
**Parent:** GLOBAL_SCENARIO_ID_AND_PROPAGATION_SCHEMA_V1.md

## 1. Root scenario fields

| Field | Type | Scientific meaning | Mutable after freeze? | Owner | Notes |
|---|---|---|---|---|---|
| ScenarioRootID | immutable ID | identity of common physical/exogenous realization | NO | GLOBAL/S3 | new scientific input => new ID/version |
| CaseID | reference | P1.5 qualified case | NO | P1.5 | scenario must belong to one case version |
| FamilyID | grouping ID | structural scenario family | NO except versioned regrouping | GLOBAL | grouping does not imply probability |
| ScenarioSetIDs | collection refs | analysis sets containing root | YES by new set version | GLOBAL | set membership changes do not change root inputs |
| Roles | controlled enum | development/validation/confirmatory/etc. | controlled amendment only | GLOBAL | independence audit required for reuse |
| Y0Ref | P1.5 field ref | common initial physical state | NO | S3 | changing Y0 creates new root |
| GraphRef | P1.5 field ref | initial P/T topology | NO | S1/S3 | changing topology creates new root |
| HazardRef | P1.5 field ref | hazard/environmental forcing realization | NO | S3 | realization, not generic hazard model |
| DemandOperatingRef | input ref | exogenous demand/operating realization | NO | S3 | root-held across matched arms unless hypothesis explicitly tests it |
| SharedParameterRef | draw/reference | parameter realization intended to be common | NO | S2/S3 | treatment-specific parameters belong in arm |
| InitialModeRef | mode ref | initial hybrid/discrete mode | NO | S3 | must align with Y0/G |
| HorizonRef | P1.5 field ref | common dynamic time support | NO | S3/S5 | lifecycle horizon separate |
| RandomnessManifestRef | manifest ref | named stochastic streams/substreams | NO | GLOBAL/S3 | seed is reproducibility metadata |
| ValidityDomainRef | P1.5 Omega ref | admissible domain | NO | GLOBAL | scenario root must lie inside Omega_case |
| ProbabilitySemantics | enum | NONE/weight/probability meaning | NO after analysis freeze | P1.7 | frequency != probability |
| Provenance | entity/activity/agent + hashes | root origin and identity | append-only | GLOBAL | exact version/hash required |
| ClaimCeiling | epistemic bound | max claim root can support | may decrease; increase needs evidence | GLOBAL | downstream cannot silently raise |
| Status | gate state | PASS/BLOCKED/FAIL/DEFERRED/N/A | controlled | GLOBAL | design freeze may leave DEFERRED |

## 2. Arm fields

| Field | Meaning | Examples |
|---|---|---|
| ArmID | immutable stage-arm identity | H1-M1, H1-M2, H2-N1, H4-a03 |
| Stage | stage owning treatment | S3...S7 |
| Hypothesis | H1...H5 or NONE | H4 |
| ComparisonGroupID | matched-comparison family | H1-CG-0001 |
| ArmRole | BASELINE/TREATMENT/ABLATION/etc. | TREATMENT |
| ModelRef | model/comparator configuration | M1/M2 |
| ActiveMechanismIDs | mechanisms active in arm | only Stage2→3-ready mechanisms for M2 |
| OperationalControlRef | operational policy/input | common u/pi or arm-specific if explicitly treatment |
| InformationOrganizationRef | S4 configuration | N0/N1/N2 |
| ResilienceRepresentationRef | S5 information arm | Q_conv or Q_VRR |
| InterventionRef | S6 strategic intervention | a_k |
| DecisionFrameRef | S7 decision information arm | X_R or X_R,S |
| ChangedFields | fields deliberately manipulated | coupling representation |
| HeldConstantFields | fields required identical | hazard, Y0, seeds |
| Overrides | explicit deviations from root/common frame | treatment-only parameter |
| Provenance | arm definition/version/hash | exact |
| ClaimCeiling | arm-specific epistemic bound | <= upstream |
| Status | PASS/BLOCKED/FAIL/DEFERRED/N/A | DEFERRED pre-data |

## 3. Run fields

| Field | Meaning |
|---|---|
| RunID | immutable executable run identity |
| ScenarioRootID | root realization used |
| ArmID | experimental arm used |
| ParentRunIDs | upstream runs/results consumed |
| InputBundleHash | hash of complete executable inputs |
| ModelHash | exact model/repository/config identity |
| SeedManifestHash | exact stochastic realization identity |
| ScenarioSchemaVersion | P1.6 schema version |
| ResultID | separate output identity |
| Status | execution/admissibility state |
| ClaimCeiling | run-level maximum claim |

## 4. Core distinction

~~~math
\boxed{
SID_r
\neq
AID_{r,a}^{(k)}
\neq
RID_{r,a}^{(k)}
\neq
ResultID_{r,a}^{(k)}.
}
~~~

One physical realization may support multiple matched arms and multiple downstream analyses without losing identity.

## 5. Root versus arm allocation rule

A quantity belongs in the ROOT if changing it would change the physical/exogenous realization common to the intended matched comparison.

A quantity belongs in the ARM if changing it is the declared treatment/comparator manipulation.

A quantity belongs in the RESULT only if it is produced after execution.

When ambiguous, the comparison protocol must resolve ownership before confirmatory execution.
