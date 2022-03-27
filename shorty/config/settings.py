"""Config settings for Shorty

   Attributes:
     CONFIG(dict): Dictionary of constants arguments taken from the environment variables
"""
import os

from pathlib import PurePath

CONFIG = {
    "environment": os.environ.get("SHORTY_DEPLOYMENT_ENVIRONMENT", "prod"),
    "bitly": {
        "hostname": os.environ.get("BITLY_ENDPOINT", "https://api-ssl.bitly.com"),
        "access_token": os.environ.get("BITLY_TOKEN", "")
    },
    "tinyurl": {
        "hostname": os.environ.get("TINY_ENDPOINT", "https://api.tinyurl.com"),
        "access_token":  os.environ.get("TINY_TOKEN", "")
    },
}
