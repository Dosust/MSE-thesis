# EGMIV H1 Autonomous Execution Package v1.0

This package turns the remaining H1 workflow into a deterministic scientific state machine:

\[
\text{execute}\rightarrow\text{verify}\rightarrow\text{freeze}\rightarrow\text{advance}.
\]

## Current hard gate

`S08 — RAW BYTE ACQUISITION` is externally blocked in the current chat runtime.

Independent checks performed:

1. official NYISO archive links and exact ZIP URLs were verified;
2. the web tool could resolve archive links but could not materialize ZIP bodies;
3. container direct download failed;
4. direct Python/container networking failed at DNS resolution;
5. ChatGPT Library search did not find the required raw files;
6. the thesis Library folder did not contain them;
7. the visible Google Drive mount did not expose them in inspected locations.

No row count, null rate, duplicate rate, gap statistic, or coverage value has been fabricated.

## EAGLE-I file IDs

Official Figshare article `24237376` file IDs independently corroborated:

- 2020: `42547894`
- 2022: `42547897`
- 2023: `44574907`
- 2024: `53581661`

## Candidate split

\[
D_{\rm train}^{cand}=\{E0,E2\},\qquad
D_{\rm test}^{cand}=\{E1,E3,E4\}.
\]

It remains **candidate only** until R1–R8 pass.

## Resume

Place publisher-original raw files under `H1_RAW_DATA_v1/` without editing them, then run:

```bash
python autonomous_h1_controller.py
```

The controller hashes every required binary and refuses progression if any required core source is absent.
