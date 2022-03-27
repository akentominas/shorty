"""
This module illustrates the usage of the tinyurl client class.
"""
from shorty.integration.tinyurl.client import TinyClient

import logging

bitly = TinyClient(
    'mskKRjTJO7Qne8Ztwydy52CsNBuKQPwQJvMggiKMizkffM4IgO3hYIEMFTEK')
result = bitly.short('https://pixelcom.gr/')

logging.info(result.json())
