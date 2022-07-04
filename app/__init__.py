import os
from flask import Flask
from flask_mail import Mail

from app import routes


def create_app():
    app = Flask(__name__)
    routes.init_app(app)

    app.config["MAIL_SERVER"] = "smtp.office365.com"
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USE_SSL"] = False

    return app
