import sqlite3
from flask import g

app = Flask(__name__)
DATABASE = '/path/to/database.db'

@app.route('/')
def connect_db():
    db = sqlite3.connect(DATABASE)
    return db


@app.route('/getitems')
def get_items():
    db = sqlite3.connect(DATABASE)
    command = "SELECT * FROM items;"
    c = db.cursor()
    c.execute(command)
    data = c.fetchall()
    return data

#@app.route('/')
#def connect_db():
 #   db = getattr(g, '_database', None)
  #  if db is None:
   #     db = g._database = sqlite3.connect(DATABASE)
    #return db

#@app.teardown_appcontext
#def close_connection(exception):
#    db = getattr(g, '_database', None)
#    if db is not None:
#        db.close()
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
