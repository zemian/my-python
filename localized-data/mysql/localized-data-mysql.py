import sys, os
import mysql.connector

def get_conn():
    return mysql.connector.connect(
        user='zemian', password='test123',
        host='127.0.0.1', database='localized_data')

# Import and reuse sqlite3 version of the code
sys.path.insert(1, os.path.join(sys.path[0], '..'))
localizeddata = __import__('localized-data')

with get_conn() as conn:

    localizeddata.insert_locales(conn, sql='''
        INSERT INTO locales(lang, country, encoding, script)
        VALUES(%(lang)s, %(country)s, %(encoding)s, %(script)s)
        ''')
    conn.commit()

    localizeddata.insert_country_tables(conn,
                                        countries_sql='''
                                        INSERT INTO c_countries(code, long_code, name, official_name, common_name, flag)
                                        VALUES(%(code)s, %(long_code)s, %(name)s, %(official_name)s, %(common_name)s, %(flag)s)
                                        ''',
                                        languages_sql='INSERT INTO c_languages(code, long_code, name) VALUES(%(code)s, %(long_code)s, %(name)s)',
                                        scripts_sql='INSERT INTO c_scripts(code, name) VALUES(%(code)s, %(name)s)',
                                        currencies_sql='INSERT INTO c_currencies(code, name) VALUES(%(code)s, %(name)s)')
    conn.commit()

    localizeddata.insert_us_states_tables(conn, states_sql='''INSERT INTO us_states(
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
                                            %(abbr)s,
                                            %(name)s,
                                            %(fips)s,
                                            %(is_territory)s,
                                            %(is_obsolete)s,
                                            %(is_contiguous)s,
                                            %(is_continental)s,
                                            %(statehood_year)s,
                                            %(capital)s,
                                            %(capital_tz)s,
                                            %(ap_abbr)s,
                                            %(name_metaphone)s)''',
                                          time_zones_sql = 'INSERT INTO us_states_time_zones(abbr, time_zone) VALUES (%(abbr)s, %(time_zone)s)')
    conn.commit()

    localizeddata.insert_tz_tables(conn, 
                                   tz_sql = 'INSERT INTO tz (zone, format, is_common) VALUES (%(zone)s, %(format)s, %(is_common)s)',
                                   tz_countries_sql = 'INSERT INTO tz_countries (country, time_zone) VALUES (%(country)s, %(time_zone)s)')
    conn.commit()
