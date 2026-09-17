import pytest

from methods.austin_case.selection import FeederSelectionError, select_feeder


def row(feeder, n_state, **gates):
    base = {
        "subregion": "P5U", "substation": "ss0", "feeder": feeder,
        "n_state": n_state,
        "G_P": True, "G_T": True, "G_S": True, "G_H": True, "G_V": True,
    }
    base.update(gates)
    return base


def test_smallest_admissible_feeder_is_selected():
    chosen = select_feeder([row("f1", 100), row("f2", 50)])
    assert chosen["feeder"] == "f2"
    assert chosen["selection_used_hypothesis_results"] is False


def test_failed_gate_excludes_feeder():
    chosen = select_feeder([row("f1", 10, G_H=False), row("f2", 50)])
    assert chosen["feeder"] == "f2"


def test_tie_break_is_lexical_and_deterministic():
    chosen = select_feeder([row("z", 50), row("a", 50)])
    assert chosen["feeder"] == "a"


def test_hypothesis_information_is_forbidden():
    bad = row("f1", 10)
    bad["h1_effect"] = 99.0
    with pytest.raises(FeederSelectionError, match="forbidden"):
        select_feeder([bad])


def test_no_admissible_feeder_fails_closed():
    with pytest.raises(FeederSelectionError, match="no scientifically admissible"):
        select_feeder([row("f1", 10, G_V=False)])
