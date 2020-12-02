import sqlite3
from flask import Flask
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)


@app.route('/')
def connect_db():
    return "THIS IS OUR DATABASE \n BUT NO OTHER PAGE WILL WORK \n I WANT TO DIE \n END IT PLEASE"


@app.route('/Recipies')
def get_recipies():
    db = sqlite3.connect("inventory.db")
    command = "SELECT * FROM recipe;"
    c = db.cursor()
    c.execute(command)
    data = c.fetchall()
    size = len(data)
    return str(data)
    db.close()

@app.route('/inventory')
def inventory():
    config = {
        'user': 'root',
        'password': 'password',
        'host': 'localhost',
        'database': 'inventory',
        'raise_on_warnings': True
    }
    db = mysql.connector.connect(**config)
    c = db.cursor()
    command = "SELECT * FROM items"
    c.execute(command)
    data = c.fetchall()
    length = len(data)
    style = "</tbody></table><style>table,td {border: 1px solid #333;padding:5px;}thead,tfoot {background-color: #333;color: #fff;}</style>"
    table = "<table><thead><tr><th colspan="+str(2)+">Inventory</th></tr><tr><td>Product Name</td><td>Quantity</td></tr></thead><tbody>"
    for x in range(length):
        x+=1
        pn = data[x][2]
        q = data[x][7]
        table = table + "<tr><td>"+str(pn)+"</td><td>"+str(q)+"</td></tr>"
    table = table+style
    return table


@app.route('/sl')
def sl():
        config = {
            'user': 'root',
            'password': 'password',
            'host': 'localhost',
            'database': 'inventory',
            'raise_on_warnings': True
        }
        db = mysql.connector.connect(**config)
        actions=[]
        c = db.cursor()
        command = "SELECT * FROM shopping_list"
        c.execute(command)
        data = c.fetchall()
        style = "</tbody></table><style>table,td {border: 1px solid #333;padding:5px;}thead,tfoot {background-color: #333;color: #fff;}</style>"
        table = "<table><thead><tr><th colspan="+str(2)+">Shopping List</th></tr><tr><td>Item</td><td>Notes</td></tr></thead><tbody>"
        length = len(data)
        for x in range(length-1):
            x+=1
            i = data[x][1]
            n = data[x][2]
            table = table + "<tr><td>"+str(i)+"</td><td>"+str(n)+"</td></tr>"
        table = table+style
        return table


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
