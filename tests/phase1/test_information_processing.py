from datetime import date

import pytest

np = pytest.importorskip("numpy")

from phase1_exec.information_processing import (  # noqa: E402
    DailyPower,
    InformationProcessingError,
    SITE_CAP_KW,
    day_type,
    delay_with_na,
    forecast_day,
    loo_calibration_residuals,
    paired_validation_rmse,
    persistence_forecast,
    reference_power_kw,
    seasonal_slot_means,
)


def _day(y, m, d, value):
    return DailyPower(date(y, m, d), tuple([float(value)] * 288))


def test_site_cap_is_frozen_caltech_default():
    assert SITE_CAP_KW == 150.0


def test_day_type_rule():
    assert day_type(date(2019, 10, 11)) == "weekday"  # Friday
    assert day_type(date(2019, 10, 12)) == "weekend"  # Saturday


def test_seasonal_slot_means_known_answer():
    cal = [
        _day(2019, 10, 10, 1.0),  # Thursday
        _day(2019, 10, 11, 3.0),  # Friday
        _day(2019, 10, 12, 10.0),  # Saturday
        _day(2019, 10, 13, 14.0),  # Sunday
    ]
    means = seasonal_slot_means(cal)
    assert np.allclose(means["weekday"], 2.0)
    assert np.allclose(means["weekend"], 12.0)
    assert np.allclose(forecast_day(_day(2019, 10, 14, 99), means), 2.0)


def test_loo_residuals_do_not_use_self():
    cal = [
        _day(2019, 10, 10, 1.0),
        _day(2019, 10, 11, 3.0),
        _day(2019, 10, 12, 10.0),
        _day(2019, 10, 13, 14.0),
    ]
    residuals, index = loo_calibration_residuals(cal)
    assert len(residuals) == 4 * 288
    assert len(index) == len(residuals)
    # weekday: 1 is predicted by 3 => -2; 3 by 1 => +2
    assert np.allclose(residuals[:288], -2.0)
    assert np.allclose(residuals[288:576], 2.0)
    # weekend: 10 by 14 => -4; 14 by 10 => +4
    assert np.allclose(residuals[576:864], -4.0)
    assert np.allclose(residuals[864:], 4.0)


def test_loo_requires_two_days_per_class():
    cal = [
        _day(2019, 10, 10, 1.0),
        _day(2019, 10, 12, 10.0),
        _day(2019, 10, 13, 14.0),
    ]
    with pytest.raises(InformationProcessingError):
        loo_calibration_residuals(cal)


def test_reference_power_is_calibration_median():
    cal = [
        _day(2019, 10, 10, 1.0),
        _day(2019, 10, 11, 3.0),
        _day(2019, 10, 12, 5.0),
    ]
    assert reference_power_kw(cal) == pytest.approx(3.0)


def test_persistence_uses_most_recent_usable_day():
    usable = [
        _day(2019, 10, 10, 1.0),
        _day(2019, 10, 12, 2.0),
        _day(2019, 10, 14, 3.0),
    ]
    source, forecast = persistence_forecast(usable[-1], usable)
    assert source == date(2019, 10, 12)
    assert np.allclose(forecast, 2.0)


def test_paired_validation_rmse_same_support():
    cal = [
        _day(2019, 10, 10, 1.0),
        _day(2019, 10, 11, 1.0),
        _day(2019, 10, 12, 4.0),
        _day(2019, 10, 13, 4.0),
    ]
    val = [_day(2019, 10, 14, 1.0), _day(2019, 10, 15, 1.0)]
    usable = cal + val
    means = seasonal_slot_means(cal)
    slot_rmse, persistence_rmse, used_days = paired_validation_rmse(
        val, usable, means
    )
    assert used_days == 2
    assert slot_rmse == pytest.approx(0.0)
    # Oct 14 persistence comes from Oct 13 (4 kW), Oct 15 from Oct 14 (1 kW).
    assert persistence_rmse > 0.0


def test_delay_operator_has_no_wraparound_and_explicit_na():
    x = [1.0, 2.0, 3.0, 4.0]
    y0 = delay_with_na(x, 0)
    assert np.allclose(y0, x)
    y = delay_with_na(x, 1)
    assert np.isnan(y[0])
    assert np.allclose(y[1:], [1.0, 2.0, 3.0])
    with pytest.raises(InformationProcessingError):
        delay_with_na(x, 2)
