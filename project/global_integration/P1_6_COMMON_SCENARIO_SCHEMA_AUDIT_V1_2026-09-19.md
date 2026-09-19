# P1.6 Common Scenario Schema Audit v1 — 2026-09-19

**Status:** EXECUTED — PASS  
**Scope:** Global scenario identity, matched-comparison, randomness and Stage 3→7 propagation architecture  
**Empirical effect:** NONE

## 1. Result

~~~math
\boxed{
G_{P1.6}^{design}=PASS
}
~~~

~~~text
52 PASS
0 FAIL
~~~

## 2. Audited artifacts

1. GLOBAL_SCENARIO_ID_AND_PROPAGATION_SCHEMA_V1.md
2. GLOBAL_SCENARIO_ID_PROPAGATION_SCHEMA_V1.schema.json
3. GLOBAL_SCENARIO_FIELD_DICTIONARY_V1.md
4. GLOBAL_SCENARIO_PROPAGATION_MATRIX_V1.md
5. GLOBAL_SCENARIO_MATCHING_AND_RANDOMNESS_PROTOCOL_V1.md
6. GLOBAL_SCENARIO_ROOT_MANIFEST_TEMPLATE_V1.csv
7. GLOBAL_SCENARIO_SEED_MANIFEST_TEMPLATE_V1.csv

## 3. Machine-structure audit

PASS:
- JSON schema parses;
- package requires scenario root, stage runs and propagation edges;
- stage vocabulary is exactly S3–S7;
- H1–H5 arm links are available;
- roles distinguish calibration, validation, held-out and confirmatory use;
- probability semantics distinguish empirical frequency from probability;
- root requires shared parameter and randomness manifest references;
- every arm declares changed fields and held-constant fields;
- every run freezes input-bundle, model and seed-manifest hashes;
- result identity is separate from run identity;
- propagation edges support derivation and aggregation.

## 4. Scientific identity audit

PASS:

~~~math
SID_r
\neq
AID_{r,a}^{(k)}
\neq
RID_{r,a}^{(k)}
\neq
ResultID_{r,a}^{(k)}.
~~~

The architecture separates:
1. immutable physical/exogenous root;
2. experimental arm;
3. executable run;
4. result.

Treatment-specific changes are explicitly allocated to ARM records.

Any change to a root-defining scientific input creates a new root ID/version.

## 5. Cross-hypothesis matching audit

### H1
PASS:
- M1 vs M2 primary contrast preserved;
- M0 retained as uncoupled reference;
- matched hazard/Y0/graph/demand/shared-parameter/randomness rules frozen;
- M2 mechanisms constrained by:

~~~math
\mathbb I_{M_2}^{active}
\subseteq
\mathbb I_3^{ready}.
~~~

### H2
PASS:
- N0/N1/N2 architecture preserved;
- physical root remains matched;
- only declared information/organization conditions change.

### H3
PASS:
- Qconv versus QVRR information contrast preserved;
- physical trajectory/outcome/data split remain common.

### H4
PASS:
- root exogenous realization remains common;
- intervention is the treatment;
- accounting/requirement/source-version matching preserved;
- favorable hazard assignment by intervention arm is prohibited.

### H5
PASS:
- ScenarioSetID is frozen across decision arms;
- XR versus XR,S contrast preserved;
- candidate universe, feasibility, EFX/EFY, UQ and decision machinery remain common.

## 6. Randomness audit

PASS:
- randomness manifest uses named semantic streams;
- common random numbers require identical stochastic meaning;
- treatment-specific structural changes may use N/A/new streams instead of invalid matching;
- PRNG draw-order divergence risk is recognized;
- seed is reproducibility metadata, not distribution evidence;
- scenario count/frequency is not probability.

## 7. Propagation audit

PASS:

~~~math
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
~~~

Every downstream run retains parent run IDs.

Stage-7 aggregation cannot omit an admissible parent because its result is unfavorable.

No orphan confirmatory result is admissible.

## 8. Result firewall

PASS:

~~~math
\boxed{
\omega_{r,a}^{(k)}
\neq
R(\omega_{r,a}^{(k)}).
}
~~~

Scenario inclusion/exclusion and RNG configuration must be result-blind for confirmatory work.

Post-result scientific input changes require a versioned amendment and disclosure.

## 9. Machine-schema boundary

The audit explicitly recognizes:

~~~math
\boxed{
\text{JSON-schema validity}
\neq
\text{scientific scenario admissibility}.
}
~~~

JSON Schema checks structure/vocabulary. Cross-record equality, parent completeness, held-constant equivalence, mechanism-readiness subset relations and random-stream semantic equivalence require the P1.6 semantic validator/audit.

## 10. Protected DEFERRED fields

No value was invented for:
- ScenarioRootID;
- scenario family/count;
- hazard or demand realization;
- parameter draw;
- random seed/substream;
- probability/weight;
- hypothesis arm count;
- intervention;
- Stage-7 scenario set;
- H1–H5 result.

## 11. Closure

~~~math
\boxed{
P1.6=PASS.
}
~~~

Next:

~~~math
\boxed{
P1.7=\text{GLOBAL UNCERTAINTY / VVUQ CONTROL}.
}
~~~
