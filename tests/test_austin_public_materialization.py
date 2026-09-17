"""Offline verification tests for Austin public-data materialization utilities."""

from __future__ import annotations

import json

import pytest

from methods.austin_case.materialize_public_data import (
    MaterializationError,
    arcgis_ids_url,
    arcgis_query_url,
    bounds,
    chunked,
    json_count,
    parse_arcgis_ids,
    parse_buscoords,
    parse_s3_listing,
    s3_list_url,
    socrata_export_url,
)


def test_s3_listing_parser_and_url_are_deterministic():
    xml = b'''<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Contents><Key>SMART-DS/v1.0/2018/AUS/P5U/scenarios/base_timeseries/opendss/Buscoords.dss</Key></Contents>
  <CommonPrefixes><Prefix>SMART-DS/v1.0/2018/AUS/P5U/scenarios/base_timeseries/opendss/p5uhs0/</Prefix></CommonPrefixes>
</ListBucketResult>'''
    keys, prefixes = parse_s3_listing(xml)
    assert keys == [
        "SMART-DS/v1.0/2018/AUS/P5U/scenarios/base_timeseries/opendss/Buscoords.dss"
    ]
    assert prefixes == [
        "SMART-DS/v1.0/2018/AUS/P5U/scenarios/base_timeseries/opendss/p5uhs0/"
    ]
    url = s3_list_url(
        "SMART-DS/v1.0/2018/AUS/P5U/scenarios/base_timeseries/opendss/",
        delimiter="/",
    )
    assert "list-type=2" in url
    assert "prefix=SMART-DS%2Fv1.0%2F2018%2FAUS%2FP5U%2F" in url
    assert "delimiter=%2F" in url


def test_buscoords_parser_rejects_non_geographic_coordinates():
    payload = b"bus1,-97.75,30.25\nbus2 -97.70 30.30\n"
    rows = parse_buscoords(payload)
    assert rows == [("bus1", -97.75, 30.25), ("bus2", -97.70, 30.30)]
    assert bounds(rows) == (-97.75, 30.25, -97.70, 30.30)

    with pytest.raises(MaterializationError, match="no plausible"):
        parse_buscoords(b"bus1 3000000 10000000\n")


def test_arcgis_id_first_query_and_page_query_are_explicit():
    bbox = (-97.8, 30.2, -97.7, 30.3)
    ids_url = arcgis_ids_url("https://example.org/FeatureServer/0", bbox)
    assert "returnIdsOnly=true" in ids_url
    assert "returnGeometry=false" in ids_url
    assert "inSR=4326" in ids_url

    page_url = arcgis_query_url(
        "https://example.org/FeatureServer/0",
        bbox,
        object_ids=[3, 5, 7],
    )
    assert page_url.startswith("https://example.org/FeatureServer/0/query?")
    assert "geometry=-97.8%2C30.2%2C-97.7%2C30.3" in page_url
    assert "geometryType=esriGeometryEnvelope" in page_url
    assert "inSR=4326" in page_url
    assert "outSR=4326" in page_url
    assert "objectIds=3%2C5%2C7" in page_url
    assert "f=geojson" in page_url


def test_arcgis_id_parser_deduplicates_sorts_and_chunking_is_complete():
    payload = json.dumps(
        {"objectIdFieldName": "OBJECTID", "objectIds": [5, 1, 5, 3, 2, 4]}
    ).encode()
    field, ids = parse_arcgis_ids(payload)
    assert field == "OBJECTID"
    assert ids == [1, 2, 3, 4, 5]
    assert chunked(ids, 2) == [[1, 2], [3, 4], [5]]
    assert [value for page in chunked(ids, 2) for value in page] == ids

    with pytest.raises(ValueError, match="positive"):
        chunked(ids, 0)


def test_arcgis_error_payload_fails_closed():
    with pytest.raises(MaterializationError, match="ArcGIS ID query error"):
        parse_arcgis_ids(json.dumps({"error": {"code": 400}}).encode())


def test_socrata_location_export_uses_public_resource_endpoint():
    assert socrata_export_url("qpuw-8eeb") == (
        "https://data.austintexas.gov/resource/qpuw-8eeb.json?$limit=50000"
    )


def test_json_count_accepts_rows_and_geojson_features():
    assert json_count(json.dumps([{"a": 1}, {"a": 2}]).encode()) == 2
    assert json_count(
        json.dumps({"type": "FeatureCollection", "features": [{}, {}, {}]}).encode()
    ) == 3
    with pytest.raises(MaterializationError, match="recognized"):
        json_count(json.dumps({"not_features": []}).encode())
