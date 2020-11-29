import sqlite3
from flask import Flask

DATABASE = 'inventory.db'
app = Flask(__name__)

@app.route('/')
def get_db():
    db = getattr(Flask, '_database', None)
    if db is None:
        db = Flask._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(Flask, '_database', None)
    if db is not None:
        db.close()
