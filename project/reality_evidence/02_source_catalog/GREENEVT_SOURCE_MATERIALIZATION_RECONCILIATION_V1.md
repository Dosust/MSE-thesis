# GreenEVT Source Materialization and Identity Reconciliation V1

**Date:** 2026-09-19  
**Scope:** Greensboro / GreenEVT / SMART-DS development case  
**Case role:** `C_DEV_GREENSBORO_GREENEVT_V1`  
**Purpose:** reconcile the repository's apparently conflicting statements that GreenEVT critical objects were previously materialized and source-audited, while current source-backed B2 execution still reports materialization as unavailable.

## 1. Conclusion

The two records refer to **different gates** and are not scientifically equivalent:

```math
oxed{
G_{SRC-ID}=PASS
quad
eqquad
G_{RUNTIME-DATA}=PASS.
}
```

Current decision:

```text
SOURCE IDENTITY / PRIOR FULL-OBJECT MATERIALIZATION: PASS
CURRENT EXECUTION-ENVIRONMENT DATA AVAILABILITY: BLOCKED
SOURCE-BACKED B2 EXECUTION: BLOCKED
```

Therefore the GreenEVT source itself is no longer classified as unqualified. The remaining blocker is binding the exact audited bytes into the execution environment used for B2/Stage 3.

## 2. Evidence chain inspected

### 2.1 Frozen upstream GreenEVT commit

Upstream commit already frozen by the Stage-3 audit:

```text
6aff1cac48869ccfa0183643979f5f04b04e1124
```

At that commit, GreenEVT tracks `*.db` and `*.net.xml` through Git LFS.

The exact upstream pointer records are:

```text
data/UDS.db
oid sha256:74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724
size 107778048

data/sumo_network/greensboro.net.xml
oid sha256:f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06
size 351967227
```

The upstream README explicitly states that the project uses Git LFS and publishes a fallback project ZIP for users unable to clone due to quota limits.

### 2.2 Existing thesis full-object audit

`models/H1/level2/artifacts/uploaded_source_audit_v1.json` records a previously supplied `GreenEVT.zip`:

```text
archive size  = 205091557 bytes
archive SHA256 = 643a0f3aab5b61d6396131ede3633741e1d1b34a921761edf3f780a1510c410e
```

It records the full extracted objects:

| Object | Full-object size | Full-object SHA-256 | Upstream LFS OID | Identity |
|---|---:|---|---|---|
| `data/UDS.db` | 107,778,048 | `74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724` | same | PASS |
| `data/sumo_network/greensboro.net.xml` | 351,967,227 | `f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06` | same | PASS |

Because the Git-LFS OID is a SHA-256 content identity, equality of full-object SHA-256 and frozen upstream OID establishes byte-level identity for these two critical objects.

### 2.3 Current runtime blocking record

`project/stage5/12_execution/SOURCE_BACKED_B2_BLOCKING_AUDIT_V1.json` records that the then-current execution environment contained only pointer identities and lacked:
- materialized critical objects;
- `git-lfs`;
- SUMO;
- OpenDSSDirect-Python;
- external DNS/network access from that runtime.

That record is retained as valid historical execution-environment evidence.

## 3. Reconciliation

The following statements can simultaneously be true:

```math
oxed{
	ext{exact GreenEVT objects were previously materialized and hash-verified}
}
```

and

```math
oxed{
	ext{the current B2 runner does not contain those materialized bytes}.
}
```

Hence:

| Gate | Meaning | Status |
|---|---|---|
| `G_SRC-PTR` | upstream pointer identities frozen | PASS |
| `G_SRC-FULLHASH` | prior full objects match LFS OIDs | PASS |
| `G_SRC-SIZE` | prior full objects match declared sizes | PASS |
| `G_SRC-PROV` | thesis audit preserves archive/object hashes | PASS |
| `G_RUNTIME-UDS` | exact UDS bytes available in active execution runtime | BLOCKED |
| `G_RUNTIME-SUMO-NET` | exact SUMO network bytes available in active execution runtime | BLOCKED |
| `G_RUNTIME-SOLVERS` | required executables/libraries available | BLOCKED |
| `G_B2-SOURCEBACKED` | source-backed B2 executable now | BLOCKED |

## 4. Provenance caution

The upstream GreenEVT README publishes a fallback ZIP URL. The existing thesis audit records the uploaded archive's name, size and SHA-256, but does **not** separately freeze a retrieval URL/HTTP provenance record for that exact archive byte stream.

Therefore:

```math
oxed{
	ext{critical-object identity}=PASS
}
```

while the stronger statement

```text
"the audited archive byte-for-byte came from the documented fallback URL"
```

is **NOT ASSERTED** without a retrieval manifest.

This limitation does not affect the exact identity of the two critical objects because their hashes match the frozen upstream Git-LFS OIDs.

## 5. Runtime materialization protocol

Before source-backed B2 execution, the execution environment must:

1. receive the exact full objects from an authorized source/archive;
2. compute SHA-256 locally;
3. require exact match to the frozen OIDs;
4. require exact byte sizes;
5. verify the ordinary Git blobs already frozen in the source audit;
6. verify database/XML parseability;
7. record runtime/tool versions;
8. record acquisition/materialization provenance;
9. preserve raw files read-only;
10. execute B2 only after all runtime gates PASS.

Required exact identities:

```text
UDS.db
SHA256 = 74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724
bytes  = 107778048

greensboro.net.xml
SHA256 = f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06
bytes  = 351967227
```

No near-match, regenerated substitute, or alternative network export may silently replace these objects in the source-backed benchmark.

## 6. Scientific effect

This audit changes **status interpretation**, not scientific results.

It does not:
- close Stage 3;
- resolve EV charging power;
- authorize feeder selection;
- validate GreenEVT against observed Greensboro utility wiring;
- authorize H1/H2/H3;
- make B2 a validation result.

## 7. Next P0 blocker

After separating source identity from runtime availability, the remaining scientific P0 sequence is:

```math
oxed{
	ext{runtime binding of exact GreenEVT bytes}
parallel
	ext{EV charging parameter/uncertainty authority}
ightarrow
G_{2	o3}(EV_{T	o P})
ightarrow
	ext{source-backed B2/Stage-3 execution}.
}
```
