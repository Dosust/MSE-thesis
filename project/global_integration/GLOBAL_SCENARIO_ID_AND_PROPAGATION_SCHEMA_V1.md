# Global Scenario ID and Propagation Schema v1

**Date:** 2026-09-19  
**Status:** CANONICAL GLOBAL PRE-DATA SCENARIO CONTRACT  
**Scope:** Stage 3→7 scenario identity, matched-comparison propagation, randomness, provenance, and result separation  
**Empirical effect:** none.

## 1. Scientific purpose

P1.6 defines **what constitutes the same scenario across model, information, resilience, intervention, and decision comparisons**.

The key distinction is:

~~~math
\boxed{
\text{immutable physical/exogenous realization}
\neq
\text{experimental arm}
\neq
\text{simulation result}.
}
~~~

P1.6 therefore uses a two-layer architecture:

~~~math
\boxed{
\omega_r^{base}
\rightarrow
\alpha_{r,a}^{(k)}
\rightarrow
\omega_{r,a}^{(k)}
\rightarrow
R_{r,a}^{(k)}.
}
~~~

where:
- \(\omega_r^{base}\) is the immutable root realization;
- \(\alpha_{r,a}^{(k)}\) is the stage/hypothesis-specific experimental arm;
- \(\omega_{r,a}^{(k)}\) is the executable stage-run scenario;
- \(R_{r,a}^{(k)}\) is the result and is never part of the scenario input identity.

## 2. External design basis

This schema uses external standards only as design guidance.

- W3C PROV explicitly supports identifying objects, versioning, procedures, derivations and reproducibility in provenance records [1].
- NASA-STD-7009B requires modeling/simulation acceptance criteria and credibility products to be tied to intended use across the M&S life cycle [2].
- NASA-HDBK-7009B provides implementation guidance for production, use and consumption of M&S products [3].
- Modelica SSP 2.0 is an example of a modern standard for exchange of composite simulation architectures and parameterizations, including metadata and traceability-oriented extensions; P1.6 does not require SSP software [4].
- NIST digital-twin credibility work emphasizes V&V and UQ for trustworthy decision-support models [5].

## 3. Root scenario object

Define the immutable base realization:

~~~math
\boxed{
\omega_r^{base}
=
(
SID_r,
CID,
FID_r,
Role_r,
Y_{0,r},
\mathcal G_{0,r},
\eta_r,
D_r,
\Theta_r^{shared},
m_{0,r},
T_r,
\xi_r,
\Omega_r,
\Pi_r,
\Lambda_r
).
}
~~~

### 3.1 Root fields

| Field | Meaning |
|---|---|
| \(SID_r\) | immutable root scenario identifier |
| \(CID\) | P1.5 case identifier |
| \(FID_r\) | scenario-family identifier |
| \(Role_r\) | declared scientific role |
| \(Y_{0,r}\) | common initial physical state reference |
| \(\mathcal G_{0,r}\) | common starting graph/topology reference |
| \(\eta_r\) | hazard/environmental realization |
| \(D_r\) | exogenous demand/operating conditions |
| \(\Theta_r^{shared}\) | shared parameter realization/draw |
| \(m_{0,r}\) | initial discrete mode |
| \(T_r\) | common dynamic horizon/timing record |
| \(\xi_r\) | randomness/realization manifest reference |
| \(\Omega_r\) | P1.5 case-domain reference |
| \(\Pi_r\) | provenance/version/hash payload |
| \(\Lambda_r\) | root scenario claim ceiling |

The root contains only quantities that are intended to remain common across a matched comparison.

## 4. Experimental-arm object

For stage \(k\) and arm \(a\):

~~~math
\boxed{
\alpha_{r,a}^{(k)}
=
(
AID_{r,a}^{(k)},
Stage_k,
H_i,
CGroup,
ArmRole,
MRef,
\mathbb I^{active},
URef,
IORef,
RRef,
a_k,
DRef,
Overrides,
\Pi_{\alpha},
\Lambda_{\alpha}
).
}
~~~

Interpretation:

| Field | Meaning |
|---|---|
| \(AID\) | immutable arm ID |
| \(Stage_k\) | S3/S4/S5/S6/S7 |
| \(H_i\) | H1–H5 link, if applicable |
| \(CGroup\) | matched comparison-group ID |
| \(ArmRole\) | baseline/treatment/ablation/sensitivity/etc. |
| \(MRef\) | model/comparator realization reference |
| \(\mathbb I^{active}\) | active mechanisms for this arm |
| \(URef\) | operational-control/policy reference |
| \(IORef\) | information/organization configuration reference |
| \(RRef\) | resilience-information representation reference |
| \(a_k\) | strategic intervention reference |
| \(DRef\) | Stage-7 decision-information frame reference |
| \(Overrides\) | explicit treatment-controlled differences from the root/common frame |
| \(\Pi_{\alpha}\) | arm provenance/version/hash |
| \(\Lambda_{\alpha}\) | arm claim ceiling |

Fields irrelevant to a stage are explicitly N/A, not silently omitted in confirmatory manifests.

## 5. Executable run object

~~~math
\boxed{
\omega_{r,a}^{(k)}
=
(
RID_{r,a}^{(k)},
SID_r,
AID_{r,a}^{(k)},
ParentRID,
InputBundleHash,
ModelHash,
SeedManifestHash,
Status,
\Lambda_{run}
).
}
~~~

The run object points to the frozen root and arm; it does not duplicate mutable copies of them.

## 6. Result firewall

A result has an independent identifier:

~~~math
\boxed{
ResultID_{r,a}^{(k)}
\neq
RID_{r,a}^{(k)}
\neq
SID_r.
}
~~~

Permanent:

~~~math
\boxed{
\omega_{r,a}^{(k)}
\neq
R(\omega_{r,a}^{(k)}).
}
~~~

Target results cannot be used to retroactively alter the root/arm identity without a versioned amendment.

## 7. Root immutability

After scenario freeze, any change to the following creates a new root scenario ID/version:

~~~text
case_id
initial_state
initial_topology
hazard_realization
exogenous_demand_or_operating_conditions
shared_parameter_realization
initial_mode
dynamic_horizon
randomness_manifest
case_domain_reference
~~~

A corrected typo in descriptive metadata may be amended with provenance if it does not change scientific meaning or executable content.

## 8. Stage-arm changes do not overwrite root identity

Treatment-specific changes are allocated to ARM records. They create or modify an ARM, never silently the root realization.

Examples:
- H1 changes coupling representation/model arm;
- H2 changes information/organization condition;
- H3 changes resilience-information representation;
- H4 changes strategic intervention;
- H5 changes the information included in the decision evaluation.

Thus the shared scenario remains traceable while the treatment remains explicit.

## 9. Global roles

Allowed root/arm roles:

~~~text
VERIFICATION_FIXTURE
SUBSYSTEM_BENCHMARK
COUPLED_SYNTHETIC_BENCHMARK
DEVELOPMENT
CALIBRATION
VALIDATION
HELD_OUT
CONFIRMATORY
SENSITIVITY
BASELINE
TREATMENT
ABLATION
DIAGNOSTIC
~~~

Role reuse requires an explicit independence audit.

A confirmatory scenario cannot silently become calibration data.

## 10. Scenario set and family

A family is a structural grouping:

~~~math
\boxed{
\mathcal F_j=\{\omega_r^{base}:FID_r=j\}.
}
~~~

A scenario set is a declared analysis set:

~~~math
\boxed{
\mathcal W_q=\{SID_r:r\in\mathcal I_q\}.
}
~~~

Families and sets do not imply probabilities.

~~~math
\boxed{
\text{scenario count/frequency}
\neq
\text{probability}.
}
~~~

A probability or weight is admissible only when its stochastic/population interpretation, source and normalization are justified.

## 11. Randomness manifest

Define:

~~~math
\boxed{
\xi_r
=
(
SeedSetID,
Generator,
GeneratorVersion,
StreamMap,
DrawProtocol,
CRNGroup,
FreezeHash
).
}
~~~

Each stochastic source receives a named stream, e.g.:

~~~text
hazard_residual
demand_variation
component_failure
repair_duration
observation_noise
organizational_delay
intervention_performance
~~~

A seed is reproducibility metadata, not evidence for a physical probability distribution.

### 11.1 Common random numbers

When scientifically justified, matched arms share the same named stochastic streams:

