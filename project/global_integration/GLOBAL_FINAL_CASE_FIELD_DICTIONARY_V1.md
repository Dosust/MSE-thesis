# Global Final-Case Field Dictionary v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.5 FIELD DICTIONARY  
**Parent:** GLOBAL_FINAL_CASE_SCHEMA_V1.md

## 1. Purpose

This dictionary fixes the scientific type, source obligation, unit rule, uncertainty obligation, P1.4 reference class, admissibility gate, pre-data status, owner and downstream consumers for every member of:

~~~math
\mathcal S_{\rm case}
=
(
\mathcal G,Y_0,\theta,\eta,T,K,G_{\rm rec},F_{\rm unsafe},
\mathcal U_{\rm feas},\mathcal A,\Omega
).
~~~

## 2. Core field dictionary

| Field ID | Symbol | Scientific type/class | Shape | Source requirement | Unit rule | UQ obligation | Allowed P1.4 classes | Owner | Consumers | Pre-data status |
|---|---|---|---|---|---|---|---|---|---|---|
| CASE-G | \(\mathcal G\) | coupled topology / PHYSICAL+ONTOLOGY | multilayer graph + geometry | authoritative/qualified network data + crosswalk provenance | geometry CRS + asset/edge native units where applicable | topology/geometry/data-quality uncertainty | VALIDATION_EVIDENCE; VALIDATION_REFERENCE; EVIDENCE_SOURCE_REFERENCE; QUALIFIED_CASE | S1,S2 | S2–S7 | DEFERRED |
| CASE-Y0 | \(Y_0\) | initial physical truth/state / PHYSICAL | heterogeneous state vector | synchronized direct/derived observations or justified initialization | per-state native→canonical units | measurement/reconstruction/initial-condition uncertainty | VALIDATION_EVIDENCE; VALIDATION_REFERENCE; QUALIFIED_CASE; AUXILIARY_COUNTERFACTUAL_MODEL where explicitly reconstructed | S3 | S3–S7 | DEFERRED |
| CASE-THETA | \(\theta\) | model/mechanism parameter collection / MIXED | parameter table/vector | measured/calibrated/inferred/manufacturer/literature/authoritative, each labeled | parameter-specific dimensions; no silent conversion | parameter + dependence + identifiability/model-form where relevant | EVIDENCE_SOURCE_REFERENCE; VALIDATION_EVIDENCE; VALIDATION_REFERENCE; EXTERNAL_PRACTICE_FACTOR_REFERENCE | S2,S3 + local owners | consuming stages | DEFERRED |
| CASE-ETA | \(\eta\) | hazard/environmental forcing / PHYSICAL EXOGENOUS | field/time series/raster/event | observed/reanalysis/authoritative/synthetic source explicitly typed | physical hazard quantity + canonical unit | hazard intensity/space/time/model uncertainty | VALIDATION_EVIDENCE; VALIDATION_REFERENCE; EVIDENCE_SOURCE_REFERENCE; SYNTHETIC_TRUTH for synthetic benchmarks only | S3 | S3–S7 | DEFERRED |
| CASE-T | \(T\) | dynamic/resilience horizon / VALIDITY/TIME | interval | engineering/experiment definition with provenance | seconds/minutes/hours/days as appropriate with explicit conversion | horizon/requirement uncertainty if not fixed | REQUIREMENT_THRESHOLD; EVIDENCE_SOURCE_REFERENCE; NONE | S3,S5 | S3–S7 | DEFERRED |
| CASE-K | \(K\) | acceptable/viable state set / REQUIREMENT | inequality/set object | requirement IDs + state mapping + authority class | every threshold dimensionally typed | requirement + mapping uncertainty | REQUIREMENT_THRESHOLD; EVIDENCE_SOURCE_REFERENCE; VALIDATION_EVIDENCE where threshold derives from data | S5 | S5–S7 | DEFERRED |
| CASE-GREC | \(G_{\rm rec}\) | recovery target set / REQUIREMENT | set + deadline | requirement/target authority + state/service mapping | target quantities and deadline units explicit | target/deadline uncertainty | REQUIREMENT_THRESHOLD; EVIDENCE_SOURCE_REFERENCE | S5 | S5–S7 | DEFERRED |
| CASE-FUNSAFE | \(F_{\rm unsafe}\) | forbidden/unsafe state set / REQUIREMENT+SAFETY | set/inequality | safety/engineering/authority basis | every threshold dimensionally typed | requirement/threshold uncertainty | REQUIREMENT_THRESHOLD; EVIDENCE_SOURCE_REFERENCE | S5 | S5–S7 | DEFERRED |
| CASE-UFEAS | \(\mathcal U_{\rm feas}\) | feasible operational-control set / CONTROL | intersection of action constraints | physical + information + organization + resource evidence | action-specific units/bounds | availability/resource/info/org uncertainty | VALIDATION_EVIDENCE; EVIDENCE_SOURCE_REFERENCE; REQUIREMENT_THRESHOLD | S4 | S5,S6,S7-context | DEFERRED |
| CASE-A | \(\mathcal A\) | strategic intervention set / INTERVENTION | finite/structured set | engineering intervention definitions + executable transformation + resource/accounting provenance | native intervention/resource units | implementation/resource/performance/model uncertainty | EVIDENCE_SOURCE_REFERENCE; EXTERNAL_PRACTICE_FACTOR_REFERENCE; VALIDATION_EVIDENCE; QUALIFIED_CASE | S6 | S6,S7 | DEFERRED |
| CASE-OMEGA | \(\Omega\) | case validity/domain object / VALIDITY_DOMAIN | Cartesian/product domain + exclusions | synthesis of spatial/temporal/hazard/operating/model/UQ bounds from qualified fields | heterogeneous; each axis typed | uncertainty-domain semantics explicit | EVIDENCE_SOURCE_REFERENCE; REQUIREMENT_THRESHOLD; NONE | GLOBAL | S1–S7 | DEFERRED |

