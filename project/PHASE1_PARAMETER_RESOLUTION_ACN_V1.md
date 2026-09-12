# Phase 1C — ACN Infrastructure Parameter Resolution v1

![Status](https://img.shields.io/badge/status-PRE--DATA%20RESOLUTION-1A7F37)
![Phase](https://img.shields.io/badge/phase-1C-0969DA)

**Date:** 2026-09-12  
**Purpose:** resolve quantities that `PHASE1_PARAMETER_REGISTER_V1.md` intentionally left pending until the charging-infrastructure executable configuration was frozen.  
**Boundary:** this resolves software/infrastructure constants only; it does not use ACN observations or validation outcomes.

---

## 1. Authority

The canonical ACN package remains

```text
acnportal==0.3.3
```

and the independently inspected upstream source is frozen at

```text
repository = zach401/acnportal
commit     = 14e723b11339e56ca3afd2bf4969f9e4bc8c2623
```

In that source, `caltech_acn()` is declared with defaults

```text
voltage         = 208 V
transformer_cap = 150 kW
```

and the Phase-1 v1 processing pipeline uses the unmodified default constructor.

---

## 2. Resolved EVSE voltage `[E/P]`

For each station `n`, v1 obtains

```math
V_n
```

from the frozen `caltech_acn().voltages` station mapping.

Under the unmodified default Caltech infrastructure:

```math
\boxed{V_n=208\ \mathrm{V}}
```

for the registered EVSEs used by the frozen configuration.

This is not inferred from ACN charging records and is not calibrated.

---

## 3. Resolved site capacity `[E/P]`

The controller parameter previously listed as

```text
bar P_site = PENDING_SOFTWARE/DATA_LOCK
```

is resolved before ACN data access as

```math
\boxed{\bar P_{site}=150\ \mathrm{kW}.}
```

Status:

```text
SOFTWARE_CONFIGURATION_FIXED [E/P]
```

Calibration permission:

```text
NONE
```

This value cannot be changed because a different capacity makes H1/H2 or service outcomes more favorable.

---

## 4. Reproducible implementation

The executable resolution is not a hand-entered universal charging voltage. The processing code calls

```text
caltech_acn().voltages
```

and fails closed if an observed `spaceID` cannot be mapped to a registered station.

Thus the implemented mapping is

```math
\boxed{
spaceID_n
\rightarrow
V_n\text{ from frozen infrastructure}
\rightarrow
P_n(t)=V_nI_n(t)/1000.
}
```

---

## 5. Claim boundary

These quantities describe the frozen ACN-Sim Caltech infrastructure configuration used by the Phase-1 demonstrator. They are not asserted as universal EV-charging values and do not validate the synthetic mapping from Caltech charging demand to IEEE-33 bus 24.

```math
\boxed{
\text{configuration resolution}
\neq
\text{data validation}
\neq
\text{coupled-model validation}.
}
```
