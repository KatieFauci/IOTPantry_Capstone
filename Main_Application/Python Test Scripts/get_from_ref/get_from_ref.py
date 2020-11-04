import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="ref_database"
)
print("THIS DATABASE IS>>>\n")
print(mydb)
print("\n\n")

# Get a barcode
code = input("Scan A Barcode: ")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM items WHERE barcode = " + code)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    print("\n")

