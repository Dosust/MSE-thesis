# CPX-Q3 access/session limitation note — 2026-09-08

## User-reported access context

The researcher is an Arizona State University student currently located in Singapore and accesses Engineering Village / Compendex through ASU authentication. Off-campus access may require VPN/proxy authentication.

## Observed technical behavior

During CPX-Q3 assembly:
- previously valid Engineering Village `SEARCHID` values became unavailable/invalid;
- Search History reached 50 searches, making session-local `#ID` references unstable;
- grouped/long Expert Search expressions sometimes returned generic system errors;
- fresh atomic Expert Search queries still worked (for example `({power grid*} WN KY) AND (2000-2026 WN YR)` returned the expected 130,964 records).

## Scientific interpretation

These events are treated as an **access/session execution limitation**, not as evidence that the frozen scientific query is invalid.

Do not claim that Engineering Village definitively rejected a Singapore IP address unless ASU Library / Engineering Village explicitly confirms this. The defensible wording is:

> Native Compendex Q3 assembly was interrupted by off-campus authentication/VPN-dependent access and Engineering Village session/search-history instability while the researcher was outside the United States.

## Protocol consequence

- Do not redesign Q3 because of this access problem.
- Preserve all completed atomic counts, screenshots, hashes, and the valid `Z_Q3 = 431,898` union.
- Resume final Q3 block assembly only when access/session stability is sufficient.
- Treat any rerun of already validated atoms as execution reconstruction, not new scientific search development.
