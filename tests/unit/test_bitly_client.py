import logging
import pytest
import logging

from shorty.integration.bitly.client import BitlyClient


def test_valid_long_url_response():
    """
    Test that BitlyClient clint returns an expected "long_url" field in the response 
    """
    bitly = BitlyClient("57b72d7bf12efac43052265139d38b87a7652c73")
    res = bitly.short("https://withplum.com/about/")
    assert res.json()["long_url"] == "https://withplum.com/about/"
