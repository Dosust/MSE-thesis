import math

from phase1_exec.information import controller_limit, delay_series
from phase1_exec.organization import energization_guard, restoration_time
from phase1_exec.reproducibility import derive_seed


def test_zero_delay_is_identity():
    values = [1.0, 2.0, 3.0]
    assert delay_series(values, 0) == values


def test_controller_reacts_monotonically_to_forecast_above_reference():
    low = controller_limit(100.0, 40.0, 50.0, 120.0)
    high = controller_limit(100.0, 80.0, 50.0, 120.0)
    assert high <= low


def test_restoration_sum_and_energization_transition():
    t_restore = restoration_time(15.0, 15.0, 20.0, 60.0)
    assert t_restore == 110.0
    assert energization_guard(109.999, t_restore) == 0
    assert energization_guard(110.0, t_restore) == 1


def test_infinite_crew_travel_makes_restoration_infeasible():
    assert restoration_time(15.0, 15.0, math.inf, 60.0) == math.inf


def test_seed_derivation_is_stable_and_identifier_specific():
    first = derive_seed("scenario-A")
    repeated = derive_seed("scenario-A")
    second = derive_seed("scenario-B")
    assert first == repeated
    assert first != second
    assert 0 <= first < 2**64
