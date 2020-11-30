import sqlite3
import click
from flask import current_app, g
# from flask.cli import with_appcontext

app = g(__name__)
DATABASE = 'inventory.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config[DATABASE],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def init_app(app):
    app.teardown_appcontext(close_db)

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close() 

if __name__ == '__main__':
    app.run(debug=True)