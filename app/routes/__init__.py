from flask import Flask
from app.routes.test_routes import bp_test
from app.routes.test_key_vault_routes import bp_key
from flask import Blueprint


def init_app(app: Flask):

    app.register_blueprint(bp_test)
    app.register_blueprint(bp_key)
