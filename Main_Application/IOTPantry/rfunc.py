import sys
import tkinter as tk
import Tcl
import sqlite3


def get_r_data(db):
    command = 'SELECT recipe_name, recipe_time FROM recipe;'
    c = db.cursor()
    c.execute(command)
    data = c.fetchall()
    return data

def configure_rButton(button):
    button.configure(activebackground="#ececec")
    button.configure(activeforeground="#000000")
    button.configure(background="#d9d9d9")
    button.configure(cursor="fleur")
    button.configure(disabledforeground="#a3a3a3")
    button.configure(foreground="#000000")
    button.configure(highlightbackground="#d9d9d9")
    button.configure(highlightcolor="black")
    button.configure(pady="0")
    button.configure(relief="flat")

def configure_timeLabel(label):
        label.configure(background="#d9d9d9")
        label.configure(disabledforeground="#a3a3a3")
        label.configure(foreground="#000000")
