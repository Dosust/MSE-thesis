# H3 SMART-DS Electrical Closure and OpenDSS QA v1.0

**Status:** PREPARED / EXECUTION GATED  
**Date:** 2026-09-17  
**Protocol:** EGMIV–TSP  
**Case:** `H3-HOU-FLOOD-V1`  
**Thesis destination:** Chapter 4 — H3 power-layer realization and model QA  
**Upstream authority:** `H3_SMARTDS_HOUSTON_PREEXTRACTION_V1.md`, `H3_SMARTDS_YEAR_QUALIFICATION_V1.md`

> This file freezes what must happen after the Houston candidate-substation inventory. It does not claim that any Houston SMART-DS substation has already been selected, downloaded, compiled, or solved.

---

## 1. Scientific destination

The power realization must produce a reproducible simulation graph and a separately defined service-accounting domain:

```math
\boxed{
\mathcal G_{P,sim}^{HOU}
\supseteq
\mathcal G_{P,svc}^{HOU}.
}
```

`G_P,sim` may include electrically necessary components outside `Omega_core`; `G_P,svc` contains only service-bearing assets/loads admitted to the Houston H3 denominator.

This distinction prevents geographical clipping from destroying electrical closure while also preventing exterior support elements from inflating Houston service.

---

## 2. Candidate-substation input

Candidate substations are defined upstream by

```math
I_s
=
\mathbf 1\{\exists v\in\mathcal V_s:\operatorname{coord}(v)\in\Omega_{core}\}.
```

Let

```math
\mathcal S_{core}=\{s:I_s=1\}.
```

Candidate status is geographic evidence only. It does not establish electrical validity, OpenDSS convergence, or final inclusion in H3.

---

## 3. Electrical closure rule

For each candidate `s`, first preserve the complete source-provided OpenDSS substation package rather than clipping individual lines/buses by municipal geometry.

Define

```math
\boxed{
\mathcal G_{P,sim}^{HOU}
=
\operatorname{closure}_{DSS}(\mathcal S_{core}),
}
```

where `closure_DSS` is the minimum set of source-provided files/elements required for each retained station-level `Master.dss` to resolve all explicit model dependencies and compile.

Operational rule:

```text
1. download the complete candidate-substation OpenDSS prefix;
2. preserve relative source paths exactly;
3. preserve all referenced internal feeders/elements;
4. if Master.dss resolves a documented dependency outside the candidate station prefix, add only that dependency and record why;
5. do not add neighboring substations merely to improve topology or H3 performance.
```

Every retained component outside `Omega_core` must ultimately be classified as service-bearing or boundary/support. Default:

```text
inside Omega_core       -> eligible for later service accounting;
outside Omega_core      -> in_service_denominator = 0 unless separately justified;
source dependency       -> is_boundary_connector/support = 1 with provenance.
```

No actual CenterPoint feeder/substation identity is inferred.

---

## 4. Raw materialization gate

Executable utility:

```text
methods/h3/materialize_smartds_houston_power.py
```

It hard-requires:

```text
G_Omega_QA = PASS;
2016 Houston candidate inventory present;
intersects_houston_core = true for every materialized station.
```

For every S3 object it freezes:

```text
S3 object key;
source size;
ETag metadata;
last-modified metadata;
raw relative path;
downloaded byte size;
SHA-256;
subregion/substation identity.
```

Raw objects are immutable after hash freeze.

Materialization success does **not** imply electrical QA success.

---

## 5. OpenDSS baseline QA gate

Executable utility:

```text
methods/h3/qa_smartds_power_layer.py
```

The QA implementation uses OpenDSSDirect.py / DSS-Extensions as a cross-platform programmatic interface to an OpenDSS-compatible engine. DSS-Extensions documents direct `redirect Master.dss` loading and exposes circuit/topology quantities including bus count, circuit elements, PD elements and convergence state.

This is a software implementation choice for **data/model verification**, not the Stage-5 H3 reachability solver.

For every retained substation, the hard baseline gate is:

```math
\boxed{
G_{P,s}^{base}
=
G_{compile}
\land
G_{solve}
\land
G_{nonempty}
\land
G_{finite}.
}
```

Required checks:

