import logging
import pytest
import logging

from shorty.integration.tinyurl.client import TinyClient


def test_valid_long_url_response():
    """
    Test that Tine Url clint returns an expected "url" field in the response 
    """
    bitly = TinyClient(
        "oKiRqU18OkR7GhJD55RbRoXgD8VamFRSp5EKhavZz590YA9s2BFIUWufDqxF")
    res = bitly.short("https://withplum.com/about/")
    assert res.json()["data"]["url"] == "https://withplum.com/about/"
