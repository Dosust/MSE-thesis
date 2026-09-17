"""Verification tests for the H3 finite-state reference DP instrument."""

from methods.h3.reference_dp import (
    confidence_set,
    finite_horizon_reach_avoid,
    finite_horizon_viability,
)


STATES = (-2, -1, 0, 1, 2)


def deterministic_transition(x, u):
    x_next = max(min(x + u, 2), -2)
    return {x_next: 1.0}


def noisy_transition(x, u):
    intended = max(min(x + u, 2), -2)
    drift = max(min(intended + 1, 2), -2)
    if drift == intended:
        return {intended: 1.0}
    return {intended: 0.8, drift: 0.2}


def actions_full(_x):
    return (-1, 0, 1)


def actions_restricted(_x):
    return (0,)


def safe(x):
    return -1 <= x <= 1


def target(x):
    return x == 0


def avoid(x):
    return abs(x) == 2


def test_probability_bounds():
    v = finite_horizon_viability(STATES, actions_full, noisy_transition, safe, 5)
    r = finite_horizon_reach_avoid(STATES, actions_full, noisy_transition, target, avoid, 5)
    for result in (v, r):
        for horizon_values in result.values:
            assert all(0.0 <= p <= 1.0 for p in horizon_values.values())


def test_confidence_threshold_nesting():
    v = finite_horizon_viability(STATES, actions_full, noisy_transition, safe, 4)
    low = confidence_set(v, 4, 0.5)
    high = confidence_set(v, 4, 0.9)
    assert high <= low


def test_viability_horizon_nesting():
    v = finite_horizon_viability(STATES, actions_full, noisy_transition, safe, 5)
    for h_short in range(5):
        short = confidence_set(v, h_short, 0.75)
        long = confidence_set(v, h_short + 1, 0.75)
        assert long <= short


def test_recovery_horizon_monotonicity():
    r = finite_horizon_reach_avoid(STATES, actions_full, deterministic_transition, target, avoid, 4)
    for h_short in range(4):
        short = confidence_set(r, h_short, 1.0)
        long = confidence_set(r, h_short + 1, 1.0)
        assert short <= long


def test_control_authority_cannot_reduce_optimal_viability():
    restricted = finite_horizon_viability(
        STATES, actions_restricted, noisy_transition, safe, 4
    )
    full = finite_horizon_viability(STATES, actions_full, noisy_transition, safe, 4)
    for x in STATES:
        assert full.at(4, x) >= restricted.at(4, x)


def test_control_authority_cannot_reduce_optimal_recovery():
    restricted = finite_horizon_reach_avoid(
        STATES, actions_restricted, deterministic_transition, target, avoid, 4
    )
    full = finite_horizon_reach_avoid(
        STATES, actions_full, deterministic_transition, target, avoid, 4
    )
    for x in STATES:
        assert full.at(4, x) >= restricted.at(4, x)


def test_deterministic_viability_known_solution():
    v = finite_horizon_viability(STATES, actions_full, deterministic_transition, safe, 5)
    assert confidence_set(v, 5, 1.0) == frozenset({-1, 0, 1})


def test_reach_avoid_known_solution():
    r = finite_horizon_reach_avoid(STATES, actions_full, deterministic_transition, target, avoid, 2)
    # +/-1 can reach 0 in one step; +/-2 are prohibited avoid states.
    assert confidence_set(r, 2, 1.0) == frozenset({-1, 0, 1})


def test_invalid_transition_probability_is_rejected():
    def invalid_transition(_x, _u):
        return {0: 0.7, 1: 0.7}

    try:
        finite_horizon_viability(STATES, actions_full, invalid_transition, safe, 1)
    except ValueError as exc:
        assert "sum to one" in str(exc)
    else:
        raise AssertionError("invalid transition probabilities must fail verification")


def test_target_avoid_overlap_is_rejected():
    try:
        finite_horizon_reach_avoid(
            STATES,
            actions_full,
            deterministic_transition,
            target=lambda x: x == 0,
            avoid=lambda x: x == 0,
            max_horizon=2,
        )
    except ValueError as exc:
        assert "disjoint" in str(exc)
    else:
        raise AssertionError("overlapping target/avoid sets must fail verification")
