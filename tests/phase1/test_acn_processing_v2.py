from datetime import datetime, timezone

import numpy as np
import pytest

from phase1_exec.acn_processing import ACNProcessingError, TimeSeries
from phase1_exec.acn_processing_v2 import (
    V2SessionTrace,
    active_amp_seconds,
    calibrate_global_effective_voltage,
    extract_timeseries_v2,
    reconstructed_active_energy_kwh,
    session_trace_v2,
)


def test_duplicate_equal_timestamp_is_collapsed_by_arithmetic_mean():
    ts = extract_timeseries_v2(
        {
            "timestamps": [
                "2019-10-10T00:00:00+00:00",
                "2019-10-10T00:00:05+00:00",
                "2019-10-10T00:00:05+00:00",
                "2019-10-10T00:00:10+00:00",
            ],
            "current": [0.0, 2.0, 4.0, 6.0],
        },
        "current",
        "chargingCurrent",
    )
    assert len(ts.timestamps) == 3
    assert ts.values == pytest.approx((0.0, 3.0, 6.0))


def test_true_backward_time_remains_rejected():
    with pytest.raises(ACNProcessingError, match="backward time"):
        extract_timeseries_v2(
            {
                "timestamps": [
                    "2019-10-10T00:00:00+00:00",
                    "2019-10-10T00:00:10+00:00",
                    "2019-10-10T00:00:05+00:00",
                ],
                "current": [0.0, 1.0, 2.0],
            },
            "current",
            "chargingCurrent",
        )


def test_gap_threshold_is_not_relaxed_after_duplicate_collapse():
    with pytest.raises(ACNProcessingError, match="gap"):
        extract_timeseries_v2(
            {
                "timestamps": [
                    "2019-10-10T00:00:00+00:00",
                    "2019-10-10T00:00:00+00:00",
                    "2019-10-10T00:06:00+00:00",
                ],
                "current": [1.0, 1.0, 1.0],
            },
            "current",
            "chargingCurrent",
        )


def test_done_charging_time_truncates_active_interval():
    session = {
        "sessionID": "s1",
        "spaceID": "CA-X",
        "connectionTime": "2019-10-10T00:00:00+00:00",
        "doneChargingTime": "2019-10-10T01:00:00+00:00",
        "disconnectTime": "2019-10-10T02:00:00+00:00",
        "kWhDelivered": 2.0,
        "timezone": "America/Los_Angeles",
        "chargingCurrent": {
            "timestamps": [
                "2019-10-10T00:00:00+00:00",
                "2019-10-10T00:05:00+00:00",
                "2019-10-10T01:00:00+00:00",
                "2019-10-10T01:05:00+00:00",
                "2019-10-10T02:00:00+00:00",
            ],
            "current": [10.0, 10.0, 10.0, 1.0, 1.0],
        },
        "pilotSignal": {
            "timestamps": [
                "2019-10-10T00:00:00+00:00",
                "2019-10-10T00:05:00+00:00",
                "2019-10-10T01:00:00+00:00",
                "2019-10-10T01:05:00+00:00",
                "2019-10-10T02:00:00+00:00",
            ],
            "pilot": [10.0, 10.0, 10.0, 0.0, 0.0],
        },
    }
    trace = session_trace_v2(session)
    assert active_amp_seconds(trace) == pytest.approx(10.0 * 3600.0)
    assert reconstructed_active_energy_kwh(trace, 200.0) == pytest.approx(2.0)


def test_global_effective_voltage_is_median_of_session_implied_values():
    base = datetime(2019, 10, 10, tzinfo=timezone.utc)
    end = datetime(2019, 10, 10, 1, tzinfo=timezone.utc)
    current = TimeSeries((base, end), (10.0, 10.0))
    pilot = TimeSeries((base, end), (10.0, 10.0))

    traces = []
    for sid, voltage in [("a", 200.0), ("b", 220.0), ("c", 240.0)]:
        energy = voltage * 10.0 * 3600.0 / (1000.0 * 3600.0)
        traces.append(
            V2SessionTrace(
                session_id=sid,
                station_id="X",
                connection=base,
                disconnect=end,
                active_end=end,
                kwh_delivered=energy,
                current=current,
                pilot=pilot,
            )
        )

    value, count = calibrate_global_effective_voltage(traces)
    assert count == 3
    assert value == pytest.approx(220.0)
