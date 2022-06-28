from flask import Flask
from app.routes.test_routes import bp_test


def init_app(app: Flask):
    app.register_blueprint(bp_test)
