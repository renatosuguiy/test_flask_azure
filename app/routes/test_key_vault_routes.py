from flask import Blueprint
from app.controllers.azure_key_vault_controller import create_key, retrive_key


bp_key = Blueprint("key", __name__, url_prefix="/key")
bp_key.get("/create_key")(create_key)
bp_key.get("/get_key")(retrive_key)
# bp_test.get("/test_read_files")()
