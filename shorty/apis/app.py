from sys import prefix
from flask import Flask
from shorty.apis.v1 import shorty


def create_app(settings_overrides=None):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    configure_settings(app, settings_overrides)
    configure_blueprints(app)
    return app


def configure_settings(app, settings_override):
    app.config.update({
        'DEBUG': True,
        'TESTING': False,
    })
    if settings_override:
        app.config.update(settings_override)


def configure_blueprints(app):
    app.register_blueprint(shorty, url_prefix='/v1')