~~~math
\boxed{
\xi_{r,a}^{shared}
=
\xi_{r,b}^{shared}.
}
~~~

Do not rely solely on a single raw PRNG sequence when treatment arms change model structure or draw count. Use named streams/substreams so semantically identical stochastic quantities remain matched.

## 12. H1 propagation rule

Primary contrast:

~~~math
M_1
\quad\text{vs}\quad
M_2,
~~~

with \(M_0\) as secondary uncoupled reference.

For a matched root \(SID_r\), hold fixed:
- \(Y_0\);
- \(\mathcal G_0\);
- \(\eta\);
- \(D\);
- shared \(\Theta\);
- \(m_0\);
- \(T\);
- shared random streams;
- native subsystem models/calibration budget/numerical accuracy target where prespecified.

Changed arm field:
- coupling/model representation and corresponding admitted active-mechanism semantics.

Permanent:

~~~math
\boxed{
\mathbb I_{r,M_2}^{active}
\subseteq
\mathbb I_3^{ready}.
}
~~~

M0/M1/M2 cannot receive different hazards or seeds merely because they are different model arms.

## 13. H2 propagation rule

For the same root \(SID_r\):

~~~math
\mathscr N_0=P+T,
\qquad
\mathscr N_1=P+T+I,
\qquad
\mathscr N_2=P+T+I+O.
~~~

Hold fixed:
- physical root realization;
- physical model/version;
- physical parameters;
- qualified causal mechanisms;
- physical disturbance;
- common stochastic physical streams.

Changed arm fields:
- information availability/latency/quality;
- organizational conditions/resources/authority according to preregistration.

An H2 arm must not alter the underlying hazard or physical initial state.

## 14. H3 propagation rule

For each root/outcome realization, preserve:
- physical trajectory/scenario identity;
- Stage-4 observation/control assumptions;
- \(K,G_{\rm rec},F_{\rm unsafe}\);
- future outcome label;
- data split;
- random realization.

Primary change:

~~~math
Q_{conv}
\quad\text{vs}\quad
Q_{VRR}=Q_{conv}\cup\mathfrak R_T.
~~~

The same outcome cannot be relabeled differently across H3 arms.

## 15. H4 propagation rule

Experimental unit remains:

~~~math
e=(a_k,\omega_r^{base},Y_0,\mathfrak M^0,u/\pi,FU_6,\mathcal B_{LC},H_{LC}).
~~~

Across intervention arms, hold the root exogenous realization fixed and change only the declared strategic intervention plus its deterministic consequences on model structure/parameters/resources.

Preserve:
- scenario root;
- hazard/demand realization;
- base model;
- common requirements;
- accounting conventions;
- source/factor versions;
- shared random streams where scientifically meaningful.

If an intervention structurally removes/adds a stochastic process, the named-stream manifest records N/A/new stream status rather than forcing an invalid one-to-one random draw.

## 16. H5 propagation rule

H5 compares:

~~~math
\boxed{
\mathcal X_R
\quad\text{vs}\quad
\mathcal X_{R,S}.
}
~~~

The scenario-set identity, candidate intervention universe, feasibility rules, uncertainty representation, common effectiveness/efficiency information, numerical tolerances and decision machinery remain fixed.

Changed information block:

~~~math
\boxed{
\mathbf J_{\rm sus}
}
~~~

in the resilience+sustainability arm.

The H5 arm identity therefore references a frozen ScenarioSetID rather than changing physical scenario roots.

## 17. Stage propagation chain

A scenario root is traceable through:

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
RID_{r,a_k}^{S6}
\rightarrow
RID_{q}^{S7}.
}
~~~

Stage 7 may aggregate a set of Stage-6 scenario/intervention records; its run record therefore carries the full ScenarioSetID and parent-run list.

## 18. Parent/derivation provenance

W3C PROV-style provenance is represented by:
- entity: scenario root, arm, run manifest, result;
- activity: parameter draw, scenario materialization, simulation, estimation, resilience analysis, intervention analysis, decision analysis;
- agent: person/software/workflow responsible.

Every downstream run records its parent run(s).

No orphan confirmatory result is admissible.

## 19. Model/version identity

Every run must freeze:
- repository commit or model package version;
- model configuration hash;
- parameter-realization hash;
- input-bundle hash;
- seed-manifest hash;
- scenario-schema version.

