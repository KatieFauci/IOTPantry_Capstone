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

def remove_entry():
    print("\n REMOVE ENTRY \n")
