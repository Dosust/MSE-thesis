# Phase 1C — ACN Acquisition Blocker and Executed Resolution Protocol v1

**Status:** `BLOCKED_EXTERNAL_CREDENTIAL`  
**Date:** 2026-09-12  
**Authority:** `PHASE1_DATA_MANIFEST_V1.md` + `PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md` + `PHASE1_DATA_PROVENANCE_REGISTER_V1.md`  
**Purpose:** record both the frozen ACN acquisition protocol and the actual executed credential-gate results without fabricating or substituting data.

---

## 1. Frozen acquisition target `[P]`

```text
site       = caltech
start      = 2019-10-10 00:00:00 America/Los_Angeles
end        = 2019-12-31 23:59:59 America/Los_Angeles
timeseries = true
client     = acnportal==0.3.3
script     = project/phase1_runtime/acquire_acn.py
workflow   = .github/workflows/phase1-acn-acquisition.yml
```

No source, site, interval or time-series requirement may be changed to bypass authentication.

---

## 2. Executed access tests `[E]`

### Attempt 1

```text
workflow name       = Phase 1 authenticated ACN acquisition
run ID              = 34698786730
run attempt         = 1
job ID              = 103566760990
head SHA            = c509d7de85627dda9f99023aa8acb5b24737cc9d
status              = completed
conclusion          = failure
```

### Attempt 2 — explicit rerun after public P/T verification closure

```text
workflow name       = Phase 1 authenticated ACN acquisition
run ID              = 34698786730
run attempt         = 2
job ID              = 103573035993
head SHA            = c509d7de85627dda9f99023aa8acb5b24737cc9d
started UTC         = 2026-09-12T15:05:06Z
completed UTC       = 2026-09-12T15:05:37Z
status              = completed
conclusion          = failure
```

Attempt-2 step evidence:

```text
checkout exact commit                     PASS
Python 3.11.16 setup                       PASS
canonical lock SHA verification/install   PASS
ACN_API_TOKEN presence gate               FAIL
raw-data acquisition                       SKIPPED
provenance freeze                          SKIPPED
credential-hygiene step                    SKIPPED
raw artifact upload                        SKIPPED
```

The second execution independently confirms that the repository Actions environment still lacks the required `ACN_API_TOKEN`. The workflow again stopped before any API request or ACN data transformation.

Scientific interpretation:

```math
\boxed{
\text{credential absence}
\neq
\text{data invalidity}
\neq
\text{model failure}.
}
```

It remains an unresolved external-access prerequisite `[U]`.

---

## 3. Secure credential rule

The authorized ACN token must be configured as GitHub Actions repository secret:

```text
ACN_API_TOKEN
```

It must **not** be pasted into Markdown, source files, notebooks, workflow YAML, committed shell history, CI output, JSON evidence or container layers.

The workflow checks only whether the secret is present; it never prints the secret.

---

## 4. Immutable raw object

On the first successful authenticated rerun, the acquisition code must record:

```text
UTC acquisition timestamp;
API/source identity;
site and exact frozen query interval;
timeseries flag;
client/software identity;
record count;
raw byte size;
raw SHA-256;
manifest SHA-256;
page/object SHA-256 identities as implemented;
credential-hygiene PASS.
```

Define

```math
H_D=SHA256(D_{raw}).
```

Raw data are never overwritten by preprocessing.

---

## 5. Processing chain

Only after `H_D` exists:

```math
D_{raw}\xrightarrow{T_1}D_{parsed}\xrightarrow{T_2}D_{5min}\xrightarrow{T_3}(\mathcal D_{cal},\mathcal D_{val}).
```

Each transformation must be deterministic, code-versioned and produce a separately hashed output.

The chronological split remains:

```math
N_{cal}=\lfloor0.70N_d\rfloor,
```

with the earliest usable complete days assigned to calibration and the remaining usable complete days assigned to validation.

---

## 6. Failure policy

If the token is configured but authenticated acquisition still fails, permitted actions are limited to diagnosing and retrying the **same frozen request**.

Not permitted inside Phase-1 v1:

```text
change Caltech to another site;
change the date window;
replace ACN with synthetic sessions;
omit required time-series information;
select another charging dataset because it is easier to obtain.
```

A source change requires a versioned experiment/data-manifest amendment before results are inspected.

---

## 7. Current gate state

```text
ACN source identity           LOCKED
ACN window                    LOCKED
ACN client                    LOCKED
canonical software lock       PASS
secure acquisition workflow   IMPLEMENTED + EXECUTED TWICE
ACN_API_TOKEN                 ABSENT / EXTERNAL ACTION REQUIRED
raw file                      NOT ACQUIRED
H_D                           BLOCKING-PENDING
processed charging trajectory BLOCKING-PENDING
calibration/validation hashes BLOCKING-PENDING
```

Therefore

```math
\boxed{G_{ACNraw}=0\text{ (gate open; credential blocked).}}
```

This `0` is not evidence of bad ACN data; no ACN data were accessed.

---

## 8. Exact unblock operation

1. Obtain/retain an authorized ACN API token through Caltech's ACN access process.
2. Add it in GitHub repository **Settings -> Secrets and variables -> Actions -> New repository secret** with name `ACN_API_TOKEN`.
3. Do not paste it into the thesis repository or chat.
4. Rerun workflow **Phase 1 authenticated ACN acquisition**.
5. Accept `G_ACNraw=1` only if the workflow records the required raw hash/provenance fields and uploads the immutable evidence artifact.

Until this occurs, `H_D`, `\mathcal R^*`, complete `G_V`, empirical validation and H1/H2 remain blocked.

---

## 9. Current hard boundary

The transport numerical blocker has now been closed independently through the audited BFW amendment. Therefore the ACN credential is the **single external blocker** preventing the next data-provenance step.

```math
\boxed{
\text{PUBLIC P/T VERIFICATION PASS}
\quad\land\quad
\text{ACN CREDENTIAL BLOCKED}
\Rightarrow
\text{STOP BEFORE VALIDATION/H1/H2}.
}
```
