import math

from phase1_exec.information import controller_limit, delay_series
from phase1_exec.organization import energization_guard, restoration_time
from phase1_exec.reproducibility import derive_seed


def test_zero_delay_is_identity():
    values = [1.0, 2.0, 3.0]
    assert delay_series(values, 0) == values


def test_declared_latency_levels_shift_exact_slots():
    values = list(range(10))
    assert delay_series(values, 1, fill=None)[1:] == values[:-1]
    assert delay_series(values, 3, fill=None)[3:] == values[:-3]
    assert delay_series(values, 6, fill=None)[6:] == values[:-6]


def test_controller_reacts_monotonically_to_forecast_above_reference():
    low = controller_limit(100.0, 40.0, 50.0, 120.0)
    high = controller_limit(100.0, 80.0, 50.0, 120.0)
    assert high <= low


def test_controller_is_always_bounded():
    for margin in (-20.0, 0.0, 50.0, 200.0):
        for forecast in (0.0, 50.0, 500.0):
            value = controller_limit(margin, forecast, 50.0, 120.0)
            assert 0.0 <= value <= 120.0


def test_restoration_sum_and_energization_transition():
    t_restore = restoration_time(15.0, 15.0, 20.0, 60.0)
    assert t_restore == 110.0
    assert energization_guard(109.999, t_restore) == 0
    assert energization_guard(110.0, t_restore) == 1


def test_zero_organizational_delays_reduce_to_crew_time():
    assert restoration_time(0.0, 0.0, 17.5, 0.0) == 17.5


def test_restoration_time_is_monotone_in_each_delay():
    base = restoration_time(10.0, 20.0, 30.0, 40.0)
    assert restoration_time(11.0, 20.0, 30.0, 40.0) >= base
    assert restoration_time(10.0, 21.0, 30.0, 40.0) >= base
    assert restoration_time(10.0, 20.0, 31.0, 40.0) >= base
    assert restoration_time(10.0, 20.0, 30.0, 41.0) >= base


def test_infinite_crew_travel_makes_restoration_infeasible():
    assert restoration_time(15.0, 15.0, math.inf, 60.0) == math.inf


def test_seed_derivation_is_stable_and_identifier_specific():
    first = derive_seed("scenario-A")
    repeated = derive_seed("scenario-A")
    second = derive_seed("scenario-B")
    assert first == repeated
    assert first != second
    assert 0 <= first < 2**64
