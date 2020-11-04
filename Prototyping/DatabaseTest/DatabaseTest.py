import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="inventory"
)
print("THIS DATABASE IS>>>\n")
print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM food_type")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    print("\n")
