"""Documentation goes here

"""
from cgitb import reset
import logging
import json

from shorty.constants.shortlinks import BITLY_URL_PROVIDER, TINY_URL_PROVIDER, PROVIDER
from shorty.integration.bitly.client import BitlyClient
from shorty.integration.tinyurl.client import TinyClient
from shorty.config.settings import CONFIG
from shorty.constants.errors import ERROR_CODES
from flask import jsonify, request

logger = logging.getLogger()

bitly_token = CONFIG['bitly']['access_token']
tiny_token = CONFIG['tinyurl']['access_token']


class Handler():

    def __init__(self, payload):
        self.payload = payload
        self.url = payload['url']

    def handle_shortener_provider(self):

        payload = request.get_json(force=True)

        if PROVIDER in payload and payload[PROVIDER] == BITLY_URL_PROVIDER:
            response = self.optionA()
            if response.status_code != 200:
                error_message = 'Error: {0}'.format(response.json())

                raise ERROR_CODES[response.status_code](error_message)
            return response

        elif PROVIDER in payload and payload[PROVIDER] == TINY_URL_PROVIDER:
            response = self.optionB()
            if response.status_code != 200:
                error_message = 'Error: {0}'.format(response.json())
                raise ERROR_CODES[response.status_code](error_message)
            return response

        else:
            response = self.optionA()
            if response.status_code != 200:
                error_message = 'Error: {0}'.format(response.json())
                raise ERROR_CODES[response.status_code](error_message)
            return response

    def optionA(self):
        bitly_client = BitlyClient(bitly_token)

        response = bitly_client.short(self.url)

        if response.status_code != 200:
            tiny_client = TinyClient(tiny_token)
            response = tiny_client.short(self.url)
            return response
        return response

    def optionB(self):
        tiny_client = TinyClient(tiny_token)
        response = tiny_client.short(self.url)

        if response.status_code != 200:
            bitly_client = BitlyClient(bitly_token)
            response = bitly_client.short(self.url)
            return response
        return response

    def createResponseObject(self, long_url, short_url):

        response = {"url": long_url, "link": short_url}
        return response
