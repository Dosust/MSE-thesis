from methods.austin_case.materialize_public_data_v2 import (
    CURRENT_FULL_WHERE,
    CURRENT_JURISDICTION_LAYER,
    PRIMARY_BOUNDARY_LAYER,
    PRIMARY_ITEM_ID,
)


def test_primary_boundary_is_explicit_full_purpose_2019_source():
    assert PRIMARY_BOUNDARY_LAYER.endswith(
        "City_of_Austin_full_purpose_boundary/FeatureServer/0"
    )
    assert PRIMARY_ITEM_ID == "46a37551e8b64f098f29a2f991df5e9d"


def test_current_boundary_is_sensitivity_only_full_class_query():
    assert CURRENT_JURISDICTION_LAYER.endswith(
        "BOUNDARIES_jurisdictions/FeatureServer/0"
    )
    assert CURRENT_FULL_WHERE == "JURISDICTION_TYPE='FULL'"


def test_primary_and_current_sources_are_not_same_endpoint():
    assert PRIMARY_BOUNDARY_LAYER != CURRENT_JURISDICTION_LAYER
