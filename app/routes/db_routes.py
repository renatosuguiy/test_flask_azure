from flask import Blueprint

from app.controllers.db_controller import (
    test_db_connection_controller,
    get_one_line_controller,
)

bp_db = Blueprint("db", __name__, url_prefix="/db")
bp_db.get("/test_db")(test_db_connection_controller)
bp_db.get("/get_one_line")(get_one_line_controller)
