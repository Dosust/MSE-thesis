# Independent controlled EV charging laboratory audit — measured output

**Source separation:** neither dataset represents the 50-day KIT field deployment.
**Electrical measurement limit:** the PHIL published CSV has U/I RMS per phase, not actual active-power or charger-command columns.

| PHIL EV | Samples | Screened voltage transitions | Median sample time (s) |
|---|---:|---:|---:|
| Volkswagen ID.4 | 8809 | 16 | 0.021 |
| Nissan Leaf | 8810 | 0 | 0.021 |
| MG4 | 8810 | 16 | 0.021 |
| Tesla Model 3 | 8810 | 16 | 0.021 |
| Renault Zoe | 8810 | 16 | 0.021 |

**Exact per-event measured voltage/current changes:** see JSON. Change-point times are voltage-screen estimates and are not verified treatment commands.
**Dortmund measurements in metadata index:** 142
**Dortmund candidate dynamic measurements:** 103
**Dortmund potentially relevant control parameter definitions:** 7 (sample capped at 35; see JSON).

**Evidence verdict:** Controlled PHIL can test voltage/current response under laboratory conditions. Dortmund metadata identifies separate charger-status/setpoint evidence sources. Neither proves the March 2026 field power transitions were controlled by grid voltage. No thermal field validation.
