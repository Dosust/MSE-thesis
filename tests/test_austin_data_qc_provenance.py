import pytest

from methods.austin_case.data_qc import AustinDataQCError, _validate_record


def arcgis_record():
    return {
        "bytes": 1,
        "sha256": "a" * 64,
        "layer": "https://services.example.test/FeatureServer/0",
        "object_id_count": 0,
        "feature_count": 0,
        "page_count": 0,
        "pages": [],
    }


def test_arcgis_layer_endpoint_is_valid_provenance():
    _validate_record("roads", arcgis_record(), None)


def test_missing_source_url_and_layer_is_rejected():
    record = arcgis_record()
    record.pop("layer")
    with pytest.raises(AustinDataQCError, match="source URL/layer endpoint"):
        _validate_record("roads", record, None)
