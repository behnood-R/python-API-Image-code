#!/usr/bin/env python
#
# Copyright (c) Christopher Peisert. All rights reserved.
#
# Copyright Perceive 2019-2022. All rights reserved.
"""Flask app initialization."""

from flask import Flask

from app.blueprints import upload

def configure_flask_app(flask_app: Flask):
    flask_app.config.update(
        DEBUG="False",
        ENV="production",
        MAX_CONTENT_LENGTH=8388608,
        PREFERRED_URL_SCHEME="http"
    )

    flask_app.register_blueprint(upload.upload)
