"""Shorty url shortener API

   Attributes:
      shortlinks_api (api namespace): Namespace to hold all resources related to URL shortener
"""
from crypt import methods
import json
import logging
from random import choices
import re
from typing_extensions import Required

from flask import request
from flask_restx import Namespace
from flask_restx import Resource
from flask_restx import fields, reqparse

from shorty.utils.handler import Handler as UrlProviderHandler
from shorty.exceptions.custom_exceptions import (
    BadRequest,
    APIUnauthorizedError,
    APIRequestTooLangeError,
    APIServiceUnavailableError,
    APIGatewayError,
    APIGatewayTimeoutError
)

logger = logging.getLogger()


shortlinks_api = Namespace("shortlinks", description="Short API converter")

shortlinks_data = shortlinks_api.model(
    "Shortlinks Data",
    {
        "url": fields.String(required=True, description="The URL to shorten"),
        "provider": fields.String(required=False, description="The provider to use for shortening", enum=["bitly", "tinyurl"])
    }
)


@shortlinks_api.route("/", methods=['POST'])
class Shortlinks(Resource):
    """Resources for creating short links"""
    @shortlinks_api.response(200, "Shortlink successfully created")
    @shortlinks_api.response(401, "Shortlink is unauthorized to access the providers")
    @shortlinks_api.expect(shortlinks_data, validate=True)
    def post(self, **kwargs):

        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True, location="form")
        parser.add_argument('provider', choices(
            'bitly, tinyurl'), location="form")

        try:
            payload = request.get_json(force=True)
            handler = UrlProviderHandler(payload)
            handler_response = handler.handle_shortener_provider().json()
            resp = {}

            if "id" in handler_response:
                long_url = handler_response["long_url"]
                short_url = handler_response["link"]
                resp = handler.createResponseObject(long_url, short_url)
            elif "data" in handler_response:
                long_url = handler_response["data"]["url"]
                short_url = handler_response["data"]["tiny_url"]
                resp = handler.createResponseObject(long_url, short_url)

            return resp, 200

        except BadRequest as e:
            return str(e), 400
        except APIUnauthorizedError as e:
            return str(e), 401
        except APIRequestTooLangeError as e:
            return str(e), 413
        except APIGatewayError as e:
            return str(e), 502
        except APIServiceUnavailableError as e:
            return str(e), 503
        except APIGatewayTimeoutError as e:
            return str(e), 504
        except Exception as e:
            return {"Unexpected error occurred"}, 500
