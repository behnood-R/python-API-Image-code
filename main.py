"""Python application entry point."""

from flask import Flask
from app import app_init
from app.env import PUBLIC_PORT, APP_NAME

LOCALHOST = "127.0.0.1"

app = Flask(APP_NAME)
app_init.configure_flask_app(app)

if __name__ == '__main__':
    # This is used when running locally only. In production, a web-server such as
    # Gunicorn (or other cloud provider infrastructure) will serve the app.
    app.run(host=LOCALHOST, port=PUBLIC_PORT)