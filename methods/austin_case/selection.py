"""Deterministic pre-result feeder selection for the Austin case."""
from __future__ import annotations

from typing import Iterable, Mapping, Any


class FeederSelectionError(ValueError):
    pass


REQUIRED_GATES = ("G_P", "G_T", "G_S", "G_H", "G_V")
FORBIDDEN_OUTCOME_KEYS = {
    "h1_effect", "h2_effect", "h3_skill", "h4_effect", "h5_distance",
    "viability_margin", "hypothesis_score", "confirmatory_result"
}


def admissible(row: Mapping[str, Any]) -> bool:
    return all(row.get(gate) is True for gate in REQUIRED_GATES)


def select_feeder(rows: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    candidates = []
    for raw in rows:
        row = dict(raw)
        if FORBIDDEN_OUTCOME_KEYS & set(row):
            raise FeederSelectionError("hypothesis/outcome information is forbidden during case selection")
        for field in ("subregion", "substation", "feeder", "n_state"):
            if field not in row:
                raise FeederSelectionError(f"missing required selection field: {field}")
        if not isinstance(row["n_state"], int) or row["n_state"] <= 0:
            raise FeederSelectionError("n_state must be a positive integer")
        if admissible(row):
            candidates.append(row)
    if not candidates:
        raise FeederSelectionError("no scientifically admissible feeder")
    candidates.sort(
        key=lambda x: (
            x["n_state"], str(x["subregion"]), str(x["substation"]), str(x["feeder"])
        )
    )
    chosen = dict(candidates[0])
    chosen["selection_rule"] = "MIN_STATE_THEN_LEXICAL_ID"
    chosen["selection_used_hypothesis_results"] = False
    return chosen
