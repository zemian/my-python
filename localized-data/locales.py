import sqlite3
import locale, re

DB_FILE = 'localetz.db'

def get_locales():
    locales = []
    for name in locale.locale_alias.values():
        # The "(?:){0,1}" pattern is for non-capturing group
        m = re.match('(\w+?)(?:_(\w\w)){0,1}\.([\w-]+)(?:@(\w+)){0,1}', name)
        if m:
            record = dict(zip(('lang', 'country', 'encoding', 'script'), m.groups()))
            locales.append(record)
    return locales


def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.executescript('''
        CREATE TABLE IF NOT EXISTS locales(
            id INTEGER PRIMARY KEY,
            lang TEXT NOT NULL,
            country TEXT NULL,
            encoding TEXT,
            script TEXT
        )
        ''')


def populate_db():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        for record in get_locales():
            cur.execute('''
            INSERT INTO locales(lang, country, encoding, script)
            VALUES(:lang, :country, :encoding, :script)
            ''', record)

init_db()
populate_db()
print("db created")
