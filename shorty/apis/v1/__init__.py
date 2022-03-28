from flask import Blueprint
from importlib_metadata import version
from flask_restx import Api

from shorty.apis.v1.shortlinks import shortlinks_api

shorty = Blueprint('shorty', __name__)
api = Api(shorty,
          title='URL shortener API service',
          version='1.0',
          doc='/'
          )

api.add_namespace(shortlinks_api, path='/shortlinks')
