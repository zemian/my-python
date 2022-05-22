import sqlite3
from datetime import datetime

DB_FILE = 'db.sqlite3'

def init_db(cur: sqlite3.Cursor):
    cur.executescript('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            event_dt DATETIME NOT NULL,
            name TEXT NOT NULL
        )
    ''')
    print("DB schema is ready.")


def setup_db(cur: sqlite3.Cursor):
    sql = 'INSERT INTO events(event_dt, name) VALUES(:event_dt, :name)'
    for i in range(10):
        cur.execute(sql, {'event_dt': datetime.now(), 'name': f"test_{i}"})
        print(f"Inserted row: ")


def query_db(cur: sqlite3.Cursor):
    event_dt = cur.execute('SELECT event_dt, name FROM events WHERE id = ?', (1,)).fetchone()[0]
    print("event_dt", event_dt, type(event_dt))

with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()
    #init_db(cur)
    #setup_db(cur)
    query_db(cur)
