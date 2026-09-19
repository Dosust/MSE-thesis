# Austin May 28–29, 2025 Microburst — Event Replay Candidate

**Status:** CANDIDATE / ADMISSIBILITY AUDIT REQUIRED  
**Scientific role:** external operational/event/organizational validation candidate.

## Why this event is promising

Identified evidence streams include:
- NWS/NOAA observed severe-weather forcing;
- Austin Energy outage/restoration reporting;
- Austin Energy after-action/follow-up organizational response evidence;
- Austin traffic/incident/open-data sources;
- Austin TPW emergency-response and mobility-management documentation.

## Required event gate

```math
G_{event}
=
G_{hazard}
\land
G_P
\land
G_T
\land
G_{time-align}.
```

For a full P–T event replay, all four components must PASS.

If synchronized transportation evidence is insufficient:

```math
\boxed{G_{event}=BLOCKED}
```

The missing transportation trajectory must **not** be invented.

## Candidate event object

```math
\omega^*
=
[
\eta(t),
P(t),
T(t),
EV(t),
I(t),
O(t),
Q(t)
].
```

## Next admissibility tasks

1. Freeze event timezone and analysis window.
2. Retrieve NWS/NCEI forcing with spatial support metadata.
3. Retrieve Austin Energy event/restoration records and exact temporal coverage.
4. Retrieve historical Austin transportation incidents/signals/road-condition evidence for the same window.
5. Determine whether EV charging evidence exists for the event window.
6. Build source-by-source reality/authority/role classification.
7. Create synchronization manifest.
8. Separate calibration from independent validation use.
