# Phase 1C — Pre-ACN Processing Verification v1

![Status](https://img.shields.io/badge/status-PRE--DATA%20IMPLEMENTATION%20PASS-1A7F37)
![Phase](https://img.shields.io/badge/phase-1C-0969DA)

**Executed:** 2026-09-12  
**Purpose:** record the verification evidence that can be established before authenticated ACN observations are accessed.  
**Boundary:** this document establishes implementation behavior on synthetic known-answer fixtures only. It does not establish ACN data quality, complete `G_D`, complete `G_V`, validation, or H1/H2.

---

## 1. Frozen implementation scope

The following objects were frozen before actual ACN records were opened:

```text
PHASE1_ACN_PROCESSING_PROTOCOL_V1.md
PHASE1_INFORMATION_PROCESSING_PROTOCOL_V1.md
PHASE1_PARAMETER_RESOLUTION_ACN_V1.md
phase1_exec/acn_processing.py
phase1_exec/information_processing.py
project/phase1_runtime/process_acn.py
project/phase1_runtime/process_information.py
tests/phase1/test_acn_processing.py
tests/phase1/test_information_processing.py
```

They define the deterministic chain

```math
\boxed{
D_{raw}
\rightarrow
\text{schema/QC}
\rightarrow
P_{ch}^{5min}
\rightarrow
(D_{cal},D_{val})
\rightarrow
\text{calibration-only information model}
\rightarrow
\text{frozen verification metrics}.
}
```

---

## 2. Pre-data rules frozen before observation `[P/D]`

The implementation now explicitly resolves edge cases that otherwise could become post-hoc degrees of freedom:

```text
1. 2019-10-10 is excluded from complete-day load analysis because the frozen
   connectionTime query cannot guarantee sessions that connected before the
   left query boundary are present.

2. 2019-11-03 America/Los_Angeles is excluded because it is a 25-hour DST
   fallback day and cannot satisfy the already-frozen 288-slot/day definition
   without silently collapsing an hour.

3. Time-series gaps greater than 5 minutes fail session QC.

4. Unknown spaceID values fail closed instead of receiving an invented voltage.

5. Charging power is reconstructed from the frozen Caltech infrastructure
   station-voltage mapping and measured charging current.

6. Reconstructed energy is not rescaled to kWhDelivered; the latter remains an
   independent consistency quantity for V-D06.

7. The information residual pool is calibration-only and uses leave-one-day-out
   day-type/slot means to avoid self-inclusion.

8. The persistence comparator uses the most recent usable prior day, same slot,
   with the seasonal and persistence RMSEs evaluated on identical support.

9. Information latency has no wrap-around; unavailable prehistory is NA.
```

These choices were made before actual ACN validation-day errors were available.

---

## 3. Resolved software-configuration quantities `[E/P]`

Under the frozen ACN Portal 0.3.3 Caltech infrastructure configuration:

```math
\boxed{V_n=208\ \mathrm{V}}
```

for registered EVSEs under the unmodified default configuration, with voltage retrieved from the station mapping, and

```math
\boxed{\bar P_{site}=150\ \mathrm{kW}.}
```

The site capacity is therefore a frozen infrastructure-software quantity, not a calibrated parameter.

---

## 4. Executed workflow evidence `[E]`

GitHub Actions execution:

```text
workflow = Phase 1 authenticated ACN acquisition
run ID   = 34702846875
job ID   = 103577541332
head SHA = 5a33d8686bb76938ea008a88af99d2aa3db824aa
```

The canonical Phase-1 hash-locked environment installed successfully before the tests.

Synthetic ACN/information fixture result:

```text
16 passed in 0.17 s
```

The executed fixture set covers at least:

```text
timezone-aware timestamp enforcement;
constant-current analytical energy reconstruction;
exact 5-minute aggregation known answer;
DST fallback exclusion;
chronological 70/30 split disjointness;
unknown-station fail-closed behavior;
>5-minute trace-gap fail-closed behavior;
Caltech site-capacity constant;
weekday/weekend classification;
seasonal-slot known-answer means;
leave-one-day-out residual known answers;
minimum data requirement for LOO residuals;
calibration median P_ref;
causal previous-usable-day persistence;
paired seasonal-vs-persistence RMSE support;
latency operator no-wrap / explicit-NA behavior.
```

Thus

```math
\boxed{G_{preACN,impl}=1}
```

for the declared synthetic known-answer implementation domain.

This is **not** one of the final empirical gates and cannot compensate for unavailable raw data.

---

## 5. Credential gate executed after synthetic tests `[E]`

The same workflow proceeded to the external credential check and observed:

```text
ACN_API_TOKEN = absent
DATA_GATE     = BLOCKED_EXTERNAL_CREDENTIAL
```

The raw ACN request was therefore skipped. The processing and information stages were also skipped because their immutable input did not exist.

Credential hygiene executed successfully and the workflow retained failure evidence.

Evidence artifact:

```text
artifact ID         = 10301410343
artifact ZIP SHA256 = 00b86e2de1ecc5f27338c5a953a739aa5088d2f8ce5a5380e12ee6b09f46ff79
```

No ACN observation was opened in this run.

---

## 6. Current gate logic

The verified pre-data implementation changes the interpretation of the remaining work, but not the gate values:

```math
\boxed{
G_{ENV}=1,
\qquad
G_D=0,
\qquad
G_V=0.
}
```

More precisely:

```text
public P/T provenance                         CLOSED
public P/T numerical verification             PASS
pre-data ACN processing implementation        PASS on synthetic fixtures
pre-data information implementation           PASS on synthetic fixtures
ACN authenticated raw provenance              OPEN / credential blocked
actual ACN QC + 5-min trajectory               NOT EXECUTED
actual D_cal / D_val hashes                    NOT GENERATED
V-D06 on actual ACN data                       NOT EXECUTED
V-I04 on actual ACN validation days            NOT EXECUTED
complete R* reproducibility                    OPEN
complete G_V                                   OPEN
validation / H1 / H2                           BLOCKED
```

---

## 7. Next admissible transition

Once the authorized repository secret `ACN_API_TOKEN` exists, rerun the already-frozen workflow. The admissible sequence is

```math
\boxed{
\text{authenticate}
\rightarrow
H_D
\rightarrow
\text{QC/5-min processing}
\rightarrow
H_{proc}
\rightarrow
H_{cal},H_{val}
\rightarrow
V\text{-}D06
\rightarrow
V\text{-}I04
\rightarrow
\text{remaining full verification}.
}
```

A failure of V-D06 or V-I04 must be preserved as a verification result; their thresholds/model definitions may not be changed merely to obtain a pass.

Validation and H1/H2 remain unauthorized until the complete mandatory verification gate closes.
