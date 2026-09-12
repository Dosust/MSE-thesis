"""Deterministic Phase-1 multi-rate event ordering."""
from dataclasses import dataclass
from typing import Any, Iterable, List


EVENT_PRIORITY = {
    "exogenous": 1,
    "information": 2,
    "controller": 3,
    "constituent_solve": 4,
    "restoration": 5,
    "output": 6,
}


@dataclass(frozen=True)
class Event:
    time_min: float
    kind: str
    event_id: str
    payload: Any = None


def sort_events(events: Iterable[Event]) -> List[Event]:
    items = list(events)
    for event in items:
        if event.kind not in EVENT_PRIORITY:
            raise ValueError(f"unknown event kind: {event.kind}")
    return sorted(
        items,
        key=lambda event: (
            event.time_min,
            EVENT_PRIORITY[event.kind],
            event.event_id,
        ),
    )
