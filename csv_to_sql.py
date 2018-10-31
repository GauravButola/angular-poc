import psycopg2
from psycopg2.extras import execute_values
import csv

conn = psycopg2.connect("dbname=aggio user=gauravbutola")
cur = conn.cursor()


def create_schema():
    cur.execute(
        "CREATE TABLE transactions (quantity integer, item varchar);"
    )
    with open('data.csv', 'rb') as csv_data:
        data = csv.DictReader(csv_data)
        values = [(r['transaction'], r['item']) for r in data]

    insert_sql = "INSERT INTO transactions (quantity, item) VALUES %s"
    execute_values(cur, insert_sql, values)
    conn.commit()
    conn.close()


create_schema()
