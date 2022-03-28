"""Shorty url shortener API

   Attributes:
      shortlinks_api (api namespace): Namespace to hold all resources related to URL shortener
"""
import logging
from typing_extensions import Required

from flask import request
from flask_restx import Namespace
from flask_restx import Resource
from flask_restx import fields

logger = logging.getLogger()

shortlinks_api = Namespace("shortlinks", description="Short API converter")

shortlinks_data = shortlinks_api.model(
    "Shortlinks Data",
    {
        "url": fields.String(required=True, description="The URL to shorten"),
        "provider": fields.String(required=False, description="The provider to use for shortening")
    }
)


@shortlinks_api.route("/")
class Shortlinks(Resource):
    """Resources for creating short links"""
    @shortlinks_api.response(200, "Shortlink successfully created")
    def post(self, **kwargs):
        try:
            logger.critical("from shortlink api")
            return "Sucess", 200
        except Exception:
            logger.critical("Error in shortlinks api namespace")
            return {"error": "Errorrrr"}, 500
