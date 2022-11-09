from db.Postgres import Postgres
from datetime import datetime, timezone


def add_new(user_id, path: str, description: str):
    sql = "INSERT into reports (created_by, document_name, description, creation_date)" \
          " values (%s, %s, %s, NOW())"
    with Postgres() as db_conn:
        db_conn.execute(sql, (user_id,
                              path,
                              description,))
