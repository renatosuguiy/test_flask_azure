import os

from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv

from app import routes
from app.services.secrets_service import retrive_secret


def create_app():
    load_dotenv()

    app = Flask(__name__)
    routes.init_app(app)

    app.config["MAIL_SERVER"] = "smtp.mailtrap.io"
    app.config["MAIL_PORT"] = 2525
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USE_SSL"] = False

    return app
