import sqlite3
from flask import Flask

app = Flask(__name__)


@app.route('/')
def connect_db():
    db = sqlite3.connect("inventory.db")
    return db


@app.route('/getitems')
def get_items():
    db = sqlite3.connect("inventory.db")
    command = "SELECT product_name, num_items FROM items;"
    c = db.cursor()
    c.execute(command)
    data = c.fetchall()
    size = len(data)
    st = ""
    out = []
    return str(data)
    #for x in range(size):
     #   cur = []
     #   st = st+data[x][0]+"\n"
      #  stt = 
       # cur.append(st)
        #cur.append(stt)
        #out.append(cur)
    #return str(out)

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
