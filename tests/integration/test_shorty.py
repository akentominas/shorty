import os
import pytest
import json
import requests

from unittest import mock


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    with mock.patch.dict(os.environ, {"BITLY_TOKEN": "57b72d7bf12efac43052265139d38b87a7652c73"}):
        yield


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("localhost", 8080)


def test_invalid_provider():
    """
    Test the /shortling endpoint , that in case of unsupported provider type
    (bitly, tinyurl) in the post body, the shortlinks API returns a 400 BadRequest
    error and the corresponding message
    """
    url = 'http://localhost:8080/v1/shortlinks'

    headers = {'Content-Type': 'application/json'}

    payload = {'url': "https://apply.workable.com/withplum/", 'provider': 'mama'}

    resp = requests.post(url, headers=headers,
                         data=json.dumps(payload, indent=4))

    assert resp.status_code == 400
    resp_body = resp.json()
    assert resp_body[
        "errors"]["provider"] == "'mama' is not one of ['bitly', 'tinyurl']"
