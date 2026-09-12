# Phase 1B — ACN Acquisition Blocker and Resolution Protocol v1

**Status:** `BLOCKED_EXTERNAL_CREDENTIAL`  
**Date:** 2026-09-12  
**Authority:** `PHASE1_DATA_MANIFEST_V1.md` + `PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md`  
**Purpose:** make the unresolved ACN raw-data hash scientifically explicit rather than fabricating or substituting data.

---

## 1. Verified external constraint `[E]`

The ACN-Data portal states that users must register to obtain an access token for the REST API. The Python `DataClient` likewise requires an API token. The `/ts` endpoint is required when time-series current/pilot information is needed.

Therefore the frozen Caltech extraction cannot be completed reproducibly in the current automated environment without an authorized ACN token.

This is an **external access constraint**, not a scientific failure of the experiment.

---

## 2. Frozen request `[P]`

The acquisition target remains unchanged:

```text
site      = caltech
start     = 2019-10-10 00:00:00 America/Los_Angeles
end       = 2019-12-31 23:59:59 America/Los_Angeles
timeseries= true where required by replay/reconstruction
client    = acnportal 0.3.3
```

The source/window may not be altered to bypass authentication.

---

## 3. Secure credential rule

The token must be supplied only at execution time through

```text
ACN_API_TOKEN
```

as an environment variable or equivalent secret store.

It must never appear in:

```text
Git commits;
Markdown manifests;
notebooks;
command history committed to the repository;
CI logs;
JSON result files;
container image layers.
```

No user credential should be pasted into thesis source files.

---

## 4. Required acquisition artifact

The acquisition script must write an immutable raw object, for example

```text
data/raw/acn/caltech_2019-10-10_2019-12-31_ts.jsonl
```

without subsequent in-place edits.

Immediately record:

```text
UTC acquisition timestamp;
API base URL;
site;
exact query interval;
timeseries flag;
client version;
client/source commit;
record count;
file byte size;
SHA-256;
schema/field snapshot.
```

Then compute

```math
h_{raw}=SHA256(D_{raw}).
```

---

## 5. Processed artifact

Using only the frozen QC and transformation rules, generate the 5-minute processed charging artifact and compute

```math
h_{processed}=SHA256(D_{processed}).
```

Also freeze:

```text
usable-day list;
excluded-day list + reason;
70/30 chronological split;
calibration-date list;
validation-date list;
processing-code Git SHA.
```

Each list/file receives its own SHA-256.

---

## 6. Failure policy

If authenticated acquisition of the frozen source/window fails:

```text
STATUS = PHASE1 DATA ACQUISITION FAILED / EXECUTION BLOCKED.
```

Permitted actions:

```text
- diagnose API/client/network failure;
- retry the same frozen request;
- update only software/transport mechanics through a versioned environment amendment if required.
```

Not permitted inside v1:

```text
- change site;
- change date window;
- switch to JPL/Office1;
- use synthetic charging sessions instead;
- use a different dataset because it is easier to download;
- omit time series if the frozen replay requires them.
```

A scientifically justified data-source change requires

```text
PHASE1_DATA_MANIFEST_V2.md
```

and a corresponding experiment amendment before results are inspected.

---

## 7. Gate state

```text
ACN SOURCE IDENTITY        LOCKED
ACN WINDOW                 LOCKED
ACN CLIENT VERSION         LOCKED
AUTHORIZATION TOKEN        REQUIRED EXTERNALLY
RAW ACN FILE               NOT YET ACQUIRED
RAW SHA-256                BLOCKING-PENDING
PROCESSED FILE             BLOCKING-PENDING
PROCESSED SHA-256          BLOCKING-PENDING
CAL/VAL DATE HASHES        BLOCKING-PENDING
```

Therefore:

```math
\boxed{
\text{Phase 1B can freeze methodology while}
\quad
\text{Phase 1 execution remains blocked.}
}
```

This is the correct outcome under the thesis rule: **never invent evidence to satisfy a workflow gate.**

---

## 8. External evidence anchors

- ACN-Data portal: API authentication requires registration/access token; API and Python client access are documented by Caltech.
- ACN Research Portal `DataClient(api_token, ...)`: token is a required constructor argument.
- ACN-Sim tutorials: data-generated events require an API key/token.
