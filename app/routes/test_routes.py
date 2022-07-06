from flask import Blueprint

from app.controllers import (
    list_files_azure,
    return_name,
    create_container,
)
from app.controllers.email_controller import send_email
from app.controllers.flask_mail_controller import flask_email, mail_graph


bp_test = Blueprint("test", __name__, url_prefix="/test")
bp_test.get("/<name>")(return_name)
bp_test.get("/create_container")(create_container)
bp_test.get("/list_files")(list_files_azure)
bp_test.get("/send_mail")(send_email)
bp_test.get("/send_mail_flask")(flask_email)
bp_test.get("/graph")(mail_graph)
# bp_test.get("/test_read_files")()
