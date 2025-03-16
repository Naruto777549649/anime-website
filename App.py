from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    animes = conn.execute('SELECT * FROM anime').fetchall()
    conn.close()
    return render_template('index.html', animes=animes)

if __name__ == '__main__':
    app.run(debug=True)
