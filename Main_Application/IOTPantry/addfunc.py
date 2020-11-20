from datetime import date


# Contains Functions for the main application to reference

# Retrieves the next id to use for an entry
def get_new_id(table, db):
    c = db.cursor()
    c.execute("SELECT MAX(item_id)+1 FROM "+table+";")
    data = c.fetchall()
    print("\n NEW ID >> "+str(data[0][0])+"\n")
    return data[0][0]


#pulls an entry from the reference database based on the barcode
def get_info(pull, table, field, code, db):
    print("\nDATABASE >> ")
    print(db)
    print("\n")
    command = '\nSELECT '+pull+' FROM '+table+' WHERE '+str(field)+' ="'+str(code)+'";\n'
    print(command)
    c = db.cursor()
    c.execute(command)
    data = c.fetchall()
    print("\n DATA >>>  ")
    print(data)
    print("\n")
    return data


# checks the geiven inventory and table based on the barcode
def check_inv(table, code, db):
    c = db.cursor()
    command = 'SELECT EXISTS(SELECT * FROM '+table+' WHERE barcode_num="'+code+'");'
    print(command)
    c.execute(command)
    data = c.fetchall()
    return data


# gets the food group ID
def get_fg_id(fg, db):
    c = db.cursor()
    command = 'SELECT type_id FROM food_type WHERE type = "'+str(fg)+'";'
    print("\n COMMAND >> "+command)
    c.execute(command)
    data = c.fetchall()
    print("RAW FG >> "+str(data))
    print("\n FG ID >> "+str(data[0][0])+"\n")
    return data[0][0]



# Add an item to the INVENTORY
def add_inv(db, itemID, fgID, name, code, UID, expDate, quan):
    c = db.cursor()
    command = 'INSERT INTO items VALUES('+str(itemID)+', '+str(fgID)+', "'+name+'", '+str(code)+',"'+str(UID)+'", "'+str(date.today())+'", "'+str(expDate)+'", '+str(quan)+');'
    #(item_id, type_id, product_name, barcode_num, UID, input_date, expiration_date, num_items)
    print("\n"+command+"\n")
    c.execute(command)
    db.commit()


# Pull the UID value from
def pull_UID(db, code):
    c = db.cursor()
    command = 'SELECT RFIDcode FROM items WHERE barcode = "'+code+'"; '
    c.execute(command)
    data = c.fetchall()
    print("\n UID >> "+str(data[0][0])+"\n")
    return data[0][0]


# increases the count of an item
def inc_count(db, code, incNum):
    # get current Quantity
    command = 'SELECT num_items FROM items WHERE barcode_num = "'+code+'";'
    c = db.cursor()
    c.execute(command)
    curNum = c.fetchall()
    print("\n CURR NUM >> "+str(curNum[0][0]))
    newNum = curNum[0][0] + int(incNum)

    command = 'UPDATE items SET num_items = '+str(newNum)+' WHERE barcode_num = "'+code+'";'
    c.execute(command)
    db.commit()
