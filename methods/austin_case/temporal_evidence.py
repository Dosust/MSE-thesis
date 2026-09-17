"""Temporal-evidence controls for the Austin 2018 candidate case."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping


class AustinTemporalEvidenceError(ValueError):
    """Raised when current/retrospective evidence is misused as 2018 truth."""


CUTOFF_2018 = datetime(2018, 12, 31, 23, 59, 59, 999000, tzinfo=timezone.utc)


def _parse_date(value: Any) -> datetime | None:
    """Parse common ArcGIS/GeoJSON date encodings to UTC."""
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(float(value) / 1000.0, tz=timezone.utc)
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return None
        if text.isdigit() or (text.startswith("-") and text[1:].isdigit()):
            return datetime.fromtimestamp(int(text) / 1000.0, tz=timezone.utc)
        if text.endswith("Z"):
            text = text[:-1] + "+00:00"
        try:
            dt = datetime.fromisoformat(text)
        except ValueError as exc:
            raise AustinTemporalEvidenceError(f"unparseable date value: {value!r}") from exc
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    raise AustinTemporalEvidenceError(f"unsupported date value type: {type(value).__name__}")


def retrospective_signal_subset(
    feature_collection: Mapping[str, Any],
    *,
    cutoff: datetime = CUTOFF_2018,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Select current signals with documented turn-on dates no later than 2018.

    This is deliberately a retrospective survivor subset, not a reconstructed
    complete historical inventory.
    """
    features = feature_collection.get("features")
    if not isinstance(features, list):
        raise AustinTemporalEvidenceError("signal GeoJSON FeatureCollection required")

    retained: list[Any] = []
    missing = 0
    invalid = 0
    post_cutoff = 0
    for feature in features:
        if not isinstance(feature, Mapping):
            invalid += 1
            continue
        props = feature.get("properties")
        if not isinstance(props, Mapping):
            invalid += 1
            continue
        value = props.get("TURN_ON_DATE")
        if value is None or value == "":
            missing += 1
            continue
        try:
            dt = _parse_date(value)
        except AustinTemporalEvidenceError:
            invalid += 1
            continue
        if dt is None:
            missing += 1
            continue
        if dt <= cutoff:
            retained.append(feature)
        else:
            post_cutoff += 1

    subset = {"type": "FeatureCollection", "features": retained}
    summary = {
        "temporal_role": "RETROSPECTIVE_2018_SUBSET",
        "cutoff_utc": cutoff.isoformat(),
        "source_feature_count": len(features),
        "retained_feature_count": len(retained),
        "missing_turn_on_date": missing,
        "invalid_turn_on_date": invalid,
        "post_2018_turn_on_date": post_cutoff,
        "survivorship_bias": True,
        "complete_2018_inventory": False,
        "allowed_use": "SEMISYNTHETIC_P_TO_T_MAPPING_AND_SENSITIVITY_ONLY",
    }
    return subset, summary


def validate_signal_summary(summary: Mapping[str, Any]) -> None:
    if summary.get("temporal_role") != "RETROSPECTIVE_2018_SUBSET":
        raise AustinTemporalEvidenceError("signal subset temporal role drift")
    if summary.get("survivorship_bias") is not True:
        raise AustinTemporalEvidenceError("signal survivorship limitation must remain explicit")
    if summary.get("complete_2018_inventory") is not False:
        raise AustinTemporalEvidenceError("retrospective signals cannot claim complete 2018 inventory")
    retained = summary.get("retained_feature_count")
    if not isinstance(retained, int) or retained < 0:
        raise AustinTemporalEvidenceError("invalid retrospective signal count")


def flood_semantics_summary(feature_collection: Mapping[str, Any]) -> dict[str, Any]:
    features = feature_collection.get("features")
    if not isinstance(features, list):
        raise AustinTemporalEvidenceError("flood GeoJSON FeatureCollection required")
    missing_zone = 0
    missing_effective = 0
    for feature in features:
        props = feature.get("properties") if isinstance(feature, Mapping) else None
        if not isinstance(props, Mapping):
            missing_zone += 1
            missing_effective += 1
            continue
        if props.get("FLOOD_ZONE") in (None, ""):
            missing_zone += 1
        if props.get("EFFECTIVE_DATE") in (None, ""):
            missing_effective += 1
    return {
        "temporal_role": "STATIC_SCENARIO_SUPPORT",
        "feature_count": len(features),
        "missing_flood_zone": missing_zone,
        "missing_effective_date": missing_effective,
        "event_time_depth_available": False,
        "historical_2018_event_truth": False,
        "common_cause_not_interdependency": True,
    }


def validate_flood_summary(summary: Mapping[str, Any]) -> None:
    if summary.get("temporal_role") != "STATIC_SCENARIO_SUPPORT":
        raise AustinTemporalEvidenceError("flood temporal role drift")
    if summary.get("event_time_depth_available") is not False:
        raise AustinTemporalEvidenceError("static floodplain cannot claim event-time depth")
    if summary.get("historical_2018_event_truth") is not False:
        raise AustinTemporalEvidenceError("current floodplain cannot claim 2018 event truth")
    if summary.get("common_cause_not_interdependency") is not True:
        raise AustinTemporalEvidenceError("flood common-cause distinction must remain explicit")
