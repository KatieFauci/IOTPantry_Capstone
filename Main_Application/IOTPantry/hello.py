import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    db = sqlite3.connect("inventory.db")
    return db
    
@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')