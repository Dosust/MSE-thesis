# Reproducibility Manifest — 2026-08-21

## Session-local source artifact hashes

The following SHA-256 hashes were computed from the session-local files before archival/synthesis:

| Artifact | SHA-256 | Note |
|---|---|---|
| `Pasted markdown(20260821-114450).md` | `4c5cd304e6b10d5cd17c90e05cd9781dcb383d601a37cd869a338de493c0c632` | 1744-line long-form six-chain source supplied in session; capsule includes a distilled snapshot, not a claim of byte-for-byte copy |
| `run_or_mc.py` | `3910176fbba5c4b542d6a658563d8e2b091ed1be6d13525241ded7540b383e26` | original session-local Monte Carlo script; repository copy preserves algorithm but changes output path to a relative path |
| `or_mc10m_results.json` | `e5726de0d3a3604d4c10bbed360f7959a582de18994c1491078afb4099ebdc0e` | original full machine-readable result file; repository snapshot preserves core score matrix/results and high-rigor scenario |
| `OR_infrastructure_AI_10M_results.txt` | `0f70b3202c54437140b2f7f054f8708d022fa69fdd2f55b9bcd944737f10e495` | human-readable result snapshot archived in this capsule |
| `wolfram_infrastructure_visual_template.wl` | `91fc7c11cadb9725d55cd48ca8984e443c264b3f3177f96f2bdadf304d56fbe3` | session-local Wolfram template; repository copy adds a status note documenting later fidelity criticism |
| `wolfram_inspired_theme.json` | `e79130b707cab1b603851136129fe0cb1e5d7654f17da636d60e51bafc851409` | session-local theme; repository copy adds a status note |

## Monte Carlo reproducibility parameters

- draws: `10_000_000`
- seed: `57420260821`
- chunk size: `200_000`
- Dirichlet concentration: `120`
- concepts: `19`
- criteria: `10`
- score bounds: `[0,100]`
- output quantiles: approximate histogram-based 5%, 50%, 95%

## GitHub archival location

`conversation/2026-08-21_math_physics_foundations/`

The folder is intended to be self-describing. Future runs should add a new dated capsule rather than silently rewriting this historical checkpoint.

## Reproduction warning

The Monte Carlo results reproduce only if the same:

- score matrix,
- criteria,
- weight prior,
- evidence-uncertainty model,
- seed,
- NumPy behavior/version,
- code path,
- number of draws

are used.

The OR portfolio values additionally depend on the exact deterministic optimization formulation/constraints described in `OR_MONTE_CARLO_REPRODUCIBILITY.md` and the session implementation.
