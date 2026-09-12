from phase1_exec.coupling import charging_availability, inject_charging_load
from phase1_exec.events import Event, sort_events


def test_zero_charging_recovers_base_load_exactly():
    base = {24: 0.420, 25: 0.420}
    assert inject_charging_load(base, 0.0, bus=24) == base


def test_charging_load_is_injected_only_at_declared_bus():
    base = {23: 0.090, 24: 0.420, 25: 0.420}
    coupled = inject_charging_load(base, 0.050, bus=24)
    assert coupled[24] == 0.470
    assert coupled[23] == base[23]
    assert coupled[25] == base[25]


def test_power_to_transport_availability_map_is_exact_binary_guard():
    assert charging_availability(True) == 1
    assert charging_availability(False) == 0


def test_equal_time_events_follow_preregistered_priority_not_input_order():
    events = [
        Event(60.0, "output", "z"),
        Event(60.0, "restoration", "r"),
        Event(60.0, "controller", "c"),
        Event(60.0, "exogenous", "x"),
        Event(60.0, "constituent_solve", "s"),
        Event(60.0, "information", "i"),
    ]
    ordered = sort_events(reversed(events))
    assert [event.kind for event in ordered] == [
        "exogenous",
        "information",
        "controller",
        "constituent_solve",
        "restoration",
        "output",
    ]
