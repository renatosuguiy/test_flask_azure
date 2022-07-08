import os
from mysql.connector import connect


def db_connect():

    sql_config = {
        "user": os.getenv("DB_USERNAME"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOSTNAME"),
    }
    try:
        cnx = connect(**sql_config)
        cur = cnx.cursor(buffered=True, dictionary=True)

        return cnx

    except:
        return False


def db_disconnect(cnx):
    cnx.close()
