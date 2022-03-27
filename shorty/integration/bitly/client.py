from urllib import response
from shorty.config.settings import CONFIG

import requests
import logging

LOGGER_BASENAME = "bitly_client"
logger = logging.getLogger(LOGGER_BASENAME)

bitlyHostname = CONFIG['bitly']['hostname']


class BitlyClient():
    """Represents bitly API client

    """

    def __init__(self, access_token):
        self.__access_token = access_token

    def short(self, url):
        """Documentation goes here"""
        tiny_url_endpoint = "{0}/v4/shorten".format(bitlyHostname)

        headers = {
            'content-type': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.__access_token)
        }

        data = {
            'long_url': url}

        response = requests.post(
            tiny_url_endpoint,
            headers=headers,
            json=data)

        return response
