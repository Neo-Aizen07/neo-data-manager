import sqlite3
from typing import Generator
from contextlib import contextmanager
def connect_db()->sqlite3.Connection:
    conn=sqlite3.connect("neo_data.db")
    conn.row_factory=sqlite3.Row
    return conn
def initialise_db(conn : sqlite3.Connection)->None:
    conn.execute("""create table if not exists records(username text primary key not null, id text unique not null , last_saved text not null)""")
    conn.commit()
@contextmanager
def get_db()-> Generator[sqlite3.Connection, None, None]:
    conn = connect_db()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()