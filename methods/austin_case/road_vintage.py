"""Fail-closed road-vintage controls for the Austin 2018 case."""
from __future__ import annotations

from typing import Any, Mapping

TXDOT_2018_LAYER = (
    "https://services.arcgis.com/KTcxiTD9dsQw4r7Z/ArcGIS/rest/services/"
    "TxDOT_Roadway_Inventory_2018/FeatureServer/0"
)
AUSTIN_CTN_LAYER = (
    "https://maps.austintexas.gov/arcgis/rest/services/Shared/"
    "Transportation_1/MapServer/22"
)
AUSTIN_CURRENT_STREET_LAYER = (
    "https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/"
    "TRANSPORTATION_street_segment/FeatureServer/0"
)
ROAD_VERSION = "V3_TXDOT_2018_PRIMARY_CITY_CURRENT_SENSITIVITY"


class AustinRoadVintageError(ValueError):
    """Raised when road provenance violates the frozen 2018 contract."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AustinRoadVintageError(message)


def _record(objects: Mapping[str, Any], name: str) -> Mapping[str, Any]:
    value = objects.get(name)
    _require(isinstance(value, Mapping), f"missing road-vintage object: {name}")
    return value


def validate_road_vintage_manifest(manifest: Mapping[str, Any]) -> dict[str, Any]:
    """Validate source identity/roles without claiming spatial or topology PASS."""
    _require(manifest.get("case_id") == "AUS-P5U-2018-V1", "unexpected Austin case ID")
    _require(manifest.get("road_version") == ROAD_VERSION, "unexpected road-vintage version")
    objects = manifest.get("objects")
    _require(isinstance(objects, Mapping), "manifest objects required")

    primary = _record(objects, "txdot_roadway_inventory_2018")
    ctn = _record(objects, "austin_ctn_current")
    current = _record(objects, "street_centerline")

    _require(primary.get("source_url") == TXDOT_2018_LAYER, "primary road source must be TxDOT 2018")
    _require(primary.get("inventory_year") == 2018, "primary road inventory year must equal 2018")
    _require(primary.get("road_role") == "PRIMARY_EXACT_2018_ANNUAL_INVENTORY", "invalid primary road role")
    _require(primary.get("strict_2018_snapshot") is True, "primary source must be marked exact annual 2018 inventory")
    _require(isinstance(primary.get("feature_count"), int) and primary["feature_count"] > 0, "primary road layer must be nonempty")
    _require(primary.get("object_id_count") == primary.get("feature_count"), "primary road pagination count mismatch")

    _require(ctn.get("source_url") == AUSTIN_CTN_LAYER, "CTN source mismatch")
    _require(ctn.get("road_role") == "CURRENT_SEMANTIC_TOPOLOGY_SENSITIVITY", "invalid CTN role")
    _require(ctn.get("strict_2018_snapshot") is False, "live CTN must never be labeled exact 2018")

    _require(current.get("road_role") == "CURRENT_GEOMETRY_SENSITIVITY", "current City street role mismatch")
    _require(current.get("strict_2018_snapshot") is False, "current City streets must never be labeled exact 2018")

    return {
        "case_id": manifest["case_id"],
        "road_source_identity": "PASS",
        "primary_inventory_year": 2018,
        "current_sources_labeled_sensitivity": "PASS",
        "spatial_overlap": "NOT_EVALUATED_HERE",
        "topology_qa": "NOT_EVALUATED_HERE",
        "repair_access": "NOT_EVALUATED_HERE",
        "scientific_scope": "ROAD_PROVENANCE_ONLY_NOT_FINAL_ROAD_ADMISSIBILITY",
    }
