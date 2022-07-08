from http import HTTPStatus
from flask import jsonify
from app.services.db_services import db_connect, db_disconnect


def test_db_connection_controller():
    cnx = db_connect()

    if cnx:
        db_disconnect(cnx)

        return "Connection OK"
    return "Connection failed"


def get_one_line_controller():
    cnx = db_connect()
    cur = cnx.cursor(dictionary=True)

    query = """
    select * from test_azure_db.ppc_links
    limit 1;
    """

    cur.execute(query)
    result = cur.fetchall()
    return jsonify(result), HTTPStatus.OK
