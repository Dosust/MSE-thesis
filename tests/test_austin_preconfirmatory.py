"""Regression tests for Austin preconfirmatory scientific controls."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from methods.austin_case.preconfirmatory import (
    PreconfirmatoryRegistryError,
    validate_registry,
)

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "config" / "austin_preconfirmatory_registry_v1.json"


def _registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_repository_registry_passes_control_validation():
    validate_registry(_registry())


def test_common_cause_cannot_be_promoted_to_interdependency():
    data = _registry()
    data["common_cause_pathways"][0]["is_interdependency"] = True
    with pytest.raises(PreconfirmatoryRegistryError, match="must not be labeled"):
        validate_registry(data)


def test_empirical_parameter_cannot_be_prefilled_without_evidence_gate():
    data = _registry()
    data["parameter_registry"][0]["range"] = [0.0, 100.0]
    with pytest.raises(PreconfirmatoryRegistryError, match="range cannot be prefilled"):
        validate_registry(data)


def test_probability_law_cannot_be_invented():
    data = _registry()
    data["uncertainty_registry"][0]["probability_law"] = "normal(0,1)"
    with pytest.raises(PreconfirmatoryRegistryError, match="probability law frozen"):
        validate_registry(data)


def test_hypothesis_threshold_cannot_be_postfilled_before_provenance():
    data = _registry()
    data["preregistration"]["H3"]["delta"] = 0.05
    with pytest.raises(PreconfirmatoryRegistryError, match="materiality threshold must remain open"):
        validate_registry(data)


def test_mechanism_direction_is_fail_closed():
    data = _registry()
    data["interdependencies"][0]["direction"] = "T->P"
    with pytest.raises(PreconfirmatoryRegistryError, match="must be P->T"):
        validate_registry(data)