SSP 2.0 is an external example showing the engineering value of exchanging system architecture and parameterization together [4]; this thesis uses repository-native manifests unless SSP is later adopted.

## 20. Amendment rule

Any post-freeze scientific input change requires:
1. new root or arm version/ID as appropriate;
2. reason;
3. changed fields;
4. whether target results were previously inspected;
5. effect on confirmatory status;
6. affected downstream runs/results.

If target results were inspected before an outcome-relevant change, the affected analysis is exploratory unless an independent confirmatory set remains protected.

## 21. Global scenario admissibility gate

~~~math
\boxed{
\begin{aligned}
G_{P1.6}(r,a,k)={}&
G_{case}
\land G_{rootID}
\land G_{role}
\land G_{root}
\land G_{arm}\\
&\land G_{match}
\land G_{random}
\land G_{modelver}
\land G_{prov}
\land G_{indep}\\
&\land G_{prob}
\land G_{resultFW}
\land G_{claim}.
\end{aligned}
}
~~~

At design level, P1.6 may PASS while final root IDs, seeds and scenario counts remain DEFERRED.

## 22. Protected DEFERRED fields

P1.6 does not select or invent:
- final ScenarioRootIDs;
- scenario family membership/count;
- hazard realizations;
- demand realizations;
- parameter draws;
- seed values;
- probability weights;
- H1–H5 arm counts;
- interventions;
- final Stage-7 scenario set;
- results.

## 23. External references

[1] W3C, PROV Overview / PROV family. https://www.w3.org/TR/prov-overview/  
[2] NASA, NASA-STD-7009B Standard for Models and Simulations. https://standards.nasa.gov/node/263  
[3] NASA, NASA-HDBK-7009B implementation guide. https://standards.nasa.gov/node/198  
[4] Modelica Association, SSP 2.0 release and specification links. https://modelica.org/news/2025-01-08-ssp-20-released/  
[5] NIST, Credibility Consideration for Digital Twins in Manufacturing. https://www.nist.gov/publications/credibility-consideration-digital-twins-manufacturing

## 24. Repository authorities

- STAGE3_SCENARIO_SCHEMA_V2.md @ faba67b66c4468d751dbaf4fbd4cf97fb2b907a8
- GLOBAL_FINAL_CASE_SCHEMA_V1.md @ 83c66ee25169bb22f6806642a0753fa589d3f42e
- GLOBAL_H1_H5_MASTER_PREREGISTRATION_V1.md @ 9b80cb8a2bbb882b53ed5dd3f86d007596e0e9f6
- GLOBAL_STAGE_HANDOFF_MATRIX_V1.md @ 711128daad5f150016cf994e1c6da497c3c84bb7
- STAGE4_H2_EXPERIMENT_PROTOCOL_V1.md @ 8f0595487fbd3b1bfc580bebc33890d67a582684
- STAGE5_H3_EXPERIMENT_PROTOCOL_V1.md @ f00f64c2b1ea01e373d0c428b597427e9f65b4b8
- STAGE6_H4_EXPERIMENT_PROTOCOL_V2.md @ 4a4f44ac4367014ea7aa63b5c548d6c22799bb57
- STAGE7_H5_PREREGISTRATION_AND_COMPARATOR_PROTOCOL_V2.md @ 93996781499c866ef02f455e8fcf9ed429c98fc9

## 25. Freeze interpretation

~~~math
\boxed{
G_{P1.6}^{design}=PASS
}
~~~

means only that scenario identity, matching, propagation and provenance rules are complete.

It does not mean any scenario has been selected or any H1–H5 result has been generated.


## 26. Machine-validation boundary

The JSON Schema validates structure, controlled vocabularies, required identifiers and field presence.

It does **not by itself** prove relational constraints such as:
- every RunID points to the single declared ScenarioRootID;
- held-constant hashes are equal across matched arms;
- a Stage-7 parent list is complete;
- a random stream has the same semantic meaning across arms;
- the M2 mechanism set is a subset of the current Stage2→3-ready set.

Those are cross-record scientific constraints and are verified by the P1.6 semantic/match audit.

~~~math
\boxed{
\text{JSON-schema validity}
\neq
\text{scientific scenario admissibility}.
}
~~~
