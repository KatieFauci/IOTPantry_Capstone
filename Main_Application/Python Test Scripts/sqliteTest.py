import sqlite3

invdb = sqlite3.connect('C:\sqlite\inventory.db')
print("\n DATABASE >>> ")
print(invdb)
print("\n\n")
c = invdb.cursor()
c.execute("SELECT * FROM food_type;")
data = c.fetchall()
print(data)
