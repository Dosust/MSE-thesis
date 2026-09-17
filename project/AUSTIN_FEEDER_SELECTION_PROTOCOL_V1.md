# Austin Feeder Selection Protocol v1.0

**Date:** 2026-09-18  
**Case family:** SMART-DS Austin v1.0 / 2018  
**Status:** SELECTION RULE FROZEN / FEEDER ID OPEN

## 1. Purpose

The feeder is selected entirely from **pre-result admissibility information**. No H1--H5 effect, viability boundary, intervention ranking or sustainability outcome may be inspected during selection.

## 2. Candidate set

For each SMART-DS feeder `f`, define:

```math
G_f
=G_P(f)G_T(f)G_S(f)G_H(f)G_V(f),
```

where each gate is Boolean.

### `G_P` -- complete power realization

PASS only if:

```text
feeder Buscoords are available;
Master/Lines/Loads/Transformers and referenced circuit files are complete;
required profile objects are materialized;
OpenDSS parses and solves the undisturbed reference case;
all model-native units/voltage bases are identified.
```

### `G_T` -- routable transportation support

PASS only if the feeder's retained power assets overlap a nonempty City road graph and every experiment repair target can be attached to a routable road component from the declared crew origin.

### `G_S` -- P->T interface support

PASS only if at least two independently located traffic signals can be retained and mapped under the frozen synthetic mapping rule. Two is the minimum required to avoid reducing the supporting interface-comparison problem to a single interface; a larger number is retained whenever the data provide it.

### `G_H` -- coupled flood exposure

For the primary flood experiment, PASS only if the qualified flood geometry intersects at least one retained power component and at least one retained road component. Flood exposure remains distinct from causal P<->T coupling.

### `G_V` -- empirical transport observation support

PASS only if at least one spatially matched 2018 Austin radar sensor has usable observations in the retained transportation domain after QC.

## 3. Selection rule

Let

```math
\mathcal F_{adm}=\{f:G_f=1\}.
```

If `F_adm` is nonempty, select

```math
\boxed{
f^*=\arg\min_{f\in\mathcal F_{adm}} n_{state}(f)
}
```

where `n_state(f)` is the declared computational state dimension of the **unreduced** feeder/road realization required by H1--H3. If an exact tie remains, break it deterministically by lexical feeder ID.

This rule chooses the smallest scientifically adequate case, not the case with the largest observed hypothesis effect.

## 4. Subregion fallback

P5U is only the first candidate subregion. If no P5U feeder satisfies all gates, evaluate the other Austin SMART-DS urban subregions under exactly the same gates. The order is deterministic by subregion identifier; the final selection again minimizes `n_state` over the full admissible set.

No subregion or feeder may be rejected because its later H1--H5 result is weak or negative.

## 5. Data-vintage rule

SMART-DS 2018, City GIS layers, current Austin Energy service-area geometry and historical radar data are not an exact historical reconstruction of one Austin year. The selected case is therefore a geographically grounded **semisynthetic mechanism-validation experiment**. Every dataset retains its own vintage in the manifest.

## 6. Selection output

The feeder freeze record must contain:

```text
subregion / substation / feeder ID;
source key prefixes and SHA-256 manifests;
state dimension before/after any validated reduction;
retained power buses/lines/loads;
road nodes/links;
retained signal interfaces;
qualified radar sensors;
flood-exposed power components and road links;
all G_P/G_T/G_S/G_H/G_V decisions;
selection code commit;
explicit statement that H1--H5 outcomes were not inspected.
```

Until this record exists, the exact Austin feeder remains `OPEN` and no confirmatory Austin simulation is authorized.
