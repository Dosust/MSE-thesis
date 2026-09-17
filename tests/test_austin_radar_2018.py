from urllib.parse import parse_qs, urlparse

import pytest

from methods.austin_case.radar_2018 import YEAR, data_page_url, inventory_url


def test_inventory_is_2018_grouped_sensor_query():
    url = inventory_url()
    query = parse_qs(urlparse(url).query)
    assert query["$where"] == [f"year={YEAR}"]
    assert query["$group"] == ["int_id"]
    assert "count(*) as n" in query["$select"][0]


def test_data_query_requires_preselected_sensor_ids():
    with pytest.raises(ValueError, match="at least one"):
        data_page_url([])


def test_data_query_is_2018_and_sensor_scoped():
    url = data_page_url([42, 7, 42], offset=50000)
    query = parse_qs(urlparse(url).query)
    assert query["$where"] == ["year=2018 AND int_id in (7,42)"]
    assert query["$offset"] == ["50000"]
    assert query["$order"] == ["curdatetime,int_id,detid,row_id"]


def test_invalid_paging_fails_closed():
    with pytest.raises(ValueError):
        data_page_url([1], offset=-1)
    with pytest.raises(ValueError):
        data_page_url([1], limit=50001)
