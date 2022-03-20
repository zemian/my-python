import sqlite3
import locale
import re
import pycountry
import us
import pytz
from datetime import datetime, timedelta, timezone


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


def create_locales_table():
    with get_conn() as conn:
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


def insert_locales():
    with get_conn() as conn:
        cur = conn.cursor()
        locales = get_locales()
        for record in locales:
            cur.execute('''
            INSERT INTO locales(lang, country, encoding, script)
            VALUES(:lang, :country, :encoding, :script)
            ''', record)
    print(f"Inserted {len(locales)} locales")


def create_country_tables():
    with get_conn() as conn:
        conn.executescript('''
        CREATE TABLE countries(code TEXT primary key, long_code TEXT, name TEXT, official_name TEXT, common_name TEXT, flag TEXT);
        CREATE TABLE languages(code TEXT primary key, long_code TEXT, name TEXT);
        CREATE TABLE currencies(code TEXT primary key, name TEXT);
        CREATE TABLE scripts(code TEXT primary key, name TEXT);
        ''')
    print("Country tables are ready")


def insert_country_tables():
    with get_conn() as conn:
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
            row = {
                'code': getattr(language, 'alpha_2', None),
                'long_code': getattr(language, 'alpha_3', None),
                'name': language.name
            }
            cur.execute('''INSERT INTO languages(code, long_code, name) VALUES(:code, :long_code, :name)''', row)
        print(f"Inserted {len(pycountry.languages)} languages")  # Inserted 7847 languages

        for script in pycountry.scripts:
            row = {'code': script.alpha_4, 'name': script.name}
            cur.execute('''INSERT INTO scripts(code, name) VALUES(:code, :name)''', row)
        print(f"Inserted {len(pycountry.scripts)} scripts")  # Inserted 182 scripts

        for currency in pycountry.currencies:
            row = {'code': currency.alpha_3, 'name': currency.name}
            cur.execute('''INSERT INTO scripts(code, name) VALUES(:code, :name)''', row)
        print(f"Inserted {len(pycountry.currencies)} currencies")  # Inserted 170 currencies


def create_us_states_tables():
    with get_conn() as conn:
        conn.executescript('''
        CREATE TABLE us_states (
            abbr TEXT primary key, 
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
            id INTEGER primary key,
            abbr TEXT,
            time_zone TEXT
        );
        ''')
    print("US states tables are ready")


def insert_us_states_tables():
    with get_conn() as conn:
        cur = conn.cursor()
        for state in us.states.STATES:
            cur.execute('''INSERT INTO us_states(
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
            :name_metaphone)''', state.__dict__)

            for time_zone in state.time_zones:
                cur.execute('INSERT INTO us_states_time_zones(abbr, time_zone) VALUES (?, ?)', (state.abbr, time_zone))

        print(f"Inserted {len(us.states.STATES)} states info.")


def create_tz_tables():
    with get_conn() as conn:
        conn.executescript('''
        CREATE TABLE tz (
            id INTEGER primary key, 
            zone TEXT,
            format TEXT,
            is_common BOOLEAN
        );
        CREATE TABLE tz_countries (
            id INTEGER primary key,
            country TEXT,
            time_zone TEXT
        );
        ''')
    print("US tz tables are ready")


def insert_tz_tables():
    with get_conn() as conn:
        cur = conn.cursor()
        fmt = '%Z%z'
        for tz_name in pytz.all_timezones:
            tz = pytz.timezone(tz_name)
            tz_format = datetime.now(timezone.utc).astimezone(tz).strftime(fmt)
            is_common = tz_name in pytz.common_timezones
            row = {'zone': tz_name, 'format': tz_format, 'is_common': is_common}
            cur.execute('INSERT INTO tz (zone, format, is_common) VALUES (:zone, :format, :is_common)', row)
        print(f"Inserted {len(pytz.all_timezones)} time zones")

        for country, tz_names in pytz.country_timezones.items():
            for tz_name in tz_names:
                cur.execute('INSERT INTO tz_countries (country, time_zone) VALUES (?, ?)', (country, tz_name))
        print(f"Inserted {len(pytz.country_timezones)} countries with time zones")

def main():
    # Data from Python locale module
    create_locales_table()
    insert_locales()

    # Data from pycountry package
    create_country_tables()
    insert_country_tables()

    # Data from us package
    create_us_states_tables()
    insert_us_states_tables()

    # Data from pytz for timezones list
    create_tz_tables()
    insert_tz_tables()


main()
