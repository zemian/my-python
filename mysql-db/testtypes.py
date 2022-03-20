import mysql.connector

# CREATE DATABASE testdb CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
with mysql.connector.connect(database='testdb', user='zemian', password='test123') as conn:
    with conn.cursor() as cur:
        # Get VARCHAR type data
        cur.execute('SELECT name FROM testtypes WHERE id = %s', (1,))
        col = cur.fetchone()[0]
        print(['Query VARCHAR id=1', col, type(col)])

        # Get NULL result
        cur.execute('SELECT name FROM testtypes WHERE id = %s', (3,))
        col = cur.fetchone()[0]
        print(['Query VARCHAR id=3', col, type(col)])

        # Check to see if result exists
        cur.execute('SELECT name FROM testtypes WHERE id = %s', (-1,))
        row = cur.fetchone()
        if row:
            col = row[0]
            print(['Query VARCHAR id=-1', col, type(col)])

        # Get CHAR type data
        cur.execute('SELECT code FROM testtypes WHERE name = %s', ('char1',))
        col = cur.fetchone()[0]
        print(['Query CHAR char1', col, type(col)])

        # Get CHAR with NULL value
        cur.execute('SELECT code FROM testtypes WHERE name = %s', ('char3',))
        col = cur.fetchone()[0]
        print(['Query CHAR char3', col, type(col)])
