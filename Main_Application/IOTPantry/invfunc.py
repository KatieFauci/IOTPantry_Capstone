import sys
import tkinter as tk
import Tcl


def get_inv(db):
    c = db.cursor()
    c.execute("SELECT product_name FROM items;")
    names = c.fetchall()
    #print("\nNAMES >> ")
    #print(names)
    c.execute("SELECT num_items fROM items;")
    quantity = c.fetchall()
    c.execute("SELECT type_id FROM items;")
    fg = c.fetchall()
    c.execute("SELECT input_date FROM items;")
    inputDate = c.fetchall()
    c.execute("SELECT expiration_date FROM items;")
    expDate = c.fetchall()
    c.execute("SELECT barcode_num FROM items;")
    code = c.fetchall()

    # build data array
    return build_inv_array(names, quantity, fg, inputDate, expDate, code, db)

def configure_label(label):
    label.configure(activebackground="#f9f9f9")
    label.configure(activeforeground="black")
    label.configure(background="#d9d9d9")
    label.configure(disabledforeground="#a3a3a3")
    label.configure(foreground="#000000")
    label.configure(highlightbackground="#d9d9d9")
    label.configure(highlightcolor="black")

def configure_nameButton(button):
    button.configure(activebackground="#ececec")
    button.configure(activeforeground="#000000")
    button.configure(background="#d3d3d3")
    button.configure(disabledforeground="#a3a3a3")
    button.configure(foreground="#000000")
    button.configure(highlightbackground="#d9d9d9")
    button.configure(highlightcolor="black")
    button.configure(pady="0")
    button.configure(relief="flat")

def get_fg_name(num, db):
    c = db.cursor()
    c.execute('SELECT type FROM food_type WHERE type_id = "'+str(num)+'";')
    fg = c.fetchall()
    return fg[0][0]

def get_inv_search(db, key):
    c = db.cursor()
    print("KEY >>>> "+key)
    print('SELECT product_name FROM items WHERE product_name LIKE "%'+key+'%";')
    c.execute('SELECT product_name FROM items WHERE product_name LIKE "%'+key+'%";')
    names = c.fetchall()
    c.execute('SELECT num_items FROM items WHERE product_name LIKE "%'+key+'%";')
    quantity = c.fetchall()
    c.execute('SELECT type_id FROM items WHERE product_name LIKE "%'+key+'%";')
    fg = c.fetchall()
    c.execute('SELECT input_date FROM items WHERE product_name LIKE "%'+key+'%";')
    inputDate = c.fetchall()
    c.execute('SELECT expiration_date FROM items WHERE product_name LIKE "%'+key+'%";')
    expDate = c.fetchall()
    c.execute('SELECT barcode_num FROM items WHERE product_name LIKE "%'+key+'%";')
    code = c.fetchall()
    # build data array
    return build_inv_array(names, quantity, fg, inputDate, expDate, code, db)

def build_inv_array(names, quantity, fg, inputDate, expDate, code, db):
    arrLength = len(names)
    #print(" \n ARRAY LENGTH >> "+str(arrLength))
    i = 0
    data_list = []
    for i in range(0, arrLength):
        # build row
        new = []
        #print("\n I >> "+str(i))
        new.append(names[i][0])
        new.append(quantity[i][0])
        new.append(get_fg_name(fg[i][0], db))
        new.append(inputDate[i][0])
        new.append(expDate[i][0])
        new.append(code[i][0])
        #print(new)
        # append data_list
        data_list.append(new)
        #print(data_list)

    return data_list
