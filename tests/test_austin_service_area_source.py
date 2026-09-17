from methods.austin_case.materialize_service_area import CASE_ID, ITEM_ID, SERVICE_AREA_LAYER


def test_service_area_source_identity_is_frozen():
    assert CASE_ID == "AUS-P5U-2018-V1"
    assert ITEM_ID == "fda30e1a33af449fa9e75e28ad36643e"
    assert SERVICE_AREA_LAYER.endswith(
        "UTILITIESCOMMUNICATION_austin_energy_service_area/FeatureServer/0"
    )


def test_service_area_source_is_not_named_as_feeder_topology():
    lower = SERVICE_AREA_LAYER.lower()
    assert "service_area" in lower
    assert "feeder" not in lower
