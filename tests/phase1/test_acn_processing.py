from datetime import date

import pytest

# The repository's generic Python matrix intentionally does not install the
# Phase-1 scientific lock. These tests are authoritative only in the canonical
# Phase-1 environment, where NumPy is hash-locked. Skip collection elsewhere
# rather than silently installing a second scientific environment.
np = pytest.importorskip("numpy")

from phase1_exec.acn_processing import (  # noqa: E402
    ACNProcessingError,
    aggregate_day_power_kw,
    chronological_split,
    day_status,
    parse_aware_timestamp,
    reconstructed_session_energy_kwh,
    session_trace,
)


def _session(
    start="Thu, 10 Oct 2019 07:00:00 GMT",
    end="Thu, 10 Oct 2019 07:10:00 GMT",
    current=10.0,
):
    return {
        "sessionID": "S1",
        "spaceID": "CA-308",
        "siteID": "caltech",
        "timezone": "America/Los_Angeles",
        "connectionTime": start,
        "disconnectTime": end,
        "kWhDelivered": 0.3466666666666667,
        "chargingCurrent": {
            "timestamps": [
                "Thu, 10 Oct 2019 07:00:00 GMT",
                "Thu, 10 Oct 2019 07:05:00 GMT",
                "Thu, 10 Oct 2019 07:10:00 GMT",
            ],
            "current": [current, current, current],
        },
        "pilotSignal": {
            "timestamps": [
                "Thu, 10 Oct 2019 07:00:00 GMT",
                "Thu, 10 Oct 2019 07:05:00 GMT",
                "Thu, 10 Oct 2019 07:10:00 GMT",
            ],
            "pilot": [16.0, 16.0, 16.0],
        },
    }


def test_timestamp_must_be_aware():
    parsed = parse_aware_timestamp("Thu, 10 Oct 2019 07:00:00 GMT")
    assert parsed.utcoffset().total_seconds() == 0
    with pytest.raises(ACNProcessingError):
        parse_aware_timestamp("2019-10-10T07:00:00")


def test_session_energy_reconstruction_constant_current():
    trace = session_trace(_session(), {"CA-308": 208.0})
    # 208 V * 10 A * (10/60 h) = 0.346666... kWh.
    assert reconstructed_session_energy_kwh(trace) == pytest.approx(
        0.3466666666666667, abs=1e-12
    )


def test_5_min_aggregation_is_exact_for_constant_trace():
    trace = session_trace(_session(), {"CA-308": 208.0})
    stamps, p = aggregate_day_power_kw(date(2019, 10, 10), [trace])
    assert len(stamps) == 288
    assert len(p) == 288
    assert p[0] == pytest.approx(2.08, abs=1e-12)
    assert p[1] == pytest.approx(2.08, abs=1e-12)
    assert np.allclose(p[2:], 0.0)


def test_dst_fallback_day_is_excluded_pre_split():
    state = day_status(date(2019, 11, 3))
    assert not state.accepted
    assert state.reason == "DST_NON_24H_DAY:25h"
    with pytest.raises(ACNProcessingError):
        aggregate_day_power_kw(date(2019, 11, 3), [])


def test_chronological_70_30_split_has_no_overlap():
    days = [date(2019, 10, i) for i in range(1, 11)]
    cal, val = chronological_split(days)
    assert len(cal) == 7
    assert len(val) == 3
    assert set(cal).isdisjoint(val)
    assert max(cal) < min(val)


def test_unknown_station_fails_closed():
    with pytest.raises(ACNProcessingError):
        session_trace(_session(), {"OTHER": 208.0})


def test_gap_larger_than_one_exchange_interval_fails_closed():
    s = _session()
    s["chargingCurrent"]["timestamps"] = [
        "Thu, 10 Oct 2019 07:00:00 GMT",
        "Thu, 10 Oct 2019 07:06:00 GMT",
    ]
    s["chargingCurrent"]["current"] = [10.0, 10.0]
    with pytest.raises(ACNProcessingError):
        session_trace(s, {"CA-308": 208.0})
