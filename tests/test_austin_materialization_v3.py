from copy import deepcopy

import methods.austin_case.materialize_public_data_v3 as v3
from methods.austin_case.road_vintage import AUSTIN_CTN_LAYER, TXDOT_2018_LAYER


def base_manifest():
    return {
        "case_id": "AUS-P5U-2018-V1",
        "status": "RAW_MATERIALIZATION_ONLY",
        "scientific_prohibitions": [],
        "objects": {
            "smartds_buscoords": {
                "bbox_wgs84": [-97.9, 30.1, -97.6, 30.4],
            },
            "street_centerline": {
                "layer": "https://city.example/current-streets",
                "feature_count": 4,
            },
        },
    }


def test_v3_assigns_exact_2018_primary_and_current_sensitivities(monkeypatch, tmp_path):
    def fake_v2(root):
        (root / "qa").mkdir(parents=True, exist_ok=True)
        return deepcopy(base_manifest())

    def fake_extra(root, *, name, layer, bbox, where="1=1"):
        return {
            "source_url": layer,
            "feature_count": 3,
            "object_id_count": 3,
            "where": where,
        }

    monkeypatch.setattr(v3.v2, "acquire", fake_v2)
    monkeypatch.setattr(v3, "_acquire_extra_arcgis", fake_extra)

    manifest = v3.acquire(tmp_path)
    primary = manifest["objects"]["txdot_roadway_inventory_2018"]
    ctn = manifest["objects"]["austin_ctn_current"]
    current = manifest["objects"]["street_centerline"]

    assert primary["source_url"] == TXDOT_2018_LAYER
    assert primary["inventory_year"] == 2018
    assert primary["strict_2018_snapshot"] is True
    assert ctn["source_url"] == AUSTIN_CTN_LAYER
    assert ctn["strict_2018_snapshot"] is False
    assert current["road_role"] == "CURRENT_GEOMETRY_SENSITIVITY"
    assert current["strict_2018_snapshot"] is False
    assert (tmp_path / "qa" / "raw_materialization_manifest_v3.json").exists()