## 3. Required subfields

### CASE-G
Minimum:
- power graph ID/version;
- transport graph ID/version;
- spatial CRS/datum;
- extent;
- topology QA;
- entity and edge typing;
- interface/crosswalk IDs;
- dependency links to Stage-2 records;
- provenance hashes.

### CASE-Y0
Minimum:
- \(t_0\);
- timezone/temporal reference;
- state ordering;
- units;
- mode \(m_0\);
- measured/estimated/assumed flag by component;
- active dependency context;
- UQ record.

### CASE-THETA
For each \(\theta_i\):
- parameter ID;
- owner model/mechanism;
- physical meaning;
- source class;
- value/range/distribution if bound;
- unit;
- calibration/inference method;
- dependence/correlation;
- validity;
- status.

### CASE-ETA
Minimum:
- hazard type;
- variable/quantity;
- unit;
- spatial support/CRS;
- temporal support;
- source/version;
- observed/reanalysis/synthetic status;
- UQ;
- any CF convention/version if applicable.

### CASE-T
Minimum:
- dynamic start/end;
- time unit;
- purpose;
- justification;
- distinction from lifecycle/accounting horizon.

### CASE-K / CASE-GREC / CASE-FUNSAFE
Every constraint/target:
- requirement ID;
- exact expression;
- variable;
- unit;
- threshold;
- authority class;
- jurisdiction/scope if applicable;
- effective date if applicable;
- UQ;
- status.

### CASE-UFEAS
Must separately expose:
- \(\mathcal U_{phys}\);
- \(\mathcal U_{info}\);
- \(\mathcal U_{org}\);
- \(\mathcal U_{resource}\);
- intersection rule;
- availability/time dependence.

### CASE-A
For each \(a_k\):
- ID/class;
- target/location;
- model transformation/operator;
- intervention parameters;
- timing;
- resources;
- implementation constraints;
- service life;
- functional unit/accounting boundary;
- eligibility;
- provenance.

### CASE-OMEGA
Must separately expose:
- \(\Omega_x\);
- \(\Omega_t\);
- \(\Omega_{hazard}\);
- \(\Omega_{operating}\);
- \(\Omega_{model}\);
- \(\Omega_{uncertainty}\);
- exclusions/invalid regions.

## 4. Cross-field consistency rules

~~~math
\boxed{
Y_0\in StateSpace(\mathcal G),
\qquad
\eta\in\Omega_{hazard},
\qquad
T\subseteq\Omega_t.
}
~~~

~~~math
\boxed{
K,G_{\rm rec},F_{\rm unsafe}
\subseteq
StateSpace_R(\mathcal G,Y^{phys}).
}
~~~

~~~math
\boxed{
\mathcal U_{\rm feas}
\text{ must be compatible with the selected model and organizational/information realization.}
}
~~~

~~~math
\boxed{
a_k\in\mathcal A
\Rightarrow
\Phi_a(\mathfrak M^0,a_k)
\text{ executable or explicitly BLOCKED.}
}
~~~

~~~math
\boxed{
\Omega_{case}
\neq
\{\omega_s\}_{s=1}^N.
}
~~~

## 5. Claim firewall

A field may be present but not admissible. Presence is not PASS.

~~~math
\boxed{
\text{present}
\not\Rightarrow
\text{qualified}
\not\Rightarrow
\text{validated}.
}
~~~
