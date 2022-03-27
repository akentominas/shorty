"""
This module illustrates the usage of the bitly client class.
"""
from shorty.integration.bitly.client import BitlyClient

import logging

bitly = BitlyClient('57b72d7bf12efac43052265139d38b87a7652c73')
result = bitly.short('https://pixelcom.gr/')

logging.info(result.json())
