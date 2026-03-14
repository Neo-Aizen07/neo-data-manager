import sqlite3
from contextlib import contextmanager
def connect_db():
    conn=sqlite3.connect("neo_data.db")
    conn.row_factory=sqlite3.Row
    return conn
def initialise_db(conn):
    conn.execute("""create table if not exists records(username text primary key, id text, last_saved text)""")
    conn.commit()
@contextmanager
def get_db():
    conn = connect_db()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()