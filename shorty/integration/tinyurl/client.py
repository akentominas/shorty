from urllib import response
import requests
import logging

LOGGER_BASENAME = "tinyurl_client"
logger = logging.getLogger(LOGGER_BASENAME)


class TinyClient():
    """Represents tinyurl API client

    """

    def __init__(self, access_token):
        self.__access_token = access_token

    def short(self, url):
        """Documentation goes here"""
        headers = {
            'content-type': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.__access_token)
        }

        data = {
            'url': url,
            'domain': 'tiny.one'
        }

        response = requests.post(
            'https://api.tinyurl.com/create',
            headers=headers,
            json=data)

        return response
