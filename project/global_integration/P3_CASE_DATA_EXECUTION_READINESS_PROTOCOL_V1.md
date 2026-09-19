# P3 Case / Data Qualification and Execution Readiness Protocol v1

**Status:** CANONICAL P3 CONTROL PLANE — IN PROGRESS  
**Effective date:** 2026-09-20  
**Parent freeze:** GLOBAL_STAGE1_7_DESIGN_FREEZE_V1.md  
**Primary candidate case:** AUS-P5U-2018-V1  
**P2 design status:** PASS / FROZEN  
**P3 case-execution status at initialization:** BLOCKED  
**H1–H5:** NOT TESTED

## 1. Purpose

P3 converts the frozen P2 design into a qualified executable case without converting missing evidence into numerical assumptions.

~~~math
\boxed{
G_{P2}^{design}=PASS
\not\Rightarrow
G_{data}=PASS
\not\Rightarrow
G_{case,exec}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~

P3 is complete only when the specific execution object required by an experiment is qualified. A design-complete repository may legitimately contain BLOCKED and DEFERRED case fields.

## 2. Current candidate-case decision

The active case candidate remains:

~~~text
case_id: AUS-P5U-2018-V1
city: Austin, Texas
SMART-DS version: v1.0
SMART-DS year: 2018
candidate subregion: P5U
scenario: base_timeseries
candidate_is_frozen: false
final_case_admissibility: false
~~~

The case is a geographically grounded semisynthetic mechanism-validation experiment. SMART-DS is not Austin Energy feeder truth.

No H1–H5 outcome may be inspected to choose a feeder/subregion.

## 3. P3 scientific object

~~~math
\boxed{
\mathcal S_{case}
=
(
\mathcal G,
Y_0,
\theta,
\eta,
T,
K,
G_{rec},
F_{unsafe},
\mathcal U_{feas},
\mathcal A,
\Omega
).
}
~~~

Every object required by a planned experiment must satisfy its applicable P1.5 field gates before execution.

## 4. Current Austin G0–G8 normalization

| Gate | Contract state | P3 control state | Meaning |
|---|---|---|---|
| G0 canonical consistency | PASS | PASS | design contract consistent |
| G1 power materialization | OPEN | BLOCKED | no selected complete feeder realization/reference solve |
| G2 common spatial support | OPEN | DEFERRED | runtime spatial QA after selected feeder |
| G3 transport topology | source-qualified/materialization open | DEFERRED | TxDOT 2018 source qualified; runtime graph QA open |
| G4 traffic observations | semantics qualified/join open | DEFERRED | schema/join/road overlap/split incomplete |
| G5 P→T mapping | retrospective mapping open | BLOCKED | selected feeder + mapping rule/tolerance required |
| G6 T→P repair access | OPEN | BLOCKED | origin/target/routing/passability/travel model incomplete |
| G7 flood exposure | semantics qualified/intersection open | BLOCKED | selected power+road support intersection required |
| G8 QC/provenance | OPEN | DEFERRED | full case execution lineage incomplete |

These are P3 readiness interpretations. They do not rewrite config/austin_case_admissibility_v3.json.

## 5. Required feeder-selection sequence

~~~math
\boxed{
G_f=G_P(f)G_T(f)G_S(f)G_H(f)G_V(f).
}
~~~

Only feeders with all five PASS enter:

~~~math
\mathcal F_{adm}=\{f:G_f=1\}.
~~~

If nonempty:

~~~math
\boxed{
f^*
=
\arg\min_{f\in\mathcal F_{adm}}n_{state}(f)
}
~~~

with lexical feeder ID as the deterministic exact-tie rule.

Selection may not use H1–H5 effects, viability margins, intervention ranking, sustainability outcomes, or confirmatory residuals.

## 6. Data qualification order

~~~math
\boxed{
\text{source identity}
\rightarrow
\text{immutable materialization}
\rightarrow
\text{schema/vintage qualification}
\rightarrow
\text{spatial/temporal alignment}
\rightarrow
\text{topology/interface QA}
\rightarrow
\text{parameter/requirement qualification}
\rightarrow
\text{case execution gate}.
}
~~~

A download success is not a gate PASS.

## 7. Mandatory provenance for every runtime object

Every runtime object must retain source identity, immutable SHA-256, byte/row/feature counts, vintage/temporal role, CRS/support, transformation code/version, upstream IDs, uncertainty/quality status, validity domain, consumers, and case/run identity.

## 8. Measurement, identification and parameter qualification

~~~math
\boxed{
G_{\theta,e}^{pre}
=
G_{\rm origin}
\land
G_{\rm meas}
\land
G_{\rm ID}^{struct}
\land
G_{\rm ID}^{strength}
\land
G_{\rm EST}^{admit}.
}
~~~

Execution readiness additionally requires:

~~~math
\boxed{
G_{\theta,e}^{ready}
=
G_{\theta,e}^{pre}
\land
G_{\rm EST-run}
\land
G_{\mathcal U}
\land
G_{\rm VAL}^{result}
\land
G_{\rm domain}.
}
~~~

For qualified noninferential specifications, identification fields may be N_A_NONINFERENTIAL with explicit provenance.

## 9. Requirements / acceptability

No P3 process may invent minimum service fractions, recovery targets/dwell, physical equipment limits, or H1–H5 materiality thresholds.

~~~math
\boxed{
\text{metric available}
\not\Rightarrow
\text{requirement authorized}.
}
~~~

K, G_rec, and F_unsafe remain BLOCKED until required provenance closes.

## 10. Hazard semantics

The current floodplain source is STATIC_SCENARIO_SUPPORT.

Allowed: exposure/susceptibility intersection and declared synthetic scenario construction.

Prohibited: interpreting FLOOD_ZONE as event depth; treating overlap as failure; calling the layer historical 2018 event truth; converting common hazard exposure into a P↔T dependency.

## 11. P→T and T→P interfaces

P→T signal-power:
- mechanism may remain causally accepted;
- local mapping is semisynthetic;
- mapping tolerance must be frozen pre-result;
- mapped power ID is never claimed as observed Austin Energy feeder assignment.

T→P repair access:
- structural route may be demonstrated first;
- road distance is not travel time;
- travel time, passability and onsite repair duration require separate qualification.

## 12. CI is part of execution readiness

~~~math
\boxed{
G_{repo,exec}
=
G_{syntax}
\land
G_{tests}
\land
G_{authority\_lint}
\land
G_{case\_instrument}.
}
~~~

CI failure is a repository execution blocker. It is not negative evidence for H1–H5.

## 13. P3 readiness instrument

methods/austin_case/p3_execution_readiness.py validates the v3 Austin contract and preconfirmatory registry, reports G0–G8 plus normalized P3 states, records runtime evidence-file presence, never upgrades a contract gate from file presence alone, preserves H1–H5 as NOT_TESTED, and writes a machine-readable manifest.

## 14. Completion criterion

~~~math
\boxed{
G_{P3}^{control}=PASS
}
~~~

means the qualification machinery is internally coherent.

~~~math
\boxed{
G_{case,exec}
=
\bigwedge_{f\in F_{required}(experiment)}G_f.
}
~~~

Only if the final-case contract itself becomes admissible may case execution become PASS.

No P3 control-plane PASS may be cited as empirical validation or hypothesis support.
