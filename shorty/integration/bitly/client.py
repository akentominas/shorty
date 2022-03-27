from urllib import response
import requests
import logging

LOGGER_BASENAME = "bitly_client"
logger = logging.getLogger(LOGGER_BASENAME)


class BitlyClient():
    """Represents bitly API client

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
            'long_url': url}

        response = requests.post(
            'https://api-ssl.bitly.com/v4/shorten',
            headers=headers,
            json=data)

        return response
