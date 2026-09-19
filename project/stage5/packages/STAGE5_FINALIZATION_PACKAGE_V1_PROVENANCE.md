# Stage 5 ZIP Snapshot Provenance

The canonical Stage-5 package is committed as individually inspectable governed artifacts under `project/stage5/`.

A local immutable ZIP snapshot was generated from the same source artifacts:

- Filename: `STAGE5_FINALIZATION_PACKAGE_V1.zip`
- Size: `48778` bytes
- SHA-256: `2c6356c0a64f61684e8dec9d431a46eab5e7b6324e9c7cc978571167782dd80d`
- Local Git blob hash: `94b393b65aba3ec0a66d4b4f7a98f918a21f08b2`

The connected GitHub binary-blob transport did not preserve this ZIP byte-for-byte during verification, so the archive itself is deliberately **not** committed. A corrupted archive must never be treated as provenance.

The individually committed source files plus `00_governance/SHA256SUMS.json` are the repository authority.
