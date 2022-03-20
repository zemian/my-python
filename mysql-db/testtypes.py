import mysql.connector

# CREATE DATABASE testdb CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
with mysql.connector.connect(database='testdb', user='zemian', password='test123') as conn:
    with conn.cursor() as cur:
        is_create_table = False
        is_insert_data = False
        is_query_data = True

        if is_create_table:
            cur.execute('''CREATE TABLE testtypes (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(10),
                code CHAR(3),
                content TEXT,
                is_on BOOLEAN,
                measurement FLOAT,
                large_measurement DOUBLE,
                total_amount DECIMAL(16,4),
                my_date DATE,
                my_time TIME,
                my_datetime DATETIME,
                my_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                my_year YEAR,
                image BLOB
            )''')

        if is_insert_data:
            # Test VARCHAR type
            # Note exception will occur if data is too long for VARCHAR! Example: "(4, 'ABC456789XXYZ')"
            cur.executemany('INSERT INTO testtypes (id, name) VALUES (%s, %s)', (
                (1, 'ABC'),
                (2, 'A'),
                (3, None)
            ))

            # Test CHAR type
            # Note exception will occur if data is too long for CHAR! Example: "('char4', 'ABCD')"
            cur.executemany('INSERT INTO testtypes (name, code) VALUES (%s, %s)', (
                            ('char1', 'ABC'),
                            ('char2', 'A'),
                            ('char3', None)
                            ))

            # Commit changes to DB
            conn.commit()

        if is_query_data:
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
