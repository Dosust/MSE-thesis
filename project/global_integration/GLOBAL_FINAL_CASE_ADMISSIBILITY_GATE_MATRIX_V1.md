# Global Final-Case Admissibility Gate Matrix v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.5 GATE CONTROL

## 1. Gate definition

For every field \(f\):

~~~math
\boxed{
\begin{aligned}
G_f={}&
G_{semantic}
\land G_{type}
\land G_{unit}
\land G_{spatial}
\land G_{temporal}
\land G_{source}\\
&\land G_{provenance}
\land G_{quality}
\land G_{uncertainty}
\land G_{reference}
\land G_{validity}
\land G_{ownership}.
\end{aligned}
}
~~~

Gate states: PASS, BLOCKED, FAIL, DEFERRED, N/A.

## 2. Gate semantics

| Gate | PASS | BLOCKED | FAIL | N/A |
|---|---|---|---|---|
| semantic | definition and scientific meaning unambiguous | meaning unresolved | meaning conflicts with authority | never N/A for core fields |
| type | data/object shape matches declared type | shape/schema unresolved | incompatible object type | never N/A |
| unit | dimensional semantics explicit/compatible | unit missing/unresolved | dimensional incompatibility documented | allowed only for truly unitless/non-quantity objects |
| spatial | CRS/support/extent adequate | required spatial metadata missing | incompatible CRS/geometry unresolved | nonspatial field |
| temporal | time reference/resolution adequate | required timing unresolved | incompatible/misaligned timing | nontemporal field |
| source | acceptable source class identified | source unavailable/unresolved | source violates declared eligibility | only if scientifically source-free derived object |
| provenance | source→transform→object lineage complete | lineage incomplete | contradictory/unverifiable lineage | never N/A for bound external/derived inputs |
| quality | relevant quality evidence described | quality not yet assessed | fails frozen quality requirement | not applicable to purely formal object |
| uncertainty | required UQ representation present | UQ unresolved | representation contradicts evidence/intended use | deterministic formal object only |
| reference | P1.4 class explicit | class unresolved | prohibited class/use | NONE only when no reference role exists |
| validity | intended-use domain defined | domain unresolved | outside declared domain | never N/A |
| ownership | owner/consumers agree with global registry | mapping unresolved | ownership contradicts frozen stage authorities | never N/A |

## 3. Applicability matrix

Legend: M = mandatory, C = conditional, N = normally N/A.

| Field | semantic | type | unit | spatial | temporal | source | provenance | quality | uncertainty | reference | validity | ownership |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\mathcal G\) | M | M | C | M | C | M | M | M | M | M | M | M |
| \(Y_0\) | M | M | M | C | M | M | M | M | M | M | M | M |
| \(\theta\) | M | M | M | C | C | M | M | C | M | M | M | M |
| \(\eta\) | M | M | M | M | M | M | M | M | M | M | M | M |
| \(T\) | M | M | M | N | M | M | M | C | C | M | M | M |
| \(K\) | M | M | M | C | C | M | M | C | M | M | M | M |
| \(G_{\rm rec}\) | M | M | M | C | M | M | M | C | M | M | M | M |
| \(F_{\rm unsafe}\) | M | M | M | C | C | M | M | C | M | M | M | M |
| \(\mathcal U_{\rm feas}\) | M | M | M | C | M | M | M | C | M | M | M | M |
| \(\mathcal A\) | M | M | M | C | M | M | M | C | M | M | M | M |
| \(\Omega\) | M | M | C | M | M | M | M | C | M | M | M | M |

## 4. Field-specific pass conditions

### G
PASS requires typed P/T topology, geometry/CRS, versioned sources, interface/crosswalk provenance, topology QA and Stage-2 linkage semantics. Spatial proximity alone cannot satisfy the interface gate.

### Y0
PASS requires common \(t_0\), state ordering, units, synchronization, source/reconstruction role, uncertainty and consistency with \(\mathcal G\).

### theta
PASS requires every active parameter used by the execution path to have type, unit, source class, value/range if bound, UQ/dependence, validity and owner. A SENSITIVITY_ONLY parameter cannot silently become CALIBRATED.

### eta
PASS requires physical hazard quantity, units, spatial/temporal support, source version, observed/reanalysis/synthetic classification and UQ.

### T
PASS requires purpose-specific dynamic horizon, time units and explicit non-equivalence with lifecycle horizon unless justified.

### K / G_rec / F_unsafe
PASS requires requirement IDs, equations/sets, dimensional thresholds, authority class, scope and UQ. Research assumptions remain labeled as such.

### U_feas
PASS requires explicit physical, information, organization and resource constraint components or documented N/A status for a component under the case architecture.

### A
PASS requires each candidate intervention used in analysis to have an executable model transformation or be excluded/BLOCKED, plus resources, timing, service life/accounting boundary and provenance.

### Omega
PASS requires explicit spatial, temporal, hazard, operating, model and uncertainty domains and exclusions. It cannot be replaced by a finite scenario list.

## 5. Aggregation rule

A required field is execution-ready only if:

~~~math
\boxed{
G_f=PASS.
}
~~~

At pre-data design freeze, field status may be DEFERRED without failing P1.5 design.

Case execution gate:

~~~math
\boxed{
G_{case,exec}
=
\bigwedge_{f\in F_{required}(experiment)}G_f.
}
~~~

No downstream stage may upgrade BLOCKED/FAIL to PASS without new qualified evidence and recorded provenance.
