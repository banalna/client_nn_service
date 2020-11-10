# -*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap

from config import Config

bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)

    from app.main import bp as api_bp, prefix_module

    app.register_blueprint(api_bp, url_prefix=prefix_module)

    return app
