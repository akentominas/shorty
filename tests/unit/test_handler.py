import pytest
import json
import os

from shorty.utils.handler import Handler
from shorty.exceptions.custom_exceptions import APIUnauthorizedError

payload = {
    "url": "https://withplum.com/about/",
    "provider": "bitly"
}

payload2 = {
    "l": "https://withplum.com/about/",
    "l": "bitly"
}


def test_unauthorized_exception():
    """
    Test that Handler, which is calling BirltyClient or TinyClient
    is raising an 401 Unauthorized error in case that the access tokens
    are wrong or not provided 
    """
    with pytest.raises(APIUnauthorizedError) as e:
        handler = Handler(json.loads(json.dumps(payload)))
        handler.handle_shortener_provider().json()
