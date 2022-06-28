from flask import Flask
from app.routes.test_routes import bp_test
from flask import Blueprint


def init_app(app: Flask):

    app.register_blueprint(bp_test)
