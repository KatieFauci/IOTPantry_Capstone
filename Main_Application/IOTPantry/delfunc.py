

# decreases the count of an item
def inc_count(db, code, incNum):
    # get current Quantity
    command = 'SELECT num_items FROM items WHERE barcode_num = "'+code+'";'
    c = db.cursor()
    c.execute(command)
    curNum = c.fetchall()
    print("\n CURR NUM >> "+str(curNum[0][0]))
    newNum = curNum[0][0] - int(incNum)

    command = 'UPDATE items SET num_items = '+str(newNum)+' WHERE barcode_num = "'+code+'";'
    c.execute(command)
    db.commit()

def remove_entry(table, value, code, db):
    command = 'DELETE FROM '+table+' WHERE '+value+' = "'+code+'";'
    c = db.cursor()
    c.execute(command)
    db.commit()

    print("\n REMOVE ENTRY \n")

# check if an item is in the inventory bases on the RFID code
def check_rfid_exists(id):
    c = db.cursor()
    command = 'SELECT EXISTS(SELECT * FROM items WHERE UID="'+str(id)+'");'
    c.execute(command)
    data = c.fetchall()
    return data

def remove_by_rfid(id, db):
    c = db.cursor()
    command = "DELETE * WHERE UID="+str(id)
    c.execute(command)
    db.commit()
    print(" ENTRY REMOVED BY RFID ")

def inc_count_rfid(id, db, cur):
    newNum = cur-1
    c = db.cursor()
    command = 'UPDATE items SET num_items = '+str(newNum)+' WHERE UID = "'+str(id)+'";'
    c.execute(command)
    db.commit()
    print(" COUNT INCREMENTED BY RFID ")
