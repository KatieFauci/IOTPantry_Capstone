import sys
import tkinter as tk
import Tcl
import sqlite3


def get_sl_data(db):
    command = 'SELECT product_name, notes FROM shopping_list;'
    c = db.cursor()
    c.execute(command)
    data = c.fetchall()
    return data

def add_sl_db(db, entry, ID, note):
    command = 'INSERT INTO shopping_list VALUES('+str(ID)+',"'+entry+'","'+note+'");'
    c = db.cursor()
    c.execute(command)
    db.commit()

def configure_slEntry(entry):
    entry.configure(activebackground="#f9f9f9")
    entry.configure(activeforeground="black")
    entry.configure(background="#d9d9d9")
    entry.configure(disabledforeground="#a3a3a3")
    entry.configure(foreground="#000000")
    entry.configure(highlightbackground="#d9d9d9")
    entry.configure(highlightcolor="black")
    entry.configure(justify='left')
    entry.configure(relief="flat")

def configure_slCheckbox(Checkbutton):
    Checkbutton.configure(activebackground="#ececec")
    Checkbutton.configure(activeforeground="#000000")
    Checkbutton.configure(background="#585670")
    Checkbutton.configure(disabledforeground="#a3a3a3")
    Checkbutton.configure(foreground="#000000")
    Checkbutton.configure(highlightbackground="#d9d9d9")
    Checkbutton.configure(highlightcolor="black")
    Checkbutton.configure(justify='left')
