from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database connection parameters
conn_params = {
    'dbname': 'prakash',
    'user': 'postgres',
    'password': 'Prakash66@',
    'host': 'localhost',
    'port': '5432'
}


def get_db_connection():
    conn = psycopg2.connect(**conn_params)
    return conn


@app.route('/')
def index():
    return "Welcome to the API!"


@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prakash")
    records = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()

    # Convert the records to a list of dictionaries
    results = [dict(zip(column_names, record)) for record in records]

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
