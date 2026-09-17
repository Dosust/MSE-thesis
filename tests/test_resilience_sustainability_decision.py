from __future__ import annotations

import pytest

from methods.decision.resilience_sustainability import (
    DecisionMathError,
    consequence_sign,
    dominates,
    nondominated,
    set_change_distance,
    sustainability_loss,
)


def test_pareto_dominance_and_nondominated_set():
    assert dominates((1.0, 2.0), (1.0, 3.0))
    assert not dominates((1.0, 3.0), (1.0, 2.0))
    obj = {"a": (1.0, 2.0), "b": (1.0, 3.0), "c": (0.5, 4.0)}
    assert nondominated(obj) == frozenset({"a", "c"})


def test_set_change_distance_known_limits():
    assert set_change_distance({"a", "b"}, {"a", "b"}) == pytest.approx(0.0)
    assert set_change_distance({"a"}, {"b"}) == pytest.approx(1.0)
    assert set_change_distance({"a", "b"}, {"b", "c"}) == pytest.approx(2.0 / 3.0)


def test_sustainability_orientation_is_all_loss():
    assert sustainability_loss(10.0, 20.0, 30.0, 40.0) == (-10.0, 20.0, 30.0, 40.0)


def test_consequence_classification():
    assert consequence_sign(0.2, -0.3, 0.1, 0.1) == "SYNERGY"
    assert consequence_sign(0.2, 0.3, 0.1, 0.1) == "TRADE_OFF"
    assert consequence_sign(0.2, 0.05, 0.1, 0.1) == "RESILIENCE_GAIN_SUSTAINABILITY_NEUTRAL_WITHIN_TOL"
    assert consequence_sign(0.05, -0.3, 0.1, 0.1) == "NO_QUALIFIED_RESILIENCE_GAIN"


def test_invalid_dimensions_fail_closed():
    with pytest.raises(DecisionMathError, match="equal dimension"):
        dominates((1.0,), (1.0, 2.0))
    with pytest.raises(DecisionMathError, match="share one dimension"):
        nondominated({"a": (1.0,), "b": (1.0, 2.0)})
    with pytest.raises(DecisionMathError, match="two empty sets"):
        set_change_distance(set(), set())
