import psycopg2
from psycopg2.extras import DictCursor
from flask_cors import CORS
from flask import Flask, redirect, jsonify

app = Flask(__name__)

# XXX: Bad for production
CORS(app)

conn = psycopg2.connect("dbname=aggio user=gauravbutola")
cur = conn.cursor(cursor_factory=DictCursor)


@app.route('/')
def home():
    return redirect('/transactions', code=302)


@app.route('/transactions')
def get_transactions():
    cur.execute('SELECT quantity, item FROM transactions;')
    data = [dict(row) for row in cur]
    items = set([i['item'] for i in data])

    result = {}
    for item in items:
        result[item] = sum(
            [i['quantity'] for i in data if i['item'] == item]
        )

    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
