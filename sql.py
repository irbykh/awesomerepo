import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
env_token = "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"
# Database connection
db = sqlite3.connect(':memory:', check_same_thread=False)
cursor = db.cursor()
cursor.execute('''CREATE TABLE cars (id INTEGER PRIMARY KEY, make TEXT, model TEXT, year INTEGER)''')
cursor.execute("INSERT INTO cars (make, model, year) VALUES ('Toyota', 'Camry', 2020)")
db.commit()

@app.route('/')
def search_cars():
    make = request.args.get('make')

    if make:
        query = "SELECT * FROM cars WHERE make LIKE ?"
        cursor.execute(query, (f'%{make}%',))
        results = cursor.fetchall()
        return jsonify(results)
    else:
        return 'No car make provided.', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
