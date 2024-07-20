import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql@123"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE podar1")

 
