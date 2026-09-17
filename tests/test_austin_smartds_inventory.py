from urllib.parse import parse_qs, urlparse

import pytest

from methods.austin_case.smartds_inventory import list_all, list_url, parse_page


def s3_xml(keys=(), prefixes=(), truncated=False, token=None):
    contents = "".join(f"<Contents><Key>{k}</Key></Contents>" for k in keys)
    prefs = "".join(f"<CommonPrefixes><Prefix>{p}</Prefix></CommonPrefixes>" for p in prefixes)
    tok = f"<NextContinuationToken>{token}</NextContinuationToken>" if token else ""
    return (
        '<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">'
        f"{contents}{prefs}<IsTruncated>{str(truncated).lower()}</IsTruncated>{tok}"
        "</ListBucketResult>"
    ).encode()


def test_parse_nontruncated_page():
    page = parse_page(s3_xml(keys=["a"], prefixes=["p/"]))
    assert page.keys == ("a",)
    assert page.prefixes == ("p/",)
    assert page.truncated is False
    assert page.next_token is None


def test_truncated_page_requires_token():
    with pytest.raises(ValueError, match="continuation token"):
        parse_page(s3_xml(truncated=True))


def test_list_url_preserves_continuation_token_and_delimiter():
    url = list_url("root/", delimiter="/", token="abc")
    q = parse_qs(urlparse(url).query)
    assert q["prefix"] == ["root/"]
    assert q["delimiter"] == ["/"]
    assert q["continuation-token"] == ["abc"]


def test_list_all_follows_pagination_and_deduplicates():
    calls = []
    def fake(url):
        calls.append(url)
        q = parse_qs(urlparse(url).query)
        if "continuation-token" not in q:
            return s3_xml(keys=["b", "a"], prefixes=["x/"], truncated=True, token="next")
        return s3_xml(keys=["c", "a"], prefixes=["y/", "x/"])
    keys, prefixes = list_all("root/", delimiter="/", fetcher=fake)
    assert keys == ("a", "b", "c")
    assert prefixes == ("x/", "y/")
    assert len(calls) == 2


def test_page_token_is_frozen_only_when_truncated():
    page = parse_page(s3_xml(keys=["a"], truncated=False, token="unused"))
    assert page.truncated is False
    assert page.next_token == "unused"
