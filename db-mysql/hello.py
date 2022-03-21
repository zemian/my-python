import mysql.connector

# CREATE DATABASE testdb CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
with mysql.connector.connect(database='testdb', user='zemian', password='test123') as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT version()')
        print(cur.fetchone())
