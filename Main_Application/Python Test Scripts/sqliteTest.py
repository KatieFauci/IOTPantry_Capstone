import sqlite3

invdb = sqlite3.connect('C:\sqlite\inventory.db')
#refdb = sqlite3.connect('C:\sqlite\Iref.db')


print("\n DATABASE >>> ")
print(invdb)
print("\n\n")
c = invdb.cursor()
#command = "SELECT * FROM food_type;"
#print(command)
c.execute("SELECT * FROM food_type;")
data = c.fetchall()
print(data)
#print("\n\n\n")
#command = "SELECT * FROM items;"

#print("SELECT * FROM items;")
#c = refdb.cursor()
#c.execute("SELECT * FROM items;")
#data = c.fetchall()
#print(data)
