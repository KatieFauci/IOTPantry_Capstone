from flask import Flask
from flask import render_template
from frlask_mysqld import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'Inventory_Database'

mysql = MySQL(app)

@app.route('/')
def Home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM food_type")
    fetchdata = cur.fetchall()
    cur.close()
    return redner_template('home.html', data = fetchdata)
