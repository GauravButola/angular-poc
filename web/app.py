import psycopg2
import json
from flask import Flask, redirect

app = Flask(__name__)

conn = psycopg2.connect("dbname=aggio user=gauravbutola")
cur = conn.cursor()


@app.route('/')
def home():
    return redirect('/transactions', code=302)


@app.route('/transactions')
def get_transactions():
    cur.execute('SELECT quantity, item FROM transactions;')
    return json.dumps(
        cur.fetchall()
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
