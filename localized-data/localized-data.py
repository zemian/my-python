import sqlite3
import locale, re
import pycountry

DB_FILE = 'localized-data.sqlite3'

def get_locales():
    locales = []
    for name in locale.locale_alias.values():
        # The "(?:){0,1}" pattern is for non-capturing group
        m = re.match('(\w+?)(?:_(\w\w)){0,1}\.([\w-]+)(?:@(\w+)){0,1}', name)
        if m:
            record = dict(zip(('lang', 'country', 'encoding', 'script'), m.groups()))
            locales.append(record)
    return locales


def create_locales_table():
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
    print("Locales table is ready")


def insert_locales():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        locales = get_locales()
        for record in locales:
            cur.execute('''
            INSERT INTO locales(lang, country, encoding, script)
            VALUES(:lang, :country, :encoding, :script)
            ''', record)
    print(f"Inserted {len(locales)} locales")


def create_country_tables():
    with sqlite3.connect(DB_FILE) as conn:
        conn.executescript('''
        CREATE TABLE countries(code TEXT primary key, long_code TEXT, name TEXT, official_name TEXT, common_name TEXT, flag TEXT);
        CREATE TABLE languages(code TEXT primary key, name TEXT);
        CREATE TABLE currencies(code TEXT primary key, name TEXT);
        CREATE TABLE scripts(code TEXT primary key, name TEXT);
        ''')
    print("Country tables are ready")


def insert_country_tables():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()

        for country in pycountry.countries:
            row = {'code': country.alpha_2,
                   'long_code': country.alpha_3,
                   'name': country.name,
                   'official_name': getattr(country, 'official_name', None),
                   'common_name': getattr(country, 'common_name', None),
                   'flag': getattr(country, 'flag', None)
                   }
            cur.execute('''
            INSERT INTO countries(code, long_code, name, official_name, common_name, flag)
            VALUES(:code, :long_code, :name, :official_name, :common_name, :flag)
            ''', row)
        print(f"Inserted {len(pycountry.countries)} countries")  # Inserted 249 countries

        for language in pycountry.languages:
            row = {'code': language.alpha_3, 'name': language.name}
            cur.execute('''INSERT INTO languages(code, name) VALUES(:code, :name)''', row)
        print(f"Inserted {len(pycountry.languages)} languages")  # Inserted 7847 languages

        for script in pycountry.scripts:
            row = {'code': script.alpha_4, 'name': script.name}
            cur.execute('''INSERT INTO scripts(code, name) VALUES(:code, :name)''', row)
        print(f"Inserted {len(pycountry.scripts)} scripts")  # Inserted 182 scripts

        for currency in pycountry.currencies:
            row = {'code': currency.alpha_3, 'name': currency.name}
            cur.execute('''INSERT INTO scripts(code, name) VALUES(:code, :name)''', row)
        print(f"Inserted {len(pycountry.currencies)} currencies")  # Inserted 170 currencies

def main():
    create_locales_table()
    insert_locales()
    create_country_tables()
    insert_country_tables()


main()
