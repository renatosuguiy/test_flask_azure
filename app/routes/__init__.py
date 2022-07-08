from flask import Flask
from app.routes.test_routes import bp_test
from app.routes.test_key_vault_routes import bp_key
from app.routes.db_routes import bp_db


def init_app(app: Flask):

    app.register_blueprint(bp_test)
    app.register_blueprint(bp_key)
    app.register_blueprint(bp_db)