```text
station-level Master.dss resolves unambiguously;
OpenDSS redirect/compile raises no unresolved-source failure;
baseline snapshot solve converges;
number of buses > 0;
number of power-delivery elements > 0;
non-finite bus-voltage outputs = 0 when voltage output is available;
network counts recorded;
isolated branches/loads and loop counts reported where supported;
engine and Python-interface versions recorded.
```

A candidate failing compile/solve is **not admitted** to confirmatory H3 until the failure is traced to a source-supported transformation or the candidate is rejected transparently.

---

## 6. Network dimensions

For a passed set of station models, define the reproducible simulation-layer dimensions as

```math
\boxed{
N_P^{sim}
=
\sum_{s\in\mathcal S_{pass}}N_{bus,s},
}
```

and

```math
\boxed{
M_P^{sim}
=
\sum_{s\in\mathcal S_{pass}}N_{PD,s},
}
```

where `N_PD` is the OpenDSS count of power-delivery elements.

These quantities characterize the simulation graph only. They are not yet the service denominator used by `S_P`.

The service accounting later requires load-to-bus coordinates and `Omega_core` membership:

```math
\boxed{
\mathcal L_{P,svc}
=
\{\ell:\operatorname{bus}(\ell)\in\Omega_{core}\},
}
```

subject to explicit handling of missing coordinates and source semantics.

---

## 7. Voltage and topology diagnostics

Baseline voltage extrema, isolated branches, isolated loads and loop counts are recorded diagnostically.

No arbitrary voltage band is introduced in this QA step:

```math
\boxed{
\text{reported voltage extrema}
\neq
\text{H3 pass/fail threshold}.
}
```

Any engineering voltage/service limit used later must enter through the existing evidence/threshold qualification process with units, source authority, validity domain and uncertainty.

Likewise, an isolated component is reported but is not automatically a hard failure until its physical/service role is evaluated.

---

## 8. Gate logic

Current state before execution:

```math
\boxed{
G_{P,source}=1,
\quad
G_{P,year}=1,
\quad
G_{P,prep}=1,
\quad
G_{\Omega,QA}=0,
\quad
G_{P,inventory}=0,
\quad
G_{P,raw}=0,
\quad
G_{P,QA}=0.
}
```

Required sequence:

```math
\boxed{
G_{\Omega,QA}=1
\rightarrow
G_{P,inventory}=1
\rightarrow
G_{P,raw}=1
\rightarrow
G_{P,QA}=1.
}
```

No downstream gate may be promoted from code preparation alone.

---

## 9. Exact future commands

After boundary QA:

```bash
python methods/h3/inventory_smartds_houston.py \
  --root data/H3-HOU-FLOOD-V1 \
  --year 2016 \
  --scenario base_timeseries
```

Then:

```bash
python methods/h3/materialize_smartds_houston_power.py \
  --root data/H3-HOU-FLOOD-V1 \
  --year 2016 \
  --scenario base_timeseries
```

Then, in a frozen environment containing OpenDSSDirect.py:

```bash
python methods/h3/qa_smartds_power_layer.py \
  --root data/H3-HOU-FLOOD-V1 \
  --year 2016 \
  --scenario base_timeseries
```

---

## 10. Stopping rule

Stop and mark `G_P_QA=0` if any of the following remains unresolved:

```text
boundary QA missing;
candidate inventory absent;
source object hash/size mismatch;
missing or ambiguous station Master.dss;
unresolved OpenDSS references;
baseline solve non-convergence;
non-finite numerical outputs;
source/provenance inconsistency.
```

Do not repair model files silently and do not substitute a hand-built power network.

---

## References

DSS-Extensions. (n.d.). *OpenDSSDirect.py*. https://dss-extensions.org/OpenDSSDirect.py/

DSS-Extensions. (n.d.). *OpenDSS: Python APIs*. https://github.com/dss-extensions/dss-extensions/blob/main/docs/python_apis.md

Mateo, C., Postigo, F., Elgindy, T., Birchfield, A., Duenas, P., Palmintier, B., Panossian, N., Gomez, T., de Cuadra, F., Overbye, T., Safdarian, F., & Wallison, D. (2024). Building and validating a large-scale combined transmission & distribution synthetic electricity system of Texas. *International Journal of Electrical Power & Energy Systems, 159*.
