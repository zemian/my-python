import sqlite3
from datetime import datetime

def datetime_type_demo():
    with sqlite3.connect(':memory:') as conn:
        cur = conn.cursor()
        cur.executescript('CREATE TABLE test (id INTEGER PRIMARY KEY, dt DATETIME)')
        cur.execute('INSERT INTO test(id, dt) VALUES(?, ?)', (1, datetime.utcnow()))
        dt = cur.execute('SELECT dt FROM test WHERE id = 1').fetchone()[0]
        print(['DB dt value', dt, type(dt)])
        print(['Current utc', datetime.utcnow().isoformat()])
        print(['Current localtime now', datetime.now().isoformat()])

def datatypes_demo():
    with sqlite3.connect(':memory:') as conn:
        script = '''
        CREATE TABLE test (
          id INTEGER PRIMARY KEY,
          name TEXT,
          amount DECIMAL(12, 2),
          measurement FLOAT,
          dt DATETIME);
          
        INSERT INTO test VALUES (1, 'test', 300000.99, 3.14, CURRENT_TIMESTAMP);
        INSERT INTO test VALUES (2, 'test', 300000.00, 3.00, CURRENT_TIMESTAMP);
        '''
        # the "amount" type changes if it's .00 is used!
        cur = conn.cursor()
        cur.executescript(script)
        row = cur.execute('SELECT * FROM test WHERE id = 2').fetchone()
        for field in row:
            print(['Field', field, type(field)])


datatypes_demo()
