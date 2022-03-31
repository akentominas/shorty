from urllib import response
from shorty.config.settings import CONFIG

import requests
import logging

LOGGER_BASENAME = "tinyurl_client"
logger = logging.getLogger(LOGGER_BASENAME)

tiny_hostname = CONFIG['tinyurl']['hostname']


class TinyClient():
    """Represents tinyurl API client, holds the endpoint and access_token
    to talk to the TinyURL API.

    Attributes:
        access_token: The token generated from the TinyURL account

    """

    def __init__(self, access_token):
        self.__access_token = access_token

    def short(self, url):
        """Documentation goes here"""

        tiny_url_endpoint = "{0}/create".format(tiny_hostname)

        headers = {
            'content-type': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.__access_token)
        }

        data = {
            'url': url,
            'domain': 'tiny.one'
        }

        response = requests.post(
            tiny_url_endpoint,
            headers=headers,
            json=data)

        return response
