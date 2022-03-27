from flask import Blueprint, jsonify
from shorty.config.settings import CONFIG

import logging

env = CONFIG["environment"]

api = Blueprint('api', __name__)


@api.route('/')
def index():
    logging.critical("haha {0}".format(env))
    return "My root"


@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    return jsonify({})
