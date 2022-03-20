import sqlite3
import locale
import re
import pycountry
import us
import pytz
from datetime import datetime, timezone

def get_conn():
    return sqlite3.connect('localized-data.sqlite3')


def get_locales():
    locales = []
    for name in locale.locale_alias.values():
        # The "(?:){0,1}" pattern is for non-capturing group
        m = re.match('(\w+?)(?:_(\w\w)){0,1}\.([\w-]+)(?:@(\w+)){0,1}', name)
        if m:
            record = dict(zip(('lang', 'country', 'encoding', 'script'), m.groups()))
            locales.append(record)
    return locales


def create_locales_table(conn):
    cur = conn.cursor()
    cur.executescript('''
    CREATE TABLE locales(
        id INTEGER PRIMARY KEY,
        lang TEXT NOT NULL,
        country TEXT NULL,
        encoding TEXT,
        script TEXT
    )
    ''')
    print("Locales table is ready")


def insert_locales(conn, sql=None):
    cur = conn.cursor()
    locales = get_locales()
    if not sql:
        sql = '''
        INSERT INTO locales(lang, country, encoding, script)
        VALUES(:lang, :country, :encoding, :script)
        '''
    for record in locales:
        cur.execute(sql, record)
    print(f"Inserted {len(locales)} locales")


def create_country_tables(conn):
    conn.executescript('''
    CREATE TABLE countries(id INTEGER PRIMARY KEY, code TEXT, long_code TEXT, name TEXT, official_name TEXT, common_name TEXT, flag TEXT);
    CREATE TABLE languages(id INTEGER PRIMARY KEY, code TEXT, long_code TEXT, name TEXT);
    CREATE TABLE currencies(id INTEGER PRIMARY KEY, code TEXT, name TEXT);
    CREATE TABLE scripts(id INTEGER PRIMARY KEY, code TEXT, name TEXT);
    ''')
    print("Country tables are ready")


def insert_country_tables(conn, countries_sql=None, languages_sql=None, scripts_sql=None, currencies_sql=None):
    cur = conn.cursor()
    if not countries_sql:
        countries_sql = '''
        INSERT INTO countries(code, long_code, name, official_name, common_name, flag)
        VALUES(:code, :long_code, :name, :official_name, :common_name, :flag)
        '''
    if not languages_sql:
        languages_sql = '''INSERT INTO languages(code, long_code, name) VALUES(:code, :long_code, :name)'''
    if not scripts_sql:
        scripts_sql = '''INSERT INTO scripts(code, name) VALUES(:code, :name)'''
    if not currencies_sql:
        currencies_sql = '''INSERT INTO currencies(code, name) VALUES(:code, :name)'''

    for country in pycountry.countries:
        row = {'code': country.alpha_2,
               'long_code': country.alpha_3,
               'name': country.name,
               'official_name': getattr(country, 'official_name', None),
               'common_name': getattr(country, 'common_name', None),
               'flag': getattr(country, 'flag', None)
               }
        cur.execute(countries_sql, row)
    print(f"Inserted {len(pycountry.countries)} countries")  # Inserted 249 countries

    for language in pycountry.languages:
        row = {
            'code': getattr(language, 'alpha_2', None),
            'long_code': getattr(language, 'alpha_3', None),
            'name': language.name
        }
        cur.execute(languages_sql, row)
    print(f"Inserted {len(pycountry.languages)} languages")  # Inserted 7847 languages

    for script in pycountry.scripts:
        row = {'code': script.alpha_4, 'name': script.name}
        cur.execute(scripts_sql, row)
    print(f"Inserted {len(pycountry.scripts)} scripts")  # Inserted 182 scripts

    for currency in pycountry.currencies:
        row = {'code': currency.alpha_3, 'name': currency.name}
        cur.execute(currencies_sql, row)
    print(f"Inserted {len(pycountry.currencies)} currencies")  # Inserted 170 currencies


def create_us_states_tables(conn):
    conn.executescript('''
    CREATE TABLE us_states (
        id INTEGER PRIMARY KEY, 
        abbr TEXT, 
        name TEXT,
        fips TEXT,
        is_territory BOOLEAN,
        is_obsolete BOOLEAN,
        is_contiguous BOOLEAN,
        is_continental BOOLEAN,
        statehood_year INTEGER,
        capital TEXT,
        capital_tz TEXT,
        ap_abbr TEXT,
        name_metaphone TEXT
    );
    CREATE TABLE us_states_time_zones (
        id INTEGER PRIMARY KEY,
        abbr TEXT,
        time_zone TEXT
    );
    ''')
    print("US states tables are ready")


def insert_us_states_tables(conn, sql=None):
    cur = conn.cursor()
    if not sql:
        sql = '''INSERT INTO us_states(
        abbr, 
        name,
        fips,
        is_territory,
        is_obsolete,
        is_contiguous,
        is_continental,
        statehood_year,
        capital,
        capital_tz,
        ap_abbr,
        name_metaphone
        ) VALUES(
        :abbr, 
        :name,
        :fips,
        :is_territory,
        :is_obsolete,
        :is_contiguous,
        :is_continental,
        :statehood_year,
        :capital,
        :capital_tz,
        :ap_abbr,
        :name_metaphone)'''
    for state in us.states.STATES:
        cur.execute(sql, state.__dict__)

        for time_zone in state.time_zones:
            cur.execute('INSERT INTO us_states_time_zones(abbr, time_zone) VALUES (?, ?)', (state.abbr, time_zone))

    print(f"Inserted {len(us.states.STATES)} states info.")


def create_tz_tables(conn):
    conn.executescript('''
    CREATE TABLE tz (
        id INTEGER PRIMARY KEY, 
        zone TEXT,
        format TEXT,
        is_common BOOLEAN
    );
    CREATE TABLE tz_countries (
        id INTEGER PRIMARY KEY,
        country TEXT,
        time_zone TEXT
    );
    ''')
    print("US tz tables are ready")


def insert_tz_tables(conn, tz_sql=None, tz_countries_sql=None):
    cur = conn.cursor()
    if not tz_sql:
        tz_sql = 'INSERT INTO tz (zone, format, is_common) VALUES (:zone, :format, :is_common)'
    if not tz_countries_sql:
        tz_countries_sql = 'INSERT INTO tz_countries (country, time_zone) VALUES (:country, :time_zone)'

    fmt = '%Z%z'
    for tz_name in pytz.all_timezones:
        tz = pytz.timezone(tz_name)
        tz_format = datetime.now(timezone.utc).astimezone(tz).strftime(fmt)
        is_common = tz_name in pytz.common_timezones
        row = {'zone': tz_name, 'format': tz_format, 'is_common': is_common}
        cur.execute(tz_sql, row)
    print(f"Inserted {len(pytz.all_timezones)} time zones")

    for country, tz_names in pytz.country_timezones.items():
        for tz_name in tz_names:
            row = {'country': country, 'time_zone': tz_name}
            cur.execute(tz_countries_sql, row)
    print(f"Inserted {len(pytz.country_timezones)} countries with time zones")

def main():
    with get_conn() as conn:
        # Data from Python locale module
        create_locales_table(conn)
        insert_locales(conn)

        # Data from pycountry package
        create_country_tables(conn)
        insert_country_tables(conn)

        # Data from us package
        create_us_states_tables(conn)
        insert_us_states_tables(conn)

        # Data from pytz for timezones list
        create_tz_tables(conn)
        insert_tz_tables(conn)


if __name__ == '__main__':
    main()
