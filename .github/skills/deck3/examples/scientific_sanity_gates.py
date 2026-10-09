#!/usr/bin/env python3
"""Conservative synthetic sanity probes for Deck3 scientific-review workflows.

These pure checks detect elementary category mistakes; they do NOT validate
actual equipment physics, causal coupling, field data, literature or PowerPoint.
"""
from __future__ import annotations

from math import isfinite

MATCHED_KEYS = ("heat_case", "asset_case", "controls_case",
                "initial_state_case", "service_requirement", "time_horizon")


def charger_input_balance(ac_kw, dc_kw, auxiliary_kw, storage_rate_kw=0.0):
    """Import-only power balance with declared common measurement boundary.

    storage_rate_kw represents dE_internal/dt (energy per unit time, kW), positive when stored internal energy accumulates. It is NOT kW per second.
    The remaining nonnegative residual is other conversion/operational losses.
    Synthetic test aid, NOT a charger model or verified performance.
    """
    values = (ac_kw, dc_kw, auxiliary_kw, storage_rate_kw)
    if not all(isinstance(v, (int, float)) and isfinite(v) for v in values):
        raise ValueError("finite numeric quantities required")
    if ac_kw < 0 or dc_kw < 0 or auxiliary_kw < 0:
        raise ValueError("import-only case requires nonnegative port powers")
    other_loss = ac_kw - dc_kw - auxiliary_kw - storage_rate_kw
    if other_loss < -1e-8:
        raise ValueError("energy accounting inconsistent with assumed ports")
    return {"total_non_dc_kw": ac_kw - dc_kw,
            "auxiliary_kw": auxiliary_kw,
            "internal_storage_rate_kw": storage_rate_kw,
            "other_loss_kw": max(0.0, other_loss),
            "science_status": "SYNTHETIC_ACCOUNTING_ONLY"}


def directional_admission_requirements(direction, evidence):
    """Structural completeness of proposed mechanism; never certifies it."""
    common = ("thermal_state", "thermal_control_law", "ac_interface_quantity",
              "ac_interface_unit", "source_locator", "receiving_effect")
    if direction == "P_TO_TE":
        required = common + ("permissible_supply_rule", "charging_capability")
    elif direction == "TE_TO_P":
        required = common + ("grid_side_ac_observation", "power_thermal_law")
    else:
        raise ValueError("unknown direction")
    missing = [k for k in required if not evidence.get(k)]
    return {"direction": direction, "missing": missing,
            "status": "CANDIDATE_OPEN" if missing else
            "STRUCTURAL_REVIEW_READY_NOT_PHYSICS_VALIDATED"}


def causal_event_delay(source_time, receiver_time, causal_interface_admitted):
    """Unknown/unobserved causal delay is NONE, never a guessed zero."""
    if source_time is None or receiver_time is None or not causal_interface_admitted:
        return None
    if not all(isinstance(t, (int, float)) and isfinite(t)
               for t in (source_time, receiver_time)):
        raise ValueError("nonfinite or invalid event time")
    delta = receiver_time - source_time
    if delta < 0:
        raise ValueError("receiver event precedes hypothesized source event")
    return delta


def comparator_matched(left, right):
    """Simple equality gate; equality alone is not causal identification."""
    missing = [k for k in MATCHED_KEYS if k not in left or k not in right]
    unequal = [k for k in MATCHED_KEYS if k in left and k in right
               and left[k] != right[k]]
    return {"matched": not missing and not unequal,
            "missing": missing, "unequal": unequal,
            "status": "MATCHED_METADATA_ONLY_NOT_CAUSAL_PROOF"}


def approval_from_raster_only(png_exists, visually_reviewed=False,
                              mechanism_reviewed=False):
    """Never certify scientific figures from PNG existence or dimensions."""
    if not png_exists:
        return "ASSET_MISSING"
    if not visually_reviewed or not mechanism_reviewed:
        return "ARTWORK_PROVISIONAL"
    return "HUMAN_REVIEW_RECORDED_NOT_FIELD_VALIDATION"
