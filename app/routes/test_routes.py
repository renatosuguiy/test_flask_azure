from flask import Blueprint

from app.controllers import list_files_azure, return_name, create_container


bp_test = Blueprint("test", __name__, url_prefix="/test")
bp_test.get("/<name>")(return_name)
bp_test.get("/create_container")(create_container)
bp_test.get("/list_files")(list_files_azure)
# bp_test.get("/test_read_files")()
