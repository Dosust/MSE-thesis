# Session Snapshot Archive

The byte-preserving snapshot of the active 2026-08-20 thesis session is stored online in the user's connected Google Drive and is indexed from GitHub through `provenance/ONLINE_ARCHIVE.md`.

## Verified current-session archive

File:

`MSE-thesis-current-session-artifacts-2026-08-20.zip`

Size:

`2,703,060 bytes`

SHA-256:

`6d2682356ad0ba4a879c3ee398f4fc65fa60f4b2b9899e5e369820dfa1f92e8c`

The Drive file was read back through the connected account after upload and the downloaded bytes were independently re-hashed to the value above.

## Why the binary archive is referenced rather than embedded here

The GitHub write interface available in this session writes UTF-8 repository content but does not expose a mounted-local-file argument for arbitrary binary files. Large/binary artifacts are therefore kept in the verified online byte archive and mapped by exact filename, size, and SHA-256 in `provenance/INVENTORY.csv` and `provenance/SHA256SUMS.txt`.

This is a deliberate provenance distinction: GitHub is the version-controlled research record; the linked Drive ZIP is the byte-preserving artifact store. No partial Base64 reconstruction set is treated as authoritative.
